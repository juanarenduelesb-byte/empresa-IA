import json

from varios.procesos.estados import DEFINICIONES, cargar


def test_carga_coincide_con_el_json():
    m = cargar()
    datos = json.loads((DEFINICIONES / "encargo.json").read_text(encoding="utf-8"))
    for t in datos["transiciones"]:
        for a in t["a"]:
            assert m.permitida(t["de"], a)


def test_finales_sin_salida_salvo_reabrir():
    m = cargar()
    for f in m.finales:
        assert m.siguientes(f) <= {"REABIERTO"}


def test_todo_estado_no_final_tiene_salida():
    m = cargar()
    for e in m.estados - m.finales:
        assert m.siguientes(e), e


def test_transicion_no_declarada_no_permitida():
    m = cargar()
    assert not m.permitida("RECIBIDO", "ENTREGADO")
    assert not m.permitida("EN_EJECUCION", "CERRADO")
