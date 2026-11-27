"""Pólizas de la cartera de cada cliente (A5): la copia que usa el proceso de referencia (apertura de siniestros).

Las reglas fijas de apertura (`varios.seguros.apertura`) comprueban vigencia y ramo contra la cartera; hasta ahora
solo existía en un archivo (`processes/.../casos/cartera.json`). Con RLS forzada como el resto de tablas de cliente.

Revision ID: 0004
Revises: 0003
"""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op

revision = "0004"
down_revision = "0003"
branch_labels = None
depends_on = None

APP = "varios_app"


def upgrade() -> None:
    op.create_table(
        "poliza",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("cliente_id", sa.Uuid(), nullable=False),
        sa.Column("numero", sa.String(length=60), nullable=False),
        sa.Column("ramo", sa.String(length=40), nullable=False),
        sa.Column("aseguradora", sa.String(length=200), server_default="", nullable=False),
        sa.Column("efecto", sa.Date(), nullable=False),
        sa.Column("vencimiento", sa.Date(), nullable=False),
        sa.Column("creado_en", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.CheckConstraint("vencimiento >= efecto", name=op.f("ck_poliza_vigencia")),
        sa.ForeignKeyConstraint(["cliente_id"], ["cliente.id"], name=op.f("fk_poliza_cliente_id_cliente"),
                                ondelete="RESTRICT"),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_poliza")),
        sa.UniqueConstraint("cliente_id", "numero", name="uq_poliza_cliente_numero"),
    )
    op.create_index(op.f("ix_poliza_cliente_id"), "poliza", ["cliente_id"], unique=False)
    op.execute("ALTER TABLE poliza ENABLE ROW LEVEL SECURITY; ALTER TABLE poliza FORCE ROW LEVEL SECURITY")
    op.execute("CREATE POLICY aislamiento ON poliza USING (cliente_id = varios_cliente_actual()) "
               "WITH CHECK (cliente_id = varios_cliente_actual())")
    op.execute(f"""
        DO $$ BEGIN
          IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '{APP}') THEN
            GRANT SELECT, INSERT, UPDATE, DELETE ON poliza TO {APP};
          END IF;
        END $$
    """)


def downgrade() -> None:
    op.drop_index(op.f("ix_poliza_cliente_id"), table_name="poliza")
    op.drop_table("poliza")
