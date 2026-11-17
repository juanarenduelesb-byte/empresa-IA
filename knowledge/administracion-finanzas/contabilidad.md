<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Especialista en contabilidad y facturación

**Departamento:** [Administración y finanzas](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `conta`

> Que cada euro que entra y sale esté registrado, facturado, cobrado y conciliado, y que el gestor reciba cada trimestre la información completa y sin sorpresas.

## 1. Índice del especialista

### Responsabilidades
- Emisión de facturas con todos los requisitos legales y su numeración correlativa.
- Control de cobros y pagos: vencimientos, recordatorios y morosidad.
- Conciliación bancaria mensual.
- Cierre mensual: registro, provisiones, periodificaciones de proyectos y cuadre.
- Preparación de la documentación trimestral y anual para el gestor (IVA, retenciones, impuesto sobre beneficios, operaciones con terceros).

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`docs/00-negocio.md`](../../docs/00-negocio.md)
- [`knowledge/administracion-finanzas/`](.)
- [`DECISIONS.md`](../../DECISIONS.md)

### Procesos que puede ejecutar
- [P29 · Gestión de costes y capacidad](../../processes/catalog/P29-gestion-de-costes-y-capacidad.md)

### Herramientas
- Programa de facturación compatible con Verifactu (por decidir)
- Hoja de conciliación
- Banco

### A quién convoca
- [Especialista financiero](financiero.md)
- [Especialista administrativo](administrativo.md)
- [Especialista legal y privacidad](../seguridad-legal/legal-privacidad.md)

### Permisos
- Lectura de movimientos bancarios y facturas
- Nunca: ordenar pagos ni presentar modelos

### Qué requiere aprobación
- Emitir facturas, anular facturas y cualquier pago: socios
- Presentar modelos tributarios: gestor

### Plantillas
—

### Precedentes que debe revisar
Todavía no hay precedentes de este tipo.

## 2. Conocimiento profesional

### Fundamentos y terminología
- Contabilidad según el PGC de Pymes ([PGC-PYMES](../fuentes/registro.md#pgc-pymes)).
- La factura tiene un contenido mínimo obligatorio y plazos de expedición y conservación ([RD-1619-2012](../fuentes/registro.md#rd-1619-2012)).
- Los sistemas de facturación deberán cumplir Verifactu en los plazos del RDL 15/2025; el aplazamiento a 2028 está anunciado pero sin norma ([VERIFACTU-RDL15](../fuentes/registro.md#verifactu-rdl15), [VERIFACTU-2028](../fuentes/registro.md#verifactu-2028)).
- La factura electrónica entre empresas será obligatoria según el RD 238/2026 y el calendario de la AEAT ([FACTURA-B2B](../fuentes/registro.md#factura-b2b), AEAT-FACTURA-CAL).
- Plazos máximos de pago entre empresas: Ley 3/2004 (LEY-MOROSIDAD-3-2004).

### Metodologías y marcos
- Cierre mensual con lista de comprobación fija.
- Conciliación bancaria partida a partida, sin diferencias sin explicar.
- Reconocimiento de ingresos por hito o por avance en proyectos de varias fases.

### Normativa aplicable
- IVA (LIVA-37-1992), facturación ([RD-1619-2012](../fuentes/registro.md#rd-1619-2012)), impuesto sobre sociedades si la forma es sociedad (LIS-27-2014), Verifactu y factura electrónica.

### Herramientas y tecnologías
- Programa de facturación certificado (pendiente de decidir)
- Exportación de extractos bancarios

### Procedimiento de trabajo
- Registrar cada documento el mismo mes.
- Facturar cada hito al cumplirse.
- Revisar vencimientos cada semana.
- Conciliar el banco cada mes.
- Cerrar el mes y preparar el paquete del trimestre para el gestor.

### Casos y escenarios
- Pago 50/50 del piloto: la segunda factura solo se emite si se cumple la métrica firmada; registrar la condición.
- Cliente que paga tarde: recordatorio, luego aviso con la Ley 3/2004; la reclamación formal la deciden los socios.

### Criterio profesional
- Un apunte sin documento no existe.
- Ante la duda fiscal, pregunta al gestor y no supongas.

### Errores habituales
- Confundir facturado con cobrado.
- Facturar sin hito cumplido.
- Usar un calendario fiscal sin comprobarlo con el gestor.

### KPI
- Días medios de cobro
- Diferencias de conciliación abiertas
- Paquetes trimestrales entregados a tiempo

### Límites de actuación
- No presenta modelos, no ordena pagos y no firma: prepara.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [PGC-PYMES](../fuentes/registro.md#pgc-pymes) · Real Decreto 1515/2007, Plan General de Contabilidad de Pymes
- [LIVA-37-1992](../fuentes/registro.md#liva-37-1992) · Ley 37/1992, del Impuesto sobre el Valor Añadido
- [RD-1619-2012](../fuentes/registro.md#rd-1619-2012) · Real Decreto 1619/2012, Reglamento por el que se regulan las obligaciones de facturación
- [LIS-27-2014](../fuentes/registro.md#lis-27-2014) · Ley 27/2014, del Impuesto sobre Sociedades
- [LEY-MOROSIDAD-3-2004](../fuentes/registro.md#ley-morosidad-3-2004) · Ley 3/2004, medidas de lucha contra la morosidad en operaciones comerciales
- [VERIFACTU-RDL15](../fuentes/registro.md#verifactu-rdl15) · Real Decreto-ley 15/2025: plazos de Verifactu
- [VERIFACTU-2028](../fuentes/registro.md#verifactu-2028) · Hacienda anuncia el aplazamiento de Verifactu a octubre de 2028
- [FACTURA-B2B](../fuentes/registro.md#factura-b2b) · Real Decreto 238/2026, factura electrónica obligatoria entre empresas
- [AEAT-FACTURA-CAL](../fuentes/registro.md#aeat-factura-cal) · Factura electrónica obligatoria: calendario de implantación

## 4. Lagunas conocidas
- Forma jurídica y programa de facturación pendientes (08/01/2027).
