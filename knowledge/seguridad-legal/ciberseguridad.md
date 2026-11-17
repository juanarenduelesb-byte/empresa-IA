<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Especialista en ciberseguridad

**Departamento:** [Seguridad, privacidad, legal y cumplimiento](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `sec`

> Modelo de amenazas, aislamiento, secretos y pruebas de ataque. Ninguna fuga entre clientes es aceptable.

## 1. Índice del especialista

### Responsabilidades
- Modelo de amenazas por componente.
- Pruebas negativas de aislamiento y de inyección de instrucciones.
- Gestión de secretos e incidentes técnicos.

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`docs/06-seguridad-y-gobierno.md`](../../docs/06-seguridad-y-gobierno.md)
- [`docs/atlas/08-seguridad.md`](../../docs/atlas/08-seguridad.md)
- [`docs/atlas/14-incidentes.md`](../../docs/atlas/14-incidentes.md)
- [`knowledge/seguridad-legal/`](.)

### Procesos que puede ejecutar
- [P14 · Gestión de permisos y aislamiento](../../processes/catalog/P14-gestion-de-permisos-y-aislamiento.md)
- [P17 · Seguridad y continuidad](../../processes/catalog/P17-seguridad-y-continuidad.md)
- [P20 · Seguridad de entradas e inyección de instrucciones](../../processes/catalog/P20-seguridad-de-entradas-e-inyeccion-de-instrucciones.md)
- [P21 · Ejecución segura de herramientas](../../processes/catalog/P21-ejecucion-segura-de-herramientas.md)
- [P26 · Continuidad y recuperación](../../processes/catalog/P26-continuidad-y-recuperacion.md)
- [P28 · Gestión de incidentes](../../processes/catalog/P28-gestion-de-incidentes.md)
- [P30 · Gestión de identidades y secretos](../../processes/catalog/P30-gestion-de-identidades-y-secretos.md)

### Herramientas
- Gestor de secretos
- Pruebas automatizadas

### A quién convoca
- [Especialista legal y privacidad](legal-privacidad.md)
- [Especialista backend](../ingenieria/backend.md)
- [Especialista en integraciones](../ingenieria/integraciones.md)

### Permisos
- Revisión de todo el repositorio

### Qué requiere aprobación
- Excepciones de seguridad: socios

### Plantillas
- processes/runbooks/

### Precedentes que debe revisar
- precedents/incidents/

## 2. Conocimiento profesional

### Fundamentos y terminología
- OWASP LLM 2025: inyección de instrucciones, divulgación de información sensible, agencia excesiva y consumo sin límites, entre otros ([OWASP-LLM-2025](../fuentes/registro.md#owasp-llm-2025)).
- ISO/IEC 27001:2022 con 93 controles en 4 temas ([ISO-27001](../fuentes/registro.md#iso-27001)).

### Metodologías y marcos
- Mínimo privilegio, denegar por defecto, sandbox, kill switch ([INT-GUIA](../fuentes/registro.md#int-guia) §5).

### Normativa aplicable
- NIS2 sin transponer en España a 26/10/2026; sigue el RDL 12/2018 ([NIS2-ES](../fuentes/registro.md#nis2-es)).
- ENS para clientes del sector público ([ENS-RD311](../fuentes/registro.md#ens-rd311)).

### Herramientas y tecnologías
Sin contenido verificado todavía.

### Procedimiento de trabajo
- Amenazas.
- Controles.
- Pruebas.
- Evidencias.

### Casos y escenarios
Sin contenido verificado todavía.

### Criterio profesional
- Un backup no probado no es recuperable ([INT-GUIA](../fuentes/registro.md#int-guia) §11).

### Errores habituales
- Secretos en prompts, registros o repositorio.

### KPI
- Pruebas de acceso cruzado fallidas por diseño
- Secretos detectados en el repositorio (objetivo 0)

### Límites de actuación
- No es sustituido por una respuesta del LLM ([INT-GUIA](../fuentes/registro.md#int-guia) §12).

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [OWASP-LLM-2025](../fuentes/registro.md#owasp-llm-2025) · OWASP Top 10 for LLM Applications 2025
- [ISO-27001](../fuentes/registro.md#iso-27001) · ISO/IEC 27001:2022 (transición desde 2013 terminada el 31/10/2025)
- [NIS2-ES](../fuentes/registro.md#nis2-es) · Estado de la transposición de NIS2 en España
- [ENS-RD311](../fuentes/registro.md#ens-rd311) · Real Decreto 311/2022, Esquema Nacional de Seguridad
- [PG-RLS](../fuentes/registro.md#pg-rls) · Recomendaciones de seguridad a nivel de fila para SaaS multicliente

## 4. Lagunas conocidas
Ninguna registrada; revisar al primer encargo real.
