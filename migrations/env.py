"""Entorno de Alembic. La URL viene de la configuración, nunca de alembic.ini."""

from __future__ import annotations

from alembic import context
from sqlalchemy import create_engine, pool

from varios.config import ajustes
from varios.db.modelos import Base

config = context.config
target_metadata = Base.metadata


# Objetos que solo existen en SQL (migración 0002) y no en los modelos.
SOLO_SQL = {"busqueda", "ix_ficha_conocimiento_busqueda"}


def _incluir(objeto, nombre, tipo, reflejado, comparado) -> bool:
    return not (reflejado and nombre in SOLO_SQL)


def _url() -> str:
    url = config.attributes.get("url") or ajustes().database_url_admin or ajustes().database_url
    if not url:
        raise RuntimeError("Falta VARIOS_DATABASE_URL_ADMIN (o VARIOS_DATABASE_URL) para migrar.")
    return url


def run_migrations_offline() -> None:
    context.configure(url=_url(), target_metadata=target_metadata, literal_binds=True, compare_type=True)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    conexion = config.attributes.get("connection")
    if conexion is not None:
        context.configure(
            connection=conexion, target_metadata=target_metadata, compare_type=True, include_object=_incluir
        )
        with context.begin_transaction():
            context.run_migrations()
        return
    motor = create_engine(_url(), poolclass=pool.NullPool)
    with motor.connect() as conexion:
        context.configure(
            connection=conexion, target_metadata=target_metadata, compare_type=True, include_object=_incluir
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
