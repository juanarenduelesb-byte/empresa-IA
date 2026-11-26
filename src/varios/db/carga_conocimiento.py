"""Carga el conocimiento común del repositorio (knowledge/) en la base de datos (tarea B1, plan S7).

Cada sección de nivel 2 (`## ...`) de cada ficha Markdown es una ficha de conocimiento. Sus fuentes son:
- siempre, el propio documento del repositorio como fuente interna (`repo:<ruta>`), para saber de dónde sale;
- además, las fuentes externas del registro (`registro.md#<id>`) que cita la sección o, si no cita ninguna,
  las del documento entero.
El recuento `con_fuente_externa` mide cuánto del cerebro está respaldado por una fuente externa.
Se puede ejecutar tantas veces como se quiera: actualiza y no duplica. Lo ejecuta el propietario (conocimiento común).

Uso: VARIOS_DATABASE_URL_ADMIN=... python -m varios.db.carga_conocimiento
"""

from __future__ import annotations

import re
import uuid
from pathlib import Path

from sqlalchemy import create_engine, text

from varios.config import ajustes

from .semilla import _id, cargar

RAIZ = Path(__file__).resolve().parents[3]
EXCLUIR = ("knowledge/grafo/",)
CITA = re.compile(r"registro\.md#([a-z0-9][a-z0-9-]*)")
SECCION = re.compile(r"^## +(.+)$", re.M)
ESTADO = re.compile(r'^estado:\s*"?([a-z_]+)"?\s*$', re.M)
ESTADOS = {"raw", "draft", "validated", "approved", "deprecated", "disputed"}


def fichas(raiz: Path = RAIZ) -> list[dict]:
    """Trocea knowledge/ en fichas: {codigo, titulo, cuerpo, estado, origen, citas}."""
    salida = []
    for p in sorted((raiz / "knowledge").rglob("*.md")):
        rel = p.relative_to(raiz).as_posix()
        if any(rel.startswith(x) for x in EXCLUIR):
            continue
        texto = p.read_text(encoding="utf-8")
        estado = ESTADO.search(texto)
        estado = estado.group(1) if estado and estado.group(1) in ESTADOS else "draft"
        cuerpo_doc = re.sub(r"^---\n.*?\n---\n", "", texto, flags=re.S)
        citas_doc = sorted(set(CITA.findall(cuerpo_doc)))
        titulo_doc = next((x[2:].strip() for x in cuerpo_doc.splitlines() if x.startswith("# ")), p.stem)
        partes = SECCION.split(cuerpo_doc)
        secciones = [(titulo_doc, partes[0])] + [(partes[i], partes[i + 1]) for i in range(1, len(partes) - 1, 2)]
        for i, (titulo, cuerpo) in enumerate(secciones):
            cuerpo = cuerpo.strip()
            if len(cuerpo) < 40:
                continue
            citas = sorted(set(CITA.findall(cuerpo))) or citas_doc
            salida.append({
                "codigo": f"{rel}#{i}",
                "titulo": (titulo if i == 0 else f"{titulo_doc} · {titulo}")[:300],
                "cuerpo": cuerpo,
                "estado": estado,
                "origen": rel,
                "citas": citas,
            })
    return salida


def cargar_conocimiento(url: str, raiz: Path = RAIZ) -> dict[str, int]:
    cargar(url)  # fuentes comunes primero (idempotente)
    cuenta = {"fichas": 0, "con_fuente_externa": 0, "citas_sin_fuente": 0}
    e = create_engine(url)
    with e.begin() as c:
        filas = c.execute(text("SELECT codigo, id FROM fuente WHERE cliente_id IS NULL"))
        codigos = {r[0].lower(): r[1] for r in filas}
        vistos = []
        internas: dict[str, uuid.UUID] = {}
        for f in fichas(raiz):
            if f["origen"] not in internas:
                iid = _id("fuente", "repo", f["origen"])
                c.execute(text(
                    "INSERT INTO fuente (id, cliente_id, codigo, titulo, organismo, tipo, autoridad, estado) "
                    "VALUES (:i, NULL, :co, :t, 'Varios', 'interno', 'interna', 'draft') ON CONFLICT DO NOTHING"),
                    {"i": iid, "co": f"repo:{f['origen']}"[:80], "t": f["origen"]})
                internas[f["origen"]] = iid
            fid = _id("ficha", f["codigo"])
            c.execute(text(
                "INSERT INTO ficha_conocimiento (id, cliente_id, codigo, titulo, cuerpo, estado, etiquetas, origen) "
                "VALUES (:i, NULL, :co, :t, :b, :e, '[]', :o) "
                "ON CONFLICT ON CONSTRAINT uq_ficha_conocimiento_cliente_codigo DO UPDATE SET "
                "titulo = excluded.titulo, cuerpo = excluded.cuerpo, estado = excluded.estado, "
                "origen = excluded.origen, actualizado_en = now()"),
                {"i": fid, "co": f["codigo"], "t": f["titulo"], "b": f["cuerpo"], "e": f["estado"], "o": f["origen"]})
            c.execute(text("DELETE FROM ficha_fuente WHERE ficha_id = :i"), {"i": fid})
            c.execute(text("INSERT INTO ficha_fuente (ficha_id, fuente_id, cliente_id, cita) "
                           "VALUES (:f, :u, NULL, :c)"),
                      {"f": fid, "u": internas[f["origen"]], "c": f["titulo"][:300]})
            enlazadas = 0
            for cita in f["citas"]:
                fuente = codigos.get(cita)
                if fuente is None:
                    cuenta["citas_sin_fuente"] += 1
                    continue
                c.execute(text("INSERT INTO ficha_fuente (ficha_id, fuente_id, cliente_id, cita) "
                               "VALUES (:f, :u, NULL, :c)"), {"f": fid, "u": fuente, "c": f["origen"]})
                enlazadas += 1
            cuenta["fichas"] += 1
            cuenta["con_fuente_externa"] += bool(enlazadas)
            vistos.append(str(fid))
        # Lo que ya no está en el repositorio queda obsoleto, no se borra (trazabilidad).
        c.execute(text("UPDATE ficha_conocimiento SET estado = 'deprecated' WHERE cliente_id IS NULL "
                       "AND origen LIKE 'knowledge/%' AND NOT (id::text = ANY(:v))"), {"v": vistos})
    e.dispose()
    return cuenta


if __name__ == "__main__":
    url = ajustes().database_url_admin
    if not url:
        raise SystemExit("Falta VARIOS_DATABASE_URL_ADMIN")
    print(cargar_conocimiento(url))
