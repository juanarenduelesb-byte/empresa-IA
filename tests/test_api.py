"""Salud de la API (plan S1)."""

from pathlib import Path

from fastapi.testclient import TestClient

from varios.api.app import app
from varios.config import ajustes


def test_salud_sin_base_de_datos(monkeypatch):
    monkeypatch.delenv("VARIOS_DATABASE_URL", raising=False)
    ajustes.cache_clear()
    r = TestClient(app).get("/health")
    assert r.status_code == 200 and r.json()["base_de_datos"] == "sin configurar"


def test_salud_con_base_caida(monkeypatch):
    monkeypatch.setenv("VARIOS_DATABASE_URL", "postgresql+psycopg://nadie@127.0.0.1:1/nada")
    ajustes.cache_clear()
    r = TestClient(app).get("/health")
    assert r.status_code == 503 and r.json()["estado"] == "degradado"
    ajustes.cache_clear()


def test_definicion_del_encargo_con_token(monkeypatch):
    import json
    import uuid
    from pathlib import Path

    from varios.api.identidad import emitir

    monkeypatch.setenv("VARIOS_JWT_SECRETO", "solo-pruebas-" + "x" * 40)
    ajustes.cache_clear()
    c = TestClient(app)
    assert c.get("/definiciones/encargo").status_code == 401
    r = c.get("/definiciones/encargo", headers={"Authorization": f"Bearer {emitir(uuid.uuid4(), uuid.uuid4())}"})
    assert r.status_code == 200
    fuente = json.loads((Path(__file__).resolve().parents[1] / "processes/definitions/encargo.json").read_text())
    esperado = {}
    for t in fuente["transiciones"]:
        esperado.setdefault(t["de"], set()).update(t["a"])
    assert {k: set(v) for k, v in r.json()["transiciones"].items()} == esperado
    ajustes.cache_clear()


def test_no_firma_con_el_secreto_de_ejemplo(monkeypatch):
    """Copiar .env.example sin cambiar el secreto no deja una API que acepte tokens firmados con un valor público."""
    import uuid

    import pytest

    from varios.api.identidad import SECRETO_DE_EJEMPLO, NoAutenticado, emitir

    ejemplo = Path(__file__).resolve().parents[1] / ".env.example"
    assert f"VARIOS_JWT_SECRETO={SECRETO_DE_EJEMPLO}" in ejemplo.read_text(encoding="utf-8")
    monkeypatch.setenv("VARIOS_JWT_SECRETO", SECRETO_DE_EJEMPLO)
    ajustes.cache_clear()
    with pytest.raises(NoAutenticado):
        emitir(uuid.uuid4(), uuid.uuid4())
    c = TestClient(app)
    assert c.get("/definiciones/encargo", headers={"Authorization": "Bearer x.y.z"}).status_code == 401
    ajustes.cache_clear()


def test_la_oficina_se_sirve_desde_la_api():
    c = TestClient(app)
    r = c.get("/oficina/")
    assert r.status_code == 200 and '<script src="api.js"></script>' in r.text
    assert c.get("/oficina/api.js").status_code == 200
    assert c.get("/oficina", follow_redirects=False).status_code == 307
