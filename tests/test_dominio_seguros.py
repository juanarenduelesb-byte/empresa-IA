"""Paquete de dominio de seguros (B2): coherencia entre dominio.json, los Markdown y el registro de fuentes."""

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PAQ = RAIZ / "knowledge" / "sectores" / "seguros"
sys.path.insert(0, str(RAIZ / "tools"))

from org_data.fuentes import FUENTES  # noqa: E402

IDS = {f["id"] for f in FUENTES}
D = json.loads((PAQ / "dominio.json").read_text(encoding="utf-8"))


def test_todo_cita_una_fuente_del_registro():
    citadas = [p["fuente"] for p in D["plazos"]] + [c["fuente"] for c in D["campos_libro_siniestros"]]
    citadas += [f for e in D["excepciones"] for f in e["fuentes"]]
    assert citadas and not [c for c in citadas if c not in IDS]


def test_plazos_tienen_duracion_y_norma():
    for p in D["plazos"]:
        assert any(k in p for k in ("dias", "meses", "anos")), p["id"]
        assert p["norma"] and p["desde"], p["id"]


def test_excepciones_siempre_acaban_en_una_persona_o_en_la_aseguradora():
    for e in D["excepciones"]:
        assert e["decide"].split(";")[0] in {"persona", "aseguradora"}, e["id"]
        assert e["base"] in {"con_fuente", "hipotesis"}, e["id"]
        assert "decide" not in e["ia"].lower() or "no" in e["ia"].lower(), e["id"]


def test_ids_de_excepcion_unicos_y_en_el_markdown():
    ids = [e["id"] for e in D["excepciones"]]
    assert len(ids) == len(set(ids))
    md = (PAQ / "excepciones.md").read_text(encoding="utf-8")
    for e in D["excepciones"]:
        assert f"## {e['id']} · {e['nombre']}" in md


def test_glosario_y_terminos_coinciden():
    md = (PAQ / "glosario-siniestros.md").read_text(encoding="utf-8")
    en_md = set(re.findall(r"\(`([a-z0-9-]+)`\)", md)) - {"terminos"}
    assert en_md == set(D["terminos"])


def test_las_fuentes_legales_del_paquete_son_oficiales_o_lo_dicen():
    # Una obligación legal citada en el paquete con autoridad media debe decir en su versión o nota de dónde sale.
    usadas = {f for e in D["excepciones"] for f in e["fuentes"]} | {p["fuente"] for p in D["plazos"]}
    for f in FUENTES:
        if f["id"] in usadas and f["tipo"] == "obligacion-legal":
            assert any(d in f["url"].lower() for d in ("boe.es", "eur-lex.europa.eu")) or f["estado"] == "draft", f["id"]
