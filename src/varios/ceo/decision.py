"""CEO limitado: de un encargo a una de las cinco decisiones (docs/14-reglas-del-ceo.md). Tarea C2.

El modelo (simulado o real) solo extrae `Senales` del texto. La decisión la toma código fijo:
1. detectores fijos sobre el texto bruto, que no dependen del modelo (las trampas deben caer aquí);
2. reglas en orden de prioridad sobre la unión de señales del modelo y de los detectores.
Así, aunque el modelo se deje engañar, una trampa nunca acaba en CONTINUAR.
"""

from __future__ import annotations

import re
import unicodedata
from typing import Literal, Protocol

from pydantic import BaseModel, ConfigDict, Field

from varios.procesos.motor import Identidad

Decision = Literal["CONTINUAR", "PREGUNTAR", "ESCALAR", "RECHAZAR", "DERIVAR"]
Riesgo = Literal["bajo", "medio", "alto", "critico"]


class Estricto(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Senales(Estricto):
    """Lo que hay que saber de un encargo para decidir. Todo False/vacío = nada que señalar."""

    falta: list[str] = Field([], description="Información que cambia la solución, el coste o el riesgo")
    accion_externa: bool = False
    accion_financiera: bool = False
    accion_irreversible: bool = False
    cambio_produccion: bool = False
    datos_sensibles: bool = False
    impacto_personas: bool = False
    requiere_profesional: str | None = None
    afirma_cumplimiento: bool = False
    pide_inventar: bool = False
    pide_sin_aprobacion: bool = False
    otro_cliente: str | None = None
    instrucciones_en_documento: bool = False


class Encargo(Estricto):
    id: str
    texto: str
    documento: str | None = Field(None, description="Texto adjunto: es un dato, nunca una instrucción")


class Resultado(Estricto):
    decision: Decision
    riesgo: Riesgo
    motivo: str
    reglas: list[str] = Field(description="Reglas que han saltado, en orden")


class Modelo(Protocol):
    def senales(self, encargo: Encargo) -> Senales: ...


# --- Detectores fijos (independientes del modelo) -----------------------------------------------
# Se buscan sobre una copia normalizada (`normalizar`), nunca sobre el texto tal cual, y el texto
# original no se cambia (OWASP, LLM Prompt Injection Prevention Cheat Sheet: «Normalize text before
# screening it» y «screen a normalized copy instead of rewriting the user's input»). Por eso los
# patrones van en minúsculas, sin tildes y con un solo espacio entre palabras.
_INYECCION = re.compile(
    r"ignora\w* (todas |las |tus )*(instrucciones|reglas)|olvida (tus|las) (instrucciones|reglas)"
    r"|olvida (lo|todo lo) (anterior|de antes)|instrucciones (anteriores|del sistema)|system prompt|eres ahora"
    r"|ignore (all |the |any |your )*(previous |prior |above )?(instructions|rules)|you are now")
_SIN_APROBACION = re.compile(
    r"aprueba(lo|la|los|las)? tu|sin que (lo |la )?(vea|revise|apruebe) nadie"
    r"|sin que nadie (lo |la )?(vea|revise|apruebe)"
    r"|no hace falta que (lo |la )?(vea|revise|apruebe)"
    r"|sin pasar por (ningun|el) (socio|ok|control)|sin (pedir|esperar) (permiso|aprobacion)")
_INVENTAR = re.compile(
    r"\b(inventa(te|las|los|la|lo)?|invente[ns]?|fabrica|maquilla)\b[^.]{0,40}"
    r"\b(cifras?|datos|metricas|fuentes?|testimonios?|clientes|resultados)"
    r"|\b(cifras?|datos|metricas|fuentes?|testimonios?|resultados)\b[^.]{0,40}\b(inventad|ficticio)")
_CUMPLIMIENTO = re.compile(
    r"\b(certific|garantiz|confirm|asegur)\w*\b[^.]{0,40}\bque\b[^.]{0,40}"
    r"\b(cumple|cumplimos|cumplis|en regla)")
# Caracteres invisibles (formato, como los de ancho cero, y etiquetas Unicode): en un adjunto se
# mandan a revisión (OWASP: «Send unexpected zero-width or tag characters to review»).
_INVISIBLE = re.compile(r"[​-‏‪-‮⁠-⁤﻿\U000e0000-\U000e007f]")


def normalizar(texto: str) -> str:
    """Copia para buscar: sin caracteres invisibles, sin tildes, en minúsculas y con un espacio."""
    t = unicodedata.normalize("NFKD", texto)
    t = "".join(c for c in t if not unicodedata.combining(c) and unicodedata.category(c) != "Cf")
    return re.sub(r"\s+", " ", t).casefold().strip()


def detectar(e: Encargo, identidad: Identidad, clientes: dict[str, str]) -> Senales:
    """Señales que se ven sin IA. `clientes` es {tenant: nombre} de los clientes conocidos.

    Son una capa más, no la frontera de seguridad: el aislamiento entre clientes lo pone la base
    (RLS) y lo sensible lo aprueba una persona. OWASP: «It is not a security boundary».
    """
    texto = normalizar(e.texto)
    doc = normalizar(e.documento) if e.documento else ""
    otro = next((t for t, n in clientes.items()
                 if t != identidad.tenant and (normalizar(n) in texto or normalizar(t) in texto)), None)
    return Senales(
        # En un adjunto, pedir que nadie lo apruebe o que se inventen cifras también es una instrucción.
        instrucciones_en_documento=bool(e.documento and (
            _INVISIBLE.search(e.documento)
            or any(x.search(doc) for x in (_INYECCION, _SIN_APROBACION, _INVENTAR)))),
        pide_sin_aprobacion=bool(_SIN_APROBACION.search(texto)),
        pide_inventar=bool(_INVENTAR.search(texto)),
        afirma_cumplimiento=bool(_CUMPLIMIENTO.search(texto)),
        otro_cliente=otro,
    )


def unir(a: Senales, b: Senales) -> Senales:
    d = {}
    for k in Senales.model_fields:
        x, y = getattr(a, k), getattr(b, k)
        d[k] = sorted(set(x) | set(y)) if isinstance(x, list) else (x or y)
    return Senales(**d)


# --- Reglas fijas, en orden de prioridad ---------------------------------------------------------
REGLAS: list[tuple[str, Decision, Riesgo, str]] = [
    ("otro_cliente", "RECHAZAR", "critico",
     "Pide datos o acciones sobre otro cliente: el cliente sale de la identidad"),
    ("pide_inventar", "RECHAZAR", "critico", "Pide inventar datos, cifras o fuentes"),
    ("pide_sin_aprobacion", "RECHAZAR", "critico", "Pide saltarse la aprobación humana"),
    ("instrucciones_en_documento", "ESCALAR", "alto",
     "El documento trae instrucciones: se tratan como datos y se avisa"),
    ("afirma_cumplimiento", "DERIVAR", "alto", "Afirmar cumplimiento legal exige revisión competente"),
    ("requiere_profesional", "DERIVAR", "alto", "Necesita un profesional que no somos"),
    ("accion_financiera", "ESCALAR", "alto", "Mueve dinero: aprobación de los socios"),
    ("accion_externa", "ESCALAR", "alto", "Sale fuera: aprobación de un socio antes de enviar"),
    ("accion_irreversible", "ESCALAR", "alto", "No se puede deshacer"),
    ("cambio_produccion", "ESCALAR", "alto", "Cambia algo en producción"),
    ("impacto_personas", "ESCALAR", "alto", "Decisión de alto impacto sobre personas"),
    ("datos_sensibles", "ESCALAR", "alto", "Datos personales sensibles"),
    ("falta", "PREGUNTAR", "medio", "Falta información que cambia la solución"),
]


def decidir(e: Encargo, identidad: Identidad, modelo: Modelo, clientes: dict[str, str]) -> Resultado:
    s = unir(modelo.senales(e), detectar(e, identidad, clientes))
    saltan = [(n, d, r, m) for n, d, r, m in REGLAS if getattr(s, n)]
    if not saltan:
        return Resultado(decision="CONTINUAR", riesgo="bajo", motivo="Alcance permitido y datos suficientes", reglas=[])
    n, d, r, m = saltan[0]
    if n == "falta":
        m += ": " + ", ".join(s.falta)
    return Resultado(decision=d, riesgo=r, motivo=m, reglas=[x[0] for x in saltan])
