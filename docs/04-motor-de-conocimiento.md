# Motor de conocimiento

## Patrón RAW / WIKI / SCHEMA
- **RAW:** fuentes originales inmutables, hash, versión, origen, fecha, propietario, clasificación y permisos.
- **WIKI:** conocimiento estructurado Markdown: conceptos, procesos, metodologías, decisiones, entidades, relaciones y aprendizajes; cada afirmación relevante enlaza a fuente.
- **SCHEMA:** reglas de ingesta, extracción, actualización, validación, permisos, recuperación, caducidad y gobierno.

## Operaciones
- **Ingest:** recibe, valida, clasifica, extrae, referencia y propone conocimiento.
- **Query:** aplica identidad y permisos antes de recuperar contenido y devuelve citas/metadatos.
- **Lint:** comprueba estructura, enlaces, duplicados, vigencia, fuentes, propietario y estado.

Estados: `raw`, `draft`, `validated`, `approved`, `deprecated`, `disputed`. La IA propone cambios; contenidos sensibles requieren revisión humana.

## Espacios separados
Corporativo, departamental, sectorial, cliente y proyecto. El aislamiento se aplica en backend antes de consultar documentos, índices o embeddings; no confiar en filtros visuales o prompts.

## Obsidian
Interfaz humana para editar/navegar Markdown; no es backend, motor de permisos, base transaccional ni auditoría. El backend indexa y relaciona contenido. Vault orientativo: 00_HOME, 01_CORPORATE, 02_DEPARTMENTS, 03_SECTORS, 04_METHODOLOGIES, 05_PROCESSES, 06_TEMPLATES, 07_DECISIONS, 08_GLOSSARY.

Metadatos mínimos: owner, source, version, valid_from, review_date, classification, tenant_id, project_id, status y timestamps.