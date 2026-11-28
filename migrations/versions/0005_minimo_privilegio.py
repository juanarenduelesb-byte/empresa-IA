"""Mínimo privilegio: la aplicación solo lee `cliente` y `usuario` (repaso del 28/11, tanda 02:30).

0002 daba a `varios_app` SELECT, INSERT, UPDATE y DELETE también sobre `cliente` y `usuario`. La API nunca escribe en
ellas, pero los papeles que deciden quién aprueba están en `usuario.roles`: con un fallo en el código, alguien de un
cliente podía darse el papel de aprobador, crear personas o borrar su propio cliente. Las altas y los papeles los da el
administrador (la semilla y, con el proveedor de identidad de D-033, lo que se decida entonces).

Revision ID: 0005
Revises: 0004
"""

from __future__ import annotations

from alembic import op

revision = "0005"
down_revision = "0004"
branch_labels = None
depends_on = None

APP = "varios_app"


def upgrade() -> None:
    op.execute(f"""
        DO $$ BEGIN
          IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '{APP}') THEN
            REVOKE INSERT, UPDATE, DELETE, TRUNCATE ON cliente, usuario FROM {APP};
            GRANT SELECT ON cliente, usuario TO {APP};
          END IF;
        END $$
    """)


def downgrade() -> None:
    op.execute(f"""
        DO $$ BEGIN
          IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '{APP}') THEN
            GRANT SELECT, INSERT, UPDATE, DELETE ON cliente, usuario TO {APP};
          END IF;
        END $$
    """)
