"""PostgreSQL real para las pruebas de base de datos.

Usa VARIOS_TEST_DATABASE_URL (administrador, p. ej. el servicio de CI) o, si no existe, arranca un PostgreSQL
desechable con tools/pg_local.py. Si no hay ninguno, las pruebas de base de datos se saltan con un aviso.
"""

from __future__ import annotations

import os
import uuid

import pg_local
import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, text
from sqlalchemy.engine import make_url

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _alembic(url: str) -> Config:
    cfg = Config(os.path.join(RAIZ, "alembic.ini"))
    cfg.set_main_option("script_location", os.path.join(RAIZ, "migrations"))
    cfg.attributes["url"] = url
    return cfg


@pytest.fixture(scope="session")
def servidor():
    """URL de administrador del servidor (base 'postgres')."""
    url = os.environ.get("VARIOS_TEST_DATABASE_URL")
    cluster = None
    if not url:
        if not pg_local.disponible():
            pytest.skip("Sin PostgreSQL: define VARIOS_TEST_DATABASE_URL o instala PostgreSQL")
        cluster = pg_local.arrancar()
        url = cluster.url()
    yield url
    if cluster:
        cluster.parar()


def crear_base(servidor: str) -> str:
    nombre = f"varios_{uuid.uuid4().hex[:10]}"
    admin = create_engine(servidor, isolation_level="AUTOCOMMIT")
    with admin.connect() as c:
        c.execute(text(f"CREATE DATABASE {nombre}"))
        existe = c.execute(text("SELECT 1 FROM pg_roles WHERE rolname = 'varios_app'")).scalar()
        if not existe:
            c.execute(text("CREATE ROLE varios_app LOGIN PASSWORD 'solo-pruebas'"))
    admin.dispose()
    return make_url(servidor).set(database=nombre).render_as_string(hide_password=False)


@pytest.fixture(scope="session")
def base(servidor):
    """Base migrada hasta la última versión. Devuelve (url_admin, url_app)."""
    url_admin = crear_base(servidor)
    command.upgrade(_alembic(url_admin), "head")
    url_app = make_url(url_admin).set(username="varios_app", password="solo-pruebas").render_as_string(
        hide_password=False
    )
    return url_admin, url_app


@pytest.fixture(scope="session")
def motor_admin(base):
    e = create_engine(base[0])
    yield e
    e.dispose()


@pytest.fixture(scope="session")
def motor_app(base):
    e = create_engine(base[1])
    yield e
    e.dispose()


@pytest.fixture()
def dos_clientes(motor_admin):
    """Dos clientes señuelo (inventados) con un usuario cada uno. Devuelve {'A': (cliente, usuario), 'B': ...}."""
    datos = {}
    with motor_admin.begin() as c:
        for letra in "AB":
            cid, uid = uuid.uuid4(), uuid.uuid4()
            c.execute(text("INSERT INTO cliente (id, nombre, slug) VALUES (:i, :n, :s)"),
                      {"i": cid, "n": f"Señuelo {letra} (inventado)", "s": f"senuelo-{letra.lower()}-{cid.hex[:6]}"})
            c.execute(text("SELECT set_config('varios.cliente_id', :c, true)"), {"c": str(cid)})
            c.execute(text("INSERT INTO usuario (id, cliente_id, email, nombre, roles) "
                           "VALUES (:u, :c, :e, :n, '[\"aprobador\"]')"),
                      {"u": uid, "c": cid, "e": f"persona@{letra.lower()}.invalid", "n": f"Persona {letra}"})
            datos[letra] = (cid, uid)
    return datos
