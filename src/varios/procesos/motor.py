"""Motor mínimo del encargo.

Reglas que aplica en código (no en el modelo de IA):
- Solo transiciones permitidas por la definición.
- El tenant viene de la identidad autenticada, no de los datos de la petición.
- ENTREGADO desde EN_QA solo con riesgo bajo y QA conforme.
- Aprobar exige una persona distinta del autor, con rol de aprobación, y la misma versión.
- Cada transición deja un evento de auditoría inmutable.
- Las acciones repetidas con la misma clave de idempotencia no se aplican dos veces.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from itertools import count

from .estados import MaquinaEstados, cargar

RIESGOS = ("bajo", "medio", "alto", "critico")


class TransicionInvalida(Exception):
    pass


class AprobacionInvalida(Exception):
    pass


@dataclass(frozen=True)
class Identidad:
    usuario: str
    tenant: str
    roles: frozenset[str] = frozenset()
    persona: bool = True  # False para agentes y procesos


@dataclass(frozen=True)
class Evento:
    id: int
    momento: str
    tenant: str
    actor: str
    accion: str
    objeto: str
    antes: str | None
    despues: str | None
    motivo: str
    version_definicion: str
    clave_idempotencia: str | None = None


@dataclass
class Encargo:
    id: str
    tenant: str
    titulo: str
    autor: str
    riesgo: str
    estado: str
    version_entregable: int = 1
    qa_conforme: bool = False
    historial: list[Evento] = field(default_factory=list)


class Motor:
    def __init__(self, maquina: MaquinaEstados | None = None) -> None:
        self.maquina = maquina or cargar()
        self._encargos: dict[str, Encargo] = {}
        # La clave vale para un encargo de un cliente: la misma clave en otro encargo u otro cliente se aplica.
        self._claves: dict[tuple[str, str, str], Evento] = {}
        self._ids = count(1)
        self.auditoria: list[Evento] = []

    # --- alta -------------------------------------------------------------
    def alta(self, quien: Identidad, titulo: str, riesgo: str = "bajo", **_ignorado: object) -> Encargo:
        """Crea un encargo. Cualquier 'tenant' en los datos se ignora a propósito."""
        if riesgo not in RIESGOS:
            raise ValueError(f"Riesgo desconocido: {riesgo}")
        enc = Encargo(
            id=f"E-{len(self._encargos) + 1:04d}",
            tenant=quien.tenant,
            titulo=titulo,
            autor=quien.usuario,
            riesgo=riesgo,
            estado=self.maquina.inicial,
        )
        self._encargos[enc.id] = enc
        self._registrar(enc, quien, "alta", None, enc.estado, "Encargo recibido")
        return enc

    def obtener(self, quien: Identidad, encargo_id: str) -> Encargo:
        enc = self._encargos.get(encargo_id)
        if enc is None or enc.tenant != quien.tenant:
            # Mismo error si no existe o es de otro cliente: no revelar existencia.
            raise KeyError(encargo_id)
        return enc

    # --- transiciones -----------------------------------------------------
    def mover(
        self,
        quien: Identidad,
        encargo_id: str,
        a: str,
        motivo: str,
        clave_idempotencia: str | None = None,
    ) -> Encargo:
        enc = self.obtener(quien, encargo_id)
        clave = (quien.tenant, enc.id, clave_idempotencia) if clave_idempotencia else None
        if clave and clave in self._claves:
            return enc
        if not motivo.strip():
            raise TransicionInvalida("Toda transición necesita motivo")
        if not self.maquina.permitida(enc.estado, a):
            raise TransicionInvalida(f"{enc.estado} → {a} no está permitida")
        if enc.estado == "EN_QA" and a == "ENTREGADO" and not (enc.riesgo == "bajo" and enc.qa_conforme):
            raise TransicionInvalida("Entrega directa desde QA solo con riesgo bajo y QA conforme")
        if enc.estado == "PENDIENTE_APROBACION" and a == "ENTREGADO":
            raise AprobacionInvalida("Usa aprobar(): la entrega tras aprobación exige una persona")
        if enc.estado == "PENDIENTE_APROBACION" and a == "ESCALADO":
            raise TransicionInvalida("PENDIENTE_APROBACION → ESCALADO solo ocurre al caducar la aprobación (N3c)")
        if enc.estado == "CERRADO" and not (quien.persona and "aprobador" in quien.roles):
            # Guía v1.4 §4: CERRADO → REABIERTO «solo con motivo, autorización y nueva versión» (repaso del 28/11).
            raise AprobacionInvalida("Reabrir un encargo cerrado necesita una persona con rol de aprobación")
        if enc.estado == "ESCALADO" and not quien.persona:
            # encargo.json: de ESCALADO sale «una persona identificada» que decide cómo seguir (repaso del 28/11).
            raise AprobacionInvalida("De ESCALADO solo sale una persona que decide cómo seguir")
        if enc.estado == "PENDIENTE_APROBACION":
            # Guía v1.4 §4: también devolver a retrabajo o rechazar exige un aprobador autorizado.
            self._comprobar_aprobador(quien, enc)
        if a == "EN_QA":
            enc.qa_conforme = False
        if a in ("RETRABAJO", "REABIERTO"):
            # Guía v1.4 §4: reabrir es «con nueva versión»; una aprobación vieja nunca vale para lo que se rehaga.
            enc.version_entregable += 1
        antes = enc.estado
        enc.estado = a
        ev = self._registrar(enc, quien, "mover", antes, a, motivo, clave_idempotencia)
        if clave:
            self._claves[clave] = ev
        return enc

    def resultado_qa(self, quien: Identidad, encargo_id: str, conforme: bool, motivo: str) -> Encargo:
        enc = self.obtener(quien, encargo_id)
        if enc.estado != "EN_QA":
            raise TransicionInvalida("El resultado de QA solo se registra en EN_QA")
        enc.qa_conforme = conforme
        self._registrar(enc, quien, "qa", "EN_QA", "EN_QA", ("conforme: " if conforme else "no conforme: ") + motivo)
        return enc

    def aprobar(self, quien: Identidad, encargo_id: str, version: int, motivo: str) -> Encargo:
        enc = self.obtener(quien, encargo_id)
        if enc.estado != "PENDIENTE_APROBACION":
            raise AprobacionInvalida("No está pendiente de aprobación")
        self._comprobar_aprobador(quien, enc)
        if version != enc.version_entregable:
            raise AprobacionInvalida("La aprobación es de otra versión del entregable")
        enc.estado = "ENTREGADO"
        self._registrar(enc, quien, "aprobar", "PENDIENTE_APROBACION", "ENTREGADO", motivo)
        return enc

    @staticmethod
    def _comprobar_aprobador(quien: Identidad, enc: Encargo) -> None:
        if not quien.persona:
            raise AprobacionInvalida("Solo una persona puede aprobar")
        if quien.usuario == enc.autor:
            raise AprobacionInvalida("Nadie aprueba su propio trabajo")
        if "aprobador" not in quien.roles:
            raise AprobacionInvalida("Falta el rol de aprobación")

    # --- auditoría --------------------------------------------------------
    def _registrar(self, enc, quien, accion, antes, despues, motivo, clave=None) -> Evento:
        ev = Evento(
            id=next(self._ids),
            momento=datetime.now(UTC).isoformat(),
            tenant=enc.tenant,
            actor=quien.usuario,
            accion=accion,
            objeto=enc.id,
            antes=antes,
            despues=despues,
            motivo=motivo,
            version_definicion=self.maquina.version,
            clave_idempotencia=clave,
        )
        self.auditoria.append(ev)
        enc.historial.append(ev)
        return ev
