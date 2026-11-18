<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Línea base y fichas de métricas · Atalaya

**Agente:** Métricas · **Estado:** Hecha · **Riesgo:** medio · **Formato:** xlsx · **Proyecto:** Diagnóstico de apertura de siniestros · Atalaya (ficticia) · **Creado:** 2026-11-17

## Encargo

Proyecto Atalaya (ficticio). Construye la hoja de línea base: volumen mensual por canal y ramo, tiempo activo por paso (rango dicho por el cliente), esperas, partes rehechos, coste de una hora de tramitador como supuesto marcado. Añade las fichas de las 5 métricas del piloto (tiempo activo por apertura, tiempo hasta el acuse al cliente, % de partes sin corrección, % que pasa a persona, coste por caso) con fórmula, fuente, exclusiones, línea base y objetivo propuesto. Distingue dato dicho, estimación y supuesto.

Todo el caso es ficticio: no uses ni busques datos reales de ninguna correduría.

## Contrato de tarea del CEO

- Decisión: CONTINUAR · Motivo: Es un análisis interno sobre datos ficticios, sin datos reales ni envíos, y las cifras desconocidas se pueden marcar sin bloquear el trabajo.
- Objetivo: Dejar una hoja de línea base con volumen, tiempos, esperas, rehechos y coste, y cinco fichas de métricas del piloto con fórmula, fuente, exclusiones y objetivo propuesto, sin datos reales.
- Criterio de aceptación: Hoja xlsx en la que cada cifra lleva etiqueta dicho, estimación, supuesto o calculado con fórmula visible; cada una de las cinco métricas tiene fórmula, fuente, exclusiones, línea base marcada y objetivo propuesto; no aparece ningún dato real.
- Confirmado: Atalaya es un caso ficticio con datos inventados; no se usan datos reales de ninguna correduría.; Volumen medio de 320 siniestros al mes, con picos de más de 600 tras temporales (dato de la directora, no medido).; Trabajo activo de 25 a 40 minutos por apertura (dicho por la directora).; Esperas por documentación que pueden alargar la apertura dos o tres días (dicho).; El 30 % de los partes se rehace al menos una vez (estimación interna, no medida).; Canales: teléfono 40 %, correo 35 %, WhatsApp 15 %, portal 5 %, comercial 5 % (dicho en sesión de arranque).; Seis aseguradoras principales (A a F); solo la A tiene formulario estructurado; el resto usa campos libres sin API conocida.; Cartera de unas 14.000 pólizas; 60 % particulares y 40 % empresas.; Alcance: autos, hogar, comercio, flotas y responsabilidad civil. Fuera: lesionados, pólizas de salud, peritaciones, pagos y coberturas.; Responsable de sistemas con 4 h al mes; el programa de gestión no se cambia.; Las cinco métricas del piloto son: tiempo activo por apertura, tiempo hasta el acuse al cliente, % de partes sin corrección, % que pasa a persona y coste por caso.; Fecha límite del encargo: 11/12/2026.
- Inferido: Volumen por canal aproximado: unos 128 siniestros al mes por teléfono y unos 112 por correo (cálculo sobre 320 y los porcentajes dichos).; Trabajo activo total de unas 133 a 213 horas al mes (320 × 25–40 min), a confirmar con medición.; Partes rehechos estimados de unos 96 al mes (320 × 30 %), con rango pendiente de medir.; La hoja debe usar la estructura de la ficha KPI de processes/templates/proceso-cliente.md.; El coste por hora de tramitador es un supuesto que hay que marcar, no un dato.
- Desconocido: Volumen por ramo (autos, hogar, comercio, flotas, RC).; Tiempo por paso de forma medida y no dicha.; Tiempo hasta el acuse al cliente y cómo se registra hoy.; Porcentaje de partes rehechos medido, y motivo de cada rehecho.; Coste de hora de tramitador (salario, cargas y horas útiles).; Proporción de siniestros con lesionados o excluidos que hay que descontar del volumen.; Objetivo propuesto por métrica, que debe marcarse como propuesta.; Precio del piloto (decidido por los socios).

## Claves del sector

## Claves del sector seguros para el encargo de línea base (Atalaya, ficticia)

**Conclusión:** en la apertura de siniestros lo difícil son las excepciones: lesionados, terceros, riesgos extraordinarios y documentación incompleta. Casi todo lo que hace hoy la correduría es práctica propia, no norma. La decisión de cobertura o rehúse es de una persona.

**Estado:** borrador para revisión de un socio. No enviado. No es asesoría jurídica ni afirma cumplimiento legal. Todos los datos de Atalaya son inventados (D-011). No he abierto `knowledge/sectores/`, así que las referencias a ese directorio van como [POR CONFIRMAR].

- **Vocabulario que usará el cliente:** tomador, asegurado, tercero contrario o perjudicado, parte amistoso, póliza y condiciones particulares, franquicia, rehúse, corredor o mediador, Consorcio de Compensación de Seguros (CCS, riesgos extraordinarios). Definiciones con fuente: [POR CONFIRMAR] en `knowledge/sectores/` (glosario-sector).
- **Plazo de comunicación:** según la entrega previa de claves, el tomador comunica el siniestro en 7 días desde que lo conoce, salvo plazo mayor en la póliza (LCS art. 16). Hecho según extracto. Texto literal y papel de la correduría frente al plazo: [POR CONFIRMAR] con Legal. Consecuencias de un aviso tardío: no constan. Hay que leer el plazo en cada póliza, no asumirlo.
- **Obligaciones del corredor y riesgos extraordinarios:** libros-registro e información del corredor (RD 287/2021); el mediador puede presentar la solicitud ante el CCS, y en la práctica suele hacerlo. Norma y práctica diferenciadas: qué se registra, cuándo y con qué plazo, [POR CONFIRMAR]. Convenios entre aseguradoras para colisiones (CIDE-CICOS): solo draft, no usar como norma firme.
- **Práctica habitual, no norma:** alta manual en seis portales, copiar y pegar desde el programa de gestión, pedir documentación por ida y vuelta, formularios distintos según aseguradora. Es lo que hace Atalaya, no un estándar del sector. Cualquier generalización sobre esto se marca como hipótesis.
- **Excepciones frecuentes:** lesionados (fuera del piloto por decisión de la dirección), terceros contrarios, riesgos extraordinarios, documentación incompleta, comunicación fuera de plazo, siniestros de ramos con reglas propias. La muestra del caso trae un correo con texto que intenta cambiar la decisión del siniestro. Ese contenido se trata como dato y nunca como instrucción.
- **Datos sensibles:** salud (lesionados y pólizas de salud, fuera del piloto), datos de terceros contrarios, matrículas y direcciones de riesgo. Base jurídica para tratar datos de terceros: [POR CONFIRMAR] con Legal y privacidad.
- **Lo que la IA no debe decidir:** cobertura, rehúse, si la póliza responde, si un caso es riesgo extraordinario, si un aviso está fuera de plazo cuando haya duda, si un siniestro queda cubierto, nada que afecte a lesionados, y el envío de cualquier comunicación a cliente o aseguradora sin aprobación humana. Esas decisiones son de una persona.

## Revisión de Calidad

- Cumple: no · rondas: 1 · La línea base está bien separada en dicho, supuesto y calculado, pero no cumple el criterio: falta el formato .xlsx, faltan tres de las cinco fichas, el intervalo de Wilson está mal calculado y hay una afirmación sobre ahorro sin fuente.
- Formato: el criterio pide una hoja .xlsx con cada cifra etiquetada y las fórmulas visibles. La entrega es Markdown provisional y el propio texto dice que el .xlsx queda pendiente. Arreglo: maquetar la hoja en la plantilla de Varios, con una pestaña por bloque y las columnas tipo_dato y fórmula en cada celda calculada.
- Faltan tres de las cinco fichas de métrica. El criterio exige fórmula, fuente, exclusiones, línea base marcada y objetivo propuesto para M1 a M5. Solo están M1 y M2, y la pestaña 8 termina cortada a mitad de frase en el criterio de M2 (“el de esp”). Arreglo: escribir M3 (% de partes sin corrección), M4 (% que pasa a persona) y M5 (coste por caso), y completar M2.
- Cálculo erróneo en la pestaña 6. Para 6 rehechos de 20 con el método de Wilson al 95 %, el intervalo es aproximadamente 13 % a 54 %, no 15 % a 52 %. El método de Wald da 10 % a 50 %, que sí coincide. Arreglo: corregir la cifra, mantener la etiqueta ESTIMACIÓN y citar la fórmula usada.
- Afirmación sin fuente en la pestaña 7: «El ahorro posible en apertura… es pequeño frente a un precio de piloto». No hay precio cerrado (el texto dice [POR CONFIRMAR]) ni cifra de ahorro comparable. Arreglo: eliminar la frase o marcarla como HIPÓTESIS con el cálculo que la sostiene y [POR CONFIRMAR] con los socios.
- Incoherencia en la conclusión: dice que «solo hay tres cifras dichas» (320 casos, 25 a 40 min y 30 % de rehechos), pero la tabla de supuestos marca también como DICHO S02, S05 y S11, además de los porcentajes de canal y los 9 empleados. Arreglo: reescribir la conclusión con el recuento real de cifras DICHO.
- Tratamiento de cifras de 'más de 600' (S02): las fórmulas de pico usan 600 como valor fijo. Está aclarado como suelo, pero la etiqueta de los resultados debe llevar también «CALCULADO con SUPUESTO» o «con suelo DICHO», no solo «CALCULADO sobre DICHO». Arreglo: ajustar la etiqueta en esas cinco filas.
- Fuentes no verificadas: las rutas de los extractos y la plantilla ficha-kpi.md están citadas pero no leídas. La entrega lo declara y lo deja como [POR CONFIRMAR], lo cual es correcto. Antes de pasar a socios, Calidad debe cotejar citas y textos literales contra el repositorio.

## Resultado

## Hoja de línea base y fichas de métrica · Atalaya (ficticia) · versión corregida

**Estado:** borrador para revisión de un socio y de Calidad. No enviado. Nada de esto es asesoría jurídica. Todo dato de Atalaya es inventado (D-011).

**Formato:** este Markdown es provisional. El archivo .xlsx queda pendiente de maquetar con la plantilla de Varios. Cada tabla de abajo es una pestaña, con columnas ya tipadas. Las fórmulas están escritas en texto visible, con referencias por id (S01, S03…), para pasarlas tal cual a las celdas CALCULADO.

**Conclusión:** la línea base de Atalaya es casi toda dicha o supuesta, no medida. Solo hay tres cifras dichas: 320 siniestros al mes, 25 a 40 minutos de trabajo activo por apertura y un 30 % de partes rehechos. Con eso no se puede firmar ningún objetivo del pago 50/50. Los objetivos van como propuesta y se fijan tras medir 20 aperturas consecutivas, según «Guiones de diagnóstico de apertura de siniestros (Atalaya)».

**Etiquetas (columna `tipo_dato`):**
- **DICHO:** lo afirma el cliente, sin medir.
- **ESTIMACIÓN:** deducido por Varios, con método y rango.
- **SUPUESTO:** valor puesto por Varios para poder calcular. Se sustituye por un dato del cliente.
- **CALCULADO:** resultado de una fórmula visible. Si depende de un SUPUESTO, la etiqueta es «CALCULADO con SUPUESTO» y no puede salir en ningún resumen sin ella.
- **[POR CONFIRMAR]:** falta el dato. Se indica quién lo confirma.

**Datos reales (regla L2):** hasta L2 no se pide ni se usa ninguna exportación del programa de gestión ni ningún dato real. Esta hoja solo usa dichos, supuestos y ejemplos ficticios. La exportación por ramo solo se plantearía en L2 o después, anonimizada y con autorización previa de Cumplimiento.

**Sobre las fuentes:** solo he leído los extractos incluidos en este encargo. No he abierto ningún archivo del repositorio. Las rutas que cito (`01-ficha-del-cliente.md`, `02-notas-del-proceso-actual.md`, `04-sistemas-y-restricciones.md`, `knowledge/plantillas/ficha-kpi.md` y las entregas previas) son referencias a esos extractos. Que existan y que el texto coincida literalmente es [POR CONFIRMAR], y lo valida Calidad contra el repositorio.

---

## Pestaña 1 · Supuestos

| id | concepto | valor | unidad | tipo_dato | fuente o método | quién confirma |
|---|---|---|---|---|---|---|
| S01 | Siniestros abiertos al mes (media) | 320 | casos/mes | DICHO | `01-ficha-del-cliente.md › El problema, contado por la dirección (ficticio)` | Directora de siniestros, con registro del programa |
| S02 | Pico tras temporal | más de 600 | casos/mes | DICHO | Ídem | Directora de siniestros |
| S03 | Tiempo activo por apertura, mínimo | 25 | min/caso | DICHO | Ídem | Cronometraje de 20 aperturas |
| S04 | Tiempo activo por apertura, máximo | 40 | min/caso | DICHO | Ídem | Cronometraje de 20 aperturas |
| S05 | Espera por documentación | 2 a 3 | días | DICHO (naturales o laborables: [POR CONFIRMAR]) | Ídem | Directora de siniestros |
| S06 | Partes rehechos al menos una vez | 30 | % | DICHO (impresión, no medida) | Ídem y `02-notas-del-proceso-actual.md › Lo que no saben (para el diagnóstico)` | Muestreo |
| S07 | Coste real de una hora de tramitador | [POR CONFIRMAR] | €/h | sin valor | No consta. No invento cifra | Director general o administración de Atalaya |
| S08 | Coste hora provisional para ensayar fórmulas | 25 | €/h | SUPUESTO (ficticio, sin fuente) | Varios | Se sustituye por S07 |
| S09 | Rango del supuesto S08 | 20 a 30 | €/h | SUPUESTO (ficticio, sin fuente) | Varios | Se sustituye por S07 |
| S10 | Horas productivas por tramitador y mes | [POR CONFIRMAR] | h/mes | sin valor | No consta | Directora de siniestros |
| S11 | Personas en el departamento de siniestros | 9 | personas | DICHO (no consta cuántas abren siniestros) | `01-ficha-del-cliente.md › Quiénes son (ficticio)` | Directora de siniestros |

S08 y S09 no son datos de Atalaya ni de mercado. Sirven solo para ver cómo funciona la fórmula. Si Calidad prefiere no mostrar ninguna cifra en euros, las celdas que dependen de S08 pasan a [POR CONFIRMAR].

---

## Pestaña 2 · Volumen_canal

Fórmula: `casos_canal = S01 × %canal`. Los porcentajes los dice la directora (`02-notas-del-proceso-actual.md › Cómo llegan los siniestros (según la directora)`). Según «Guiones de diagnóstico…», el mix de canales se mide y no se usa como objetivo. Aquí es línea base provisional.

| canal | % | tipo_dato del % | casos/mes | fórmula | tipo_dato del resultado |
|---|---|---|---|---|---|
| Teléfono | 40 | DICHO | 128 | =S01*0,40 | CALCULADO |
| Correo electrónico | 35 | DICHO | 112 | =S01*0,35 | CALCULADO |
| WhatsApp Business | 15 | DICHO | 48 | =S01*0,15 | CALCULADO |
| Portal web del cliente | 5 | DICHO | 16 | =S01*0,05 | CALCULADO |
| Comercial que reenvía | 5 | DICHO | 16 | =S01*0,05 | CALCULADO |
| Total | 100 | CALCULADO | 320 | =SUMA(casos) | CALCULADO |

---

## Pestaña 3 · Volumen_ramo

| ramo | % | casos/mes | tipo_dato | quién confirma |
|---|---|---|---|---|
| Autos | [POR CONFIRMAR] | [POR CONFIRMAR] | sin dato | Directora de siniestros |
| Hogar | [POR CONFIRMAR] | [POR CONFIRMAR] | sin dato | Ídem |
| Comercio | [POR CONFIRMAR] | [POR CONFIRMAR] | sin dato | Ídem |
| Flotas | [POR CONFIRMAR] | [POR CONFIRMAR] | sin dato | Ídem |
| Responsabilidad civil | [POR CONFIRMAR] | [POR CONFIRMAR] | sin dato | Ídem |

- No hay reparto por ramo en el material.
- El único dato indirecto es la cartera: 60 % particulares y 40 % empresas (`01-ficha-del-cliente.md › Quiénes son (ficticio)`). Es cartera de pólizas, no de siniestros, y no sirve para estimar el reparto.
- `03-muestra-de-siniestros.csv` solo se ha leído en extracto (nueve filas). Que sea un fichero ficticio y no contenga datos reales es [POR CONFIRMAR] con quien lo preparó y con Calidad. No se usa para estimar proporciones.
- No se pide ninguna exportación del programa de gestión en esta fase. Ver el apartado «Datos reales (regla L2)» al inicio.

---

## Pestaña 4 · Tiempo_paso

El cliente dio un rango global y un único dato por paso: encontrar la póliza puede llevar 5 minutos si el cliente no la da. No hay desglose y no lo invento.

| paso | descripción | tiempo dicho | tipo_dato | observación |
|---|---|---|---|---|
| 1 | Identificar cliente y póliza | hasta 5 min si no da la póliza | DICHO (caso concreto, no media) | `02-notas-del-proceso-actual.md › Pasos que describen las tramitadoras` |
| 2 | Comprobar vigencia y garantía | [POR CONFIRMAR] | sin dato | «En hogar hay que leer bastante» |
| 3 | Comprobar plazo de comunicación | [POR CONFIRMAR] | sin dato | «Normalmente no es problema» |
| 4 | Pedir lo que falta (ida y vuelta) | [POR CONFIRMAR] | sin dato | «Lo que más tiempo hace perder» |
| 5 | Alta en el portal de la aseguradora | [POR CONFIRMAR] | sin dato | Seis portales, solo A con formulario estructurado (`04-sistemas-y-restricciones.md › Sistemas que usan hoy`) |
| 6 | Registrar número de siniestro | [POR CONFIRMAR] | sin dato | El extracto se corta en este paso |
| 7 | Aviso al cliente | [POR CONFIRMAR] | sin dato | Alcance del proyecto. Numeración y existencia del paso en las notas: [POR CONFIRMAR] con el AS-IS |
| Total | | 25 a 40 min | DICHO | Global, sin desglose |

**Carga mensual de trabajo activo**

| escenario | fórmula | horas/mes | tipo_dato |
|---|---|---|---|
| Mínimo | =S01*S03/60 | 133,3 | CALCULADO sobre DICHO |
| Punto medio | =S01*((S03+S04)/2)/60 | 173,3 | CALCULADO sobre DICHO (media aritmética del rango, no estimación de la media real) |
| Máximo | =S01*S04/60 | 213,3 | CALCULADO sobre DICHO |
| Pico, mínimo | =600*S03/60 | 250 | CALCULADO sobre DICHO (600 es un suelo: «más de 600») |
| Pico, máximo | =600*S04/60 | 400 | CALCULADO sobre DICHO (ídem) |

El rango dicho puede esconder una cola larga (flotas, varios implicados, temporales). Por eso el objetivo se fija sobre la mediana medida y no sobre la media.

---

## Pestaña 5 · Esperas

| espera | valor | tipo_dato | cómo se medirá |
|---|---|---|---|
| Espera por documentación | 2 a 3 días | DICHO | Por caso, fecha de comunicación a fecha de alta en portal. Mediana y percentil 90 |
| Primera respuesta al cliente | [POR CONFIRMAR] | sin dato | Sellos de hora de correo, WhatsApp y registro. La centralita no graba, hay que anotar la hora de las llamadas |
| Espera por el portal de la aseguradora | [POR CONFIRMAR] | sin dato | Cronometraje en la muestra de 20 |

---

## Pestaña 6 · Rehechos

| dato | valor | tipo_dato | fórmula | fuente |
|---|---|---|---|---|
| Partes rehechos al menos una vez | 30 % | DICHO (impresión) | | `01-ficha-del-cliente.md` |
| Casos rehechos al mes con la media | 96 | CALCULADO sobre DICHO | =S01*S06/100 | S01, S06 |
| Proporción con datos completos | [POR CONFIRMAR] | sin dato | | `02-notas-del-proceso-actual.md › Lo que no saben` |
| Causa del retrabajo (incompletos o mal copiados) | [POR CONFIRMAR] | sin dato | | Separar las dos causas en la muestra |

**Margen de error de una muestra de 20 (recalculado):**
- Ejemplo de cálculo: si en 20 aperturas se observaran 6 rehechos (30 %), el intervalo al 95 % con el método de Wilson sale de aproximadamente 15 % a 52 %. Con el método de Wald saldría de aproximadamente 10 % a 50 %.
- La cifra del borrador anterior (12 % a 54 %) era incorrecta y queda retirada.
- Los 6 de 20 son un ejemplo para dimensionar la muestra, no un resultado. Etiqueta: ESTIMACIÓN, método Wilson, pendiente de revisión por Calidad.
- Conclusión: con 20 casos el intervalo es muy ancho. Si el piloto se decide por una métrica de rehechos, hay que ampliar la muestra.

---

## Pestaña 7 · Coste (todo depende de SUPUESTO)

Todas las filas dependen de S08 o S09, que son supuestos ficticios. Ninguna cifra de esta pestaña es dato del cliente ni debe citarse sin la etiqueta.

| concepto | fórmula | valor | tipo_dato | depende_de_supuesto |
|---|---|---|---|---|
| Coste hora | =S08 | 25 €/h | SUPUESTO | sí |
| Coste de apertura, mínimo | =S03/60*S08 | 10,42 €/caso | CALCULADO con SUPUESTO | sí |
| Coste de apertura, máximo | =S04/60*S08 | 16,67 €/caso | CALCULADO con SUPUESTO | sí |
| Coste mensual, mínimo | =133,3*S08 | 3.333 € | CALCULADO con SUPUESTO | sí |
| Coste mensual, máximo | =213,3*S08 | 5.333 € | CALCULADO con SUPUESTO | sí |
| Rango mensual con S09 | =133,3*20 a =213,3*30 | 2.667 € a 6.400 € | CALCULADO con SUPUESTO | sí |

El coste por caso cubre solo trabajo activo de apertura. No incluye esperas, retrabajo, supervisión ni costes indirectos. El ahorro posible en apertura, con estos números, es pequeño frente a un precio de piloto. El caso de negocio con tres escenarios y el precio quedan fuera de esta entrega: el precio es [POR CONFIRMAR] por los socios.

---

## Pestaña 8 · Fichas de métrica

Cada ficha sigue `knowledge/plantillas/ficha-kpi.md`. La plantilla no se ha abierto, así que que los campos coincidan es [POR CONFIRMAR] con Calidad. Todos los objetivos son propuestas y no se firman con el cliente (límite del puesto).

**Horario laborable (aplica a M2):** propuesta de criterio provisional, lunes a viernes en el horario de oficina de Atalaya. El horario exacto es [POR CONFIRMAR] con la directora de siniestros.

### M1 · Tiempo activo por apertura

| campo | contenido |
|---|---|
| Pregunta | ¿Cuánto trabajo humano lleva abrir un siniestro sencillo? |
| Dueña | Directora de siniestros |
| Fórmula | Mediana de los minutos de trabajo humano activo, desde que el tramitador abre el caso hasta que queda dado de alta, registrado y con el aviso preparado, sobre casos sencillos. Se informa también el percentil 90 |
| Unidades y frecuencia | Minutos por caso. Semanal |
| Fuente | Cronometraje de 20 aperturas consecutivas desde un punto de arranque fijado de antemano («Guiones de diagnóstico…»). En el piloto, sellos de hora de la herramienta más muestreo |
| Exclusiones | Esperas de documentación (van en M2 y Esperas). Casos con lesionados, salud, riesgo extraordinario y fuera de plazo con duda. Casos que la persona abandona sin cerrar |
| «Sencillo» | Propuesta: sin documentación pendiente, un solo ramo y sin tercero. Definición final [POR CONFIRMAR] con la directora |
| Línea base | 25 a 40 min (DICHO, global, no medido). Valor medido: [POR CONFIRMAR] |
| Objetivo propuesto | Reducir a la mitad la mediana medida en casos sencillos (criterio de la dirección, `04-sistemas-y-restricciones.md › Lo que se considera éxito (borrador de la dirección)`). Sobre el rango dicho serían 12,5 a 20 min (CALCULADO: =S03/2 y =S04/2). Se fija con la medición |
| Alerta | Mediana por encima del 75 % de la línea base medida dos semanas seguidas |
| Cuidado | La media engaña con colas largas: mediana y percentil 90 |

### M2 · Tiempo hasta el acuse al cliente

| campo | contenido |
|---|---|
| Pregunta | ¿Cuánto tarda el cliente en recibir número de siniestro y siguientes pasos? |
| Dueña | Directora de siniestros |
| Fórmula | Horas laborables entre el sello de hora de la comunicación del cliente y el sello de hora del envío del acuse con número y siguientes pasos. Se informa la mediana y el % de casos con acuse en menos de 2 horas laborables |
| Unidades y frecuencia | Horas laborables y % de casos. Semanal |
| Fuente | Sellos de hora de correo y registro. Las llamadas necesitan anotar la hora porque la centralita no graba |
| Exclusiones | Casos sin número por demora de la aseguradora (se cuentan aparte). Casos excluidos del piloto. Comunicaciones fuera de horario: el reloj arranca en la siguiente apertura del horario |
| Línea base | No consta. Solo la queja cualitativa de «nadie les dice nada» en 48 h (DICHO). Valor medido: [POR CONFIRMAR] |
| Objetivo propuesto | Acuse en menos de 2 horas laborables (criterio de la dirección). % de casos que debe cumplirlo: [POR CONFIRMAR] hasta medir |
| Alerta | Cumplimiento por debajo del % pactado en una semana |
| Criterio sobre la aprobación humana | Propuesta: el tiempo cuenta hasta el envío efectivo, incluida la espera de aprobación, y se informa aparte el tiempo de preparación y el de espera de aprobación para saber dónde se pierde. Confirmación [POR CONFIRMAR] con la directora y Calidad |

### M3 · % de partes sin corrección

| campo | contenido |
|---|---|
| Pregunta | ¿Cuántas altas salen correctas a la primera? |
| Dueña | Directora de siniestros |
| Fórmula | (casos dados de alta sin corrección posterior de datos / casos dados de alta) × 100. Corrección: cambio de un dato ya enviado a la aseguradora, o rehacer el parte por datos incompletos o mal copiados |
| Unidades y frecuencia | %. Semanal, con muestreo |
| Fuente | Marca de corrección en el expediente del programa de gestión o revisión de una muestra por Calidad |
| Exclusiones | Correcciones pedidas por el cliente con información nueva (no son error de alta). Casos excluidos del piloto |
| Línea base | 70 % (CALCULADO: =100−S06 sobre un DICHO que es una impresión). Etiqueta: ESTIMACIÓN con rango amplio. Con n = 20 y 30 % observado, el intervalo Wilson sería de unos 48 % a 85 % sin corrección (complemento del intervalo de la pestaña Rehechos). Pendiente de Calidad. Valor medido: [POR CONFIRMAR] |
| Objetivo propuesto | Principio de la dirección: ningún alta con datos incorrectos por culpa de la herramienta (cero, medido por muestreo). Objetivo numérico global: [POR CONFIRMAR] tras medir |
| Alerta | Cualquier alta incorrecta atribuible a la herramienta |
| Cuidado | Solo cuenta lo que se detecta. Quién revisa y con qué frecuencia: [POR CONFIRMAR] con Calidad. Criterio de «por culpa de la herramienta»: [POR CONFIRMAR] con Calidad |

### M4 · % de casos que pasa a persona

| campo | contenido |
|---|---|
| Pregunta | ¿Qué parte de los casos requiere intervención humana más allá de la aprobación obligatoria? |
| Dueña | Directora de siniestros |
| Fórmula | (casos derivados a persona por duda, falta de datos, excepción o riesgo / casos que entran en el flujo) × 100. Se informa por motivo |
| Unidades y frecuencia | %. Semanal |
| Fuente | Registro de decisiones del CEO digital (CONTINUAR, PREGUNTAR, ESCALAR, RECHAZAR, DERIVAR) |
| Exclusiones | La aprobación humana del envío, siempre obligatoria, no cuenta como paso a persona. Casos fuera de alcance (lesionados, salud) que no entran en el flujo |
| Línea base | No existe como tal: hoy todo lo hace una persona. Proporción de casos con excepción en la muestra: [POR CONFIRMAR] |
| Objetivo propuesto | Sin objetivo único. Propuesta: el 100 % de los casos de riesgo alto se derivan. El % total aceptable se fija tras medir, porque un % alto no es un fallo si los motivos son correctos |
| Alerta | Cualquier caso de riesgo alto no derivado. Subida brusca del % |
| Cuidado | Métrica de control, no de resultado. Se lee junto a M1 y M3 |

### M5 · Coste por caso

| campo | contenido |
|---|---|
| Pregunta | ¿Cuánto cuesta abrir un siniestro con el cambio frente a hoy? |
| Dueño | Director general |
| Fórmula | (minutos de trabajo humano activo por caso / 60) × coste hora S07. Opcional: más coste de operación por caso (Costes, [POR CONFIRMAR]) |
| Unidades y frecuencia | € por caso. Mensual |
| Fuente | M1 y coste hora facilitado por Atalaya |
| Exclusiones | Esperas. Coste de construcción del piloto. Licencias hasta que Costes las entregue |
| Línea base | 10,42 € a 16,67 € por caso: CALCULADO con SUPUESTO ficticio de 25 €/h. No es dato del cliente y no es válida hasta tener S07 |
| Objetivo propuesto | Reducción proporcional a M1, con la misma fórmula. Cifra en euros: [POR CONFIRMAR] |
| Alerta | Coste por caso con herramienta superior a la línea base |
| Cuidado | Depende de un supuesto que no consta. No usar en el contrato ni en resúmenes sin la etiqueta SUPUESTO |

---

## Hecho, hipótesis y propuesta

**Hecho (con fuente en extracto):**
- Volumen medio, rango de minutos, 30 % y canales son lo que dice la dirección, no mediciones.
- Atalaya no mide el tiempo por paso, ni los partes rehechos, ni los datos completos (`02-notas-del-proceso-actual.md › Lo que no saben`).

**Hipótesis (cómo se comprueba):**
- El tiempo real cae entre 25 y 40 min: cronometrar 20 aperturas.
- El 30 % de rehechos es razonable: revisar una muestra de expedientes.
- Hay una cola larga de casos complejos que sube la media: comparar media y mediana.

**Propuesta:**
- Medir antes de fijar objetivos en euros.
- Usar mediana y percentil 90 en M1 y M2.
- Fijar el pago 50/50 sobre una métrica principal (M1 o M3), con las demás como control. Cinco métricas con pago serían difíciles de defender.
- No firmar nada con el cliente: lo hacen los socios con el abogado.

## Lista [POR CONFIRMAR]

| qué falta | quién lo confirma |
|---|---|
| Coste hora real (S07) y horas productivas (S10) | Director general o administración de Atalaya |
| Reparto por ramo (solo en L2 o después, con autorización) | Directora de siniestros y Cumplimiento |
| Que `03-muestra-de-siniestros.csv` sea ficticio y sin datos reales | Quien lo preparó y Calidad |
| Tiempo por paso (pasos 2 a 7) | Cronometraje de 20 aperturas |
| Definición de «caso sencillo» | Directora de siniestros |
| Horario laborable y criterio de espera de aprobación (M2) | Directora de siniestros y Calidad |
| Criterio de «por culpa de la herramienta» y quién revisa (M3) | Calidad |
| Revisión del intervalo Wilson | Calidad |
| «Dos o tres días» naturales o laborables | Directora de siniestros |
| Coste de operación por caso y precio del piloto | Costes y socios |
| Existencia y literalidad de las rutas citadas, campos de `ficha-kpi.md` y numeración de pasos del AS-IS | Calidad |

## Estructura del .xlsx pendiente

Pestañas: Supuestos, Volumen_canal, Volumen_ramo, Tiempo_paso, Esperas, Rehechos, Coste, Fichas_metrica, Por_confirmar. Columnas comunes: `id`, `concepto`, `valor` (número), `unidad`, `tipo_dato` (lista: DICHO, ESTIMACIÓN, SUPUESTO, CALCULADO, CALCULADO con SUPUESTO, POR CONFIRMAR), `fórmula` (texto visible), `depende_de_supuesto` (sí/no), `fuente`, `responsable`.

Usado del cerebro: `precedents/projects/caso-correduria-atalaya/documentos/01-ficha-del-cliente.md › El problema, contado por la dirección (ficticio)`; `processes/templates/proceso-cliente.md › Línea base (ficha KPI por métrica)`; `knowledge/agentes/kpi.md › Reglas del puesto`; `claude/habilidades/business-case.md › Pasos`; `precedents/projects/caso-correduria-atalaya/documentos/04-sistemas-y-restricciones.md › Lo que se considera éxito (borrador de la dirección)`; `precedents/projects/caso-correduria-atalaya/documentos/02-notas-del-proceso-actual.md › Lo que no saben (para el diagnóstico)`; entregas «Guiones de diagnóstico de apertura de siniestros (Atalaya)» y «Claves del sector seguros para Atalaya».

Necesita aprobación: un socio debe decidir si se mantiene el 25 €/h ficticio (S08) o se sustituye por [POR CONFIRMAR], y si el pago 50/50 se liga a una sola métrica principal. Calidad debe revisar el intervalo Wilson, el criterio de M2 sobre la espera de aprobación y la literalidad de las rutas citadas. El .xlsx está pendiente de maquetar.

## Historial

- 2026-11-17 22:30 · Encargo recibido
- 2026-11-17 22:30 · Histórico: 5 antecedentes parecidos (Guiones de diagnóstico de apertura de siniestros (Atalaya); AS-IS de apertura de siniestros · Atalaya; Claves del sector seguros para Atalaya; Mapa de obligacio)
- 2026-11-17 22:30 · CEO: CONTINUAR · riesgo medio → Métricas. Es un análisis interno sobre datos ficticios, sin datos reales ni envíos, y las cifras desconocidas se pueden marcar sin bloquear el trabajo.
- 2026-11-17 22:30 · Métricas empieza
- 2026-11-17 22:30 · Coordinación sectorial · Seguros aporta las claves del sector a Métricas
- 2026-11-17 22:31 · Calidad revisa la entrega contra el criterio
- 2026-11-17 22:32 · Calidad la devuelve: Entrega truncada: termina a mitad de la ficha de M3 («Exclusiones | Correcciones pedidas por el cliente con información n»). Completar la ficha de M3 con las filas que faltan: línea base, objetivo propuesto y alerta, marcando como [POR CONFIRMAR] lo que no conste.; Faltan M4 y M5. El criterio exige las cinco métricas (tiempo activo, tiempo hasta el acuse, % sin corrección, % que pasa a persona y coste por caso) con fórmula, fuente, exclusiones, línea base marcada y objetivo propuesto. Solo hay tres fichas completas y una incompleta. Hay que añadir M4 (% de casos que pasa a persona) y M5 (coste por caso), cada una con los siete campos.; El formato no es el pedido. El criterio habla de una hoja xlsx con cada cifra etiquetada y fórmula visible, y la entrega es Markdown con tablas. Hay que generar el xlsx (o indicar explícitamente que el borrador en Markdown es provisional y que la hoja xlsx queda pendiente) y trasladar a ella las fórmulas de las celdas CALCULADO.; Cifra de intervalo de confianza con error de cálculo. En Hoja 6 se dice que, con 6 partes rehechos de 20 (30 %), el intervalo es «aproximadamente entre 12 % y 54 %». Con el método de Wald sale aproximadamente 10 % a 50 %, y con Wilson aproximadamente 15 % a 52 %. Hay que recalcular, indicar el método usado y dejar la cifra como ESTIMACIÓN pendiente de revisión por Calidad, o retirarla.; La propuesta de exportar datos reales del programa de gestión (Hoja 3) choca con la regla de no usar datos reales de clientes antes de L2. Aunque se condiciona a la autorización de Cumplimiento, debe quedar explícito que la exportación no se pide ni se usa antes de L2 y que, hasta entonces, la hoja solo usa dichos, supuestos y ejemplos ficticios. Además, en la Hoja 3 se afirma que el CSV de muestra tiene «casos de ensayo»: hay que marcar como [POR CONFIRMAR] que ese fichero es ficticio y no contiene datos reales.; Citas de fuentes no verificables en el contexto. La entrega cita rutas como 01-ficha-del-cliente.md, 02-notas-del-proceso-actual.md, 04-sistemas-y-restricciones.md, «Guiones de diagnóstico…» y knowledge/plantillas/ficha-kpi.md. Ninguna se puede comprobar desde esta revisión. Hay que confirmar que existen y que los textos citados coinciden literalmente, o marcarlas como [POR CONFIRMAR] con quién las valida. Lo mismo para el horario laborable de M2, que sigue sin definirse.; Mezcla de etiquetas en el coste por caso. La Hoja 7 y la ficha M2 usan el supuesto de 25 €/h para dar cifras de coste mensual en euros (3.333 €, 5.333 €) con la misma presentación que los cálculos sobre datos. Hay que mantener visible en esas celdas que el resultado depende de SUPUESTO y no de un dato del cliente, y no incluirlas en cualquier resumen sin esa etiqueta.; Errores de redacción menores que no bloquean por sí solos: «Ninguna objetivo» (debe ser «Ningún objetivo») y «Cuidado» en M2 que dice «Hay que decidir si cuenta» sin proponer criterio. Proponer un criterio o marcarlo como [POR CONFIRMAR].
- 2026-11-17 22:33 · Métricas lo maqueta como hoja de cálculo con la plantilla de Varios
- 2026-11-17 22:34 · Entregable listo: Hoja de cálculo v1
- 2026-11-17 22:34 · Calidad: no cumple del todo. Espera aprobación de un socio (riesgo medio)
- 2026-11-17 22:34 · Guardado en la memoria: precedente y lección
- 2026-11-17 22:34 · Aprobado por un socio
