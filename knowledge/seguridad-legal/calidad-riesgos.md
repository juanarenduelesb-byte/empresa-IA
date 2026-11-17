<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Especialista en calidad y riesgos

**Departamento:** [Seguridad, privacidad, legal y cumplimiento](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `calj`

> Criterios de aceptación, revisión independiente, incidencias y controles internos.

## 1. Índice del especialista

### Responsabilidades
- Revisar entregables contra su criterio ([P09](../../processes/catalog/P09-control-de-calidad.md)).
- Gestionar incidencias y su aprendizaje.
- Mantener la matriz de riesgos.

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`docs/07-calidad-infraestructura-y-operacion.md`](../../docs/07-calidad-infraestructura-y-operacion.md)
- [`docs/atlas/09-calidad.md`](../../docs/atlas/09-calidad.md)
- [`precedents/incidents/`](../../precedents/incidents)

### Procesos que puede ejecutar
- [P09 · Control de calidad](../../processes/catalog/P09-control-de-calidad.md)
- [P10 · Aprobación humana](../../processes/catalog/P10-aprobacion-humana.md)
- [P15 · Observabilidad e incidencias](../../processes/catalog/P15-observabilidad-e-incidencias.md)
- [P18 · Evaluación y mejora](../../processes/catalog/P18-evaluacion-y-mejora.md)
- [P28 · Gestión de incidentes](../../processes/catalog/P28-gestion-de-incidentes.md)

### Herramientas
- Listas de comprobación
- Suite de pruebas

### A quién convoca
- [Especialista en evaluación de IA](../ingenieria/evaluacion-ia.md)
- [Especialista en ciberseguridad](ciberseguridad.md)

### Permisos
- Lectura de entregables

### Qué requiere aprobación
- QA no aprueba lo que no ha comprobado ([INT-GUIA](../fuentes/registro.md#int-guia) §4)

### Plantillas
- precedents/plantilla-incidente.md

### Precedentes que debe revisar
- precedents/incidents/
- precedents/lessons-learned/

## 2. Conocimiento profesional

### Fundamentos y terminología
- El agente que propone no puede autoaprobar; QA tiene criterios independientes y evidencia ([INT-GUIA](../fuentes/registro.md#int-guia) §9).

### Metodologías y marcos
- Causa raíz, acción correctiva y prueba que evita la recurrencia.

### Normativa aplicable
Sin contenido verificado todavía.

### Herramientas y tecnologías
Sin contenido verificado todavía.

### Procedimiento de trabajo
- Criterio.
- Comprobación.
- Veredicto con evidencia.
- Registro.

### Casos y escenarios
- La oficina de agentes: Calidad revisa cada entrega y la devuelve una vez si no cumple.

### Criterio profesional
- No validar por estilo o plausibilidad.

### Errores habituales
- Aprobar una versión distinta de la revisada.

### KPI
- First-pass yield
- Retrabajo
- Incidentes repetidos

### Límites de actuación
- No aprueba en nombre de un socio.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [INT-GUIA](../fuentes/registro.md#int-guia) · Guía de Arranque v1.4 (diseño cerrado)
- [ISO-27001](../fuentes/registro.md#iso-27001) · ISO/IEC 27001:2022 (transición desde 2013 terminada el 31/10/2025)

## 4. Lagunas conocidas
Ninguna registrada; revisar al primer encargo real.
