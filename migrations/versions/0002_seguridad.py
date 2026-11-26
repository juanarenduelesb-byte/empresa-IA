"""Seguridad en la propia base de datos.

- RLS (FORCE) en todas las tablas: cada fila solo es visible y escribible para su cliente, que la aplicación fija
  con `set_config('varios.cliente_id', ...)` al abrir la transacción (varios.db.sesion). Sin cliente fijado, nada.
- El conocimiento común (cliente_id nulo) se lee desde cualquier cliente, pero solo lo escribe el administrador.
- La auditoría no se puede modificar, borrar ni vaciar, ni siquiera con el usuario propietario.
- Búsqueda de texto en español sobre las fichas (columna generada e índice GIN).
- Permisos mínimos para el usuario de la aplicación `varios_app`, si existe.

Revision ID: 0002
Revises: 0001
"""

from __future__ import annotations

from alembic import op

revision = "0002"
down_revision = "0001"
branch_labels = None
depends_on = None

DE_CLIENTE = (
    "usuario", "solicitud", "plan", "tarea", "documento", "aprobacion", "evento_auditoria",
    "ejecucion_modelo", "uso_herramienta",
)
CONOCIMIENTO = ("fuente", "ficha_conocimiento", "ficha_fuente")
APP = "varios_app"


def upgrade() -> None:
    op.execute(
        """
        CREATE FUNCTION varios_cliente_actual() RETURNS uuid LANGUAGE sql STABLE AS
        $$ SELECT NULLIF(current_setting('varios.cliente_id', true), '')::uuid $$
        """
    )
    # Cliente: cada uno solo se ve a sí mismo.
    op.execute("ALTER TABLE cliente ENABLE ROW LEVEL SECURITY; ALTER TABLE cliente FORCE ROW LEVEL SECURITY")
    op.execute("CREATE POLICY aislamiento ON cliente USING (id = varios_cliente_actual())")
    for t in DE_CLIENTE:
        op.execute(f"ALTER TABLE {t} ENABLE ROW LEVEL SECURITY; ALTER TABLE {t} FORCE ROW LEVEL SECURITY")
        op.execute(
            f"CREATE POLICY aislamiento ON {t} USING (cliente_id = varios_cliente_actual()) "
            "WITH CHECK (cliente_id = varios_cliente_actual())"
        )
    for t in CONOCIMIENTO:
        op.execute(f"ALTER TABLE {t} ENABLE ROW LEVEL SECURITY; ALTER TABLE {t} FORCE ROW LEVEL SECURITY")
        op.execute(
            f"CREATE POLICY lectura ON {t} FOR SELECT "
            "USING (cliente_id IS NULL OR cliente_id = varios_cliente_actual())"
        )
        op.execute(f"CREATE POLICY alta ON {t} FOR INSERT WITH CHECK (cliente_id = varios_cliente_actual())")
        op.execute(
            f"CREATE POLICY cambio ON {t} FOR UPDATE USING (cliente_id = varios_cliente_actual()) "
            "WITH CHECK (cliente_id = varios_cliente_actual())"
        )
        op.execute(f"CREATE POLICY baja ON {t} FOR DELETE USING (cliente_id = varios_cliente_actual())")

    # Auditoría inmutable.
    op.execute(
        """
        CREATE FUNCTION varios_auditoria_inmutable() RETURNS trigger LANGUAGE plpgsql AS
        $$ BEGIN RAISE EXCEPTION 'La auditoría no se puede modificar ni borrar (%).', TG_OP; END $$
        """
    )
    op.execute(
        "CREATE TRIGGER auditoria_inmutable BEFORE UPDATE OR DELETE ON evento_auditoria "
        "FOR EACH ROW EXECUTE FUNCTION varios_auditoria_inmutable()"
    )
    op.execute(
        "CREATE TRIGGER auditoria_no_truncar BEFORE TRUNCATE ON evento_auditoria "
        "FOR EACH STATEMENT EXECUTE FUNCTION varios_auditoria_inmutable()"
    )

    # Búsqueda de texto en español.
    op.execute(
        "ALTER TABLE ficha_conocimiento ADD COLUMN busqueda tsvector GENERATED ALWAYS AS "
        "(to_tsvector('spanish', coalesce(titulo, '') || ' ' || coalesce(cuerpo, ''))) STORED"
    )
    op.execute("CREATE INDEX ix_ficha_conocimiento_busqueda ON ficha_conocimiento USING gin (busqueda)")

    # Permisos del usuario de la aplicación (se crea fuera de las migraciones, con su contraseña en el entorno).
    tablas = ", ".join(("cliente", *DE_CLIENTE, *CONOCIMIENTO))
    op.execute(
        f"""
        DO $$ BEGIN
          IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '{APP}') THEN
            GRANT USAGE ON SCHEMA public TO {APP};
            GRANT SELECT ON cliente TO {APP};
            GRANT SELECT, INSERT, UPDATE, DELETE ON {tablas} TO {APP};
            REVOKE UPDATE, DELETE, TRUNCATE ON evento_auditoria FROM {APP};
            GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO {APP};
            GRANT EXECUTE ON FUNCTION varios_cliente_actual() TO {APP};
          END IF;
        END $$
        """
    )


def downgrade() -> None:
    op.execute(
        f"""
        DO $$ BEGIN
          IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '{APP}') THEN
            REVOKE ALL ON ALL TABLES IN SCHEMA public FROM {APP};
            REVOKE ALL ON ALL SEQUENCES IN SCHEMA public FROM {APP};
          END IF;
        END $$
        """
    )
    op.execute("DROP INDEX IF EXISTS ix_ficha_conocimiento_busqueda")
    op.execute("ALTER TABLE ficha_conocimiento DROP COLUMN IF EXISTS busqueda")
    op.execute("DROP TRIGGER IF EXISTS auditoria_no_truncar ON evento_auditoria")
    op.execute("DROP TRIGGER IF EXISTS auditoria_inmutable ON evento_auditoria")
    op.execute("DROP FUNCTION IF EXISTS varios_auditoria_inmutable()")
    for t in ("cliente", *DE_CLIENTE, *CONOCIMIENTO):
        for pol in ("aislamiento", "lectura", "alta", "cambio", "baja"):
            op.execute(f"DROP POLICY IF EXISTS {pol} ON {t}")
        op.execute(f"ALTER TABLE {t} NO FORCE ROW LEVEL SECURITY; ALTER TABLE {t} DISABLE ROW LEVEL SECURITY")
    op.execute("DROP FUNCTION IF EXISTS varios_cliente_actual()")
