#!/usr/bin/env python3
"""Genera las fichas de los agentes de la oficina y la biblioteca de habilidades.

Fuente: tools/org_data/agentes.py y tools/org_data/habilidades.py.
Salida:
  knowledge/agentes/README.md y knowledge/agentes/<id>.md   (las lee el cerebro)
  claude/habilidades/README.md y claude/habilidades/<id>.md (habilidades reutilizables)
  oficina/agentes.json                                       (las usa la oficina)
Uso: python3 tools/agentes_gen.py [--check]
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from org_data.agentes import AGENTES, DEPS, REGLAS_OFICINA  # noqa: E402
from org_data.especialistas import ESPECIALISTAS  # noqa: E402
from org_data.habilidades import HABILIDADES  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AVISO = "<!-- Generado por tools/agentes_gen.py desde tools/org_data/. No editar a mano. -->\n"
AG = {a["id"]: a for a in AGENTES}
HB = {h["id"]: h for h in HABILIDADES}
ESP = {e["id"]: e for e in ESPECIALISTAS}


def validar():
    errores = []
    if len(AG) != len(AGENTES):
        errores.append("ids de agente repetidos")
    for a in AGENTES:
        if a["dep"] not in DEPS:
            errores.append(f"{a['id']}: departamento desconocido {a['dep']}")
        for h in a["habilidades"]:
            if h not in HB:
                errores.append(f"{a['id']}: habilidad desconocida {h}")
        for c, _ in a["colabora"]:
            if c not in AG:
                errores.append(f"{a['id']}: colabora con desconocido {c}")
        for e in a["especialista"]:
            if e not in ESP:
                errores.append(f"{a['id']}: especialista desconocido {e}")
        for campo in ("mision", "nivel"):
            if not a.get(campo):
                errores.append(f"{a['id']}: falta {campo}")
        if len(a["reglas"]) < 2 or len(a["procedimiento"]) < 3:
            errores.append(f"{a['id']}: ficha incompleta")
    for d in DEPS:
        if sum(1 for a in AGENTES if a["dep"] == d and a["lead"]) != 1:
            errores.append(f"{d}: debe tener exactamente un jefe")
    return errores


def lista(items):
    return "\n".join(f"- {x}" for x in items) or "—"


def esp_path(eid):
    return f"knowledge/{ESP[eid]['dep']}/{eid}.md"


def usan(hid):
    return [a for a in AGENTES if hid in a["habilidades"]]


def ficha_md(a):
    out = [AVISO, f"# {a['nombre']}\n",
           f"**Departamento:** {DEPS[a['dep']]}{' · **Jefe del departamento**' if a['lead'] else ''} · **Puesto en la oficina:** `{a['id']}` · **Estado:** draft, pendiente de revisión de un socio\n",
           f"> {a['mision']}\n",
           f"**Nivel:** {a['nivel']}\n",
           "## Responsabilidades\n", lista(a["responsabilidades"]), "",
           "## Entregables\n", lista(a["entregables"]), "",
           "## Cómo trabaja\n", "\n".join(f"{i}. {p}" for i, p in enumerate(a["procedimiento"], 1)), "",
           "## Reglas del puesto\n", lista(a["reglas"]), "",
           "## Reglas de la oficina (para todos)\n", lista(REGLAS_OFICINA), "",
           "## Habilidades\n",
           lista(f"[{HB[h]['nombre']}](../../claude/habilidades/{h}.md)" for h in a["habilidades"]), "",
           "## Criterio de nivel senior\n", lista(a["criterio"]), "",
           "## Errores que evita\n", lista(a["errores"]), "",
           "## Cómo se mide\n", lista(a["kpis"]), "",
           "## Con quién trabaja\n", lista(f"**{AG[c]['nombre']}** (`{c}`): {m}" for c, m in a["colabora"]), "",
           "## Límites\n", lista(a["limites"]), "",
           "## Conocimiento de referencia\n",
           lista(f"[{ESP[e]['nombre']}](../../{esp_path(e)})" for e in a["especialista"]), ""]
    return "\n".join(out)


def readme_agentes():
    out = [AVISO, "# Agentes de la oficina\n",
           f"{len(AGENTES)} puestos en {len(DEPS)} departamentos. Cada ficha dice qué hace el agente, cómo trabaja, sus reglas, sus habilidades y sus límites. "
           "Las genera `tools/agentes_gen.py` desde `tools/org_data/agentes.py`; las reglas que los socios añaden desde la oficina se vuelcan aparte en `oficina/registro/`.\n"]
    for d, n in DEPS.items():
        out.append(f"## {n}\n")
        for a in AGENTES:
            if a["dep"] == d:
                out.append(f"- [{a['nombre']}]({a['id']}.md){' · jefe' if a['lead'] else ''}: {a['mision']}")
        out.append("")
    return "\n".join(out)


def hab_md(h):
    u = usan(h["id"])
    return "\n".join([AVISO, f"# {h['nombre']}\n", f"`{h['id']}` · **Estado:** draft\n",
                      f"**Cuándo se usa:** {h['cuando']}\n", "## Pasos\n",
                      "\n".join(f"{i}. {p}" for i, p in enumerate(h["pasos"], 1)), "",
                      f"## Resultado\n\n{h['salida']}\n", "## Lista de control\n", lista(h["control"]), "",
                      "## Quién la usa\n", lista(f"[{a['nombre']}](../../knowledge/agentes/{a['id']}.md)" for a in u), ""])


def readme_hab():
    out = [AVISO, "# Habilidades de los agentes\n",
           "Formas de trabajar que se pueden repetir y revisar. Las usan los agentes de la oficina y servirán como habilidades del proyecto de Claude.\n",
           "| Habilidad | Cuándo | Quién la usa |", "|---|---|---|"]
    for h in HABILIDADES:
        out.append(f"| [{h['nombre']}]({h['id']}.md) | {h['cuando']} | {', '.join(a['id'] for a in usan(h['id'])) or '—'} |")
    return "\n".join(out) + "\n"


def json_oficina():
    return json.dumps({
        "generado": "tools/agentes_gen.py",
        "reglas_oficina": REGLAS_OFICINA,
        "agentes": {a["id"]: {k: a[k] for k in ("nombre", "rol", "dep", "lead", "nivel", "mision", "responsabilidades", "entregables", "procedimiento",
                                                 "reglas", "habilidades", "criterio", "errores", "kpis", "limites")}
                    | {"colabora": [{"id": c, "motivo": m} for c, m in a["colabora"]], "especialista": [esp_path(e) for e in a["especialista"]]}
                    for a in AGENTES},
        "habilidades": {h["id"]: {k: h[k] for k in ("nombre", "cuando", "pasos", "salida", "control")} for h in HABILIDADES},
    }, ensure_ascii=False, indent=1) + "\n"


def salidas():
    o = {"knowledge/agentes/README.md": readme_agentes(), "claude/habilidades/README.md": readme_hab(), "oficina/agentes.json": json_oficina()}
    for a in AGENTES:
        o[f"knowledge/agentes/{a['id']}.md"] = ficha_md(a)
    for h in HABILIDADES:
        o[f"claude/habilidades/{h['id']}.md"] = hab_md(h)
    return o


def main(check):
    err = validar()
    if err:
        print("\n".join(err))
        return 1
    stale = []
    for rel, txt in salidas().items():
        p = os.path.join(ROOT, rel)
        cur = open(p, encoding="utf-8").read() if os.path.exists(p) else None
        if cur != txt:
            if check:
                stale.append(rel)
            else:
                os.makedirs(os.path.dirname(p), exist_ok=True)
                open(p, "w", encoding="utf-8").write(txt)
    if stale:
        print("Desactualizado (ejecuta python3 tools/agentes_gen.py):\n" + "\n".join(stale))
        return 1
    print(f"{len(AGENTES)} agentes y {len(HABILIDADES)} habilidades {'al día' if check else 'generados'}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
