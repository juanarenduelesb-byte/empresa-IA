<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Reunión: IA y evaluación y Seguridad

**Agente:** IA y evaluación · **Estado:** Hecha · **Riesgo:** bajo · **Formato:** texto · **Creado:** 2026-11-17

## Encargo

como proteger nuestra IA

## Contrato de tarea del CEO

- Decisión: CONTINUAR · Motivo: —
- Objetivo: Acta de la reunión sobre: como proteger nuestra IA
- Criterio de aceptación: Acta con asistentes, acuerdos, decisiones y siguientes pasos con responsable
- Confirmado: —
- Inferido: —
- Desconocido: —

## Resultado

## Acta de reunión: protección de la IA y examen de 50 casos

**Estado:** borrador. No se ha enviado ni publicado. Pendiente de revisión por los socios.
**Fecha de la reunión:** [POR CONFIRMAR]
**Ruta sugerida en el repositorio:** [POR CONFIRMAR]

### Asistentes
- IA y evaluación (Ingeniería)
- Seguridad (Calidad-seguridad-legal)

Los socios (Juan y Álvaro) no asistieron. Las decisiones quedan como propuesta para ellos.

### Tema
Cómo proteger la IA del producto (CEO digital, adaptador de modelos, puerta de herramientas) y cómo medirlo con el examen de 50 casos (S9) y las 5 trampas del control A (18/12/2026).

### Hechos
- El plan vigente (D-011) fija el control A el 18/12/2026 (20 casos + 5 trampas), la seguridad y el aislamiento de clientes en S3, la puerta de herramientas en S6 y el examen de 50 casos en S9.
- Hasta L2 solo se usan datos inventados.
- Con 50 casos no se puede prometer un porcentaje de robustez general. Solo se informa de qué casos pasan y cuáles no.

### Acuerdos
1. El texto externo (correos, PDFs de siniestros) se trata como dato y no como instrucción. Las instrucciones del sistema van aparte.
2. El modelo propone y no ejecuta. La puerta de herramientas decide y ninguna acción se aprueba a sí misma.
3. La salida se valida contra un esquema estricto (campos confirmados, inferidos o desconocidos). Si no valida, el CEO pregunta o escala.
4. Se registra cada llamada al modelo en auditoría (versión de instrucciones, modelo, resultado) para poder repetir cualquier examen.
5. El examen completo se repite ante cada cambio de modelo o de instrucciones.
6. El examen incluye una parte adversa: inyección en documentos, intentos de saltar el aislamiento entre clientes y peticiones de acciones prohibidas. Las 5 trampas del control A son su primera versión.
7. Solo se informa de qué casos pasan y cuáles no, sin prometer un porcentaje general.

### Desacuerdos abiertos
| Tema | IA y evaluación | Seguridad | Estado |
|---|---|---|---|
| Valor de la regla del adaptador | Lo impone el adaptador de modelos | No basta: la inyección puede colarse. La defensa real es que el modelo no pueda ejecutar nada ni ver datos de otro cliente | Hipótesis de Seguridad, a validar. No es un hecho |
| Umbral de aprobación | [POR CONFIRMAR] con Seguridad | Cero fallos en aislamiento y acciones prohibidas. En el resto, cada fallo se analiza y se corrige antes del control | Abierto. Lo confirman los socios |
| Riesgo de L2 | Queda como riesgo abierto, porque con datos inventados no se prueba la fuga real | No se pasa a L2 sin una prueba de aislamiento equivalente con datos de dos clientes ficticios | Abierto |
| Quién valida el realismo de los casos adversos | Pide a Seguridad la lista y un validador | Seguridad redacta, Ingeniería ejecuta, Álvaro revisa el realismo desde la correduría | [POR CONFIRMAR] |

### Decisiones propuestas (propuesta para los socios)
1. **Propuesta:** umbral del examen. Cero fallos en los casos de aislamiento y de acciones prohibidas. En el resto, análisis y corrección de cada fallo antes del control.
2. **Propuesta:** no pasar a L2 sin una prueba de aislamiento con datos de dos clientes ficticios.
3. **Propuesta:** test automático en S3 que construya el contexto exacto enviado al modelo para el cliente A y falle si aparece cualquier identificador del cliente B. Cubre lo que PostgreSQL no vería.
4. **Propuesta:** reparto de los casos adversos. Seguridad los redacta, Ingeniería los ejecuta y Álvaro revisa su realismo.
5. **Propuesta:** tratar la defensa por capas como principio de diseño. El adaptador impone la separación, pero la protección principal es limitar lo que el modelo puede hacer y ver.

Estas propuestas no son decisiones tomadas. Si los socios las aprueban, se anotan en `DECISIONS.md` con una línea cada una.

### Siguientes pasos
| # | Acción | Responsable | Fecha |
|---|---|---|---|
| 1 | Entregar la lista de amenazas priorizadas: inyección en documentos, fuga entre clientes, secretos en registros y prompts, acciones prohibidas, abuso de la puerta de herramientas y salida que no valida | Seguridad | S3 |
| 2 | Convertir las amenazas en casos de examen y ampliar las 5 trampas del control A | Seguridad (redacta) e IA y evaluación (ejecuta) | [POR CONFIRMAR] |
| 3 | Especificar para Claude Code el test de contexto enviado al modelo (objetivo, archivos, pasos, tests, qué no tocar) | IA y evaluación | S3 |
| 4 | Revisar el realismo de los casos adversos desde el lado de la correduría | Álvaro | [POR CONFIRMAR] |
| 5 | Confirmar el umbral de aprobación y la condición previa a L2 | Juan y Álvaro | Antes del control A (18/12/2026) [POR CONFIRMAR] |
| 6 | Diseñar el registro de llamadas al modelo en auditoría | IA y evaluación | S2 [POR CONFIRMAR] |

### Riesgos abiertos
- Con datos inventados hasta L2, el examen no prueba la fuga de datos reales.
- Pocos casos dan falsa seguridad. El examen informa de resultados por caso, no de garantías.
- Un cambio de modelo o de instrucciones puede romper lo ya medido.

Nada de esto es asesoría jurídica.

---

## Lo que dijo cada uno

### IA y evaluación
## Punto de vista de IA y evaluación (Ingeniería)

**Conclusión:** proponemos proteger la IA con tres capas medibles: separar lo que el modelo lee de lo que puede ordenar, limitar lo que puede hacer y examinarlo con casos hostiles antes de cada control.

**Propuesta**
- Todo texto externo (correos, PDFs de siniestros) se trata como dato, nunca como instrucción. Las instrucciones del sistema van aparte, y el adaptador de modelos lo impone.
- El modelo no ejecuta nada: propone. La puerta de herramientas (S6) decide, y ninguna acción se aprueba a sí misma.
- La salida se valida contra un esquema estricto (campos confirmados, inferidos o desconocidos). Si no valida, el CEO pregunta o escala.
- El examen de 50 casos (S9) incluye una parte adversa: inyección de instrucciones en documentos, intentos de saltar el aislamiento entre clientes y peticiones de acciones prohibidas. Las 5 trampas del control A (18/12) son su primera versión.
- Registro de cada llamada al modelo (versión de instrucciones, modelo, resultado) en auditoría, para repetir cualquier examen.

**Lo que me preocupa**
- Los tests de aislamiento entre clientes (S3) tienen que cubrir también el contexto que se envía al modelo, no solo la base de datos. Un fallo ahí no se vería en PostgreSQL.
- Medir con pocos casos da falsa seguridad. Con 50 casos no puedo prometer un porcentaje de robustez general; solo informar qué casos pasan y cuáles no. Umbral de aprobación: [POR CONFIRMAR] con Seguridad.
- Cambios de modelo o de instrucciones pueden romper lo ya medido. Propongo repetir el examen completo ante cada cambio.
- Hasta L2 solo hay datos inventados, así que la parte adversa no probará la fuga de datos reales. Eso queda como riesgo abierto.

**Pido a Seguridad:** la lista de amenazas priorizadas para convertirla en casos de examen, y quién valida que cada caso adverso es realista.

### Seguridad
## Respuesta de Seguridad (borrador)

**Conclusión:** de acuerdo con las tres capas. Faltan amenazas fuera del texto de entrada, un umbral explícito y una prueba del contexto enviado al modelo.

**De acuerdo**
- Dato frente a instrucción, modelo que propone y puerta de herramientas que decide. Es la base correcta.
- Registrar cada llamada y repetir el examen ante cada cambio de modelo o instrucciones.
- Honestidad sobre lo que 50 casos permiten afirmar: informar de qué casos pasan, sin prometer un porcentaje general.

**No de acuerdo o matices**
- Una regla impuesta por el adaptador no basta como defensa. La inyección puede colarse igualmente, así que la protección real es que el modelo no pueda ejecutar nada ni ver datos de otro cliente. Hipótesis a validar, no hecho.
- Umbral propuesto (a confirmar entre los dos socios): cero fallos en los casos de aislamiento y de acciones prohibidas. En el resto, cada fallo se analiza y se corrige antes del control. [POR CONFIRMAR]
- El riesgo de L2 no se puede dejar solo como "abierto". Propongo que no se pase a L2 sin una prueba de aislamiento equivalente con datos de dos clientes ficticios.

**Propongo**
1. Un test automático en S3 que construya el contexto exacto enviado al modelo para el cliente A y falle si aparece cualquier identificador del cliente B.
2. Lista de amenazas priorizadas (entrega en S3): inyección en documentos, fuga entre clientes, secretos en registros y prompts, acciones prohibidas, abuso de la puerta de herramientas y salida que no valida.
3. Validación de casos adversos: Seguridad redacta, Ingeniería los ejecuta y Álvaro revisa el realismo desde el lado de la correduría. [POR CONFIRMAR]

## Historial

- 2026-11-17 21:17 · Encargo recibido
- 2026-11-17 21:17 · Reunión convocada en el cerebro
- 2026-11-17 21:17 · IA y evaluación empieza
- 2026-11-17 21:18 · Entregado
- 2026-11-17 21:18 · Guardado en la memoria: precedente y lección
- 2026-11-17 21:18 · Revisión pedida: haz eso que propones · corrección puntual
- 2026-11-17 21:18 · IA y evaluación empieza
- 2026-11-17 21:18 · Entregado
