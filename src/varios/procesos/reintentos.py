"""Reintentos con espera creciente, clasificación de errores e idempotencia (P22).

Solo se reintentan errores transitorios o de dependencia externa. Autorización,
seguridad, política y errores permanentes no se reintentan nunca.
"""

from __future__ import annotations

import random
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import TypeVar

T = TypeVar("T")

REINTENTABLES = frozenset({"transitorio", "dependencia_externa"})
NO_REINTENTABLES = frozenset({"autorizacion", "seguridad", "politica", "permanente"})


class ErrorClasificado(Exception):
    def __init__(self, tipo: str, mensaje: str = "") -> None:
        if tipo not in REINTENTABLES | NO_REINTENTABLES:
            raise ValueError(f"Tipo de error desconocido: {tipo}")
        super().__init__(mensaje or tipo)
        self.tipo = tipo


class Agotado(Exception):
    def __init__(self, intentos: int, ultimo: ErrorClasificado) -> None:
        super().__init__(f"Agotados {intentos} intentos: {ultimo}")
        self.intentos = intentos
        self.ultimo = ultimo


def espera(intento: int, base: float = 1.0, tope: float = 60.0, azar: random.Random | None = None) -> float:
    """Espera exponencial con jitter completo: entre 0 y min(tope, base·2^(intento-1))."""
    techo = min(tope, base * 2 ** (intento - 1))
    return (azar or random).uniform(0, techo)


def con_reintentos(
    accion: Callable[[], T],
    max_intentos: int = 3,
    dormir: Callable[[float], None] = lambda s: None,
    base: float = 1.0,
    tope: float = 60.0,
) -> T:
    """Ejecuta la acción reintentando solo errores reintentables."""
    for intento in range(1, max_intentos + 1):
        try:
            return accion()
        except ErrorClasificado as e:
            if e.tipo in NO_REINTENTABLES:
                raise
            if intento == max_intentos:
                raise Agotado(intento, e) from e
            dormir(espera(intento, base, tope))
    raise AssertionError("inalcanzable")


@dataclass
class RegistroIdempotencia:
    """Guarda el resultado de cada acción externa por su clave.

    En el piloto vivirá en PostgreSQL; aquí, en memoria, para fijar el comportamiento.
    """

    _hechos: dict[str, object] = field(default_factory=dict)

    def ejecutar(self, clave: str, accion: Callable[[], T]) -> T:
        if not clave:
            raise ValueError("Toda acción externa necesita clave de idempotencia")
        if clave in self._hechos:
            return self._hechos[clave]  # type: ignore[return-value]
        resultado = accion()
        self._hechos[clave] = resultado
        return resultado

    def ya_hecho(self, clave: str) -> bool:
        return clave in self._hechos
