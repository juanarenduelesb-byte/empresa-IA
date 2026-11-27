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
- Verifactu: el RDL 43/2026 (BOE 25/11/2026) aplaza la adaptación al 06/10/2028 para todos; está pendiente de convalidación y, si no se convalida, vuelven las fechas del RDL 15/2025: antes del 01/01/2027 para los contribuyentes del Impuesto sobre Sociedades y antes del 01/07/2027 para el resto ([VERIFACTU-RDL43](../fuentes/registro.md#verifactu-rdl43), [VERIFACTU-RDL15](../fuentes/registro.md#verifactu-rdl15); las del RDL 15/2025, leídas en el BOE el 27/11/2026).
- Factura electrónica: obligatoria en las operaciones entre empresarios y profesionales establecidos en España; no en las operaciones con particulares ni en las facturas simplificadas no cualificadas ([AEAT-FE-OBLIGADOS](../fuentes/registro.md#aeat-fe-obligados)). Los plazos corren desde el 06/10/2026, día en que entró en vigor la Orden HAC/1028/2026 ([ORDEN-HAC-1028-2026](../fuentes/registro.md#orden-hac-1028-2026)): emitir y recibir a los 12 meses (06/10/2027) si el volumen de operaciones del año anterior pasó de 8 millones de euros y a los 24 meses (06/10/2028) el resto, según el calendario de la AEAT ([AEAT-FACTURA-CAL](../fuentes/registro.md#aeat-factura-cal)). **Sin confirmar** en el texto del BOE del RD 238/2026 y de la Ley 18/2022: no se pudieron leer de noche.
- En una encuesta de un proveedor de software a 194 despachos, el 81 % declaró trabajo extra no facturable por los cambios normativos ([HOLDED-ASESORIAS-2026](../fuentes/registro.md#holded-asesorias-2026); señal, no dato de mercado).

### Metodologías y marcos
- Medir horas no facturables por tipo de tarea antes de proponer automatizar.
- Lo que firma o presenta el despacho, siempre lo revisa el profesional.

### Normativa aplicable
- Verifactu: RD 1007/2023 (reglamento; **sin confirmar** en el BOE), modificado por el RDL 15/2025 ([VERIFACTU-RDL15](../fuentes/registro.md#verifactu-rdl15)) y el RDL 43/2026 ([VERIFACTU-RDL43](../fuentes/registro.md#verifactu-rdl43)).
- Factura electrónica: Ley 18/2022, art. 12, que modifica el art. 2 bis de la Ley 56/2007 (lo dice la Orden HAC/1028/2026, [ORDEN-HAC-1028-2026](../fuentes/registro.md#orden-hac-1028-2026); **sin confirmar** en el texto de la Ley); RD 238/2026 ([FACTURA-B2B](../fuentes/registro.md#factura-b2b), resumen de un despacho; **sin confirmar** en el BOE); Orden HAC/1028/2026 ([ORDEN-HAC-1028-2026](../fuentes/registro.md#orden-hac-1028-2026)).
- Secreto profesional: depende de la profesión (abogacía, asesoría fiscal, graduados sociales) y de su norma o código; **sin confirmar**, no se ha leído ninguna.
- Protección de datos: RGPD ([RGPD-2016-679](../fuentes/registro.md#rgpd-2016-679)).

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
- [VERIFACTU-RDL15](../fuentes/registro.md#verifactu-rdl15) · Real Decreto-ley 15/2025, de 2 de diciembre (modifica el RD 1007/2023: plazos de Verifactu)
- [VERIFACTU-2028](../fuentes/registro.md#verifactu-2028) · Hacienda anuncia el aplazamiento de Verifactu a octubre de 2028
- [FACTURA-B2B](../fuentes/registro.md#factura-b2b) · Real Decreto 238/2026, factura electrónica obligatoria entre empresas
- [AEAT-FACTURA-CAL](../fuentes/registro.md#aeat-factura-cal) · Factura electrónica obligatoria: calendario de implantación
- [AEAT-FE-OBLIGADOS](../fuentes/registro.md#aeat-fe-obligados) · Factura electrónica: quiénes están obligados y qué operaciones incluye
- [ORDEN-HAC-1028-2026](../fuentes/registro.md#orden-hac-1028-2026) · Orden HAC/1028/2026, de 2 de octubre, por la que se regula la solución pública de facturación electrónica
- [RGPD-2016-679](../fuentes/registro.md#rgpd-2016-679) · Reglamento (UE) 2016/679, General de Protección de Datos
- [HOLDED-ASESORIAS-2026](../fuentes/registro.md#holded-asesorias-2026) · Impacto normativo 2026-2027 en asesorías y despachos
- [INE-TIC-2026](../fuentes/registro.md#ine-tic-2026) · Encuesta sobre el uso de TIC y del comercio electrónico en las empresas, año 2025 y primer trimestre de 2026

## 4. Lagunas conocidas
- Número de despachos medianos (no pequeños) en España: buscar en DIRCE o en colegios profesionales.
