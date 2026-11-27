#!/usr/bin/env python3
"""Genera el conocimiento organizativo y el catálogo de procesos desde tools/org_data/.

Uso: python3 tools/org_gen.py            (escribe en el repositorio)
     python3 tools/org_gen.py --check    (falla si lo generado no coincide con lo guardado)

No edites a mano los archivos generados: cambia tools/org_data/ y vuelve a generar.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from org_data.especialistas import DEPARTAMENTOS, ESPECIALISTAS  # noqa: E402
from org_data.fuentes import CONSULTA, FUENTES  # noqa: E402
from org_data.procesos import PROCESOS  # noqa: E402

AVISO = "<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->\n"
FUENTE = {f["id"]: f for f in FUENTES}
ESP = {e["id"]: e for e in ESPECIALISTAS}
PRO = {p["id"]: p for p in PROCESOS}
DEP = {d[0]: d for d in DEPARTAMENTOS}
TIPO = {"regla": "Regla (código)", "ia": "IA propone", "humano": "Persona", "sistema": "Sistema"}
OUT = {}



def fm(d):
    """Propiedades de Obsidian (YAML plano) al principio de la nota."""
    def v(x):
        if isinstance(x, bool):
            return " true" if x else " false"
        if isinstance(x, (int, float)):
            return " " + str(x)
        if isinstance(x, list):
            return "\n" + "".join("  - " + json.dumps(str(i), ensure_ascii=False) + "\n" for i in x) if x else " []"
        return " " + json.dumps(str(x), ensure_ascii=False)
    return "---\n" + "".join(k + ":" + (v(x) if isinstance(x, list) else v(x)) + ("" if isinstance(x, list) and x else "\n") for k, x in d.items()) + "---\n"


def slug(t):
    t = t.lower()
    for a, b in (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"), ("ñ", "n"), ("ü", "u")):
        t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60]


def pfile(p):
    return "processes/catalog/%s-%s.md" % (p["id"], slug(p["nombre"]))


def efile(e):
    return "knowledge/%s/%s.md" % (e["dep"], e["id"])


def rel(frm, to):
    return os.path.relpath(to, os.path.dirname(frm)).replace("\\", "/")


IDS_FUENTE = re.compile(r"(?<![\w-])(" + "|".join(sorted((re.escape(x["id"]) for x in FUENTES if "-" in x["id"]), key=len, reverse=True)) + r"|MEDDICC)(?![\w-])")


def link_ref(frm, ref):
    """Convierte ids de fuente y de proceso en enlaces."""
    def f(m):
        i = m.group(0)
        if i in FUENTE:
            return "[%s](%s#%s)" % (i, rel(frm, "knowledge/fuentes/registro.md"), i.lower())
        return i
    # Cualquier id del registro con guion (LEY-10-2025, DGSFP-MEDIACION…) y MEDDICC. Antes solo se enlazaban
    # algunos prefijos y las citas como LEY-… o UNESPA-… quedaban sin enlace ni cómputo de fuente externa (K1).
    ref = re.sub(IDS_FUENTE, f, ref)

    def pp(m):
        i = m.group(0)
        return "[%s](%s)" % (i, rel(frm, pfile(PRO[i]))) if i in PRO else i
    return re.sub(r"\bP(0[1-9]|[12][0-9]|3[0-8])\b", pp, ref)


def bl(frm, items, vacio="—"):
    if not items:
        return vacio + "\n"
    return "".join("- %s\n" % link_ref(frm, x) for x in items)


def path_link(frm, p):
    target = p.rstrip("/")
    if "*" in target:
        return "`%s`" % p
    return "[`%s`](%s)" % (p, rel(frm, target))


# ---------------- Especialistas ----------------
def ficha(e):
    fn = efile(e)
    d = DEP[e["dep"]]
    s = fm({"tipo": "especialista", "id": e["id"], "departamento": e["dep"], "puestos": e.get("oficina", []), "procesos": e.get("procesos", []), "estado": "draft", "tags": ["especialista", "area/" + e["dep"]]}) + AVISO + "# %s\n\n" % e["nombre"]
    s += "**Departamento:** [%s](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** %s\n\n" % (d[1], CONSULTA)
    s += "**Puestos de la oficina que lo cubren:** %s\n\n" % (", ".join("`%s`" % o for o in e["oficina"]) or "ninguno todavía")
    s += "> %s\n\n" % e["mision"]
    s += "## 1. Índice del especialista\n\n"
    s += "### Responsabilidades\n" + bl(fn, e["responsabilidades"])
    s += "\n### Qué consultar antes de empezar\n" + "".join("- %s\n" % path_link(fn, c) for c in e["consulta"])
    s += "\n### Procesos que puede ejecutar\n" + "".join("- [%s · %s](%s)\n" % (p, PRO[p]["nombre"], rel(fn, pfile(PRO[p]))) for p in e["procesos"])
    s += "\n### Herramientas\n" + bl(fn, e["herramientas"])
    conv = []
    for c in e["convoca"]:
        cid = c.split(" ")[0]
        conv.append(("[%s](%s)%s" % (ESP[cid]["nombre"], rel(fn, efile(ESP[cid])), c[len(cid):])) if cid in ESP else c)
    s += "\n### A quién convoca\n" + "".join("- %s\n" % c for c in conv)
    s += "\n### Permisos\n" + bl(fn, e["permisos"])
    s += "\n### Qué requiere aprobación\n" + bl(fn, e["aprobacion"])
    s += "\n### Plantillas\n" + bl(fn, e["plantillas"])
    s += "\n### Precedentes que debe revisar\n" + bl(fn, e["precedentes"], "Todavía no hay precedentes de este tipo.")
    s += "\n## 2. Conocimiento profesional\n\n"
    for t, k in (("Fundamentos y terminología", "fundamentos"), ("Metodologías y marcos", "metodologias"), ("Normativa aplicable", "normativa"), ("Herramientas y tecnologías", "herramientas_tec"), ("Procedimiento de trabajo", "procedimiento"), ("Casos y escenarios", "casos"), ("Criterio profesional", "criterio"), ("Errores habituales", "errores"), ("KPI", "kpis"), ("Límites de actuación", "limites")):
        s += "### %s\n" % t + bl(fn, e[k], "Sin contenido verificado todavía.") + "\n"
    s += "### Relaciones con otros departamentos\nVer *A quién convoca* y [`knowledge/navigation.json`](%s).\n\n" % rel(fn, "knowledge/navigation.json")
    s += "## 3. Fuentes\n" + "".join("- [%s](%s#%s) · %s\n" % (f, rel(fn, "knowledge/fuentes/registro.md"), f.lower(), FUENTE[f]["titulo"]) for f in e["fuentes"])
    s += "\n## 4. Lagunas conocidas\n" + bl(fn, e["lagunas"], "Ninguna registrada; revisar al primer encargo real.")
    OUT[fn] = s


def dep_readme(d):
    fn = "knowledge/%s/README.md" % d[0]
    s = AVISO + "# %s\n\n%s\n\n| Especialista | Puestos de la oficina | Procesos |\n|---|---|---|\n" % (d[1], d[2])
    for e in ESPECIALISTAS:
        if e["dep"] == d[0]:
            s += "| [%s](%s) | %s | %s |\n" % (e["nombre"], os.path.basename(efile(e)), ", ".join(e["oficina"]) or "—", ", ".join(e["procesos"]))
    if d[0] == "procesos":
        s += "\nEl conocimiento de cada sector está en el departamento de [Sectores](../sectores/README.md).\n"
    if d[0] == "sectores":
        s += "\n**Por qué estos sectores:** [priorizacion.md](priorizacion.md) (propuesta, con fuentes y criterios).\n"
        s += "\n**Primer paquete sectorial:** [seguros](seguros/README.md) (normas con artículo, glosario, excepciones y `dominio.json`, que leen las reglas del proceso de referencia; D-024).\n\n> Estado draft. Son hipótesis hasta validarlas con profesionales de cada sector. No se abre un segundo paquete sectorial hasta validar el primero (Atlas §11).\n"
    if d[0] == "seguridad-legal":
        s += "\n> Estado draft. Nada de esto es asesoría jurídica: antes de usarlo con un cliente, revisión de un profesional competente.\n"
    OUT[fn] = s


# ---------------- Navegación ----------------
TAREAS = [
    ("propuesta-comercial", "Preparar una propuesta o responder a un pliego", ["propuestas-licitaciones", "director-comercial"], ["legal-privacidad", "ciberseguridad", "costes-proveedores"], ["P31", "P38"], ["docs/00-negocio.md", "knowledge/comercial/", "knowledge/estudios/", "knowledge/seguridad-legal/"], "Comercial consulta a Legal antes de cualquier cláusula contractual."),
    ("validacion", "Preparar o resumir una conversación de validación", ["director-comercial"], ["arquitecto-procesos", "especialista-sectorial"], ["P32"], ["processes/referencia-seguros-apertura-siniestros/README.md", "docs/10-plan-12-semanas.md"], "Se escucha, no se vende (D-011)."),
    ("descubrir-proceso", "Descubrir o diseñar un proceso de cliente", ["arquitecto-procesos"], ["especialista-sectorial", "metricas", "legal-privacidad"], ["P32", "P33", "P34"], ["processes/templates/proceso-cliente.md", "knowledge/sectores/README.md"], "Validar con quien ejecuta el proceso."),
    ("automatizacion", "Diseñar una automatización", ["automatizacion", "arquitecto-procesos"], ["arquitecto-tecnico", "ciberseguridad"], ["P08", "P21", "P22", "P36"], ["integrations/catalog/README.md", "processes/definitions/"], "Procesos consulta a Ingeniería antes de diseñar una automatización."),
    ("integracion", "Habilitar una integración o conector", ["integraciones"], ["ciberseguridad", "legal-privacidad"], ["P21", "P30", "P36"], ["integrations/catalog/README.md", "integrations/contracts/"], "Ingeniería consulta a Seguridad antes de habilitar una integración."),
    ("aprobar-plan", "Aprobar un plan o tomar una decisión", ["ceo-digital", "decisiones-seguimiento"], ["calidad-riesgos"], ["P05", "P10"], ["DECISIONS.md", "precedents/"], "El CEO consulta precedentes y decisiones antes de aprobar un plan."),
    ("regulatorio", "Investigar una obligación legal o regulatoria", ["legal-privacidad", "cumplimiento"], ["especialista-sectorial", "bibliotecario"], ["P19", "P24"], ["docs/fuentes/Marco_Integral_Legal_Ciberseguridad_IA_Espana_UE_2026-11-16.md", "knowledge/fuentes/registro.md"], "Fuente primaria y vigente; nunca afirmar cumplimiento."),
    ("sector-seguros", "Trabajo en el sector seguros", ["especialista-sectorial"], ["arquitecto-procesos", "cumplimiento"], ["P02", "P32", "P33"], ["knowledge/sectores/seguros/README.md", "knowledge/sectores/README.md", "processes/referencia-seguros-apertura-siniestros/README.md"], "El especialista de seguros consulta también los procesos transversales."),
    ("sector", "Trabajo en otro sector (sanidad, despachos, finanzas, industria, logística)", ["especialista-sectorial"], ["sector-sanidad", "sector-despachos", "sector-financiero", "sector-industria", "sector-logistica"], ["P02", "P32", "P33"], ["knowledge/sectores/README.md", "knowledge/sectores/priorizacion.md"], "La coordinación sectorial elige al experto; el experto consulta a Legal si hay datos sensibles."),
    ("cambio-modelo", "Cambiar de modelo o de instrucciones", ["datos-ia", "evaluacion-ia"], ["calidad-riesgos"], ["P16", "P23", "P25"], ["docs/atlas/10-cambios-modelos.md", "processes/tests/README.md"], "Sin evaluación superada no hay cambio."),
    ("incidente", "Gestionar un incidente", ["ciberseguridad", "calidad-riesgos"], ["legal-privacidad"], ["P28", "P15", "P17"], ["processes/runbooks/", "precedents/incidents/"], "Preservar evidencias antes de corregir."),
    ("conocimiento", "Añadir o actualizar conocimiento", ["bibliotecario"], ["el dueño del tema"], ["P13", "P04"], ["knowledge/metodologias-transversales/", "knowledge/fuentes/registro.md"], "Buscar antes de crear; draft hasta revisión."),
    ("proveedor", "Dar de alta un proveedor o herramienta", ["costes-proveedores"], ["legal-privacidad", "ciberseguridad", "arquitecto-tecnico"], ["P27", "P29"], ["integrations/catalog/README.md", "knowledge/plantillas/ficha-proveedor.md"], "Licencia, datos, región, retención, salida."),
    ("escribir-cliente", "Escribir algo que leerá un cliente o el público (correo, propuesta, web, informe)", ["propuestas-licitaciones", "director-comercial"], ["calidad-riesgos", "legal-privacidad"], ["P31", "P32"], ["knowledge/identidad/README.md", "knowledge/identidad/voz.md", "knowledge/identidad/manifiesto.md"], "Sin clientes, cifras ni testimonios inventados; lo legal, con prudencia."),
    ("facturacion", "Facturar o preparar trámites", ["administrativo", "financiero"], [], ["P11"], ["knowledge/administracion-finanzas/"], "Fechas de Verifactu y factura electrónica según norma vigente."),
]


def navegacion():
    nav = {"generado_por": "tools/org_gen.py", "consulta_fuentes": CONSULTA, "siempre": ["DECISIONS.md", "CLAUDE.md", "knowledge/INDEX.md", "precedents/README.md"], "tareas": [], "especialistas": {}}
    for t in TAREAS:
        nav["tareas"].append({"id": t[0], "tarea": t[1], "responsables": t[2], "consultar_a": t[3], "procesos": t[4], "leer": t[5], "regla_cruzada": t[6]})
    for e in ESPECIALISTAS:
        nav["especialistas"][e["id"]] = {"nombre": e["nombre"], "departamento": e["dep"], "ficha": efile(e), "oficina": e["oficina"], "procesos": e["procesos"], "leer": e["consulta"], "convoca": [c.split(" ")[0] for c in e["convoca"]]}
    OUT["knowledge/navigation.json"] = json.dumps(nav, ensure_ascii=False, indent=1) + "\n"
    fn = "knowledge/INDEX.md"
    s = AVISO + "# Índice del conocimiento de Varios\n\nPunto de entrada para cualquier especialista, humano o agente. Antes de empezar una tarea:\n\n"
    s += "1. Lee [DECISIONS.md](../DECISIONS.md) y [CLAUDE.md](../CLAUDE.md).\n2. Busca precedentes en [precedents/](../precedents/README.md) ([protocolo](metodologias-transversales/consultar-historico.md)).\n3. Localiza tu tarea en la tabla y abre lo que indica.\n4. Si investigas fuera, sigue [investigar.md](metodologias-transversales/investigar.md) y registra la fuente.\n\n"
    s += "Versión para máquinas: [navigation.json](navigation.json).\n\n## Por tipo de tarea\n\n| Tarea | Responsable | Consultar a | Procesos | Leer | Regla cruzada |\n|---|---|---|---|---|---|\n"
    for t in TAREAS:
        s += "| %s | %s | %s | %s | %s | %s |\n" % (t[1], ", ".join("[%s](%s)" % (ESP[r]["nombre"], rel(fn, efile(ESP[r]))) for r in t[2]), ", ".join(("[%s](%s)" % (ESP[r]["nombre"], rel(fn, efile(ESP[r])))) if r in ESP else r for r in t[3]) or "—", ", ".join("[%s](%s)" % (p, rel(fn, pfile(PRO[p]))) for p in t[4]), "<br>".join(path_link(fn, x) for x in t[5]), t[6])
    s += "\n## Por departamento\n\n"
    for d in DEPARTAMENTOS:
        s += "### [%s](%s/README.md)\n%s\n\n" % (d[1], d[0], d[2])
        for e in ESPECIALISTAS:
            if e["dep"] == d[0]:
                s += "- [%s](%s)%s\n" % (e["nombre"], rel(fn, efile(e)), " · sin puesto en la oficina" if not e["oficina"] else "")
        s += "\n"
    s += "## Transversal\n\n- [Identidad de la empresa](identidad/README.md) (manifiesto, forma de trabajar y voz) · [Fuentes](fuentes/registro.md) · [Metodologías](metodologias-transversales/README.md) · [Plantillas](plantillas/README.md) · [Glosario](glosario/README.md) · [Estudios](estudios/README.md)\n- [Catálogo de procesos P01–P38](../processes/catalog/README.md) · [Integraciones](../integrations/catalog/README.md) · [Precedentes](../precedents/README.md) · [Gobierno](../governance/README.md)\n"
    OUT[fn] = s


# ---------------- Fuentes ----------------
def fuentes():
    fn = "knowledge/fuentes/registro.md"
    s = AVISO + "# Registro de fuentes\n\nConsultadas el %s salvo las que indican otra fecha en su ficha. Tipos: obligación legal, estándar voluntario, recomendación técnica, buena práctica, documentación de producto, prensa especializada e interno. Estado: validated (contrastada con dos fuentes), draft (una fuente o secundaria), disputed (contradictoria o anunciada sin norma).\n\n" % CONSULTA
    s += "> Las fuentes secundarias (despachos, blogs) se marcan como tales. Antes de usar una afirmación legal en un documento para un cliente, ve al texto oficial.\n\n"
    s += "| Id | Fuente | Tipo | Autoridad | Vigencia | Estado |\n|---|---|---|---|---|---|\n"
    for f in FUENTES:
        s += "| [%s](#%s) | %s | %s | %s | %s | %s |\n" % (f["id"], f["id"].lower(), f["titulo"], f["tipo"], f["autoridad"], f["vigencia"], f["estado"])
    s += "\n"
    for f in FUENTES:
        url = f["url"] if f["url"].startswith("http") else rel(fn, f["url"])
        s += '<a id="%s"></a>\n### %s\n- **Título:** %s\n- **Autor u organismo:** %s\n- **URL:** <%s>\n- **Tipo:** %s · **Jurisdicción:** %s · **Versión o fecha:** %s\n- **Consultada:** %s · **Autoridad:** %s · **Vigencia:** %s · **Estado:** %s\n' % (f["id"].lower(), f["id"], f["titulo"], f["organismo"], url, f["tipo"], f["jurisdiccion"], f["version"], f.get("consultada", CONSULTA), f["autoridad"], f["vigencia"], f["estado"])
        usos = [e["nombre"] for e in ESPECIALISTAS if f["id"] in e["fuentes"]]
        s += "- **Especialistas relacionados:** %s\n" % (", ".join(usos) or "—")
        if f["nota"]:
            s += "- **Nota:** %s\n" % f["nota"]
        s += "\n"
    OUT[fn] = s
    OUT["knowledge/fuentes/fuentes.json"] = json.dumps({"consulta": CONSULTA, "fuentes": FUENTES}, ensure_ascii=False, indent=1) + "\n"


# ---------------- Procesos ----------------
CAMPOS = ["Descripción y objetivo", "Evento de inicio", "Condiciones y datos de entrada", "Actividades y tareas", "Responsables", "Departamentos y especialistas", "Decisiones y reglas", "Estados y transiciones", "Entradas y salidas de cada tarea", "Sistemas y conectores", "Permisos y controles", "Excepciones y rutas alternativas", "Aprobaciones humanas", "Timeouts y reintentos", "Criterio de finalización", "Evidencias que se conservan", "KPI", "Dependencias", "Precedentes y plantillas", "Pruebas necesarias"]


def mermaid(p):
    lines = ["flowchart TD", '  S(["%s"])' % p["inicio"].replace('"', "'")[:70]]
    prev = "S"
    shape = {"regla": ("[", "]"), "ia": ("[/", "/]"), "humano": ("[[", "]]"), "sistema": ("(", ")")}
    for i, (t, ty, _) in enumerate(p["actividades"]):
        n = "A%d" % i
        a, b = shape[ty]
        lines.append('  %s%s"%s · %s"%s' % (n, a, TIPO[ty], t.replace('"', "'")[:70], b))
        lines.append("  %s --> %s" % (prev, n))
        prev = n
    lines.append('  F(["%s"])' % p["fin"].replace('"', "'")[:70])
    lines.append("  %s --> F" % prev)
    if p["excepciones"]:
        lines.append('  X{{"Excepción: %s"}}' % p["excepciones"][0].replace('"', "'")[:70])
        lines.append("  A0 -. fallo .-> X")
        lines.append('  X -. "P22 / P28" .-> E(["Bloqueado o escalado con evidencia"])')
    return "\n".join(lines)


def proceso(p):
    fn = pfile(p)
    nombres = [ESP[e]["nombre"] for e in p["especialistas"]]
    s = fm({"tipo": "proceso", "id": p["id"], "nombre": p["nombre"], "estado": "draft", "especialistas": p.get("especialistas", []) or [], "tags": ["proceso"]}) + AVISO + "# %s · %s\n\n" % (p["id"], p["nombre"])
    s += "**Origen:** %s · **Cuándo implantar:** %s · **Estado de la ficha:** draft · **Implementado:** %s\n\n" % (p["origen"], p["cuando"], p["implementado"])
    s += "```mermaid\n%s\n```\n\nLeyenda: rectángulo, regla en código · paralelogramo, la IA propone · doble barra, persona · redondeado, sistema.\n\n" % mermaid(p)
    vals = [
        p["objetivo"], p["inicio"], p["entradas"],
        "".join("%d. %s (%s)\n" % (i + 1, a[0], TIPO[a[1]]) for i, a in enumerate(p["actividades"])),
        p["responsables"],
        "".join("- [%s](%s)\n" % (ESP[e]["nombre"], rel(fn, efile(ESP[e]))) for e in p["especialistas"]),
        bl(fn, p["reglas"]), p["estados"],
        "| Tarea | Tipo | Salida |\n|---|---|---|\n" + "".join("| %s | %s | %s |\n" % (a[0], TIPO[a[1]], a[2]) for a in p["actividades"]),
        bl(fn, p["sistemas"], "Motor de procesos y PostgreSQL (por defecto)."), bl(fn, p["permisos"], "Mínimos para la tarea; cliente derivado de la identidad."),
        bl(fn, p["excepciones"], "Errores según P22; incidentes según P28."), bl(fn, p["aprobaciones"], "Según la matriz de riesgo (docs/14)."), p["timeouts"], p["fin"],
        bl(fn, p["evidencias"], "Evento de auditoría por transición."), bl(fn, p["kpis"]), bl(fn, p["depende"]), bl(fn, p["plantillas"], "Ninguna todavía."), bl(fn, p["pruebas"]),
    ]
    for i, (c, v) in enumerate(zip(CAMPOS, vals)):
        v = v if v.endswith("\n") else v + "\n"
        s += "## %d. %s\n%s\n" % (i + 1, c, link_ref(fn, v) if i in (0, 1, 2, 4, 7, 13, 14) else v)
    s += "---\nEspecialistas: %s. Definición original: %s.\n" % (", ".join(nombres), p["origen"])
    OUT[fn] = s


def catalogo():
    fn = "processes/catalog/README.md"
    s = AVISO + "# Catálogo de procesos P01–P38\n\nP01–P30 vienen de la Guía de Arranque v1.4 y P31–P38 del Atlas Evolución v1.1, que sigue en estado de propuesta. No se renumera nada. Cada ficha tiene los 20 apartados del prompt maestro, en estado draft.\n\n"
    s += "Ciclo completo de un encargo: [diagrams/ciclo-encargo.md](../diagrams/ciclo-encargo.md) · Dependencias: [diagrams/dependencias.md](../diagrams/dependencias.md) · Definiciones ejecutables: [definitions/](../definitions/README.md)\n\n"
    s += "| Id | Proceso | Origen | Cuándo | Implementado | Especialistas |\n|---|---|---|---|---|---|\n"
    for p in PROCESOS:
        s += "| %s | [%s](%s) | %s | %s | %s | %s |\n" % (p["id"], p["nombre"], os.path.basename(pfile(p)), "Guía v1.4" if p["origen"] == PROCESOS[0]["origen"] else "Atlas v1.1 (propuesta)", p["cuando"], p["implementado"].split(":")[0], ", ".join(ESP[e]["nombre"] for e in p["especialistas"]))
    OUT[fn] = s
    g = ["flowchart LR"]
    for p in PROCESOS:
        g.append('  %s["%s · %s"]' % (p["id"], p["id"], p["nombre"][:28]))
    for p in PROCESOS:
        for d in p["depende"]:
            g.append("  %s --> %s" % (p["id"], d))
    OUT["processes/diagrams/dependencias.md"] = AVISO + "# Dependencias entre procesos\n\nUna flecha de A a B significa que A usa o activa B.\n\n```mermaid\n%s\n```\n" % "\n".join(g)


def main(check):
    for e in ESPECIALISTAS:
        ficha(e)
    for d in DEPARTAMENTOS:
        dep_readme(d)
    navegacion()
    fuentes()
    for p in PROCESOS:
        proceso(p)
    catalogo()
    errores = []
    for fn, txt in sorted(OUT.items()):
        path = os.path.join(ROOT, fn)
        if check:
            if not os.path.exists(path) or open(path, encoding="utf-8").read() != txt:
                errores.append(fn)
            continue
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(txt)
    if check:
        if errores:
            print("Desactualizados (ejecuta python3 tools/org_gen.py):\n  " + "\n  ".join(errores))
            return 1
        print("Generado al día: %d archivos" % len(OUT))
        return 0
    print("%d especialistas, %d procesos, %d fuentes, %d archivos" % (len(ESPECIALISTAS), len(PROCESOS), len(FUENTES), len(OUT)))
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
