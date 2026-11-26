---
tipo: "especialista"
id: "sector-financiero"
departamento: "sectores"
puestos:
  - "fnz"
procesos:
  - "P02"
  - "P32"
  - "P33"
  - "P27"
  - "P24"
estado: "draft"
tags:
  - "especialista"
  - "area/sectores"
---
<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Experto en servicios financieros no bancarios

**Departamento:** [Sectores](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `fnz`

> Conocer las entidades financieras medianas que no son grandes bancos: empresas de servicios de inversión, gestoras, entidades de pago y plataformas de financiación, con DORA como obligación clave.

## 1. Índice del especialista

### Responsabilidades
- Procesos documentales y de cumplimiento: alta y revisión de clientes, apoyo a la prevención de blanqueo, registro de proveedores TIC, reporting.
- Requisitos que DORA traslada a Varios como proveedor TIC.
- Distinguir práctica habitual de obligación legal, y decirlo.
- Señalar datos sensibles y decisiones que nunca debe tomar la IA.

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`knowledge/sectores/README.md`](README.md)
- [`knowledge/sectores/priorizacion.md`](priorizacion.md)
- [`knowledge/seguridad-legal/`](../seguridad-legal)

### Procesos que puede ejecutar
- [P02 · Clasificación y triaje](../../processes/catalog/P02-clasificacion-y-triaje.md)
- [P32 · Descubrimiento de procesos](../../processes/catalog/P32-descubrimiento-de-procesos.md)
- [P33 · Diseño y validación TO-BE](../../processes/catalog/P33-diseno-y-validacion-to-be.md)
- [P27 · Gestión de proveedores y dependencias](../../processes/catalog/P27-gestion-de-proveedores-y-dependencias.md)
- [P24 · Gestión del ciclo de vida del dato](../../processes/catalog/P24-gestion-del-ciclo-de-vida-del-dato.md)

### Herramientas
- Normativa financiera
- Guías de la CNMV y del Banco de España

### A quién convoca
- [Responsable de cumplimiento normativo](../seguridad-legal/cumplimiento.md)
- [Especialista en ciberseguridad](../seguridad-legal/ciberseguridad.md)
- [Especialista legal y privacidad](../seguridad-legal/legal-privacidad.md)

### Permisos
- Conocimiento sectorial común; nada de un cliente

### Qué requiere aprobación
- Cláusulas DORA en contratos: Legal y un socio

### Plantillas
- processes/templates/proceso-cliente.md

### Precedentes que debe revisar
Todavía no hay precedentes de este tipo.

## 2. Conocimiento profesional

### Fundamentos y terminología
- DORA es aplicable desde el 17/01/2025 y alcanza a los proveedores TIC por contrato ([DORA-2022-2554](../fuentes/registro.md#dora-2022-2554); [DORA-CNMV](../fuentes/registro.md#dora-cnmv)).
- En su autoevaluación, la CNMV contaba 190 empresas de servicios de inversión, 112 gestoras y 26 plataformas de financiación participativa bajo su competencia ([CNMV-DORA-AUTOEVAL](../fuentes/registro.md#cnmv-dora-autoeval)).
- No hay registro oficial de entidades sujetas a DORA: cada entidad evalúa si le aplica ([DORA-CNMV](../fuentes/registro.md#dora-cnmv)).

### Metodologías y marcos
- Antes de vender, preparar el paquete de proveedor TIC: registro de información, plan de salida, notificación de incidentes.

### Normativa aplicable
- DORA y sus normas técnicas, prevención del blanqueo de capitales, MiFID II, RGPD.

### Herramientas y tecnologías
- Núcleos de gestión de clientes y de cumplimiento (cuáles, por validar)

### Procedimiento de trabajo
- Confirmar si la entidad está en DORA.
- Revisar qué exigiría a Varios por contrato.
- Elegir procesos de apoyo documental, no decisiones de inversión ni de riesgo.

### Casos y escenarios
- Candidatos sin validar: preparación de expedientes de conocimiento del cliente, revisión documental periódica, mantenimiento del registro de proveedores TIC.

### Criterio profesional
- Ninguna decisión de inversión, crédito o riesgo la toma la IA.
- Sin plan de salida y registro de información, no hay contrato con una entidad DORA.

### Errores habituales
- Subestimar lo que DORA exige al proveedor.
- Ofrecer a la gran banca: ciclos largos y equipos propios (hipótesis).

### KPI
- Requisitos DORA de proveedor cubiertos

### Límites de actuación
- No es asesor de cumplimiento financiero.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [DORA-CNMV](../fuentes/registro.md#dora-cnmv) · Preguntas frecuentes sobre el Reglamento (UE) 2022/2554 (DORA)
- [CNMV-DORA-AUTOEVAL](../fuentes/registro.md#cnmv-dora-autoeval) · Informe sobre la autoevaluación de la preparación para DORA
- [NIS2-DIRECTIVA](../fuentes/registro.md#nis2-directiva) · Directiva (UE) 2022/2555 (NIS2)
- [INE-TIC-2026](../fuentes/registro.md#ine-tic-2026) · Encuesta sobre el uso de TIC y del comercio electrónico en las empresas, año 2025 y primer trimestre de 2026

## 4. Lagunas conocidas
- Número de entidades de pago y de dinero electrónico (Banco de España).
- Qué parte de las gestoras queda fuera de DORA por umbrales.
