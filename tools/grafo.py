#!/usr/bin/env python3
"""Grafo de conocimiento del cerebro de Varios (D-018).

Convierte el repositorio en un grafo con nodos tipados y relaciones explicadas, sin IA y sin dependencias:
  - Nodos: documentos, secciones, decisiones (D-0xx), procesos (P01–P38), agentes de la oficina, especialistas,
    habilidades, fuentes, puertas (G0–G6, L0–L4) y departamentos.
  - Relaciones con etiqueta de confianza:
      EXTRACTADA (1.0)  está escrita en la fuente: un enlace, una mención de D-011, una ficha que dice «usa esta habilidad».
      INFERIDA (0.85 / 0.75 / 0.65)  dos secciones de documentos distintos tratan lo mismo (términos raros compartidos).
      AMBIGUA (0.5)     una referencia que encaja con varios destinos; se marca para revisarla.
  - Comunidades (Louvain), nodos centrales, puentes, conexiones sorprendentes, huecos y preguntas sugeridas.

Ideas tomadas de Graphify (github.com/Graphify-Labs/graphify, Apache-2.0): confianza por relación, comunidades
con etiquetas sin IA, nodos centrales, conexiones sorprendentes, preguntas sugeridas, informe del grafo,
consulta con presupuesto y «camino» con la confianza del eslabón más débil. El código es propio.

Uso:
  python3 tools/grafo.py consulta "pregunta"      subgrafo para una pregunta, con presupuesto de tokens
  python3 tools/grafo.py camino "A" "B"           cómo se conectan dos cosas
  python3 tools/grafo.py explica "X"              qué es X y con qué se relaciona
  python3 tools/grafo.py diff viejo.json nuevo.json
El grafo se genera dentro de oficina/brain.json con tools/brain_build.py, que también escribe knowledge/grafo/INFORME.md.
"""
import heapq
import json
import math
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

TIPOS = ["documento", "seccion", "decision", "proceso", "agente", "especialista", "habilidad", "fuente", "puerta", "departamento"]
RELS = ["parte_de", "enlaza", "menciona", "usa", "colabora_con", "se_apoya_en", "pertenece_a", "ejecuta", "cita",
        "responsable_de", "depende_de", "describe", "relacionada", "posible_enlace"]
TAGS = ["EXTRACTADA", "INFERIDA", "AMBIGUA"]
STOP = set("""para como este esta estos estas pero porque sobre entre desde hasta cuando donde quien quienes cual cuales
todo toda todos todas otro otra otros otras cada mismo misma solo sola tambien mas menos muy sin con por que los las
del una uno unos unas sus ser son fue han hay haya tiene tienen puede pueden debe deben hace hacen lo le les se su
nos ya no si al el la de en y o a es un ni the and for with this that from are was not you your will can
readme index md html json catalog process docs knowledge tools oficina site http https www github com""".split())


def limpio(t):
    """Texto sin código, diagramas, HTML, rutas ni destinos de enlaces: lo que se usa para comparar temas."""
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"<[^>]{0,400}>", " ", t)
    t = re.sub(r"\]\([^)]*\)", "]", t)
    t = re.sub(r"`[^`]*`", " ", t)
    t = re.sub(r"https?://\S+", " ", t)
    return t


def es_lista_de_enlaces(t):
    lineas = [x for x in t.splitlines() if x.strip()]
    if not lineas:
        return True
    enl = sum(1 for x in lineas if "](" in x or x.strip().startswith(("- [", "| [")))
    return enl / len(lineas) > 0.5 or len(limpio(t).strip()) < 120


def norm(s):
    s = unicodedata.normalize("NFD", str(s).lower())
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def toks(s):
    out = []
    for w in re.findall(r"[a-z0-9]{3,}", norm(s)):
        if w in STOP or w.isdigit():
            continue
        out.append(w[:-2] if len(w) > 6 and w.endswith("es") else w[:-1] if len(w) > 5 and w.endswith("s") else w)
    return out


class Grafo:
    def __init__(self):
        self.nodes = []  # [id, tipo, etiqueta, ref]
        self.idx = {}
        self.edges = {}  # (a, b, rel) -> [score, tag]

    def node(self, nid, tipo, label, ref=""):
        if nid not in self.idx:
            self.idx[nid] = len(self.nodes)
            self.nodes.append([nid, tipo, label, ref])
        return self.idx[nid]

    def edge(self, a, b, rel, score=1.0, tag="EXTRACTADA"):
        if a == b or a not in self.idx or b not in self.idx:
            return
        k = (a, b, rel)
        if k not in self.edges or self.edges[k][0] < score:
            self.edges[k] = [round(score, 2), tag]

    def adj(self, skip=("parte_de",)):
        A = defaultdict(dict)
        for (a, b, r), (s, t) in self.edges.items():
            if r in skip:
                continue
            for x, y in ((a, b), (b, a)):
                if A[x].get(y, (0,))[0] < s:
                    A[x][y] = (s, r, t)
        return A


# ------------------------------------------------------------------ construcción
def construir(docs, chunks, links, decisiones):
    """docs: [{id,p,t}], chunks: [{d,h,t}], links: [(id,id)], decisiones: [{id,t,raw}]."""
    from org_data.agentes import AGENTES, DEPS
    from org_data.especialistas import ESPECIALISTAS
    from org_data.fuentes import FUENTES
    from org_data.habilidades import HABILIDADES
    from org_data.procesos import PROCESOS

    G = Grafo()
    por_ruta = {d["p"]: d for d in docs}
    for d in docs:
        G.node(d["id"], "documento", d["t"], d["p"])
    for i, c in enumerate(chunks):
        G.node(f"c{i}", "seccion", c["h"] or por_ruta_titulo(docs, c["d"]), str(i))
        G.edge(f"c{i}", c["d"], "parte_de")
    for a, b in links:
        G.edge(a, b, "enlaza")
    dec_ids = {d["id"] for d in decisiones}
    for d in decisiones:
        G.node(d["id"], "decision", f"{d['id']} · {d['t']}", "DECISIONS.md")
    for p in PROCESOS:
        G.node(p["id"], "proceso", f"{p['id']} · {p['nombre']}", "")
    for k, n in DEPS.items():
        G.node("dep:" + k, "departamento", n)
    for e in ESPECIALISTAS:
        G.node("esp:" + e["id"], "especialista", e["nombre"], f"knowledge/{e['dep']}/{e['id']}.md")
    for h in HABILIDADES:
        G.node("hab:" + h["id"], "habilidad", h["nombre"], f"claude/habilidades/{h['id']}.md")
    for f in FUENTES:
        G.node("fue:" + f["id"], "fuente", f"{f['id']} · {f['titulo']}", "knowledge/fuentes/registro.md")
    for g in [f"G{i}" for i in range(7)] + [f"L{i}" for i in range(5)]:
        G.node(g, "puerta", g + (" (puerta de cliente)" if g[0] == "G" else " (puerta técnica)"))
    for a in AGENTES:
        G.node("ag:" + a["id"], "agente", a["nombre"], f"knowledge/agentes/{a['id']}.md")

    # relaciones estructuradas (fichas y catálogos): EXTRACTADAS
    for a in AGENTES:
        x = "ag:" + a["id"]
        G.edge(x, "dep:" + a["dep"], "pertenece_a")
        for h in a["habilidades"]:
            G.edge(x, "hab:" + h, "usa")
        for c, _ in a["colabora"]:
            G.edge(x, "ag:" + c, "colabora_con")
        for e in a["especialista"]:
            G.edge(x, "esp:" + e, "se_apoya_en")
    for e in ESPECIALISTAS:
        for p in e.get("procesos", []):
            G.edge("esp:" + e["id"], p, "ejecuta")
        for f in e.get("fuentes", []):
            G.edge("esp:" + e["id"], "fue:" + f, "cita")
    for p in PROCESOS:
        for d in p.get("depende", []) or []:
            for pid in re.findall(r"P\d{2}", str(d)):
                G.edge(p["id"], pid, "depende_de")
        for e in p.get("especialistas", []) or []:
            if "esp:" + str(e) in G.idx:
                G.edge("esp:" + str(e), p["id"], "responsable_de")
    # nodo ↔ documento que lo describe
    for nid, (tipo, label, ref) in [(n[0], (n[1], n[2], n[3])) for n in G.nodes]:
        if tipo in ("especialista", "habilidad", "agente") and ref in por_ruta:
            G.edge(por_ruta[ref]["id"], nid, "describe")
    for d in docs:
        m = re.match(r"processes/catalog/(P\d{2})-", d["p"])
        if m:
            G.edge(d["id"], m.group(1), "describe")
    if "DECISIONS.md" in por_ruta:
        for did in dec_ids:
            G.edge(por_ruta["DECISIONS.md"]["id"], did, "describe")

    # menciones en el texto: EXTRACTADAS si el destino existe; rotas al informe
    fuente_ids = sorted((f["id"] for f in FUENTES), key=len, reverse=True)
    rx_fuente = re.compile(r"(?<![\w-])(" + "|".join(re.escape(f) for f in fuente_ids) + r")(?![\w-])")
    rotas = Counter()
    for i, c in enumerate(chunks):
        t, s = c["t"], f"c{i}"
        for did in set(re.findall(r"\bD-\d{3}\b", t)):
            if did in dec_ids:
                G.edge(s, did, "menciona")
            else:
                rotas[did] += 1
        for pid in set(re.findall(r"\bP\d{2}\b", t)):
            if pid in G.idx:
                G.edge(s, pid, "menciona")
            elif int(pid[1:]) > 0:
                rotas[pid] += 1
        for fid in set(rx_fuente.findall(t)):
            G.edge(s, "fue:" + fid, "cita")
        for g in set(re.findall(r"\b([GL][0-6])\b", t)):
            if g in G.idx and re.search(r"puerta|gate|L0|G0|L[1-4]\b|G[1-6]\b", t):
                G.edge(s, g, "menciona")
    for d in decisiones:
        for did in set(re.findall(r"\bD-\d{3}\b", d.get("raw", ""))):
            if did in dec_ids and did != d["id"]:
                G.edge(d["id"], did, "menciona")

    # enlaces por nombre de archivo que encaja con varios destinos: AMBIGUOS
    base = defaultdict(list)
    for d in docs:
        base[os.path.basename(d["p"])].append(d["id"])
    for i, c in enumerate(chunks):
        for target in set(re.findall(r"`([\w.-]+\.md)`", c["t"])):
            cand = base.get(target, [])
            if len(cand) > 1:
                for dd in cand:
                    if dd != c["d"]:
                        G.edge(f"c{i}", dd, "posible_enlace", 0.5, "AMBIGUA")

    relacionar(G, chunks)
    return G, rotas


def por_ruta_titulo(docs, did):
    for d in docs:
        if d["id"] == did:
            return d["t"]
    return did


def relacionar(G, chunks, top=3):
    """Secciones de documentos distintos que comparten términos poco frecuentes: INFERIDAS."""
    N = len(chunks)
    tf = [Counter() if es_lista_de_enlaces(c["t"]) else Counter(toks(c["h"] + " " + c["h"] + " " + limpio(c["t"]))) for c in chunks]
    df = Counter(w for t in tf for w in t)
    lim = max(3, int(N * 0.04))
    vec, inv = [], defaultdict(list)
    for i, t in enumerate(tf):
        v = {w: (1 + math.log(f)) * math.log(N / df[w]) for w, f in t.items() if 2 <= df[w] <= lim}
        n = math.sqrt(sum(x * x for x in v.values())) or 1
        v = {w: x / n for w, x in v.items()}
        vec.append(v)
        for w, x in v.items():
            inv[w].append((i, x))
    for i, v in enumerate(vec):
        acc = defaultdict(float)
        for w, x in v.items():
            for j, y in inv[w]:
                if j != i and chunks[j]["d"] != chunks[i]["d"]:
                    acc[j] += x * y
        mejores = sorted(acc.items(), key=lambda kv: (-kv[1], kv[0]))[:top]
        for j, cos in mejores:
            sc = 0.85 if cos >= 0.5 else 0.75 if cos >= 0.35 else 0.65 if cos >= 0.25 else 0
            if sc:
                a, b = sorted((f"c{i}", f"c{j}"), key=lambda s: int(s[1:]))
                G.edge(a, b, "relacionada", sc, "INFERIDA")


# ------------------------------------------------------------------ análisis
def grafo_docs(G):
    """Vista agregada: documentos y entidades (las secciones se pliegan en su documento)."""
    sec_doc = {}
    for (a, b, r) in G.edges:
        if r == "parte_de":
            sec_doc[a] = b
    W = defaultdict(lambda: defaultdict(float))
    for (a, b, r), (s, t) in G.edges.items():
        if r == "parte_de":
            continue
        x, y = sec_doc.get(a, a), sec_doc.get(b, b)
        if x != y:
            W[x][y] += s
            W[y][x] += s
    return W


def louvain(W, pasos=8, gamma=1.6):
    """Louvain determinista sobre un grafo ponderado no dirigido {u: {v: w}}."""
    nodos = sorted(W)
    com = {u: u for u in nodos}
    grupo = {u: [u] for u in nodos}
    Wc = {u: dict(W[u]) for u in nodos}
    for _ in range(pasos):
        m2 = sum(sum(v.values()) for v in Wc.values()) or 1
        k = {u: sum(Wc[u].values()) for u in Wc}
        c = {u: u for u in Wc}
        tot = dict(k)
        cambio = True
        vueltas = 0
        while cambio and vueltas < 20:
            cambio, vueltas = False, vueltas + 1
            for u in sorted(Wc):
                cu = c[u]
                tot[cu] -= k[u]
                pesos = defaultdict(float)
                for v, w in Wc[u].items():
                    if v != u:
                        pesos[c[v]] += w
                mejor, ganancia = cu, pesos.get(cu, 0) - gamma * tot[cu] * k[u] / m2
                for cc, w in sorted(pesos.items()):
                    g = w - gamma * tot[cc] * k[u] / m2
                    if g > ganancia + 1e-12:
                        mejor, ganancia = cc, g
                c[u] = mejor
                tot[mejor] = tot.get(mejor, 0) + k[u]
                if mejor != cu:
                    cambio = True
        if all(c[u] == u for u in c):
            break
        nuevo = defaultdict(lambda: defaultdict(float))
        for u in Wc:
            for v, w in Wc[u].items():
                nuevo[c[u]][c[v]] += w
        grupo2 = defaultdict(list)
        for u in Wc:
            grupo2[c[u]].extend(grupo[u])
        grupo = dict(grupo2)
        Wc = {u: dict(v) for u, v in nuevo.items()}
    for cid, miembros in grupo.items():
        for u in miembros:
            com[u] = cid
    return com


def intermediacion(W, muestras=None):
    """Brandes sobre el grafo agregado (no ponderado)."""
    nodos = sorted(W)
    bc = dict.fromkeys(nodos, 0.0)
    for s in nodos if muestras is None else nodos[::max(1, len(nodos) // muestras)]:
        S, P, sigma, dist = [], defaultdict(list), dict.fromkeys(nodos, 0), dict.fromkeys(nodos, -1)
        sigma[s], dist[s], Q = 1, 0, [s]
        while Q:
            v = Q.pop(0)
            S.append(v)
            for w in W[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    Q.append(w)
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    P[w].append(v)
        delta = dict.fromkeys(nodos, 0.0)
        while S:
            w = S.pop()
            for v in P[w]:
                delta[v] += sigma[v] / sigma[w] * (1 + delta[w])
            if w != s:
                bc[w] += delta[w]
    n = len(nodos)
    f = 1 / ((n - 1) * (n - 2)) if n > 2 else 1
    return {u: x * f for u, x in bc.items()}


def analizar(G, chunks, rotas, decisiones):
    lab = {n[0]: n[2] for n in G.nodes}
    tipo = {n[0]: n[1] for n in G.nodes}
    ref = {n[0]: n[3] for n in G.nodes}
    W = grafo_docs(G)
    com = louvain(W)
    miembros = defaultdict(list)
    for u, c in com.items():
        miembros[c].append(u)
    # etiquetas sin IA: carpeta dominante + términos distintivos
    sec_doc = {a: b for (a, b, r) in G.edges if r == "parte_de"}
    por_doc = defaultdict(set)
    for i, c in enumerate(chunks):
        d = sec_doc.get(f"c{i}")
        if d in com and not es_lista_de_enlaces(c["t"]):
            por_doc[d].update(toks(c["h"] + " " + limpio(c["t"])))
    ndocs = len(por_doc) or 1
    dfg = Counter(w for ws in por_doc.values() for w in ws)
    textos = defaultdict(Counter)
    for d, ws in por_doc.items():
        textos[com[d]].update(w for w in ws if dfg[w] <= ndocs * 0.3 and len(w) > 4 and w.isalpha())
    glob = Counter()
    for t in textos.values():
        glob.update(set(t))
    comunidades = []
    orden = sorted(miembros, key=lambda c: (-len(miembros[c]), str(c)))
    for k, c in enumerate(orden):
        ms = sorted(miembros[c], key=lambda u: (-sum(W[u].values()), u))
        carpetas = Counter(os.path.dirname(ref[u]).split("/")[0] + ("/" + os.path.dirname(ref[u]).split("/")[1] if "/" in os.path.dirname(ref[u]) else "")
                           for u in ms if tipo[u] == "documento" and ref[u])
        t = textos.get(c, Counter())
        dist = sorted(((x / max(1, len(t)) ** 0 * math.log((len(textos) + 1) / (glob[w] + 0.5)) * (x / (dfg[w] or 1)), w) for w, x in t.items() if x >= 2), reverse=True)[:4]
        carpeta = carpetas.most_common(1)[0][0] if carpetas else ""
        if not carpeta:
            tipos = Counter(tipo[u] for u in ms)
            carpeta = {"agente": "Agentes de la oficina", "habilidad": "Habilidades", "proceso": "Procesos", "fuente": "Fuentes",
                       "especialista": "Especialistas", "decision": "Decisiones"}.get(tipos.most_common(1)[0][0], "")
        claves = [lab[u] for u in ms if tipo[u] in ("documento", "decision", "proceso", "agente", "habilidad", "especialista")][:2]
        etiqueta = (carpeta + " · " if carpeta else "") + " y ".join(claves)
        interno = sum(1 for u in ms for v in W[u] if com.get(v) == c) / 2
        n = len(ms)
        comunidades.append({"id": k, "etiqueta": etiqueta or f"Comunidad {k}", "n": n, "cohesion": round(interno / (n * (n - 1) / 2), 2) if n > 1 else 1.0,
                            "miembros": ms})
    cid = {u: comunidades[k]["id"] for k, c in enumerate(orden) for u in miembros[c]}
    # nodos centrales: grado en el grafo agregado (vecinos distintos)
    centrales = sorted(((len(W[u]), u) for u in W), key=lambda x: (-x[0], x[1]))[:15]
    bc = intermediacion(W, muestras=None if len(W) <= 700 else 300)
    puentes = []
    for u, x in sorted(bc.items(), key=lambda kv: (-kv[1], kv[0]))[:10]:
        otras = sorted({cid[v] for v in W[u] if cid.get(v) != cid.get(u)})
        if otras:
            puentes.append({"id": u, "bc": round(x, 3), "comunidad": cid.get(u), "conecta": otras})
    # conexiones sorprendentes: INFERIDAS fuertes entre comunidades y carpetas distintas
    sorpresas = []
    for (a, b, r), (s, t) in G.edges.items():
        if r != "relacionada" or s < 0.75:
            continue
        da, db = sec_doc.get(a), sec_doc.get(b)
        if not da or not db or cid.get(da) == cid.get(db):
            continue
        ca, cb = ref[da].split("/")[0], ref[db].split("/")[0]
        if ca == cb:
            continue
        sorpresas.append((s, a, b))
    sorpresas.sort(key=lambda x: (-x[0], x[1], x[2]))
    # huecos
    grado = defaultdict(int)
    for (a, b, r) in G.edges:
        if r != "parte_de":
            grado[sec_doc.get(a, a)] += 1
            grado[sec_doc.get(b, b)] += 1
    huerfanos = sorted(u for u in lab if tipo[u] == "documento" and not grado[u])
    menc = Counter()
    for (a, b, r) in G.edges:
        if r in ("menciona", "cita") and a.startswith("c"):
            menc[b] += 1
    dec_sin = sorted(d["id"] for d in decisiones if not menc[d["id"]])
    proc_sin = sorted(u for u in lab if tipo[u] == "proceso" and not any(b == u and r in ("ejecuta", "responsable_de") for (a, b, r) in G.edges))
    fue_sin = sorted(u for u in lab if tipo[u] == "fuente" and not menc[u] and not any(b == u and r == "cita" for (a, b, r) in G.edges))
    ambiguas = sorted({(sec_doc.get(a, a), b) for (a, b, r), (s, t) in G.edges.items() if t == "AMBIGUA"})
    # decisiones en propuesta muy citadas: candidatas a aprobar
    estado = {d["id"]: (d.get("f", {}).get("Estado") or "") for d in decisiones}
    prop_citadas = sorted(((menc[d], d) for d in estado if "propuesta" in estado[d].lower() and menc[d] >= 3), key=lambda x: (-x[0], x[1]))
    preguntas = []
    for p in puentes[:3]:
        preguntas.append((f"¿Por qué «{lab[p['id']]}» conecta la comunidad {p['comunidad']} con las comunidades {', '.join(map(str, p['conecta'][:4]))}?",
                          f"Intermediación alta ({p['bc']}): es un puente entre temas."))
    for n_, d in prop_citadas[:3]:
        preguntas.append((f"¿Se aprueba {lab[d]}? Sigue en propuesta y la citan {n_} secciones.", "Una decisión en propuesta que ya sostiene mucho contenido."))
    for s, a, b in sorpresas[:2]:
        preguntas.append((f"¿Deberían enlazarse «{ref[sec_doc[a]]}» y «{ref[sec_doc[b]]}»?", f"Tratan lo mismo (relación INFERIDA {s}) pero no se citan."))
    if dec_sin:
        preguntas.append((f"¿Siguen vigentes {', '.join(dec_sin[:4])}? Ningún documento las cita.", "Decisiones que nadie menciona."))
    for r_, n_ in rotas.most_common(2):
        preguntas.append((f"¿Qué es {r_}? Se menciona {n_} veces pero no existe en el registro.", "Referencia rota."))
    tags = Counter(t for (a, b, r), (s, t) in G.edges.items() if r != "parte_de")
    return {"comunidades": comunidades, "cid": cid, "centrales": centrales, "puentes": puentes, "sorpresas": sorpresas[:12],
            "huerfanos": huerfanos, "dec_sin": dec_sin, "proc_sin": proc_sin, "fue_sin": fue_sin, "ambiguas": ambiguas[:20],
            "rotas": rotas, "prop_citadas": prop_citadas, "preguntas": preguntas, "tags": tags}


# ------------------------------------------------------------------ salida
def a_json(G, A):
    """Formato compacto para brain.json: índices de nodo, relación y etiqueta."""
    ri, ti = {r: i for i, r in enumerate(RELS)}, {t: i for i, t in enumerate(TAGS)}
    nodos = [[n[0], TIPOS.index(n[1]), n[2], n[3], A["cid"].get(n[0], -1)] for n in G.nodes if n[1] != "seccion"]
    pos = {n[0]: i for i, n in enumerate(nodos)}
    def ref(x):  # secciones como -1-indice para no duplicarlas
        return pos[x] if x in pos else -1 - int(x[1:])
    aristas = sorted([ref(a), ref(b), ri[r], int(s * 100), ti[t]] for (a, b, r), (s, t) in G.edges.items() if r != "parte_de")
    com = [{"id": c["id"], "etiqueta": c["etiqueta"], "n": c["n"], "cohesion": c["cohesion"], "top": [pos[u] for u in c["miembros"][:8] if u in pos]}
           for c in A["comunidades"]]
    lab = {n[0]: n[2] for n in G.nodes}
    return {"tipos": TIPOS, "rels": RELS, "tags": TAGS, "nodos": nodos, "aristas": aristas, "comunidades": com,
            "centrales": [[pos[u], g] for g, u in A["centrales"] if u in pos],
            "puentes": [[pos[p["id"]], p["bc"], p["conecta"]] for p in A["puentes"] if p["id"] in pos],
            "preguntas": [[q, w] for q, w in A["preguntas"]],
            "huecos": {"documentos_sin_enlaces": [lab[u] for u in A["huerfanos"]], "decisiones_sin_citar": A["dec_sin"],
                       "procesos_sin_responsable": A["proc_sin"], "fuentes_sin_citar": [x[4:] for x in A["fue_sin"]],
                       "referencias_rotas": dict(A["rotas"].most_common(20))}}


def informe(G, A, chunks):
    lab = {n[0]: n[2] for n in G.nodes}
    ref = {n[0]: n[3] for n in G.nodes}
    tipo = {n[0]: n[1] for n in G.nodes}
    sec_doc = {a: b for (a, b, r) in G.edges if r == "parte_de"}
    nt = Counter(n[1] for n in G.nodes)
    tot = sum(A["tags"].values()) or 1
    L = ["<!-- Generado por tools/brain_build.py (tools/grafo.py). No editar a mano. -->",
         "# Informe del grafo de conocimiento\n",
         "Cómo está conectado el cerebro de Varios: qué sostiene todo, qué temas forman grupos, qué conecta temas distintos, qué falta y qué preguntas conviene hacerse. Se regenera con el cerebro (D-018); no forma parte del grafo.\n",
         "## Resumen\n",
         f"- {len(G.nodes)} nodos: " + ", ".join(f"{k} {v}" for k, v in nt.most_common()) + ".",
         f"- {tot} relaciones: {round(100 * A['tags']['EXTRACTADA'] / tot)} % EXTRACTADAS (escritas en la fuente), "
         f"{round(100 * A['tags']['INFERIDA'] / tot)} % INFERIDAS (temas compartidos, con puntuación) y {A['tags']['AMBIGUA']} AMBIGUAS (para revisar).",
         f"- {len(A['comunidades'])} comunidades de temas.\n",
         "## Nodos centrales\n", "Lo que más cosas conecta. Si cambia, cambia mucho.\n"]
    L += [f"{i}. **{lab[u]}**{' (`' + ref[u] + '`)' if ref[u] and tipo[u] == 'documento' else ''} · {g} conexiones" for i, (g, u) in enumerate(A["centrales"][:12], 1)]
    L += ["", "## Puentes entre temas\n", "Nodos por los que pasa el camino entre comunidades distintas (intermediación).\n"]
    L += [f"- **{lab[p['id']]}** · intermediación {p['bc']} · une la comunidad {p['comunidad']} con {', '.join(map(str, p['conecta'][:6]))}" for p in A["puentes"]]
    L += ["", "## Conexiones sorprendentes\n", "Secciones de carpetas y comunidades distintas que tratan lo mismo y no se enlazan. Relación INFERIDA: compruébala.\n"]
    for s, a, b in A["sorpresas"][:10]:
        L.append(f"- `{ref[sec_doc[a]]}` › {lab[a]}  ↔  `{ref[sec_doc[b]]}` › {lab[b]}  [INFERIDA {s}]")
    L += ["", "## Comunidades\n"]
    for c in A["comunidades"]:
        nombres = [lab[u] for u in c["miembros"][:8]]
        L.append(f"### {c['id']} · {c['etiqueta']}\n\nCohesión {c['cohesion']} · {c['n']} nodos: {'; '.join(nombres)}{' (y ' + str(c['n'] - 8) + ' más)' if c['n'] > 8 else ''}\n")
    L += ["## Huecos\n",
          f"- **Documentos sin ninguna relación** ({len(A['huerfanos'])}): " + ("; ".join(f"`{ref[u]}`" for u in A["huerfanos"][:25]) or "ninguno") + ("…" if len(A["huerfanos"]) > 25 else ""),
          f"- **Decisiones que no cita ninguna sección** ({len(A['dec_sin'])}): " + (", ".join(A["dec_sin"]) or "ninguna"),
          f"- **Procesos sin especialista responsable** ({len(A['proc_sin'])}): " + (", ".join(A["proc_sin"]) or "ninguno"),
          f"- **Fuentes registradas que nadie cita** ({len(A['fue_sin'])}): " + (", ".join(x[4:] for x in A["fue_sin"]) or "ninguna"),
          f"- **Referencias rotas** (se citan pero no existen): " + (", ".join(f"{k} ×{v}" for k, v in A["rotas"].most_common(15)) or "ninguna"),
          f"- **Enlaces ambiguos** (un nombre de archivo con varios destinos): {len(A['ambiguas'])}" + ("".join(f"\n  - `{ref.get(a, a)}` → `{ref[b]}`" for a, b in A["ambiguas"][:10])),
          "", "## Preguntas sugeridas\n", "_Preguntas que este grafo ayuda a responder o que conviene decidir:_\n"]
    L += [f"- **{q}**\n  _{w}_" for q, w in A["preguntas"]]
    L += ["", "## Cómo usarlo\n",
          "- En la oficina, cada agente recibe las secciones que encajan con su encargo **y lo conectado a ellas** (decisiones, procesos, fuentes y secciones relacionadas), con la etiqueta de confianza de cada relación.",
          "- En local: `python3 tools/grafo.py consulta \"pregunta\"`, `camino \"A\" \"B\"` y `explica \"X\"`.",
          "- Las relaciones INFERIDAS son pistas, no hechos: si una es buena, conviértela en un enlace en el documento y pasará a EXTRACTADA.", ""]
    return "\n".join(L)


# ------------------------------------------------------------------ consulta (CLI)
def cargar(path=os.path.join(ROOT, "oficina", "brain.json")):
    B = json.load(open(path, encoding="utf-8"))
    g = B["graph"]
    nodos = g["nodos"]
    def nid(x):
        return nodos[x][0] if x >= 0 else f"c{-1 - x}"
    lab = {n[0]: n[2] for n in nodos}
    tipo = {n[0]: g["tipos"][n[1]] for n in nodos}
    titulo = {d["id"]: d["t"] for d in B["docs"]}
    for i, c in enumerate(B["chunks"]):
        lab[f"c{i}"] = titulo.get(c["d"], c["d"]) + (" › " + c["h"] if c["h"] else "")
        tipo[f"c{i}"] = "seccion"
    B["_tipo"] = tipo
    A = defaultdict(list)
    for a, b, r, s, t in g["aristas"]:
        x, y = nid(a), nid(b)
        A[x].append((y, g["rels"][r], s / 100, g["tags"][t]))
        A[y].append((x, "←" + g["rels"][r], s / 100, g["tags"][t]))
    return B, lab, A


PRIO = {"decision": 0.4, "proceso": 0.4, "agente": 0.35, "especialista": 0.3, "habilidad": 0.3, "fuente": 0.3, "puerta": 0.3,
        "departamento": 0.2, "documento": 0.2, "seccion": 0}


def buscar(B, lab, q):
    qt = set(toks(q))
    tipo = B["_tipo"]
    res = []
    for k, v in lab.items():
        lt = set(toks(v))
        bonus = PRIO.get(tipo.get(k), 0)
        if k.lower() == q.lower() or norm(q) == norm(v) or norm(v).startswith(norm(q) + " ·"):
            res.append((100 + bonus, k))
        elif qt and qt <= lt:
            res.append((len(qt) / (len(lt) or 1) + bonus, k))
    res.sort(key=lambda x: (-x[0], len(lab[x[1]]), x[1]))
    return res


def elegir(B, lab, q):
    r = buscar(B, lab, q)
    if not r:
        print(f"Nada encaja con «{q}».")
        sys.exit(4)
    if len(r) > 1 and r[0][0] == r[1][0] and r[0][0] < 100:
        print(f"«{q}» es ambiguo. Candidatos:\n" + "\n".join(f"- {lab[k]} ({B['_tipo'].get(k)}, {k})" for _, k in r[:8]))
        sys.exit(3)
    return r[0][1]


def camino(a, b):
    B, lab, A = cargar()
    s, t = elegir(B, lab, a), elegir(B, lab, b)
    dist, prev, pq = {s: 0}, {}, [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if u == t:
            break
        if d > dist[u]:
            continue
        for v, r, sc, tag in A[u]:
            nd = d + 1 + (1 - sc) * 2
            if nd < dist.get(v, 1e9):
                dist[v], prev[v] = nd, (u, r, sc, tag)
                heapq.heappush(pq, (nd, v))
    if t not in prev:
        print("No hay camino.")
        return 1
    pasos, u = [], t
    while u != s:
        p, r, sc, tag = prev[u]
        pasos.append((p, r, sc, tag, u))
        u = p
    pasos.reverse()
    T = B["_tipo"]
    for p, r, sc, tag, u in pasos:
        flecha = f"<--{r[1:]}--" if r.startswith("←") else f"--{r}-->"
        print(f"{lab[p]} ({T.get(p)}) {flecha} {lab[u]} ({T.get(u)})  [{tag} {sc}]")
    print(f"Confianza del camino: {min(x[2] for x in pasos)} (la del eslabón más débil)")
    return 0


def explica(x):
    B, lab, A = cargar()
    u = elegir(B, lab, x)
    print(f"# {lab[u]}  ({B['_tipo'].get(u)}, {u})")
    for v, r, sc, tag in sorted(A[u], key=lambda e: (-e[2], e[1], lab[e[0]]))[:40]:
        print(f"- {r} → {lab[v]}  [{tag} {sc}]")
    return 0


def consulta(q, presupuesto=2000):
    B, lab, A = cargar()
    qt = toks(q)
    df = Counter(w for c in B["chunks"] for w in set(toks(c["h"] + " " + c["t"])))
    N = len(B["chunks"])
    sc = []
    for i, c in enumerate(B["chunks"]):
        t = Counter(toks(c["h"] * 3 + " " + c["t"]))
        s = sum((1 + math.log(t[w])) * math.log(N / df[w]) for w in qt if t[w])
        if s:
            sc.append((s, f"c{i}"))
    sc.sort(key=lambda x: (-x[0], x[1]))
    semillas = [k for _, k in sc[:4]]
    out, vistos = [], set(semillas)
    for k in semillas:
        out.append(f"[{lab[k]}]")
        for v, r, s, tag in sorted(A[k], key=lambda e: (-e[2], e[0])):
            if v not in vistos and (tag == "EXTRACTADA" or s >= 0.75):
                vistos.add(v)
                out.append(f"  --{r}--> {lab[v]}  [{tag} {s}]")
    txt = "\n".join(out)
    print(txt[: presupuesto * 3])
    return 0


def diff(viejo, nuevo):
    a, b = json.load(open(viejo, encoding="utf-8")).get("graph", {}), json.load(open(nuevo, encoding="utf-8"))["graph"]
    na, nb = {n[0] for n in a.get("nodos", [])}, {n[0] for n in b["nodos"]}
    print(f"Nodos: +{len(nb - na)} −{len(na - nb)} · Relaciones: {len(a.get('aristas', []))} → {len(b['aristas'])} · Comunidades: {len(a.get('comunidades', []))} → {len(b['comunidades'])}")
    for x in sorted(nb - na)[:20]:
        print(f"+ {x}")
    for x in sorted(na - nb)[:20]:
        print(f"− {x}")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        sys.exit(2)
    f = {"consulta": lambda: consulta(" ".join(a[1:])), "camino": lambda: camino(a[1], a[2]), "explica": lambda: explica(" ".join(a[1:])),
         "diff": lambda: diff(a[1], a[2])}.get(a[0])
    sys.exit(f() if f else 2)
