"""Máquina de estados del encargo, cargada de processes/definitions/encargo.json.

La fuente de verdad es el JSON (Guía v1.4 §4 más los huecos marcados como añadidos).
El código no repite la tabla: la lee y la valida.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]


def _definiciones() -> Path:
    """En el repositorio, junto al código; instalado (imagen de Docker), en la carpeta de trabajo."""
    junto = RAIZ / "processes" / "definitions"
    return junto if junto.is_dir() else Path.cwd() / "processes" / "definitions"


DEFINICIONES = _definiciones()


@dataclass(frozen=True)
class MaquinaEstados:
    id: str
    version: str
    inicial: str
    finales: frozenset[str]
    estados: frozenset[str]
    transiciones: dict[str, frozenset[str]]

    def permitida(self, de: str, a: str) -> bool:
        return a in self.transiciones.get(de, frozenset())

    def siguientes(self, de: str) -> frozenset[str]:
        return self.transiciones.get(de, frozenset())


def cargar(nombre: str = "encargo", carpeta: Path = DEFINICIONES) -> MaquinaEstados:
    datos = json.loads((carpeta / f"{nombre}.json").read_text(encoding="utf-8"))
    tabla: dict[str, set[str]] = {}
    for t in datos["transiciones"]:
        tabla.setdefault(t["de"], set()).update(t["a"])
    estados = frozenset(datos["estados"])
    for de, destinos in tabla.items():
        desconocidos = ({de} | destinos) - estados
        if desconocidos:
            raise ValueError(f"Estados no declarados en {nombre}: {sorted(desconocidos)}")
    return MaquinaEstados(
        id=datos["id"],
        version=datos["version"],
        inicial=datos["inicial"],
        finales=frozenset(datos["finales"]),
        estados=estados,
        transiciones={k: frozenset(v) for k, v in tabla.items()},
    )


def cargar_objeto(nombre: str, carpeta: Path = DEFINICIONES) -> MaquinaEstados:
    """Máquina de un objeto de objetos.json (tarea, instancia de proceso…). Sin estados finales declarados: son
    finales los que no tienen salida."""
    datos = json.loads((carpeta / "objetos.json").read_text(encoding="utf-8"))
    obj = next((o for o in datos["objetos"] if o["id"] == nombre), None)
    if obj is None:
        raise ValueError(f"Objeto desconocido en objetos.json: {nombre}")
    tabla: dict[str, set[str]] = {}
    for t in obj["transiciones"]:
        tabla.setdefault(t["de"], set()).update(t["a"])
    estados = frozenset(obj["estados"])
    for de, destinos in tabla.items():
        desconocidos = ({de} | destinos) - estados
        if desconocidos:
            raise ValueError(f"Estados no declarados en {nombre}: {sorted(desconocidos)}")
    return MaquinaEstados(
        id=obj["id"],
        version=datos["version"],
        inicial=obj["inicial"],
        finales=frozenset(e for e in estados if e not in tabla),
        estados=estados,
        transiciones={k: frozenset(v) for k, v in tabla.items()},
    )
