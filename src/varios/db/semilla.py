"""Datos de ejemplo (plan S2, «si da tiempo»). TODO INVENTADO: ningún dato real (D-011).

Carga, con la conexión de administrador:
- las fuentes comunes del registro (tools/org_data/fuentes.py), sin cliente;
- dos clientes inventados (una correduría y un señuelo) con dos usuarios cada uno y unas solicitudes.
Se puede ejecutar varias veces: no duplica.

Uso: VARIOS_DATABASE_URL_ADMIN=... python -m varios.db.semilla
"""

from __future__ import annotations

import sys
import uuid
from pathlib import Path

from sqlalchemy import create_engine, text

from varios.config import ajustes

RAIZ = Path(__file__).resolve().parents[3]
ESPACIO = uuid.UUID("6f1c2d3e-0000-4000-8000-000000000000")  # para ids estables

CLIENTES = [
    ("atalaya", "Correduría Atalaya (inventada)", [
        ("tramitador@atalaya.invalid", "Tramitadora (inventada)", ["operador"]),
        ("gerente@atalaya.invalid", "Gerente (inventado)", ["aprobador"]),
    ], [
        ("Abrir siniestro de hogar por daños por agua (caso inventado)", "bajo"),
        ("Abrir siniestro de autos con daños personales (caso inventado)", "alto"),
    ]),
    ("senuelo", "Señuelo de aislamiento (inventado)", [
        ("persona@senuelo.invalid", "Persona señuelo", ["aprobador"]),
        ("otra@senuelo.invalid", "Otra persona señuelo", ["operador"]),
    ], [
        ("Solicitud que nadie de otro cliente debe ver", "bajo"),
    ]),
]


def _id(*partes: str) -> uuid.UUID:
    return uuid.uuid5(ESPACIO, "/".join(partes))


def cargar(url: str) -> dict[str, int]:
    sys.path.insert(0, str(RAIZ / "tools"))
    from org_data.fuentes import FUENTES  # noqa: PLC0415

    cuenta = {"fuentes": 0, "clientes": 0, "usuarios": 0, "solicitudes": 0}
    e = create_engine(url)
    with e.begin() as c:
        for f in FUENTES:
            r = c.execute(text(
                "INSERT INTO fuente (id, cliente_id, codigo, titulo, organismo, url, tipo, autoridad, vigencia, "
                "estado) VALUES (:i, NULL, :co, :t, :o, :u, :ti, :a, :v, :e) ON CONFLICT DO NOTHING"),
                {"i": _id("fuente", f["id"]), "co": f["id"], "t": f["titulo"][:500], "o": f.get("organismo", "")[:200],
                 "u": f.get("url", "")[:1000], "ti": f.get("tipo", "")[:60], "a": f.get("autoridad", "")[:20],
                 "v": f.get("vigencia", "")[:60], "e": f.get("estado", "draft")[:20]})
            cuenta["fuentes"] += r.rowcount
        for slug, nombre, usuarios, solicitudes in CLIENTES:
            cid = _id("cliente", slug)
            r = c.execute(text("INSERT INTO cliente (id, nombre, slug) VALUES (:i, :n, :s) ON CONFLICT DO NOTHING"),
                          {"i": cid, "n": nombre, "s": slug})
            cuenta["clientes"] += r.rowcount
            c.execute(text("SELECT set_config('varios.cliente_id', :c, true)"), {"c": str(cid)})
            autor = None
            for email, nom, roles in usuarios:
                uid = _id("usuario", slug, email)
                autor = autor or uid
                r = c.execute(text("INSERT INTO usuario (id, cliente_id, email, nombre, roles) "
                                   "VALUES (:i, :c, :e, :n, CAST(:r AS json)) ON CONFLICT DO NOTHING"),
                              {"i": uid, "c": cid, "e": email, "n": nom, "r": str(roles).replace("'", '"')})
                cuenta["usuarios"] += r.rowcount
            for titulo, riesgo in solicitudes:
                r = c.execute(text("INSERT INTO solicitud (id, cliente_id, autor_id, titulo, riesgo) "
                                   "VALUES (:i, :c, :a, :t, :r) ON CONFLICT DO NOTHING"),
                              {"i": _id("solicitud", slug, titulo), "c": cid, "a": autor, "t": titulo, "r": riesgo})
                cuenta["solicitudes"] += r.rowcount
    e.dispose()
    return cuenta


if __name__ == "__main__":
    url = ajustes().database_url_admin
    if not url:
        raise SystemExit("Falta VARIOS_DATABASE_URL_ADMIN")
    print(cargar(url))
