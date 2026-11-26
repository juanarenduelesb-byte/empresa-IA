"""Identidad autenticada de cada petición (D-028, propuesta; provisional hasta el proveedor de identidad de S3).

- El token es un JWT firmado (HS256) con `sub` (usuario), `cliente` (tenant), `exp`, `iss` y `aud`, como recomienda
  la hoja de seguridad de FastAPI de OWASP: algoritmo fijo, campos obligatorios y secreto fuera del código.
- El cliente sale del token verificado, nunca del cuerpo ni de la URL. Los roles y si es persona salen de la base de
  datos, no del token: un token no puede darse a sí mismo el rol de aprobador.
- Con el proveedor de identidad real (OIDC) cambia solo `verificar`: el resto de la API no se entera.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime, timedelta

import jwt

from varios.config import ajustes

ALGORITMO = "HS256"


class NoAutenticado(Exception):
    pass


def _secreto() -> str:
    s = ajustes().jwt_secreto
    if not s or len(s) < 32:
        raise NoAutenticado("Falta VARIOS_JWT_SECRETO (al menos 32 caracteres)")
    return s


def emitir(usuario_id: uuid.UUID | str, cliente_id: uuid.UUID | str, minutos: int = 60) -> str:
    """Emite un token. Solo para desarrollo y pruebas: en producción lo emite el proveedor de identidad."""
    ahora = datetime.now(UTC)
    a = ajustes()
    datos = {"sub": str(usuario_id), "cliente": str(cliente_id), "iat": ahora,
             "exp": ahora + timedelta(minutes=minutos), "iss": a.jwt_emisor, "aud": a.jwt_audiencia}
    return jwt.encode(datos, _secreto(), algorithm=ALGORITMO)


def verificar(token: str) -> tuple[uuid.UUID, uuid.UUID]:
    """Devuelve (usuario_id, cliente_id) de un token válido o lanza NoAutenticado."""
    a = ajustes()
    try:
        datos = jwt.decode(token, _secreto(), algorithms=[ALGORITMO], audience=a.jwt_audiencia, issuer=a.jwt_emisor,
                           options={"require": ["exp", "iss", "aud", "sub", "cliente"]})
        return uuid.UUID(datos["sub"]), uuid.UUID(datos["cliente"])
    except (jwt.PyJWTError, ValueError, KeyError) as e:
        raise NoAutenticado("Token no válido") from e
