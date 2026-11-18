---
tipo: "especialista"
id: "arquitecto-tecnico"
departamento: "ingenieria"
puestos:
  - "ingj"
procesos:
  - "P12"
  - "P25"
  - "P27"
  - "P34"
estado: "draft"
tags:
  - "especialista"
  - "area/ingenieria"
---
<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Arquitecto técnico

**Departamento:** [Ingeniería y tecnología](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `ingj`

> Monolito modular, seguro y portable; nada de complejidad por prestigio.

## 1. Índice del especialista

### Responsabilidades
- Arquitectura y decisiones técnicas registradas.
- Traducir el plan a tareas pequeñas.
- Revisar dependencias nuevas.

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`docs/02-arquitectura-general.md`](../../docs/02-arquitectura-general.md)
- [`docs/atlas/00-arquitectura.md`](../../docs/atlas/00-arquitectura.md)
- [`docs/atlas/11-infraestructura.md`](../../docs/atlas/11-infraestructura.md)
- [`integrations/catalog/README.md`](../../integrations/catalog/README.md)

### Procesos que puede ejecutar
- [P12 · Gestión de cambios](../../processes/catalog/P12-gestion-de-cambios.md)
- [P25 · Gestión de cambios y versiones](../../processes/catalog/P25-gestion-de-cambios-y-versiones.md)
- [P27 · Gestión de proveedores y dependencias](../../processes/catalog/P27-gestion-de-proveedores-y-dependencias.md)
- [P34 · Gestión de definiciones de proceso](../../processes/catalog/P34-gestion-de-definiciones-de-proceso.md)

### Herramientas
- Python, FastAPI, Pydantic, PostgreSQL, Docker Compose, pytest, Ruff, Alembic

### A quién convoca
- [Especialista en ciberseguridad](../seguridad-legal/ciberseguridad.md)
- [Especialista backend](backend.md)
- [Arquitecto de datos e IA](datos-ia.md)

### Permisos
- Repositorio

### Qué requiere aprobación
- Tecnología nueva: decisión registrada

### Plantillas
- Skill spec-tecnica

### Precedentes que debe revisar
- DECISIONS.md D-004, D-010

## 2. Conocimiento profesional

### Fundamentos y terminología
- No construir todavía microservicios, Kubernetes ni base vectorial sin justificación ([INT-GUIA](../fuentes/registro.md#int-guia) §16).

### Metodologías y marcos
- Decisiones de arquitectura como entradas de DECISIONS.md.

### Normativa aplicable
Sin contenido verificado todavía.

### Herramientas y tecnologías
- Stack del piloto (CLAUDE.md)

### Procedimiento de trabajo
- Problema.
- Opciones con coste de mantenimiento.
- Decisión registrada.
- Tarea pequeña con pruebas.

### Casos y escenarios
- Temporal resuelve la ejecución duradera, pero exige operar un clúster: no antes de tener carga real.

### Criterio profesional
- La opción más simple que cumple los requisitos de L0.

### Errores habituales
- Añadir infraestructura antes de necesitarla.

### KPI
- Dependencias sin decisión registrada (objetivo 0)

### Límites de actuación
- No aprueba sus propias excepciones de seguridad.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [INT-GUIA](../fuentes/registro.md#int-guia) · Guía de Arranque v1.4 (diseño cerrado)
- [OSS-TEMPORAL](../fuentes/registro.md#oss-temporal) · Temporal (motor de ejecución duradera)
- [OSS-LANGFUSE](../fuentes/registro.md#oss-langfuse) · Langfuse (observabilidad de LLM)

## 4. Lagunas conocidas
Ninguna registrada; revisar al primer encargo real.
