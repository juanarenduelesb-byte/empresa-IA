"""C1: los 20 siniestros inventados cumplen el esquema y las reglas fijas dan el resultado esperado."""

import json
from pathlib import Path

import pytest

from varios.seguros.apertura import Caso, Poliza, dominio, evaluar

RAIZ = Path(__file__).resolve().parents[1]
DIR = RAIZ / "processes" / "referencia-seguros-apertura-siniestros" / "casos"
CARTERA = {p["numero"]: Poliza(**p) for p in json.loads((DIR / "cartera.json").read_text(encoding="utf-8"))["polizas"]}
CASOS = [Caso(**c) for c in json.loads((DIR / "casos.json").read_text(encoding="utf-8"))["casos"]]


def test_hay_20_casos_con_id_unico():
    assert len(CASOS) == 20
    assert len({c.id for c in CASOS}) == 20


def test_el_esquema_publicado_esta_al_dia():
    publicado = json.loads((DIR / "esquema.json").read_text(encoding="utf-8"))
    assert publicado == Caso.model_json_schema(), "Regenera: python -m varios.seguros.esquema"


def test_todas_las_excepciones_del_catalogo_tienen_al_menos_un_caso():
    catalogo = {e["id"] for e in dominio()["excepciones"]}
    cubiertas = {x for c in CASOS for x in c.esperado.excepciones}
    assert cubiertas <= catalogo
    assert catalogo - cubiertas == set()


def test_hay_casos_limpios_y_cada_accion_aparece():
    assert any(not c.esperado.excepciones for c in CASOS)
    assert {c.esperado.accion for c in CASOS} == {"preparar_parte", "pedir_documentacion",
                                                 "trasladar_a_aseguradora", "pasar_a_persona"}


def test_las_polizas_citadas_existen_salvo_que_falten():
    for c in CASOS:
        assert c.hechos.poliza_numero is None or c.hechos.poliza_numero in CARTERA, c.id


@pytest.mark.parametrize("caso", CASOS, ids=[c.id for c in CASOS])
def test_reglas_dan_el_resultado_esperado(caso):
    r = evaluar(caso.hechos, caso.fecha_recepcion, CARTERA)
    e = caso.esperado
    assert (r.excepciones, r.accion, r.tambien, r.anotar_libro_siniestros) == (
        e.excepciones, e.accion, e.tambien, e.anotar_libro_siniestros), r.detalle


def test_nunca_hay_accion_externa_sin_persona():
    for c in CASOS:
        r = evaluar(c.hechos, c.fecha_recepcion, CARTERA)
        assert r.requiere_aprobacion_humana


def test_el_plazo_sale_del_dominio_y_no_del_codigo(monkeypatch):
    c = next(c for c in CASOS if c.id == "S02")
    d = json.loads(json.dumps(dominio()))
    next(p for p in d["plazos"] if p["id"] == "PL-COMUNICACION")["dias"] = 30
    monkeypatch.setattr("varios.seguros.apertura.dominio", lambda: d)
    assert "EX-01" not in evaluar(c.hechos, c.fecha_recepcion, CARTERA).excepciones
