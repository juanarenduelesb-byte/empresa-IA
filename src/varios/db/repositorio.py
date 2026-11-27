"""Acceso a datos con el cliente de la identidad. Defensa doble: filtro explícito aquí y RLS en PostgreSQL."""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

from sqlalchemy import or_, select, text
from sqlalchemy.orm import Session

from varios.config import ajustes
from varios.procesos.estados import cargar, cargar_objeto
from varios.procesos.motor import RIESGOS, AprobacionInvalida, Identidad, TransicionInvalida

from .modelos import Aprobacion, EventoAuditoria, Solicitud, Tarea

MAQUINA = cargar("encargo")
MAQUINA_TAREA = cargar_objeto("tarea")
# Estados a los que solo se llega por su propia operación, no por un cambio de estado libre.
SOLO_POR_OPERACION = {"PENDIENTE_APROBACION": "pedir_aprobacion", "ENTREGADO": "decidir_aprobacion"}
ESTADOS_CON_TAREAS = ("PLANIFICADO", "EN_EJECUCION", "RETRABAJO")
# Estados en los que el encargo espera a una persona: son los únicos que se pueden posponer (N3c, como en la oficina).
ESTADOS_QUE_ESPERAN = ("PENDIENTE_APROBACION", "PENDIENTE_INFO", "ESCALADO", "BLOQUEADO")
# Quien firma lo que hace el sistema sin que nadie lo pida (la caducidad). Nunca es un usuario: no puede aprobar.
ACTOR_SISTEMA = "sistema:caducidad"


class NoEncontrado(LookupError):
    """Lo mismo si no existe que si es de otro cliente: no se revela la existencia (OWASP IDOR)."""


@dataclass
class Repositorio:
    sesion: Session
    quien: Identidad

    @property
    def cliente_id(self) -> uuid.UUID:
        return uuid.UUID(self.quien.tenant)

    def crear_solicitud(self, autor_id: uuid.UUID, titulo: str, descripcion: str = "", riesgo: str = "bajo",
                        **_ignorado: object) -> Solicitud:
        """Cualquier `cliente_id` que venga en los datos se ignora: manda la identidad."""
        if riesgo not in RIESGOS:
            raise ValueError(f"Riesgo desconocido: {riesgo}")
        sol = Solicitud(cliente_id=self.cliente_id, autor_id=autor_id, titulo=titulo, descripcion=descripcion,
                        riesgo=riesgo)
        self.sesion.add(sol)
        self.sesion.flush()
        self.registrar("alta", f"solicitud:{sol.id}", None, sol.estado, "Alta de la solicitud", solicitud=str(sol.id))
        return sol

    def solicitud(self, solicitud_id: uuid.UUID, bloquear: bool = False) -> Solicitud:
        """Con `bloquear`, la fila queda reservada hasta el final de la transacción (SELECT … FOR UPDATE):
        dos cambios a la vez sobre el mismo encargo se aplican uno detrás de otro, no a la vez."""
        q = select(Solicitud).where(Solicitud.id == solicitud_id, Solicitud.cliente_id == self.cliente_id)
        sol = self.sesion.scalar(q.with_for_update() if bloquear else q)
        if sol is None:
            raise NoEncontrado(str(solicitud_id))
        return sol

    def solicitudes(self) -> list[Solicitud]:
        consulta = select(Solicitud).where(Solicitud.cliente_id == self.cliente_id).order_by(Solicitud.creado_en)
        return list(self.sesion.scalars(consulta))

    # --- encargo: cambios de estado -------------------------------------------------
    def _ya_aplicada(self, clave: str | None, solicitud_id: uuid.UUID) -> bool:
        """La clave vale para un encargo: la misma clave en otro encargo no lo deja sin aplicar."""
        if not clave:
            return False
        q = select(EventoAuditoria.id).where(EventoAuditoria.cliente_id == self.cliente_id,
                                             EventoAuditoria.clave_idempotencia == clave,
                                             EventoAuditoria.datos["solicitud"].as_string() == str(solicitud_id))
        return self.sesion.scalar(q) is not None

    def _cambiar(self, sol: Solicitud, a: str, motivo: str, clave: str | None = None, actor: str | None = None,
                 **datos: object) -> None:
        if not MAQUINA.permitida(sol.estado, a):
            raise TransicionInvalida(f"{sol.estado} → {a} no está permitida")
        antes = sol.estado
        sol.estado = a
        if a == "RETRABAJO":
            sol.version += 1
        if sol.pospuesto_hasta is not None:
            # Posponer vale para el estado en que se pospuso; al cambiar de estado se pierde (regla de la oficina, N4).
            datos["pospuesto_retirado"] = sol.pospuesto_hasta.isoformat()
            sol.pospuesto_hasta = None
        self.sesion.flush()
        self.registrar("mover", f"solicitud:{sol.id}", antes, a, motivo, clave, actor=actor, solicitud=str(sol.id),
                       **datos)

    def mover_solicitud(self, solicitud_id: uuid.UUID, a: str, motivo: str, clave: str | None = None) -> Solicitud:
        """Cambio de estado según encargo.json. Toda transición lleva motivo y deja evento de auditoría."""
        sol = self.solicitud(solicitud_id, bloquear=True)
        if self._ya_aplicada(clave, sol.id):
            return sol
        if not motivo.strip():
            raise TransicionInvalida("Toda transición necesita motivo")
        if a in SOLO_POR_OPERACION:
            raise TransicionInvalida(f"A {a} solo se llega con {SOLO_POR_OPERACION[a]} (D-019: todo pasa por un socio)")
        if sol.estado == "PENDIENTE_APROBACION":
            # Guía v1.4 §4: de aquí solo se sale con un aprobador autorizado y la versión exacta, es decir, decidiendo
            # la aprobación. Un cambio libre la dejaría «pendiente» para siempre y lo podría hacer cualquiera.
            raise TransicionInvalida("Un encargo pendiente de aprobación solo sale con decidir_aprobacion")
        self._cambiar(sol, a, motivo, clave)
        return sol

    def posponer(self, solicitud_id: uuid.UUID, hasta: datetime, motivo: str = "") -> Solicitud:
        """Aparta un encargo que espera a una persona hasta `hasta` (N3c). No decide nada: la caducidad sigue contando
        y el encargo vuelve igual que estaba. Solo una persona pospone, y como mucho `posponer_max_dias`."""
        if not self.quien.persona:
            raise AprobacionInvalida("Solo una persona puede posponer")
        sol = self.solicitud(solicitud_id, bloquear=True)
        if sol.estado not in ESTADOS_QUE_ESPERAN:
            raise TransicionInvalida(f"Un encargo en {sol.estado} no espera a nadie: no se pospone")
        if hasta.tzinfo is None:
            raise TransicionInvalida("La hora de vuelta necesita zona horaria")
        ahora = datetime.now(UTC)
        if hasta <= ahora:
            raise TransicionInvalida("Se pospone hasta una hora futura")
        if hasta > ahora + timedelta(days=ajustes().posponer_max_dias):
            raise TransicionInvalida(f"Como mucho {ajustes().posponer_max_dias} días")
        antes = sol.pospuesto_hasta.isoformat() if sol.pospuesto_hasta else None
        sol.pospuesto_hasta = hasta
        self.sesion.flush()
        self.registrar("pospuesto", f"solicitud:{sol.id}", antes, hasta.isoformat(), motivo or "Pospuesto",
                       solicitud=str(sol.id), estado=sol.estado)
        return sol

    # --- tareas ------------------------------------------------------------------------
    def crear_tarea(self, solicitud_id: uuid.UUID, titulo: str, responsable: str, clave: str | None = None,
                    **_ignorado: object) -> tuple[Tarea, bool]:
        """Devuelve (tarea, creada). Con la misma clave de idempotencia devuelve la que ya existe."""
        sol = self.solicitud(solicitud_id)
        if clave:
            previa = self.sesion.scalar(select(Tarea).where(Tarea.cliente_id == self.cliente_id,
                                                            Tarea.clave_idempotencia == clave))
            if previa is not None:
                if previa.solicitud_id != sol.id:
                    raise TransicionInvalida("La clave de idempotencia ya se usó en otro encargo")
                return previa, False
        if sol.estado not in ESTADOS_CON_TAREAS:
            raise TransicionInvalida(f"Un encargo en {sol.estado} no admite tareas nuevas")
        t = Tarea(cliente_id=self.cliente_id, solicitud_id=sol.id, titulo=titulo, responsable=responsable,
                  clave_idempotencia=clave)
        self.sesion.add(t)
        self.sesion.flush()
        self.registrar("tarea_alta", f"tarea:{t.id}", None, t.estado, f"Tarea: {titulo}", clave, solicitud=str(sol.id))
        return t, True

    def tareas(self, solicitud_id: uuid.UUID) -> list[Tarea]:
        sol = self.solicitud(solicitud_id)
        q = select(Tarea).where(Tarea.cliente_id == self.cliente_id, Tarea.solicitud_id == sol.id)
        return list(self.sesion.scalars(q.order_by(Tarea.creado_en)))

    def tarea(self, tarea_id: uuid.UUID) -> Tarea:
        t = self.sesion.scalar(select(Tarea).where(Tarea.id == tarea_id, Tarea.cliente_id == self.cliente_id))
        if t is None:
            raise NoEncontrado(str(tarea_id))
        return t

    def mover_tarea(self, tarea_id: uuid.UUID, a: str, motivo: str, clave: str | None = None) -> Tarea:
        """Cambio de estado de una tarea según objetos.json (N3c). Cada cambio deja auditoría.

        De una tarea que pide aprobación (needs_approval) solo sale (a succeeded, running o cancelled) una persona con
        rol de aprobación que no sea quien la puso a esperar ni el autor del encargo (las mismas reglas que las
        aprobaciones, P10). Una tarea que alguna vez pidió aprobación solo acaba en succeeded aprobándola."""
        t = self.tarea(tarea_id)
        sol = self.solicitud(t.solicitud_id, bloquear=True)  # primero el encargo, como en el resto de operaciones
        self.sesion.refresh(t, with_for_update=True)
        if self._ya_aplicada(clave, sol.id):
            return t
        if not motivo.strip():
            raise TransicionInvalida("Toda transición necesita motivo")
        if sol.estado not in ESTADOS_CON_TAREAS:
            raise TransicionInvalida(f"Un encargo en {sol.estado} no admite cambios en sus tareas")
        if not MAQUINA_TAREA.permitida(t.estado, a):
            raise TransicionInvalida(f"Tarea: {t.estado} → {a} no está permitida")
        q = (select(EventoAuditoria.actor)
             .where(EventoAuditoria.cliente_id == self.cliente_id, EventoAuditoria.objeto == f"tarea:{t.id}",
                    EventoAuditoria.despues == "needs_approval")
             .order_by(EventoAuditoria.id.desc()).limit(1))
        pidio = self.sesion.scalar(q)  # quien la puso a esperar la última vez (None si nunca pidió aprobación)
        if t.estado == "needs_approval":
            # Toda salida de needs_approval (aprobar, devolver a running o cancelar) es de un aprobador, como las de
            # PENDIENTE_APROBACION (Guía v1.4 §4): si no, se volvía a running y de ahí a succeeded sin aprobar.
            if not self.quien.persona:
                raise AprobacionInvalida("Solo una persona puede decidir una tarea que pide aprobación")
            if "aprobador" not in self.quien.roles:
                raise AprobacionInvalida("Falta el rol de aprobación")
            if self.quien.usuario in (pidio, str(sol.autor_id)):
                # Igual que en decidir_aprobacion: ni quien la pidió ni el autor del encargo.
                raise AprobacionInvalida("Nadie decide lo que ha pedido él mismo")
        elif a == "succeeded" and pidio is not None:
            raise TransicionInvalida("Esta tarea pidió aprobación: solo se da por hecha aprobándola")
        antes = t.estado
        t.estado = a
        self.sesion.flush()
        self.registrar("tarea_mover", f"tarea:{t.id}", antes, a, motivo, clave, solicitud=str(sol.id))
        return t

    def tareas_del_cliente(self) -> list[Tarea]:
        q = select(Tarea).where(Tarea.cliente_id == self.cliente_id).order_by(Tarea.creado_en)
        return list(self.sesion.scalars(q))

    # --- aprobaciones (P10) --------------------------------------------------------------
    def pedir_aprobacion(self, solicitud_id: uuid.UUID, objeto: str, motivo: str) -> Aprobacion:
        """Pide la aprobación de la versión actual y pasa el encargo de EN_QA a PENDIENTE_APROBACION."""
        sol = self.solicitud(solicitud_id, bloquear=True)
        ap = Aprobacion(cliente_id=self.cliente_id, solicitud_id=sol.id, objeto=objeto, version=sol.version,
                        solicitada_por=self.quien.usuario,
                        caduca_en=datetime.now(UTC) + timedelta(hours=ajustes().aprobacion_caduca_h))
        self.sesion.add(ap)
        self.sesion.flush()
        self._cambiar(sol, "PENDIENTE_APROBACION", motivo or "Pide aprobación", aprobacion=str(ap.id))
        self.registrar("aprobacion_pedida", f"aprobacion:{ap.id}", None, "pendiente", motivo,
                       solicitud=str(sol.id), version=ap.version, caduca_en=ap.caduca_en.isoformat())
        return ap

    def aprobacion(self, aprobacion_id: uuid.UUID) -> Aprobacion:
        ap = self.sesion.scalar(select(Aprobacion).where(Aprobacion.id == aprobacion_id,
                                                         Aprobacion.cliente_id == self.cliente_id))
        if ap is None:
            raise NoEncontrado(str(aprobacion_id))
        return ap

    def aprobaciones(self, solicitud_id: uuid.UUID) -> list[Aprobacion]:
        sol = self.solicitud(solicitud_id)
        q = select(Aprobacion).where(Aprobacion.cliente_id == self.cliente_id, Aprobacion.solicitud_id == sol.id)
        return list(self.sesion.scalars(q.order_by(Aprobacion.creado_en)))

    def decidir_aprobacion(self, aprobacion_id: uuid.UUID, aprobada: bool, motivo: str,
                           si_rechaza: str = "RETRABAJO") -> Aprobacion:
        """Aprobar o rechazar. Reglas de P10 y de motor.aprobar, en código y no en el modelo.

        Al rechazar, el aprobador elige entre devolver (RETRABAJO, versión + 1) o rechazar del todo (RECHAZADO): son las
        dos salidas de PENDIENTE_APROBACION que da la Guía v1.4 §4 además de ENTREGADO.
        """
        if si_rechaza not in ("RETRABAJO", "RECHAZADO"):
            raise TransicionInvalida(f"Al rechazar se va a RETRABAJO o a RECHAZADO, no a {si_rechaza}")
        ap = self.aprobacion(aprobacion_id)
        sol = self.solicitud(ap.solicitud_id, bloquear=True)
        self.sesion.refresh(ap, with_for_update=True)  # nadie más la decide a la vez
        if ap.decision == "caducada":
            raise AprobacionInvalida("Esta aprobación caducó sin decisión: el encargo ha vuelto como pregunta")
        if ap.decision != "pendiente":
            raise AprobacionInvalida("Esta aprobación ya está decidida")
        if ap.caduca_en is not None and ap.caduca_en <= datetime.now(UTC):
            raise AprobacionInvalida("Esta aprobación ha caducado: ya no se puede decidir")
        if not self.quien.persona:
            raise AprobacionInvalida("Solo una persona puede aprobar")
        if self.quien.usuario in (ap.solicitada_por, str(sol.autor_id)):
            raise AprobacionInvalida("Nadie aprueba lo que ha pedido él mismo")
        if "aprobador" not in self.quien.roles:
            raise AprobacionInvalida("Falta el rol de aprobación")
        if sol.estado != "PENDIENTE_APROBACION" or ap.version != sol.version:
            raise AprobacionInvalida("La aprobación es de otra versión o el encargo ya no la espera")
        if not motivo.strip():
            raise AprobacionInvalida("La decisión necesita motivo")
        ap.decision = "aprobada" if aprobada else "rechazada"
        ap.aprobador_id = uuid.UUID(self.quien.usuario)
        ap.motivo = motivo
        ap.decidida_en = datetime.now(UTC)
        self.sesion.flush()
        self.registrar("aprobacion_decidida", f"aprobacion:{ap.id}", "pendiente", ap.decision, motivo,
                       solicitud=str(sol.id), version=ap.version)
        self._cambiar(sol, "ENTREGADO" if aprobada else si_rechaza, motivo, aprobacion=str(ap.id))
        return ap

    def caducar_vencidas(self, ahora: datetime | None = None) -> list[Aprobacion]:
        """Caduca las aprobaciones pendientes de este cliente cuyo plazo ha pasado (N3c; P10: nunca aprobación tácita).

        Caducidad perezosa, como la expiración pasiva de Redis (`REDIS-EXPIRE`): no hace falta un proceso aparte; se
        comprueba al empezar cada petición del cliente, dentro de su transacción y con su RLS, así que un cliente no
        caduca nunca lo de otro. La aprobación queda «caducada» sin aprobador y el encargo pasa a ESCALADO: vuelve como
        pregunta y no continúa. Bloquea en el mismo orden que `decidir_aprobacion` (encargo y después aprobación) para
        que una decisión y una caducidad a la vez no se crucen."""
        ahora = ahora or datetime.now(UTC)
        q = select(Aprobacion.id, Aprobacion.solicitud_id).where(
            Aprobacion.cliente_id == self.cliente_id, Aprobacion.decision == "pendiente",
            Aprobacion.caduca_en.is_not(None), Aprobacion.caduca_en <= ahora)
        caducadas = []
        for ap_id, sol_id in self.sesion.execute(q).all():
            sol = self.solicitud(sol_id, bloquear=True)
            ap = self.aprobacion(ap_id)
            self.sesion.refresh(ap, with_for_update=True)
            if ap.decision != "pendiente":  # la decidió alguien mientras esperábamos el bloqueo
                continue
            ap.decision = "caducada"
            ap.decidida_en = ahora
            ap.motivo = "Caducó sin decisión: no continúa y vuelve como pregunta"
            self.sesion.flush()
            self.registrar("aprobacion_caducada", f"aprobacion:{ap.id}", "pendiente", "caducada", ap.motivo,
                           actor=ACTOR_SISTEMA, solicitud=str(sol.id), version=ap.version,
                           caduca_en=ap.caduca_en.isoformat(), disparado_por=self.quien.usuario)
            if sol.estado == "PENDIENTE_APROBACION":
                self._cambiar(sol, "ESCALADO", "Aprobación caducada: una persona decide cómo seguir",
                              actor=ACTOR_SISTEMA, aprobacion=str(ap.id))
            caducadas.append(ap)
        return caducadas

    def ultimas_aprobaciones(self) -> dict[uuid.UUID, Aprobacion]:
        """La última aprobación de cada encargo del cliente (para la lista de la oficina)."""
        q = select(Aprobacion).where(Aprobacion.cliente_id == self.cliente_id).order_by(Aprobacion.creado_en)
        return {a.solicitud_id: a for a in self.sesion.scalars(q)}

    # --- auditoría ----------------------------------------------------------------------
    def eventos(self, solicitud_id: uuid.UUID) -> list[EventoAuditoria]:
        sol = self.solicitud(solicitud_id)
        q = select(EventoAuditoria).where(
            EventoAuditoria.cliente_id == self.cliente_id,
            or_(EventoAuditoria.objeto == f"solicitud:{sol.id}",
                EventoAuditoria.datos["solicitud"].as_string() == str(sol.id)),
        )
        return list(self.sesion.scalars(q.order_by(EventoAuditoria.id)))

    def registrar(self, accion: str, objeto: str, antes: str | None, despues: str | None, motivo: str,
                  clave: str | None = None, actor: str | None = None, **datos: object) -> EventoAuditoria:
        ev = EventoAuditoria(cliente_id=self.cliente_id, actor=actor or self.quien.usuario, accion=accion,
                             objeto=objeto,
                             antes=antes, despues=despues, motivo=motivo, clave_idempotencia=clave, datos=datos)
        self.sesion.add(ev)
        self.sesion.flush()
        return ev

    def buscar_conocimiento(self, consulta: str, limite: int = 10) -> list[dict]:
        """Búsqueda de texto con permisos (RLS) y cita obligatoria: fichas sin fuente no se devuelven."""
        filas = self.sesion.execute(
            text(
                """
                SELECT f.id, f.codigo, f.titulo, f.estado, f.cliente_id,
                       ts_rank(f.busqueda, q) AS relevancia,
                       json_agg(json_build_object('codigo', fu.codigo, 'titulo', fu.titulo, 'url', fu.url,
                                                  'cita', ff.cita) ORDER BY fu.codigo) AS fuentes
                FROM ficha_conocimiento f
                CROSS JOIN websearch_to_tsquery('spanish', :consulta) q
                JOIN ficha_fuente ff ON ff.ficha_id = f.id
                JOIN fuente fu ON fu.id = ff.fuente_id
                WHERE f.busqueda @@ q AND f.estado NOT IN ('deprecated', 'raw')
                  AND (f.cliente_id IS NULL OR f.cliente_id = :cliente)
                GROUP BY f.id, q
                ORDER BY relevancia DESC, f.codigo
                LIMIT :limite
                """
            ),
            {"consulta": consulta, "cliente": self.cliente_id, "limite": limite},
        ).mappings()
        return [dict(f) for f in filas]
