#!/usr/bin/env python3
"""PostgreSQL desechable para pruebas y desarrollo sin Docker.

Busca initdb en el sistema, crea un clúster en una carpeta temporal y lo arranca en un puerto libre.
Como root, ejecuta PostgreSQL con el usuario del sistema `postgres` (initdb no se deja ejecutar como root).
Uso en consola: python3 tools/pg_local.py  → imprime las URL y espera hasta Ctrl+C.
"""

from __future__ import annotations

import glob
import os
import shutil
import socket
import subprocess
import tempfile
import time
from dataclasses import dataclass


def _bin() -> str | None:
    if shutil.which("initdb"):
        return os.path.dirname(shutil.which("initdb"))
    candidatos = sorted(glob.glob("/usr/lib/postgresql/*/bin/initdb"))
    return os.path.dirname(candidatos[-1]) if candidatos else None


def disponible() -> bool:
    return _bin() is not None


def _puerto() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


@dataclass
class Cluster:
    carpeta: str
    puerto: int
    bin: str
    como: list[str]

    def url(self, usuario: str = "postgres", base: str = "postgres") -> str:
        return f"postgresql+psycopg://{usuario}@127.0.0.1:{self.puerto}/{base}"

    def parar(self) -> None:
        subprocess.run([*self.como, f"{self.bin}/pg_ctl", "-D", self.carpeta, "-m", "immediate", "stop"],
                       capture_output=True)
        shutil.rmtree(os.path.dirname(self.carpeta), ignore_errors=True)


def arrancar() -> Cluster:
    b = _bin()
    if not b:
        raise RuntimeError("No hay PostgreSQL instalado (initdb no encontrado).")
    raiz = tempfile.mkdtemp(prefix="varios-pg-")
    datos = os.path.join(raiz, "datos")
    como: list[str] = []
    if os.geteuid() == 0:
        como = ["runuser", "-u", "postgres", "--"]
        shutil.chown(raiz, "postgres")
        os.chmod(raiz, 0o755)
    subprocess.run([*como, f"{b}/initdb", "-D", datos, "-U", "postgres", "-A", "trust", "-E", "UTF8",
                    "--locale=C.UTF-8"], check=True, capture_output=True)
    puerto = _puerto()
    subprocess.run([*como, f"{b}/pg_ctl", "-D", datos, "-w", "-l", os.path.join(raiz, "log.txt"), "-o",
                    f"-p {puerto} -k {raiz} -c listen_addresses=127.0.0.1 -c fsync=off", "start"],
                   check=True, capture_output=True)
    return Cluster(datos, puerto, b, como)


if __name__ == "__main__":
    c = arrancar()
    print("Administrador:", c.url())
    print("Pulsa Ctrl+C para parar.")
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        c.parar()
