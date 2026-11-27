"""Configuración por variables de entorno (prefijo VARIOS_) o archivo .env. Nunca secretos en el código."""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Ajustes(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="VARIOS_", extra="ignore")

    entorno: str = "local"
    # Conexión de la aplicación: usuario sin privilegios, sujeto a RLS.
    database_url: str | None = None
    # Conexión para migraciones y cargas de conocimiento común (propietario de las tablas).
    database_url_admin: str | None = None
    # Firma de los tokens de acceso (provisional hasta el proveedor de identidad de S3, D-028). Nunca en el código.
    jwt_secreto: str | None = None
    jwt_emisor: str = "varios-local"
    jwt_audiencia: str = "varios-api"
    # N3c: una aprobación sin decidir caduca a las 72 h (plazo propuesto en N4; lo fijan los socios) y un encargo se
    # puede posponer como mucho 7 días (propuesta: que nada quede apartado sin que nadie lo vuelva a ver).
    aprobacion_caduca_h: int = 72
    posponer_max_dias: int = 7


@lru_cache
def ajustes() -> Ajustes:
    return Ajustes()
