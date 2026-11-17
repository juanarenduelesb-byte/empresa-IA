#!/usr/bin/env python3
"""Genera el cerebro de la oficina de agentes a partir del repositorio.

Uso: python3 tools/brain_build.py oficina/brain.json

Lee los Markdown del repositorio (salvo archive/, site/ y oficina/), los trocea por
secciones, saca los enlaces entre documentos y las decisiones de DECISIONS.md.
La oficina usa el resultado para dar a cada agente las secciones que necesita.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = ("archive/", "site/", "oficina/", ".git/", "node_modules/")
MAX = 2200


def group(path):
    if "/" not in path:
        return 0
    if path.startswith("docs/fuentes/"):
        return 3
    if path.startswith("docs/atlas/"):
        return 2
    if path.startswith("docs/"):
        return 1
    return 4


def title_of(path, text):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    t = m.group(1).strip() if m else ""
    if not t or re.match(r"^\d+\.\s", t):
        t = re.sub(r"^\d+_\d+_", "", os.path.basename(path)[:-3]).replace("_", " ")
        t = t[:1].upper() + t[1:]
    return t.replace("`", "")


def summary_of(text):
    for para in re.split(r"\n\s*\n", text):
        p = para.strip()
        if p and not p.startswith(("#", "|", "```", "%%", "<", "-", "*", ">")):
            return re.sub(r"\s+", " ", p)[:240]
    return ""


def chunks_of(text):
    out, head, buf = [], "", []

    def flush():
        body = "\n".join(buf).strip()
        if not body:
            return
        while len(body) > MAX:
            cut = body.rfind("\n\n", 0, MAX)
            cut = cut if cut > MAX // 3 else MAX
            out.append((head, body[:cut].strip()))
            body = body[cut:].strip()
        if body:
            out.append((head, body))

    for line in text.splitlines():
        m = re.match(r"^(#{1,3})\s+(.+)$", line)
        if m:
            flush()
            buf = []
            head = m.group(2).strip()
        else:
            buf.append(line)
    flush()
    return out


def decisions(text):
    res = []
    for m in re.finditer(r"^## (D-\d{3})\s*[—-]\s*(.+?)\n(.*?)(?=^## |\Z)", text, re.M | re.S):
        body = m.group(3).strip()
        f = {}
        for k in ("Fecha", "Decisión", "Motivo", "Impacto", "Estado", "Riesgo aceptado"):
            mm = re.search(r"^- " + k + r":\s*(.+)$", body, re.M)
            if mm:
                f[k] = mm.group(1).strip()
        if "Estado" not in f:
            mm = re.search(r"Estado:\s*(.+?)\.?\s*$", body, re.M)
            if mm:
                f["Estado"] = mm.group(1).strip()
        for k in f:
            f[k] = f[k].rstrip(".")
        res.append({"id": m.group(1), "t": m.group(2).strip(), "f": f, "raw": body})
    pend = []
    m = re.search(r"^## Decisiones pendientes.*?\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if m:
        for line in m.group(1).splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2 and line.strip().startswith("|") and not re.match(r"^:?-+", cells[0]) and cells[0] != "Decisión":
                pend.append(cells)
    return res, pend


def main(dst):
    files = []
    for base, dirs, names in os.walk(ROOT):
        rel = os.path.relpath(base, ROOT)
        rel = "" if rel == "." else rel + "/"
        if any(rel.startswith(s) for s in SKIP) or any(part.startswith(".") for part in rel.split("/")[:-1]):
            continue
        for n in sorted(names):
            if n.endswith(".md"):
                files.append(rel + n)
    files.sort()
    ids = {p: "d%02d" % i for i, p in enumerate(files)}
    docs, chunks, links = [], [], set()
    names = {os.path.basename(p): p for p in files}
    for p in files:
        text = open(os.path.join(ROOT, p), encoding="utf-8").read()
        docs.append({"id": ids[p], "p": p, "t": title_of(p, text), "g": group(p), "s": summary_of(text), "n": len(text)})
        for h, body in chunks_of(text):
            chunks.append({"d": ids[p], "h": h, "t": body})
        here = os.path.dirname(p)
        for target in re.findall(r"\]\(([^)#\s]+\.md)", text):
            q = os.path.normpath(os.path.join(here, target)).replace("\\", "/")
            if q in ids and q != p:
                links.add(tuple(sorted((ids[p], ids[q]))))
        for target in re.findall(r"`([\w./-]+\.md)`", text):
            q = target if target in ids else names.get(os.path.basename(target))
            if q in ids and q != p:
                links.add(tuple(sorted((ids[p], ids[q]))))
    dec, pend = decisions(open(os.path.join(ROOT, "DECISIONS.md"), encoding="utf-8").read())
    procs = []
    pt = open(os.path.join(ROOT, "docs/13-procesos-y-estados.md"), encoding="utf-8").read()
    for m in re.finditer(r"^\|\s*(P\d{2})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", pt, re.M):
        procs.append([m.group(1), m.group(2), m.group(3)])
    out = {"built": __import__("datetime").date.today().isoformat(), "docs": docs, "links": sorted(links), "chunks": chunks, "decisions": dec, "pending": pend, "processes": procs}
    with open(dst, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, separators=(",", ":"))
    print("%d documentos, %d secciones, %d enlaces, %d decisiones, %d pendientes" % (len(docs), len(chunks), len(links), len(dec), len(pend)))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "oficina/brain.json")
