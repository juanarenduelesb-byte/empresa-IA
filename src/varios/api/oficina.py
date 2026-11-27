"""Encargos, tareas y aprobaciones de la oficina sobre PostgreSQL (N3a y N3c, M-041).

Cada petición: token verificado → usuario activo del cliente del token → una transacción con ese cliente fijado (RLS)
→ el repositorio aplica las reglas y deja un evento de auditoría por cambio. Cualquier `cliente_id` en el cuerpo se
ignora. Lo de otro cliente responde 404, igual que lo que no existe (OWASP IDOR).
"""

from __future__ import annotations

import uuid
from collections.abc import Iterator
from contextlib import contextmanager
from functools import lru_cache
from typing import Annotated, Literal

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from sqlalchemy import Engine, select

from varios.db.modelos import RIESGOS, Usuario
from varios.db.repositorio import MAQUINA, MAQUINA_TAREA, NoEncontrado, Repositorio
from varios.db.sesion import motor, sesion_de_cliente
from varios.procesos.motor import AprobacionInvalida, Identidad, TransicionInvalida

from .identidad import NoAutenticado, verificar

router = APIRouter(tags=["oficina"])
_portador = HTTPBearer(auto_error=False)


@lru_cache
def _motor_por_defecto() -> Engine:
    return motor()


def obtener_motor() -> Engine:
    """Se sustituye en las pruebas por el motor de la base de pruebas."""
    return _motor_por_defecto()


class Credencial(BaseModel):
    usuario_id: uuid.UUID
    cliente_id: uuid.UUID


def credencial(cred: Annotated[HTTPAuthorizationCredentials | None, Depends(_portador)]) -> Credencial:
    """Solo verifica el token. El usuario se comprueba en la misma transacción que el trabajo (`abrir`)."""
    if cred is None:
        raise _no_autenticado()
    try:
        usuario_id, cliente_id = verificar(cred.credentials)
    except NoAutenticado:
        raise _no_autenticado() from None
    return Credencial(usuario_id=usuario_id, cliente_id=cliente_id)


def _no_autenticado() -> HTTPException:
    return HTTPException(status.HTTP_401_UNAUTHORIZED, "No autenticado", headers={"WWW-Authenticate": "Bearer"})


class Contexto:
    """Una transacción por petición con el cliente del token fijado. Si algo falla, no se guarda nada."""

    def __init__(self, c: Annotated[Credencial, Depends(credencial)],
                 engine: Annotated[Engine, Depends(obtener_motor)]) -> None:
        self.c, self.engine = c, engine

    def _repositorio(self, s) -> Repositorio:
        q = select(Usuario).where(Usuario.id == self.c.usuario_id, Usuario.cliente_id == self.c.cliente_id)
        u = s.scalar(q)
        if u is None or not u.activo:
            raise _no_autenticado()
        quien = Identidad(usuario=str(u.id), tenant=str(self.c.cliente_id), roles=frozenset(u.roles or []),
                          persona=u.es_persona)
        return Repositorio(s, quien)

    @contextmanager
    def abrir(self) -> Iterator[Repositorio]:
        # Primero, en su propia transacción, caducan las aprobaciones vencidas de este cliente (N3c). Va aparte para
        # que una petición que falla (por ejemplo, decidir lo que acaba de caducar) no deshaga la caducidad.
        with sesion_de_cliente(self.engine, self.c.cliente_id) as s:
            self._repositorio(s).caducar_vencidas()
        with sesion_de_cliente(self.engine, self.c.cliente_id) as s:
            yield self._repositorio(s)


def errores_de_dominio(app) -> None:
    """Traduce las reglas del repositorio a HTTP. La transacción ya se ha deshecho al llegar aquí."""
    from fastapi.responses import JSONResponse

    # Solo errores del dominio, con mensajes escritos por nosotros. Un ValueError cualquiera no se traduce: su texto
    # podría enseñar detalles internos (hoja de FastAPI de OWASP). La validación de entrada la hace Pydantic (422).
    codigos = {NoEncontrado: 404, AprobacionInvalida: 403, TransicionInvalida: 409}
    for clase, codigo in codigos.items():
        def manejar(_peticion, exc, codigo=codigo, clase=clase):
            detalle = "No encontrado" if clase is NoEncontrado else str(exc)
            return JSONResponse({"detail": detalle}, status_code=codigo)
        app.add_exception_handler(clase, manejar)


Ctx = Annotated[Contexto, Depends()]


# --- Esquemas: lo que entra no trae cliente ni autor; si los trae, se ignoran (extra="ignore"). ---
class Entrada(BaseModel):
    model_config = ConfigDict(extra="ignore")


class EncargoNuevo(Entrada):
    titulo: str = Field(min_length=1, max_length=300)
    descripcion: str = ""
    riesgo: Literal[RIESGOS] = "bajo"  # type: ignore[valid-type]


class CambioEstado(Entrada):
    a: str
    motivo: str = Field(min_length=1)
    clave_idempotencia: str | None = Field(default=None, max_length=200)


class TareaNueva(Entrada):
    titulo: str = Field(min_length=1, max_length=300)
    responsable: str = Field(min_length=1, max_length=200)
    clave_idempotencia: str | None = Field(default=None, max_length=200)


class PeticionAprobacion(Entrada):
    objeto: str = Field(default="entregable", max_length=200)
    motivo: str = ""


class Posposicion(Entrada):
    hasta: AwareDatetime
    motivo: str = Field(default="", max_length=500)


class CambioTarea(Entrada):
    a: str
    motivo: str = Field(min_length=1)
    clave_idempotencia: str | None = Field(default=None, max_length=200)


class Decision(Entrada):
    decision: Literal["aprobada", "rechazada"]
    motivo: str = Field(min_length=1)
    # Solo cuenta al rechazar: devolver para rehacer (por defecto) o rechazar del todo (Guía v1.4 §4).
    si_rechaza: Literal["RETRABAJO", "RECHAZADO"] = "RETRABAJO"


def _iso(d) -> str | None:
    return d.isoformat() if d else None


def _encargo(s, aprobacion=None, tareas=None) -> dict:
    """El encargo y, en la lista, su última aprobación y sus tareas: la oficina se rehace solo con esto (N3c)."""
    e = {"id": str(s.id), "titulo": s.titulo, "descripcion": s.descripcion, "estado": s.estado, "riesgo": s.riesgo,
         "version": s.version, "autor_id": str(s.autor_id), "creado_en": s.creado_en.isoformat(),
         "pospuesto_hasta": _iso(s.pospuesto_hasta)}
    if aprobacion is not None or tareas is not None:
        e["aprobacion"] = _aprobacion(aprobacion) if aprobacion is not None else None
        e["tareas"] = [_tarea(t) for t in tareas or []]
    return e


def _tarea(t) -> dict:
    return {"id": str(t.id), "encargo_id": str(t.solicitud_id), "titulo": t.titulo, "responsable": t.responsable,
            "estado": t.estado, "clave_idempotencia": t.clave_idempotencia}


def _aprobacion(a) -> dict:
    return {"id": str(a.id), "encargo_id": str(a.solicitud_id), "objeto": a.objeto, "version": a.version,
            "solicitada_por": a.solicitada_por, "aprobador_id": str(a.aprobador_id) if a.aprobador_id else None,
            "decision": a.decision, "motivo": a.motivo, "creado_en": _iso(a.creado_en),
            "caduca_en": _iso(a.caduca_en), "decidida_en": _iso(a.decidida_en)}


@router.get("/definiciones/encargo")
def definicion_encargo(c: Annotated[Credencial, Depends(credencial)]) -> dict:
    """Transiciones de encargo.json, para que la oficina no copie la tabla (la fuente sigue siendo el JSON)."""
    return {"id": MAQUINA.id, "version": MAQUINA.version, "inicial": MAQUINA.inicial,
            "transiciones": {k: sorted(v) for k, v in MAQUINA.transiciones.items()}}


@router.post("/encargos", status_code=201)
def crear_encargo(datos: EncargoNuevo, ctx: Ctx) -> dict:
    with ctx.abrir() as repo:
        sol = repo.crear_solicitud(uuid.UUID(repo.quien.usuario), datos.titulo, datos.descripcion, datos.riesgo)
        return _encargo(sol)


@router.get("/encargos")
def listar_encargos(ctx: Ctx) -> list[dict]:
    with ctx.abrir() as repo:
        aprob, tareas = repo.ultimas_aprobaciones(), {}
        for t in repo.tareas_del_cliente():
            tareas.setdefault(t.solicitud_id, []).append(t)
        return [_encargo(s, aprob.get(s.id), tareas.get(s.id, [])) for s in repo.solicitudes()]


@router.get("/encargos/{encargo_id}")
def ver_encargo(encargo_id: uuid.UUID, ctx: Ctx) -> dict:
    with ctx.abrir() as repo:
        return _encargo(repo.solicitud(encargo_id))


@router.post("/encargos/{encargo_id}/estado")
def cambiar_estado(encargo_id: uuid.UUID, datos: CambioEstado, ctx: Ctx) -> dict:
    with ctx.abrir() as repo:
        return _encargo(repo.mover_solicitud(encargo_id, datos.a, datos.motivo, datos.clave_idempotencia))


@router.post("/encargos/{encargo_id}/posponer")
def posponer(encargo_id: uuid.UUID, datos: Posposicion, ctx: Ctx) -> dict:
    with ctx.abrir() as repo:
        return _encargo(repo.posponer(encargo_id, datos.hasta, datos.motivo))


@router.post("/tareas/{tarea_id}/estado")
def cambiar_estado_tarea(tarea_id: uuid.UUID, datos: CambioTarea, ctx: Ctx) -> dict:
    with ctx.abrir() as repo:
        return _tarea(repo.mover_tarea(tarea_id, datos.a, datos.motivo, datos.clave_idempotencia))


@router.get("/definiciones/tarea")
def definicion_tarea(c: Annotated[Credencial, Depends(credencial)]) -> dict:
    return {"id": MAQUINA_TAREA.id, "version": MAQUINA_TAREA.version, "inicial": MAQUINA_TAREA.inicial,
            "transiciones": {k: sorted(v) for k, v in MAQUINA_TAREA.transiciones.items()}}


@router.post("/encargos/{encargo_id}/tareas", status_code=201)
def crear_tarea(encargo_id: uuid.UUID, datos: TareaNueva, ctx: Ctx) -> dict:
    with ctx.abrir() as repo:
        t, _ = repo.crear_tarea(encargo_id, datos.titulo, datos.responsable, datos.clave_idempotencia)
        return _tarea(t)


@router.get("/encargos/{encargo_id}/tareas")
def listar_tareas(encargo_id: uuid.UUID, ctx: Ctx) -> list[dict]:
    with ctx.abrir() as repo:
        return [_tarea(t) for t in repo.tareas(encargo_id)]


@router.post("/encargos/{encargo_id}/aprobaciones", status_code=201)
def pedir_aprobacion(encargo_id: uuid.UUID, datos: PeticionAprobacion, ctx: Ctx) -> dict:
    with ctx.abrir() as repo:
        return _aprobacion(repo.pedir_aprobacion(encargo_id, datos.objeto, datos.motivo))


@router.get("/encargos/{encargo_id}/aprobaciones")
def listar_aprobaciones(encargo_id: uuid.UUID, ctx: Ctx) -> list[dict]:
    with ctx.abrir() as repo:
        return [_aprobacion(a) for a in repo.aprobaciones(encargo_id)]


@router.post("/aprobaciones/{aprobacion_id}/decision")
def decidir(aprobacion_id: uuid.UUID, datos: Decision, ctx: Ctx) -> dict:
    with ctx.abrir() as repo:
        return _aprobacion(repo.decidir_aprobacion(aprobacion_id, datos.decision == "aprobada", datos.motivo,
                                                     datos.si_rechaza))


@router.get("/encargos/{encargo_id}/auditoria")
def auditoria(encargo_id: uuid.UUID, ctx: Ctx) -> list[dict]:
    with ctx.abrir() as repo:
        return [{"id": e.id, "momento": e.momento.isoformat(), "actor": e.actor, "accion": e.accion, "objeto": e.objeto,
                 "antes": e.antes, "despues": e.despues, "motivo": e.motivo} for e in repo.eventos(encargo_id)]
