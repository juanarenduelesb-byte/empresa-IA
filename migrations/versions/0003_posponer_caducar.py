"""Posponer y caducar en la base (N3c, resto de M-041).

- `solicitud.pospuesto_hasta`: un socio aparta un encargo que espera a una persona hasta una hora. No aprueba ni
  rechaza nada y se pierde cuando el encargo cambia de estado (la misma regla que la oficina, N4).
- `aprobacion.caduca_en`: hora a la que caduca una aprobación sin decidir. Al caducar, la decisión pasa a
  `caducada` (sin aprobador: no la ha decidido nadie) y el encargo vuelve como pregunta (ESCALADO), nunca aprobado
  (P10: «nunca aprobación tácita»; D-019).
- Las columnas nuevas quedan bajo las mismas políticas RLS de su tabla; no hace falta ninguna política nueva.

Revision ID: 0003
Revises: 0002
"""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op

revision = "0003"
down_revision = "0002"
branch_labels = None
depends_on = None

DECIDIDA = (
    "decision = 'pendiente' "
    "OR (decision = 'caducada' AND aprobador_id IS NULL AND decidida_en IS NOT NULL) "
    "OR (decision IN ('aprobada', 'rechazada') AND aprobador_id IS NOT NULL AND decidida_en IS NOT NULL)"
)


def upgrade() -> None:
    op.add_column("solicitud", sa.Column("pospuesto_hasta", sa.DateTime(timezone=True), nullable=True))
    op.add_column("aprobacion", sa.Column("caduca_en", sa.DateTime(timezone=True), nullable=True))
    op.drop_constraint(op.f("ck_aprobacion_decision"), "aprobacion", type_="check")
    op.create_check_constraint(op.f("ck_aprobacion_decision"), "aprobacion",
                               "decision IN ('pendiente', 'aprobada', 'rechazada', 'caducada')")
    op.drop_constraint(op.f("ck_aprobacion_decidida"), "aprobacion", type_="check")
    op.create_check_constraint(op.f("ck_aprobacion_decidida"), "aprobacion", DECIDIDA)
    op.create_index("ix_aprobacion_pendiente_caduca", "aprobacion", ["cliente_id", "caduca_en"],
                    postgresql_where=sa.text("decision = 'pendiente'"))


def downgrade() -> None:
    op.drop_index("ix_aprobacion_pendiente_caduca", table_name="aprobacion")
    # Una aprobación caducada no se puede convertir en otra cosa sin inventar una decisión: no se baja con ellas.
    hay = op.get_bind().execute(sa.text("SELECT count(*) FROM aprobacion WHERE decision = 'caducada'")).scalar()
    if hay:
        raise RuntimeError(f"Hay {hay} aprobaciones caducadas: bajar de 0003 obligaría a inventar su decisión")
    op.drop_constraint(op.f("ck_aprobacion_decidida"), "aprobacion", type_="check")
    op.drop_constraint(op.f("ck_aprobacion_decision"), "aprobacion", type_="check")
    op.create_check_constraint(op.f("ck_aprobacion_decision"), "aprobacion",
                               "decision IN ('pendiente', 'aprobada', 'rechazada')")
    op.create_check_constraint(
        op.f("ck_aprobacion_decidida"), "aprobacion",
        "decision = 'pendiente' OR (aprobador_id IS NOT NULL AND decidida_en IS NOT NULL)")
    op.drop_column("aprobacion", "caduca_en")
    op.drop_column("solicitud", "pospuesto_hasta")
