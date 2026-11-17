#!/usr/bin/env python3
"""Vuelca al repositorio lo que pasa en la oficina de agentes (D-017).

Entrada: una carpeta con un JSON por colección de la base de datos de la oficina
(tasks, convs, memory, rules, skills, agents, decisions, projects, deliverables, docs),
cada uno con una lista de {"id": ..., "data": {...}} tal como los devuelve db_list.

Salida:
  oficina/registro/datos/<colección>.jsonl  copia fiel, se fusiona por id (no la lee el cerebro)
  precedents/oficina/...                     Markdown legible que sí entra en el cerebro:
     README.md, encargos/, conversaciones/, proyectos/, memoria.md, reglas-y-habilidades.md, decisiones.md

Privacidad: se excluye todo lo de proyectos marcados como confidenciales, el texto de los
documentos subidos (solo se guarda su nombre) y cualquier registro que contenga un posible secreto.
Uso: python3 tools/registro_oficina.py CARPETA [--desde ISO]
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS = os.path.join(ROOT, "oficina", "registro", "datos")
MD = os.path.join(ROOT, "precedents", "oficina")
COLS = ["projects", "tasks", "convs", "chats", "routines", "memory", "rules", "skills", "agents", "decisions", "deliverables", "docs"]
AVISO = "<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->\n"
SECRETO = re.compile(r"(sk-ant-[A-Za-z0-9_-]{10,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----|xox[baprs]-[A-Za-z0-9-]{10,})")
ESTADO = {"prog": "Programado", "cola": "En cola", "marcha": "En marcha", "revision": "Calidad revisa", "maqueta": "Maquetando",
          "aprob": "Espera el OK de un socio", "preg": "Pregunta pendiente", "hecha": "Hecha", "rech": "Rechazada"}


def slug(t, n=50):
    t = re.sub(r"[^a-z0-9]+", "-", str(t).lower().translate(str.maketrans("áéíóúüñ", "aeiouun"))).strip("-")
    return t[:n].strip("-") or "sin-titulo"


def cargar(col):
    p = os.path.join(DATOS, f"{col}.jsonl")
    out = {}
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            if line.strip():
                r = json.loads(line)
                out[r["id"]] = r["data"]
    return out


def guardar(col, d):
    os.makedirs(DATOS, exist_ok=True)
    with open(os.path.join(DATOS, f"{col}.jsonl"), "w", encoding="utf-8") as f:
        for k in sorted(d):
            f.write(json.dumps({"id": k, "data": d[k]}, ensure_ascii=False, sort_keys=True) + "\n")


def leer_entrada(carpeta, col):
    p = os.path.join(carpeta, f"{col}.json")
    if not os.path.exists(p):
        return []
    j = json.load(open(p, encoding="utf-8"))
    if isinstance(j, dict) and "docs" in j:
        j = j["docs"]
    if isinstance(j, dict):
        j = [{"id": k, "data": v} for k, v in j.items()]
    return [r for r in j if isinstance(r, dict) and r.get("id") and isinstance(r.get("data"), dict)]


def fusionar(carpeta):
    total = {}
    db = {c: cargar(c) for c in COLS}
    for c in COLS:
        nuevos = 0
        entrada = leer_entrada(carpeta, c)
        if c == "chats":  # la oficina guarda solo los 30 últimos mensajes por agente: aquí se acumulan todos
            entrada = [{"id": f"{r['id']}|{m.get('t', i)}", "data": dict(m, agent=r["id"])} for r in entrada for i, m in enumerate(r["data"].get("list", []))]
        for r in entrada:
            d = dict(r["data"])
            if c == "docs":  # nunca el texto de documentos subidos
                d.pop("text", None)
            if SECRETO.search(json.dumps(d, ensure_ascii=False)):
                print(f"[omitido por posible secreto] {c}/{r['id']}")
                continue
            if db[c].get(r["id"]) != d:
                db[c][r["id"]] = d
                nuevos += 1
        total[c] = nuevos
    # proyectos confidenciales: fuera todo lo suyo
    conf = {k for k, p in db["projects"].items() if p.get("confidencial")}
    for c in COLS:
        for k in list(db[c]):
            v = db[c][k]
            if (c == "projects" and k in conf) or v.get("project") in conf:
                del db[c][k]
    for c in COLS:
        guardar(c, db[c])
    return db, total


def fecha(s):
    return str(s or "")[:10]


def lista(x):
    return "\n".join(f"- {i}" for i in x if i) or "—"


def write(rel, txt):
    p = os.path.join(MD, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(txt)


def nombre(agents_base, aid):
    return agents_base.get(aid, aid or "—")


def render(db):
    import shutil
    if os.path.isdir(MD):
        shutil.rmtree(MD)
    base = {}
    try:
        base = {k: v["nombre"] for k, v in json.load(open(os.path.join(ROOT, "oficina", "agentes.json"), encoding="utf-8"))["agentes"].items()}
    except Exception:
        pass
    n = lambda a: nombre(base, a)  # noqa: E731
    P, T, C, M = db["projects"], db["tasks"], db["convs"], db["memory"]

    # encargos (sin piezas sueltas: van dentro del encargo padre)
    idx = []
    for k, t in sorted(T.items(), key=lambda kv: str(kv[1].get("created", ""))):
        if t.get("piece") or t.get("deleted"):
            continue
        rel = f"encargos/{fecha(t.get('created'))[:7] or 'sin-fecha'}/{fecha(t.get('created'))}-{slug(t.get('title') or t.get('text'))}-{k[-5:]}.md"
        piezas = [T[p] for p in t.get("pieces", []) if p in T]
        proy = P.get(t.get("project") or "", {}).get("name", "")
        txt = [AVISO, f"# {t.get('title') or t.get('text', '')[:70]}\n",
               f"**Agente:** {n(t.get('agent'))} · **Estado:** {ESTADO.get(t.get('status'), t.get('status'))} · **Riesgo:** {t.get('risk') or '—'} · **Formato:** {t.get('format') or 'texto'}"
               + (f" · **Proyecto:** {proy}" if proy else "") + f" · **Creado:** {fecha(t.get('created'))}\n",
               "## Encargo\n", str(t.get("text", "")), ""]
        ceo = t.get("ceo") or {}
        if ceo:
            txt += ["## Contrato de tarea del CEO\n", f"- Decisión: {t.get('decision', '—')} · Motivo: {t.get('reason', '—')}",
                    f"- Objetivo: {ceo.get('objetivo') or '—'}", f"- Criterio de aceptación: {ceo.get('criterio') or '—'}",
                    f"- Confirmado: {'; '.join(ceo.get('confirmado') or []) or '—'}", f"- Inferido: {'; '.join(ceo.get('inferido') or []) or '—'}",
                    f"- Desconocido: {'; '.join(ceo.get('desconocido') or []) or '—'}", ""]
        if t.get("sectorNotes"):
            txt += ["## Claves del sector\n", str(t["sectorNotes"]), ""]
        if t.get("qa"):
            q = t["qa"]
            txt += ["## Revisión de Calidad\n", f"- Cumple: {'sí' if q.get('cumple') else 'no'} · {q.get('nota', '')}", lista(q.get("problemas") or []), ""]
        if t.get("result"):
            txt += ["## Resultado\n", str(t["result"]), ""]
        if piezas:
            txt += ["## Piezas del equipo\n"] + [f"### {n(p.get('agent'))}\n\n{p.get('result', '')}\n" for p in piezas]
        txt += ["## Historial\n", lista(f"{fecha(x.get('t'))} {str(x.get('t', ''))[11:16]} · {x.get('m', '')}" for x in t.get("log", []))]
        write(rel, "\n".join(txt) + "\n")
        idx.append((t.get("created", ""), rel, t))

    # conversaciones entre agentes
    conv_idx = []
    for k, c in sorted(C.items(), key=lambda kv: kv[1].get("started", 0)):
        if c.get("sim"):
            continue
        ts = c.get("startedIso") or ""
        rel = f"conversaciones/{fecha(ts)[:7] or 'sin-fecha'}/{fecha(ts)}-{slug(n(c.get('from')))}-a-{slug(n(c.get('to')))}-{k[-5:]}.md"
        txt = [AVISO, f"# {n(c.get('from'))} → {n(c.get('to'))}\n", f"**Motivo:** {c.get('reason') or '—'} · **Fecha:** {fecha(ts)}"
               + (f" · **Encargo:** {T.get(c.get('task'), {}).get('title', '')}" if c.get("task") else "") + "\n"]
        for l in c.get("lines", []):
            txt.append(f"**{n(l.get('from'))}:** {l.get('text', '')}\n")
        write(rel, "\n".join(txt))
        conv_idx.append(rel)

    # chats de los socios con cada agente
    porag = {}
    for k, m in sorted(db["chats"].items(), key=lambda kv: str(kv[1].get("t", ""))):
        porag.setdefault(m.get("agent"), []).append(m)
    for aid, L in porag.items():
        txt = [AVISO, f"# Conversaciones con {n(aid)}\n"]
        for m in L:
            quien = "Socio" if m.get("role") == "user" else n(aid)
            txt.append(f"**{quien}** · {fecha(m.get('t'))} {str(m.get('t', ''))[11:16]}\n\n{m.get('content', '')}\n")
        write(f"chats/{slug(n(aid))}.md", "\n".join(txt))

    # proyectos
    for k, p in P.items():
        if p.get("deleted"):
            continue
        tareas = [x for x in idx if x[2].get("project") == k]
        ent = [d for d in db["deliverables"].values() if d.get("project") == k]
        docs = [d for d in db["docs"].values() if d.get("project") == k and not d.get("deleted")]
        txt = [AVISO, f"# {p.get('name')}\n", f"**Cliente:** {p.get('client') or '—'} · **Tipo:** {p.get('type') or '—'} · **Estado:** {p.get('status') or 'abierto'}\n",
               f"**Objetivo:** {p.get('objective') or '—'}\n", f"**Alcance:** {p.get('scope') or '—'}\n", f"**Fuera de alcance:** {p.get('out') or '—'}\n",
               f"**Criterio de éxito:** {p.get('success') or '—'}\n", "## Encargos\n",
               lista(f"[{x[2].get('title')}](../{x[1]}) · {ESTADO.get(x[2].get('status'), '')}" for x in tareas), "",
               "## Entregables\n", lista(f"{d.get('title') or d.get('name')} · {d.get('kind')} v{d.get('version')} · {d.get('status', 'borrador')}" for d in ent), "",
               "## Documentos (solo nombres)\n", lista(d.get("name") for d in docs), ""]
        write(f"proyectos/{slug(p.get('name'))}.md", "\n".join(txt))

    # memoria: lecciones, correcciones, decisiones de los socios
    mem = sorted((m for m in M.values() if not m.get("deleted")), key=lambda m: str(m.get("created", "")), reverse=True)
    grupos = {}
    for m in mem:
        grupos.setdefault(m.get("kind", "otro"), []).append(m)
    txt = [AVISO, "# Memoria de la oficina\n", "Lo que la oficina ha aprendido: precedentes, lecciones, correcciones y decisiones de los socios. Lo lee el cerebro.\n"]
    for kind, L in sorted(grupos.items()):
        txt.append(f"## {kind.capitalize()} ({len(L)})\n")
        txt += [f"### {fecha(m.get('created'))} · {m.get('title', '')}\n\n{m.get('text', '')}\n" + (f"\n_Agente: {n(m.get('agent'))}_\n" if m.get("agent") else "") for m in L]
    write("memoria.md", "\n".join(txt))

    # reglas y habilidades enseñadas por los socios
    txt = [AVISO, "# Reglas y habilidades enseñadas en la oficina\n", "Lo que los socios han añadido a cada agente desde la oficina. Si una regla vale para siempre, pásala a `tools/org_data/agentes.py`.\n", "## Reglas fijas\n"]
    for aid, r in sorted(db["rules"].items()):
        if r.get("list"):
            txt += [f"### {n(aid)}\n", lista(r["list"]), ""]
    txt.append("## Habilidades propias\n")
    for k, s in sorted(db["skills"].items()):
        if not s.get("deleted"):
            txt += [f"### {s.get('name')}\n", f"**Cuándo:** {s.get('desc') or '—'} · **Para:** {', '.join(n(a) for a in s.get('agents', [])) or ', '.join(s.get('deps', [])) or '—'}\n", str(s.get("body", "")), ""]
    txt.append("## Fichas ajustadas en la oficina\n")
    for aid, o in sorted(db["agents"].items()):
        txt += [f"### {n(aid)}\n", lista(f"{k}: {v}" for k, v in o.items() if k != "id"), ""]
    write("reglas-y-habilidades.md", "\n".join(txt))

    # decisiones propuestas desde la oficina
    txt = [AVISO, "# Decisiones de la oficina\n", "Propuestas redactadas en la oficina. Solo son decisiones cuando un socio las pasa a DECISIONS.md.\n"]
    for k, d in sorted(db["decisions"].items(), key=lambda kv: str(kv[1].get("created", ""))):
        txt.append(f"## {d.get('title') or k} · {d.get('estado', 'propuesta')}\n\n{d.get('text') or d.get('decision') or ''}\n")
    write("decisiones.md", "\n".join(txt))

    # índice
    txt = [AVISO, "# Registro de la oficina de agentes\n",
           "Volcado automático de lo que pasa en la oficina (D-017). La copia fiel está en `oficina/registro/datos/`; aquí, la versión legible que entra en el cerebro.\n",
           f"- Encargos: {len(idx)} · Conversaciones: {len(conv_idx)} · Proyectos: {len([p for p in P.values() if not p.get('deleted')])} · Entradas de memoria: {len(mem)}\n",
           "- [Memoria](memoria.md) · [Reglas y habilidades](reglas-y-habilidades.md) · [Decisiones](decisiones.md)\n", "## Últimos encargos\n",
           lista(f"[{x[2].get('title')}]({x[1]}) · {n(x[2].get('agent'))} · {ESTADO.get(x[2].get('status'), '')}" for x in sorted(idx, key=lambda x: str(x[0]), reverse=True)[:30])]
    write("README.md", "\n".join(txt) + "\n")
    return len(idx), len(conv_idx)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    db, total = fusionar(sys.argv[1])
    e, c = render(db)
    cambios = ", ".join(f"{k} {v}" for k, v in total.items() if v)
    print("Nuevos o cambiados: " + (cambios or "nada"))
    print(f"Registro: {e} encargos, {c} conversaciones")
    return 0


if __name__ == "__main__":
    sys.exit(main())
