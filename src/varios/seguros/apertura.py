"""Reglas fijas de la apertura de un siniestro (tarea C1, D-024).

La IA extrae los hechos del mensaje (`Hechos`); este módulo decide, con código fijo, qué excepciones
saltan y qué se hace después. Los plazos, las listas y los umbrales salen de
`knowledge/sectores/seguros/dominio.json`, no del código. Nada de esto decide cobertura, culpa,
fraude ni importes: como mucho prepara un borrador y lo pasa a una persona.
"""

from __future__ import annotations

import json
from datetime import date
from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

RAIZ = Path(__file__).resolve().parents[3]
DOMINIO = RAIZ / "knowledge" / "sectores" / "seguros" / "dominio.json"

Ramo = Literal["hogar", "comercio", "automovil", "responsabilidad_civil", "accidentes", "vida", "salud"]
Accion = Literal["preparar_parte", "pedir_documentacion", "trasladar_a_aseguradora", "pasar_a_persona"]


class Estricto(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Poliza(Estricto):
    """Una póliza de la cartera inventada de la correduría."""

    numero: str
    ramo: Ramo
    aseguradora: str
    efecto: date
    vencimiento: date
    recibo_pagado: bool = True
    plazo_comunicacion_dias: int | None = Field(None, description="Solo si la póliza fija un plazo mayor de 7 días")


class Hechos(Estricto):
    """Lo que un extractor perfecto sacaría del mensaje. Es la «verdad» contra la que se medirá la IA."""

    remitente: Literal["asegurado", "tomador", "beneficiario", "tercero"] = "asegurado"
    poliza_numero: str | None = None
    ramo: Ramo | None = None
    causa: str | None = None
    fecha_ocurrencia: date | None = None
    fecha_conocimiento: date | None = None
    hay_descripcion: bool = True
    hay_contacto: bool = True
    danos_personales: bool = False
    vehiculos: int | None = None
    colision_directa: bool | None = None
    declaracion_amistosa: bool | None = None
    queja: bool = False
    pide_persona: bool = False
    incoherencias: list[str] = []
    otras_polizas: bool = False
    movimiento_dinero: bool = False
    reclamacion_judicial_o_atestado: bool = False
    vulnerable_o_fallecimiento: bool = False


class Resultado(Estricto):
    excepciones: list[str]
    accion: Accion
    tambien: list[Literal["abrir_reclamacion", "pedir_declaracion_amistosa"]] = []
    anotar_libro_siniestros: bool
    detalle: dict[str, str] = {}
    requiere_aprobacion_humana: bool = True  # toda acción externa la aprueba una persona (CLAUDE.md)


class Caso(Estricto):
    id: str
    titulo: str
    canal: Literal["correo", "telefono", "whatsapp", "formulario", "presencial"]
    fecha_recepcion: date
    mensaje: str
    hechos: Hechos
    esperado: Resultado
    por_que: str


@lru_cache
def dominio() -> dict:
    return json.loads(DOMINIO.read_text(encoding="utf-8"))


def _plazo_general() -> int:
    return next(p["dias"] for p in dominio()["plazos"] if p["id"] == "PL-COMUNICACION")


def _carencia() -> int:
    return next(p["dias"] for p in dominio()["plazos"] if p["id"] == "PL-CARENCIA-CCS")


def _meses(desde: date, hasta: date) -> int:
    return (hasta.year - desde.year) * 12 + hasta.month - desde.month - (hasta.day < desde.day)


def evaluar(h: Hechos, recepcion: date, cartera: dict[str, Poliza]) -> Resultado:
    """Aplica las reglas del catálogo de excepciones (EX-01 a EX-15) a unos hechos."""
    r = dominio()["reglas"]
    ex: dict[str, str] = {}
    pol = cartera.get(h.poliza_numero) if h.poliza_numero else None
    ramo = h.ramo or (pol.ramo if pol else None)

    faltan = [n for n, v in (("póliza", h.poliza_numero), ("fecha de ocurrencia", h.fecha_ocurrencia),
                             ("descripción", h.hay_descripcion), ("contacto", h.hay_contacto)) if not v]
    if faltan:
        ex["EX-13"] = "Falta: " + ", ".join(faltan)

    if h.poliza_numero:
        if pol is None:
            ex["EX-02"] = "La póliza no está en la cartera"
        elif h.fecha_ocurrencia and not pol.efecto <= h.fecha_ocurrencia <= pol.vencimiento:
            ex["EX-02"] = "El siniestro cae fuera de la vigencia"
        elif not pol.recibo_pagado:
            ex["EX-02"] = "Recibo pendiente"

    if h.fecha_conocimiento:
        plazo = max(_plazo_general(), (pol.plazo_comunicacion_dias or 0) if pol else 0)
        dias = (recepcion - h.fecha_conocimiento).days
        if dias > plazo:
            ex["EX-01"] = f"{dias} días desde que lo conoció; plazo {plazo}"

    if h.causa in r["causas_extraordinarias"]["lista"]:
        nota = "Posible vía CCS"
        if (pol and h.fecha_ocurrencia and h.causa in r["causas_naturales_con_carencia"]["lista"]
                and (h.fecha_ocurrencia - pol.efecto).days < _carencia()):
            nota += "; dentro de la carencia de 7 días desde el efecto (comprobar el cómputo)"
        ex["EX-03"] = nota

    if h.danos_personales:
        ex["EX-04"] = "No guardar datos de salud"

    if ramo == "automovil" and (h.vehiculos or 0) >= 2 and not h.danos_personales:
        ex["EX-05"] = "Posible convenio" if h.vehiculos == 2 and h.colision_directa else "Posible SDM"

    if h.remitente == "tercero":
        ex["EX-06"] = "Reclama un tercero"
    if h.queja:
        ex["EX-07"] = "Hay una queja: un mes para resolver"
    if h.pide_persona:
        ex["EX-08"] = "Pide hablar con una persona"
    if h.incoherencias:
        ex["EX-09"] = "; ".join(h.incoherencias)

    if h.fecha_ocurrencia:
        personas = ramo in r["ramos_de_personas"]["lista"]
        umbral = r["aviso_prescripcion_meses"]["personas" if personas else "danos"]
        if _meses(h.fecha_ocurrencia, recepcion) >= umbral:
            ex["EX-10"] = f"Más de {umbral} meses desde el siniestro"

    if h.otras_polizas:
        ex["EX-11"] = "Varias pólizas para el mismo daño"
    if h.movimiento_dinero:
        ex["EX-12"] = "Hay dinero por medio"
    if h.reclamacion_judicial_o_atestado:
        ex["EX-14"] = "Anotar la reclamación en el libro de siniestros"
    if h.vulnerable_o_fallecimiento:
        ex["EX-15"] = "Atender con prioridad"

    ids = sorted(ex)
    if "EX-08" in ex or set(ids) & set(r["bloquean"]["lista"]):
        accion = "pasar_a_persona"
    elif "EX-13" in ex:
        accion = "pedir_documentacion"
    elif "EX-06" in ex:
        accion = "trasladar_a_aseguradora"
    else:
        accion = "preparar_parte"

    tambien = []
    if "EX-07" in ex:
        tambien.append("abrir_reclamacion")
    if "EX-05" in ex and ex["EX-05"] == "Posible convenio" and not h.declaracion_amistosa:
        tambien.append("pedir_declaracion_amistosa")

    return Resultado(excepciones=ids, accion=accion, tambien=tambien,
                     anotar_libro_siniestros=pol is not None and h.remitente != "tercero", detalle=ex)
