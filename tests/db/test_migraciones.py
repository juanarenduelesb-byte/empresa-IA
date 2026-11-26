"""Las migraciones suben y bajan desde cero, y el esquema coincide con los modelos y las definiciones."""

import json
import os

from alembic import command
from sqlalchemy import create_engine, inspect, text

from varios.db import modelos

from .conftest import RAIZ, _alembic, crear_base


def test_suben_bajan_y_vuelven_a_subir(servidor):
    url = crear_base(servidor)
    cfg = _alembic(url)
    command.upgrade(cfg, "head")
    command.downgrade(cfg, "base")
    e = create_engine(url)
    assert set(inspect(e).get_table_names()) <= {"alembic_version"}
    command.upgrade(cfg, "head")
    tablas = set(inspect(e).get_table_names())
    assert {t.name for t in modelos.Base.metadata.sorted_tables} <= tablas
    e.dispose()


def test_rls_forzada_en_todas_las_tablas(motor_admin):
    with motor_admin.connect() as c:
        filas = c.execute(text("SELECT relname, relrowsecurity, relforcerowsecurity FROM pg_class "
                               "WHERE relkind = 'r' AND relnamespace = 'public'::regnamespace "
                               "AND relname <> 'alembic_version'")).all()
    sin = [r.relname for r in filas if not (r.relrowsecurity and r.relforcerowsecurity)]
    assert not sin, f"Tablas sin RLS forzada: {sin}"


def test_estados_coinciden_con_las_definiciones():
    defs = os.path.join(RAIZ, "processes", "definitions")
    encargo = json.load(open(os.path.join(defs, "encargo.json"), encoding="utf-8"))
    objetos = {o["id"]: o for o in json.load(open(os.path.join(defs, "objetos.json"), encoding="utf-8"))["objetos"]}
    assert set(modelos.ESTADOS_SOLICITUD) == set(encargo["estados"])
    assert set(modelos.ESTADOS_TAREA) == set(objetos["tarea"]["estados"])
    assert set(modelos.ESTADOS_FICHA) == set(objetos["ficha_conocimiento"]["estados"])
