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


@lru_cache
def ajustes() -> Ajustes:
    return Ajustes()
