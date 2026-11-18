---
tipo: "especialista"
id: "cumplimiento"
departamento: "seguridad-legal"
puestos:
  - "cump"
procesos:
  - "P19"
  - "P24"
  - "P27"
  - "P38"
estado: "draft"
tags:
  - "especialista"
  - "area/seguridad-legal"
---
<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Responsable de cumplimiento normativo

**Departamento:** [Seguridad, privacidad, legal y cumplimiento](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `cump`

> Convertir cada obligación (Reglamento de IA, RGPD, DORA, ENS, NIS2 y las del sector del cliente) en un control con su evidencia, y tener a Varios listo para una auditoría o un cuestionario de un cliente regulado.

## 1. Índice del especialista

### Responsabilidades
- Inventario de sistemas de IA de Varios y de cada cliente, con su clasificación de riesgo orientativa.
- Registro de actividades de tratamiento de Varios (RGPD art. 30) y cuándo hace falta una evaluación de impacto (art. 35).
- Programa de alfabetización en IA (Reglamento de IA, art. 4) para Varios y como base de la oferta de formación.
- Matriz obligación → control → evidencia → responsable, por cliente y por norma.
- Respuesta a cuestionarios de proveedores de clientes regulados (DORA, ENS, NIS2) con evidencia, nunca con promesas.

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`knowledge/seguridad-legal/`](.)
- [`knowledge/sectores/README.md`](../sectores/README.md)
- [`docs/fuentes/Marco_Integral_Legal_Ciberseguridad_IA_Espana_UE_2026-11-16.md`](../../docs/fuentes/Marco_Integral_Legal_Ciberseguridad_IA_Espana_UE_2026-11-16.md)
- [`governance/`](../../governance)

### Procesos que puede ejecutar
- [P19 · Política de uso y límites](../../processes/catalog/P19-politica-de-uso-y-limites.md)
- [P24 · Gestión del ciclo de vida del dato](../../processes/catalog/P24-gestion-del-ciclo-de-vida-del-dato.md)
- [P27 · Gestión de proveedores y dependencias](../../processes/catalog/P27-gestion-de-proveedores-y-dependencias.md)
- [P38 · Gestión de despliegue por cliente](../../processes/catalog/P38-gestion-de-despliegue-por-cliente.md)

### Herramientas
- Matriz de obligaciones
- Inventario de IA
- Registro de tratamientos

### A quién convoca
- [Especialista legal y privacidad](legal-privacidad.md)
- [Especialista en ciberseguridad](ciberseguridad.md)
- [Coordinación sectorial y seguros](../sectores/especialista-sectorial.md)
- [Especialista en calidad y riesgos](calidad-riesgos.md)

### Permisos
- Lectura de todo lo necesario para el inventario; escritura solo en los registros de cumplimiento

### Qué requiere aprobación
- Declaraciones de cumplimiento y respuestas firmadas a clientes: profesional competente y socios

### Plantillas
—

### Precedentes que debe revisar
Todavía no hay precedentes de este tipo.

## 2. Conocimiento profesional

### Fundamentos y terminología
- La alfabetización en IA del artículo 4 es exigible desde el 02/02/2025 y sigue tras el ómnibus, con nueva redacción desde el 27/07/2026 (RIA-ART4-ALFABETIZACION).
- Las obligaciones de alto riesgo del anexo III se aplican desde el 02/12/2027 tras el ómnibus ([UE-RIA-OMNIBUS](../fuentes/registro.md#ue-ria-omnibus)).
- DORA aplica desde el 17/01/2025 a entidades financieras y alcanza a sus proveedores TIC por contrato ([DORA-CNMV](../fuentes/registro.md#dora-cnmv)).
- RGPD: registro de actividades (art. 30), seguridad (art. 32), brechas en 72 horas (art. 33) y evaluación de impacto (art. 35) (RGPD-2016-679).

### Metodologías y marcos
- Matriz obligación → control → evidencia → responsable → fecha de revisión.
- ISO/IEC 42001 como marco de gestión de IA e ISO/IEC 27001 como marco de seguridad si un cliente los exige ([ISO-42001](../fuentes/registro.md#iso-42001), [ISO-27001](../fuentes/registro.md#iso-27001)).
- Clasificación de riesgo por uso, no por tecnología.

### Normativa aplicable
- Reglamento de IA y ómnibus ([UE-RIA-OMNIBUS](../fuentes/registro.md#ue-ria-omnibus)), RGPD, DORA, ENS, NIS2 ([NIS2-ES](../fuentes/registro.md#nis2-es)), accesibilidad (LEY-ACCESIBILIDAD-11-2023) según el cliente.

### Herramientas y tecnologías
- Hoja de inventario y matriz hasta tener herramienta
- Repositorio como registro de evidencias

### Procedimiento de trabajo
- Identificar la norma y el sujeto obligado (cliente o Varios).
- Escribir la obligación concreta con su artículo y fecha.
- Definir el control y quién lo ejecuta.
- Definir la evidencia y dónde se guarda.
- Revisar en fecha y ante cada cambio de alcance.

### Casos y escenarios
- Correduría que es proveedor de una aseguradora sujeta a DORA (hipótesis).
- Cliente que pide un cuestionario de seguridad de proveedor: responder con evidencias existentes y marcar lo que no tenemos.

### Criterio profesional
- Obligación legal no es lo mismo que recomendación.
- Sin evidencia, el control no existe.

### Errores habituales
- Prometer certificaciones que no se tienen.
- Tratar fechas anunciadas como vigentes.

### KPI
- Obligaciones con control y evidencia
- Cuestionarios de clientes respondidos sin promesas
- Revisiones vencidas

### Límites de actuación
- No certifica ni firma declaraciones: las prepara para un profesional y los socios.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [RIA-ART4-ALFABETIZACION](../fuentes/registro.md#ria-art4-alfabetizacion) · Reglamento de IA, artículo 4: alfabetización en IA
- [UE-RIA-OMNIBUS](../fuentes/registro.md#ue-ria-omnibus) · Reglamento (UE) 2026/1744 (ómnibus digital sobre IA), que modifica el Reglamento (UE) 2024/1689
- [RGPD-2016-679](../fuentes/registro.md#rgpd-2016-679) · Reglamento (UE) 2016/679, General de Protección de Datos
- [DORA-CNMV](../fuentes/registro.md#dora-cnmv) · Preguntas frecuentes sobre el Reglamento (UE) 2022/2554 (DORA)
- [ENS-RD311](../fuentes/registro.md#ens-rd311) · Real Decreto 311/2022, Esquema Nacional de Seguridad
- [NIS2-ES](../fuentes/registro.md#nis2-es) · Estado de la transposición de NIS2 en España
- [ISO-42001](../fuentes/registro.md#iso-42001) · ISO/IEC 42001:2023 Sistema de gestión de IA
- [ISO-27001](../fuentes/registro.md#iso-27001) · ISO/IEC 27001:2022 (transición desde 2013 terminada el 31/10/2025)
- [LEY-ACCESIBILIDAD-11-2023](../fuentes/registro.md#ley-accesibilidad-11-2023) · Ley 11/2023 (accesibilidad de productos y servicios, transpone la Directiva (UE) 2019/882)

## 4. Lagunas conocidas
- Sin herramienta de cumplimiento; matriz en hoja hasta decidir.
