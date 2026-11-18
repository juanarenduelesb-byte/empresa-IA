"""La capa de Obsidian (D-021): propiedades válidas, notas por decisión y fuente, y Bases sin sintaxis de Dataview."""
import pathlib
import re

RAIZ = pathlib.Path(__file__).resolve().parents[1]
GRAFO = RAIZ / "knowledge" / "grafo"


def propiedades(p):
    t = p.read_text(encoding="utf-8")
    assert t.startswith("---\n"), p
    bloque = t[4:t.index("\n---\n", 4)]
    for linea in bloque.splitlines():
        assert re.match(r'^([a-z_]+: .+|[a-z_]+:( \[\])?|  - ".*")$', linea), f"{p}: {linea!r}"
    return bloque


def test_una_nota_por_decision():
    ids = re.findall(r"^## (D-\d{3})", (RAIZ / "DECISIONS.md").read_text(encoding="utf-8"), re.M)
    notas = sorted(x.stem for x in (GRAFO / "decisiones").glob("D-*.md"))
    assert notas == sorted(ids)
    for x in (GRAFO / "decisiones").glob("*.md"):
        assert 'tipo: "decision"' in propiedades(x)


def test_una_nota_por_fuente():
    from tools.org_data.fuentes import FUENTES
    assert len(list((GRAFO / "fuentes").glob("*.md"))) == len(FUENTES)


def test_fichas_generadas_con_propiedades():
    for carpeta, tipo in (("knowledge/agentes", "agente"), ("claude/habilidades", "habilidad")):
        fichas = [p for p in (RAIZ / carpeta).glob("*.md") if p.name != "README.md"]
        assert fichas
        for p in fichas:
            assert f'tipo: "{tipo}"' in propiedades(p)


def test_bases_sin_dataview():
    bases = list((GRAFO / "bases").glob("*.base"))
    assert len(bases) == 6
    for b in bases:
        t = b.read_text(encoding="utf-8")
        assert "views:" in t and "filters:" in t
        assert not re.search(r"^\s*(from|where):", t, re.M)


def test_enlaces_de_obsidian_existen():
    rotos = []
    for p in list(GRAFO.rglob("*.md")) + [RAIZ / "Inicio.md"]:
        for destino in re.findall(r"\[\[([^\]|#]+)", p.read_text(encoding="utf-8")):
            d = RAIZ / destino
            if not (d.exists() or d.with_suffix(d.suffix + ".md").exists() or (RAIZ / (destino + ".md")).exists()):
                rotos.append(f"{p.relative_to(RAIZ)} → {destino}")
    assert not rotos, rotos[:10]
