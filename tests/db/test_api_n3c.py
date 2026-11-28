"""N3c (resto de M-041): posponer, caducar y tareas en PostgreSQL, y decidir desde otra oficina.

Contra PostgreSQL real y con datos inventados. Las de acceso cruzado comprueban que otro cliente no ve ni toca nada.
"""

from datetime import UTC, datetime, timedelta

from sqlalchemy import text

from .test_api_oficina import _hasta_qa, _nuevo, api, gente, h  # noqa: F401 (fixtures)


def _pendiente(api, quien):  # noqa: F811
    enc = _nuevo(api, quien)
    _hasta_qa(api, quien, enc["id"])
    r = api.post(f"/encargos/{enc['id']}/aprobaciones", json={"motivo": "Listo"}, headers=h(quien))
    assert r.status_code == 201, r.text
    return enc, r.json()


def _vencer(motor_admin, cliente_id, aprobacion_id):
    """Simula que han pasado las 72 h: adelanta el plazo con la conexión de administrador."""
    with motor_admin.begin() as c:
        c.execute(text("SELECT set_config('varios.cliente_id', :c, true)"), {"c": str(cliente_id)})
        c.execute(text("UPDATE aprobacion SET caduca_en = now() - interval '1 minute' WHERE id = :i"),
                  {"i": aprobacion_id})


def _manana():
    return (datetime.now(UTC) + timedelta(days=1)).replace(microsecond=0).isoformat()


# --- posponer ---------------------------------------------------------------------------------------------------
def test_posponer_se_guarda_deja_auditoria_y_se_pierde_al_cambiar_de_estado(api, gente):  # noqa: F811
    autor, aprobador = gente["autor"], gente["aprobador"]
    enc, ap = _pendiente(api, autor)
    hasta = _manana()
    r = api.post(f"/encargos/{enc['id']}/posponer", json={"hasta": hasta, "motivo": "Lo miro mañana"},
                 headers=h(aprobador))
    assert r.status_code == 200, r.text
    # Sobrevive a recargar: otra petición (otra oficina) lo lee de la base.
    lista = {e["id"]: e for e in api.get("/encargos", headers=h(gente["aprobador2"])).json()}
    assert datetime.fromisoformat(lista[enc["id"]]["pospuesto_hasta"]) == datetime.fromisoformat(hasta)
    assert lista[enc["id"]]["estado"] == "PENDIENTE_APROBACION"  # posponer no decide nada
    assert lista[enc["id"]]["aprobacion"]["decision"] == "pendiente"
    ev = api.get(f"/encargos/{enc['id']}/auditoria", headers=h(autor)).json()
    assert ev[-1]["accion"] == "pospuesto" and ev[-1]["actor"] == str(aprobador[0])

    r = api.post(f"/aprobaciones/{ap['id']}/decision", json={"decision": "aprobada", "motivo": "Revisado"},
                 headers=h(aprobador))
    assert r.status_code == 200
    e = api.get(f"/encargos/{enc['id']}", headers=h(autor)).json()
    assert e["estado"] == "ENTREGADO" and e["pospuesto_hasta"] is None


def test_posponer_tiene_limites(api, gente):  # noqa: F811
    autor, aprobador, agente = gente["autor"], gente["aprobador"], gente["agente"]
    enc, _ = _pendiente(api, autor)
    url = f"/encargos/{enc['id']}/posponer"
    pasado = (datetime.now(UTC) - timedelta(hours=1)).isoformat()
    lejos = (datetime.now(UTC) + timedelta(days=30)).isoformat()
    assert api.post(url, json={"hasta": pasado}, headers=h(aprobador)).status_code == 409
    assert api.post(url, json={"hasta": lejos}, headers=h(aprobador)).status_code == 409
    assert api.post(url, json={"hasta": "2026-12-01T09:00:00"}, headers=h(aprobador)).status_code == 422  # sin zona
    assert api.post(url, json={"hasta": _manana()}, headers=h(agente)).status_code == 403  # un agente no pospone
    # Lo que no espera a nadie no se pospone.
    otro = _nuevo(api, autor)
    assert api.post(f"/encargos/{otro['id']}/posponer", json={"hasta": _manana()},
                    headers=h(aprobador)).status_code == 409
    assert api.get(f"/encargos/{enc['id']}", headers=h(autor)).json()["pospuesto_hasta"] is None


# --- caducar ----------------------------------------------------------------------------------------------------
def test_aprobacion_caducada_vuelve_como_pregunta_sin_aprobarse(api, gente, motor_admin):  # noqa: F811
    autor, aprobador = gente["autor"], gente["aprobador"]
    enc, ap = _pendiente(api, autor)
    plazo = datetime.fromisoformat(ap["caduca_en"]) - datetime.now(UTC)
    assert timedelta(hours=71) < plazo <= timedelta(hours=72)
    _vencer(motor_admin, autor[1], ap["id"])

    # Cualquier petición del cliente la caduca; decidirla ya no vale.
    r = api.post(f"/aprobaciones/{ap['id']}/decision", json={"decision": "aprobada", "motivo": "Tarde"},
                 headers=h(aprobador))
    assert r.status_code == 403 and "caduc" in r.json()["detail"]
    e = {x["id"]: x for x in api.get("/encargos", headers=h(autor)).json()}[enc["id"]]
    assert e["estado"] == "ESCALADO"
    assert e["aprobacion"]["decision"] == "caducada" and e["aprobacion"]["aprobador_id"] is None
    ev = api.get(f"/encargos/{enc['id']}/auditoria", headers=h(autor)).json()
    assert [x["accion"] for x in ev[-2:]] == ["aprobacion_caducada", "mover"]
    assert {x["actor"] for x in ev[-2:]} == {"sistema:caducidad"}
    assert ev[-1]["antes"] == "PENDIENTE_APROBACION" and ev[-1]["despues"] == "ESCALADO"
    assert not any(x["despues"] == "ENTREGADO" for x in ev)
    # Desde ESCALADO una persona decide cómo seguir; un agente no (encargo.json, repaso del 28/11).
    r = api.post(f"/encargos/{enc['id']}/estado", json={"a": "PLANIFICADO", "motivo": "Sigo yo"},
                 headers=h(gente["agente"]))
    assert r.status_code == 403
    assert api.get(f"/encargos/{enc['id']}", headers=h(autor)).json()["estado"] == "ESCALADO"
    # La persona puede volver a pedir el OK por el camino normal.
    for a in ("PLANIFICADO", "EN_EJECUCION", "EN_QA"):
        assert api.post(f"/encargos/{enc['id']}/estado", json={"a": a, "motivo": "Sigue"},
                        headers=h(autor)).status_code == 200
    assert api.post(f"/encargos/{enc['id']}/aprobaciones", json={}, headers=h(autor)).status_code == 201


def test_la_caducidad_no_es_un_cambio_libre(api, gente):  # noqa: F811
    autor, aprobador = gente["autor"], gente["aprobador"]
    enc, _ = _pendiente(api, autor)
    r = api.post(f"/encargos/{enc['id']}/estado", json={"a": "ESCALADO", "motivo": "Me lo salto"},
                 headers=h(aprobador))
    assert r.status_code == 409
    assert api.get(f"/encargos/{enc['id']}", headers=h(autor)).json()["estado"] == "PENDIENTE_APROBACION"


def test_un_cliente_no_caduca_ni_ve_lo_de_otro(api, gente, motor_admin):  # noqa: F811
    autor, b = gente["autor"], gente["b"]
    enc, ap = _pendiente(api, autor)
    _vencer(motor_admin, autor[1], ap["id"])
    assert enc["id"] not in {e["id"] for e in api.get("/encargos", headers=h(b)).json()}
    with motor_admin.connect() as c:
        c.execute(text("SELECT set_config('varios.cliente_id', :c, false)"), {"c": str(autor[1])})
        decision = c.execute(text("SELECT decision FROM aprobacion WHERE id = :i"), {"i": ap["id"]}).scalar()
    assert decision == "pendiente"  # la petición del cliente B no ha tocado la aprobación de A
    assert api.post(f"/encargos/{enc['id']}/posponer", json={"hasta": _manana()}, headers=h(b)).status_code == 404


# --- decidir desde otra oficina ---------------------------------------------------------------------------------
def test_otra_oficina_del_mismo_cliente_decide_y_quien_la_pidio_nunca(api, gente):  # noqa: F811
    aprobador, aprobador2, b = gente["aprobador"], gente["aprobador2"], gente["b"]
    enc, ap = _pendiente(api, aprobador)  # pide quien también tiene rol de aprobación
    # La otra oficina (otro token) ve la aprobación pendiente en la lista y la puede decidir.
    lista = {e["id"]: e for e in api.get("/encargos", headers=h(aprobador2)).json()}
    assert lista[enc["id"]]["aprobacion"]["id"] == ap["id"]
    assert lista[enc["id"]]["aprobacion"]["solicitada_por"] == str(aprobador[0])
    cuerpo = {"decision": "aprobada", "motivo": "Revisado en otra oficina"}
    assert api.post(f"/aprobaciones/{ap['id']}/decision", json=cuerpo, headers=h(aprobador)).status_code == 403
    assert api.post(f"/aprobaciones/{ap['id']}/decision", json=cuerpo, headers=h(b)).status_code == 404
    r = api.post(f"/aprobaciones/{ap['id']}/decision", json=cuerpo, headers=h(aprobador2))
    assert r.status_code == 200 and r.json()["aprobador_id"] == str(aprobador2[0])


# --- tareas -----------------------------------------------------------------------------------------------------
def _con_tarea(api, quien):  # noqa: F811
    enc = _nuevo(api, quien)
    for a in ("EN_CLASIFICACION", "PLANIFICADO", "EN_EJECUCION"):
        assert api.post(f"/encargos/{enc['id']}/estado", json={"a": a, "motivo": "Paso"},
                        headers=h(quien)).status_code == 200
    r = api.post(f"/encargos/{enc['id']}/tareas",
                 json={"titulo": "Pieza: resumen (inventado)", "responsable": "redactor", "clave_idempotencia": "p1"},
                 headers=h(quien))
    assert r.status_code == 201
    return enc, r.json()


def test_el_estado_de_las_tareas_se_guarda_con_auditoria(api, gente):  # noqa: F811
    autor = gente["autor"]
    enc, t = _con_tarea(api, autor)
    assert t["estado"] == "queued"
    for a in ("running", "succeeded"):
        r = api.post(f"/tareas/{t['id']}/estado", json={"a": a, "motivo": f"Oficina: {a}"}, headers=h(autor))
        assert r.status_code == 200, r.text
    assert api.post(f"/tareas/{t['id']}/estado", json={"a": "running", "motivo": "x"},
                    headers=h(autor)).status_code == 409  # succeeded es final
    lista = {e["id"]: e for e in api.get("/encargos", headers=h(autor)).json()}
    assert [x["estado"] for x in lista[enc["id"]]["tareas"]] == ["succeeded"]
    ev = [e for e in api.get(f"/encargos/{enc['id']}/auditoria", headers=h(autor)).json()
          if e["accion"] == "tarea_mover"]
    assert [(e["antes"], e["despues"]) for e in ev] == [("queued", "running"), ("running", "succeeded")]


def test_una_tarea_que_pide_aprobacion_no_la_aprueba_quien_la_pidio(api, gente):  # noqa: F811
    aprobador, aprobador2, agente = gente["aprobador"], gente["aprobador2"], gente["agente"]
    _, t = _con_tarea(api, aprobador)
    url = f"/tareas/{t['id']}/estado"
    for a in ("running", "needs_approval"):
        assert api.post(url, json={"a": a, "motivo": a}, headers=h(aprobador)).status_code == 200
    ok = {"a": "succeeded", "motivo": "Visto"}
    assert api.post(url, json=ok, headers=h(aprobador)).status_code == 403
    assert api.post(url, json=ok, headers=h(agente)).status_code == 403
    assert api.post(url, json=ok, headers=h(gente["autor"])).status_code == 403  # sin rol
    assert api.post(url, json=ok, headers=h(aprobador2)).status_code == 200


def test_otro_cliente_no_toca_las_tareas(api, gente):  # noqa: F811
    _, t = _con_tarea(api, gente["autor"])
    r = api.post(f"/tareas/{t['id']}/estado", json={"a": "running", "motivo": "x"}, headers=h(gente["b"]))
    assert r.status_code == 404
    assert all(not e["tareas"] for e in api.get("/encargos", headers=h(gente["b"])).json())


def test_las_tareas_no_cambian_cuando_el_encargo_ya_no_trabaja(api, gente):  # noqa: F811
    autor = gente["autor"]
    enc, t = _con_tarea(api, autor)
    assert api.post(f"/encargos/{enc['id']}/estado", json={"a": "EN_QA", "motivo": "QA"},
                    headers=h(autor)).status_code == 200
    r = api.post(f"/tareas/{t['id']}/estado", json={"a": "running", "motivo": "tarde"}, headers=h(autor))
    assert r.status_code == 409


def test_el_autor_del_encargo_no_da_por_buena_una_tarea_aunque_la_pida_otro(api, gente):  # noqa: F811
    """Repaso de N3c: la misma regla que en las aprobaciones (decidir_aprobacion), también en las tareas."""
    aprobador, aprobador2 = gente["aprobador"], gente["aprobador2"]
    _, t = _con_tarea(api, aprobador)  # autor del encargo: aprobador
    url = f"/tareas/{t['id']}/estado"
    for a in ("running", "needs_approval"):
        assert api.post(url, json={"a": a, "motivo": a}, headers=h(aprobador2)).status_code == 200
    ok = {"a": "succeeded", "motivo": "Visto"}
    assert api.post(url, json=ok, headers=h(aprobador)).status_code == 403


def test_una_tarea_que_pide_aprobacion_no_se_da_por_hecha_dando_un_rodeo(api, gente):  # noqa: F811
    """Repaso de N3c (tanda 23:30): de needs_approval se puede volver a running, y de running a succeeded no hacía
    falta aprobador, así que quien la puso a esperar (o un agente) la daba por hecha en dos pasos. Ahora toda salida
    de needs_approval es de un aprobador, como las de PENDIENTE_APROBACION (Guía v1.4 §4), y una tarea que pidió
    aprobación solo acaba en succeeded aprobándola."""
    aprobador, aprobador2, agente = gente["aprobador"], gente["aprobador2"], gente["agente"]
    _, t = _con_tarea(api, aprobador)
    url = f"/tareas/{t['id']}/estado"
    for a in ("running", "needs_approval"):
        assert api.post(url, json={"a": a, "motivo": a}, headers=h(aprobador)).status_code == 200
    for quien in (aprobador, agente):
        for a in ("running", "cancelled"):
            assert api.post(url, json={"a": a, "motivo": "rodeo"}, headers=h(quien)).status_code == 403, (quien, a)
    # Otro aprobador la devuelve a trabajar: después no se da por hecha sin volver a pedir aprobación.
    assert api.post(url, json={"a": "running", "motivo": "Falta un dato"}, headers=h(aprobador2)).status_code == 200
    for quien in (aprobador, aprobador2):
        assert api.post(url, json={"a": "succeeded", "motivo": "x"}, headers=h(quien)).status_code == 409
    assert api.post(url, json={"a": "needs_approval", "motivo": "Corregido"}, headers=h(aprobador)).status_code == 200
    assert api.post(url, json={"a": "succeeded", "motivo": "Visto"}, headers=h(aprobador2)).status_code == 200


def test_reabrir_da_nueva_version_y_un_cerrado_pide_autorizacion(api, gente):  # noqa: F811
    """Guía v1.4 §4: reabrir es con nueva versión y, desde CERRADO, con autorización (repaso del 28/11)."""
    autor, aprobador, agente = gente["autor"], gente["aprobador"], gente["agente"]
    enc, ap = _pendiente(api, autor)
    ok = {"decision": "aprobada", "motivo": "Revisado"}
    assert api.post(f"/aprobaciones/{ap['id']}/decision", json=ok, headers=h(aprobador)).status_code == 200
    url = f"/encargos/{enc['id']}/estado"
    assert api.post(url, json={"a": "CERRADO", "motivo": "Aceptado"}, headers=h(autor)).status_code == 200
    v = api.get(f"/encargos/{enc['id']}", headers=h(autor)).json()["version"]
    for quien in (autor, agente):  # sin rol de aprobación, o sin ser persona
        assert api.post(url, json={"a": "REABIERTO", "motivo": "Lo reabro"}, headers=h(quien)).status_code == 403
    e = api.get(f"/encargos/{enc['id']}", headers=h(autor)).json()
    assert e["estado"] == "CERRADO" and e["version"] == v
    assert api.post(url, json={"a": "REABIERTO", "motivo": "Piden un cambio"}, headers=h(aprobador)).status_code == 200
    assert api.get(f"/encargos/{enc['id']}", headers=h(autor)).json()["version"] == v + 1
