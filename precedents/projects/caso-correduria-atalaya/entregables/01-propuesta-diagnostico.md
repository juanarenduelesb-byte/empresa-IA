---
tipo: "entregable-ejemplo"
id: "atalaya-propuesta-diagnostico"
estado: "draft"
ficticio: true
plantilla: "knowledge/plantillas/entregables/01-propuesta-diagnostico.md"
---
# Propuesta de diagnóstico · Atalaya Correduría de Seguros (FICTICIA)

> **Ejemplo ficticio.** Atalaya no existe: todo sale de los documentos inventados del caso ([`documentos/`](../documentos/01-ficha-del-cliente.md)). Ninguna cifra es una medición: lo que «dice» el cliente va como **declarado**, lo que creemos como **hipótesis** y lo que no sabemos como hueco entre corchetes. Los huecos se rellenan cuando los socios decidan (precio, fechas) o cuando se mida. Hecho con la plantilla de E1 en la tarea N6 (26/11/2026) y puntuado con la rúbrica de C3 ([revisión](01-propuesta-diagnostico.revision.md)).

**0. Cabecera.** Cliente: Atalaya Correduría de Seguros (ficticia) · Proyecto: diagnóstico de la apertura de siniestros · Fase: venta (G0) · Versión: v1 · Fecha: 26/11/2026 · Autor: Propuestas (agente) · Revisado por: [socio] · Estado: borrador · Confidencial · Datos: ninguno del cliente; solo lo que contó la dirección (L0).

## 1. Resumen
En tres semanas mediremos cómo abrís hoy los siniestros y os diremos qué parte puede hacer la IA con control, qué no debe hacer nunca, con qué riesgo y en qué orden. Pedimos al **director general** que apruebe empezar el **[fecha de arranque]**, con la **directora de siniestros** como responsable del proceso. Precio cerrado: **[precio sin IVA, pendiente de los socios]**. El informe llega al comité tres semanas después del arranque.

## 2. Contexto
- **Situación (declarado):** el departamento de siniestros, con 9 personas, abre unos 320 siniestros al mes de media y más de 600 tras un temporal ([ficha del cliente](../documentos/01-ficha-del-cliente.md)). Llegan por teléfono (40 %), correo (35 %), WhatsApp (15 %), portal web (5 %) y a través de un comercial (5 %) ([notas de la sesión de arranque](../documentos/02-notas-del-proceso-actual.md)).
- **Lo que duele (declarado):** abrir un siniestro lleva, según la directora de siniestros, entre 25 y 40 minutos de trabajo activo, y las esperas por documentación alargan la apertura dos o tres días. Cada aseguradora tiene su portal y sus campos, y los datos se copian a mano desde el programa de gestión. Los clientes dicen que «nadie les dice nada» en las primeras 48 horas.
- **Lo que no se sabe (declarado):** nadie mide cuánto lleva cada paso; el 30 % de partes que se rehacen es una impresión interna, no una medición; tampoco se sabe cuántos siniestros llegan con los datos completos.
- **Pregunta que responde el diagnóstico:** ¿qué parte de la apertura de siniestros puede hacer la IA con control, cuánto tiempo devuelve al equipo y qué riesgo tiene hacerlo?

## 3. Qué haremos
| Semana | Qué | Con quién (rol) | Resultado |
|---|---|---|---|
| 1 | Entrevistas y observación de la apertura en cada canal; volúmenes por canal, ramo y aseguradora | Directora de siniestros y dos tramitadoras | Mapa AS-IS en borrador, con las excepciones que ya conocéis (lesionados, Consorcio, sospecha de fraude, impagos, siniestros de empresa con varios implicados) |
| 2 | Medición: tiempo activo y esperas por paso, partes rehechos y por qué, siniestros que llegan completos | Tramitadoras (registro de tiempos de [número de días] días laborables) | Línea base medida, que sustituye las cifras declaradas |
| 3 | Casos de uso puntuados con el mismo criterio, riesgo (Reglamento de IA y protección de datos), hoja de ruta a 12 meses | Director general, directora de siniestros y responsable de cumplimiento | Informe de diagnóstico para el comité |

**Qué entra:** la apertura de siniestros, desde que llega el aviso hasta que el cliente recibe el número y los siguientes pasos, en todos los canales y ramos.
**Qué no entra:** construir nada, tocar el programa de gestión ni los portales de las aseguradoras, tramitar o liquidar siniestros, y usar datos reales de vuestros clientes. Los expedientes con lesionados o datos de salud se describen en el mapa, pero no se proponen para la IA (lo pidió la dirección).
**Qué necesitamos:** la directora de siniestros [horas] a la semana; dos tramitadoras que registren sus tiempos [número de días] días (sin anotar datos de clientes; lo que les cuesta se estima en la sesión de arranque); una hora a la semana para validar; y, del responsable de sistemas, una lista de los campos que exporta el programa de gestión (dentro de sus 4 horas al mes).
**Entregables:** mapa AS-IS validado por quien hace el proceso, línea base medida, catálogo de excepciones con su frecuencia, casos de uso puntuados con su riesgo, hoja de ruta a 12 meses e informe de diagnóstico.

**Cómo medimos sin datos personales.** El registro de tiempos anota canal, ramo, aseguradora (A–F), paso, minutos y si faltaba algo; nunca nombres, pólizas, matrículas ni contenido de los mensajes. Lo que haya que ver de un expediente se ve en vuestras instalaciones y no sale de ellas.

## 4. Decisiones que se piden
| Decisión | Opciones | Recomendación | Quién | Fecha |
|---|---|---|---|---|
| Empezar el diagnóstico | Sí / ajustar alcance / no | Sí: la dirección ya pide medir antes de decidir un piloto | Director general | [fecha] |
| Responsable del proceso durante el diagnóstico | Directora de siniestros / otra persona | Directora de siniestros: es la dueña del proceso y quien usará el resultado | Director general | [fecha] |
| Cómo se registran los tiempos | Hoja sencilla / formulario / observación directa | Hoja sencilla sin datos de clientes: no toca sistemas y se puede empezar el primer día | Directora de siniestros y responsable de cumplimiento | [fecha] |

## 5. Riesgos, supuestos y límites
- **Hecho:** no usamos datos reales de vuestros clientes en esta fase; la confidencialidad se firma antes de empezar.
- **Hecho:** el tomador tiene que comunicar el siniestro en un máximo de 7 días desde que lo conoce, salvo plazo mayor en la póliza ([Ley 50/1980, art. 16](../../../../knowledge/fuentes/registro.md#lcs-50-1980)). Por eso el plazo de comunicación aparece como paso y como excepción en el mapa. Esta referencia no es asesoría jurídica.
- **Supuesto:** las tramitadoras pueden registrar tiempos [número de días] días sin que baje el servicio. Si coincide con un temporal, se aplaza la semana 2 y se dice.
- **Hipótesis:** el mayor ahorro está en identificar al cliente y la póliza, pedir lo que falta y copiar los datos al portal de cada aseguradora, porque es lo que las tramitadoras describen como «buscar, copiar y pedir». La medición de la semana 2 la confirma o la descarta.
- **Riesgo:** que la medición dé un ahorro menor del que esperáis. El diagnóstico no garantiza que haya un caso rentable; si no lo hay, lo diremos.
- **Límite:** nada saldrá hacia clientes o aseguradoras sin que lo apruebe una persona, ni en el diagnóstico ni en un piloto posterior. Los expedientes con lesionados o datos de salud no se proponen para la IA.

## 6. Siguientes pasos
| Qué | Quién (rol) | Cuándo |
|---|---|---|
| Revisar esta propuesta y dar el OK para enviarla | [socio] | [fecha] |
| Firmar el acuerdo de confidencialidad y el pedido | Director general | [fecha] |
| Sesión de arranque y entrega de la hoja de tiempos | [socio] y directora de siniestros | Día 1 del diagnóstico |
| Lista de campos que exporta el programa de gestión | Responsable de sistemas | Semana 1 |

## 7. Condiciones, fuentes y anexos
- **Condiciones:** precio [sin IVA, pendiente de los socios], pago [al entregar el informe, pendiente], plazo de pago [pendiente]. Contrato marco y pedido de la fase (borradores para abogado en `governance/legal/borradores/`).
- **Fuentes del cliente (ficticias):** [ficha del cliente](../documentos/01-ficha-del-cliente.md), [notas de la sesión de arranque](../documentos/02-notas-del-proceso-actual.md), [sistemas y restricciones](../documentos/04-sistemas-y-restricciones.md) y [muestra de 15 siniestros](../documentos/03-muestra-de-siniestros.csv), todas del caso de práctica, tal como están en el repositorio el 26/11/2026.
- **Fuentes del registro:** [LCS-50-1980](../../../../knowledge/fuentes/registro.md#lcs-50-1980).
