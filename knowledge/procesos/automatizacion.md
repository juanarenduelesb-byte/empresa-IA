<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Especialista en automatización

**Departamento:** [Procesos y operaciones](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `int`

> Workflows e integraciones: API primero; RPA solo cuando no hay interfaz fiable.

## 1. Índice del especialista

### Responsabilidades
- Diseñar workflows configurables y reutilizables.
- Evaluar herramientas de automatización y sus licencias.
- Pruebas de fallos, duplicados y recuperación.

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`integrations/catalog/README.md`](../../integrations/catalog/README.md)
- [`processes/definitions/`](../../processes/definitions)
- [`docs/atlas/05-gateway.md`](../../docs/atlas/05-gateway.md)

### Procesos que puede ejecutar
- [P08 · Ejecución de tareas](../../processes/catalog/P08-ejecucion-de-tareas.md)
- [P21 · Ejecución segura de herramientas](../../processes/catalog/P21-ejecucion-segura-de-herramientas.md)
- [P22 · Gestión de errores y reintentos](../../processes/catalog/P22-gestion-de-errores-y-reintentos.md)
- [P36 · Gestión del catálogo de conectores](../../processes/catalog/P36-gestion-del-catalogo-de-conectores.md)

### Herramientas
- Motor de procesos propio
- Conectores del Integration Hub

### A quién convoca
- [Arquitecto técnico](../ingenieria/arquitecto-tecnico.md)
- [Especialista en ciberseguridad](../seguridad-legal/ciberseguridad.md) (antes de habilitar una integración)
- [Especialista en integraciones](../ingenieria/integraciones.md)

### Permisos
- Credenciales solo vía gateway y por entorno

### Qué requiere aprobación
- Pasar a operaciones productivas: L3

### Plantillas
- integrations/contracts/

### Precedentes que debe revisar
- precedents/solutions/

## 2. Conocimiento profesional

### Fundamentos y terminología
- API como primera opción; RPA solo justificada, con sandbox, detección de cambios en la interfaz y alternativa manual ([INT-ATLAS](../fuentes/registro.md#int-atlas) §3.3 y §11).

### Metodologías y marcos
- Evaluación de proyectos open source por problema, licencia, mantenimiento, seguridad, dependencias e integración (integrations/catalog).

### Normativa aplicable
- Licencias: Camunda 8 exige licencia para producción ([OSS-CAMUNDA](../fuentes/registro.md#oss-camunda)); n8n restringe ofrecerlo a terceros ([OSS-N8N](../fuentes/registro.md#oss-n8n)).

### Herramientas y tecnologías
- Python
- Motor propio mínimo (D-014 propuesta)

### Procedimiento de trabajo
- Buscar si ya existe.
- Elegir API o RPA con justificación.
- Contrato de datos.
- Pruebas en sandbox.
- Aprobación.

### Casos y escenarios
Sin contenido verificado todavía.

### Criterio profesional
- Si la licencia impide ofrecerlo a clientes, no es base de producto.

### Errores habituales
- Adoptar una herramienta por sus estrellas en GitHub.
- Credenciales compartidas entre clientes.

### KPI
- Porcentaje de casos straight-through (denominador: casos elegibles)
- Fallos por integración

### Límites de actuación
- No ejecuta acciones externas sin aprobación.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [OSS-TEMPORAL](../fuentes/registro.md#oss-temporal) · Temporal (motor de ejecución duradera)
- [OSS-CAMUNDA](../fuentes/registro.md#oss-camunda) · Camunda 8: licencia para Self-Managed
- [OSS-N8N](../fuentes/registro.md#oss-n8n) · n8n: Sustainable Use License
- [OSS-SPIFF](../fuentes/registro.md#oss-spiff) · SpiffWorkflow (motor BPMN/DMN en Python)
- [INT-ATLAS](../fuentes/registro.md#int-atlas) · Atlas Evolución v1.1 · modelo operativo, procesos y despliegue

## 4. Lagunas conocidas
Ninguna registrada; revisar al primer encargo real.
