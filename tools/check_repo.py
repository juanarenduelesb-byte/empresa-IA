"""Comprobaciones del repositorio.

    python3 tools/check_repo.py

- Los enlaces relativos de los .md existen (archivo y, si lleva #ancla de fuente, la fuente).
- Las 38 fichas de proceso tienen los 20 apartados.
- Las fuentes citadas en especialistas y procesos existen en el registro.
- No hay patrones evidentes de secretos.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "tools"))

ENLACE = re.compile(r"\]\(([^)\s]+)\)")
# sk-ant-: claves de la API de Anthropic (formato del ejemplo de secretlint, `SECRETLINT-ANTHROPIC`); el patrón antiguo
# `sk-[A-Za-z0-9]{20,}` no las veía por el guion de «sk-ant-api03-» (repaso del 28/11).
SECRETO = re.compile(r"(sk-ant-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{30,}|AKIA[0-9A-Z]{16}"
                     r"|-----BEGIN [A-Z ]*PRIVATE KEY-----)")
# Los secretos se buscan en TODO el repositorio, también en archive/ y en .sh, .env.example, Dockerfile o .ini (antes
# solo en siete extensiones y sin archive/). Solo se saltan la carpeta de git, las cachés y los binarios.
SIN_SECRETOS = (".git/", "node_modules/", "__pycache__/", ".pytest_cache/", ".ruff_cache/")
BINARIOS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".xlsx", ".docx", ".pptx", ".zip", ".pyc",
            ".woff", ".woff2", ".ttf", ".glb"}
EXCLUIR = ("archive/", "node_modules/", ".git/")
CARPETAS = ("knowledge", "processes", "integrations", "precedents", "governance", "docs", "claude", "web")


def md_archivos():
    # También los de la raíz (README, DECISIONS, CLAUDE): antes no se miraban (repaso del 28/11).
    yield from sorted(RAIZ.glob("*.md"))
    for c in CARPETAS:
        for p in (RAIZ / c).rglob("*.md"):
            if not any(x in p.as_posix() for x in EXCLUIR):
                yield p


def enlaces_rotos() -> list[str]:
    from org_data.fuentes import FUENTES

    anclas = {f["id"].lower() for f in FUENTES}
    rotos = []
    for p in md_archivos():
        texto = re.sub(r"```.*?```", "", p.read_text(encoding="utf-8"), flags=re.S)
        for destino in ENLACE.findall(texto):
            if destino.startswith(("http://", "https://", "mailto:", "#")):
                continue
            ruta, _, ancla = destino.partition("#")
            objetivo = (p.parent / ruta).resolve()
            if not objetivo.exists():
                rotos.append(f"{p.relative_to(RAIZ)} → {destino}")
            elif ancla and objetivo.name == "registro.md" and ancla not in anclas:
                rotos.append(f"{p.relative_to(RAIZ)} → {destino} (fuente inexistente)")
    return rotos


def fichas_incompletas() -> list[str]:
    from org_gen import CAMPOS

    malas = []
    fichas = sorted((RAIZ / "processes" / "catalog").glob("P[0-9][0-9]-*.md"))
    if len(fichas) != 38:
        malas.append(f"Hay {len(fichas)} fichas de proceso, se esperaban 38")
    for f in fichas:
        t = f.read_text(encoding="utf-8")
        faltan = [c for c in CAMPOS if c not in t]
        if faltan:
            malas.append(f"{f.name}: faltan {faltan}")
    return malas


def fuentes_inexistentes() -> list[str]:
    from org_data.especialistas import ESPECIALISTAS
    from org_data.fuentes import FUENTES

    ids = {f["id"] for f in FUENTES}
    return [f"{e['id']} cita {s}" for e in ESPECIALISTAS for s in e.get("fuentes", []) if s not in ids]


def secretos(raiz: Path = RAIZ) -> list[str]:
    hallados = []
    for p in raiz.rglob("*"):
        rel = p.relative_to(raiz).as_posix()
        if not p.is_file() or p.suffix.lower() in BINARIOS or any(rel.startswith(x) or f"/{x}" in rel
                                                                    for x in SIN_SECRETOS):
            continue
        if SECRETO.search(p.read_text(encoding="utf-8", errors="ignore")):
            hallados.append(rel)
    return sorted(hallados)


def entornos_subidos(rastreados: list[str] | None = None) -> list[str]:
    """Un `.env` subido al repositorio lleva contraseñas aunque ningún patrón de `secretos()` las reconozca.

    `.gitignore` los excluye, pero `git add -f` se lo salta (repaso del 28/11). Solo vale `.env.example`.
    """
    if rastreados is None:
        salida = subprocess.run(["git", "ls-files", "-z"], cwd=RAIZ, capture_output=True, check=True).stdout
        rastreados = [x for x in salida.decode("utf-8").split("\0") if x]
    return sorted(r for r in rastreados
                  if re.fullmatch(r"\.env(\..+)?", Path(r).name) and Path(r).name != ".env.example")


def agentes() -> list[str]:
    import agentes_gen

    err = agentes_gen.validar()
    stale = [rel for rel, txt in agentes_gen.salidas().items()
             if not (RAIZ / rel).exists() or (RAIZ / rel).read_text(encoding="utf-8") != txt]
    return err + [f"{r} desactualizado (python3 tools/agentes_gen.py)" for r in stale]


def main() -> int:
    problemas = {
        "agentes y habilidades": agentes(),
        "enlaces rotos": enlaces_rotos(),
        "fichas incompletas": fichas_incompletas(),
        "fuentes inexistentes": fuentes_inexistentes(),
        "posibles secretos": secretos(),
        "archivos .env subidos": entornos_subidos(),
    }
    total = 0
    for nombre, lista in problemas.items():
        for x in lista:
            print(f"[{nombre}] {x}")
        total += len(lista)
    print("ok" if total == 0 else f"{total} problemas")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
