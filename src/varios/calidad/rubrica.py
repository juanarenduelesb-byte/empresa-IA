"""Regla fija de la rúbrica de entregables (D-019, tarea C3).

Un revisor (persona o modelo) puntúa cada criterio de 1 a 5 y anota problemas con su gravedad.
Este módulo decide si el entregable cumple; el revisor no puede decidirlo por su cuenta.
Criterios, umbrales, bloqueantes y listas por tipo están en knowledge/plantillas/entregables/.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

RAIZ = Path(__file__).resolve().parents[3]
DIR = RAIZ / "knowledge" / "plantillas" / "entregables"


class Estricto(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Problema(Estricto):
    criterio: str
    gravedad: Literal["grave", "medio", "leve"]
    donde: str
    como_arreglarlo: str


class Revision(Estricto):
    tipo: str = Field(description="Id de la lista de comprobación del entregable")
    puntos: dict[str, int]
    problemas: list[Problema] = []
    comprobaciones: dict[str, bool] = Field({}, description="Id de cada punto de la lista → cumple o no")


class Veredicto(Estricto):
    cumple: bool
    media: float
    motivos: list[str]


@lru_cache
def rubrica() -> dict:
    return json.loads((DIR / "rubrica.json").read_text(encoding="utf-8"))


@lru_cache
def listas() -> dict:
    return json.loads((DIR / "listas-comprobacion.json").read_text(encoding="utf-8"))


def evaluar(r: Revision) -> Veredicto:
    ru, motivos = rubrica(), []
    ids = [c["id"] for c in ru["criterios"]]
    if set(r.puntos) != set(ids):
        raise ValueError(f"Hay que puntuar exactamente: {ids}")
    if any(not 1 <= v <= 5 for v in r.puntos.values()):
        raise ValueError("Las puntuaciones van de 1 a 5")
    regla = ru["regla"]
    media = round(sum(r.puntos.values()) / len(ids), 2)
    bajos = [k for k in ids if r.puntos[k] < regla["minimo_por_criterio"]]
    if bajos:
        motivos.append("Por debajo de " + str(regla["minimo_por_criterio"]) + ": " + ", ".join(bajos))
    if media < regla["media_minima"]:
        motivos.append(f"Media {media} por debajo de {regla['media_minima']}")
    graves = [p for p in r.problemas if p.gravedad in regla["gravedades_que_bloquean"]]
    if graves:
        motivos.append(f"{len(graves)} problemas graves o medios sin resolver")
    lista = listas()["tipos"].get(r.tipo)
    if lista is None:
        raise ValueError(f"Tipo de entregable desconocido: {r.tipo}")
    puntos = listas()["comunes"] + lista["puntos"]
    # Un id mal escrito o de otro tipo de entregable no puede contar como cumplido sin que nadie lo vea (N6).
    ajenos = sorted(set(r.comprobaciones) - {p["id"] for p in puntos})
    if ajenos:
        raise ValueError(f"Puntos que no son de la lista de {r.tipo}: {ajenos}")
    sin_criterio = sorted({p.criterio for p in r.problemas} - set(ids))
    if sin_criterio:
        raise ValueError(f"Problemas con un criterio que no existe: {sin_criterio}")
    faltan = [p["id"] for p in puntos if not r.comprobaciones.get(p["id"], False)]
    if faltan:
        motivos.append("Lista de comprobación sin cumplir: " + ", ".join(faltan))
    return Veredicto(cumple=not motivos, media=media, motivos=motivos)
