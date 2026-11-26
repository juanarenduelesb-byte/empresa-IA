"""N3a (M-041): la oficina guarda en la API. Pruebas contra PostgreSQL real, con datos inventados."""

import uuid
from datetime import UTC, datetime, timedelta

import jwt
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text

from varios.api import oficina
from varios.api.app import app
from varios.api.identidad import emitir
from varios.config import ajustes

SECRETO = "solo-pruebas-" + "x" * 40


@pytest.fixture()
def api(monkeypatch, motor_app):
    monkeypatch.setenv("VARIOS_JWT_SECRETO", SECRETO)
    ajustes.cache_clear()
    app.dependency_overrides[oficina.obtener_motor] = lambda: motor_app
    yield TestClient(app)
    app.dependency_overrides.clear()
    ajustes.cache_clear()


@pytest.fixture()
def gente(motor_admin, dos_clientes):
    """Cliente A: autor sin rol, aprobador, otro aprobador y un agente con rol (no persona). Cliente B: su usuario."""
    ca, _ = dos_clientes["A"]
    cb, ub = dos_clientes["B"]
    p = {}
    with motor_admin.begin() as c:
        c.execute(text("SELECT set_config('varios.cliente_id', :c, true)"), {"c": str(ca)})
        for nombre, roles, persona in (("autor", "[]", True), ("aprobador", '["aprobador"]', True),
                                       ("aprobador2", '["aprobador"]', True), ("agente", '["aprobador"]', False)):
            uid = uuid.uuid4()
            c.execute(text("INSERT INTO usuario (id, cliente_id, email, nombre, roles, es_persona) "
                           "VALUES (:u, :c, :e, :n, CAST(:r AS json), :p)"),
                      {"u": uid, "c": ca, "e": f"{nombre}@a.invalid", "n": f"{nombre} (inventado)", "r": roles,
                       "p": persona})
            p[nombre] = (uid, ca)
    p["b"] = (ub, cb)
    return p


def h(persona) -> dict:
    return {"Authorization": f"Bearer {emitir(*persona)}"}


def _hasta_qa(api, quien, encargo_id):
    for a in ("EN_CLASIFICACION", "PLANIFICADO"):
        r = api.post(f"/encargos/{encargo_id}/estado", json={"a": a, "motivo": f"Paso a {a}"}, headers=h(quien))
        assert r.status_code == 200, r.text
    r = api.post(f"/encargos/{encargo_id}/tareas", json={"titulo": "Redactar borrador", "responsable": "prop"},
                 headers=h(quien))
    assert r.status_code == 201, r.text
    for a in ("EN_EJECUCION", "EN_QA"):
        r = api.post(f"/encargos/{encargo_id}/estado", json={"a": a, "motivo": f"Paso a {a}"}, headers=h(quien))
        assert r.status_code == 200, r.text


def _nuevo(api, quien, **extra):
    r = api.post("/encargos", json={"titulo": "Propuesta de diagnóstico (caso inventado)", "riesgo": "medio", **extra},
                 headers=h(quien))
    assert r.status_code == 201, r.text
    return r.json()


def test_de_encargo_a_entregado_con_auditoria_en_cada_paso(api, gente):
    autor, aprobador = gente["autor"], gente["aprobador"]
    enc = _nuevo(api, autor)
    assert enc["estado"] == "RECIBIDO"
    _hasta_qa(api, autor, enc["id"])
    r = api.post(f"/encargos/{enc['id']}/aprobaciones", json={"motivo": "Listo para revisar"}, headers=h(autor))
    assert r.status_code == 201, r.text
    ap = r.json()
    assert ap["decision"] == "pendiente" and ap["solicitada_por"] == str(autor[0])
    assert api.get(f"/encargos/{enc['id']}", headers=h(autor)).json()["estado"] == "PENDIENTE_APROBACION"

    r = api.post(f"/aprobaciones/{ap['id']}/decision", json={"decision": "aprobada", "motivo": "Revisado"},
                 headers=h(aprobador))
    assert r.status_code == 200, r.text
    assert r.json()["aprobador_id"] == str(aprobador[0])
    assert api.get(f"/encargos/{enc['id']}", headers=h(autor)).json()["estado"] == "ENTREGADO"

    eventos = api.get(f"/encargos/{enc['id']}/auditoria", headers=h(autor)).json()
    assert [e["accion"] for e in eventos] == ["alta", "mover", "mover", "tarea_alta", "mover", "mover", "mover",
                                              "aprobacion_pedida", "aprobacion_decidida", "mover"]
    assert eventos[-1]["despues"] == "ENTREGADO" and eventos[-1]["actor"] == str(aprobador[0])
    assert eventos[-3]["actor"] == str(autor[0])


def test_nadie_aprueba_lo_que_ha_pedido_el_mismo(api, gente):
    aprobador, aprobador2, autor = gente["aprobador"], gente["aprobador2"], gente["autor"]
    enc = _nuevo(api, aprobador)  # el autor tiene rol de aprobador
    _hasta_qa(api, aprobador, enc["id"])
    ap = api.post(f"/encargos/{enc['id']}/aprobaciones", json={}, headers=h(aprobador)).json()
    r = api.post(f"/aprobaciones/{ap['id']}/decision", json={"decision": "aprobada", "motivo": "Me lo apruebo"},
                 headers=h(aprobador))
    assert r.status_code == 403
    # Sin rol de aprobación tampoco, aunque no sea el autor.
    r = api.post(f"/aprobaciones/{ap['id']}/decision", json={"decision": "aprobada", "motivo": "x"}, headers=h(autor))
    assert r.status_code == 403
    r = api.post(f"/aprobaciones/{ap['id']}/decision", json={"decision": "aprobada", "motivo": "Revisado"},
                 headers=h(aprobador2))
    assert r.status_code == 200


def test_el_autor_del_encargo_no_aprueba_aunque_lo_pida_otro(api, gente):
    aprobador, aprobador2 = gente["aprobador"], gente["aprobador2"]
    enc = _nuevo(api, aprobador)
    _hasta_qa(api, aprobador, enc["id"])
    ap = api.post(f"/encargos/{enc['id']}/aprobaciones", json={}, headers=h(aprobador2)).json()
    r = api.post(f"/aprobaciones/{ap['id']}/decision", json={"decision": "aprobada", "motivo": "x"},
                 headers=h(aprobador))
    assert r.status_code == 403


def test_un_agente_no_aprueba(api, gente):
    autor, agente = gente["autor"], gente["agente"]
    enc = _nuevo(api, autor)
    _hasta_qa(api, autor, enc["id"])
    ap = api.post(f"/encargos/{enc['id']}/aprobaciones", json={}, headers=h(autor)).json()
    r = api.post(f"/aprobaciones/{ap['id']}/decision", json={"decision": "aprobada", "motivo": "x"}, headers=h(agente))
    assert r.status_code == 403


def test_rechazar_devuelve_a_retrabajo_y_sube_la_version(api, gente):
    autor, aprobador = gente["autor"], gente["aprobador"]
    enc = _nuevo(api, autor)
    _hasta_qa(api, autor, enc["id"])
    ap = api.post(f"/encargos/{enc['id']}/aprobaciones", json={}, headers=h(autor)).json()
    r = api.post(f"/aprobaciones/{ap['id']}/decision", json={"decision": "rechazada", "motivo": "Falta la fuente"},
                 headers=h(aprobador))
    assert r.status_code == 200
    e = api.get(f"/encargos/{enc['id']}", headers=h(autor)).json()
    assert e["estado"] == "RETRABAJO" and e["version"] == 2
    r = api.post(f"/aprobaciones/{ap['id']}/decision", json={"decision": "aprobada", "motivo": "x"},
                 headers=h(aprobador))
    assert r.status_code == 403  # ya decidida


def test_el_cliente_del_cuerpo_se_ignora(api, gente):
    autor, b = gente["autor"], gente["b"]
    enc = _nuevo(api, autor, cliente_id=str(b[1]), autor_id=str(b[0]))
    assert enc["autor_id"] == str(autor[0])
    assert api.get(f"/encargos/{enc['id']}", headers=h(autor)).status_code == 200
    assert api.get(f"/encargos/{enc['id']}", headers=h(b)).status_code == 404


def test_acceso_cruzado_entre_clientes(api, gente):
    autor, b = gente["autor"], gente["b"]
    enc = _nuevo(api, autor)
    _hasta_qa(api, autor, enc["id"])
    ap = api.post(f"/encargos/{enc['id']}/aprobaciones", json={}, headers=h(autor)).json()
    assert api.get("/encargos", headers=h(b)).json() == []
    for metodo, ruta, cuerpo in (
        ("get", f"/encargos/{enc['id']}", None),
        ("get", f"/encargos/{enc['id']}/tareas", None),
        ("get", f"/encargos/{enc['id']}/auditoria", None),
        ("get", f"/encargos/{enc['id']}/aprobaciones", None),
        ("post", f"/encargos/{enc['id']}/estado", {"a": "CANCELADO", "motivo": "intruso"}),
        ("post", f"/encargos/{enc['id']}/tareas", {"titulo": "intrusa", "responsable": "x"}),
        ("post", f"/aprobaciones/{ap['id']}/decision", {"decision": "aprobada", "motivo": "intruso"}),
    ):
        r = getattr(api, metodo)(ruta, headers=h(b), **({"json": cuerpo} if cuerpo else {}))
        assert r.status_code == 404, (ruta, r.status_code)
    # Un token que mezcla el usuario de A con el cliente B no vale.
    assert api.get("/encargos", headers=h((autor[0], b[1]))).status_code == 401
    assert api.get(f"/encargos/{enc['id']}", headers=h(autor)).json()["estado"] == "PENDIENTE_APROBACION"


def test_tokens_no_validos(api, gente):
    autor = gente["autor"]
    assert api.get("/encargos").status_code == 401
    ahora = datetime.now(UTC)
    base = {"sub": str(autor[0]), "cliente": str(autor[1]), "iss": "varios-local", "aud": "varios-api"}
    malos = [
        jwt.encode({**base, "exp": ahora - timedelta(minutes=1)}, SECRETO, algorithm="HS256"),  # caducado
        jwt.encode({**base, "exp": ahora + timedelta(minutes=5)}, "otro-secreto-" + "y" * 40, algorithm="HS256"),
        jwt.encode({**base, "exp": ahora + timedelta(minutes=5), "aud": "otra"}, SECRETO, algorithm="HS256"),
        jwt.encode(base, SECRETO, algorithm="HS256"),  # sin caducidad
        jwt.encode({**base, "exp": ahora + timedelta(minutes=5)}, None, algorithm="none"),
        "no-es-un-token",
    ]
    for t in malos:
        assert api.get("/encargos", headers={"Authorization": f"Bearer {t}"}).status_code == 401


def test_transicion_no_permitida_no_deja_rastro(api, gente):
    autor = gente["autor"]
    enc = _nuevo(api, autor)
    for a in ("ENTREGADO", "EN_QA", "PENDIENTE_APROBACION"):
        r = api.post(f"/encargos/{enc['id']}/estado", json={"a": a, "motivo": "atajo"}, headers=h(autor))
        assert r.status_code == 409, a
    assert [e["accion"] for e in api.get(f"/encargos/{enc['id']}/auditoria", headers=h(autor)).json()] == ["alta"]
    # Pedir aprobación fuera de QA tampoco se guarda a medias.
    r = api.post(f"/encargos/{enc['id']}/aprobaciones", json={}, headers=h(autor))
    assert r.status_code == 409
    assert api.get(f"/encargos/{enc['id']}/aprobaciones", headers=h(autor)).json() == []


def test_idempotencia(api, gente):
    autor = gente["autor"]
    enc = _nuevo(api, autor)
    cuerpo = {"a": "EN_CLASIFICACION", "motivo": "Clasificar", "clave_idempotencia": f"k-{enc['id']}"}
    assert api.post(f"/encargos/{enc['id']}/estado", json=cuerpo, headers=h(autor)).status_code == 200
    assert api.post(f"/encargos/{enc['id']}/estado", json=cuerpo, headers=h(autor)).status_code == 200
    api.post(f"/encargos/{enc['id']}/estado", json={"a": "PLANIFICADO", "motivo": "Plan"}, headers=h(autor))
    tarea = {"titulo": "Borrador", "responsable": "prop", "clave_idempotencia": f"t-{enc['id']}"}
    t1 = api.post(f"/encargos/{enc['id']}/tareas", json=tarea, headers=h(autor)).json()
    t2 = api.post(f"/encargos/{enc['id']}/tareas", json=tarea, headers=h(autor)).json()
    assert t1["id"] == t2["id"]
    acciones = [e["accion"] for e in api.get(f"/encargos/{enc['id']}/auditoria", headers=h(autor)).json()]
    assert acciones == ["alta", "mover", "mover", "tarea_alta"]
