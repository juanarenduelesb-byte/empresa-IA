"""Los datos de ejemplo cargan, no se duplican, respetan el aislamiento y coinciden con los archivos de casos (A5)."""

import json

from fastapi.testclient import TestClient
from sqlalchemy import text

from varios.api import oficina
from varios.api.app import app
from varios.api.identidad import emitir
from varios.config import ajustes
from varios.db.semilla import CASOS, CLIENTES, CONTROL_A, RAIZ, _id, cargar, ejemplos, vaciar
from varios.db.sesion import sesion_de_cliente

CERO = {"fuentes": 0, "clientes": 0, "usuarios": 0, "solicitudes": 0, "polizas": 0, "siniestros": 0,
        "encargos_control_a": 0}


def _archivo(ruta):
    return json.loads((RAIZ / ruta).read_text(encoding="utf-8"))


def test_semilla_idempotente_y_aislada(base, motor_app):
    cargar(base[0])
    assert cargar(base[0]) == CERO
    ej = ejemplos()
    for slug, _, usuarios, solicitudes in CLIENTES:
        mias = [x for k in ("siniestros", "encargos") for x in ej[k] if x["cliente"] == slug]
        with sesion_de_cliente(motor_app, _id("cliente", slug)) as s:
            assert s.execute(text("SELECT count(*) FROM solicitud")).scalar() == len(solicitudes) + len(mias)
            assert s.execute(text("SELECT count(*) FROM usuario")).scalar() == len(usuarios)
            assert s.execute(text("SELECT count(*) FROM fuente WHERE cliente_id IS NULL")).scalar() > 0
            polizas = set(s.execute(text("SELECT numero FROM poliza")).scalars())
            assert polizas == {p["numero"] for p in ej["polizas"] if p["cliente"] == slug}


def test_la_semilla_coincide_con_los_archivos_de_casos(base, motor_app):
    """Cada caso de los archivos está una vez en la base, en un solo cliente y con su texto, sin nada de más."""
    cargar(base[0])
    casos = _archivo(CASOS / "casos.json")["casos"]
    cartera = _archivo(CASOS / "cartera.json")["polizas"]
    control = _archivo(CONTROL_A)["encargos"]
    assert (len(casos), len(cartera), len(control)) == (20, 11, 25)
    vistos = {"siniestros": [], "encargos": [], "polizas": []}
    for slug, *_ in CLIENTES:
        with sesion_de_cliente(motor_app, _id("cliente", slug)) as c:  # con RLS, como la aplicación
            for x in casos:
                fila = c.execute(text("SELECT descripcion FROM solicitud WHERE id = :i"),
                                 {"i": _id("ejemplo", slug, x["id"])}).scalar()
                if fila is not None:
                    assert fila == x["mensaje"]
                    vistos["siniestros"].append(x["id"])
            for x in control:
                fila = c.execute(text("SELECT titulo FROM solicitud WHERE id = :i"),
                                 {"i": _id("ejemplo", slug, x["id"])}).scalar()
                if fila is not None:
                    assert x["texto"][:200] in fila
                    vistos["encargos"].append(x["id"])
            for p in c.execute(text("SELECT numero, ramo, aseguradora, efecto, vencimiento FROM poliza")).mappings():
                orig = next(o for o in cartera if o["numero"] == p["numero"])
                assert (p["ramo"], p["aseguradora"], str(p["efecto"]), str(p["vencimiento"])) == (
                    orig["ramo"], orig["aseguradora"], orig["efecto"], orig["vencimiento"])
                vistos["polizas"].append(p["numero"])
    assert sorted(vistos["siniestros"]) == sorted(x["id"] for x in casos)
    assert sorted(vistos["encargos"]) == sorted(x["id"] for x in control)
    assert sorted(vistos["polizas"]) == sorted(p["numero"] for p in cartera)
    # Cada siniestro está en el cliente de su póliza: la regla de apertura nunca mira la cartera de otro cliente.
    de = {p["numero"]: p["cliente"] for p in ejemplos()["polizas"]}
    for s in ejemplos()["siniestros"]:
        num = next(x for x in casos if x["id"] == s["id"])["hechos"].get("poliza_numero")
        if num in de:
            assert s["cliente"] == de[num]
    assert {x["cliente"] for k in ("siniestros", "encargos", "polizas") for x in ejemplos()[k]} == {"atalaya",
                                                                                                    "senuelo"}


def test_cada_cliente_ve_solo_lo_suyo_en_la_api(base, motor_app, monkeypatch):
    cargar(base[0])
    monkeypatch.setenv("VARIOS_JWT_SECRETO", "solo-pruebas-" + "y" * 40)
    ajustes.cache_clear()
    app.dependency_overrides[oficina.obtener_motor] = lambda: motor_app
    try:
        api = TestClient(app)
        titulos = {}
        for slug, _, usuarios, _ in CLIENTES:
            tok = emitir(_id("usuario", slug, usuarios[0][0]), _id("cliente", slug))
            r = api.get("/encargos", headers={"Authorization": f"Bearer {tok}"})
            assert r.status_code == 200
            titulos[slug] = {e["titulo"] for e in r.json()}
        ej = ejemplos()
        for slug in titulos:
            propios = {x["titulo"] for k in ("siniestros", "encargos") for x in ej[k] if x["cliente"] == slug}
            ajenos = {x["titulo"] for k in ("siniestros", "encargos") for x in ej[k] if x["cliente"] != slug}
            assert propios <= titulos[slug] and not (ajenos & titulos[slug])
    finally:
        app.dependency_overrides.clear()
        ajustes.cache_clear()


def test_vaciar_quita_solo_los_ejemplos(base, motor_admin, motor_app):
    cargar(base[0])
    atalaya = _id("cliente", "atalaya")
    with motor_admin.begin() as c:  # algo que ha creado una persona: no se toca
        c.execute(text("SELECT set_config('varios.cliente_id', :c, true)"), {"c": str(atalaya)})
        c.execute(text("INSERT INTO solicitud (id, cliente_id, autor_id, titulo) VALUES (gen_random_uuid(), :c, :a, "
                       "'Creado por una persona (inventado)')"),
                  {"c": atalaya, "a": _id("usuario", "atalaya", "tramitador@atalaya.invalid")})
    quitado = vaciar(base[0])
    assert quitado == {"polizas": 11, "solicitudes": 45}
    with sesion_de_cliente(motor_app, atalaya) as s:
        titulos = set(s.execute(text("SELECT titulo FROM solicitud")).scalars())
        assert "Creado por una persona (inventado)" in titulos
        assert not any(t.startswith(("Siniestro S", "Control A ")) for t in titulos)
        assert s.execute(text("SELECT count(*) FROM poliza")).scalar() == 0
    assert vaciar(base[0]) == {"polizas": 0, "solicitudes": 0}
    cargar(base[0])  # se puede volver a cargar
