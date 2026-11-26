"""N1 (M-045): cada proceso tiene nivel A0–A4 y criterio; nada externo, legal, financiero o contractual pasa de A2."""

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "tools"))

import autonomia_gen as g  # noqa: E402
from org_data.auditoria import PROCESOS_CLIENTE  # noqa: E402
from org_data.procesos import P  # noqa: E402

DATOS = g.cargar()
PROCESOS = DATOS["procesos"]


def test_estan_los_38_procesos_y_el_de_referencia():
    ids = [p["id"] for p in PROCESOS]
    assert len(ids) == len(set(ids))
    assert set(ids) == {p["id"] for p in P} | set(PROCESOS_CLIENTE)


def test_niveles_validos_y_dentro_del_techo():
    for p in PROCESOS:
        for campo in ("actual", "objetivo_febrero", "tope"):
            assert p[campo] in DATOS["niveles"], (p["id"], campo)
        assert g.nivel(p["actual"]) <= g.nivel(p["objetivo_febrero"]) <= g.nivel(p["tope"]), p["id"]


def errores_sensibles(procesos) -> list[str]:
    malos = []
    for p in procesos:
        if set(p["categorias"]) & g.CATEGORIAS_SENSIBLES:
            for campo in ("actual", "objetivo_febrero", "tope"):
                if g.nivel(p[campo]) > g.nivel(g.TOPE_SENSIBLE):
                    malos.append(f"{p['id']}.{campo}={p[campo]}")
    return malos


def test_lo_externo_legal_financiero_o_contractual_no_pasa_de_A2():
    assert errores_sensibles(PROCESOS) == []


def test_la_prueba_detecta_un_proceso_legal_en_A3():
    malo = dict(PROCESOS[0], categorias=["legal"], actual="A0", objetivo_febrero="A1", tope="A3")
    assert errores_sensibles([malo]) == [f"{malo['id']}.tope=A3"]


def test_categorias_conocidas():
    for p in PROCESOS:
        assert set(p["categorias"]) <= g.CATEGORIAS_SENSIBLES, p["id"]


def test_la_aprobacion_humana_no_pasa_de_A1():
    p10 = next(p for p in PROCESOS if p["id"] == "P10")
    assert g.nivel(p10["tope"]) <= 1


def errores_techo_humano(procesos, humanos) -> list[str]:
    return [p["id"] for p in procesos if humanos.get(p["id"]) and g.nivel(p["tope"]) >= 4]


def test_un_proceso_con_pasos_humanos_no_llega_a_A4():
    """A4 es «autónomo con muestreo»: no cabe si el catálogo deja pasos a una persona (P15 y P35 lo tenían, 26/11)."""
    assert errores_techo_humano(PROCESOS, g.pasos_humanos()) == []


def test_la_prueba_detecta_un_paso_humano_en_A4():
    malo = dict(PROCESOS[0], tope="A4")
    assert errores_techo_humano([malo], {malo["id"]: ["Decidir"]}) == [malo["id"]]


def test_cada_proceso_tiene_criterio_para_subir_y_bajar():
    for p in PROCESOS:
        assert p["subir"]["metrica"].strip() and p["subir"]["periodo"].strip() and p["subir"]["umbral"].strip(), p["id"]
        assert p["bajar"].strip(), p["id"]


def test_documento_al_dia():
    actual = (RAIZ / "docs" / "29-autonomia.md").read_text(encoding="utf-8")
    assert actual == g.generar(), "python3 tools/autonomia_gen.py"
