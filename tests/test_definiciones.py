import json

from varios.procesos.definiciones import procesos_catalogo, validar, validar_archivo
from varios.procesos.estados import DEFINICIONES


def base():
    return json.loads((DEFINICIONES / "ciclo-encargo.json").read_text(encoding="utf-8"))


def test_ciclo_encargo_valido():
    assert validar_archivo() == []


def test_catalogo_tiene_38_procesos():
    assert procesos_catalogo() == {f"P{i:02d}" for i in range(1, 39)}


def test_detecta_proceso_inexistente_y_tipo():
    d = base()
    d["tareas"][0]["proceso"] = "P99"
    d["tareas"][1]["tipo"] = "magia"
    err = validar(d, procesos_catalogo())
    assert any("P99" in e for e in err) and any("magia" in e for e in err)


def test_detecta_tarea_inalcanzable():
    d = base()
    d["tareas"].append(dict(d["tareas"][0], id="suelta"))
    assert any("inalcanzables" in e for e in validar(d, procesos_catalogo()))


def test_exige_no_reintentar_seguridad():
    d = base()
    d["errores"]["no_reintentar"] = ["permanente"]
    assert any("no reintentables" in e for e in validar(d, procesos_catalogo()))


def test_aprobaciones_declaradas_con_rol():
    d = base()
    aprob = {t["id"]: t.get("aprobacion") for t in d["tareas"]}
    assert aprob["aprobar"]["rol"] and "alto" in aprob["aprobar"]["si_riesgo"]
