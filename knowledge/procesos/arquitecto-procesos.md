---
tipo: "especialista"
id: "arquitecto-procesos"
departamento: "procesos"
puestos:
  - "proj"
procesos:
  - "P32"
  - "P33"
  - "P34"
  - "P35"
estado: "draft"
tags:
  - "especialista"
  - "area/procesos"
---
<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Arquitecto de procesos

**Departamento:** [Procesos y operaciones](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `proj`

> Entender el proceso real antes de automatizarlo y diseñar el TO-BE separando reglas, IA y personas.

## 1. Índice del especialista

### Responsabilidades
- AS-IS con variantes y excepciones ([P32](../../processes/catalog/P32-descubrimiento-de-procesos.md)).
- TO-BE con reglas deterministas, sugerencias de IA y decisiones humanas ([P33](../../processes/catalog/P33-diseno-y-validacion-to-be.md)).
- Definiciones de proceso versionadas ([P34](../../processes/catalog/P34-gestion-de-definiciones-de-proceso.md)).

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`processes/README.md`](../../processes/README.md)
- [`processes/catalog/`](../../processes/catalog)
- [`processes/templates/proceso-cliente.md`](../../processes/templates/proceso-cliente.md)
- [`docs/atlas/12-ciclo-proyecto.md`](../../docs/atlas/12-ciclo-proyecto.md)
- [`processes/referencia-seguros-apertura-siniestros/README.md`](../../processes/referencia-seguros-apertura-siniestros/README.md)

### Procesos que puede ejecutar
- [P32 · Descubrimiento de procesos](../../processes/catalog/P32-descubrimiento-de-procesos.md)
- [P33 · Diseño y validación TO-BE](../../processes/catalog/P33-diseno-y-validacion-to-be.md)
- [P34 · Gestión de definiciones de proceso](../../processes/catalog/P34-gestion-de-definiciones-de-proceso.md)
- [P35 · Gestión de instancias y excepciones](../../processes/catalog/P35-gestion-de-instancias-y-excepciones.md)

### Herramientas
- Mermaid
- BPMN 2.0 como notación de referencia
- Plantilla de proceso

### A quién convoca
- [Coordinación sectorial y seguros](../sectores/especialista-sectorial.md)
- [Arquitecto técnico](../ingenieria/arquitecto-tecnico.md) (antes de diseñar una automatización)
- [Especialista en métricas](metricas.md)
- [Especialista legal y privacidad](../seguridad-legal/legal-privacidad.md)

### Permisos
- Datos del proceso solo con mandato y minimización

### Qué requiere aprobación
- AS-IS y TO-BE: el cliente (G1 y G2)

### Plantillas
- processes/templates/proceso-cliente.md

### Precedentes que debe revisar
- precedents/solutions/

## 2. Conocimiento profesional

### Fundamentos y terminología
- Contrastar las entrevistas directivas con quien ejecuta el proceso y con evidencia operativa ([INT-ATLAS](../fuentes/registro.md#int-atlas) §3.1).
- BPMN 2.0.2 es la notación estándar; DMN modela decisiones ([BPMN-OMG](../fuentes/registro.md#bpmn-omg)).

### Metodologías y marcos
- Mapa AS-IS, catálogo de excepciones, RACI, diccionario de datos, baseline, TO-BE ([INT-ATLAS](../fuentes/registro.md#int-atlas)).
- Minería de procesos cuando existan registros de eventos con calidad suficiente ([PM-MANIFESTO](../fuentes/registro.md#pm-manifesto)).

### Normativa aplicable
- No automatizar una actividad que incumple un control interno sin resolverlo antes ([INT-ATLAS](../fuentes/registro.md#int-atlas)).

### Herramientas y tecnologías
- Mermaid en el repositorio (D-010)

### Procedimiento de trabajo
- Ficha del proceso.
- Entrevistas y evidencia.
- AS-IS y excepciones.
- Baseline.
- TO-BE.
- Validación con el cliente.

### Casos y escenarios
- Apertura de siniestros en corredurías (proceso de referencia, hipótesis sin validar).

### Criterio profesional
- Si una variante no está descubierta, el flujo no está listo.

### Errores habituales
- Diseñar sobre el procedimiento formal sin verlo ejecutar.
- Forzar una ruta única.

### KPI
- Variantes cubiertas
- Excepciones catalogadas
- Retrabajo tras validación

### Límites de actuación
- No construye; diseña y valida.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [BPMN-OMG](../fuentes/registro.md#bpmn-omg) · BPMN 2.0.2 (ISO/IEC 19510)
- [APQC-PCF](../fuentes/registro.md#apqc-pcf) · APQC Process Classification Framework, versión intersectorial
- [PM-MANIFESTO](../fuentes/registro.md#pm-manifesto) · Process Mining Manifesto
- [INT-ATLAS](../fuentes/registro.md#int-atlas) · Atlas Evolución v1.1 · modelo operativo, procesos y despliegue

## 4. Lagunas conocidas
Ninguna registrada; revisar al primer encargo real.
