"""C3: la rúbrica decide con la regla de D-019 y cada plantilla tiene su lista de comprobación."""

import pytest

from varios.calidad.rubrica import DIR, Problema, Revision, evaluar, listas, rubrica

IDS = [c["id"] for c in rubrica()["criterios"]]


def todo_ok(tipo):
    puntos = listas()["comunes"] + listas()["tipos"][tipo]["puntos"]
    return {p["id"]: True for p in puntos}


def rev(puntos, tipo="acta", problemas=(), comprobaciones=None):
    return Revision(tipo=tipo, puntos=dict(zip(IDS, puntos, strict=True)), problemas=list(problemas),
                    comprobaciones=todo_ok(tipo) if comprobaciones is None else comprobaciones)


def test_seis_criterios_con_descriptores():
    assert IDS == ["criterio", "completo", "veracidad", "coherencia", "nivel", "forma"]
    for c in rubrica()["criterios"]:
        assert set(c["niveles"]) == {"1", "2", "4", "5"}


def test_cada_plantilla_tiene_su_lista_y_existe():
    tipos = listas()["tipos"]
    assert len(tipos) == 6
    for t in tipos.values():
        assert (DIR / t["plantilla"]).exists() and t["puntos"]


def test_cumple_con_todo_bien():
    assert evaluar(rev([5, 5, 5, 4, 5, 4])).cumple


@pytest.mark.parametrize("puntos", [[5, 5, 5, 5, 5, 3], [4, 4, 4, 4, 4, 5]])
def test_no_cumple_con_un_criterio_bajo_o_media_baja(puntos):
    assert not evaluar(rev(puntos)).cumple


def test_un_problema_medio_bloquea_aunque_las_notas_sean_altas():
    p = Problema(criterio="veracidad", gravedad="medio", donde="3.2", como_arreglarlo="citar la medición")
    assert not evaluar(rev([5] * 6, problemas=[p])).cumple


def test_un_problema_leve_no_bloquea():
    p = Problema(criterio="forma", gravedad="leve", donde="2", como_arreglarlo="acortar")
    assert evaluar(rev([5] * 6, problemas=[p])).cumple


def test_la_lista_de_comprobacion_bloquea():
    c = todo_ok("informe-diagnostico")
    c["ID2"] = False
    v = evaluar(rev([5] * 6, tipo="informe-diagnostico", comprobaciones=c))
    assert not v.cumple and "ID2" in v.motivos[0]


def test_puntuar_mal_es_un_error():
    with pytest.raises(ValueError):
        evaluar(Revision(tipo="acta", puntos={"criterio": 5}))
    with pytest.raises(ValueError):
        evaluar(rev([6, 5, 5, 5, 5, 5]))


def test_un_punto_de_otra_lista_no_cuenta_como_cumplido():
    import pytest

    from varios.calidad.rubrica import Revision, evaluar, rubrica

    puntos = {c["id"]: 5 for c in rubrica()["criterios"]}
    with pytest.raises(ValueError, match="no son de la lista"):
        evaluar(Revision(tipo="propuesta-diagnostico", puntos=puntos, comprobaciones={"PD9": True}))
    with pytest.raises(ValueError, match="no son de la lista"):
        evaluar(Revision(tipo="propuesta-diagnostico", puntos=puntos, comprobaciones={"ID1": True}))
