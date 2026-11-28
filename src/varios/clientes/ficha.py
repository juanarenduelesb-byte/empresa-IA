"""Ficha de cliente (tarea B3). Modelo Pydantic del que sale el esquema JSON publicado.

Reglas que el modelo impone:
- Sin datos personales: los interlocutores se guardan por rol, nunca con nombre, correo o teléfono. Ningún texto de
  la ficha admite un correo, un teléfono o un DNI o NIE (un nombre no se reconoce con un patrón: lo vigila quien
  escribe la ficha).
- Cada dato del proceso dice de dónde sale: medido, declarado por el cliente o hipótesis nuestra.
- Las cifras de tamaño van por rangos, no exactas.
- Una ficha de un cliente inventado lo dice (`ficticio`), y hasta L2 solo hay fichas inventadas (D-011).

Uso: python -m varios.clientes.ficha   → escribe knowledge/plantillas/ficha-cliente.schema.json
"""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

RAIZ = Path(__file__).resolve().parents[3]
ESQUEMA = RAIZ / "knowledge" / "plantillas" / "ficha-cliente.schema.json"

Base = Literal["medido", "declarado", "hipotesis"]
Puerta = Literal["G0", "G1", "G2", "G3", "G4", "G5", "G6"]
Nivel = Literal["L0", "L1", "L2", "L3", "L4"]
SiNo = Literal["si", "no", "por_confirmar"]


# Lo que se puede reconocer sin IA: correo, teléfono español y DNI o NIE. Un nombre no se reconoce con un patrón;
# para eso están los campos por rol y la revisión de quien escribe la ficha.
_PERSONAL = {
    "un correo": re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+"),
    "un teléfono": re.compile(r"(?<!\d)(\+?34)?[6789]\d{8}(?!\d)"),
    "un DNI o NIE": re.compile(r"\b[XYZ]?\d{7,8}[A-Z]\b", re.I),
}


class Estricto(BaseModel):
    model_config = ConfigDict(extra="forbid")

    @field_validator("*", mode="after")
    @classmethod
    def _sin_datos_personales(cls, v):
        """La ficha no guarda datos personales: rechaza correos, teléfonos y DNI en cualquier texto (repaso 28/11)."""
        for t in ([v] if isinstance(v, str) else v if isinstance(v, list) else []):
            if isinstance(t, str):
                plano = re.sub(r"[\s.()-]", "", t)
                for que, patron in _PERSONAL.items():
                    if patron.search(plano if que == "un teléfono" else t):
                        raise ValueError(f"La ficha no guarda datos personales: parece {que}")
        return v


class Dato(Estricto):
    """Un valor con su procedencia. Sin procedencia no entra en la ficha."""

    valor: str
    base: Base
    fuente: str = Field(description="De dónde sale: conversación del día, documento del cliente o id del registro")


class Interlocutor(Estricto):
    rol: str = Field(description="Cargo o función, nunca el nombre de la persona")
    decide: bool = False
    hace_el_proceso: bool = False
    impulsor_interno: bool = False


class Sistema(Estricto):
    tipo: str = Field(description="Programa de gestión, portal de aseguradora, correo…")
    uso: str
    integracion: Literal["api", "exportacion", "portal_manual", "ninguna", "por_confirmar"] = "por_confirmar"


class ProcesoCandidato(Estricto):
    nombre: str
    volumen_mes: Dato | None = None
    tiempo_activo_min: Dato | None = None
    tiempo_total: Dato | None = Field(None, description="Lead time: desde que llega hasta que termina, con esperas")
    retrabajo: Dato | None = None
    dolor: Literal[1, 2, 3, 4, 5] | None = Field(None, description="Cuánto les duele, según su propio relato (1–5)")
    riesgo: Literal["bajo", "medio", "alto"] | None = None
    datos_sensibles: SiNo = "por_confirmar"
    elegido: bool = False


class Cualificacion(Estricto):
    """MEDDPICC (registro: MEDDICC). Cada campo es un Dato para separar lo dicho de lo supuesto."""

    metricas: Dato | None = None
    comprador_economico: Dato | None = Field(None, description="Rol que firma el gasto")
    criterios_decision: Dato | None = None
    proceso_decision: Dato | None = None
    proceso_compra: Dato | None = None
    dolor: Dato | None = None
    impulsor: Dato | None = Field(None, description="Rol que empuja dentro")
    competencia: Dato | None = None


class Hito(Estricto):
    fecha: date
    puerta: Puerta
    decision: str
    quien: str = Field(description="Rol")


class Conversacion(Estricto):
    fecha: date
    tipo: Literal["descubrimiento", "validacion_semanal", "presentacion", "decision"]
    con: list[str] = Field(description="Roles")
    aprendido: list[str]
    compromiso: str | None = Field(None, description="Lo que pone el cliente: tiempo, reputación o dinero")
    siguiente_paso: str
    cambia: list[str] = Field([], description="Qué archivos o decisiones cambian por lo aprendido")


class FichaCliente(Estricto):
    id: str
    nombre: str
    ficticio: bool
    estado: Literal["draft", "validated"] = "draft"
    actualizada: date
    sector: Literal["seg", "sal", "ase", "fnz", "ind", "log", "otro"]
    tipo_entidad: str = Field(description="Correduría, aseguradora, agencia… según el sector")
    plantilla: Literal["1-9", "10-49", "50-249", "250+", "por_confirmar"] = "por_confirmar"
    sujeto_dora: SiNo = "por_confirmar"
    puerta: Puerta = "G0"
    nivel_datos: Nivel = "L0"
    interlocutores: list[Interlocutor] = []
    sistemas: list[Sistema] = []
    procesos: list[ProcesoCandidato] = []
    cualificacion: Cualificacion = Cualificacion()
    restricciones: list[str] = []
    normas: list[str] = Field([], description="Ids del registro de fuentes que aplican")
    hitos: list[Hito] = []
    conversaciones: list[Conversacion] = []
    preguntas_abiertas: list[str] = []


if __name__ == "__main__":
    texto = json.dumps(FichaCliente.model_json_schema(), ensure_ascii=False, indent=1) + "\n"
    ESQUEMA.write_text(texto, encoding="utf-8")
    print(ESQUEMA.relative_to(RAIZ))
