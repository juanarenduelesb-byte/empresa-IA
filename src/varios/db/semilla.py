"""Datos de ejemplo (plan S2 y A5). TODO INVENTADO: ningún dato real (D-011).

Carga, con la conexión de administrador:
- las fuentes comunes del registro (tools/org_data/fuentes.py), sin cliente;
- dos clientes inventados (una correduría y un señuelo) con dos usuarios cada uno y unas solicitudes;
- A5: las 11 pólizas y los 20 siniestros del proceso de referencia y los 25 encargos del Control A, leídos de sus
  archivos (`processes/…/casos/` y `processes/ceo-control-a/`) y repartidos entre los dos clientes (ver `REPARTO`).
Se puede ejecutar varias veces: no duplica (los identificadores son fijos).

Uso: VARIOS_DATABASE_URL_ADMIN=... python -m varios.db.semilla            (cargar)
     VARIOS_DATABASE_URL_ADMIN=... python -m varios.db.semilla --vaciar   (quitar los ejemplos de A5)
"""

from __future__ import annotations

import json
import sys
import uuid
from pathlib import Path

from sqlalchemy import create_engine, text

from varios.config import ajustes


def _raiz() -> Path:
    """En el repositorio, junto al código; instalado (imagen de Docker), en la carpeta de trabajo."""
    junto = Path(__file__).resolve().parents[3]
    return junto if (junto / "processes").is_dir() else Path.cwd()


RAIZ = _raiz()
CASOS = Path("processes/referencia-seguros-apertura-siniestros/casos")
CONTROL_A = Path("processes/ceo-control-a/encargos.json")
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


# --- A5: cómo se reparten los ejemplos entre los dos clientes (regla fija, para que cada uno tenga de todo) -------
# Las pólizas, por ramo; cada siniestro va con el cliente de su póliza (sin póliza, a Atalaya); los encargos del
# Control A se alternan en el orden del archivo (pares a Atalaya, impares al señuelo).
REPARTO_RAMO = {"hogar": "atalaya", "comercio": "atalaya", "automovil": "senuelo",
                "responsabilidad_civil": "senuelo", "accidentes": "senuelo"}
# Riesgo de un siniestro: alto si toca a personas, dinero o un juzgado (las mismas razones que las reglas fijas del
# CEO, `varios.ceo.decision.REGLAS`); si no, medio, porque abrirlo acaba en un envío a la aseguradora con el OK de un
# socio (D-019). Es una propuesta: lo ajusta quien valide los casos.
ALTO_SI = ("danos_personales", "vulnerable_o_fallecimiento", "movimiento_dinero", "reclamacion_judicial_o_atestado")


def _json(ruta: Path) -> dict:
    return json.loads((RAIZ / ruta).read_text(encoding="utf-8"))


def ejemplos() -> dict[str, list[dict]]:
    """Las filas de A5, ya repartidas, sin tocar la base. Las pruebas comparan esto con los archivos de casos."""
    from varios.ceo.decision import REGLAS  # noqa: PLC0415

    cartera = _json(CASOS / "cartera.json")["polizas"]
    de_poliza = {p["numero"]: REPARTO_RAMO[p["ramo"]] for p in cartera}
    polizas = [dict(p, cliente=REPARTO_RAMO[p["ramo"]]) for p in cartera]
    siniestros = []
    for c in _json(CASOS / "casos.json")["casos"]:
        h = c["hechos"]
        siniestros.append({"id": c["id"], "cliente": de_poliza.get(h.get("poliza_numero") or "", "atalaya"),
                           "titulo": f"Siniestro {c['id']}: {c['titulo']} (inventado)"[:300],
                           "descripcion": c["mensaje"],
                           "riesgo": "alto" if any(h.get(k) for k in ALTO_SI) else "medio"})
    encargos = []
    for i, e in enumerate(_json(CONTROL_A)["encargos"]):
        senales = e.get("senales", {})
        riesgo = next((r for nombre, _, r, _ in REGLAS if senales.get(nombre)), "bajo")
        encargos.append({"id": e["id"], "cliente": "atalaya" if i % 2 == 0 else "senuelo",
                         "titulo": f"Control A {e['id']}: {e['texto']}"[:300],
                         "descripcion": f"{e['texto']}\n\nEncargo inventado del banco del Control A ({e['tipo']}).",
                         "riesgo": riesgo})
    return {"polizas": polizas, "siniestros": siniestros, "encargos": encargos}


def _autor(slug: str) -> uuid.UUID:
    """El primer usuario operador del cliente: quien da de alta los ejemplos."""
    usuarios = next(u for s, _, u, _ in CLIENTES if s == slug)
    email = next(e for e, _, roles in usuarios if "operador" in roles)
    return _id("usuario", slug, email)


def _cargar_ejemplos(c) -> dict[str, int]:
    cuenta = {"polizas": 0, "siniestros": 0, "encargos_control_a": 0}
    ej = ejemplos()
    for slug, *_ in CLIENTES:
        c.execute(text("SELECT set_config('varios.cliente_id', :c, true)"), {"c": str(_id("cliente", slug))})
        for p in (x for x in ej["polizas"] if x["cliente"] == slug):
            r = c.execute(text("INSERT INTO poliza (id, cliente_id, numero, ramo, aseguradora, efecto, vencimiento) "
                               "VALUES (:i, :c, :n, :r, :a, :e, :v) ON CONFLICT DO NOTHING"),
                          {"i": _id("poliza", slug, p["numero"]), "c": _id("cliente", slug), "n": p["numero"],
                           "r": p["ramo"], "a": p.get("aseguradora", ""), "e": p["efecto"], "v": p["vencimiento"]})
            cuenta["polizas"] += r.rowcount
        for clave, tipo in (("siniestros", "siniestros"), ("encargos", "encargos_control_a")):
            for x in (y for y in ej[clave] if y["cliente"] == slug):
                r = c.execute(text("INSERT INTO solicitud (id, cliente_id, autor_id, titulo, descripcion, riesgo) "
                                   "VALUES (:i, :c, :a, :t, :d, :r) ON CONFLICT DO NOTHING"),
                              {"i": _id("ejemplo", slug, x["id"]), "c": _id("cliente", slug), "a": _autor(slug),
                               "t": x["titulo"], "d": x["descripcion"], "r": x["riesgo"]})
                cuenta[tipo] += r.rowcount
    return cuenta


def vaciar(url: str) -> dict[str, int]:
    """Quita los ejemplos de A5 (solo las filas con los identificadores fijos de la semilla; lo que hayan creado las
    personas no se toca). Sus tareas y aprobaciones se van con ellos; la auditoría no se borra nunca (es inmutable)."""
    cuenta = {"polizas": 0, "solicitudes": 0}
    ej = ejemplos()
    e = create_engine(url)
    with e.begin() as c:
        for slug, *_ in CLIENTES:
            c.execute(text("SELECT set_config('varios.cliente_id', :c, true)"), {"c": str(_id("cliente", slug))})
            ids = [_id("ejemplo", slug, x["id"]) for k in ("siniestros", "encargos") for x in ej[k]
                   if x["cliente"] == slug]
            pol = [_id("poliza", slug, p["numero"]) for p in ej["polizas"] if p["cliente"] == slug]
            cuenta["solicitudes"] += c.execute(text("DELETE FROM solicitud WHERE id = ANY(:i)"), {"i": ids}).rowcount
            cuenta["polizas"] += c.execute(text("DELETE FROM poliza WHERE id = ANY(:i)"), {"i": pol}).rowcount
    e.dispose()
    return cuenta


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
        cuenta.update(_cargar_ejemplos(c))
    e.dispose()
    return cuenta


if __name__ == "__main__":
    url = ajustes().database_url_admin
    if not url:
        raise SystemExit("Falta VARIOS_DATABASE_URL_ADMIN")
    print(vaciar(url) if "--vaciar" in sys.argv[1:] else cargar(url))
