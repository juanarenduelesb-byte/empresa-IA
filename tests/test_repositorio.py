import json
import subprocess
import sys
from pathlib import Path

import check_repo

RAIZ = Path(__file__).resolve().parents[1]


def test_enlaces_internos_existen():
    assert check_repo.enlaces_rotos() == []


def test_fichas_de_proceso_completas():
    assert check_repo.fichas_incompletas() == []


def test_fuentes_citadas_existen():
    assert check_repo.fuentes_inexistentes() == []


def test_sin_secretos():
    assert check_repo.secretos() == []


def test_generado_al_dia():
    r = subprocess.run([sys.executable, "tools/org_gen.py", "--check"], cwd=RAIZ, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_contratos_json_validos():
    for p in (RAIZ / "integrations" / "contracts").glob("*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        assert d["required"] and set(d["required"]) <= set(d["properties"]), p.name
    enc = json.loads((RAIZ / "integrations" / "contracts" / "encargo.schema.json").read_text(encoding="utf-8"))
    assert "identidad" in enc["properties"]["tenant"]["description"]


def test_navegacion_apunta_a_archivos_existentes():
    nav = json.loads((RAIZ / "knowledge" / "navigation.json").read_text(encoding="utf-8"))
    texto = json.dumps(nav, ensure_ascii=False)
    import re

    for ruta in set(re.findall(r'"((?:knowledge|processes|precedents|docs)/[^"#]+\.(?:md|json))"', texto)):
        assert (RAIZ / ruta).exists(), ruta
