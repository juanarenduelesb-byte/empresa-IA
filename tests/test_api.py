"""Salud de la API (plan S1)."""

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
