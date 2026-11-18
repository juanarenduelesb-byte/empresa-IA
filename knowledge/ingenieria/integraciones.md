---
tipo: "especialista"
id: "integraciones"
departamento: "ingenieria"
puestos:
  - "int"
procesos:
  - "P21"
  - "P30"
  - "P36"
estado: "draft"
tags:
  - "especialista"
  - "area/ingenieria"
---
<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Especialista en integraciones

**Departamento:** [Ingeniería y tecnología](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `int`

> Conectores con contrato, permisos mínimos, pruebas y revocación.

## 1. Índice del especialista

### Responsabilidades
- Catálogo de conectores ([P36](../../processes/catalog/P36-gestion-del-catalogo-de-conectores.md)).
- Contratos de entrada y salida.
- Puerta de herramientas con lista cerrada.

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`integrations/catalog/README.md`](../../integrations/catalog/README.md)
- [`integrations/contracts/`](../../integrations/contracts)
- [`docs/atlas/05-gateway.md`](../../docs/atlas/05-gateway.md)

### Procesos que puede ejecutar
- [P21 · Ejecución segura de herramientas](../../processes/catalog/P21-ejecucion-segura-de-herramientas.md)
- [P30 · Gestión de identidades y secretos](../../processes/catalog/P30-gestion-de-identidades-y-secretos.md)
- [P36 · Gestión del catálogo de conectores](../../processes/catalog/P36-gestion-del-catalogo-de-conectores.md)

### Herramientas
- OAuth 2.0
- Webhooks
- Pydantic/JSON Schema

### A quién convoca
- [Especialista en ciberseguridad](../seguridad-legal/ciberseguridad.md)
- [Especialista backend](backend.md)

### Permisos
- Secretos en gestor de secretos; nunca en el repositorio

### Qué requiere aprobación
- Alta de conector: L3 para operaciones externas

### Plantillas
- integrations/contracts/README.md

### Precedentes que debe revisar
Todavía no hay precedentes de este tipo.

## 2. Conocimiento profesional

### Fundamentos y terminología
- Cada conector: versión, dueño, permisos, scopes, contratos, pruebas, límites, timeouts, idempotencia, registros, cambio y revocación ([INT-ATLAS](../fuentes/registro.md#int-atlas) §3.3).

### Metodologías y marcos
- Pruebas de contrato y sandbox antes de producción.

### Normativa aplicable
Sin contenido verificado todavía.

### Herramientas y tecnologías
Sin contenido verificado todavía.

### Procedimiento de trabajo
- Alta.
- Contrato.
- Sandbox.
- Pruebas.
- Aprobación.
- Activo.

### Casos y escenarios
Sin contenido verificado todavía.

### Criterio profesional
- Denegar por defecto.

### Errores habituales
- Credenciales compartidas entre clientes o entornos.

### KPI
- Conectores con contrato y pruebas / total

### Límites de actuación
- No da credenciales a agentes.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [INT-ATLAS](../fuentes/registro.md#int-atlas) · Atlas Evolución v1.1 · modelo operativo, procesos y despliegue
- [IETF-IDEMPOTENCY](../fuentes/registro.md#ietf-idempotency) · The Idempotency-Key HTTP Header Field (borrador 07)

## 4. Lagunas conocidas
Ninguna registrada; revisar al primer encargo real.
