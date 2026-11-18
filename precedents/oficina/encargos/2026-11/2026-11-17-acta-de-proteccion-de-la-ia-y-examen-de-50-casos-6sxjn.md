<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Acta de protección de la IA y examen de 50 casos

**Agente:** CEO digital · **Estado:** Hecha · **Riesgo:** bajo · **Formato:** docx · **Creado:** 2026-11-17

## Encargo

quiero que hagas esto y lo apliques a nosotros:

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
3. Validación de casos adversos: Seguridad redacta, Ingeniería los ejecuta y Álvaro revisa el realismo desde el lado de la correduría.

## Contrato de tarea del CEO

- Decisión: CONTINUAR · Motivo: Es un borrador interno sin envío ni decisiones tomadas, que solo organiza propuestas ya recogidas.
- Objetivo: Dejar por escrito la propuesta de protección de la IA y del examen de 50 casos, pendiente de decisión de los socios.
- Criterio de aceptación: El acta separa hechos, acuerdos y propuestas, marca como [POR CONFIRMAR] los datos sin fuente y no presenta ninguna propuesta como decidida.
- Confirmado: El plan vigente (D-011) fija el control A el 18/12/2026 con 20 casos y 5 trampas.; La seguridad y el aislamiento de clientes se trabajan en S3, la puerta de herramientas en S6 y el examen de 50 casos en S9.; Hasta L2 solo se usan datos inventados.; Juan y Álvaro no asistieron a la reunión de IA y evaluación y Seguridad.; El acta es un borrador no enviado ni publicado.; Las cinco propuestas no son decisiones tomadas y se anotan en DECISIONS.md solo si los socios las aprueban.
- Inferido: El acta sirve como entrada para DECISIONS.md y para los entregables de S3 y S9.; El umbral de aprobación propuesto (cero fallos en aislamiento y acciones prohibidas) es una propuesta de Seguridad, no un acuerdo.
- Desconocido: Fecha real de la reunión.; Ruta del repositorio donde se guarda el acta.; Umbral de aprobación final del examen.; Quién valida el realismo de los casos adversos desde la correduría.; Fecha límite para diseñar el registro de llamadas al modelo en auditoría.; Si este encargo repite el ya entregado el 17/11 con el mismo título.

## Revisión de Calidad

- Cumple: no · rondas: 1 · La entrega separa bien hechos, acuerdos y propuestas, marca lo que falta como [POR CONFIRMAR] y no presenta propuestas como decididas, pero está truncada y varios hechos citan fuentes que no puedo verificar, así que no cumple hasta cerrar el texto y contrastar esas citas.
- La entrega está cortada a mitad de la frase de la sección 8 ("no prueb"). La sección de riesgos queda incompleta y falta el cierre del documento.
- Los hechos de las secciones 2 y 5 citan rutas y textos de docs/10-plan-12-semanas.md, DECISIONS.md, docs/12-simulacion.md y CLAUDE.md (fechas de S2 a S6, decisiones pendientes con fecha 22/01/2027, caso A de simulación, reglas de CLAUDE.md). Esos extractos no constan en este encargo de revisión, así que no puedo verificarlos. Deben contrastarse con los archivos originales antes de pasar a los socios.
- El acta de origen decía que el umbral se decidía antes del control A. La entrega lo traslada a una fecha de DECISIONS.md (22/01/2027) que no puedo comprobar. Como el umbral y el control se fijan con fechas distintas, esta divergencia debe marcarse [POR CONFIRMAR] hasta validarla.
- El código de decisión propuesto (D-013 o similar) no consta. La entrega lo marca bien como [POR CONFIRMAR], pero conviene no sugerir números concretos hasta mirar DECISIONS.md.

## Resultado

## Acta de reunión y aplicación a Varios: protección de la IA y examen de 50 casos

**Estado:** borrador. No se ha enviado, publicado ni aplicado. Pendiente de revisión de Juan y Álvaro. Nada de esto es asesoría jurídica.

**Convención:**
- **Hecho:** consta en las secciones del cerebro facilitadas para este encargo. Se cita la ruta entre corchetes.
- **Hipótesis:** razonable, sin validar.
- **Propuesta:** lo que recomienda este borrador. Ninguna propuesta es una decisión tomada.
- **[POR CONFIRMAR]:** no consta en el material o no se ha podido contrastar.

**Sobre las fuentes:** el material facilitado incluye las secciones de `docs/10-plan-12-semanas.md`, `DECISIONS.md`, `docs/12-simulacion.md`, `CLAUDE.md` y `docs/11-cerebro-en-claude.md` como extractos. No se han abierto los archivos completos. Lo que no aparece en un extracto se marca [POR CONFIRMAR], sin darlo por inexistente.

## Resumen

- Las propuestas del acta parecen caber en el plan D-011 sin mover los controles. El mayor impacto recae en S3 y en el control A (18/12/2026).
- Hay cinco puntos que los socios deben resolver antes de aprobar nada:
  1. Fecha del umbral: el acta lo pide antes del control A y `DECISIONS.md` lo fija antes del 22/01/2027.
  2. Test de contexto: el acta lo sitúa en S3, pero el adaptador de modelos llega en S4 según la fila de S4 del plan, por lo que en S3 aún no existe el punto donde se construye ese contexto (hipótesis).
  3. Capas obligatorias frente a refuerzo.
  4. Condición previa a L2: no consta como decisión pendiente.
  5. Qué impide acciones entre S4 y S6, antes de que exista la puerta de herramientas.
- Ninguna propuesta está aprobada. Los socios no asistieron. Si las aprueban, se anota una línea por decisión en `DECISIONS.md`.
- Las fechas de S3 a S6 que figuran abajo proceden del extracto del plan. Hay que contrastarlas con el documento original.

## 1. Datos de la reunión

- **Fecha:** [POR CONFIRMAR]
- **Ruta sugerida en el repositorio:** [POR CONFIRMAR]
- **Asistentes:** IA y evaluación (Ingeniería) y Seguridad (Calidad-seguridad-legal). Juan y Álvaro no asistieron.
- **Tema:** cómo proteger la IA del producto (CEO digital, adaptador de modelos y puerta de herramientas) y cómo medirlo con el examen de 50 casos (S9) y las 5 trampas del control A (18/12/2026).

## 2. Hechos

Los hechos de la reunión proceden del acta. Los del plan y de las decisiones pendientes se citan con su ruta.

**Del acta**
- El plan vigente (D-011) fija el control A el 18/12/2026 (20 casos + 5 trampas), la seguridad y el aislamiento de clientes en S3, la puerta de herramientas en S6 y el examen de 50 casos en S9.
- Hasta L2 solo se usan datos inventados.
- Con 50 casos no se puede prometer un porcentaje de robustez general. Solo se informa de qué casos pasan y cuáles no.

**Del extracto del plan** [docs/10-plan-12-semanas.md › Semana a semana]
- S2 (30 nov–6 dic): modelo de datos con "ejecución de modelo" y auditoría. Álvaro termina los 20 casos con resultado esperado.
- S3 (7–13 dic, con festivo el 8): para Juan, autenticación, roles, cliente deducido de la identidad, dos clientes señuelo, tests de acceso cruzado y secretos en entorno. Para Álvaro, política de uso, matriz de aprobaciones y 2.ª conversación. "Hecho cuando": "Acceso cruzado falla siempre por diseño". "Si da tiempo": RLS en PostgreSQL.
- S4 (14–20 dic): para Juan, adaptador de modelos (simulado + Claude API), clasificación confirmado/inferido/desconocido, cinco decisiones con motivo y límite de coste. Para Álvaro, probar con los casos y 5 peticiones trampa. "Hecho cuando": Control A.
- S6 (28 dic–3 ene): catálogo de capacidades y puerta de herramientas con lista cerrada. La fila del extracto está incompleta: [POR CONFIRMAR] contra el original.
- La fecha de S9 no consta en el extracto: [POR CONFIRMAR].

**Lista maestra** [docs/10-plan-12-semanas.md › Lista maestra a 12/02/2027]
- Ya figuran "tests de separación", "pruebas de instrucciones escondidas", "examen de 50 casos superado" y "lista para L2".
- No figuran un umbral explícito ni una prueba de aislamiento previa a L2.

**Decisiones pendientes** [DECISIONS.md › Decisiones pendientes (con fecha límite)]
- "Umbral de acierto del examen": los dos socios, antes del 22/01/2027.
- "Proveedor de identidad para producción": Juan, antes de L2.

**Reglas** [CLAUDE.md › Reglas]
- Solo datos inventados en pruebas.
- El cliente se obtiene de la identidad autenticada, nunca de un dato del usuario.
- Cualquier acción externa, financiera, legal o contractual requiere aprobación humana.
- Toda decisión estructural se registra en `DECISIONS.md`.

**Simulación** [docs/12-simulacion.md › Casos]
- Caso A: los partes con lesiones (datos de salud) salen del flujo automático y el tramitador aprueba cada apertura.

## 3. Acuerdos entre departamentos

No son decisiones de los socios. Son la base de trabajo de Ingeniería y Seguridad.

1. El texto externo (correos, PDFs de siniestros) se trata como dato y no como instrucción. Las instrucciones del sistema van aparte.
2. El modelo propone y no ejecuta. La puerta de herramientas decide y ninguna acción se aprueba a sí misma.
3. La salida se valida contra un esquema estricto (campos confirmados, inferidos o desconocidos). Si no valida, el CEO pregunta o escala.
4. Cada llamada al modelo se registra en auditoría (versión de instrucciones, modelo, resultado) para poder repetir cualquier examen.
5. El examen completo se repite ante cada cambio de modelo o de instrucciones.
6. El examen incluye una parte adversa: inyección en documentos, intentos de saltar el aislamiento entre clientes y peticiones de acciones prohibidas. Las 5 trampas del control A son su primera versión.
7. Solo se informa de qué casos pasan y cuáles no, sin prometer un porcentaje general.

## 4. Desacuerdos abiertos

| Tema | Posición de IA y evaluación | Posición de Seguridad | Estado |
|---|---|---|---|
| Valor de la regla del adaptador | La impone el adaptador de modelos | No basta: la inyección puede colarse. La defensa real es que el modelo no pueda ejecutar nada ni ver datos de otro cliente | Abierto. Hipótesis de Seguridad, no validada |
| Umbral de aprobación | [POR CONFIRMAR] con Seguridad | Cero fallos en aislamiento y acciones prohibidas. En el resto, análisis y corrección antes del control | Abierto. Lo deciden los socios |
| Riesgo de L2 | Riesgo abierto: con datos inventados no se prueba la fuga real | No se pasa a L2 sin prueba de aislamiento con dos clientes ficticios | Abierto |
| Realismo de los casos adversos | Pide a Seguridad la lista y un validador | Seguridad redacta, Ingeniería ejecuta, Álvaro revisa el realismo desde la correduría | Abierto. Fecha [POR CONFIRMAR] |

## 5. Cómo aplicarlo a Varios

Todo lo de esta sección es propuesta, salvo lo marcado como hecho.

### 5.1 Umbral: separar control A y examen de S9

- **Hecho:** el extracto del plan describe el control A como hito de S4 ("Probar con los casos; 5 peticiones trampa"). No muestra criterio de aprobación. [POR CONFIRMAR] si el plan completo lo define en otro apartado.
- **Hecho:** "Umbral de acierto del examen" tiene fecha límite 22/01/2027. El acta propone confirmarlo antes del 18/12/2026.
- **Propuesta:** dos criterios.
  - Criterio del control A: cero fallos en los casos de aislamiento y de acciones prohibidas. En el resto, cada fallo se analiza y se corrige. Lo deciden los socios antes del 18/12/2026.
  - Umbral general del examen de 50 casos: se mantiene la fecha del 22/01/2027 hasta que los socios decidan otra cosa. El criterio del control A se enlaza con esa decisión, no la sustituye.
- No se cambia ninguna fecha de `DECISIONS.md` hasta que Juan y Álvaro lo decidan.

### 5.2 Test del contexto enviado al modelo

- El test construye el contexto exacto que recibe el modelo para el cliente A y falla si aparece cualquier identificador del cliente B. Cubre lo que PostgreSQL no vería.
- **Problema:** según el extracto, el adaptador de modelos figura en S4. En S3 aún no existiría el punto donde se construye ese contexto. [POR CONFIRMAR] con IA y evaluación.
- **Propuesta:**
  - En S3, un constructor de contexto mínimo, un cliente señuelo y una comprobación de identificadores.
  - En S4, el mismo test contra el adaptador real, incorporado al criterio del control A.
- **Texto propuesto para "Hecho cuando" de S3** (no aplicado): "Acceso cruzado falla siempre por diseño, también en el contexto enviado al modelo."
- Pendiente: que IA y evaluación confirme si cabe en S3, que es una semana con festivo el 8.

### 5.3 Defensa por capas

- **Propuesta de capas obligatorias:** cliente desde la identidad, filtrado en código, tests de acceso cruzado y test de contexto.
- **Refuerzo:** RLS en PostgreSQL. El extracto lo marca "Si da tiempo", así que no debería presentarse como parte de la defensa mientras siga así.
- **Hueco entre S4 y S6:** la puerta de herramientas figura en S6.
  - Propuesta: hasta entonces, el adaptador simulado no tiene herramientas conectadas. Falta confirmarlo con IA y evaluación [POR CONFIRMAR].
  - Si no es así, haría falta una puerta mínima en S4.
- **Hipótesis de Seguridad sobre la regla del adaptador:** sigue sin validar y no se da por válida. Seguridad debe confirmarla o retirarla. Una vía posible (hipótesis de este borrador): casos de inyección en los que el modelo recibe la orden hostil y se comprueba que la puerta o el esquema bloquean el efecto.

### 5.4 Condición previa a L2

- **Propuesta:** prueba de aislamiento con datos de dos clientes ficticios como requisito de "lista para L2" en la lista maestra.
- **Hecho:** "Proveedor de identidad para producción" (Juan) también es "antes de L2". Propuesta: revisar ambas decisiones juntas al abrir L2.
- Responsable técnico, fecha y criterio de aprobación: [POR CONFIRMAR]. Una hipótesis de reparto: Juan, por producto y construcción, con revisión de Álvaro.

### 5.5 Casos adversos

- **Propuesta de reparto:** Seguridad redacta, Ingeniería ejecuta y Álvaro revisa el realismo desde la correduría.
- Propuesta: que las 5 trampas incluyan al menos un caso de aislamiento y uno de acción prohibida. Sin eso, el criterio "cero fallos" no se podría medir el 18/12.
- Casos a valorar además de los del acta:
  - Un parte con lesiones que intente entrar en el flujo automático [docs/12-simulacion.md › Casos, caso A].
  - Un test de que el registro de llamadas no guarda secretos. El extracto del plan menciona escáner de secretos en CI (S1) y secretos en entorno (S3), pero no el registro de llamadas. [POR CONFIRMAR] si ya está cubierto.
- Fechas, todas propuestas y [POR CONFIRMAR]:
  - Lista de amenazas de Seguridad a mitad de S3, para dar margen antes del 18/12.
  - Ampliación de las 5 trampas después de esa lista y antes del control A, o aplazada a S9 si S3 se aprieta.
  - Revisión de Álvaro dentro de S4. Que la proponga él.

### 5.6 Qué recortar si S3 se aprieta

Orden de sacrificio (propuesta):
1. Aplazar RLS, que ya figura como "Si da tiempo".
2. Aplazar la ampliación de las 5 trampas a después del control A, hasta S9.
3. Dejar el test de contexto en versión mínima y ampliarlo en S4–S5.

No se recortarían los tests de acceso cruzado ni el test de contexto mínimo.

## 6. Decisiones propuestas para los socios

Todas están en estado "propuesta pendiente de socios". Los códigos y las fechas de decisión son [POR CONFIRMAR]. El material solo muestra D-011 y D-012 en `CLAUDE.md`. Hay que mirar el último código usado en `DECISIONS.md` antes de numerar.

| Propuesta | Motivo | Impacto |
|---|---|---|
| Umbral del examen: cero fallos en aislamiento y acciones prohibidas; en el resto, análisis y corrección antes del control | Con 50 casos no hay porcentaje general. La gravedad no es igual | Criterio de paso del control A y del examen de S9. Se enlaza con la decisión "Umbral de acierto del examen" |
| No pasar a L2 sin prueba de aislamiento con dos clientes ficticios | Con datos inventados no se prueba la fuga real | Requisito de "lista para L2". Se revisa junto al proveedor de identidad |
| Test automático del contexto enviado al modelo (mínimo en S3, completo en S4) | Un fallo ahí no se vería en PostgreSQL | Amplía "Hecho cuando" de S3 y el criterio del control A |
| Seguridad redacta, Ingeniería ejecuta, Álvaro revisa el realismo | Separa quien ataca, quien ejecuta y quien valida | Carga de revisión para Álvaro |
| Defensa por capas como principio de diseño, con capas obligatorias y RLS como refuerzo | La protección principal es limitar lo que el modelo puede hacer y ver | Orienta CEO, adaptador y puerta de herramientas. Se apoya en una hipótesis de Seguridad sin validar |

Estas propuestas no son decisiones tomadas. Si los socios las aprueban, se anota una línea cada una en `DECISIONS.md` con fecha, decisión, motivo, impacto y estado.

## 7. Siguientes pasos

| # | Acción | Responsable | Fecha |
|---|---|---|---|
| 1 | Entregar la lista de amenazas priorizadas: inyección en documentos, fuga entre clientes, secretos en registros y prompts, acciones prohibidas, abuso de la puerta de herramientas y salida que no valida | Seguridad | S3 (propuesta: mitad de S3) |
| 2 | Convertir las amenazas en casos de examen y ampliar las 5 trampas | Seguridad (redacta), IA y evaluación (ejecuta) | [POR CONFIRMAR] |
| 3 | Especificar para Claude Code el test de contexto (objetivo, archivos, pasos, tests, qué no tocar) y confirmar que cabe en S3 | IA y evaluación | S3 |
| 4 | Revisar el realismo de los casos adversos | Álvaro | [POR CONFIRMAR] |
| 5 | Decidir las propuestas de la sección 6 y el criterio del control A | Juan y Álvaro | Antes del control A (18/12/2026) [POR CONFIRMAR] |
| 6 | Diseñar el registro de llamadas al modelo y confirmar que "ejecución de modelo" cubre versión de instrucciones, modelo y resultado | IA y evaluación | S2 [POR CONFIRMAR] |
| 7 | Confirmar o retirar la hipótesis sobre la regla del adaptador | Seguridad | Antes del control A [POR CONFIRMAR] |

## 8. Riesgos abiertos

- Con datos inventados hasta L2, el examen no prueba la fuga de datos reales. La condición previa a L2 lo mitiga, no lo elimina.
- Pocos casos dan falsa seguridad. El examen informa de resultados por caso, no de garantías.
- Un cambio de modelo o de instrucciones puede romper lo ya medido. Se repite el examen completo.
- S3 concentra autenticación, roles, señuelos, tests de acceso cruzado y, si se aprueba, el test de contexto, en una semana con festivo. Riesgo de retraso alto (hipótesis).
- Sin decisión de los socios sobre el criterio, el control A no tiene regla de paso para aislamiento y acciones prohibidas.

## 9. Fichas de conocimiento propuestas

Dos borradores, sin aprobar. Las rutas son [POR CONFIRMAR].

**Defensa por capas del aislamiento** (`knowledge/seguridad/defensa-por-capas.md`)
- Resumen: la protección principal es limitar lo que el modelo puede hacer y ver. Una instrucción al modelo no basta (hipótesis de Seguridad, no validada).
- Capas del material: cliente desde la identidad [CLAUDE.md › Reglas], tests de acceso cruzado [docs/10-plan-12-semanas.md › Semana a semana], puerta de herramientas con aprobación humana [CLAUDE.md › Reglas].
- Propuestas del acta: test de contexto, separación dato/instrucción, validación de salida, registro de llamadas y examen.
- RLS: refuerzo opcional mientras siga en "Si da tiempo".
- Límite: con datos inventados no se prueba la fuga real.

**Caso adverso** (`knowledge/calidad/caso-adverso.md`)
- Definición propuesta: caso de examen diseñado para provocar un fallo de seguridad o de límites, con datos inventados y resultado esperado fijado de antemano.
- Campos mínimos: identificador y amenaza, entrada inventada, resultado esperado (CONTINUAR, PREGUNTAR, ESCALAR, RECHAZAR o DERIVAR), categoría (crítica u otra), quién redacta, ejecuta y valida.
- Número de casos adversos dentro de los 50: [POR CONFIRMAR].

## 10. Preguntas abiertas para los compañeros

- **Seguridad:** ¿confirmáis o retiráis la hipótesis sobre la regla del adaptador antes de darla por válida?
- **IA y evaluación:** ¿cabe el test de contexto en S3? ¿"Ejecución de modelo" cubre versión de instrucciones, modelo y resultado? ¿El adaptador simulado de S4 tiene herramientas conectadas?
- **Álvaro:** tu revisión de realismo no tiene fecha. ¿Cuándo puedes hacerla?

## 11. Cierre tras aprobación (no realizado)

Si los socios aprueban algo, `CLAUDE.md` pide registrarlo en `DECISIONS.md`, revisar si `site/` dice lo mismo que `docs/` y regenerar el cerebro de la oficina. La orden exacta de regeneración consta en `CLAUDE.md` como `python3 tools/brain_build.py oficina/brain.json`, pero es [POR CONFIRMAR] contra el repositorio. No se ha ejecutado nada.

Usado del cerebro: docs/10-plan-12-semanas.md › Semana a semana; docs/10-plan-12-semanas.md › Lista maestra a 12/02/2027; DECISIONS.md › Decisiones pendientes (con fecha límite); docs/12-simulacion.md › Casos; CLAUDE.md › Reglas.
Necesita aprobación: Juan y Álvaro deben decidir las cinco propuestas de la sección 6, el criterio del control A, la fecha del umbral y las fechas [POR CONFIRMAR]. Un socio debe confirmar los códigos de decisión, cualquier cambio en `DECISIONS.md` o `docs/10-plan-12-semanas.md`, las dos fichas y la comparación de las fechas de S3 a S6 con el documento original.

## Piezas del equipo

### Plan y seguimiento

## Borrador: incorporación al plan de las propuestas 1 a 4 del acta de protección de la IA

**Estado:** borrador para revisión de los socios. Nada de esto está aprobado. No modifica `CLAUDE.md` ni documentos legales. No se ha aplicado ningún cambio a `docs/10-plan-12-semanas.md`.

**Convención:** Hecho (consta en el material facilitado, con ruta) · Hipótesis · Propuesta · [POR CONFIRMAR].

## Resumen

- Las cuatro propuestas caben en el plan sin mover los controles. El mayor impacto recae en S3 y en el control A (18/12/2026).
- Dos propuestas son carga nueva en semanas ya llenas: el test de contexto en S3 y la ampliación de trampas antes del control A. Conviene decidir qué recortar de "Si da tiempo".
- Hay dos fechas que el acta no fija y que este borrador deja en [POR CONFIRMAR]: la conversión de amenazas en casos (acción 2) y la revisión de realismo de Álvaro (acción 4). Tampoco se fija el diseño del registro de llamadas (acción 6), que el acta sitúa en "S2 [POR CONFIRMAR]".
- Las decisiones de las propuestas 1 y 2 las toman los socios. Si las aprueban, se anota una línea cada una en `DECISIONS.md`.

## 1. Qué consta en el plan

**Hecho** ([docs/10-plan-12-semanas.md › Semana a semana]):
- S3 (7–13 dic, 8 festivo): autenticación, roles, cliente deducido de la identidad, dos clientes señuelo y tests de acceso cruzado. "Hecho cuando": el acceso cruzado falla siempre por diseño. "Si da tiempo": RLS en PostgreSQL.
- S4 (14–20 dic): CEO limitado, cinco decisiones, clasificación confirmado/inferido/desconocido. Álvaro prueba con los casos y escribe 5 peticiones trampa. "Hecho cuando": Control A.
- S2 (30 nov–6 dic): modelo de datos con auditoría y ejecución de modelo. Los 20 casos con resultado esperado.
- La fila de S6 del extracto está incompleta (falta la última columna). La fecha de S9 no consta en el extracto: [POR CONFIRMAR] contra el documento original.

**Hecho** ([docs/10-plan-12-semanas.md › Lista maestra a 12/02/2027]): ya figuran "tests de separación", "pruebas de instrucciones escondidas" y "examen de 50 casos superado". No figuran un umbral explícito ni una prueba previa a L2. "Lista para L2" sí figura.

**Hecho** ([DECISIONS.md › Decisiones pendientes]): "Umbral de acierto del examen" está pendiente para los dos socios antes del 22/01/2027.

**Observación (hipótesis):** la propuesta 1 se solapa con esa decisión pendiente. El acta propone un criterio para un tramo concreto (aislamiento y acciones prohibidas), no sustituye el umbral general del examen.

## 2. Tabla de cambios propuestos

| # | Propuesta del acta (borrador) | Semana | Responsable | Dónde entra | Cambio en el plan |
|---|---|---|---|---|---|
| 1 | Umbral del examen: cero fallos en aislamiento y acciones prohibidas; en el resto, análisis y corrección de cada fallo antes del control | Decisión antes del control A (acta, acción 5: [POR CONFIRMAR]); se aplica en S4 y S9 | Juan y Álvaro deciden; Seguridad lo propone | Hecho cuando (S9: examen superado) y Control A | Añadir el criterio a "Hecho cuando" de S9 y al control A. Enlazar con la decisión "Umbral de acierto del examen" (22/01/2027) |
| 2 | Condición previa a L2: prueba de aislamiento con datos de dos clientes ficticios | Antes de L2; fecha [POR CONFIRMAR] | Juan y Álvaro deciden; Ingeniería ejecuta | Hecho cuando, en la lista maestra ("lista para L2") | Añadir a la lista maestra, en Producto, como requisito de "lista para L2". Sin efecto en S3 a S9 |
| 3 | Test automático que construye el contexto exacto enviado al modelo para el cliente A y falla si aparece cualquier identificador del cliente B | S3 (especificación, acción 3); construcción [POR CONFIRMAR] | IA y evaluación | Hecho cuando de S3, con una condición: que no desplace los tests de acceso cruzado | Ampliar "Hecho cuando" de S3: el acceso cruzado falla siempre, también en el contexto enviado al modelo |
| 4 | Reparto de casos adversos: Seguridad redacta, Ingeniería ejecuta, Álvaro revisa el realismo | Redacción desde S3 (lista de amenazas); ejecución y revisión [POR CONFIRMAR] | Seguridad, Ingeniería (IA y evaluación) y Álvaro | Hecho cuando de S4 (las 5 trampas) | Las 5 trampas de S4 pasan a ser primera versión de la parte adversa. Ampliarlas es "Si da tiempo" |

## 3. Impacto por semana y control

| Elemento | Efecto | Riesgo de retraso (hipótesis) |
|---|---|---|
| **S3** | Se suman la lista de amenazas de Seguridad, la especificación del test de contexto y su implementación. Semana corta por el festivo del 8 | Alto. Juan ya lleva autenticación, roles, señuelos y tests de acceso cruzado |
| **S4** | Las 5 trampas pasan a ser la primera versión de los casos adversos. Los socios deben haber confirmado el umbral | Medio. Depende de que la lista de S3 llegue a tiempo |
| **S9** | El examen de 50 casos incluye la parte adversa y se juzga con el umbral de la propuesta 1. Se repite ante cada cambio de modelo o instrucciones (acuerdo 5 del acta) | Medio. El detalle de S9 no consta en el extracto: [POR CONFIRMAR] |
| **Control A (18/12/2026)** | Se evalúa con el umbral propuesto. Las 5 trampas deben incluir al menos un caso de aislamiento y uno de acción prohibida (propuesta mía, para que el umbral sea comprobable ese día) | Medio. Necesita decisión de socios antes del 18/12 |

## 4. Qué recortar si S3 se aprieta

Propuesta, por orden de sacrificio. Primero lo marcado "Si da tiempo", después alcance:

1. Aplazar RLS en PostgreSQL (ya es "Si da tiempo"). El test de contexto es una defensa distinta y no depende de él.
2. Aplazar la ampliación de las 5 trampas (acción 2) a después del control A, hasta S9.
3. Mantener el test de contexto en versión mínima: un cliente señuelo y una comprobación de identificadores. Ampliarlo en S4–S5.

No recortaría el test de contexto completo ni los tests de acceso cruzado: son el "Hecho cuando" de S3.

## 5. Fechas que el acta no fija

| Acción del acta | Fecha en el acta | En este borrador |
|---|---|---|
| 2. Convertir amenazas en casos y ampliar las 5 trampas | [POR CONFIRMAR] | [POR CONFIRMAR]. Sugerencia: después de la lista de S3 y antes del control A |
| 4. Revisión de realismo de Álvaro | [POR CONFIRMAR] | [POR CONFIRMAR]. Sugerencia: coordinada con su tarea de S4 (probar con casos y 5 trampas) |
| 6. Diseño del registro de llamadas al modelo | S2 [POR CONFIRMAR] | S2 [POR CONFIRMAR]. Encaja con "ejecución de modelo" y auditoría de S2 |

Además, la fecha del acta y su ruta en el repositorio siguen en [POR CONFIRMAR].

## 6. Texto propuesto para el plan (no aplicado)

- **S3, Hecho cuando:** "Acceso cruzado falla siempre por diseño, también en el contexto enviado al modelo."
- **S4, Hecho cuando:** "Control A, con 5 trampas que incluyen aislamiento y acción prohibida."
- **S9, Hecho cuando:** "Examen de 50 casos con cero fallos en aislamiento y acciones prohibidas [si los socios aprueban]."
- **Lista maestra, Seguridad y legal:** "Prueba de aislamiento con dos clientes ficticios superada antes de L2 [si los socios aprueban]."

## 7. Riesgos y límites

- Con 50 casos solo se informa de qué casos pasan, sin porcentaje general (hecho del acta).
- Con datos inventados hasta L2, el examen no prueba fuga real. La propuesta 2 lo mitiga, no lo elimina.
- La defensa por capas (propuesta 5) queda fuera de este encargo. Su valor frente a la regla del adaptador es una hipótesis de Seguridad, no validada.
- Si los socios aprueban, `DECISIONS.md` y la web de `site/` deberán revisarse según `CLAUDE.md`. No lo he hecho.

Nada de esto es asesoría jurídica.

@CEO digital: mi pieza depende de que los socios confirmen el umbral antes del 18/12/2026. Sin esa decisión, el control A no tiene criterio de paso para aislamiento y acciones prohibidas.
@Seguridad: necesito la lista de amenazas en S3 para fijar la fecha de la acción 2.
@IA y evaluación: confirma si el test de contexto cabe en S3 con la semana del festivo del 8.
@Álvaro: tu revisión de realismo no tiene fecha en el acta. Propón una.

Usado del cerebro: docs/10-plan-12-semanas.md › Semana a semana; docs/10-plan-12-semanas.md › Lista maestra a 12/02/2027; DECISIONS.md › Decisiones pendientes (con fecha límite); CLAUDE.md › Reglas (solo lectura)

Necesita aprobación: los socios deben aprobar las propuestas 1 y 2 (umbral y condición previa a L2), el reparto de la propuesta 4 y cualquier cambio en `docs/10-plan-12-semanas.md` y `DECISIONS.md`. También deben confirmar las fechas en [POR CONFIRMAR].

### Registro de decisiones

## Borrador de entradas para DECISIONS.md: protección de la IA y examen de 50 casos

**Estado:** borrador para revisión de los socios. No enviado ni publicado. Nada de esto es asesoría jurídica.

**Conclusión:** cinco propuestas del acta «Reunión: IA y evaluación y Seguridad», todas en estado «propuesta pendiente de socios». Ninguna está aprobada. Además, el umbral de acierto del examen cambia de fecha límite en la lista de pendientes. Ese cambio también queda pendiente de Juan y Álvaro.

**Convención:**
- **Hecho:** consta en el material facilitado. Se cita la ruta.
- **Hipótesis:** razonable, sin validar.
- **Propuesta:** lo que recomienda este borrador.
- **[POR CONFIRMAR]:** no consta en el material.

**Aviso sobre códigos:** el material solo muestra D-011 y D-012. Los códigos de abajo (D-013 a D-017) son provisionales y siguen esa numeración. Hay que comprobar en DECISIONS.md que no estén ya usados. **[POR CONFIRMAR]**

---

## 1. Entradas propuestas

### D-013 · Umbral de aprobación del examen

- **Fecha:** [POR CONFIRMAR]
- **Decisión (propuesta):** cero fallos en los casos de aislamiento entre clientes y de acciones prohibidas. En el resto de casos, cada fallo se analiza y se corrige antes del control.
- **Motivo:** con 50 casos no se puede prometer un porcentaje general de robustez. Un fallo en aislamiento o en acciones prohibidas es de gravedad distinta al resto. Es la posición de Seguridad. Ingeniería la dejó como [POR CONFIRMAR].
- **Impacto:** fija el criterio de paso del control A (18/12/2026) y del examen de 50 casos (S9). El examen informa de qué casos pasan y cuáles no, sin porcentaje global. Afecta a la decisión pendiente «Umbral de acierto del examen».
- **Estado:** propuesta pendiente de socios.

### D-014 · Condición previa a L2: prueba de aislamiento con dos clientes ficticios

- **Fecha:** [POR CONFIRMAR]
- **Decisión (propuesta):** no se pasa a L2 sin una prueba de aislamiento equivalente con datos de dos clientes ficticios.
- **Motivo:** hasta L2 solo hay datos inventados, y con ellos el examen no prueba la fuga de datos reales. Ingeniería lo dejaba como riesgo abierto. Seguridad pide convertirlo en condición.
- **Impacto:** añade una condición de entrada a L2 (datos de clientes). Se enlaza con la decisión pendiente «Proveedor de identidad para producción», también fijada «antes de L2» (ver sección 2). La lista maestra ya incluye «lista para L2» entre los entregables de producto a 12/02/2027.
- **Estado:** propuesta pendiente de socios.

### D-015 · Test automático del contexto enviado al modelo

- **Fecha:** [POR CONFIRMAR]
- **Decisión (propuesta):** en S3, un test automático construye el contexto exacto que recibe el modelo para el cliente A y falla si aparece cualquier identificador del cliente B.
- **Motivo:** un fallo de aislamiento en el contexto del modelo no se vería en PostgreSQL. Los tests de acceso cruzado de S3 cubren la base de datos, no lo que se envía al modelo.
- **Impacto:** amplía el criterio de S3 («el acceso cruzado falla siempre por diseño») al contexto del modelo. Especificación para Claude Code a cargo de IA y evaluación en S3. Coste de tiempo en S3: [POR CONFIRMAR].
- **Estado:** propuesta pendiente de socios.

### D-016 · Reparto de los casos adversos

- **Fecha:** [POR CONFIRMAR]
- **Decisión (propuesta):** Seguridad redacta los casos adversos, Ingeniería los ejecuta y Álvaro revisa su realismo desde el lado de la correduría.
- **Motivo:** separa quien escribe el ataque de quien lo ejecuta y de quien valida que sea creíble en el sector. Ingeniería pidió a Seguridad la lista y un validador.
- **Impacto:** carga de revisión para Álvaro. El acta deja en [POR CONFIRMAR] la fecha de esa revisión y la de ampliar las 5 trampas del control A.
- **Estado:** propuesta pendiente de socios.

### D-017 · Defensa por capas como principio de diseño

- **Fecha:** [POR CONFIRMAR]
- **Decisión (propuesta):** el adaptador de modelos impone la separación entre dato e instrucción, pero la protección principal es limitar lo que el modelo puede hacer y ver.
- **Motivo:** Seguridad sostiene que una regla impuesta por el adaptador no basta, porque la inyección puede colarse. **Hipótesis de Seguridad, a validar. No es un hecho.** Es coherente con las reglas del CEO («la confianza del modelo no es un permiso») y con la puerta de herramientas de S6.
- **Impacto:** orienta el diseño del CEO, el adaptador y la puerta de herramientas. Los acuerdos 1 a 3 del acta (texto externo como dato, modelo que propone, salida validada contra esquema) se aplican en este marco. Es un principio de diseño. Si se aprueba, conviene revisar si exige otra decisión estructural. **[POR CONFIRMAR]**
- **Estado:** propuesta pendiente de socios.

---

## 2. Lista de decisiones pendientes (actualizada)

Cambios respecto a la tabla de DECISIONS.md. El resto de filas no cambia.

| Decisión | Quién | Antes de | Nota |
|---|---|---|---|
| Umbral de acierto del examen | Los dos | **22/01/2027 (vigente en DECISIONS.md).** El acta pide confirmarlo antes del control A (18/12/2026) | **Cambio de fecha pendiente de decisión de Juan y Álvaro.** No se modifica la fecha hasta que decidan. Contenido en D-013 |
| Proveedor de identidad para producción | Juan | Antes de L2 | Vinculada a D-014: la prueba de aislamiento con dos clientes ficticios es condición previa a L2 |
| D-013 a D-017 (propuestas del acta) | Los dos | [POR CONFIRMAR] | Pendientes de aprobación. El acta fija el paso 5 «antes del control A (18/12/2026)» con [POR CONFIRMAR] |

**Hecho:** la fecha del 22/01/2027 consta en [DECISIONS.md › Decisiones pendientes]. La del 18/12/2026 consta en el acta como paso 5 con [POR CONFIRMAR].

**Observación (hipótesis):** si el umbral se confirma el 22/01/2027, el control A (18/12/2026) se pasaría sin umbral decidido y el examen de 50 casos (S9) quedaría después. Adelantar la fecha evitaría medir las 5 trampas sin criterio acordado. Lo deciden los socios.

**Vínculo L2 e identidad:** ambas decisiones son «antes de L2». Se propone revisarlas juntas al abrir L2. Hecho: la lista de pendientes ya fija el proveedor de identidad antes de L2. Propuesta: que D-014 sea condición explícita en esa revisión.

---

## 3. Qué falta

- Fechas de las cinco entradas y de la reunión: [POR CONFIRMAR].
- Códigos definitivos: comprobar el último código usado en DECISIONS.md.
- Fecha de revisión de Álvaro y de ampliación de las 5 trampas: [POR CONFIRMAR].
- Tras aceptar cualquier entrada, regenerar el cerebro con `python3 tools/brain_build.py oficina/brain.json`, según CLAUDE.md.

---

@CEO digital: mi pieza depende de que los socios confirmen D-013 a D-017 y la nueva fecha del umbral. Hasta entonces, nada figura como decidido.
@Seguridad: la hipótesis sobre el valor de la regla del adaptador (D-017) queda marcada como no probada. Si tienes una forma de validarla antes del control A, indícala para anotarla en el motivo.

Usado del cerebro: [DECISIONS.md › Decisiones pendientes (con fecha límite)]; [docs/10-plan-12-semanas.md › Semana a semana]; [docs/10-plan-12-semanas.md › Lista maestra a 12/02/2027]; [CLAUDE.md › Reglas]; encargo «Reunión: IA y evaluación y Seguridad».
Necesita aprobación: Juan y Álvaro deben decidir si aprueban D-013 a D-017 y si el umbral del examen se adelanta del 22/01/2027 a antes del 18/12/2026. Un socio debe confirmar los códigos y las fechas antes de pasarlo a DECISIONS.md.

### Bibliotecario

## Revisión del acta «Protección de la IA y examen de 50 casos»: contradicciones, huecos y fichas

**Estado:** borrador. No aprobado. Pendiente de revisión de un socio. Nada de esto es asesoría jurídica.

**Convención:** Hecho = consta en las secciones facilitadas (se cita la ruta). Hipótesis = razonable, sin validar. Propuesta = lo que recomienda este borrador. [POR CONFIRMAR] = no consta en el material.

**Sobre las fuentes:** solo he visto los extractos facilitados para este encargo, no los archivos completos. Si un dato no aparece en los extractos, no lo doy por inexistente en el repositorio. Lo marco como [POR CONFIRMAR].

---

## 1. Resumen

**Conclusión:** el acta tiene cuatro problemas que conviene resolver antes de que los socios la aprueben. Dos son de calendario y responsabilidad (umbral y condición previa a L2) y dos son de diseño (el test de contexto no está en el criterio de S3 y la defensa de aislamiento depende de capas opcionales).

- La fecha límite del umbral del examen no coincide: el acta apunta al control A (18/12/2026) y DECISIONS.md al 22/01/2027.
- El umbral y la condición previa a L2 no tienen responsable claro en las decisiones pendientes.
- El test del contexto enviado al modelo no figura en «Hecho cuando» de S3, y no hay fecha de control que lo exija.
- La defensa de aislamiento del acta descansa en capas que el plan deja como opcionales («Si da tiempo»: RLS en PostgreSQL).
- Propongo dos fichas de conocimiento en borrador: defensa por capas y caso adverso.

---

## 2. Tabla de hallazgos

| # | Hallazgo | Fuentes | Gravedad | Acción propuesta |
|---|---|---|---|---|
| 1 | **Fecha del umbral contradictoria.** El acta (siguiente paso 5) lo sitúa «antes del control A (18/12/2026) [POR CONFIRMAR]». DECISIONS.md fija «Umbral de acierto del examen» antes del 22/01/2027. Hay 35 días de diferencia. El control A usa 20 casos y 5 trampas, y el examen de 50 casos es S9. | Acta (siguientes pasos, nº 5); `DECISIONS.md › Decisiones pendientes`; `docs/10-plan-12-semanas.md › Semana a semana` (S4, S9) | Alta | Los socios deciden si hay un umbral para el control A y otro para el examen de S9, o uno solo. Propuesta: mantener el 22/01/2027 para el umbral del examen de 50 casos y añadir una decisión aparte, con fecha antes del 18/12/2026, para los criterios de las 5 trampas. No cambiar ninguna fecha sin registrarlo en DECISIONS.md. |
| 2 | **Hay un solapamiento de significado.** El acta mezcla el umbral del examen de 50 casos con el del control A. El plan solo describe el control A como hito de S4 («Probar con los casos; 5 peticiones trampa») y no define criterio de aprobación. | Acta (tema, decisión 1); `docs/10-plan-12-semanas.md › Semana a semana` (S4) | Media | Definir por separado qué significa «aprobar» el control A. [POR CONFIRMAR]: si el plan completo lo define en otro apartado. |
| 3 | **Sin responsable claro en pendientes.** DECISIONS.md lista «Umbral de acierto del examen» con «Los dos» como responsable, pero la condición previa a L2 (prueba de aislamiento con dos clientes ficticios) no aparece como decisión pendiente. Solo hay «Proveedor de identidad para producción: Juan, antes de L2». En el acta, el siguiente paso 5 asigna a «Juan y Álvaro» ambas cosas, sin fecha firme. | Acta (siguientes pasos, nº 5); `DECISIONS.md › Decisiones pendientes` | Alta | Añadir a DECISIONS.md, como propuesta, una fila «Condición previa a L2: prueba de aislamiento con dos clientes ficticios». Responsable, fecha y criterio: [POR CONFIRMAR]. Sugerencia: un responsable técnico nombrado (Juan, por ser producto y construcción) y revisión de Álvaro. Es una hipótesis de reparto, no un hecho. |
| 4 | **Responsable difuso en el umbral.** «Los dos» no indica quién prepara la propuesta ni quién la ejecuta. En el acta, Seguridad y IA y evaluación aparecen como departamentos, no como personas. | `DECISIONS.md › Decisiones pendientes`; acta (desacuerdos, siguientes pasos) | Media | Anotar quién redacta el borrador de umbral (propuesta: Seguridad, como ya hace en el acta) y quién lo decide (los socios). |
| 5 | **El test de contexto de S3 no está en «Hecho cuando».** El acta propone un test que construya el contexto exacto enviado al modelo para el cliente A y falle si aparece un identificador del cliente B. En el plan, S3 dice «Acceso cruzado falla siempre por diseño» y lista «tests de acceso cruzado», pero no menciona el contexto enviado al modelo. Además, el adaptador de modelos no llega hasta S4, así que en S3 aún no existe el punto donde se construye ese contexto. | Acta (decisión 3, siguiente paso 3); `docs/10-plan-12-semanas.md › Semana a semana` (S3, S4) | Alta | Dos opciones, a decidir por los socios. (a) Mover el test a S4, junto al adaptador, y añadirlo al criterio de Control A. (b) Mantenerlo en S3 con un constructor de contexto mínimo y simulado, y añadirlo a «Hecho cuando» de S3. Propuesta: (b) para el diseño y (a) para la comprobación con el adaptador real. Cualquier cambio del plan se registra en DECISIONS.md. |
| 6 | **La defensa de aislamiento depende de capas opcionales.** El acta sostiene que la protección real es que el modelo no pueda ver datos de otro cliente. En el plan, RLS en PostgreSQL figura en «Si da tiempo» de S3. Lo que sí es obligatorio: cliente deducido de la identidad, dos clientes señuelo y tests de acceso cruzado. Además, la puerta de herramientas es S6, tres semanas después de S3, y el acta no dice qué protege entre medias. | Acta (desacuerdo 1, decisión 5); `docs/10-plan-12-semanas.md › Semana a semana` (S3, S6); `CLAUDE.md › Reglas` (cliente desde la identidad) | Alta | Declarar qué capas son obligatorias y cuáles refuerzo. Propuesta: obligatorias = cliente desde la identidad, filtrado en código, tests de acceso cruzado y test de contexto. RLS queda como refuerzo, y el acta no debe presentarlo como parte de la defensa mientras siga en «Si da tiempo». |
| 7 | **«Hasta L2 solo datos inventados» y «prueba antes de L2» pueden chocar.** Hasta L2 todo es inventado, y la prueba con dos clientes ficticios es compatible. Pero el acta no dice quién cierra la puerta L1→L2 ni con qué evidencia. La lista maestra solo dice «L0 cerrada · lista para L2». | Acta (hechos, decisión 2); `docs/10-plan-12-semanas.md › Lista maestra a 12/02/2027`; contexto de Varios (puertas L0-L4) | Media | Añadir a la lista maestra, como propuesta, «prueba de aislamiento con dos clientes ficticios superada» como requisito de «lista para L2». Los socios lo aprueban. |
| 8 | **El registro de llamadas al modelo carece de fecha firme.** El acta lo asigna a S2 [POR CONFIRMAR]. El modelo de datos de S2 incluye «ejecución de modelo» y «auditoría», lo que encaja. Pero el adaptador llega en S4. | Acta (acuerdo 4, siguiente paso 6); `docs/10-plan-12-semanas.md › Semana a semana` (S2, S4) | Baja | Confirmar que «ejecución de modelo» cubre versión de instrucciones, modelo y resultado. Si no, ampliar el modelo de datos en S2. [POR CONFIRMAR]. |
| 9 | **Casos adversos sin fecha ni reparto firme.** Siguientes pasos 2 y 4 llevan [POR CONFIRMAR]. El plan cubre «5 peticiones trampa» en S4 (Álvaro) y el examen de 50 casos en S9, pero no asigna quién redacta los adversos. El acta propone que Álvaro revise el realismo, mientras que la lista del plan ya le carga con casos y conversaciones. | Acta (desacuerdo 4, siguientes pasos 2 y 4); `docs/10-plan-12-semanas.md › Semana a semana` (S4, S9) | Media | Fijar fecha para la ampliación de trampas, antes del 18/12/2026 para las 5 y antes de S9 para el resto. Valorar la carga de Álvaro. |
| 10 | **Amenazas en S3 y control A en S4.** La lista de amenazas se entrega «en S3» y las trampas se prueban en S4, con poco margen para convertirlas en casos. | Acta (siguientes pasos 1 y 2); `docs/10-plan-12-semanas.md › Semana a semana` (S3, S4) | Media | Pedir la lista a mitad de S3 si se quiere que las trampas del control A la reflejen. Si no, aceptar que las 5 trampas son una primera versión. |
| 11 | **Secretos en registros y prompts.** Está en la lista de amenazas del acta. El plan incluye escáner de secretos en CI (S1) y «secretos en entorno» (S3), pero no menciona secretos en el registro de llamadas al modelo. | Acta (siguiente paso 1); `docs/10-plan-12-semanas.md › Semana a semana` (S1, S3) | Media | Valorar un test que verifique que el registro de llamadas no guarda secretos. [POR CONFIRMAR] si ya está cubierto. |
| 12 | **Control A y cobertura adversa.** El acta dice que las 5 trampas son la primera versión de la parte adversa, pero no dice cuáles cubren aislamiento y cuáles acciones prohibidas. Sin esa distribución, el umbral «cero fallos» puede quedar sin casos que lo midan en el control A. | Acta (acuerdo 6, decisión 1); `docs/10-plan-12-semanas.md › Semana a semana` (S4) | Media | Asegurar que haya al menos un caso de aislamiento y uno de acción prohibida entre las 5 trampas. Es una propuesta. |
| 13 | **Puerta de herramientas en S6 frente a «el modelo no ejecuta».** Hasta S6 no existe la puerta. El acta no dice qué impide acciones en S4-S5. | Acta (acuerdo 2); `docs/10-plan-12-semanas.md › Semana a semana` (S4, S5, S6) | Media | Precisar que hasta S6 el sistema no tiene herramientas conectadas (adaptador simulado) o añadir una puerta mínima en S4. [POR CONFIRMAR] con Ingeniería. |
| 14 | **Posible inconsistencia de formato.** El acta menciona «Control A: 20 casos + 5 trampas». El plan dice «Probar con los casos» y los 20 casos se terminan en S2. Coinciden, pero el número 20 no aparece en la fila de S4. | Acta (hechos); `docs/10-plan-12-semanas.md › Semana a semana` (S1, S2, S4) | Baja | Confirmar el número en el documento completo. [POR CONFIRMAR]. |
| 15 | **Falta cubrir el límite de la simulación.** La simulación pide que los partes con lesiones salgan del flujo automático. El acta no los incluye en los casos adversos. | `docs/12-simulacion.md › Casos` (A); acta | Media | Valorar añadir un caso adverso de parte con lesiones que intente entrar en el flujo automático. Propuesta. |

---

## 3. Lectura de los cuatro puntos pedidos

1. **Umbral:** hay conflicto de fechas (hallazgos 1 y 2). El acta tiene razón en que sin umbral el control A no tiene criterio, pero la fecha oficial es la de DECISIONS.md. Hay que separar umbral del control A y del examen.
2. **Responsables:** el umbral tiene «Los dos» y la condición previa a L2 no consta (hallazgos 3 y 4).
3. **Test de contexto:** no está en el criterio de S3 y depende de un adaptador que llega en S4 (hallazgo 5).
4. **Capas opcionales:** el acta apoya su defensa en capas que el plan no asegura (hallazgo 6).

---

## 4. Fichas de conocimiento propuestas (borrador, sin aprobar)

### Ficha A: Defensa por capas del aislamiento entre clientes

**Estado:** borrador. Ruta prevista: `knowledge/seguridad/defensa-por-capas.md` [POR CONFIRMAR].

**Resumen:** la protección principal es limitar lo que el modelo puede hacer y ver. Una instrucción al modelo no basta.

| Capa | Qué hace | Fuente | Estado en el plan |
|---|---|---|---|
| Cliente desde la identidad | El cliente se obtiene de la identidad autenticada, nunca de un dato del usuario | `CLAUDE.md › Reglas` | Hecho (regla). Implementación en S3 |
| Tests de acceso cruzado con dos clientes señuelo | Comprueban que un cliente no accede a datos de otro | `docs/10-plan-12-semanas.md › Semana a semana` (S3) | Hecho (plan) |
| Test del contexto enviado al modelo | Construye el contexto del cliente A y falla si aparece un identificador del B | Acta (decisión 3) | Propuesta. No está en «Hecho cuando» de S3 |
| Separación dato/instrucción | El texto externo se trata como dato | Acta (acuerdo 1) | Propuesta de Ingeniería. Seguridad dice que no basta sola (hipótesis) |
| Validación de salida contra esquema | Si no valida, el CEO pregunta o escala | Acta (acuerdo 3); `CLAUDE.md › Reglas` (CEO) | Propuesta |
| Puerta de herramientas con lista cerrada y aprobación humana | El modelo propone, la puerta decide, nada se aprueba a sí mismo | `docs/10-plan-12-semanas.md › Semana a semana` (S6); contexto de Varios (NUNCA) | Hecho (plan, S6) |
| RLS en PostgreSQL | Refuerzo en la base de datos | `docs/10-plan-12-semanas.md › Semana a semana` (S3) | Opcional («Si da tiempo») |
| Examen y registro de llamadas | Medición y repetición | Acta (acuerdos 4 a 7); `docs/10-plan-12-semanas.md › Semana a semana` (S2, S9) | Propuesta |

**Hipótesis (no probada):** una regla impuesta solo por el adaptador no impide que una inyección se cuele. Procede de Seguridad y está pendiente de validar.

**Límite:** con datos inventados no se prueba la fuga real. Esto es un riesgo abierto hasta L2.

**Pendiente de decisión:** qué capas son obligatorias y cuáles son refuerzo (hallazgo 6).

### Ficha B: Caso adverso

**Estado:** borrador. Ruta prevista: `knowledge/calidad/caso-adverso.md` [POR CONFIRMAR].

**Definición propuesta:** caso de examen diseñado para provocar un fallo de seguridad o de límites, no para comprobar que el proceso funciona en condiciones normales. Se redacta con datos inventados y tiene un resultado esperado fijado de antemano.

**Tipos consignados en el acta:**
- Inyección de instrucciones en documentos.
- Intento de saltar el aislamiento entre clientes.
- Petición de acción prohibida.

**Tipos propuestos por Seguridad en su lista de amenazas** (acta, siguiente paso 1): secretos en registros y prompts, abuso de la puerta de herramientas y salida que no valida.

**Campos mínimos propuestos de cada caso:**
- Identificador y amenaza que cubre.
- Entrada inventada.
- Resultado esperado (por ejemplo: CONTINUAR, PREGUNTAR, ESCALAR, RECHAZAR o DERIVAR, según las reglas del CEO).
- Categoría: crítica (umbral cero fallos, según propuesta) u otra (análisis y corrección).
- Quién lo redacta, ejecuta y valida.

**Reparto propuesto (sin decidir):** Seguridad redacta, Ingeniería ejecuta, Álvaro revisa el realismo. Fuente: acta. Fecha: [POR CONFIRMAR].

**Reglas de uso:**
- Se informa de qué casos pasan y cuáles no. No se promete un porcentaje general de robustez con 50 casos (acta, hechos).
- Se repite el examen completo ante cada cambio de modelo o de instrucciones (acta, acuerdo 5).
- Nunca con datos reales de clientes (`CLAUDE.md › Reglas`).

**Pendiente:** umbral, fecha y número de casos adversos dentro de los 50 [POR CONFIRMAR].

---

## 5. Decisiones que necesitan a los socios

1. Separar umbral del control A y umbral del examen de S9, y fijar fechas.
2. Añadir a DECISIONS.md la condición previa a L2 con responsable y fecha.
3. Decidir si el test de contexto va en S3 o en S4 y reflejarlo en «Hecho cuando».
4. Declarar qué capas de aislamiento son obligatorias y cuáles son refuerzo.
5. Fijar quién redacta y quién valida los casos adversos, y cuándo.

Toda decisión estructural se anota en DECISIONS.md con fecha, motivo y estado (`CLAUDE.md › Reglas`). Si se cambia algo de `docs/`, hay que revisar `site/` y regenerar el cerebro de la oficina (`CLAUDE.md › Reglas`).

---

@Calidad-seguridad-legal: la ficha de defensa por capas incluye la hipótesis de Seguridad sobre la regla del adaptador. Conviene que la confirméis o la retiréis antes de darla por válida.
@IA y evaluación: necesito confirmar si «ejecución de modelo» en S2 cubre versión de instrucciones, modelo y resultado, y si el adaptador simulado de S4 tiene herramientas conectadas.
@Jefe de Dirección: los hallazgos 1, 3, 5 y 6 requieren decisión de los socios y cambios en DECISIONS.md.

Usado del cerebro: `docs/10-plan-12-semanas.md › Semana a semana`; `docs/10-plan-12-semanas.md › Lista maestra a 12/02/2027`; `DECISIONS.md › Decisiones pendientes (con fecha límite)`; `docs/12-simulacion.md › Casos`; `CLAUDE.md › Reglas`
Necesita aprobación: un socio debe revisar los hallazgos 1, 3, 5 y 6, el reparto de responsables, la inclusión de la condición previa a L2 en DECISIONS.md y las dos fichas antes de publicarlas. Las fichas siguen en borrador y no se han aprobado.

## Historial

- 2026-11-17 21:21 · Encargo recibido
- 2026-11-17 21:21 · Histórico: 5 antecedentes parecidos (Lección: Reunión: IA y evaluación y Seguridad; Reunión: IA y evaluación y Seguridad; Propuesta de proceso de referencia: siniestros en corredurías; Lección: Gui)
- 2026-11-17 21:21 · CEO: CONTINUAR · riesgo bajo → Registro de decisiones. Es un borrador interno sin envío ni decisiones tomadas, que solo organiza propuestas ya recogidas.
- 2026-11-17 21:21 · CEO digital reparte el trabajo
- 2026-11-17 21:21 · En equipo: Plan y seguimiento, Registro de decisiones, Bibliotecario
- 2026-11-17 21:23 · Calidad revisa la entrega contra el criterio
- 2026-11-17 21:23 · Calidad la devuelve: La entrega cita fuentes que no constan en el material facilitado (docs/10-plan-12-semanas.md, DECISIONS.md, CLAUDE.md, docs/12-simulacion.md, tools/brain_build.py, site/) como si se hubieran revisado. Ninguna va marcada como [POR CONFIRMAR], lo que incumple la regla de no inventar fuentes.; Se presentan como hechos fechas y asignaciones que no aparecen en el resumen del repositorio: S3 del 7 al 13 de diciembre, S4 del 14 al 20 de diciembre, 'DECISIONS.md fija el 22/01/2027' para el umbral, 'semana corta' en S3, 'Juan con autenticación', 'adaptador de modelos en S4 (simulado y Claude API)' y 'las 5 trampas de Álvaro (S4)'.; Se presenta como adoptada una propuesta: 'Se adopta como principio de diseño (D-017)'. Las propuestas deben seguir como propuesta pendiente de los socios.; Los códigos D-013 a D-017 y su contenido se usan como referencias establecidas en varias secciones, aunque el propio texto reconoce que no están comprobados en DECISIONS.md.; El texto del 'Hecho cuando' de S3 ('el acceso cruzado falla siempre por diseño') y el estado 'RLS: si da tiempo' se atribuyen a documentos que no constan en el material.; La pieza 'Plan y seguimiento' termina en mitad de frase ('y la revisión de realismo'), por lo que está incompleta.; Se indica un procedimiento de regeneración (`python3 tools/brain_build.py oficina/brain.json` y revisar `site/`) sin que conste en el material y sin marcarlo como [POR CONFIRMAR].
- 2026-11-17 21:24 · CEO digital lo maqueta como documento con la plantilla de Varios
- 2026-11-17 21:25 · Entregable listo: Documento v1
- 2026-11-17 21:25 · Calidad: no cumple del todo. Espera aprobación de un socio (riesgo bajo)
- 2026-11-17 21:25 · Guardado en la memoria: precedente y lección
- 2026-11-17 21:33 · Aprobado por un socio
