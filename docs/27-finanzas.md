# Finanzas: forma jurídica, facturación, precio y caja (D2)

**Estado:** propuesta para hablar con el gestor (decisión «forma jurídica y facturación», Álvaro con el gestor, antes del 08/01/2027). **No es asesoramiento fiscal ni jurídico.** Fuentes leídas el 26/11/2026. **Ninguna cifra de precio ni de caja es inventada:** la hoja trae los parámetros vacíos.

## 1. Novedad de esta noche: Verifactu se aplaza al 06/10/2028
- El **Real Decreto-ley 43/2026** se publicó en el BOE el 25/11/2026 y está en vigor desde el 26/11/2026. Aplaza la adaptación de los sistemas de facturación hasta que venza el último plazo del RD 238/2026. Según la AEAT, eso es **antes del 06/10/2028 para todos**, sin distinguir a quien tributa por el Impuesto sobre Sociedades ([VERIFACTU-RDL43](../knowledge/fuentes/registro.md#verifactu-rdl43)).
- **Cautela:** el Congreso tiene que convalidarlo en 30 días. Si no lo hace, vuelven las fechas del RDL 15/2025: 01/01/2027 para quien tributa por Sociedades y 01/07/2027 para el resto ([VERIFACTU-RDL15](../knowledge/fuentes/registro.md#verifactu-rdl15)). Hay que comprobarlo antes del 26/12/2026.
- La **factura electrónica entre empresas** es obligatoria desde el 06/10/2027 para quien factura más de 8 millones de euros y desde el 06/10/2028 para el resto ([AEAT-FACTURA-CAL](../knowledge/fuentes/registro.md#aeat-factura-cal), [FACTURA-B2B](../knowledge/fuentes/registro.md#factura-b2b)).
- **Para nosotros:** una empresa nueva y pequeña tendría las dos obligaciones el mismo día, el 06/10/2028, si se convalida el RDL. Aun así, conviene facturar desde el principio con un programa que ya cumpla las dos, para no tener que cambiar después.

Corregido en el repositorio: la ficha de la fuente, los dos especialistas que daban 2027 como fecha vigente, la priorización de sectores y `docs/17`.

## 2. Forma jurídica: comparativa
| | Sociedad limitada (SL) | Dos autónomos en sociedad civil o comunidad de bienes | SL reconocida como empresa emergente |
|---|---|---|---|
| Responsabilidad | Limitada al capital. Con capital inferior a 3.000 €, los socios responden solidariamente de la diferencia hasta 3.000 € en la liquidación ([LSC-ART4](../knowledge/fuentes/registro.md#lsc-art4)) | Personal e ilimitada de los socios | Como la SL |
| Capital mínimo | 1 €. Mientras no se llegue a 3.000 €, al menos el 20 % del beneficio va a reserva legal | No hay | Como la SL |
| Impuesto sobre el beneficio | Impuesto sobre Sociedades. Nueva creación: 15 % el primer periodo con base positiva y el siguiente. Después, si factura menos de 1 millón, 2026: 19 % hasta 50.000 € de base y 21 % el resto; 2027: 17 % y 20 % ([AEAT-IS-TIPOS](../knowledge/fuentes/registro.md#aeat-is-tipos)) | Depende de la figura: **verificar con el gestor** si tributa por Sociedades o por IRPF en atribución de rentas | 15 % durante cuatro periodos desde el primero con base positiva ([LEY-STARTUPS-28-2022](../knowledge/fuentes/registro.md#ley-startups-28-2022), art. 7) |
| Seguridad Social de los socios | Con control efectivo (la mitad del capital o más; se presume con un tercio, o con un cuarto si tiene funciones de dirección), alta en el RETA como autónomo societario ([SEGSOC-RETA-2026](../knowledge/fuentes/registro.md#segsoc-reta-2026)) | Alta en el RETA de cada socio | Como la SL |
| Con vuestros empleos actuales | Pluriactividad: reintegro del 50 % de lo cotizado por contingencias comunes por encima de 17.323,68 €. **Compatibilidad contractual: M-001, laboralista** | Igual | Igual |
| Requisitos especiales | Notaría y Registro Mercantil | Contrato entre socios | ENISA debe acreditar que el proyecto es innovador y escalable; menos de cinco años; sin repartir dividendos; el 60 % de la plantilla con contrato en España. **Dudoso para una consultora de servicios**: preguntar a ENISA |
| Imagen ante un cliente regulado | **Hipótesis:** una SL transmite más solidez para contratos con aseguradoras | **Hipótesis:** menos | Como la SL |

**Propuesta para hablar con el gestor:** una SL de dos socios. Motivo: la responsabilidad limitada importa cuando se firman contratos con clientes regulados, y el tipo del 15 % del primer año con beneficio reduce la diferencia de coste frente a ser autónomos. Además, pedir a ENISA una opinión sobre la figura de empresa emergente antes de constituir, porque cambia el impuesto de cuatro años. **No se decide aquí**: depende de M-001 (compatibilidad con vuestros empleos), M-003 (acuerdo de socios: reparto, que define quién tiene control efectivo) y del gestor.

Preguntas para el gestor:
1. Con el 50 % cada uno, ¿los dos estamos obligados al RETA como societarios? ¿Cuánto cotizaríamos en pluriactividad y nos aplica la cuota reducida de nuevos autónomos? No se ha encontrado el importe oficial de 2026.
2. ¿Sociedad civil con objeto mercantil o SL? ¿Qué diferencia de coste anual hay, contando gestoría y Registro?
3. ¿Qué programa de facturación nos recomienda, que ya cumpla Verifactu y la factura electrónica?
4. ¿Encaja una consultora de servicios como empresa emergente?

## 3. Requisitos de facturación
- Contenido obligatorio de la factura, plazos de expedición y conservación: [RD-1619-2012](../knowledge/fuentes/registro.md#rd-1619-2012). El IVA, según la [Ley 37/1992](../knowledge/fuentes/registro.md#liva-37-1992); el tipo lo confirma el gestor.
- Plazo de pago entre empresas: 30 días si no se pacta otro y nunca más de 60 por pacto. Mora automática, con interés del BCE más 8 puntos y 40 € por costes de cobro ([LEY-MOROSIDAD-3-2004](../knowledge/fuentes/registro.md#ley-morosidad-3-2004)). Ya está en el contrato marco (D1).
- Verifactu y factura electrónica: sección 1.
- Numeración correlativa por series, una serie para rectificativas. [Validar con el gestor.]

## 4. Modelo de precio y previsión de caja
Hoja: [`knowledge/administracion-finanzas/hojas/precio-y-caja.xlsx`](../knowledge/administracion-finanzas/hojas/precio-y-caja.xlsx). Celdas amarillas para los parámetros y grises para los cálculos.

- **Precio por fase.** Coste = horas de socio × tarifa + costes directos. Precio = coste × (1 + margen). Se calcula con y sin IVA.
- **Piloto 50/50.** La hoja da el cobro esperado (la mitad, más la otra mitad por la probabilidad de éxito) y el margen si el piloto falla. Si ese margen sale negativo, un piloto fallido pierde dinero: es una decisión consciente de los socios.
- **Caja a 18 meses** (diciembre de 2026 a mayo de 2028), en tres escenarios. Se rellenan los diagnósticos que empiezan cada mes y las tasas de paso a diseño y a piloto. La hoja calcula diseños, pilotos, clientes en operación, cobros (al terminar cada fase más el plazo de cobro), pagos y saldo.
- **Probada** con valores de prueba que no se han guardado: sin errores de fórmula, y los cobros caen en el mes esperado.
- **No modela:** el IVA (se cobra y se ingresa), los impuestos sobre el beneficio ni la estacionalidad.

**Para rellenar:** la tarifa y el margen los deciden los socios antes del 29/01/2027. Las horas por fase se miden en el primer diagnóstico; hasta entonces, cualquier número es una hipótesis y así hay que decirlo.
