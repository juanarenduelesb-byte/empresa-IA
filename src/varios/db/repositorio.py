"""Acceso a datos con el cliente de la identidad. Defensa doble: filtro explícito aquí y RLS en PostgreSQL."""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import UTC, datetime

from sqlalchemy import or_, select, text
from sqlalchemy.orm import Session

from varios.procesos.estados import cargar
from varios.procesos.motor import RIESGOS, AprobacionInvalida, Identidad, TransicionInvalida

from .modelos import Aprobacion, EventoAuditoria, Solicitud, Tarea

MAQUINA = cargar("encargo")
# Estados a los que solo se llega por su propia operación, no por un cambio de estado libre.
SOLO_POR_OPERACION = {"PENDIENTE_APROBACION": "pedir_aprobacion", "ENTREGADO": "decidir_aprobacion"}
ESTADOS_CON_TAREAS = ("PLANIFICADO", "EN_EJECUCION", "RETRABAJO")


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

    def _cambiar(self, sol: Solicitud, a: str, motivo: str, clave: str | None = None, **datos: object) -> None:
        if not MAQUINA.permitida(sol.estado, a):
            raise TransicionInvalida(f"{sol.estado} → {a} no está permitida")
        antes = sol.estado
        sol.estado = a
        if a == "RETRABAJO":
            sol.version += 1
        self.sesion.flush()
        self.registrar("mover", f"solicitud:{sol.id}", antes, a, motivo, clave, solicitud=str(sol.id), **datos)

    def mover_solicitud(self, solicitud_id: uuid.UUID, a: str, motivo: str, clave: str | None = None) -> Solicitud:
        """Cambio de estado según encargo.json. Toda transición lleva motivo y deja evento de auditoría."""
        sol = self.solicitud(solicitud_id, bloquear=True)
        if self._ya_aplicada(clave, sol.id):
            return sol
        if not motivo.strip():
            raise TransicionInvalida("Toda transición necesita motivo")
        if a in SOLO_POR_OPERACION:
            raise TransicionInvalida(f"A {a} solo se llega con {SOLO_POR_OPERACION[a]} (D-019: todo pasa por un socio)")
        self._cambiar(sol, a, motivo, clave)
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

    # --- aprobaciones (P10) --------------------------------------------------------------
    def pedir_aprobacion(self, solicitud_id: uuid.UUID, objeto: str, motivo: str) -> Aprobacion:
        """Pide la aprobación de la versión actual y pasa el encargo de EN_QA a PENDIENTE_APROBACION."""
        sol = self.solicitud(solicitud_id, bloquear=True)
        ap = Aprobacion(cliente_id=self.cliente_id, solicitud_id=sol.id, objeto=objeto, version=sol.version,
                        solicitada_por=self.quien.usuario)
        self.sesion.add(ap)
        self.sesion.flush()
        self._cambiar(sol, "PENDIENTE_APROBACION", motivo or "Pide aprobación", aprobacion=str(ap.id))
        self.registrar("aprobacion_pedida", f"aprobacion:{ap.id}", None, "pendiente", motivo,
                       solicitud=str(sol.id), version=ap.version)
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

    def decidir_aprobacion(self, aprobacion_id: uuid.UUID, aprobada: bool, motivo: str) -> Aprobacion:
        """Aprobar o rechazar. Reglas de P10 y de motor.aprobar, en código y no en el modelo."""
        ap = self.aprobacion(aprobacion_id)
        sol = self.solicitud(ap.solicitud_id, bloquear=True)
        self.sesion.refresh(ap, with_for_update=True)  # nadie más la decide a la vez
        if ap.decision != "pendiente":
            raise AprobacionInvalida("Esta aprobación ya está decidida")
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
        self._cambiar(sol, "ENTREGADO" if aprobada else "RETRABAJO", motivo, aprobacion=str(ap.id))
        return ap

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
                  clave: str | None = None, **datos: object) -> EventoAuditoria:
        ev = EventoAuditoria(cliente_id=self.cliente_id, actor=self.quien.usuario, accion=accion, objeto=objeto,
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
