"""N2 (M-040): cada agente y habilidad sirve a un proceso con métrica, o tiene propuesta de fusión o retirada."""

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "tools"))

import auditoria_gen  # noqa: E402
from org_data.agentes import A  # noqa: E402
from org_data.auditoria import AGENTES, HABILIDADES, PROCESOS_CLIENTE  # noqa: E402
from org_data.habilidades import H  # noqa: E402
from org_data.procesos import P  # noqa: E402

PROCESOS = {p["id"] for p in P} | set(PROCESOS_CLIENTE)


def _comprobar(entradas: dict, ids: set[str], que: str) -> list[str]:
    errores = []
    for i in sorted(ids - set(entradas)):
        errores.append(f"{que} «{i}» sin entrada en tools/org_data/auditoria.py: "
                       "dale proceso y métrica, o propón fusión o retirada")
    for i in sorted(set(entradas) - ids):
        errores.append(f"{que} «{i}» está en la auditoría pero ya no existe")
    for i, e in entradas.items():
        v = e["veredicto"]
        if v == "mantener":
            if not e["procesos"]:
                errores.append(f"{que} «{i}» se mantiene sin proceso")
            for p in e["procesos"]:
                if p not in PROCESOS:
                    errores.append(f"{que} «{i}»: proceso {p} inexistente")
            if not e["metrica"].strip():
                errores.append(f"{que} «{i}» se mantiene sin métrica")
        elif v == "fusionar":
            d = entradas.get(e["destino"])
            if not d or d["veredicto"] != "mantener":
                errores.append(f"{que} «{i}» se fusiona con «{e['destino']}», que no se mantiene")
            if not e["motivo"].strip():
                errores.append(f"{que} «{i}» se fusiona sin motivo")
        elif v == "retirar":
            if not e["motivo"].strip() or not e.get("reactivar", "").strip():
                errores.append(f"{que} «{i}» se retira sin motivo o sin condición para recuperarlo")
        else:
            errores.append(f"{que} «{i}»: veredicto desconocido {v}")
    return errores


def test_cada_agente_tiene_proceso_y_metrica_o_propuesta():
    assert _comprobar(AGENTES, {a["id"] for a in A}, "Agente") == []


def test_cada_habilidad_tiene_proceso_y_metrica_o_propuesta():
    assert _comprobar(HABILIDADES, {h["id"] for h in H}, "Habilidad") == []


def test_habilidad_que_se_queda_la_usa_un_agente_que_se_queda():
    duenos = {}
    for a in A:
        d = auditoria_gen.dueno_efectivo(a["id"])
        for h in a["habilidades"]:
            if d:
                duenos.setdefault(h, set()).add(d)
    huerfanas = [h for h, e in HABILIDADES.items() if e["veredicto"] == "mantener" and not duenos.get(h)]
    assert huerfanas == []


def test_ningun_proceso_se_queda_sin_agente():
    cubiertos = {p for e in AGENTES.values() for p in e["procesos"]}
    assert sorted(PROCESOS - cubiertos) == []


def test_documento_al_dia():
    esperado = auditoria_gen.generar()
    actual = (RAIZ / "docs" / "28-auditoria-agentes.md").read_text(encoding="utf-8")
    assert actual == esperado, "python3 tools/auditoria_gen.py"


def test_la_prueba_detecta_un_agente_nuevo_sin_proceso():
    ids = {a["id"] for a in A} | {"agente-nuevo"}
    errores = _comprobar(AGENTES, ids, "Agente")
    assert any("agente-nuevo" in e for e in errores)
