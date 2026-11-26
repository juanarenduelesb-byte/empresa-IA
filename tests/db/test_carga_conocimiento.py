"""El conocimiento del repositorio se carga en la base, se busca con cita y no se duplica (B1)."""

from sqlalchemy import text

from varios.db.carga_conocimiento import cargar_conocimiento, fichas
from varios.db.repositorio import Repositorio
from varios.db.sesion import sesion_de_cliente
from varios.procesos.motor import Identidad


def test_trocea_knowledge():
    fs = fichas()
    assert len(fs) > 100
    assert all(f["origen"].startswith("knowledge/") and not f["origen"].startswith("knowledge/grafo/") for f in fs)
    assert len({f["codigo"] for f in fs}) == len(fs)


def test_carga_busca_con_cita_y_es_idempotente(base, motor_admin, motor_app, dos_clientes):
    primera = cargar_conocimiento(base[0])
    segunda = cargar_conocimiento(base[0])
    assert primera["fichas"] == segunda["fichas"] > 100
    assert primera["con_fuente_externa"] > 0
    with motor_admin.connect() as c:
        n = c.execute(text("SELECT count(*) FROM ficha_conocimiento WHERE origen LIKE 'knowledge/%'")).scalar()
    assert n == primera["fichas"]
    ca, ua = dos_clientes["A"]
    with sesion_de_cliente(motor_app, ca) as s:
        res = Repositorio(s, Identidad(str(ua), str(ca))).buscar_conocimiento("siniestro")
    assert res, "La búsqueda de 'siniestro' en el conocimiento común no devuelve nada"
    assert all(any(f["codigo"].startswith("repo:") for f in r["fuentes"]) for r in res)
