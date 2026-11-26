"""Genera docs/29-autonomia.md desde processes/autonomia.json (N1, M-045).

    python3 tools/autonomia_gen.py          # escribe el documento
    python3 tools/autonomia_gen.py --check  # falla si el documento no está al día
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "tools"))

from org_data.auditoria import AGENTES, PROCESOS_CLIENTE  # noqa: E402
from org_data.procesos import P  # noqa: E402

FUENTE = RAIZ / "processes" / "autonomia.json"
SALIDA = RAIZ / "docs" / "29-autonomia.md"
TOPE_SENSIBLE = "A2"
CATEGORIAS_SENSIBLES = {"externo", "legal", "financiero", "contractual"}


def nivel(n: str) -> int:
    return int(n[1])


def cargar() -> dict:
    return json.loads(FUENTE.read_text(encoding="utf-8"))


def generar() -> str:
    d = cargar()
    nombres = {p["id"]: p["nombre"] for p in P} | {k: v[0] for k, v in PROCESOS_CLIENTE.items()}
    agentes = {}
    for aid, e in AGENTES.items():
        for pid in e["procesos"]:
            agentes.setdefault(pid, []).append(aid)
    cuenta = {}
    for p in d["procesos"]:
        cuenta[p["objetivo_febrero"]] = cuenta.get(p["objetivo_febrero"], 0) + 1
    sensibles = [p for p in d["procesos"] if set(p["categorias"]) & CATEGORIAS_SENSIBLES]
    s = ["<!-- Generado por tools/autonomia_gen.py desde processes/autonomia.json. No editar a mano. -->",
         "# Mapa de autonomía por proceso, A0–A4 (M-045)",
         "",
         "**Estado:** %s. Fecha: 26/11/2026. Fuente máquina: [processes/autonomia.json](../processes/autonomia.json). "
         "Sale de la [auditoría de agentes](28-auditoria-agentes.md) (N2): cada proceso tiene agentes que se quedan y una métrica." % d["estado"],
         "",
         "## Conclusión",
         "",
         "Hoy todos los procesos están en A0: %s "
         "Para el 12/02/2027 se propone: %s. "
         "%d de los %d procesos tocan algo externo, legal, financiero o contractual y tienen el techo en A2 o por debajo; "
         "la aprobación humana (P10) no pasa nunca de A1." % (
             d["actual"].split(": ", 1)[1],
             ", ".join("%d en %s" % (cuenta[k], k) for k in sorted(cuenta)),
             len(sensibles), len(d["procesos"])),
         "",
         "## Niveles",
         "",
         "| Nivel | Qué hace el sistema |", "|---|---|"]
    s += ["| %s | %s |" % (k, v) for k, v in d["niveles"].items()]
    s += ["",
          "Los niveles son los de [docs/22](22-plan-hasta-febrero.md) («La autonomía se gana con datos»). Coinciden con los cinco papeles del "
          "usuario que proponen Feng, McDonald y Zhang (Knight First Amendment Institute, 2025): operador, colaborador, consultor, aprobador y "
          "observador. De ellos se toma la idea central: la autonomía «can instead be a deliberate design decision» independiente de la "
          "capacidad, de modo que un agente capaz puede trabajar con poca autonomía si debe consultar antes de cada acción "
          "([KNIGHT-NIVELES-AUTONOMIA](../knowledge/fuentes/registro.md#knight-niveles-autonomia)). El techo de cada proceso sigue la tabla de "
          "riesgo de la [Guía v1.4](fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md) (§3: lo de riesgo alto se prepara pero no se "
          "finaliza ni se envía solo) y la regla de [CLAUDE.md](../CLAUDE.md): %s" % d["regla"],
          "",
          "## Cómo se sube y se baja (propuesta)",
          "",
          "- **Subir un nivel** (nunca dos de golpe): la métrica del proceso cumple el umbral durante el periodo y lo aprueba un socio. "
          "El periodo propuesto para todos es «%s»; el umbral es %s." % (d["procesos"][0]["subir"]["periodo"], d["procesos"][0]["subir"]["umbral"]),
          "- **Bajar:** %s." % d["procesos"][0]["bajar"],
          "- **Nunca por encima del techo.** Subir el techo de un proceso sensible no es una mejora técnica: exige cambiar CLAUDE.md, y eso lo "
          "deciden los socios.",
          "- Los periodos y la regla de bajada son una propuesta de esta noche, no un dato: los fijan los socios con D-027.",
          "",
          "## Procesos",
          "",
          "| Proceso | Toca | Hoy | Febrero | Techo | Métrica para subir | Agentes | Nota |",
          "|---|---|---|---|---|---|---|---|"]
    for p in d["procesos"]:
        s.append("| %s · %s | %s | %s | %s | %s | %s | %s | %s |" % (
            p["id"], nombres[p["id"]], ", ".join(p["categorias"]) or "—", p["actual"], p["objetivo_febrero"], p["tope"],
            p["subir"]["metrica"], ", ".join(agentes.get(p["id"], [])), p["nota"] or ""))
    s += ["", "## Cómo se mantiene", "",
          "- Se edita `processes/autonomia.json` y se regenera con `python3 tools/autonomia_gen.py`.",
          "- `tests/test_autonomia.py` falla si falta un proceso, si un nivel no existe, si hoy o febrero superan el techo, si algo externo, "
          "legal, financiero o contractual pasa de A2, si P10 pasa de A1, si falta la métrica o el criterio de bajada, o si este documento no "
          "está al día.",
          ""]
    return "\n".join(s)


def main() -> int:
    texto = generar()
    if "--check" in sys.argv:
        if not SALIDA.exists() or SALIDA.read_text(encoding="utf-8") != texto:
            print("docs/29-autonomia.md desactualizado: python3 tools/autonomia_gen.py")
            return 1
        return 0
    SALIDA.write_text(texto, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
