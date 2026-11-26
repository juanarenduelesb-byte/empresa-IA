"""API (plan S1 y N3a): salud y oficina (encargos, tareas y aprobaciones). Identidad provisional en D-028."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text

from varios import __version__
from varios.config import ajustes
from varios.db.sesion import motor

from .oficina import errores_de_dominio, router

app = FastAPI(title="Varios", version=__version__)
app.include_router(router)
errores_de_dominio(app)


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


def _carpeta_oficina() -> Path | None:
    """La oficina (HTML estático) se sirve desde la API para que use la misma dirección y no haga falta CORS."""
    for c in (Path(__file__).resolve().parents[3] / "oficina", Path.cwd() / "oficina"):
        if (c / "index.html").is_file():
            return c
    return None


_oficina = _carpeta_oficina()
if _oficina:
    @app.get("/oficina", include_in_schema=False)
    def _a_la_oficina() -> RedirectResponse:
        return RedirectResponse("/oficina/")

    app.mount("/oficina", StaticFiles(directory=_oficina, html=True), name="oficina")
