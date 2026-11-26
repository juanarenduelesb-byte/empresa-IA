---
tipo: "metodologia"
id: "cuestionario-descubrimiento"
estado: "draft"
---
# Cuestionario de descubrimiento por puertas (G0–G2)

**Estado:** draft. Lo usan Álvaro (clientes) y Juan (producto). Cada respuesta va a la [ficha de cliente](../plantillas/ficha-cliente.md) con su base: `medido`, `declarado` o `hipotesis`.

## Cómo preguntar
Tres reglas de [The Mom Test](../fuentes/registro.md#mom-test):
1. **Hablar de su trabajo, no de nuestra idea.** No se enseña la solución hasta G2.
2. **Hechos del pasado, no opiniones ni futuro.** «¿Cuándo fue la última vez que…?» en lugar de «¿Usaríais…?». «¿Cuánto pagaríais?» no vale; «¿qué habéis probado y cuánto os costó?» sí.
3. **Escuchar más que hablar** y pedir un compromiso al final: tiempo, una presentación a otra persona o dinero. Los cumplidos no cuentan.

Además:
- Preguntar por roles, nunca pedir datos personales de clientes finales.
- Si enseñan un caso real, verlo en su pantalla, sin copiarlo (D-011).

## G0 · Caso elegido (primera conversación, 45 min, con quien decide)
Objetivo: saber si hay un proceso que duele lo bastante, quién decide y cómo compran. Campos: cualificación, procesos candidatos, interlocutores.

| # | Pregunta | Para qué (campo) |
|---|---|---|
| 1 | ¿Qué tarea repetitiva os ha hecho perder más tiempo el último mes? Contadme la última vez. | procesos.dolor |
| 2 | ¿Cuántas veces pasa al mes? ¿De dónde sale ese número? | procesos.volumen_mes (declarado o medido) |
| 3 | ¿Qué habéis intentado ya para arreglarlo? ¿Qué pasó? ¿Cuánto costó? | cualificacion.competencia |
| 4 | Si mañana se arreglara, ¿cómo lo notaríais? ¿Qué número cambiaría? | cualificacion.metricas |
| 5 | La última vez que comprasteis un servicio parecido, ¿quién lo propuso, quién lo aprobó y cuánto tardó? | proceso_decision, proceso_compra, comprador_economico |
| 6 | ¿Quién sufre más este problema en el día a día? ¿Podemos hablar con esa persona? | interlocutores (hace_el_proceso), impulsor |
| 7 | ¿Qué no podríamos tocar nunca: datos, sistemas, normas, clientes? | restricciones |
| 8 | ¿Sois pyme? ¿Alguna aseguradora os ha pedido cláusulas de DORA? | plantilla, sujeto_dora |

**Puerta superada si:** hay un proceso con volumen y dolor declarados, sabemos quién firma y nos dan acceso a quien lo hace (compromiso de tiempo).

## G1 · Proceso entendido (observación y dos o tres conversaciones con quien hace el proceso)
Objetivo: el proceso actual medido. Campos: procesos (medidos), sistemas y excepciones. Base: [LEI-VSM](../fuentes/registro.md#lei-vsm) (trabajo activo frente a espera).

| # | Pregunta u observación | Para qué |
|---|---|---|
| 1 | Enséñame el último siniestro que abriste, de principio a fin, en tu pantalla. | Secuencia real |
| 2 | ¿Por qué canales llegaron los últimos diez avisos? | Canales (hipótesis 1 del proceso de referencia) |
| 3 | Cronometrar tres aperturas: tiempo activo y esperas. | tiempo_activo_min y tiempo_total (medido) |
| 4 | ¿Qué dato faltó la última vez y cómo lo conseguiste? | Excepción EX-13 |
| 5 | ¿En cuántos portales de aseguradoras entraste esta semana? ¿Cómo se accede a cada uno? | sistemas.integracion |
| 6 | ¿Cuál fue el último parte que tuviste que rehacer? ¿Por qué? | retrabajo |
| 7 | Del catálogo de excepciones (EX-01 a EX-15): ¿cuáles te pasaron el último mes? ¿Hay alguna que no esté? | Validar el [catálogo](../sectores/seguros/excepciones.md) |
| 8 | ¿Qué decides tú y qué consultas? ¿Qué no debería decidir nunca una máquina? | Matriz de aprobaciones |
| 9 | ¿Cómo anotáis hoy el libro de siniestros? | RD 287/2021, art. 15 c |
| 10 | ¿Cuánto tiempo os cuesta, en horas, un siniestro mal abierto? Pensad en el último. | Coste del error |

**Puerta superada si:** el proceso actual está dibujado y validado por quien lo hace, hay línea base **medida** de al menos el tiempo activo y el volumen, y la lista de excepciones está revisada.

## G2 · Diseño aceptado (presentación del proceso propuesto y de la métrica)
Objetivo: que el cliente acepte el proceso nuevo, los controles y una métrica con umbral. Ahora sí se enseña la propuesta.

| # | Pregunta | Para qué |
|---|---|---|
| 1 | Recorramos el proceso propuesto con el último siniestro real: ¿dónde se rompería? | Validación con un caso |
| 2 | ¿Quién aprueba cada envío? ¿Quién lo sustituye en vacaciones? | Matriz de aprobaciones |
| 3 | La métrica: tiempo desde el aviso hasta el parte registrado, con línea base [X] medida. ¿Qué umbral os haría seguir con el piloto? | Métrica y umbral firmados |
| 4 | ¿Qué tendría que pasar para que paréis el piloto? | Criterio de parada |
| 5 | ¿Qué datos reales harán falta en el piloto y quién firma el encargo del tratamiento? | Paso a L2 |
| 6 | ¿Quién más tiene que dar el visto bueno (informática, protección de datos, la aseguradora)? | proceso_decision |

**Puerta superada si:** hay diseño aprobado por escrito, métrica con línea base, umbral y quién la certifica, y la persona que firmará el piloto identificada.
