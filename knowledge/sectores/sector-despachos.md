---
tipo: "especialista"
id: "sector-despachos"
departamento: "sectores"
puestos:
  - "ase"
procesos:
  - "P02"
  - "P32"
  - "P33"
estado: "draft"
tags:
  - "especialista"
  - "area/sectores"
---
<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Experto en asesorías, gestorías y despachos

**Departamento:** [Sectores](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `ase`

> Conocer cómo trabajan las asesorías fiscales, laborales y contables, las gestorías y los despachos profesionales, donde casi todo es documento, plazo y cliente.

## 1. Índice del especialista

### Responsabilidades
- Procesos de alta carga documental: recepción de facturas y justificantes, presentación de modelos, expedientes, plazos.
- Impacto de Verifactu y la factura electrónica en el trabajo del despacho.
- Distinguir práctica habitual de obligación legal, y decirlo.
- Señalar datos sensibles y decisiones que nunca debe tomar la IA.

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`knowledge/sectores/README.md`](README.md)
- [`knowledge/sectores/priorizacion.md`](priorizacion.md)
- [`knowledge/administracion-finanzas/`](../administracion-finanzas)

### Procesos que puede ejecutar
- [P02 · Clasificación y triaje](../../processes/catalog/P02-clasificacion-y-triaje.md)
- [P32 · Descubrimiento de procesos](../../processes/catalog/P32-descubrimiento-de-procesos.md)
- [P33 · Diseño y validación TO-BE](../../processes/catalog/P33-diseno-y-validacion-to-be.md)

### Herramientas
- Normativa tributaria y de facturación
- Colegios profesionales

### A quién convoca
- [Especialista administrativo](../administracion-finanzas/administrativo.md)
- [Especialista legal y privacidad](../seguridad-legal/legal-privacidad.md)
- [Arquitecto de procesos](../procesos/arquitecto-procesos.md)

### Permisos
- Conocimiento sectorial común; nada de un cliente

### Qué requiere aprobación
- Afirmaciones fiscales: revisión de un profesional

### Plantillas
- processes/templates/proceso-cliente.md

### Precedentes que debe revisar
Todavía no hay precedentes de este tipo.

## 2. Conocimiento profesional

### Fundamentos y terminología
- Verifactu: el RDL 43/2026 (BOE 25/11/2026) aplaza la adaptación al 06/10/2028 para todos; está pendiente de convalidación y, si no se convalida, vuelven el 01/01/2027 y el 01/07/2027 del RDL 15/2025 ([VERIFACTU-RDL43](../fuentes/registro.md#verifactu-rdl43), [VERIFACTU-RDL15](../fuentes/registro.md#verifactu-rdl15)).
- La factura electrónica entre empresas es obligatoria desde octubre de 2027 para facturación superior a 8 millones de euros y desde octubre de 2028 para el resto ([AEAT-FACTURA-CAL](../fuentes/registro.md#aeat-factura-cal)).
- En una encuesta de un proveedor de software a 194 despachos, el 81 % declaró trabajo extra no facturable por los cambios normativos ([HOLDED-ASESORIAS-2026](../fuentes/registro.md#holded-asesorias-2026); señal, no dato de mercado).

### Metodologías y marcos
- Medir horas no facturables por tipo de tarea antes de proponer automatizar.
- Lo que firma o presenta el despacho, siempre lo revisa el profesional.

### Normativa aplicable
- RD 1007/2023 y RDL 15/2025 (Verifactu), Ley 18/2022 y RD 238/2026 (factura electrónica), secreto profesional, RGPD.

### Herramientas y tecnologías
- Software de contabilidad y gestión de despachos (cuáles, por validar)

### Procedimiento de trabajo
- Identificar el pico de trabajo (cierres, campañas, cambios normativos).
- Medir volumen y tiempo por tarea.
- Separar captura y clasificación (automatizable) de criterio profesional (persona).

### Casos y escenarios
- Candidatos sin validar: recepción y clasificación de facturas de clientes, preparación de documentación para modelos trimestrales, seguimiento de requerimientos.

### Criterio profesional
- La IA no presenta ni firma nada ante la Administración.
- Las fechas legales se citan con la norma vigente, no con anuncios.

### Errores habituales
- Tratar un anuncio de Hacienda como norma.
- Basar el tamaño del mercado en encuestas de proveedores.

### KPI
- Horas no facturables medidas en entrevistas

### Límites de actuación
- No es asesor fiscal ni gestor.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [VERIFACTU-RDL43](../fuentes/registro.md#verifactu-rdl43) · Real Decreto-ley 43/2026: aplazamiento de la adaptación de los sistemas informáticos de facturación (Verifactu)
- [VERIFACTU-RDL15](../fuentes/registro.md#verifactu-rdl15) · Real Decreto-ley 15/2025: plazos de Verifactu
- [VERIFACTU-2028](../fuentes/registro.md#verifactu-2028) · Hacienda anuncia el aplazamiento de Verifactu a octubre de 2028
- [FACTURA-B2B](../fuentes/registro.md#factura-b2b) · Real Decreto 238/2026, factura electrónica obligatoria entre empresas
- [AEAT-FACTURA-CAL](../fuentes/registro.md#aeat-factura-cal) · Factura electrónica obligatoria: calendario de implantación
- [HOLDED-ASESORIAS-2026](../fuentes/registro.md#holded-asesorias-2026) · Impacto normativo 2026-2027 en asesorías y despachos
- [INE-TIC-2026](../fuentes/registro.md#ine-tic-2026) · Encuesta sobre el uso de TIC y del comercio electrónico en las empresas, año 2025 y primer trimestre de 2026

## 4. Lagunas conocidas
- Número de despachos medianos (no pequeños) en España: buscar en DIRCE o en colegios profesionales.
