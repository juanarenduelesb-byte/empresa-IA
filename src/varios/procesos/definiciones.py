"""Validación de definiciones de workflow (P34).

Una definición es válida si:
- sus tareas tienen id único, proceso existente, tipo conocido, timeout y criterio;
- el flujo solo une tareas declaradas y todas son alcanzables desde la primera;
- las tareas humanas o con aprobación lo declaran;
- los errores no reintentables incluyen autorización, seguridad y política.
"""

from __future__ import annotations

import json
from pathlib import Path

from .estados import DEFINICIONES, RAIZ

TIPOS = frozenset({"regla", "ia", "humano", "sistema"})
OBLIGATORIOS_NO_REINTENTAR = frozenset({"autorizacion", "seguridad", "politica"})


def procesos_catalogo(carpeta: Path = RAIZ / "processes" / "catalog") -> set[str]:
    return {p.name[:3] for p in carpeta.glob("P[0-9][0-9]-*.md")}


def validar(defn: dict, procesos: set[str]) -> list[str]:
    errores: list[str] = []
    tareas = defn.get("tareas", [])
    ids = [t.get("id") for t in tareas]
    if len(ids) != len(set(ids)):
        errores.append("Ids de tarea repetidos")
    for t in tareas:
        tid = t.get("id", "?")
        if t.get("proceso") not in procesos:
            errores.append(f"{tid}: proceso {t.get('proceso')} no existe en el catálogo")
        if t.get("tipo") not in TIPOS:
            errores.append(f"{tid}: tipo {t.get('tipo')} desconocido")
        if not isinstance(t.get("timeout_s"), int) or t["timeout_s"] <= 0:
            errores.append(f"{tid}: timeout_s debe ser un entero positivo")
        if not isinstance(t.get("max_intentos"), int) or t["max_intentos"] < 1:
            errores.append(f"{tid}: max_intentos debe ser al menos 1")
        if not t.get("criterio_aceptacion"):
            errores.append(f"{tid}: falta criterio de aceptación")
        aprob = t.get("aprobacion")
        if aprob is not None and not aprob.get("rol"):
            errores.append(f"{tid}: aprobación sin rol")
    conocidas = set(ids)
    for de, a in defn.get("flujo", []):
        if de not in conocidas or a not in conocidas:
            errores.append(f"Flujo con tarea desconocida: {de} → {a}")
    if tareas:
        vistos, pila = set(), [tareas[0]["id"]]
        while pila:
            n = pila.pop()
            if n in vistos:
                continue
            vistos.add(n)
            pila.extend(a for de, a in defn.get("flujo", []) if de == n)
        sueltas = conocidas - vistos
        if sueltas:
            errores.append(f"Tareas inalcanzables: {sorted(sueltas)}")
    falta = OBLIGATORIOS_NO_REINTENTAR - set(defn.get("errores", {}).get("no_reintentar", []))
    if falta:
        errores.append(f"Deben ser no reintentables: {sorted(falta)}")
    return errores


def validar_archivo(nombre: str = "ciclo-encargo", carpeta: Path = DEFINICIONES) -> list[str]:
    defn = json.loads((carpeta / f"{nombre}.json").read_text(encoding="utf-8"))
    return validar(defn, procesos_catalogo())
