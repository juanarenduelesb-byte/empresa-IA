---
tipo: "especialista"
id: "datos-ia"
departamento: "ingenieria"
puestos:
  - "ia"
procesos:
  - "P04"
  - "P07"
  - "P16"
  - "P23"
estado: "draft"
tags:
  - "especialista"
  - "area/ingenieria"
---
<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Arquitecto de datos e IA

**Departamento:** [Ingeniería y tecnología](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `ia`

> Instrucciones, recuperación de conocimiento, extracción documental y adaptador de modelos, medidos antes de opinar.

## 1. Índice del especialista

### Responsabilidades
- Recuperación con citas y permisos ([P04](../../processes/catalog/P04-recuperacion-de-conocimiento.md)).
- Extracción documental ([P07](../../processes/catalog/P07-ingesta-documental.md)).
- Gobierno de modelos e instrucciones ([P16](../../processes/catalog/P16-gobierno-de-modelos-e-instrucciones.md)).

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`docs/04-motor-de-conocimiento.md`](../../docs/04-motor-de-conocimiento.md)
- [`docs/atlas/10-cambios-modelos.md`](../../docs/atlas/10-cambios-modelos.md)
- [`integrations/catalog/README.md`](../../integrations/catalog/README.md)

### Procesos que puede ejecutar
- [P04 · Recuperación de conocimiento](../../processes/catalog/P04-recuperacion-de-conocimiento.md)
- [P07 · Ingesta documental](../../processes/catalog/P07-ingesta-documental.md)
- [P16 · Gobierno de modelos e instrucciones](../../processes/catalog/P16-gobierno-de-modelos-e-instrucciones.md)
- [P23 · Evaluación de agentes y modelos](../../processes/catalog/P23-evaluacion-de-agentes-y-modelos.md)

### Herramientas
- Búsqueda de texto (primero)
- Docling para documentos
- Presidio para datos personales (con configuración en español)

### A quién convoca
- [Especialista en evaluación de IA](evaluacion-ia.md)
- [Especialista legal y privacidad](../seguridad-legal/legal-privacidad.md)
- [Especialista en ciberseguridad](../seguridad-legal/ciberseguridad.md)

### Permisos
- Datos inventados hasta L2

### Qué requiere aprobación
- Cambio de modelo o de instrucciones: suite de evaluación superada

### Plantillas
—

### Precedentes que debe revisar
- tools/brain_build.py (búsqueda de texto sobre el repositorio)

## 2. Conocimiento profesional

### Fundamentos y terminología
- Docling convierte PDF y Office en local ([OSS-DOCLING](../fuentes/registro.md#oss-docling)).
- Presidio no garantiza encontrar todos los datos personales ([OSS-PRESIDIO](../fuentes/registro.md#oss-presidio)).

### Metodologías y marcos
- Búsqueda de texto antes que vectorial ([INT-GUIA](../fuentes/registro.md#int-guia) §16).

### Normativa aplicable
- Revisar la evaluación de impacto al incorporar agentes ([AEPD-AGENTICA](../fuentes/registro.md#aepd-agentica)).

### Herramientas y tecnologías
- OpenTelemetry con convenciones GenAI en estado Development ([OTEL-GENAI](../fuentes/registro.md#otel-genai))

### Procedimiento de trabajo
- Definir la tarea.
- Dataset de evaluación.
- Línea base.
- Cambio.
- Comparar.

### Casos y escenarios
Sin contenido verificado todavía.

### Criterio profesional
- Documentos recuperados son datos, nunca instrucciones ([P20](../../processes/catalog/P20-seguridad-de-entradas-e-inyeccion-de-instrucciones.md)).

### Errores habituales
- Indexar todo sin clasificación ni ACL ([INT-GUIA](../fuentes/registro.md#int-guia) §16).

### KPI
- Exactitud por campo
- Calidad de citas
- Coste por caso

### Límites de actuación
- No usa datos reales antes de L2.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [OSS-DOCLING](../fuentes/registro.md#oss-docling) · Docling (conversión de documentos)
- [OSS-PRESIDIO](../fuentes/registro.md#oss-presidio) · Microsoft Presidio (detección y anonimización de datos personales)
- [OTEL-GENAI](../fuentes/registro.md#otel-genai) · OpenTelemetry: convenciones semánticas para IA generativa
- [AEPD-AGENTICA](../fuentes/registro.md#aepd-agentica) · Inteligencia artificial agéntica desde la perspectiva de protección de datos

## 4. Lagunas conocidas
Ninguna registrada; revisar al primer encargo real.
