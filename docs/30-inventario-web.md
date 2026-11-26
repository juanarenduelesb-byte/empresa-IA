# Inventario de la web interna (`site/`) frente a la web para clientes (N5)

**Estado:** propuesta · **Fecha:** 26/11/2026 (tarea N5) · **No se ha borrado ni movido nada.** Compara las 15 páginas de `site/` con la estructura de la web para clientes de [docs/26](26-web-clientes.md) y su maqueta (`web/maqueta/`).

## Conclusión
`site/` es la web interna del proyecto, escrita para los socios: habla de planes, riesgos, decisiones pendientes y del propio cerebro. **Ninguna página se puede publicar tal cual para clientes.** Cuatro tienen contenido que, reescrito para el cliente, alimenta páginas de la web pública (método, seguridad, sector y caso). Propongo que `site/` siga siendo interna y que la web pública se construya desde la maqueta, no desde `site/`. Como candidatas a retirar propongo dos páginas que repiten lo que ya está en el repositorio y una tercera que habría que fusionar; la decisión es de los socios.

## Página a página
| Página de `site/` | Qué cuenta | Para quién | Propuesta | Si se mueve, a qué página de docs/26 |
|---|---|---|---|---|
| `index.html` | Mapa del proyecto y trece temas | Socios | **Se queda** (interna) | — |
| `negocio.html` | Idea de negocio, cliente, cuatro productos, competencia, a qué decimos que no | Socios | **Se queda**; se reescriben frases para Inicio y Nosotros | Inicio (el problema), Nosotros (por qué somos pequeños a propósito) |
| `metodo.html` | Cuatro fases, siete fases internas con puertas G0–G6, puertas técnicas L0–L4 y papeles | Socios | **Se mueve en parte:** las fases, su duración, el entregable y la decisión del cliente. Las puertas L0–L4 y los papeles internos no salen | Cómo trabajamos |
| `seguridad.html` | Lo que nunca se negocia, ocho fallos de la IA, lista antes de datos reales, marcos, calendario | Socios | **Se mueve en parte:** lo que nunca se negocia y cómo se controla la IA. La lista previa a datos reales es interna | Seguridad y cumplimiento |
| `legal.html` | Etiquetas por norma, calendario, papeles en el tratamiento, fases y lista de producción | Socios | **Se queda** (interna); comparte calendario y marcos con `seguridad.html`: propuesta de fusionar las dos en una página interna | Seguridad y cumplimiento toma solo el resumen de normas, cuando lo revise el abogado |
| `flujos.html` | Recorrido de un encargo, cinco decisiones, estados de una tarea, aprobaciones, ejemplo de siniestro | Socios | **Se queda**; el ejemplo del siniestro, reescrito, sirve al cliente | Seguros y corredurías, Caso de referencia |
| `procesos.html` | P01–P38, estados y modelo de datos | Socios | **Se queda** (interna) | — |
| `cerebro.html` | Departamentos, especialistas y herramientas | Socios | **Se queda** (interna) | — |
| `conocimiento.html` | Motor de conocimiento, revisión humana, aislamiento | Socios | **Se queda** (interna); la idea «lo de un cliente nunca se mezcla con lo de otro» ya está en la maqueta | Seguridad y cumplimiento (ya cubierto) |
| `decisiones.html` | Decisiones, pendientes, riesgos, documentos fuente y correcciones | Socios | **Se queda** (interna). Nunca pública: contiene riesgos y decisiones abiertas | — |
| `planning.html` | Plan de 12 semanas | Socios | **Se queda**, pero repite `docs/10` y `docs/22` y ya va por detrás (por ejemplo, cita `uv`, que no está en el stack de CLAUDE.md). Propuesta: enlazar a docs/22 en vez de mantener dos planes | — |
| `atlas.html` | Diagramas generados desde `tools/atlas_data.py` | Socios | **Se queda** (interna, generada) | — |
| `glosario.html` | Palabras técnicas en una frase | Socios | **Se queda**; para el cliente sirve más el [glosario de siniestros](../knowledge/sectores/seguros/glosario-siniestros.md) | Seguros y corredurías (vocabulario del sector) |
| `claude.html` | Pasos para montar el cerebro en Claude, instrucciones y CLAUDE.md | Socios | **Candidata a retirar:** repite `claude/instrucciones-proyecto.md` y `CLAUDE.md`, y una copia acaba desfasada | — |
| `simulacion.html` | Simulación del cerebro con un cliente ficticio (40 KB, la página más pesada) | Socios | **Candidata a retirar o archivar:** la oficina de agentes (`oficina/`) ya hace el recorrido real con el caso Atalaya | — |

## Lo que la web para clientes necesita y `site/` no tiene
- Titular por proceso y una sola llamada a la acción («Pedir un diagnóstico»): solo en la maqueta.
- La garantía 50/50 ligada a una métrica firmada, explicada para el cliente: en `site/` aparece como modelo de negocio, no como promesa.
- Caso de referencia etiquetado como inventado: está en la maqueta y en `precedents/`, no en `site/`.
- Páginas legales (aviso legal, privacidad, cookies): dependen de la marca (M-002) y de la forma jurídica (M-003).
- Contacto: formulario mínimo, inactivo hasta que haya privacidad revisada.

## Arreglado al hacer el inventario
- `decisiones.html` decía «Veinticinco decisiones registradas» y ya hay 28 (D-026 a D-028 de esta noche).
- `conocimiento.html` decía «30 especialistas, 53 fuentes»: son 34 especialistas y 121 fuentes en el registro.

## Para decidir
| Decisión | Quién | Antes de |
|---|---|---|
| `site/` queda solo como web interna | Los dos | La web pública (semana 10) |
| Retirar o archivar `claude.html` y `simulacion.html`; fusionar `legal.html` y `seguridad.html`; `planning.html` enlaza a docs/22 | Juan | Cuando convenga; no bloquea nada |
