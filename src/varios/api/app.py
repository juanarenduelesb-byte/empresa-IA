"""API mínima (plan S1). De momento solo salud; la autenticación llega en S3."""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import text

from varios import __version__
from varios.config import ajustes
from varios.db.sesion import motor

app = FastAPI(title="Varios", version=__version__)


@app.get("/health")
def salud() -> JSONResponse:
    estado = {"estado": "ok", "version": __version__, "entorno": ajustes().entorno, "base_de_datos": "sin configurar"}
    if ajustes().database_url:
        try:
            with motor().connect() as c:
                c.execute(text("SELECT 1"))
            estado["base_de_datos"] = "ok"
        except Exception:  # noqa: BLE001 - la salud informa, no falla
            estado["base_de_datos"] = "error"
    codigo = 503 if estado["base_de_datos"] == "error" else 200
    if codigo != 200:
        estado["estado"] = "degradado"
    return JSONResponse(estado, status_code=codigo)
