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
- [Responsable de cumplimiento](../seguridad-legal/cumplimiento.md)
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
- Los corredores tienen obligaciones de formación, libros-registro e información ([RD-287-2021](../fuentes/registro.md#rd-287-2021)).
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
- Siniestro de daños materiales entre dos vehículos: posible tramitación por convenio entre aseguradoras ([CIDE-CICOS](../fuentes/registro.md#cide-cicos)).
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
- [RDL-3-2020](../fuentes/registro.md#rdl-3-2020) · Real Decreto-ley 3/2020 (distribución de seguros): actualización de importes por la DGSFP
- [RD-287-2021](../fuentes/registro.md#rd-287-2021) · Real Decreto 287/2021: formación y libros-registro de distribuidores de seguros
- [CIDE-CICOS](../fuentes/registro.md#cide-cicos) · Convenios CIDE/ASCIDE y Centro Informático de Compensación de Siniestros (CICOS)
- [CCS](../fuentes/registro.md#ccs) · Consorcio de Compensación de Seguros: riesgos extraordinarios
- [DORA-CNMV](../fuentes/registro.md#dora-cnmv) · Preguntas frecuentes sobre el Reglamento (UE) 2022/2554 (DORA)
- [DGSFP-MEDIACION](../fuentes/registro.md#dgsfp-mediacion) · Informe estadístico anual de mediación de seguros 2024
- [PL-MA-CORREDURIAS](../fuentes/registro.md#pl-ma-corredurias) · Fusiones y adquisiciones de corredurías de seguros en España: tendencias y situación en 2025
- [INE-TIC-2026](../fuentes/registro.md#ine-tic-2026) · Encuesta sobre el uso de TIC y del comercio electrónico en las empresas, año 2025 y primer trimestre de 2026

## 4. Lagunas conocidas
- Plazos internos reales y sistemas de una correduría.
- Informe original de mediación de la DGSFP (solo hay cita de prensa).
