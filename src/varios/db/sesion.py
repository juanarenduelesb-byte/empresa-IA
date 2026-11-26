"""Sesiones con el cliente fijado. Toda consulta de la aplicación pasa por `sesion_de_cliente`.

El cliente sale de la identidad autenticada (varios.procesos.motor.Identidad), nunca de la petición. Se fija con
`set_config(..., true)`, que dura solo la transacción: al terminar, la conexión vuelve al pool sin cliente.
"""

from __future__ import annotations

import uuid
from collections.abc import Iterator
from contextlib import contextmanager

from sqlalchemy import Engine, create_engine, text
from sqlalchemy.orm import Session, sessionmaker

from varios.config import ajustes


def motor(url: str | None = None) -> Engine:
    url = url or ajustes().database_url
    if not url:
        raise RuntimeError("Falta VARIOS_DATABASE_URL.")
    return create_engine(url, pool_pre_ping=True)


@contextmanager
def sesion_de_cliente(engine: Engine, cliente_id: uuid.UUID | str) -> Iterator[Session]:
    fabrica = sessionmaker(bind=engine, expire_on_commit=False)
    with fabrica() as s, s.begin():
        s.execute(text("SELECT set_config('varios.cliente_id', :c, true)"), {"c": str(uuid.UUID(str(cliente_id)))})
        yield s
