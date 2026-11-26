# Seguros · Apertura de siniestros en corredurías (proceso de referencia)

**Estado:** draft. **Todo lo de este documento son hipótesis**, salvo lo que tiene fuente. Se valida en las conversaciones semanales (D-011). Datos: solo inventados. La decisión sobre el proceso de referencia está pendiente (vence el 22/11/2026).

## Lo que sabemos con fuente
Detalle, plazos, glosario y catálogo de excepciones en el [paquete de dominio de seguros](../../knowledge/sectores/seguros/README.md) (B2, draft, borrador para abogado).

- El tomador comunica el siniestro en un máximo de 7 días desde que lo conoce, salvo plazo mayor en la póliza. Si se retrasa, la aseguradora puede reclamar daños y perjuicios, pero no se pierde la cobertura por eso ([LCS art. 16](../../knowledge/fuentes/registro.md#lcs-50-1980)).
- El corredor presta asistencia y asesoramiento en caso de siniestro, y lo que comunica en nombre del tomador vale como si lo hiciera el tomador ([RDL 3/2020 art. 155.3](../../knowledge/fuentes/registro.md#rdl-3-2020); [LCS art. 21](../../knowledge/fuentes/registro.md#lcs-50-1980)).
- Los riesgos extraordinarios los gestiona el Consorcio de Compensación de Seguros. La solicitud puede presentarla el mediador, y en la práctica suele llegar a través de agentes y corredores ([CCS](../../knowledge/fuentes/registro.md#ccs)).
- En daños materiales de una colisión directa entre dos vehículos se aplica el convenio de indemnización directa entre aseguradoras, que desde abril de 2026 refunde CIDE y ASCIDE ([UNESPA-CONVENIO-2026](../../knowledge/fuentes/registro.md#unespa-convenio-2026)).
- Los corredores anotan cada siniestro en su libro-registro en cuanto lo conocen, con un retraso máximo de tres meses ([RD 287/2021 art. 14 y 15](../../knowledge/fuentes/registro.md#rd-287-2021)).
- Las quejas y reclamaciones se resuelven en un mes, y el cliente puede pedir en cualquier momento que le atienda una persona ([Ley 10/2025](../../knowledge/fuentes/registro.md#ley-10-2025)).

## AS-IS hipotético (por validar)
```mermaid
flowchart TD
  A[Cliente comunica el siniestro: teléfono, correo, WhatsApp] --> B[Tramitador identifica cliente y póliza]
  B --> C{¿Cubierto y en plazo?}
  C -- dudas --> D[Pide documentación al cliente]
  D --> B
  C -- sí --> E[Rellena el parte en el portal de la aseguradora]
  E --> F[Registra el expediente en el programa de gestión]
  F --> G[Informa al cliente del número y los siguientes pasos]
  C -- riesgo extraordinario --> H[Solicitud al CCS]
```

## Preguntas para la validación
1. ¿Por qué canales llegan los siniestros y en qué proporción?
2. ¿Cuántos se abren al mes y cuánto tiempo lleva abrir uno: trabajo activo y espera?
3. ¿Qué datos faltan con más frecuencia?
4. ¿Cuántos portales de aseguradoras usáis y cómo se entra en cada uno?
5. ¿Qué errores obligan a rehacer un parte?
6. ¿Qué excepciones son frecuentes (extraordinarios, daños personales, fraude sospechado)?
7. ¿Quién decide qué y qué no debería decidir nunca una máquina?
8. ¿Cuánto cuesta hoy, en horas, un siniestro mal abierto?

## TO-BE candidato (no diseñar en firme hasta validar el AS-IS)
| Paso | Regla | IA propone | Persona |
|---|---|---|---|
| Recepción multicanal | Registro, identificación por póliza | Extraer datos del mensaje | — |
| Comprobación de plazo y póliza | Plazo de 7 días como aviso, nunca como rechazo; póliza vigente (datos inventados) | — | Excepciones (EX-01 a EX-15) |
| Petición de documentación | Lista por tipo de siniestro | Redactar la petición | Aprobar envío (acción externa) |
| Parte en el portal de la aseguradora | — | Prellenar | Enviar (acción externa) |
| Riesgo extraordinario | Detectar por tipo de causa | — | Decidir la vía CCS |

La cobertura y la indemnización no las decide la IA (Atlas §5).

## Métrica de éxito candidata
Tiempo desde la comunicación hasta el parte registrado, con la línea base de las entrevistas. El umbral del examen está pendiente de decidir (22/01/2027).
