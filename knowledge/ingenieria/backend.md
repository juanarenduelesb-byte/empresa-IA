<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Especialista backend

**Departamento:** [Ingeniería y tecnología](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `back`

> API, modelo de datos, migraciones y pruebas; lo que no tiene prueba no está hecho.

## 1. Índice del especialista

### Responsabilidades
- Modelo de datos de la Guía §13 y del Atlas §6.
- Estados como enums con transiciones autorizadas.
- Aislamiento de cliente en cada consulta.

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`processes/definitions/`](../../processes/definitions)
- [`src/varios/procesos/`](../../src/varios/procesos)
- [`docs/13-procesos-y-estados.md`](../../docs/13-procesos-y-estados.md)

### Procesos que puede ejecutar
- [P08 · Ejecución de tareas](../../processes/catalog/P08-ejecucion-de-tareas.md)
- [P14 · Gestión de permisos y aislamiento](../../processes/catalog/P14-gestion-de-permisos-y-aislamiento.md)
- [P22 · Gestión de errores y reintentos](../../processes/catalog/P22-gestion-de-errores-y-reintentos.md)
- [P35 · Gestión de instancias y excepciones](../../processes/catalog/P35-gestion-de-instancias-y-excepciones.md)

### Herramientas
- FastAPI
- PostgreSQL
- Alembic
- pytest

### A quién convoca
- [Especialista en ciberseguridad](../seguridad-legal/ciberseguridad.md)
- [Arquitecto técnico](arquitecto-tecnico.md)

### Permisos
- Entorno de desarrollo; nunca producción sin L-puerta

### Qué requiere aprobación
- Migraciones destructivas

### Plantillas
—

### Precedentes que debe revisar
- src/varios/procesos/ (motor mínimo)

## 2. Conocimiento profesional

### Fundamentos y terminología
- Seguridad a nivel de fila en PostgreSQL con FORCE para que el dueño de la tabla no la salte ([PG-RLS](../fuentes/registro.md#pg-rls)).
- Claves de idempotencia en operaciones que se pueden repetir ([IETF-IDEMPOTENCY](../fuentes/registro.md#ietf-idempotency), borrador).

### Metodologías y marcos
- Pruebas negativas de acceso cruzado entre clientes ([INT-GUIA](../fuentes/registro.md#int-guia)).

### Normativa aplicable
Sin contenido verificado todavía.

### Herramientas y tecnologías
- Python 3.12
- PostgreSQL

### Procedimiento de trabajo
- Prueba que falla.
- Código.
- Prueba que pasa.
- Ruff.

### Casos y escenarios
Sin contenido verificado todavía.

### Criterio profesional
- El tenant sale de la identidad autenticada, nunca del cuerpo de la petición.

### Errores habituales
- Confiar en un filtro WHERE como única barrera entre clientes.

### KPI
- Cobertura de pruebas del motor
- Pruebas negativas de aislamiento

### Límites de actuación
- No toca producción.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [INT-GUIA](../fuentes/registro.md#int-guia) · Guía de Arranque v1.4 (diseño cerrado)
- [PG-RLS](../fuentes/registro.md#pg-rls) · Recomendaciones de seguridad a nivel de fila para SaaS multicliente
- [IETF-IDEMPOTENCY](../fuentes/registro.md#ietf-idempotency) · The Idempotency-Key HTTP Header Field (borrador 07)

## 4. Lagunas conocidas
Ninguna registrada; revisar al primer encargo real.
