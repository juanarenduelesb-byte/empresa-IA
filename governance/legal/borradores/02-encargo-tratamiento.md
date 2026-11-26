# Contrato de encargo del tratamiento (art. 28 RGPD) · BORRADOR PARA ABOGADO

> No firmar ni enviar. Se recomienda **no redactar cláusulas propias**: adoptar las cláusulas contractuales tipo de la Comisión ([CCT-ENCARGO-2021-915](../../../knowledge/fuentes/registro.md#cct-encargo-2021-915)) sin modificarlas y rellenar sus cuatro anexos. Valen como garantía suficiente del art. 28 (art. 28.6 y 28.7 del RGPD). Lo que sigue es cómo rellenarlas para el proceso de referencia, más una comprobación del art. 28.3.

## 1. Papeles
- **Responsable del tratamiento:** el Cliente (la correduría). Según la AEPD, el corredor es responsable del tratamiento de los datos de sus clientes ([AEPD-CORREDOR-2018](../../../knowledge/fuentes/registro.md#aepd-corredor-2018)).
- **Encargado del tratamiento:** Varios, que trata los datos solo por cuenta e instrucción del Cliente para prestar el servicio.
- Si Varios decidiera para qué o cómo se tratan los datos, pasaría a ser responsable (art. 28.10 RGPD; [EDPB-GL-07-2020](../../../knowledge/fuentes/registro.md#edpb-gl-07-2020)). Por eso Varios **no usa los datos para entrenar modelos ni para otros clientes**.

## 2. Cómo rellenar las cláusulas tipo
| Cláusula | Elección propuesta | Quién decide |
|---|---|---|
| 5 · Incorporación de terceros | No se usa | Abogado |
| 7.7 · Subencargados | **Opción 2, autorización general**, con preaviso de [30] días y derecho de oposición. La opción 1 (específica) da más control al cliente pero frena cada cambio de proveedor. | Socios con el abogado |
| 7.8 · Transferencias internacionales | Solo si un subencargado trata datos fuera del EEE; ver anexo IV | Abogado |
| 9.2 · Violaciones de seguridad | Notificar al Cliente «sin dilación indebida» y como objetivo en [24] horas, para que el Cliente pueda cumplir sus 72 horas (art. 33 RGPD) | Socios |
| 10 · Resolución | La de las cláusulas tipo (un mes para corregir) | — |

## 3. Anexo I · Partes
Responsable: [razón social del Cliente, contacto del delegado de protección de datos si lo tiene]. Encargado: [razón social de Varios, contacto].

## 4. Anexo II · Descripción del tratamiento (proceso de referencia)
| Campo | Contenido |
|---|---|
| Categorías de interesados | Tomadores, asegurados, beneficiarios y terceros perjudicados que comunican un siniestro; personal de la correduría que lo tramita |
| Categorías de datos | Identificación y contacto; número de póliza; descripción del siniestro, fechas, lugar, bienes dañados; matrículas en automóviles; documentos que adjunte el interesado |
| Datos sensibles | **Por defecto, ninguno.** Si el siniestro tiene daños personales, el sistema registra solo que los hay y no guarda diagnósticos ni partes médicos (excepción EX-04). Cambiarlo exige la base del art. 9.2 que fije el abogado y una adenda. |
| Naturaleza | Recepción, extracción de datos de mensajes, consulta de la cartera, preparación de borradores de parte y de peticiones de documentación, registro del expediente |
| Finalidad | Ayudar a la correduría a abrir siniestros (RDL 3/2020, art. 155.3) y a llevar su libro de siniestros (RD 287/2021, art. 15 c) |
| Duración | La del pedido. Al terminar, devolución o supresión a elección del Cliente (art. 28.3 g) |
| Conservación en Varios | [Ninguna copia tras la devolución, salvo los registros de auditoría sin datos personales] |
| Lugar | [Región del alojamiento, pendiente de decidir antes del 05/02/2027] |

## 5. Anexo III · Medidas técnicas y organizativas
Las cláusulas tipo piden describirlas «de manera concreta y no de manera genérica». Las que ya existen en el código o en la documentación:
- **Aislamiento por cliente:** el cliente sale de la identidad autenticada y nunca de un dato que envía el usuario. Seguridad a nivel de fila forzada en PostgreSQL y pruebas de acceso cruzado ([docs/24-base-de-datos.md](../../../docs/24-base-de-datos.md), D-023).
- **Auditoría que no se puede modificar ni borrar** (D-023).
- **Aprobación humana** de toda acción externa (anexo 5).
- **Datos inventados** en desarrollo y pruebas (D-011).
- Por completar antes de L2: cifrado en tránsito y en reposo, gestión de identidades, copias con restauración probada, registro de accesos y procedimiento de violaciones de seguridad. [Pendiente: tareas S3 y S11 del plan.]

## 6. Anexo IV · Subencargados
| Subencargado | Servicio | Lugar | Garantía de transferencia |
|---|---|---|---|
| [Proveedor del modelo de IA] | Procesamiento de texto | [·] | [·] |
| [Proveedor de alojamiento] | Infraestructura | [·] | [·] |

*Nota: no se rellena con nombres hasta elegir proveedores (decisión «alojamiento y región de datos», antes del 05/02/2027).*

## 7. Comprobación del art. 28.3 RGPD
Las cláusulas tipo cubren todo; esta tabla sirve para comprobarlo si el abogado prefiere un contrato propio ([RGPD-2016-679](../../../knowledge/fuentes/registro.md#rgpd-2016-679)).

| Art. 28.3 | Qué exige | Cláusula tipo |
|---|---|---|
| Encabezado | Objeto, duración, naturaleza, finalidad, tipo de datos, categorías de interesados, obligaciones y derechos del responsable | 6 y anexo II |
| a | Solo instrucciones documentadas del responsable, también para transferencias | 7.1 y 7.8 |
| b | Confidencialidad de las personas autorizadas | 7.4 |
| c | Medidas del art. 32 | 7.4 y anexo III |
| d | Condiciones para subencargados (art. 28.2 y 28.4) | 7.7 |
| e | Asistencia con los derechos de los interesados | 8 |
| f | Ayuda con los art. 32 a 36 (seguridad, brechas, evaluación de impacto, consulta previa) | 8 y 9 |
| g | Suprimir o devolver los datos al terminar, a elección del responsable | 7.3 y 10 |
| h | Información para demostrar el cumplimiento y auditorías, incluidas inspecciones | 7.6 |
| Párrafo final | Avisar si una instrucción infringe el RGPD | 7.1 |
