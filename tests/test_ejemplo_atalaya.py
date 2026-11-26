"""N6: el ejemplo de propuesta de Atalaya está marcado como ficticio, no inventa precio y su puntuación se recalcula."""

import json
import re
from pathlib import Path

from varios.calidad.rubrica import Revision, evaluar

DIR = Path(__file__).resolve().parents[1] / "precedents" / "projects" / "caso-correduria-atalaya" / "entregables"
TEXTO = (DIR / "01-propuesta-diagnostico.md").read_text(encoding="utf-8")


def test_marcado_como_ficticio():
    assert "ficticio: true" in TEXTO and "FICTICIA" in TEXTO


def test_sin_precio_ni_importes_inventados():
    assert not re.search(r"\d[\d.,]*\s*(€|euros)", TEXTO)
    assert "[precio sin IVA" in TEXTO


def test_misma_estructura_que_la_plantilla():
    assert "**0. Cabecera.**" in TEXTO
    assert [int(n) for n in re.findall(r"^## (\d)\. ", TEXTO, re.M)] == [1, 2, 3, 4, 5, 6, 7]


def test_la_puntuacion_publicada_es_la_que_da_el_codigo():
    v = evaluar(Revision(**json.loads((DIR / "01-propuesta-diagnostico.revision.json").read_text(encoding="utf-8"))))
    md = (DIR / "01-propuesta-diagnostico.revision.md").read_text(encoding="utf-8")
    assert not v.cumple and v.media == 4.33
    assert "no cumple todavía" in md and "4,33" in md
