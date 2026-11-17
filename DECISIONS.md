# Registro de decisiones

## D-001 — Arquitectura orientada a procesos
- Fecha: 2026-11-17
- Decisión: evolucionar desde una visión centrada en CEO/agentes hacia procesos completos, con CEO como coordinador.
- Motivo: valor en completar procesos con controles, integraciones, medición y trazabilidad.
- Impacto: Process Discovery, Process Engine, Integration Hub, Operational Intelligence y Client Deployment Management.
- Estado: propuesta; validar con primer piloto.

## D-002 — Modelo matricial
Departamentos funcionales reutilizables + especialistas sectoriales activados según contexto. Evitar un agente por combinación. Estado: diseño.

## D-003 — Obsidian como interfaz humana
Obsidian edita y navega Markdown; backend y PostgreSQL gestionan permisos, operaciones y auditoría. Estado: diseño.

## D-004 — PostgreSQL como fuente operativa
PostgreSQL para datos operativos/metadatos; Markdown + Git para conocimiento versionado no confidencial. Estado: diseño.

## D-005 — Aislamiento multi-cliente
Tenant derivado de identidad autenticada y autorización antes de recuperar datos o invocar herramientas. Estado: requisito obligatorio.

## D-006 — Primer proceso piloto
No construir primero un CEO omnisciente; descubrir, diseñar, integrar y medir un proceso real. Estado: siguiente paso recomendado.
## D-007 — Nombre provisional: Varios
- Fecha: 2026-11-17
- Decisión: el proyecto pasa a llamarse "Varios" de forma provisional. Sustituye a ExcluSa / Esclusa / Cauce.
- Motivo: decisión de los socios.
- Impacto: web `site/`, documentos nuevos y la habilidad de marca anterior (hay que adaptarla o retirarla). Identidad visual: burdeos, turquesa y champán; tipografía Instrument Sans.
- Estado: provisional.

## D-008 — Repositorio como memoria oficial y web visual
- Fecha: 2026-11-17
- Decisión: este repositorio es la única fuente de verdad. Se añade `site/` (web visual con simulación), `CLAUDE.md` y `claude/instrucciones-proyecto.md` para dar contexto a una cuenta nueva de Claude.
- Motivo: tener una base de contexto antes de crear la cuenta de Claude del proyecto.
- Estado: aprobada.

## D-009 — Unificación de puertas y estados
- Fecha: 2026-11-17
- Decisión: G0–G6 son las puertas de cliente (una por fase D0–D6, según Atlas Evolución v1.1). Las puertas de lanzamiento de la Guía v1.4 pasan a llamarse L0–L4. Los estados se separan por objeto (encargo, tarea, instancia, definición, conector, despliegue, conocimiento, capacidad).
- Motivo: había tres juegos de puertas con el mismo nombre y listas de estados mezcladas.
- Impacto: `docs/08`, `docs/13`, web (Método, Procesos).
- Estado: aprobada como corrección documental; confirmar entre socios.

## D-010 — Diagramas como código
- Fecha: 2026-11-17
- Decisión: los diagramas viven como Mermaid en `tools/atlas_data.py`, que genera a la vez la web (`site/js/atlas-data.js`) y `docs/atlas/`. Las imágenes de los Word quedan solo como histórico en `archive/originales/`.
- Motivo: los PNG tenían errores y no se podían corregir ni versionar. GitHub dibuja Mermaid directamente.
- Uso: `python3 tools/gen.py site/js/atlas-data.js docs/atlas`
- Estado: aprobada.

## Decisiones pendientes (con fecha límite)
| Decisión | Quién | Antes de |
|---|---|---|
| Acuerdo entre socios: roles, horas, reparto, salida | Los dos | 22/11/2026 |
| Plan de Claude | Juan | 22/11/2026 |
| Nicho de entrada | Los dos, propone Álvaro | 27/11/2026 |
| Precio del diagnóstico y del piloto | Los dos | 11/12/2026 |
| Proceso piloto | Los dos | 18/12/2026 |
| Forma jurídica y facturación | Álvaro, con gestor | 08/01/2027 |
| Alojamiento y región de datos del piloto | Juan | 15/01/2027 |
| Aprobaciones humanas por tipo de acción | Juan, con el cliente | Fase de diseño |
| Primer conector | Juan | Fase de diseño |
