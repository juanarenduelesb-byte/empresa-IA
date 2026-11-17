# Registro de correcciones a los documentos recibidos el 17/11/2026

Originales sin modificar en `archive/originales/`. Versión de trabajo en `docs/fuentes/`. Diagramas corregidos en `docs/atlas/`.

| # | Tipo | Documento | Problema | Corrección |
|---|---|---|---|---|
| 1 | Contenido | Atlas · Mapa 2 | El dibujo ponía la aprobación humana después de la entrega; el texto (pasos 9 y 10) dice lo contrario | Redibujado: aprobación antes de entregar (`atlas/02`) |
| 2 | Contenido | Guía v1.4 / Atlas Evolución / repo `docs/08` | Tres juegos de puertas llamados G0… con significados distintos | G0–G6 = puertas de cliente (Atlas Evolución); L0–L4 = puertas técnicas (Guía v1.4). D-009 |
| 3 | Contenido | Guía v1.4 / repo | Estados de encargo, de tarea y de instancia mezclados sin decir a qué objeto pertenecen | Tabla por objeto en `docs/13` |
| 4 | Contenido | Mapas 1–9 | El Atlas de Evolución (apartado 15) pedía actualizarlos con motor de procesos, integraciones, D0–D6, roles nuevos y entidades; no se había hecho | Aplicado en `atlas/00`, `01`, `04`, `12`, `15` |
| 5 | Forma | Los 25 diagramas | Flechas que cruzan cajas y textos, etiquetas superpuestas ("artifact ref/vent", "no / respuesta" sobre "baja confianza"), texto fuera de las cajas | 17 diagramas redibujados en Mermaid (`tools/atlas_data.py`) |
| 6 | Forma | Atlas · Mapa 6 | Mezclaba control de resultados y control de cambios con flechas cruzadas | Separado en `atlas/09` y `atlas/10` |
| 7 | Forma | Guía v1.4 | La portada decía "versión 1.3"; "nombre por definir"; diseño azul marino | Versión corregida; nombre provisional Varios; identidad burdeos, turquesa y champán |
| 8 | Forma | Mapas 2–9 | Apartados 7, 8 y 9 idénticos en los ocho documentos | Consolidados una vez en `docs/atlas/README.md` |
| 9 | Forma | Varios documentos | Nombres ExcluSa, Esclusa, Cauce | Unificado como Varios (D-007) |
| 10 | Error propio | Web, página Seguridad (versión anterior) | Atribuía al 02/12/2026 la transparencia general del Reglamento de IA | Corregido según el Marco legal: art. 50 desde 02/08/2026; el 02/12/2026 son nuevas prohibiciones y transición del etiquetado |

## Tensión abierta (decisión de socios)

La Guía v1.4 propone construir ya el MVP técnico con un caso interno; el plan de 12 semanas prioriza las entrevistas con clientes. Propuesta: en paralelo, sin que lo técnico retrase las entrevistas. El entorno técnico básico entra en la semana 5 del plan.
