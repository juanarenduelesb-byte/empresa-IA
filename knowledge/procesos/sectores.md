# Especialistas sectoriales

Un paquete sectorial es una combinación versionada de procesos, reglas, plantillas, conocimiento, conectores, pruebas y controles; no es un agente gigante (Atlas Evolución §5). Estado: draft. Solo el sector seguros tiene fuentes primarias verificadas.

## Seguros (sector del proceso de referencia)

| Tema | Lo que sabemos | Fuente |
|---|---|---|
| Comunicación del siniestro | El tomador, asegurado o beneficiario lo comunica en un máximo de 7 días desde que lo conoce, salvo plazo mayor en la póliza (art. 16) | [LCS-50-1980](../fuentes/registro.md#lcs-50-1980) |
| Pago e intereses | Plazos de pago y mora del asegurador (art. 18 y 20) | [LCS-50-1980](../fuentes/registro.md#lcs-50-1980) |
| Distribución y corredores | El RDL 3/2020 transpone la Directiva de distribución de seguros (IDD) | [RDL-3-2020](../fuentes/registro.md#rdl-3-2020) |
| Obligaciones del corredor | Formación, libros-registro e información estadístico-contable | [RD-287-2021](../fuentes/registro.md#rd-287-2021) |
| Riesgos extraordinarios | Los cubre el CCS; la solicitud la presenta el asegurado, su aseguradora o su mediador, y suele llegar a través de agentes y corredores | [CCS](../fuentes/registro.md#ccs), [CCS-MEDIADOR](../fuentes/registro.md#ccs-mediador) |
| Daños materiales de automóvil | Convenios entre aseguradoras (CIDE/ASCIDE) y compensación electrónica (CICOS), con soporte de TIREA | [CIDE-CICOS](../fuentes/registro.md#cide-cicos) (draft) |
| Proveedores TIC | Si el cliente es una aseguradora sujeta a DORA, los requisitos llegan al proveedor por contrato | [DORA-CNMV](../fuentes/registro.md#dora-cnmv) |
| Contabilidad del sector | Las aseguradoras tienen un plan contable propio (RD 1317/2008) | [PGC-PYMES](../fuentes/registro.md#pgc-pymes) (nota) |
| Datos sensibles | Siniestros con daños personales pueden incluir datos de salud: categoría especial del RGPD | [INT-MARCO](../fuentes/registro.md#int-marco) |

**Límite (Atlas §5):** las decisiones de cobertura e indemnización corresponden a una persona con autoridad. La IA no las toma.

**Lagunas:**
- Plazos internos reales de una correduría para abrir un siniestro.
- Sistemas que usan: programa de gestión, portales de aseguradoras.
- Volumen y tipología. Todo esto sale de las conversaciones de validación.

## Otros sectores (por investigar)

| Sector | Procesos candidatos (Atlas §5) | Dependencias y límites | Normativa a investigar |
|---|---|---|---|
| Banca y finanzas | Alta de clientes, apoyo documental KYC, conciliación, reporting | DORA, secreto, AML, crédito | DORA verificada ([DORA-CNMV](../fuentes/registro.md#dora-cnmv)); el resto, pendiente |
| Salud | Por definir | Datos de salud; responsabilidad clínica | Pendiente |
| Construcción | Por definir | Documentación técnica y de obra | Pendiente |
| Industria | Compras, homologación, órdenes, calidad, incidencias, mantenimiento | Integración ERP/OT; separar IT y OT | Reglamento de máquinas (UE) 2023/1230, modificado por el ómnibus de IA: pendiente |
| Logística | Incidencias, documentación, seguimiento, asignación, excepciones | Eventos, API, geolocalización | Pendiente |
| Retail | Atención, devoluciones, inventario, pedidos, demanda | Datos de consumidores y pagos | Pendiente |
| Inmobiliario | Por definir | Datos personales de inquilinos | Pendiente |
| Servicios profesionales | Propuestas, expedientes, entregables, revisión documental, plazos | Confidencialidad, aprobación del experto | Pendiente |

**Regla:** no se abre un segundo paquete sectorial hasta validar el primero (Atlas §11, P2).
