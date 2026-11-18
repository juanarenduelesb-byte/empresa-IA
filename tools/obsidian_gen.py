"""Capa de Obsidian sobre el repositorio (D-003, D-021). Sin IA y determinista.

La llama tools/brain_build.py después de calcular el grafo. Escribe:
- knowledge/grafo/decisiones/D-0xx.md   una nota por decisión, con propiedades y quién la cita
- knowledge/grafo/fuentes/<ID>.md       una nota por fuente del registro, con vigencia y quién la cita
- knowledge/grafo/mapas/*.md            un mapa por comunidad del grafo y un mapa general
- knowledge/grafo/bases/*.base          vistas de tabla (plugin Bases, Obsidian 1.9 o posterior)
- .obsidian/{app,core-plugins,graph}.json solo si no existen: son ajustes que el usuario puede cambiar

Todo lo de knowledge/grafo/ se regenera entero: no se edita a mano.
"""
import json
import os
import re
import shutil
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "knowledge", "grafo")
AVISO = "<!-- Generado por tools/obsidian_gen.py. No editar a mano: se regenera con tools/brain_build.py. -->\n"

# Colores del grafo de Obsidian: la primera regla que encaja gana, así que lo concreto va antes.
COLORES = [
    ("path:knowledge/grafo/decisiones", 0xB83232),
    ("path:knowledge/grafo/fuentes", 0x7E520D),
    ("path:knowledge/grafo/mapas", 0x0C1416),
    ("path:knowledge/agentes", 0x0A6B76),
    ("path:claude/habilidades", 0x5ED3C8),
    ("path:processes", 0x4A5BC4),
    ("path:docs/fuentes", 0x56646A),
    ("path:docs", 0x166B3B),
    ("path:knowledge", 0x86DCD3),
    ("path:governance", 0xB26B3C),
    ("path:precedents", 0xA9BCFF),
]

BASES = {
    "agentes": ("Agentes de la oficina", 'tipo == "agente"', ["file.name", "departamento", "rol", "jefe", "habilidades", "estado"], "departamento"),
    "habilidades": ("Habilidades", 'tipo == "habilidad"', ["file.name", "usan", "estado"], None),
    "especialistas": ("Especialistas", 'tipo == "especialista"', ["file.name", "departamento", "puestos", "procesos", "estado"], "departamento"),
    "procesos": ("Procesos", 'tipo == "proceso"', ["id", "nombre", "especialistas", "estado"], None),
    "decisiones": ("Decisiones", 'tipo == "decision"', ["id", "titulo", "fecha", "estado", "citada"], "estado"),
    "fuentes": ("Fuentes", 'tipo == "fuente"', ["id", "titulo", "organismo", "autoridad", "vigencia", "estado", "citada"], "vigencia"),
}


def q(x):
    return json.dumps(str(x), ensure_ascii=False)


def fm(d):
    s = "---\n"
    for k, v in d.items():
        if isinstance(v, list):
            s += k + ":" + ("".join("\n  - " + q(i) for i in v) if v else " []") + "\n"
        elif isinstance(v, bool):
            s += f"{k}: {'true' if v else 'false'}\n"
        elif isinstance(v, (int, float)):
            s += f"{k}: {v}\n"
        else:
            s += f"{k}: {q(v)}\n"
    return s + "---\n"


def wl(ruta, texto=None):
    """Enlace de Obsidian a un archivo del repositorio (sin .md)."""
    r = ruta[:-3] if ruta.endswith(".md") else ruta
    t = (texto or "").replace("|", "·").replace("[", "(").replace("]", ")")
    return f"[[{r}|{t}]]" if t else f"[[{r}]]"


def nombre_seguro(s):
    return re.sub(r"[^A-Za-z0-9._-]+", "-", s).strip("-")


def escribir(rel, texto, solo_si_no_existe=False):
    p = os.path.join(ROOT, rel)
    if solo_si_no_existe and os.path.exists(p):
        return
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(texto)


def generar(G, A, decisiones):
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    from org_data.fuentes import FUENTES

    lab = {n[0]: n[2] for n in G.nodes}
    tipo = {n[0]: n[1] for n in G.nodes}
    ref = {n[0]: n[3] for n in G.nodes}
    sec_doc = {a: b for (a, b, r) in G.edges if r == "parte_de"}
    cat = os.path.join(ROOT, "processes", "catalog")
    proc_file = {f.split("-")[0]: "processes/catalog/" + f for f in sorted(os.listdir(cat)) if re.match(r"P\d\d-.*\.md$", f)}

    def enlace(u):
        t = tipo.get(u)
        if t == "decision":
            return wl(f"knowledge/grafo/decisiones/{u}", lab[u])
        if t == "fuente":
            return wl(f"knowledge/grafo/fuentes/{nombre_seguro(u[4:])}", lab[u])
        if t == "proceso" and u in proc_file:
            return wl(proc_file[u], lab[u])
        if ref.get(u, "").endswith(".md"):
            return wl(ref[u], lab[u])
        return lab.get(u, u)

    # quién cita a quién (documento → decisión o fuente)
    citan = defaultdict(set)
    for (a, b, r) in G.edges:
        if r in ("menciona", "cita") and tipo.get(b) in ("decision", "fuente"):
            d = sec_doc.get(a, a)
            if tipo.get(d) == "documento" and ref.get(d) not in ("DECISIONS.md", "knowledge/fuentes/registro.md"):
                citan[b].add(d)

    shutil.rmtree(OUT + "/decisiones", ignore_errors=True)
    shutil.rmtree(OUT + "/fuentes", ignore_errors=True)
    shutil.rmtree(OUT + "/mapas", ignore_errors=True)
    shutil.rmtree(OUT + "/bases", ignore_errors=True)

    def lista_citas(u):
        ds = sorted(citan[u], key=lambda d: ref[d])
        return "".join(f"- {wl(ref[d], lab[d])}\n" for d in ds) or "- Ningún documento la cita todavía.\n"

    # decisiones
    for d in decisiones:
        f = d.get("f", {})
        estado = (f.get("Estado") or "sin estado").split(";")[0].split(",")[0].strip().lower()
        cuerpo = re.sub(r"\n{3,}", "\n\n", d["raw"]).strip()
        escribir(f"knowledge/grafo/decisiones/{d['id']}.md",
                 fm({"tipo": "decision", "id": d["id"], "titulo": d["t"], "fecha": f.get("Fecha", ""), "estado": estado,
                     "citada": len(citan[d["id"]]), "tags": ["decision", "estado/" + nombre_seguro(estado)]})
                 + AVISO + f"# {d['id']} · {d['t']}\n\nOriginal: {wl('DECISIONS#' + d['id'] + ' — ' + d['t'], 'DECISIONS.md')}\n\n"
                 + cuerpo + "\n\n## Citada en\n\n" + lista_citas(d["id"]))

    # fuentes
    for fu in FUENTES:
        u = "fue:" + fu["id"]
        url = fu.get("url", "")
        origen = wl(url) if url and not url.startswith("http") and url.endswith(".md") else (f"<{url}>" if url else "sin enlace")
        escribir(f"knowledge/grafo/fuentes/{nombre_seguro(fu['id'])}.md",
                 fm({"tipo": "fuente", "id": fu["id"], "titulo": fu["titulo"], "organismo": fu.get("organismo", ""), "fuente_tipo": fu.get("tipo", ""),
                     "version": fu.get("version", ""), "autoridad": fu.get("autoridad", ""), "vigencia": fu.get("vigencia", ""),
                     "estado": fu.get("estado", ""), "citada": len(citan[u]), "tags": ["fuente", "vigencia/" + nombre_seguro(fu.get("vigencia", "") or "-")]})
                 + AVISO + f"# {fu['id']} · {fu['titulo']}\n\n- Origen: {origen}\n- Registro: {wl('knowledge/fuentes/registro', 'registro de fuentes')}\n"
                 + (f"- Nota: {fu['nota']}\n" if fu.get("nota") else "") + "\n## Citada en\n\n" + lista_citas(u))

    # mapas por comunidad
    idx = []
    for c in A["comunidades"]:
        if c["n"] < 3:
            continue
        nom = f"comunidad-{c['id']:02d}"
        idx.append((nom, c))
        por_tipo = defaultdict(list)
        for u in c["miembros"]:
            por_tipo[tipo[u]].append(u)
        s = fm({"tipo": "mapa", "comunidad": c["id"], "miembros": c["n"], "cohesion": c["cohesion"], "tags": ["mapa"]}) + AVISO
        s += f"# Comunidad {c['id']} · {c['etiqueta']}\n\n{c['n']} nodos agrupados por el algoritmo de Louvain. Cohesión {c['cohesion']}.\n"
        for t, titulo in (("documento", "Documentos"), ("decision", "Decisiones"), ("proceso", "Procesos"), ("agente", "Agentes"),
                          ("especialista", "Especialistas"), ("habilidad", "Habilidades"), ("fuente", "Fuentes")):
            if por_tipo[t]:
                s += f"\n## {titulo}\n\n" + "".join(f"- {enlace(u)}\n" for u in por_tipo[t][:60])
                if len(por_tipo[t]) > 60:
                    s += f"- … y {len(por_tipo[t]) - 60} más\n"
        escribir(f"knowledge/grafo/mapas/{nom}.md", s)

    s = fm({"tipo": "mapa", "tags": ["mapa"]}) + AVISO + "# Mapa del cerebro\n\nResumen del grafo calculado sin IA (D-018). El detalle está en " + wl("knowledge/grafo/INFORME", "el informe del grafo") + ".\n\n## Comunidades\n\n"
    s += "".join(f"- {wl('knowledge/grafo/mapas/' + n, 'Comunidad ' + str(c['id']) + ' · ' + c['etiqueta'])} ({c['n']} nodos)\n" for n, c in idx)
    s += "\n## Nodos centrales\n\n" + "".join(f"- {enlace(u)} · {g} vecinos\n" for g, u in A["centrales"])
    s += "\n## Puentes entre temas\n\n" + "".join(f"- {enlace(p['id'])} · conecta las comunidades {', '.join(map(str, p['conecta'][:6]))}\n" for p in A["puentes"])
    s += "\n## Preguntas abiertas\n\n" + "".join(f"- {p}  \n  {r}\n" for p, r in A["preguntas"])
    escribir("knowledge/grafo/mapas/Mapa del cerebro.md", s)

    # bases
    for nom, (titulo, filtro, orden, grupo) in BASES.items():
        b = "# Generado por tools/obsidian_gen.py. No editar a mano.\nfilters:\n  and:\n    - '" + filtro + "'\n"
        b += "views:\n  - type: table\n    name: " + q(titulo) + "\n    order:\n" + "".join(f"      - {o}\n" for o in orden)
        if grupo:
            b += f"    groupBy:\n      property: {grupo}\n      direction: ASC\n"
        if nom == "decisiones":
            b += "  - type: table\n    name: \"En propuesta\"\n    filters:\n      and:\n        - 'estado == \"propuesta\"'\n    order:\n" + "".join(f"      - {o}\n" for o in orden)
        if nom == "fuentes":
            b += "  - type: table\n    name: \"Por revisar\"\n    filters:\n      or:\n        - 'vigencia != \"vigente\"'\n        - 'estado != \"validated\"'\n    order:\n" + "".join(f"      - {o}\n" for o in orden)
        escribir(f"knowledge/grafo/bases/{nom}.base", b)

    # ajustes del vault: solo la primera vez, luego son del usuario
    escribir(".obsidian/app.json", json.dumps({
        "userIgnoreFilters": ["site/", "oficina/vendor/", "archive/", "node_modules/", ".github/"],
        "showUnsupportedFiles": False, "alwaysUpdateLinks": True, "newLinkFormat": "relative", "useMarkdownLinks": False,
    }, indent=2) + "\n", solo_si_no_existe=True)
    escribir(".obsidian/core-plugins.json", json.dumps([
        "file-explorer", "global-search", "switcher", "graph", "backlink", "outgoing-link", "tag-pane", "properties",
        "page-preview", "outline", "bases", "canvas", "bookmarks", "word-count", "file-recovery",
    ], indent=2) + "\n", solo_si_no_existe=True)
    escribir(".obsidian/graph.json", json.dumps({
        "search": "-path:archive -path:site -path:oficina", "showTags": False, "showAttachments": False, "hideUnresolved": True, "showOrphans": False,
        "colorGroups": [{"query": qy, "color": {"a": 1, "rgb": rgb}} for qy, rgb in COLORES],
        "showArrow": True, "textFadeMultiplier": 0, "nodeSizeMultiplier": 1.1, "lineSizeMultiplier": 1,
        "centerStrength": 0.5, "repelStrength": 12, "linkStrength": 1, "linkDistance": 160,
    }, indent=2) + "\n", solo_si_no_existe=True)
    return len(decisiones), len(FUENTES), len(idx)
