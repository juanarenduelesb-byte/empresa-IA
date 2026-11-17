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