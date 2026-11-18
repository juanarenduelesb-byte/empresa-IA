<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Conversaciones con Métricas

**Métricas** · 2026-11-17 20:05

**Pieza para Arquitecto de procesos**

# Métrica de éxito y línea base: apertura de siniestros en corredurías

Borrador. Pieza de Métricas (Línea base), departamento de Procesos. Nada de esto es asesoría jurídica.

## Conclusión

Hoy no hay ninguna cifra de partida en el repositorio. Toda la situación de partida está [POR CONFIRMAR]. Lo que sí hay son los controles y los casos del plan, y sobre ellos se puede medir ya, con datos inventados. Propongo medir primero la línea base sobre los 20 siniestros inventados del control B (15/01/2027) y dejar el objetivo con cliente real para L2.

## 1. Hechos (lo que dice el repositorio)

- Proceso de referencia: apertura de siniestros en corredurías, por confirmar en S0 (`docs/10-plan-12-semanas.md`).
- Caso A: la IA lee y extrae; las reglas comprueban póliza y cobertura; los partes con lesiones (datos de salud) salen del flujo automático; el tramitador aprueba cada apertura; una fecha ambigua se marca para revisión. Riesgo medio (`docs/12-simulacion.md`).
- Control A (18/12/2026): 20 casos + 5 trampas acaban en la decisión correcta o en una pregunta, guardado; tests de separación en verde.
- Control B (15/01/2027): 20 siniestros inventados recorren lectura, extracción, reglas, revisión humana, apertura simulada y registro.
- Ningún dato real en todo el periodo. Los datos reales no se usan antes de L2.
- Estado actual: 0 clientes, 0 líneas de código.

## 2. Situación de partida (AS-IS medido)

Ninguna cifra está en el repositorio. Todas quedan por confirmar con una correduría.

| Dato | Valor | Cómo se mide hoy |
|---|---|---|
| Volumen de siniestros al mes | [POR CONFIRMAR] | [POR CONFIRMAR] (registro de la correduría o gestor de siniestros) |
| Tiempo por caso, de la recepción a la apertura | [POR CONFIRMAR] | [POR CONFIRMAR] (probable: marcas de hora del correo y de la apertura) |
| Tiempo de trabajo activo del tramitador por caso | [POR CONFIRMAR] | [POR CONFIRMAR] (cronometrado en una muestra) |
| Errores en la apertura (campos mal, póliza equivocada, duplicados) | [POR CONFIRMAR] | [POR CONFIRMAR] (revisión de una muestra) |
| Partes devueltos o reabiertos por falta de datos | [POR CONFIRMAR] | [POR CONFIRMAR] |
| Porcentaje de partes con lesiones | [POR CONFIRMAR] | [POR CONFIRMAR] |

## 3. Métricas

Cada métrica lleva fórmula, fuente, exclusiones, frecuencia y revisor. Los revisores son una propuesta.

| # | Métrica | Fórmula | Fuente | Exclusiones | Frecuencia | Revisa |
|---|---|---|---|---|---|---|
| E1 | Tiempo por caso (extremo a extremo) | Mediana de (hora de apertura simulada − hora de entrada) | Registro de auditoría en PostgreSQL | Casos bloqueados o en espera de datos del asegurado; el tiempo de espera de aprobación se informa aparte | Por ejecución de prueba; semanal desde S8 | Juan |
| E2 | Tiempo activo del tramitador por caso | Mediana de segundos entre abrir la revisión y aprobar o rechazar | Registro de auditoría | Casos fuera del flujo automático | Por ejecución | Álvaro |
| Q1 | Aperturas correctas sobre 20 | Aperturas con todos los campos correctos ÷ 20 | Casos inventados con resultado esperado (S8) frente a registro | Casos de lesiones, que deben salir del flujo y se miden en S1 | Control B (15/01/2027) y cada ejecución de S9 | Álvaro |
| Q2 | Trampas bien tratadas | Trampas con decisión correcta o pregunta ÷ 5 | Casos trampa con decisión esperada frente a decisión del CEO | Ninguna | Control A (18/12/2026) | Juan y Álvaro |
| Q3 | Falsos positivos de la revisión | Casos marcados para revisión que estaban bien ÷ casos marcados | Etiqueta esperada frente a marca del sistema | Marcas obligatorias por regla (lesiones) | Por ejecución | Álvaro |
| Q4 | Falsos negativos de la revisión | Casos con error no marcados ÷ casos con error | Ídem | Ninguna | Por ejecución | Álvaro |
| Q5 | Campos inferidos mal etiquetados | Campos inferidos presentados como confirmados ÷ campos inferidos | Salida de extracción frente a caso esperado | Ninguna | Por ejecución | Juan |
| S1 | Datos de salud fuera del flujo automático | Partes con lesiones apartados ÷ partes con lesiones | Casos con lesiones inventados frente a registro | Ninguna | Cada ejecución y cada cambio de reglas | Álvaro |
| S2 | Aperturas sin aprobación humana | Número de aperturas sin aprobación registrada | Registro de auditoría | Ninguna | Cada ejecución | Juan |
| S3 | Acciones externas reales | Número de envíos, firmas, pagos o borrados efectivos | Registro de la puerta de herramientas | Ninguna | Cada ejecución | Juan |
| S4 | Acceso entre clientes | Consultas que devuelven datos de otro cliente | Tests de separación | Ninguna | Cada integración en CI | Juan |

## 4. Propuesta

Todo lo que sigue es propuesta, no hecho.

**Objetivos con datos inventados (control B y S9):**

- Q1: 20 de 20 correctas, o un umbral que fijen los socios [POR CONFIRMAR].
- Q2: 5 de 5.
- S1: 100 %.
- S2, S3 y S4: 0 incumplimientos. Un solo fallo cuenta como incumplimiento.
- Q3 y Q4: umbral [POR CONFIRMAR]. Con 20 casos, un solo error ya pesa un 5 %, así que no conviene fijar un porcentaje fino hasta tener el examen de 50 casos de S9. Q4 es la prioridad: un error sin marcar es peor que una marca de más.

**Objetivo de tiempo con cliente (piloto):** reducir el tiempo activo del tramitador por caso, medido frente a la línea base del propio cliente. Propongo expresarlo como reducción porcentual, por ejemplo [POR CONFIRMAR] %, y fijarlo solo cuando exista la línea base real. No se promete ninguna cifra antes. La métrica firmada del piloto 50/50 debe incluir la calidad (Q1, Q4) y la seguridad (S1) como condiciones, no solo el tiempo.

**Condición de lectura:** una mejora de tiempo con peor Q4 o con cualquier fallo de seguridad no cuenta como éxito.

## 5. Cómo medir la línea base con datos inventados

1. Álvaro prepara 20 siniestros inventados con resultado esperado por campo, incluidos casos con lesiones, fecha ambigua, póliza no vigente y cobertura dudosa. Marcados como ejemplos.
2. Se añaden las 5 trampas del control A, con la decisión esperada (CONTINUAR, PREGUNTAR, ESCALAR, RECHAZAR o DERIVAR) y su motivo.
3. Un compañero distinto de quien creó cada caso etiqueta el resultado esperado antes de ejecutar.
4. Línea base manual simulada: Álvaro tramita una muestra a mano y cronometra. Es una referencia orientativa, no la del cliente, y se declara así.
5. Se ejecuta el sistema y se calculan E1, E2, Q1 a Q5 y S1 a S4 desde el registro de auditoría.
6. Se repite en S9 con el examen de 50 casos y se guardan los resultados con fecha y versión.
7. Antes de L2 se pide a una correduría real, con acuerdo y DPA revisado, el volumen, el tiempo y los errores de una muestra [POR CONFIRMAR]. Hasta entonces no se usan datos reales.

## 6. Riesgos de la medición

- Con 20 casos la muestra es pequeña. No se extrapolan porcentajes al cliente.
- Casos inventados por quien construye pueden ser demasiado fáciles. Por eso los etiqueta otra persona.
- El tiempo con datos inventados no equivale al tiempo real y no debe presentarse como tal.

@Arquitecto de procesos: mi pieza usa los pasos AS-IS y TO-BE de tu parte para fijar los puntos de medida de tiempo (entrada y apertura simulada). Confirma que coinciden.
@Diseñador de casos de prueba: necesito que los 10 casos incluyan al menos uno con lesiones, uno con fecha ambigua y uno con póliza no vigente, cada uno con resultado esperado por campo.
@Álvaro: hace falta una correduría que aporte volumen, tiempo y errores de una muestra. Sin ella, la sección 2 sigue entera en [POR CONFIRMAR].

Usado del cerebro: `docs/10-plan-12-semanas.md › Objetivo a 12/02/2027`; `docs/10-plan-12-semanas.md › Controles de paso`; `docs/12-simulacion.md › Casos`; `docs/12-simulacion.md › Los 12 pasos`; `processes/README.md › Catálogo de procesos`; `CLAUDE.md › Contexto rápido`.

Necesita aprobación: un socio debe revisar los umbrales propuestos (Q1, Q3, Q4), la asignación de revisores y la regla de que la mejora de tiempo no cuenta sin calidad ni seguridad, ant

**Métricas** · 2026-11-17 22:34

**Entrega: Línea base y fichas de métricas · Atalaya**

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

| espera | valor | tipo_dato | 
