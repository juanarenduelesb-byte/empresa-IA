# Priorización de sectores

**Estado:** propuesta, pendiente de que la revisen los socios. **Fecha:** 17/11/2026. **Dueño:** coordinación sectorial.

## Por qué hacía falta
`docs/00-negocio.md` nombraba siete sectores: seguros, banca, salud, servicios profesionales, industria, logística e inmobiliario. Ninguno estaba priorizado con datos. Este documento propone seis sectores con criterios explícitos, para que se pueda discutir y cambiar.

## Lo que dicen los datos generales (hechos con fuente)
- En el primer trimestre de 2026 usaba IA el 33,6 % de las empresas de 10 o más empleados, frente al 21,1 % un año antes. Los servicios van por delante, con un 38,2 %, seguidos de la industria (29,1 %) y la construcción (22,6 %) ([INE-TIC-2026](../fuentes/registro.md#ine-tic-2026)).
- Terceros citan un 48,9 % en las empresas de 50 a 249 empleados, el tamaño al que nos dirigimos. Hay que confirmarlo en INEbase.
- Lectura (hipótesis): la mitad de las medianas ya prueba algo de IA. El hueco no está en «empezar con la IA», sino en que haga trabajo real dentro de un proceso, con control. Eso encaja con nuestra oferta.

## Criterios (propuesta)
1. **Presión normativa con fecha:** una obligación con fecha obliga a ordenar procesos.
2. **Volumen documental repetitivo:** mucho documento y mucha excepción que hoy resuelven personas.
3. **Empresas medianas suficientes** para tener a quién vender.
4. **Riesgo y ciclo de venta:** cuanto más alto el riesgo (datos de salud, decisiones financieras), más lenta la venta y más cara la entrega.
5. **Acceso:** contactos reales de los socios en el sector. **Laguna:** no lo sabemos; lo tienen que decir Juan y Álvaro.

## Los seis sectores propuestos

| Orden | Sector | Presión normativa | Volumen documental | Riesgo y ciclo | Motivo principal |
|---|---|---|---|---|---|
| 1 | [Seguros y mediación](especialista-sectorial.md) | Media: DORA para aseguradoras, distribución | Alto: siniestros, renovaciones | Medio | Proceso de referencia ya elegido por defecto. Sector en consolidación ([PL-MA-CORREDURIAS](../fuentes/registro.md#pl-ma-corredurias)) |
| 2 | [Asesorías, gestorías y despachos](sector-despachos.md) | Alta y con fecha: Verifactu en 2027 y factura electrónica B2B en octubre de 2027 y 2028 ([AEAT-FACTURA-CAL](../fuentes/registro.md#aeat-factura-cal)) | Muy alto | Bajo a medio | Carga extra no facturable declarada por los propios despachos ([HOLDED-ASESORIAS-2026](../fuentes/registro.md#holded-asesorias-2026), señal débil) |
| 3 | [Industria manufacturera](sector-industria.md) | Media: NIS2 anexo II, Reglamento de máquinas | Medio a alto en oficina técnica | Medio | Adopción por debajo de los servicios ([INE-TIC-2026](../fuentes/registro.md#ine-tic-2026)): más hueco |
| 4 | [Logística y transporte](sector-logistica.md) | Media: NIS2 (transporte, mensajería) | Alto: incidencias y excepciones | Medio | Rentabilidad a la baja ([UNO-LOGISTICA](../fuentes/registro.md#uno-logistica)): presión por la productividad |
| 5 | [Servicios financieros no bancarios](sector-financiero.md) | Alta: DORA desde el 17/01/2025 | Alto: expedientes y cumplimiento | Alto: exigencias al proveedor TIC | Cientos de entidades medianas supervisadas ([CNMV-DORA-AUTOEVAL](../fuentes/registro.md#cnmv-dora-autoeval)) |
| 6 | [Sanidad privada](sector-sanidad.md) | Alta: datos de salud, Reglamento de IA y EEDS | Alto en administración | Muy alto | Mercado grande ([IDIS-2026](../fuentes/registro.md#idis-2026)), pero solo procesos administrativos y con revisión legal |

## Descartados por ahora (y por qué)
- **Gran banca:** ciclos de compra largos y equipos propios. Es una hipótesis: sin datos propios.
- **Construcción:** es el sector con menor uso de IA ([INE-TIC-2026](../fuentes/registro.md#ine-tic-2026)). Es un hueco, pero también una señal de baja demanda. Revisar si aparece un contacto.
- **Inmobiliario y retail:** sin fuentes reunidas todavía. Quedan como candidatos.

## Lo que esto NO significa
- No vamos a vender en seis sectores. Hasta el 12/02/2027 se construye un solo proceso de referencia (D-011), y no se abre un segundo paquete sectorial hasta validar el primero (Atlas §11).
- Los expertos sirven para que cada encargo use el vocabulario y las normas correctas, y para decidir el nicho comercial antes del 12/02/2027.

## Qué haría cambiar el orden
- Un socio con contactos fuertes en un sector, porque el acceso pesa más que cualquier criterio.
- Una conversación de validación que confirme o refute el dolor medido en horas.
- Un cambio normativo con fecha (por ejemplo, la ley española de NIS2).
