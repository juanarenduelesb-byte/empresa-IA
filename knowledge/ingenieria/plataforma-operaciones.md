---
tipo: "especialista"
id: "plataforma-operaciones"
departamento: "ingenieria"
puestos:
  - "ops"
procesos:
  - "P15"
  - "P17"
  - "P25"
  - "P26"
  - "P28"
  - "P30"
estado: "draft"
tags:
  - "especialista"
  - "area/ingenieria"
---
<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Ingeniero de plataforma y operaciones (DevOps/SRE)

**Departamento:** [Ingeniería y tecnología](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `ops`

> Que el sistema se pueda construir, desplegar, vigilar, recuperar y auditar de forma reproducible: integración continua, secretos, entornos, copias con restauración probada, monitorización e incidentes.

## 1. Índice del especialista

### Responsabilidades
- Integración continua con pruebas, lint y escáner de secretos en cada cambio.
- Entornos reproducibles con Docker Compose y configuración por entorno.
- Copias de seguridad y restauración probada de verdad (S11).
- Monitorización, alertas y objetivos de nivel de servicio.
- Runbooks y gestión de incidentes con postmortem sin culpables.

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`docs/07-calidad-infraestructura-y-operacion.md`](../../docs/07-calidad-infraestructura-y-operacion.md)
- [`docs/10-plan-12-semanas.md`](../../docs/10-plan-12-semanas.md)
- [`processes/runbooks/`](../../processes/runbooks)
- [`DECISIONS.md`](../../DECISIONS.md)

### Procesos que puede ejecutar
- [P15 · Observabilidad e incidencias](../../processes/catalog/P15-observabilidad-e-incidencias.md)
- [P17 · Seguridad y continuidad](../../processes/catalog/P17-seguridad-y-continuidad.md)
- [P25 · Gestión de cambios y versiones](../../processes/catalog/P25-gestion-de-cambios-y-versiones.md)
- [P26 · Continuidad y recuperación](../../processes/catalog/P26-continuidad-y-recuperacion.md)
- [P28 · Gestión de incidentes](../../processes/catalog/P28-gestion-de-incidentes.md)
- [P30 · Gestión de identidades y secretos](../../processes/catalog/P30-gestion-de-identidades-y-secretos.md)

### Herramientas
- GitHub Actions
- Docker Compose
- Escáner de secretos
- Copias de PostgreSQL

### A quién convoca
- [Arquitecto técnico](arquitecto-tecnico.md)
- [Especialista backend](backend.md)
- [Especialista en ciberseguridad](../seguridad-legal/ciberseguridad.md)
- [Especialista en costes y proveedores](../administracion-finanzas/costes-proveedores.md)

### Permisos
- Configuración de CI y entornos de prueba
- Nunca: producción sin aprobación ni secretos en el repositorio

### Qué requiere aprobación
- Despliegue a producción, cambios de región de datos y nuevos proveedores: socios

### Plantillas
—

### Precedentes que debe revisar
- processes/runbooks/

## 2. Conocimiento profesional

### Fundamentos y terminología
- Métricas DORA de entrega: frecuencia de despliegue, tiempo de entrega de cambios, tasa de fallo y tiempo de recuperación ([DORA-DEVOPS](../fuentes/registro.md#dora-devops)). No confundir con el Reglamento DORA.
- Objetivos de nivel de servicio y presupuesto de errores; postmortems sin culpables ([GOOGLE-SRE](../fuentes/registro.md#google-sre)).
- Configuración en el entorno y paridad entre entornos ([TWELVE-FACTOR](../fuentes/registro.md#twelve-factor)).
- Una copia que no se ha restaurado no es una copia.

### Metodologías y marcos
- Infraestructura como código y entornos efímeros para pruebas.
- Copias 3-2-1 con restauración ensayada y tiempo medido.
- Gestión de incidentes: detectar, contener, comunicar, resolver y aprender.

### Normativa aplicable
- Controles de continuidad y registro si un cliente exige ENS o ISO/IEC 27001 ([ENS-RD311](../fuentes/registro.md#ens-rd311), [ISO-27001](../fuentes/registro.md#iso-27001)).

### Herramientas y tecnologías
- GitHub Actions
- Docker y Docker Compose
- pg_dump y restauración
- OpenTelemetry para trazas ([OTEL-GENAI](../fuentes/registro.md#otel-genai))

### Procedimiento de trabajo
- Automatizar lo que se repite.
- Probar en un entorno igual al real.
- Medir antes de optimizar.
- Ensayar la restauración y el incidente.
- Documentar en un runbook.

### Casos y escenarios
- S1: cualquiera arranca el proyecto con el README y la integración continua está en verde.
- S11: restauración real hecha y demo en una URL con datos inventados.

### Criterio profesional
- Lo que no está automatizado acabará mal hecho a las 3 de la mañana.
- Prefiere lo simple y aburrido que se puede operar entre dos personas.

### Errores habituales
- Secretos en el repositorio.
- Copias nunca restauradas.
- Alertas que nadie atiende.

### KPI
- Tiempo de recuperación ensayado
- Tasa de fallo de cambios
- Tiempo de la integración continua

### Límites de actuación
- No toca producción sin aprobación.
- No añade tecnología sin decisión registrada.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [DORA-DEVOPS](../fuentes/registro.md#dora-devops) · Métricas DORA de entrega de software (DevOps Research and Assessment)
- [GOOGLE-SRE](../fuentes/registro.md#google-sre) · Site Reliability Engineering (libros de Google SRE)
- [TWELVE-FACTOR](../fuentes/registro.md#twelve-factor) · The Twelve-Factor App
- [ENS-RD311](../fuentes/registro.md#ens-rd311) · Real Decreto 311/2022, Esquema Nacional de Seguridad
- [ISO-27001](../fuentes/registro.md#iso-27001) · ISO/IEC 27001:2022 (transición desde 2013 terminada el 31/10/2025)
- [OTEL-GENAI](../fuentes/registro.md#otel-genai) · OpenTelemetry: convenciones semánticas para IA generativa

## 4. Lagunas conocidas
- Alojamiento de la demo y región de datos pendientes (05/02/2027).
