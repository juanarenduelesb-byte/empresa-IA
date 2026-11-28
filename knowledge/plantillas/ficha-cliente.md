---
tipo: "plantilla"
id: "ficha-cliente"
estado: "draft"
---
# Plantilla · Ficha de cliente

Una ficha por cliente. Es la versión legible del esquema [`ficha-cliente.schema.json`](ficha-cliente.schema.json), que sale de `src/varios/clientes/ficha.py`. Ejemplo relleno, con un cliente inventado: [`ejemplos/ficha-cliente-atalaya.json`](ejemplos/ficha-cliente-atalaya.json).

## Reglas
- **Sin datos personales.** Los interlocutores se guardan por **rol**. Nombres, correos y teléfonos van al CRM (M-014), no aquí. El modelo rechaza cualquier texto con un correo, un teléfono o un DNI o NIE; un nombre no se puede reconocer con un patrón, así que lo vigila quien escribe la ficha.
- **Cada dato dice de dónde sale:** `medido` (lo hemos visto o cronometrado), `declarado` (lo dice el cliente) o `hipotesis` (lo suponemos nosotros). Una cifra sin origen no entra.
- **Tamaño por rangos**, no cifras exactas.
- **Hasta L2, solo clientes inventados** y marcados como `ficticio` (D-011).
- Se actualiza después de cada conversación (ver [guion semanal](../metodologias-transversales/guion-validacion-semanal.md)).

## Campos
| Bloque | Qué va | Se rellena en |
|---|---|---|
| Identificación | id, nombre, `ficticio`, sector, tipo de entidad, plantilla (rango), sujeto a DORA (sí, no o por confirmar) | G0 |
| Estado | puerta actual (G0–G6) y nivel de datos (L0–L4) | Cada puerta |
| Interlocutores | Rol, si decide, si hace el proceso, si empuja dentro | G0 y G1 |
| Sistemas | Tipo, uso y si se puede integrar (API, exportación, portal manual) | G1 |
| Procesos candidatos | Volumen al mes, tiempo activo, tiempo total, retrabajo, dolor de 1 a 5, riesgo, datos sensibles, si es el elegido. Cada número con su base | G0 (candidatos) y G1 (medidos) |
| Cualificación (MEDDPICC) | Métricas, comprador económico, criterios y proceso de decisión, proceso de compra, dolor, impulsor y competencia. Cada uno con su base | G0 |
| Restricciones y normas | Lo que no se puede hacer; ids del registro de fuentes que aplican | G0–G2 |
| Hitos | Fecha, puerta, decisión y quién decidió (rol) | Cada puerta |
| Conversaciones | Fecha, tipo, con quién (roles), qué aprendimos, qué compromiso puso el cliente, siguiente paso y qué cambia | Cada semana |
| Preguntas abiertas | Lo que aún no sabemos | Siempre |

## Fuentes
- Cualificación: [MEDDICC](../fuentes/registro.md#meddicc).
- Medición del proceso: tiempo de proceso frente a tiempo total ([LEI-VSM](../fuentes/registro.md#lei-vsm)).
- Conversaciones: preguntar por hechos pasados y medir compromisos ([MOM-TEST](../fuentes/registro.md#mom-test)).
