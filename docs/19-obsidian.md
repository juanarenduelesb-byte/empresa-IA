# Obsidian: el cerebro abierto en tu equipo

Decisión: D-021 (propuesta), que desarrolla D-003. Este documento explica cómo se monta, cómo se mantiene al día y qué no hay que tocar.

## La idea

El repositorio entero es el vault. Obsidian lee el mismo Markdown que está en GitHub, así que no hay copia ni importación. Lo que añade Obsidian:

- **Grafo** con colores por tipo de nota: rojo para decisiones, ocre para fuentes, turquesa para agentes, azul para procesos y verde para documentos.
- **Propiedades** (YAML al principio de cada ficha generada): tipo, departamento, estado… Se pueden filtrar y ordenar.
- **Notas por decisión y por fuente** en `knowledge/grafo/decisiones/` y `knowledge/grafo/fuentes/`. Cada una lista los documentos que la citan, así que en el grafo se ve qué sostiene cada decisión.
- **Mapas** en `knowledge/grafo/mapas/`: uno por comunidad del grafo (Louvain, D-018) y el *Mapa del cerebro*, con nodos centrales, puentes y preguntas abiertas.
- **Bases** en `knowledge/grafo/bases/`: tablas nativas de Obsidian (1.9 o posterior) para agentes, habilidades, especialistas, procesos, decisiones (con la vista *En propuesta*) y fuentes (con la vista *Por revisar*).
- **Inicio.md** en la raíz, que hace de portada.

## Montarlo (una vez por socio)

1. Tener el repositorio clonado en el equipo, con Git. La forma más sencilla es GitHub Desktop → *Clone repository* → `juanarenduelesb-byte/empresa-IA`, que además guarda tu acceso a GitHub en el llavero del Mac.
2. En Obsidian: *Open folder as vault* → la carpeta del clon. Si pregunta si confías en el autor, contesta que sí: la carpeta `.obsidian/` solo trae ajustes, no plugins.
3. Abrir `Inicio.md`.
4. Para que se actualice solo: *Settings → Community plugins → Browse → Obsidian Git* → instalar y activar. En sus ajustes:
   - *Pull on startup*: activado.
   - *Auto pull interval*: 10 minutos.
   - *Auto commit-and-sync interval*: 0. Subir cambios es una acción consciente (*Commit-and-sync* desde la paleta de comandos).
   - *Pull before push*: activado.

Ningún token va al repositorio. Si Git pide credenciales, se resuelven en el equipo de cada socio (GitHub Desktop o el llavero de macOS).

## Qué se edita y qué no

| Se edita a mano | Se regenera solo (no tocar) |
|---|---|
| `docs/`, `DECISIONS.md`, `governance/`, `processes/*/` (AS-IS, TO-BE), `knowledge/principios`, `knowledge/sectores`… | `knowledge/grafo/`, `knowledge/agentes/`, `claude/habilidades/`, fichas de especialistas, `processes/catalog/`, `oficina/brain.json` |

Lo generado nace en `tools/org_data/` y en los documentos. Cuando cambias un documento y lo subes a `main`, la Action *Regenerar cerebro* rehace el grafo, las notas y las fichas sin usar IA. La próxima vez que Obsidian traiga cambios, los verás.

## Ajustes versionados

- `.obsidian/app.json`: ignora `site/`, `oficina/vendor/`, `archive/` y `.github/` en búsquedas y grafo.
- `.obsidian/core-plugins.json`: grafo, enlaces entrantes y salientes, propiedades, Bases, etiquetas, esquema, lienzo y marcadores.
- `.obsidian/graph.json`: grupos de color y filtro del grafo. Obsidian lo reescribe al cerrar; si cambias los colores, súbelo solo si quieres que los demás los vean.

`tools/obsidian_gen.py` escribe estos tres archivos solo si no existen, para no pisar tus ajustes. El estado local (pestañas abiertas, plugins de la comunidad, temas) queda fuera por `.gitignore`.

## Límites

- Obsidian no sustituye al backend: permisos, operaciones y auditoría siguen en PostgreSQL (D-003, D-004).
- Nada de datos reales de clientes en el vault, igual que en el repositorio.
- Las Bases y las propiedades son de Obsidian; para el resto del sistema son YAML y Markdown normales.
