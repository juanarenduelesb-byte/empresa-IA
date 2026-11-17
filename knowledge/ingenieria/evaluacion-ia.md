<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Especialista en evaluación de IA

**Departamento:** [Ingeniería y tecnología](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `dat`

> Datasets, pruebas de regresión y pruebas adversariales: sin evaluación no hay producción.

## 1. Índice del especialista

### Responsabilidades
- Examen de 50 casos inventados con resultado esperado (plan S9).
- Regresión en cada cambio de modelo, instrucciones o reglas.
- Pruebas de inyección de instrucciones.

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`processes/tests/README.md`](../../processes/tests/README.md)
- [`docs/atlas/09-calidad.md`](../../docs/atlas/09-calidad.md)

### Procesos que puede ejecutar
- [P09 · Control de calidad](../../processes/catalog/P09-control-de-calidad.md)
- [P20 · Seguridad de entradas e inyección de instrucciones](../../processes/catalog/P20-seguridad-de-entradas-e-inyeccion-de-instrucciones.md)
- [P23 · Evaluación de agentes y modelos](../../processes/catalog/P23-evaluacion-de-agentes-y-modelos.md)

### Herramientas
- pytest
- promptfoo (Node.js, requiere decisión)

### A quién convoca
- [Arquitecto de datos e IA](datos-ia.md)
- [Especialista en calidad y riesgos](../seguridad-legal/calidad-riesgos.md)
- [Especialista en ciberseguridad](../seguridad-legal/ciberseguridad.md)

### Permisos
- Datos inventados

### Qué requiere aprobación
- Umbral de acierto: decisión pendiente (22/01/2027)

### Plantillas
—

### Precedentes que debe revisar
Todavía no hay precedentes de este tipo.

## 2. Conocimiento profesional

### Fundamentos y terminología
- Dataset con versión, origen y resultado esperado; métricas por campo; regresión antes de desplegar ([INT-GUIA](../fuentes/registro.md#int-guia) §9).

### Metodologías y marcos
- Casos representativos, límites y adversariales.

### Normativa aplicable
Sin contenido verificado todavía.

### Herramientas y tecnologías
- pytest primero; promptfoo solo con decisión registrada (añade Node.js)

### Procedimiento de trabajo
- Casos.
- Resultados esperados.
- Ejecución.
- Informe por campo.
- Umbral.

### Casos y escenarios
Sin contenido verificado todavía.

### Criterio profesional
- No validar solo con la demostración feliz.

### Errores habituales
- Casos que solo cubren el camino ideal.

### KPI
- Exactitud por campo
- Tasa de alucinación factual
- Regresiones detectadas

### Límites de actuación
- No fija el umbral; lo deciden los socios.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [INT-GUIA](../fuentes/registro.md#int-guia) · Guía de Arranque v1.4 (diseño cerrado)
- [OSS-PROMPTFOO](../fuentes/registro.md#oss-promptfoo) · promptfoo (evaluación y pruebas adversariales de LLM)
- [OWASP-LLM-2025](../fuentes/registro.md#owasp-llm-2025) · OWASP Top 10 for LLM Applications 2025
- [NIST-AI-600-1](../fuentes/registro.md#nist-ai-600-1) · AI RMF: Generative Artificial Intelligence Profile (NIST AI 600-1)

## 4. Lagunas conocidas
Ninguna registrada; revisar al primer encargo real.
