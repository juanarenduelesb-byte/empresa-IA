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


def test_los_secretos_se_buscan_donde_pueden_estar(tmp_path):
    """Repaso del 28/11: el patrón no veía las claves de Anthropic (sk-ant-api03-…, la que usará S4) y solo se miraban
    siete extensiones fuera de archive/: una clave en un .sh, en .env.example, en el Dockerfile o en archive/ pasaba.
    Las claves de prueba se montan por partes para que el propio repositorio no lleve ninguna."""
    anthropic = "sk-" + "ant-api03-" + "Ab1_" * 10
    github = "gh" + "p_" + "a1B2" * 9
    casos = {"tools/arranque.sh": f"export ANTHROPIC_API_KEY={anthropic}\n", ".env.example": f"TOKEN={github}\n",
             "Dockerfile": f"ENV CLAVE={anthropic}\n", "archive/viejo.md": f"clave: {anthropic}\n",
             "alembic.ini": "-----BEGIN RSA " + "PRIVATE KEY-----\n"}
    for rel, texto in casos.items():
        (tmp_path / rel).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / rel).write_text(texto, encoding="utf-8")
    (tmp_path / ".git").mkdir()
    (tmp_path / ".git" / "config").write_text(anthropic, encoding="utf-8")  # la carpeta de git no se mira
    (tmp_path / "limpio.md").write_text("sk-ant- sin clave y ghp_corto", encoding="utf-8")
    assert check_repo.secretos(tmp_path) == sorted(casos)


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
