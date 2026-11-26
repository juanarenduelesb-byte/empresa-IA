---
tipo: "especialista"
id: "especialista-sectorial"
departamento: "sectores"
puestos:
  - "seg"
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
# Coordinación sectorial y seguros

**Departamento:** [Sectores](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `seg`

> Coordinar a los expertos de sector y llevar el sector del proceso de referencia: seguros y mediación. Decide qué experto entra en cada encargo y mantiene la priorización de sectores.

## 1. Índice del especialista

### Responsabilidades
- Elegir el experto sectorial de cada encargo ([P02](../../processes/catalog/P02-clasificacion-y-triaje.md)) y convocar a otro si el caso cruza sectores.
- Mantener knowledge/sectores/priorizacion.md con fuentes y fecha.
- Vocabulario, reglas y excepciones de corredurías y aseguradoras.
- Distinguir práctica habitual de obligación legal, y decirlo.
- Señalar datos sensibles y decisiones que nunca debe tomar la IA.

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`knowledge/sectores/README.md`](README.md)
- [`knowledge/sectores/priorizacion.md`](priorizacion.md)
- [`knowledge/sectores/seguros/README.md`](seguros/README.md)
- [`processes/referencia-seguros-apertura-siniestros/README.md`](../../processes/referencia-seguros-apertura-siniestros/README.md)

### Procesos que puede ejecutar
- [P02 · Clasificación y triaje](../../processes/catalog/P02-clasificacion-y-triaje.md)
- [P32 · Descubrimiento de procesos](../../processes/catalog/P32-descubrimiento-de-procesos.md)
- [P33 · Diseño y validación TO-BE](../../processes/catalog/P33-diseno-y-validacion-to-be.md)

### Herramientas
- Normativa de seguros
- Registro de mediadores de la DGSFP
- Asociaciones del sector

### A quién convoca
- [Arquitecto de procesos](../procesos/arquitecto-procesos.md)
- [Responsable de cumplimiento normativo](../seguridad-legal/cumplimiento.md)
- y el experto del sector del encargo

### Permisos
- Conocimiento sectorial común; nada de un cliente

### Qué requiere aprobación
- Afirmaciones regulatorias: revisión competente
- Abrir un segundo sector: los socios (Atlas §11)

### Plantillas
- processes/templates/proceso-cliente.md

### Precedentes que debe revisar
- precedents/lessons-learned/

## 2. Conocimiento profesional

### Fundamentos y terminología
- El tomador comunica el siniestro en un máximo de 7 días desde que lo conoce, salvo plazo mayor en la póliza ([LCS-50-1980](../fuentes/registro.md#lcs-50-1980), art. 16).
- Los corredores tienen obligaciones de formación, libros-registro e información; el libro de siniestros se anota en cuanto el corredor conoce el siniestro y no puede ir más de tres meses retrasado ([RD-287-2021](../fuentes/registro.md#rd-287-2021), art. 14 y 15).
- El corredor presta asistencia y asesoramiento al cliente en caso de siniestro ([RDL-3-2020](../fuentes/registro.md#rdl-3-2020), art. 155.3), y lo que comunica en nombre del tomador vale como si lo comunicara el tomador ([LCS-50-1980](../fuentes/registro.md#lcs-50-1980), art. 21).
- Corredores y aseguradoras resuelven quejas y reclamaciones en un mes (Ley 44/2002, art. 29, en la redacción de LEY-10-2025); adaptación hasta el 28/12/2026.
- Detalle y catálogo de excepciones: knowledge/sectores/seguros/.
- A 21/11/2025 había 3.445 corredores inscritos en la DGSFP: 884 personas físicas y 2.561 sociedades (DGSFP-MEDIACION, cita indirecta).
- El mercado de corredurías se consolida por escala, sucesión y requisitos regulatorios (PL-MA-CORREDURIAS): más tamaño, más procesos que ordenar.
- Si el cliente es una aseguradora sujeta a DORA, los requisitos llegan al proveedor TIC por contrato ([DORA-CNMV](../fuentes/registro.md#dora-cnmv)).

### Metodologías y marcos
- Paquete sectorial: procesos, reglas, plantillas, conocimiento, conectores, pruebas y controles versionados ([INT-ATLAS](../fuentes/registro.md#int-atlas) §5).
- Priorizar sectores con criterios explícitos y revisables, no por intuición (knowledge/sectores/priorizacion.md).

### Normativa aplicable
- LCS, RDL 3/2020 (distribución), RD 287/2021, DORA para aseguradoras, RGPD (datos de salud en siniestros con daños personales).

### Herramientas y tecnologías
- Programas de gestión de corredurías y portales de aseguradoras (cuáles, por validar)

### Procedimiento de trabajo
- Leer la ficha del sector y la priorización.
- Verificar la vigencia de la norma.
- Elegir y convocar al experto del sector.
- Validar con un profesional del sector antes de usarlo con un cliente.

### Casos y escenarios
- Apertura de siniestros en corredurías (proceso de referencia, hipótesis).
- Siniestro de daños materiales entre dos vehículos: posible tramitación por el convenio de indemnización directa (UNESPA-CONVENIO-2026).
- Candidatos sin validar: renovaciones, solicitudes al CCS, conciliación de comisiones.

### Criterio profesional
- Cobertura e indemnización las decide una persona con autoridad ([INT-ATLAS](../fuentes/registro.md#int-atlas) §5).
- Ninguna afirmación sectorial sin fuente o sin marcar como hipótesis.

### Errores habituales
- Inventar requisitos sectoriales.
- Abrir varios sectores a la vez antes de validar el primero.

### KPI
- Afirmaciones sectoriales con fuente / total
- Hipótesis del sector confirmadas o refutadas en entrevistas

### Límites de actuación
- No sustituye a un abogado, perito ni tramitador.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [LCS-50-1980](../fuentes/registro.md#lcs-50-1980) · Ley 50/1980, de Contrato de Seguro
- [RDL-3-2020](../fuentes/registro.md#rdl-3-2020) · Real Decreto-ley 3/2020, libro II: distribución de seguros y reaseguros privados
- [RD-287-2021](../fuentes/registro.md#rd-287-2021) · Real Decreto 287/2021, sobre formación y remisión de la información estadístico-contable de los distribuidores de seguros y reaseguros
- [LEY-10-2025](../fuentes/registro.md#ley-10-2025) · Ley 10/2025, de 26 de diciembre, por la que se regulan los servicios de atención a la clientela
- [RDLEG-8-2004](../fuentes/registro.md#rdleg-8-2004) · Real Decreto Legislativo 8/2004, texto refundido de la Ley sobre responsabilidad civil y seguro en la circulación de vehículos a motor
- [BAREMO-2026](../fuentes/registro.md#baremo-2026) · Resolución de 3 de febrero de 2026, de la DGSFP, cuantías actualizadas del baremo de tráfico
- [UNESPA-CONVENIO-2026](../fuentes/registro.md#unespa-convenio-2026) · Convenio entre entidades aseguradoras de automóviles para la indemnización directa de daños materiales a vehículos (refunde CIDE, ASCIDE y CICOS)
- [RD-300-2004](../fuentes/registro.md#rd-300-2004) · Real Decreto 300/2004, Reglamento del seguro de riesgos extraordinarios
- [CCS-SOLICITUD](../fuentes/registro.md#ccs-solicitud) · CCS: solicitud de indemnización por riesgos extraordinarios
- [LOSSEAR-ART99](../fuentes/registro.md#lossear-art99) · Ley 20/2015, de ordenación, supervisión y solvencia de las entidades aseguradoras y reaseguradoras, art. 99
- [CIDE-CICOS](../fuentes/registro.md#cide-cicos) · Convenios CIDE/ASCIDE y Centro Informático de Compensación de Siniestros (CICOS)
- [CCS](../fuentes/registro.md#ccs) · Consorcio de Compensación de Seguros: riesgos extraordinarios
- [DORA-CNMV](../fuentes/registro.md#dora-cnmv) · Preguntas frecuentes sobre el Reglamento (UE) 2022/2554 (DORA)
- [DGSFP-MEDIACION](../fuentes/registro.md#dgsfp-mediacion) · Informe estadístico anual de mediación de seguros 2024
- [PL-MA-CORREDURIAS](../fuentes/registro.md#pl-ma-corredurias) · Fusiones y adquisiciones de corredurías de seguros en España: tendencias y situación en 2025
- [INE-TIC-2026](../fuentes/registro.md#ine-tic-2026) · Encuesta sobre el uso de TIC y del comercio electrónico en las empresas, año 2025 y primer trimestre de 2026

## 4. Lagunas conocidas
- Plazos internos reales y sistemas de una correduría.
- Informe original de mediación de la DGSFP (solo hay cita de prensa).
