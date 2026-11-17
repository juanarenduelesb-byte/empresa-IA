#!/usr/bin/env python3
"""Avisos semanales sin IA (D-017): decisiones pendientes, semana del plan y fuentes que revisar.

Lee DECISIONS.md, docs/10-plan-12-semanas.md y tools/org_data/fuentes.py, y escribe un resumen en Markdown.
Lo ejecuta GitHub Actions cada lunes y lo publica como issue; también se puede ejecutar a mano.
Uso: python3 tools/avisos.py [AAAA-MM-DD]
"""
import datetime as dt
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))


def fecha_es(s):
    m = re.search(r"(\d{1,2})/(\d{1,2})/(\d{4})", s)
    return dt.date(int(m.group(3)), int(m.group(2)), int(m.group(1))) if m else None


def pendientes(hoy):
    txt = open(os.path.join(ROOT, "DECISIONS.md"), encoding="utf-8").read()
    bloque = txt.split("## Decisiones pendientes", 1)[-1]
    out = []
    for linea in bloque.splitlines():
        cel = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(cel) >= 3 and cel[0] not in ("Decisión", "") and not set(cel[0]) <= set("-"):
            f = fecha_es(cel[2])
            out.append((f, cel[0], cel[1], cel[2]))
    venc = [x for x in out if x[0] and x[0] < hoy]
    prox = [x for x in out if x[0] and hoy <= x[0] <= hoy + dt.timedelta(days=14)]
    return venc, prox


def propuestas():
    txt = open(os.path.join(ROOT, "DECISIONS.md"), encoding="utf-8").read()
    out = []
    for m in re.finditer(r"^## (D-\d+) — (.+?)$(.*?)(?=^## |\Z)", txt, re.M | re.S):
        if re.search(r"Estado:\s*propuesta", m.group(3)):
            out.append(f"{m.group(1)} · {m.group(2)}")
    return out


def semana(hoy):
    txt = open(os.path.join(ROOT, "docs", "10-plan-12-semanas.md"), encoding="utf-8").read()
    for linea in txt.splitlines():
        cel = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(cel) >= 7 and cel[0].startswith("S") and re.match(r"S\d+", cel[0]):
            m = re.match(r"(\d{1,2})(?:\s*(\w+))?[–-](\d{1,2})\s*(\w+)", cel[1])
            if not m:
                continue
            meses = {"nov": 11, "dic": 12, "ene": 1, "feb": 2}
            mf = meses.get(m.group(4)[:3])
            mi = meses.get((m.group(2) or m.group(4))[:3])
            if not (mf and mi):
                continue
            yi = 2026 if mi >= 11 else 2027
            yf = 2026 if mf >= 11 else 2027
            ini, fin = dt.date(yi, mi, int(m.group(1))), dt.date(yf, mf, int(m.group(3)))
            if ini <= hoy <= fin:
                return cel
    return None


def fuentes():
    from org_data.fuentes import FUENTES

    return [f"{f['id']} · {f['titulo']} ({f['vigencia']}, {f['estado']})" for f in FUENTES
            if f.get("vigencia") in ("en-tramitacion", "anunciado-sin-norma", "borrador") or f.get("estado") == "disputed"]


def main():
    hoy = dt.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else dt.date.today()
    venc, prox = pendientes(hoy)
    s = semana(hoy)
    L = [f"# Avisos de la semana · {hoy.strftime('%d/%m/%Y')}\n", "Generado sin IA por `tools/avisos.py` (D-017).\n"]
    L.append("## Semana del plan\n")
    if s:
        L.append(f"**{s[0]} ({s[1]})** · {s[2]}\n\n- Juan: {s[3]}\n- Álvaro: {s[4]}\n- Hecho cuando: {s[5]}\n- Si da tiempo: {s[6]}\n")
    else:
        L.append("Fuera del calendario del plan de 12 semanas.\n")
    L.append("## Decisiones pendientes vencidas\n")
    L.append("\n".join(f"- **{d}** · {q} · vencía el {t}" for _, d, q, t in venc) or "Ninguna.")
    L.append("\n## Vencen en los próximos 14 días\n")
    L.append("\n".join(f"- **{d}** · {q} · antes del {t}" for _, d, q, t in prox) or "Ninguna.")
    pr = propuestas()
    L.append(f"\n## Decisiones en estado de propuesta ({len(pr)})\n")
    L.append("\n".join(f"- {x}" for x in pr) or "Ninguna.")
    fu = fuentes()
    L.append(f"\n## Fuentes que conviene revisar ({len(fu)})\n")
    L.append("\n".join(f"- {x}" for x in fu) or "Ninguna.")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
