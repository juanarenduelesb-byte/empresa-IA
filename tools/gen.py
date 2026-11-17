import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from atlas_data import M, INIT, CLASSES, ORDER_GROUPS

def full(m):
    src = m["mermaid"].strip()
    body = INIT + "\n" + src
    if src.startswith("flowchart"):
        body += "\n" + CLASSES.strip()
    return body

def site(out):
    data = []
    for m in M:
        d = dict(m); d["code"] = full(m)
        if os.path.exists(os.path.join(os.path.dirname(out), "..", "img", "originales", m["id"] + ".jpg")): d["orig"] = "img/originales/" + m["id"] + ".jpg"
        data.append(d)
    with open(out, "w") as f:
        f.write("window.ATLAS=" + json.dumps(data, ensure_ascii=False) + ";\nwindow.ATLAS_GROUPS=" + json.dumps(ORDER_GROUPS, ensure_ascii=False) + ";\n")

def md(outdir):
    os.makedirs(outdir, exist_ok=True)
    idx = ["# Atlas de diagramas\n", "Fuente única: `tools/atlas_data.py` (genera la web y estos archivos). GitHub dibuja los diagramas Mermaid directamente.\n",
           "Leyenda de colores: turquesa = IA · blanco = reglas fijas · burdeos claro = persona · ocre = decisión · rojo = parada o error · verde = resultado.\n",
           "| Nº | Mapa | Grupo |", "|---|---|---|"]
    for m in M:
        fn = f"{m['num']}-{m['id']}.md"
        idx.append(f"| {m['num']} | [{m['titulo']}]({fn}) | {m['grupo']} |")
        L = [f"# {m['num']} · {m['titulo']}\n", f"_{m['sub']}_\n", f"**Fuente:** {m['fuente']}\n",
             "## En palabras sencillas\n", m["simple"] + "\n", "## Diagrama\n", "```mermaid", full(m), "```\n",
             "## Pasos\n"] + [f"{i+1}. {p}" for i, p in enumerate(m["pasos"])] + ["", "## Si algo falla\n"] + [f"- {e}" for e in m["excepciones"]] + \
            ["", "## Qué tiene que existir\n"] + [f"- {a}" for a in m["artefactos"]]
        if m.get("prueba"):
            L += ["", "## Prueba de aceptación\n", m["prueba"]]
        L += ["", "## Correcciones respecto al original\n"] + [f"- {c}" for c in m["correcciones"]] + [""]
        open(os.path.join(outdir, fn), "w").write("\n".join(L))
    idx += ["", "## Criterios comunes a todos los mapas", "",
            "Los mapas originales 2 a 9 repetían el mismo texto en sus apartados 7, 8 y 9. Se consolida aquí una sola vez:", "",
            "- El flujo se puede ejecutar de extremo a extremo en un entorno de pruebas.",
            "- Entradas, salidas, responsables, estados y decisiones quedan registrados.",
            "- Se prueban los casos de error y denegación, no solo el camino feliz.",
            "- Los permisos se verifican en el servidor y se prueban con identidades distintas.",
            "- Hay documentación suficiente para que otra persona mantenga y despliegue el componente.", "",
            "**Prioridad:** MVP = recorrido mínimo con estados guardados. Antes de datos reales de clientes = seguridad, privacidad, copias, recuperación, evaluación y contratos de proveedores. Escalado = colas, observabilidad avanzada y redundancia cuando el uso lo justifique.", ""]
    open(os.path.join(outdir, "README.md"), "w").write("\n".join(idx))

if __name__ == "__main__":
    site(sys.argv[1]); md(sys.argv[2])
    print(len(M), "mapas")
