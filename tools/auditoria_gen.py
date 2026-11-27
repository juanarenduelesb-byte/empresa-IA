"""Genera docs/28-auditoria-agentes.md desde tools/org_data/auditoria.py (N2, M-040).

    python3 tools/auditoria_gen.py          # escribe el documento
    python3 tools/auditoria_gen.py --check  # falla si el documento no está al día
"""

from __future__ import annotations

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "tools"))

from org_data.agentes import A, DEPS  # noqa: E402
from org_data.auditoria import AGENTES, HABILIDADES, PROCESOS_CLIENTE  # noqa: E402
from org_data.habilidades import H  # noqa: E402
from org_data.procesos import P  # noqa: E402

SALIDA = RAIZ / "docs" / "28-auditoria-agentes.md"
NOMBRE_P = {p["id"]: p["nombre"] for p in P} | {k: v[0] for k, v in PROCESOS_CLIENTE.items()}
CUANDO_P = {p["id"]: p["cuando"] for p in P} | {k: "Proceso de cliente" for k in PROCESOS_CLIENTE}


def dueno_efectivo(aid: str) -> str | None:
    """Agente que hace el trabajo si se aprueba la propuesta (el mismo, su destino o ninguno)."""
    e = AGENTES[aid]
    if e["veredicto"] == "mantener":
        return aid
    if e["veredicto"] == "fusionar":
        return e["destino"]
    return None


def cuenta(d: dict) -> dict:
    c = {"mantener": 0, "fusionar": 0, "retirar": 0}
    for e in d.values():
        c[e["veredicto"]] += 1
    return c


def detalle(e: dict) -> str:
    if e["veredicto"] == "mantener":
        return ", ".join(e["procesos"]) + " · " + e["metrica"] + ((" · " + e["motivo"]) if e["motivo"] else "")
    if e["veredicto"] == "fusionar":
        return "Con **%s**. %s" % (e["destino"], e["motivo"])
    return "%s **Se recupera si:** %s" % (e["motivo"], e["reactivar"])


def generar() -> str:
    ca, ch = cuenta(AGENTES), cuenta(HABILIDADES)
    nombre_a = {a["id"]: a["nombre"] for a in A}
    nombre_h = {h["id"]: h["nombre"] for h in H}
    usan = {}
    for a in A:
        for h in a["habilidades"]:
            usan.setdefault(h, []).append(a["id"])

    s = ["<!-- Generado por tools/auditoria_gen.py desde tools/org_data/auditoria.py. No editar a mano. -->",
         "# Auditoría de agentes y habilidades frente a los procesos (M-040)",
         "",
         "**Estado:** propuesta (D-026), pendiente de los socios. **No se ha borrado ni cambiado ningún agente:** "
         "`tools/org_data/agentes.py` y `tools/org_data/habilidades.py` siguen igual hasta que se apruebe. "
         "Fecha: 26/11/2026 (tanda de las 22:00).",
         "",
         "## Conclusión",
         "",
         "De %d agentes se proponen mantener %d, fusionar %d y retirar %d. De %d habilidades, mantener %d, fusionar %d y retirar %d. "
         % (len(AGENTES), ca["mantener"], ca["fusionar"], ca["retirar"], len(HABILIDADES), ch["mantener"], ch["fusionar"], ch["retirar"])
         + "Lo que se retira no sirve hoy a ningún proceso del catálogo ni al proceso de referencia: los cinco expertos de sectores "
         "que no son seguros, y la administración y la contabilidad de una sociedad que aún no existe. Lo que se fusiona son pares que comparten "
         "la misma ficha de conocimiento y el mismo proceso. Cada agente y cada habilidad que se queda tiene al menos un proceso y una métrica "
         "que diría si lo hace bien.",
         "",
         "## Criterio",
         "",
         "1. **Proceso antes que agente** ([CLAUDE.md](../CLAUDE.md)). Un agente existe porque un proceso de [P01–P38](13-procesos-y-estados.md) "
         "o el [proceso de referencia](../processes/referencia-seguros-apertura-siniestros/README.md) lo necesita; si no, es una ficha, no capacidad "
         "([plan maestro, punto 4](23-plan-maestro.md)).",
         "2. **Lo más simple que funcione.** La guía de Anthropic sobre agentes eficaces dice «we recommend finding the simplest solution possible, and only "
         "increasing complexity when needed» y distingue los flujos de trabajo, donde el modelo y las herramientas siguen «predefined code paths», "
         "de los agentes que deciden sus propios pasos ([ANTHROPIC-AGENTES](../knowledge/fuentes/registro.md#anthropic-agentes)). "
         "Nuestros puestos son, en sus términos, trabajadores de un orquestador (el CEO limitado): cada uno más es una ruta más que probar.",
         "3. **Métrica o nada.** Cada agente y habilidad que se queda dice qué número mostraría que lo hace bien. Varias métricas aún no se pueden "
         "medir (no hay clientes): se miden con los casos inventados hasta el 15/02/2027.",
         "4. **Fusionar si comparten ficha y proceso; retirar si no hay proceso.** Al retirar se conserva la ficha de conocimiento y se dice qué "
         "tendría que pasar para recuperarlo.",
         "",
         "## Agentes",
         "",
         "| Agente | Departamento | Veredicto | Procesos · métrica, o motivo |",
         "|---|---|---|---|"]
    for a in A:
        e = AGENTES[a["id"]]
        s.append("| %s (`%s`) | %s | %s | %s |" % (a["nombre"], a["id"], DEPS[a["dep"]], e["veredicto"], detalle(e)))

    s += ["", "## Habilidades", "",
          "| Habilidad | La usan hoy | Veredicto | Procesos · métrica, o motivo |",
          "|---|---|---|---|"]
    for h in H:
        e = HABILIDADES[h["id"]]
        s.append("| %s (`%s`) | %s | %s | %s |" % (nombre_h[h["id"]], h["id"], ", ".join(usan.get(h["id"], [])) or "—", e["veredicto"], detalle(e)))

    # Cobertura por proceso después de la propuesta
    cubre = {pid: set() for pid in NOMBRE_P}
    for aid, e in AGENTES.items():
        for pid in e["procesos"]:
            cubre[pid].add(aid)
    s += ["", "## Cobertura de los procesos si se aprueba", "",
          "Agentes que quedan en cada proceso. Ningún proceso se queda sin agente; los que solo tienen uno dependen de que ese agente funcione.", "",
          "| Proceso | Cuándo | Agentes |", "|---|---|---|"]
    for pid in NOMBRE_P:
        ags = sorted(cubre[pid])
        s.append("| %s · %s | %s | %s |" % (pid, NOMBRE_P[pid], CUANDO_P[pid], ", ".join(nombre_a[x] for x in ags) or "**ninguno**"))
    solos = [pid for pid in NOMBRE_P if len(cubre[pid]) == 1]
    s += ["", "Procesos con un solo agente: %s." % ", ".join(solos), ""]

    # Qué cambiaría en agentes.py
    s += ["## Qué cambiaría en `agentes.py` si se aprueba", ""]
    for aid, e in AGENTES.items():
        if e["veredicto"] == "fusionar":
            orig = next(a for a in A if a["id"] == aid)
            destino = next(a for a in A if a["id"] == e["destino"])
            nuevas = [h for h in orig["habilidades"] if h not in destino["habilidades"] and HABILIDADES[h]["veredicto"] == "mantener"]
            s.append("- **%s** pasa a **%s**%s." % (nombre_a[aid], nombre_a[e["destino"]],
                     (", que recibe " + ", ".join("`%s`" % h for h in nuevas)) if nuevas else ""))
    ret = [nombre_a[a] for a, e in AGENTES.items() if e["veredicto"] == "retirar"]
    s.append("- Se marcan como retirados, sin borrar su ficha: %s." % ", ".join(ret))
    s.append("- Las habilidades fusionadas se unen a su destino: %s." % "; ".join(
        "`%s` en `%s`" % (h, e["destino"]) for h, e in HABILIDADES.items() if e["veredicto"] == "fusionar"))
    s += ["- D-020 (seis puestos nuevos) se revisa: de los seis, se quedan Director financiero, Éxito de cliente, Plataforma y operaciones y "
          "Diseño y experiencia; Contabilidad se retira y Cumplimiento se une a Legal.",
          "", "## Cómo se mantiene", "",
          "- La fuente es `tools/org_data/auditoria.py`; este documento se genera con `python3 tools/auditoria_gen.py`.",
          "- `tests/test_auditoria_agentes.py` falla si se añade un agente o una habilidad sin entrada en la auditoría, si una entrada que se "
          "mantiene no tiene proceso existente o métrica, si una fusión apunta a algo que no se queda, si una retirada no dice cómo se recupera, "
          "si un proceso se queda sin agente o si este documento no está al día.",
          "- El nivel de autonomía de cada proceso (A0–A4) sale de esta auditoría en N1 (M-045).",
          ""]
    return "\n".join(s)


def main() -> int:
    texto = generar()
    if "--check" in sys.argv:
        if not SALIDA.exists() or SALIDA.read_text(encoding="utf-8") != texto:
            print("docs/28-auditoria-agentes.md desactualizado: python3 tools/auditoria_gen.py")
            return 1
        return 0
    SALIDA.write_text(texto, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
