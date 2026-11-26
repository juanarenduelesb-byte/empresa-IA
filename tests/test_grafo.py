"""Pruebas del grafo de conocimiento (D-018)."""
import json
import os
import subprocess
import sys

import grafo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_louvain_separa_dos_grupos():
    W = {}
    for grupo in ("abc", "xyz"):
        for u in grupo:
            W.setdefault(u, {})
            for v in grupo:
                if u != v:
                    W[u][v] = 1.0
    W["c"]["x"] = W["x"]["c"] = 0.1
    com = grafo.louvain(W)
    assert com["a"] == com["b"] == com["c"]
    assert com["x"] == com["y"] == com["z"]
    assert com["a"] != com["x"]


def test_intermediacion_del_puente():
    W = {"a": {"b": 1}, "b": {"a": 1, "c": 1}, "c": {"b": 1}}
    bc = grafo.intermediacion(W)
    assert bc["b"] > bc["a"] == bc["c"] == 0


def test_limpio_quita_codigo_y_enlaces():
    t = grafo.limpio("Texto ```mermaid\nflowchart rectangulo\n``` y [enlace](docs/x.md) `ruta/x.md` <svg>z</svg>")
    assert "rectangulo" not in t and "docs/x.md" not in t and "svg" not in t and "enlace" in t


def _brain(tmp_path):
    out = tmp_path / "brain.json"
    subprocess.run(
        [sys.executable, os.path.join(ROOT, "tools", "brain_build.py"), str(out)],
        check=True, cwd=ROOT, capture_output=True,
    )
    return json.loads(out.read_text(encoding="utf-8"))


def test_grafo_valido_y_estable(tmp_path):
    b1 = _brain(tmp_path)
    g = b1["graph"]
    n = len(g["nodos"])
    nchunks = len(b1["chunks"])
    for a, c, r, s, t in g["aristas"]:
        for x in (a, c):
            assert (0 <= x < n) or (0 <= -1 - x < nchunks)
        assert g["rels"][r] != "parte_de"
        tag = g["tags"][t]
        assert (
            (tag == "EXTRACTADA" and s == 100)
            or (tag == "INFERIDA" and s in (65, 75, 85))
            or (tag == "AMBIGUA" and s == 50)
        )
    ids = {x[0] for x in g["nodos"]}
    for d in ("D-011", "P01", "ag:ceo", "hab:marca-varios", "esp:ceo-digital"):
        assert d in ids
    b2 = _brain(tmp_path)
    b1.pop("built")
    b2.pop("built")
    assert b1 == b2, "el cerebro debe ser determinista"


def test_el_informe_no_entra_en_el_cerebro(tmp_path):
    b = _brain(tmp_path)
    assert not any(d["p"].startswith("knowledge/grafo/") for d in b["docs"])
    assert os.path.exists(os.path.join(ROOT, "knowledge", "grafo", "INFORME.md"))
