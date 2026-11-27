"""Modelo de datos del núcleo (plan S2) y del conocimiento (plan S7).

Reglas que el esquema hace cumplir, además del código:
- Toda fila operativa lleva `cliente_id` (el tenant). La aplicación lo toma de la identidad, nunca de la petición,
  y PostgreSQL lo vuelve a comprobar con RLS (migración 0002).
- Los estados son los de processes/definitions (encargo.json y objetos.json); una prueba comprueba que coinciden.
- La auditoría no se puede modificar ni borrar (disparador en la migración 0002).
- El conocimiento con `cliente_id` nulo es común (normas, sectores); el resto solo lo ve su cliente.
"""

from __future__ import annotations

import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    JSON,
    BigInteger,
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Identity,
    Index,
    Integer,
    MetaData,
    Numeric,
    String,
    Text,
    UniqueConstraint,
    Uuid,
    func,
    text,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

CONVENCION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

ESTADOS_SOLICITUD = (
    "RECIBIDO", "EN_CLASIFICACION", "PENDIENTE_INFO", "PLANIFICADO", "EN_EJECUCION", "EN_QA",
    "PENDIENTE_APROBACION", "ENTREGADO", "CERRADO", "BLOQUEADO", "ESCALADO", "RETRABAJO", "RECHAZADO",
    "CANCELADO", "REABIERTO",
)
ESTADOS_TAREA = ("queued", "running", "needs_approval", "succeeded", "blocked", "failed", "cancelled")
ESTADOS_FICHA = ("raw", "draft", "validated", "approved", "deprecated", "disputed")
RIESGOS = ("bajo", "medio", "alto", "critico")
CLASIFICACIONES = ("publico", "interno", "confidencial", "datos_personales", "datos_salud")
ESTADOS_DOCUMENTO = ("cuarentena", "aceptado", "rechazado")
DECISIONES = ("pendiente", "aprobada", "rechazada", "caducada")  # caducada: sin decidir en plazo (N3c)
RESULTADOS_MODELO = ("ok", "error", "rechazado")
RESULTADOS_HERRAMIENTA = ("ok", "error", "bloqueado", "pendiente")


def _en(columna: str, valores: tuple[str, ...]) -> str:
    return f"{columna} IN ({', '.join(repr(v) for v in valores)})"


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=CONVENCION)


def _id() -> Mapped[uuid.UUID]:
    return mapped_column(Uuid, primary_key=True, default=uuid.uuid4)


def _cliente(nullable: bool = False) -> Mapped[uuid.UUID]:
    return mapped_column(Uuid, ForeignKey("cliente.id", ondelete="RESTRICT"), nullable=nullable, index=True)


def _creado() -> Mapped[datetime]:
    return mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class Cliente(Base):
    """El tenant. Varios es un cliente más para su propio trabajo interno."""

    __tablename__ = "cliente"
    id: Mapped[uuid.UUID] = _id()
    nombre: Mapped[str] = mapped_column(String(200))
    slug: Mapped[str] = mapped_column(String(80), unique=True)
    activo: Mapped[bool] = mapped_column(Boolean, default=True, server_default="true")
    creado_en: Mapped[datetime] = _creado()


class Usuario(Base):
    __tablename__ = "usuario"
    __table_args__ = (UniqueConstraint("cliente_id", "email", name="uq_usuario_cliente_email"),)
    id: Mapped[uuid.UUID] = _id()
    cliente_id: Mapped[uuid.UUID] = _cliente()
    email: Mapped[str] = mapped_column(String(320))
    nombre: Mapped[str] = mapped_column(String(200))
    roles: Mapped[list] = mapped_column(JSON, default=list, server_default="[]")
    es_persona: Mapped[bool] = mapped_column(Boolean, default=True, server_default="true")
    activo: Mapped[bool] = mapped_column(Boolean, default=True, server_default="true")
    creado_en: Mapped[datetime] = _creado()


class Solicitud(Base):
    """El encargo (Guía v1.4 §4): lo que alguien pide, con su estado y su riesgo."""

    __tablename__ = "solicitud"
    __table_args__ = (
        CheckConstraint(_en("estado", ESTADOS_SOLICITUD), name="estado"),
        CheckConstraint(_en("riesgo", RIESGOS), name="riesgo"),
    )
    id: Mapped[uuid.UUID] = _id()
    cliente_id: Mapped[uuid.UUID] = _cliente()
    autor_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("usuario.id"))
    titulo: Mapped[str] = mapped_column(String(300))
    descripcion: Mapped[str] = mapped_column(Text, default="", server_default="")
    estado: Mapped[str] = mapped_column(String(30), default="RECIBIDO", server_default="RECIBIDO")
    riesgo: Mapped[str] = mapped_column(String(10), default="bajo", server_default="bajo")
    version: Mapped[int] = mapped_column(Integer, default=1, server_default="1")
    version_definicion: Mapped[str | None] = mapped_column(String(20))
    # Apartado por un socio hasta esta hora (N3c). No decide nada; se pierde al cambiar de estado.
    pospuesto_hasta: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    creado_en: Mapped[datetime] = _creado()
    actualizado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class Plan(Base):
    __tablename__ = "plan"
    id: Mapped[uuid.UUID] = _id()
    cliente_id: Mapped[uuid.UUID] = _cliente()
    solicitud_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("solicitud.id", ondelete="CASCADE"), index=True)
    version: Mapped[int] = mapped_column(Integer, default=1, server_default="1")
    contenido: Mapped[dict] = mapped_column(JSON, default=dict, server_default="{}")
    creado_por: Mapped[str] = mapped_column(String(200))
    aprobado_por: Mapped[uuid.UUID | None] = mapped_column(Uuid, ForeignKey("usuario.id"))
    creado_en: Mapped[datetime] = _creado()


class Tarea(Base):
    __tablename__ = "tarea"
    __table_args__ = (
        CheckConstraint(_en("estado", ESTADOS_TAREA), name="estado"),
        CheckConstraint("intentos >= 0 AND intentos <= max_intentos", name="intentos"),
        UniqueConstraint("cliente_id", "clave_idempotencia", name="uq_tarea_cliente_clave"),
    )
    id: Mapped[uuid.UUID] = _id()
    cliente_id: Mapped[uuid.UUID] = _cliente()
    solicitud_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("solicitud.id", ondelete="CASCADE"), index=True)
    plan_id: Mapped[uuid.UUID | None] = mapped_column(Uuid, ForeignKey("plan.id", ondelete="SET NULL"))
    titulo: Mapped[str] = mapped_column(String(300))
    responsable: Mapped[str] = mapped_column(String(200))
    estado: Mapped[str] = mapped_column(String(20), default="queued", server_default="queued")
    intentos: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
    max_intentos: Mapped[int] = mapped_column(Integer, default=3, server_default="3")
    clave_idempotencia: Mapped[str | None] = mapped_column(String(200))
    depende_de: Mapped[list] = mapped_column(JSON, default=list, server_default="[]")
    creado_en: Mapped[datetime] = _creado()
    actualizado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class Documento(Base):
    """Documento recibido. Entra en cuarentena y se identifica por su huella (plan S7)."""

    __tablename__ = "documento"
    __table_args__ = (
        CheckConstraint(_en("clasificacion", CLASIFICACIONES), name="clasificacion"),
        CheckConstraint(_en("estado", ESTADOS_DOCUMENTO), name="estado"),
        CheckConstraint("length(huella_sha256) = 64", name="huella"),
        UniqueConstraint("cliente_id", "huella_sha256", name="uq_documento_cliente_huella"),
    )
    id: Mapped[uuid.UUID] = _id()
    cliente_id: Mapped[uuid.UUID] = _cliente()
    solicitud_id: Mapped[uuid.UUID | None] = mapped_column(Uuid, ForeignKey("solicitud.id", ondelete="SET NULL"))
    nombre: Mapped[str] = mapped_column(String(300))
    tipo_mime: Mapped[str] = mapped_column(String(100))
    tamano_bytes: Mapped[int] = mapped_column(BigInteger)
    huella_sha256: Mapped[str] = mapped_column(String(64))
    ruta: Mapped[str] = mapped_column(String(500))
    clasificacion: Mapped[str] = mapped_column(String(20), default="interno", server_default="interno")
    estado: Mapped[str] = mapped_column(String(20), default="cuarentena", server_default="cuarentena")
    subido_por: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("usuario.id"))
    creado_en: Mapped[datetime] = _creado()


class Aprobacion(Base):
    """Aprobación humana (P10). Nadie se aprueba a sí mismo."""

    __tablename__ = "aprobacion"
    __table_args__ = (
        CheckConstraint(_en("decision", DECISIONES), name="decision"),
        # Caducada: no la ha decidido nadie, así que no tiene aprobador (P10: nunca aprobación tácita).
        CheckConstraint(
            "decision = 'pendiente' "
            "OR (decision = 'caducada' AND aprobador_id IS NULL AND decidida_en IS NOT NULL) "
            "OR (decision IN ('aprobada', 'rechazada') AND aprobador_id IS NOT NULL AND decidida_en IS NOT NULL)",
            name="decidida",
        ),
        Index("ix_aprobacion_pendiente_caduca", "cliente_id", "caduca_en",
              postgresql_where=text("decision = 'pendiente'")),
        CheckConstraint("aprobador_id IS NULL OR solicitada_por <> aprobador_id::text", name="no_autoaprobacion"),
    )
    id: Mapped[uuid.UUID] = _id()
    cliente_id: Mapped[uuid.UUID] = _cliente()
    solicitud_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("solicitud.id", ondelete="CASCADE"), index=True)
    objeto: Mapped[str] = mapped_column(String(200))
    version: Mapped[int] = mapped_column(Integer)
    solicitada_por: Mapped[str] = mapped_column(String(200))
    aprobador_id: Mapped[uuid.UUID | None] = mapped_column(Uuid, ForeignKey("usuario.id"))
    decision: Mapped[str] = mapped_column(String(12), default="pendiente", server_default="pendiente")
    motivo: Mapped[str] = mapped_column(Text, default="", server_default="")
    creado_en: Mapped[datetime] = _creado()
    decidida_en: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    caduca_en: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))


class EventoAuditoria(Base):
    """Registro inmutable de todo cambio de estado y acción (integrations/contracts/evento-auditoria.schema.json)."""

    __tablename__ = "evento_auditoria"
    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True), primary_key=True)
    cliente_id: Mapped[uuid.UUID] = _cliente()
    momento: Mapped[datetime] = _creado()
    actor: Mapped[str] = mapped_column(String(200))
    accion: Mapped[str] = mapped_column(String(100))
    objeto: Mapped[str] = mapped_column(String(200))
    antes: Mapped[str | None] = mapped_column(String(50))
    despues: Mapped[str | None] = mapped_column(String(50))
    motivo: Mapped[str] = mapped_column(Text, default="", server_default="")
    version_definicion: Mapped[str | None] = mapped_column(String(20))
    clave_idempotencia: Mapped[str | None] = mapped_column(String(200))
    datos: Mapped[dict] = mapped_column(JSON, default=dict, server_default="{}")


class EjecucionModelo(Base):
    """Cada llamada a un modelo de IA: quién, qué modelo, cuánto costó y cómo acabó (P16, P29)."""

    __tablename__ = "ejecucion_modelo"
    __table_args__ = (CheckConstraint(_en("resultado", RESULTADOS_MODELO), name="resultado"),)
    id: Mapped[uuid.UUID] = _id()
    cliente_id: Mapped[uuid.UUID] = _cliente()
    solicitud_id: Mapped[uuid.UUID | None] = mapped_column(Uuid, ForeignKey("solicitud.id", ondelete="SET NULL"))
    tarea_id: Mapped[uuid.UUID | None] = mapped_column(Uuid, ForeignKey("tarea.id", ondelete="SET NULL"))
    proveedor: Mapped[str] = mapped_column(String(50))
    modelo: Mapped[str] = mapped_column(String(100))
    version_instrucciones: Mapped[str] = mapped_column(String(50))
    tokens_entrada: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
    tokens_salida: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
    coste_eur: Mapped[Decimal] = mapped_column(Numeric(12, 6), default=0, server_default="0")
    latencia_ms: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
    resultado: Mapped[str] = mapped_column(String(12))
    error: Mapped[str | None] = mapped_column(Text)
    creado_en: Mapped[datetime] = _creado()


class UsoHerramienta(Base):
    """Cada intento de usar una herramienta, autorizado o no (P21)."""

    __tablename__ = "uso_herramienta"
    __table_args__ = (CheckConstraint(_en("resultado", RESULTADOS_HERRAMIENTA), name="resultado"),)
    id: Mapped[uuid.UUID] = _id()
    cliente_id: Mapped[uuid.UUID] = _cliente()
    tarea_id: Mapped[uuid.UUID | None] = mapped_column(Uuid, ForeignKey("tarea.id", ondelete="SET NULL"))
    herramienta: Mapped[str] = mapped_column(String(100))
    parametros: Mapped[dict] = mapped_column(JSON, default=dict, server_default="{}")
    autorizado: Mapped[bool] = mapped_column(Boolean)
    requiere_aprobacion: Mapped[bool] = mapped_column(Boolean, default=False, server_default="false")
    aprobacion_id: Mapped[uuid.UUID | None] = mapped_column(Uuid, ForeignKey("aprobacion.id", ondelete="SET NULL"))
    resultado: Mapped[str] = mapped_column(String(12))
    creado_en: Mapped[datetime] = _creado()


# ----------------------------- Conocimiento (cerebro) -----------------------------


class Fuente(Base):
    """Fuente citable. Las comunes (cliente_id nulo) vienen de tools/org_data/fuentes.py."""

    __tablename__ = "fuente"
    __table_args__ = (
        UniqueConstraint("cliente_id", "codigo", name="uq_fuente_cliente_codigo", postgresql_nulls_not_distinct=True),
    )
    id: Mapped[uuid.UUID] = _id()
    cliente_id: Mapped[uuid.UUID | None] = _cliente(nullable=True)
    codigo: Mapped[str] = mapped_column(String(80))
    titulo: Mapped[str] = mapped_column(String(500))
    organismo: Mapped[str] = mapped_column(String(200), default="", server_default="")
    url: Mapped[str] = mapped_column(String(1000), default="", server_default="")
    tipo: Mapped[str] = mapped_column(String(60), default="", server_default="")
    autoridad: Mapped[str] = mapped_column(String(20), default="", server_default="")
    vigencia: Mapped[str] = mapped_column(String(60), default="", server_default="")
    estado: Mapped[str] = mapped_column(String(20), default="draft", server_default="draft")
    creado_en: Mapped[datetime] = _creado()


class FichaConocimiento(Base):
    """Unidad de conocimiento con estado y fuentes. La búsqueda solo devuelve fichas con al menos una fuente."""

    __tablename__ = "ficha_conocimiento"
    __table_args__ = (
        CheckConstraint(_en("estado", ESTADOS_FICHA), name="estado"),
        UniqueConstraint(
            "cliente_id", "codigo", name="uq_ficha_conocimiento_cliente_codigo", postgresql_nulls_not_distinct=True
        ),
    )
    id: Mapped[uuid.UUID] = _id()
    cliente_id: Mapped[uuid.UUID | None] = _cliente(nullable=True)
    codigo: Mapped[str] = mapped_column(String(160))
    titulo: Mapped[str] = mapped_column(String(300))
    cuerpo: Mapped[str] = mapped_column(Text)
    estado: Mapped[str] = mapped_column(String(12), default="draft", server_default="draft")
    etiquetas: Mapped[list] = mapped_column(JSON, default=list, server_default="[]")
    origen: Mapped[str] = mapped_column(String(300), default="", server_default="")
    creado_en: Mapped[datetime] = _creado()
    actualizado_en: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class FichaFuente(Base):
    __tablename__ = "ficha_fuente"
    ficha_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("ficha_conocimiento.id", ondelete="CASCADE"), primary_key=True
    )
    fuente_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("fuente.id", ondelete="RESTRICT"), primary_key=True)
    cliente_id: Mapped[uuid.UUID | None] = _cliente(nullable=True)
    cita: Mapped[str] = mapped_column(String(300), default="", server_default="")


TABLAS_DE_CLIENTE = (
    "usuario", "solicitud", "plan", "tarea", "documento", "aprobacion", "evento_auditoria",
    "ejecucion_modelo", "uso_herramienta",
)
TABLAS_DE_CONOCIMIENTO = ("fuente", "ficha_conocimiento", "ficha_fuente")
