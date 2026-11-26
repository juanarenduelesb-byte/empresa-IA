"""E1: las seis plantillas de entregables comparten estructura (cabecera y apartados 1–7)."""

import re
from pathlib import Path

import pytest

DIR = Path(__file__).resolve().parents[1] / "knowledge" / "plantillas" / "entregables"
PLANTILLAS = sorted(DIR.glob("0[1-6]-*.md"))


def test_hay_seis_plantillas():
    assert len(PLANTILLAS) == 6


@pytest.mark.parametrize("p", PLANTILLAS, ids=lambda p: p.stem)
def test_misma_estructura(p):
    t = p.read_text(encoding="utf-8")
    assert "**0. Cabecera.**" in t
    apartados = [int(n) for n in re.findall(r"^## (\d)\. ", t, re.M)]
    assert apartados == [1, 2, 3, 4, 5, 6, 7], apartados
    assert re.search(r"^## 1\. Resumen", t, re.M) and re.search(r"^## 2\. Contexto", t, re.M)
    assert re.search(r"^## 4\. Decisiones", t, re.M)
    assert "confidencial" in t.lower()
