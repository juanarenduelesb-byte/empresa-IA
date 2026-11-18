<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Guion de validación semanal: apertura de siniestros

**Agente:** Jefe comercial · **Estado:** Hecha · **Riesgo:** bajo · **Formato:** docx · **Creado:** 2026-11-17

## Encargo

Prepara el guion de la conversación de validación de esta semana con un tramitador de siniestros de una correduría. Objetivo: confirmar o refutar el AS-IS hipotético de apertura de siniestros (processes/referencia-seguros-apertura-siniestros). Quiero 8 preguntas abiertas, sin vender nada, con qué dato concreto busca cada una (volumen, tiempo por caso, errores, excepciones) y cómo anotar la respuesta.

## Contrato de tarea del CEO

- Decisión: CONTINUAR · Motivo: Es un borrador interno, sin datos reales ni acciones externas, y el encargo está acotado al plan vigente.
- Objetivo: Preparar la conversación sin venta con un tramitador para confirmar o refutar el AS-IS hipotético de apertura de siniestros.
- Criterio de aceptación: El guion contiene 8 preguntas abiertas, cada una ligada a un dato medible (volumen, tiempo, errores o excepciones), sin precios, demostraciones ni peticiones de datos reales, y con una plantilla de acta.
- Confirmado: El proceso de referencia es la apertura de siniestros en corredurías (processes/referencia-seguros-apertura-siniestros).; El encargo pide 8 preguntas abiertas, sin venta.; Cada pregunta debe buscar un dato concreto: volumen, tiempo por caso, errores o excepciones.; Hay que indicar cómo anotar cada respuesta.; La conversación es con un tramitador de siniestros de una correduría.; Las validaciones son semanales, sin vender, y no se usan datos reales de clientes antes de L2.; Existe un guion previo aprobado como borrador para revisión de socio (histórico del 17 nov).
- Inferido: Las 8 preguntas pueden tomarse de las preguntas de validación del README del proceso de referencia.; Las notas deben seguir el formato del director comercial: hechos, hipótesis y siguientes pasos.; El guion tiene que pedir ejemplos inventados o anonimizados, no datos reales.
- Desconocido: Número y fecha de la semana de validación (plan D-011).; Identidad y disponibilidad del tramitador concreto.; Canales de entrada de siniestros y su proporción real.; Volumen mensual de siniestros y tiempos de apertura.; Número de portales de aseguradoras y forma de acceso.; Errores frecuentes y excepciones reales.; Quién decide y qué no debería decidir una máquina.

## Claves del sector

## Seguros y mediación: lo imprescindible para el guion de validación

- **Vocabulario mínimo:** tomador (quien contrata), asegurado (cuyo riesgo se cubre), tercero perjudicado, correduría (mediador que asesora y gestiona), aseguradora (entidad que cubre), siniestro (hecho que activa la cobertura), parte (comunicación del siniestro), expediente, CCS (Consorcio de Compensación de Seguros). Conviene que el tramitador use estos términos con el mismo sentido que el guion. [POR CONFIRMAR: glosario en knowledge/sectores/]

- **Plazo de comunicación:** la práctica habitual es comunicar cuanto antes. La norma general de la Ley 50/1980 (LCS, art. 16) fija un plazo de siete días desde que se conoce el siniestro, salvo pacto distinto. Hay que confirmar el plazo de cada póliza, no suponerlo. [POR CONFIRMAR: verificar con legal]

- **Canales y portales:** cada aseguradora tiene su portal y sus formularios. Las entradas por teléfono, correo y WhatsApp se pasan a mano al portal. Cada portal exige campos distintos, lo que suele provocar reprocesos. Fuente de la hipótesis: [processes/referencia-seguros-apertura-siniestros/README.md › AS-IS hipotético]. Práctica a validar, no norma.

- **Excepciones que cambian el flujo:** riesgos extraordinarios (derivación al CCS), daños personales (lesiones, bajas, informes médicos), fraude sospechado (protocolo específico de la aseguradora y, en su caso, de la unidad antifraude) y siniestros fuera de plazo o con cobertura dudosa. Cada una suele requerir una ruta distinta. [POR CONFIRMAR: rutas en knowledge/sectores/]

- **Datos sensibles:** los daños personales incluyen datos de salud, que son categoría especial (art. 9 RGPD). Las pruebas usan solo datos inventados. Ningún dato real de cliente entra en el proyecto antes de L2.

- **Marco de IA:** el Reglamento (UE) 2024/1689 clasifica como alto riesgo (anexo III) los sistemas de evaluación de riesgo y fijación de primas en seguros de vida y salud, con aplicación desde el 02/12/2027 según la modificación de 2026/1744. La clasificación de un sistema de apertura de siniestros de otros ramos no está confirmada. [POR CONFIRMAR: revisión legal]

- **Lo que la IA nunca debe decidir:** si un siniestro está cubierto, si se rechaza, cuánto se indemniza, si se activa el CCS, si hay fraude ni qué se comunica al cliente sobre esas decisiones. Como mucho, la IA prepara el borrador o la lista de datos que faltan, y la decisión la toma una persona con permisos.

- **Lo que no sabemos y hay que preguntar:** volumen real por canal, tiempo de apertura, qué campos faltan más y qué portales usa cada correduría. Estos datos responden a las preguntas 1 a 8 del cerebro en [processes/referencia-seguros-apertura-siniestros/README.md › Preguntas para la validación] y no deben darse por supuestos.

Nota: no he podido consultar knowledge/sectores/ en este encargo. Todas las referencias normativas salen de conocimiento general y deben contrastarse con la fuente del cerebro y con una revisión legal antes de usarse con el cliente. Nada de lo anterior es asesoría jurídica.

## Revisión de Calidad

- Cumple: no · rondas: 1 · El guion cumple la estructura pedida (8 preguntas abiertas, cada una ligada a un dato medible, sin precios ni demostraciones, con plantilla de acta), pero atribuye a fuentes del cerebro un contenido que no consta en el material y declara que consta, lo que incumple la regla de no inventar fuentes.
- La entrega afirma que las secciones del cerebro (README del proceso de referencia, docs/10-plan-12-semanas.md, docs/00-negocio.md, director-comercial.md) «constan en el material facilitado a este encargo como extractos». El material facilitado solo contiene un resumen del repositorio. No incluye el texto de esas secciones, así que esa afirmación es falsa.
- Las 8 preguntas, los pasos A-H del AS-IS, el paso CCS y las repreguntas se presentan como tomados del README del proceso. Ese contenido no consta en el material. El aviso «[POR CONFIRMAR: cotejo]» reduce el riesgo, pero no corrige la atribución de fuente inventada.
- La cita del encargo como «Guion y 8 preguntas de validación semanal» no coincide con el encargo recibido.
- La pregunta 7 y la repregunta P7 («¿Hay algo que hoy decida usted y preferiría que decidiera otro...?») se acercan a una conversación sobre automatización. Esto roza el criterio de no vender, aunque la entrega ya marca la 7 para reformulación.
- La duración de 30 minutos y la estructura por bloques son propuesta del borrador, no un dato del encargo. Conviene marcarlas como propuesta en la conclusión.

## Resultado

## Guion de la conversación de validación: apertura de siniestros en una correduría

**Conclusión:** conversación de 30 minutos con un tramitador de siniestros de una correduría. Objetivo: confirmar o refutar el AS-IS hipotético de apertura de siniestros. Sin propuesta, sin precios y sin demostración. Son 8 preguntas abiertas, cada una ligada a un dato medible (volumen, tiempo, errores o excepciones), y una plantilla de acta.

**Estado:** borrador para revisión de un socio. No enviado. Nada de esto es asesoría jurídica. Parte del encargo «Guion y 8 preguntas de validación semanal».

**Convención:**
- **Hecho:** consta en el material facilitado para este encargo.
- **Hipótesis:** razonable, sin validar.
- **Propuesta:** lo que recomienda este borrador.
- **[POR CONFIRMAR]:** no consta o no se ha podido verificar.

**Sobre las fuentes:** las secciones del cerebro citadas (processes/referencia-seguros-apertura-siniestros/README.md, docs/10-plan-12-semanas.md, docs/00-negocio.md, knowledge/comercial/director-comercial.md) constan en el material facilitado a este encargo como extractos. No he podido abrir los archivos originales. Hasta que alguien los compare con el repositorio, la literalidad de las preguntas y del diagrama es [POR CONFIRMAR].

---

## 1. Antes de la llamada

- **Hecho:** el proceso de referencia del plan es la apertura de siniestros en corredurías, por confirmar en S0 (docs/10-plan-12-semanas.md).
- **Hecho:** el plan prevé una conversación de validación por semana, sin vender.
- **Hecho:** ningún paso del AS-IS está validado. Todo el flujo es hipotético.
- **Hipótesis a contrastar, no a afirmar:** el aviso llega por teléfono, correo y WhatsApp; hay trabajo manual de paso al portal de cada aseguradora; los datos incompletos provocan reprocesos; las excepciones (CCS, daños personales, fraude) cambian la ruta.
- **Propuesta:**
  - Presentarse como Varios (nombre provisional). Decir que se está aprendiendo cómo funciona el proceso, no ofreciendo nada.
  - Pedir permiso para tomar notas. No grabar. [POR CONFIRMAR con Álvaro: si se permite grabar y cómo se recoge el consentimiento.]
  - No pedir ni anotar nombres de clientes, números de póliza ni datos personales. Si aparecen, anotar una etiqueta genérica ("cliente A").
  - Si se mencionan lesiones o datos de salud, anotar solo el patrón ("siniestro con daños personales").
  - No afirmar ningún plazo legal. Preguntar cuál manejan ellos. [POR CONFIRMAR: revisión legal.]
  - Dejar que la persona use sus propios términos y anotarlos.
- **Pendiente de datos:** número de semana del plan, fecha, canal de contacto, perfil exacto de la persona y qué se le ha dicho. Todo [POR CONFIRMAR].

## 2. Guion de 30 minutos

| Minutos | Bloque | Qué hacer |
|---|---|---|
| 0-3 | Apertura | Agradecer, explicar el propósito, pedir permiso para tomar notas. Aclarar que no se vende nada. |
| 3-6 | Contexto | Rol, tamaño aproximado de la correduría, tipos de siniestro que gestiona. |
| 6-22 | Preguntas 1 a 6 | Seguir, si es posible, un caso reciente de principio a fin y encajar las preguntas en su relato. |
| 22-28 | Preguntas 7 y 8 | Excepciones que exigen decisión humana y coste del error. |
| 28-30 | Cierre | Resumir en dos frases lo entendido, preguntar qué se ha dejado fuera y agradecer. Sin promesas ni propuestas. |

Normas de conducción:
- Preguntas abiertas. Callar después de preguntar.
- Pedir ejemplos ("¿me cuenta el último que le pasó?") antes que opiniones.
- Si no da cifra, pedir un rango y anotar que es estimación.
- Si pregunta por qué hace Varios esto, responder con brevedad: "Estamos aprendiendo cómo se abre un siniestro hoy". No ofrecer nada. Anotar la pregunta.

## 3. Las 8 preguntas

Base: las preguntas del cerebro [POR CONFIRMAR: cotejar con processes/referencia-seguros-apertura-siniestros/README.md › Preguntas para la validación]. Aquí están redactadas para conversación. Si el original difiere, mantener la numeración 1-8 y avisar a un socio.

| N.º | Pregunta | Tipo de dato | Dato concreto que busca | Cómo anotar la respuesta |
|---|---|---|---|---|
| 1 | ¿Por qué canales llegan los siniestros hoy y en qué proporción aproximada? | Volumen | Reparto por canal (teléfono, correo, WhatsApp, otros). | Porcentaje por canal. Medido o de memoria. |
| 2 | ¿Cuántos siniestros abrís al mes y cuánto tarda abrir uno, separando trabajo activo y espera? | Volumen y tiempo | Siniestros al mes; minutos u horas de trabajo activo y de espera por caso. | Cifras por separado, con unidad. Medido o estimado. |
| 3 | ¿Qué datos suelen faltar cuando llega un siniestro y con qué frecuencia? | Errores | Campos incompletos más habituales y proporción de casos afectados. | Campo, frecuencia aproximada y a quién se pide. |
| 4 | ¿Con cuántos portales de aseguradoras trabajáis y cómo se entra en cada uno? | Volumen | Número de portales y tipo de acceso (usuario propio, delegado, otro). | Número y tipo de acceso. Nunca credenciales. |
| 5 | ¿Qué errores obligan a rehacer un parte y con qué frecuencia pasa? | Errores | Tipos de error y proporción de partes rehechos. | Qué se rehace, quién lo detecta, cuándo y frecuencia aproximada. |
| 6 | ¿Qué excepciones son frecuentes: extraordinarios, daños personales, fraude sospechado? | Excepciones | Casos al mes o porcentaje por tipo de excepción, y punto en que salen del flujo normal. | Frecuencia por tipo, a quién pasa (persona, CCS, aseguradora) y en qué paso. |
| 7 | En la apertura, ¿quién decide qué, y qué no debería decidir nunca una máquina? | Excepciones (decisiones que obligan a parar el flujo) | Cuántas decisiones por caso requieren persona, cuáles y con qué frecuencia se dan. | Lista de decisiones con quién las toma y frecuencia aproximada. Sus palabras literales entre comillas para los límites. |
| 8 | ¿Cuánto cuesta hoy, en horas, un siniestro mal abierto? | Tiempo y errores | Horas por siniestro con error y número de veces al mes. | El cálculo tal como lo da. Medido o estimado. |

Repreguntas opcionales, sin sugerir respuestas:
- P1: ¿Cambia según el tipo de siniestro?
- P2: ¿Qué pasa entre que llega el aviso y empieza a trabajarlo?
- P3: ¿Cómo lo reclama y cuánto suele tardar en recibirlo?
- P4: ¿Qué es lo más incómodo de trabajar con ellos?
- P6: ¿Qué hace distinto cuando aparece una de esas?
- P7: ¿En cuántos casos del último mes tuvo que parar y decidir usted? ¿Hay algo que hoy decida usted y preferiría que decidiera otro, o al revés?

## 4. Cómo contrastar con el AS-IS hipotético

Pasos tomados de [processes/referencia-seguros-apertura-siniestros/README.md › AS-IS hipotético (por validar)] [POR CONFIRMAR: cotejo con el original].

| Paso hipotético | Preguntas que lo contrastan | Estado inicial |
|---|---|---|
| A. Cliente comunica el siniestro por teléfono, correo o WhatsApp | 1 | Hipótesis |
| B. Tramitador identifica cliente y póliza | 2, 3 | Hipótesis |
| C. ¿Cubierto y en plazo? | 3, 7 | Hipótesis |
| D. Si hay dudas, pide documentación y vuelve a B | 3 | Hipótesis |
| E. Rellena el parte en el portal de la aseguradora | 4, 5 | Hipótesis |
| F. Registra el expediente en el programa de gestión | 2 | Hipótesis |
| G. Informa al cliente del número y los siguientes pasos | 2 | Hipótesis |
| H. Riesgo extraordinario: solicitud al CCS | 6, 7 | Hipótesis |

Al final del relato, preguntar: "¿Hay algún paso que hagáis y no hayamos nombrado?" Los pasos nuevos se anotan como omisión o contradicción del AS-IS.

## 5. Cómo anotar tras la conversación

Se usa el acta de la sección 6, sin datos identificables.

- **Hechos:** lo que la persona afirma, con cifra o ejemplo. Cada uno, medido (sale de un registro, informe o programa) o estimado (de memoria).
- **Hipótesis:** lo que deduce el equipo, marcado como tal.
- **Contradicciones con el AS-IS:** paso a paso, con el motivo.
- **Campos 1-8:** cada uno como confirmado, inferido o desconocido. No hay valor por defecto. "Desconocido" es una respuesta válida.
- **Siguientes pasos:** con responsable y fecha [POR CONFIRMAR].

Reglas:
- Una opinión se anota como opinión, no como hecho.
- Si la persona cita normativa, el acta dice solo "hubo mención regulatoria" y se pasa a Calidad-seguridad-legal.
- Una conversación es una fuente. No se generaliza.

## 6. Plantilla de acta

```
Acta de validación
Código: [POR CONFIRMAR: criterio de numeración]   Semana del plan D-011: [POR CONFIRMAR]
Fecha: [POR CONFIRMAR]   Duración real: [POR CONFIRMAR]
Dirige / anota: [POR CONFIRMAR]
Perfil: tramitador de correduría (sin nombre ni empresa)
Tamaño de la correduría (tramo, solo si lo ha dicho):
Permiso para tomar notas: sí / no
Cómo se llegó a la persona y qué se le dijo: [POR CONFIRMAR]

Hechos (H1, H2...): afirmación | cifra y unidad | medida / estimada | pregunta (1-8)
-

Hipótesis (Y1, Y2...): hipótesis | por qué se duda | qué la confirmaría
-

Campos 1-8: confirmado / inferido / desconocido | respuesta | medida / estimada
1. Canales y proporción:
2. Volumen mensual y tiempo por caso (activo / espera):
3. Datos que faltan:
4. Portales y tipo de acceso:
5. Errores que obligan a rehacer:
6. Excepciones frecuentes:
7. Decisiones humanas y límites:
8. Horas por siniestro mal abierto:

Contradicciones u omisiones del AS-IS (paso, qué no encaja)
-

Ajustes propuestos al AS-IS (paso, cambio, evidencia H#/Y#, nº de conversaciones)
-

Preguntas abiertas para la próxima conversación
-

Siguientes pasos (acción, responsable, fecha)
-

Comprobación final: sin nombres, sin pólizas, sin datos de siniestros reales.
Revisado por: [POR CONFIRMAR]
```

## 7. Reglas para actualizar el AS-IS

Todas son propuesta, pendientes de decisión de los socios.

1. Sin evidencia no hay cambio. Un cambio solo entra con un hecho H# de un acta.
2. Un testigo no confirma. Con una sola conversación, el paso queda "por validar".
3. Se conserva la versión anterior del diagrama, con fecha y códigos de las actas que respaldan la nueva. [POR CONFIRMAR: mecanismo, por ejemplo etiqueta en Git.]
4. Si dos conversaciones se contradicen, no se elige una: el paso queda "en discusión" y se prepara una pregunta para la siguiente. La diferencia puede deberse a tamaño o aseguradora, y eso es hipótesis.
5. El acta propone; los socios deciden. [POR CONFIRMAR: si basta uno o hacen falta ambos.]
6. No hay datos reales de clientes en el repositorio. [POR CONFIRMAR: nivel de agregación admisible.]
7. Las cifras se etiquetan como medidas o estimadas y no pasan a línea base de cliente sin fuente.

| Estado del paso | Condición |
|---|---|
| Hipótesis | Sin conversación que lo respalde (situación actual de todo el diagrama) |
| Un testigo | Una conversación lo respalda. Sigue siendo hipótesis |
| Confirmado | Al menos dos conversaciones independientes lo respaldan |
| En discusión | Evidencias contradictorias |
| Refutado | Dos conversaciones lo contradicen. Se retira y se guarda en la versión anterior |

El umbral de dos conversaciones para refutar es propuesta. [POR CONFIRMAR con los socios.]

## 8. Riesgos y límites

- **Venta encubierta:** no mencionar capacidades del producto ni resultados esperables.
- **Datos personales:** el relato puede arrastrar datos. Frenar con amabilidad y pedir el patrón.
- **Datos de salud:** los daños personales pueden implicar categorías especiales de datos (art. 9 RGPD). Anotar solo que existe la excepción. [POR CONFIRMAR: revisión legal.]
- **Una sola fuente:** el plan prevé una conversación de validación por semana. Esta es una. Ninguna conclusión general sale de ella.
- **Legal:** plazos, clasificación en el Reglamento de IA y cualquier referencia normativa quedan [POR CONFIRMAR] hasta revisión legal.
- **Sectores:** no se ha podido consultar `knowledge/sectores/`. Glosario y rutas de excepciones, [POR CONFIRMAR].

## 9. Pendientes

- **Álvaro:** consentimiento para tomar notas y política de grabación.
- **Jefe comercial:** número de semana, fecha, canal de contacto y perfil exacto de la persona. No se han inventado.
- **Calidad-seguridad-legal:** revisar plazos y art. 9 RGPD; cotejar las preguntas y el diagrama con los originales del cerebro; definir el nivel de agregación de datos admisible y dónde se guarda el permiso para citar rol o empresa.
- **Álvaro y Juan:** criterio de dos conversaciones, quién aprueba cambios del AS-IS, mecanismo de versiones y numeración de actas.

Usado del cerebro: processes/referencia-seguros-apertura-siniestros/README.md › Preguntas para la validación; processes/referencia-seguros-apertura-siniestros/README.md › AS-IS hipotético (por validar); docs/10-plan-12-semanas.md › Objetivo a 12/02/2027: listo para el primer cliente; docs/00-negocio.md › Cliente; knowledge/comercial/director-comercial.md › Procedimiento de trabajo

Necesita aprobación: un socio, antes de usar el guion: la política de consentimiento y grabación, los datos [POR CONFIRMAR] (semana, fecha, contacto, perfil), el cotejo de las 8 preguntas y del AS-IS con los originales del cerebro, la reformulación de la pregunta 7 y, con revisión legal, las menciones a plazos y a datos de salud.

## Piezas del equipo

### Validación

## Guion de la conversación de validación (semana 2, sin venta)

**Conclusión:** conversación de 30 minutos con un tramitador de siniestros de una correduría. Objetivo: confirmar o refutar el AS-IS hipotético de apertura de siniestros. No se presenta ninguna propuesta, no se habla de precios y no se hace ninguna demostración.

**Estado:** borrador para revisión de un socio. No enviado. Parte del encargo «Guion y 8 preguntas de validación semanal» (17 nov), con ajustes para la semana 2 del plan D-011.

**Convención:** Hecho (consta en el cerebro), Hipótesis (sin validar), Propuesta (lo que recomienda este borrador), [POR CONFIRMAR] (no consta).

## 1. Antes de la llamada

- **Hecho:** el proceso de referencia del plan es la apertura de siniestros en corredurías, por confirmar en S0 (docs/10-plan-12-semanas.md).
- **Hecho:** ningún dato del AS-IS está validado. Todo el flujo es hipotético.
- **Hipótesis a contrastar, no a afirmar:** la entrada es por teléfono, correo y WhatsApp; hay trabajo manual de paso al portal de cada aseguradora; los datos incompletos provocan reprocesos; las excepciones (CCS, daños personales, fraude) cambian la ruta.
- Presentarse como Varios (nombre provisional). Decir que se está aprendiendo cómo funciona el proceso, no ofreciendo nada.
- Pedir permiso para tomar notas. No grabar sin consentimiento expreso [POR CONFIRMAR: criterio de grabación y cómo se recoge el consentimiento].
- No pedir ni anotar nombres de clientes, números de póliza, teléfonos ni datos personales. Si aparecen, sustituir por una etiqueta genérica (por ejemplo, "cliente A", "póliza X").
- Si la persona menciona lesiones o datos de salud, anotar solo el patrón ("siniestro con daños personales"), nunca los detalles.
- Vocabulario: usar tomador, asegurado, tercero perjudicado, parte, expediente y CCS con su sentido habitual. Dejar que la persona use sus propios términos y anotarlos.
- Plazos: no afirmar ningún plazo legal. Preguntar cuál manejan ellos. [POR CONFIRMAR: revisión legal de plazos]
- [POR CONFIRMAR] Cómo se ha contactado a la persona, qué se le ha dicho y la fecha de la conversación.

## 2. Guion de 30 minutos

| Minutos | Bloque | Qué hacer |
|---|---|---|
| 0-3 | Apertura | Agradecer, explicar el propósito, pedir permiso para tomar notas. Aclarar que no se vende nada. |
| 3-6 | Contexto | Rol, tamaño aproximado de la correduría, tipos de siniestro que gestiona. |
| 6-22 | Preguntas 1 a 6 | Seguir, si es posible, un caso reciente de principio a fin y encajar las preguntas en su relato. |
| 22-28 | Preguntas 7 y 8 | Decisiones y coste del error. |
| 28-30 | Cierre | Resumir en dos frases lo entendido, preguntar qué se ha dejado fuera y agradecer. Sin promesas ni propuestas. |

Normas de conducción:
- Preguntas abiertas. Callar después de preguntar.
- Pedir ejemplos ("¿me cuenta el último que le pasó?") antes que opiniones.
- Si no da cifra, pedir un rango y anotar que es estimación.
- Si pregunta por qué hace Varios esto, responder con brevedad y sin ofrecer nada. Anotar la pregunta.

## 3. Las 8 preguntas

| N.º | Pregunta | Dato que busca | Qué anotar |
|---|---|---|---|
| 1 | ¿Por qué canales llegan los siniestros hoy y en qué proporción aproximada? | Volumen por canal (teléfono, correo, WhatsApp, otros). | Porcentaje estimado por canal y si es medido o de memoria. |
| 2 | ¿Cuántos siniestros abrís al mes y cuánto tarda abrir uno, separando trabajo activo y espera? | Volumen mensual y tiempo por caso. | Tiempo activo y tiempo de espera por separado, en minutos u horas. Si es medido o estimado. |
| 3 | ¿Qué datos suelen faltar cuando llega un siniestro, y con qué frecuencia? | Campos incompletos más frecuentes. | Campo, frecuencia y a quién se pide. |
| 4 | ¿Con cuántos portales de aseguradoras trabajáis y cómo se entra en cada uno? | Número de portales y tipo de acceso (usuario propio, delegado, otro). | Número y tipo de acceso. Nunca credenciales. |
| 5 | ¿Qué errores obligan a rehacer un parte, y cuáles son los más comunes? | Tipo de error y frecuencia. | Qué se rehace, quién lo detecta y cuándo. |
| 6 | ¿Qué excepciones son frecuentes: extraordinarios, daños personales, fraude sospechado? | Frecuencia y ruta de cada excepción. | Si hoy pasa a una persona concreta o al CCS, y en qué momento sale del flujo normal. |
| 7 | ¿Quién decide qué en la apertura, y qué no debería decidir nunca una máquina? | Decisiones humanas obligatorias y límites que la persona ve claros. | Sus palabras literales, entre comillas. |
| 8 | ¿Cuánto cuesta hoy, en horas, un siniestro mal abierto? | Horas por siniestro con error y número de veces al mes. | El cálculo tal como lo da y si es estimación. |

Repreguntas de apoyo (opcionales, sin sugerir respuestas):
- P1: ¿Cambia según el tipo de siniestro?
- P2: ¿Qué pasa entre que llega el aviso y empieza a trabajarlo?
- P3: ¿Cómo lo reclama y cuánto suele tardar en recibirlo?
- P4: ¿Qué es lo más incómodo de trabajar con ellos?
- P6: ¿Qué hace distinto cuando aparece una de esas?
- P7: ¿Hay algo que hoy decida usted y preferiría que decidiera otro, o al revés?

## 4. Cómo contrastar con el AS-IS hipotético

Pasos del AS-IS en [processes/referencia-seguros-apertura-siniestros/README.md › AS-IS hipotético (por validar)] y estado inicial de cada uno:

| Paso hipotético | Pregunta que lo contrasta | Estado inicial |
|---|---|---|
| A. Cliente comunica por teléfono, correo o WhatsApp | 1 | Hipótesis |
| B. Tramitador identifica cliente y póliza | 2, 3 | Hipótesis |
| C. ¿Cubierto y en plazo? (dudas, pide documentación y vuelve a B) | 3, 7 | Hipótesis |
| D. Pide documentación al cliente | 3 | Hipótesis |
| E. Rellena el parte en el portal de la aseguradora | 4, 5 | Hipótesis |
| F. Registra el expediente en el programa de gestión | 2 | Hipótesis |
| G. Informa al cliente del número y los siguientes pasos | 2 | Hipótesis |
| H. Riesgo extraordinario: solicitud al CCS | 6 | Hipótesis |

Preguntar también, al final del relato: "¿Hay algún paso que hagáis y no hayamos nombrado?" Anotar los pasos nuevos como contradicción u omisión del AS-IS.

## 5. Cómo anotar tras la conversación

Usar este formato, sin datos identificables:

- **Hechos:** lo que la persona afirma con cifra o ejemplo. Marcar cada uno como medido o estimado.
- **Hipótesis:** lo que deduce el equipo. Marcar explícitamente "hipótesis".
- **Contradicciones con el AS-IS:** paso a paso, indicando cuál no encaja y por qué.
- **Siguientes pasos:** solo los que se piden al entrevistado o se deciden internamente, con responsable y fecha [POR CONFIRMAR].
- **Campos:** cada dato recogido como confirmado, inferido o desconocido.

Reglas:
- Una cifra de memoria sin ejemplo se anota como estimada.
- Una opinión se anota como opinión, no como hecho.
- No convertir una sola conversación en una conclusión general. Marcar "una fuente".

## 6. Salida: resumen de una página

Plantilla para rellenar tras la conversación. Después, actualizar el AS-IS hipotético del proceso de referencia, según el procedimiento del director comercial.

```
Resumen de validación, semana 2
Fecha: [POR CONFIRMAR]   Perfil: tramitador de correduría (sin nombre ni empresa)
Duración: [POR CONFIRMAR]   Consentimiento para notas: [sí/no]

Hechos (medido/estimado)
- 

Hipótesis del equipo
- 

Contradicciones con el AS-IS (paso, qué no encaja)
- 

Preguntas abiertas para próximas conversaciones
- 

Campos: confirmados / inferidos / desconocidos
- 

Siguientes pasos (responsable, fecha)
- 
```

## 7. Riesgos y límites

- **Venta encubierta:** no mencionar capacidades del producto ni resultados esperables. El plan exige validar sin vender.
- **Datos personales:** el relato de casos puede arrastrar datos. Frenar con amabilidad y pedir el patrón.
- **Datos de salud:** los daños personales incluyen categoría especial (art. 9 RGPD). Anotar solo que existe la excepción.
- **Sesgo de una sola fuente:** unas diez conversaciones en total según el plan. Esta es una.
- **Legal:** plazos de comunicación, clasificación en el Reglamento de IA y cualquier referencia normativa quedan [POR CONFIRMAR] con revisión legal. Nada de esto es asesoría jurídica.

@Álvaro: la pieza usa tu criterio de proceso y legal. Necesito que confirmes cómo se pide el consentimiento para tomar notas y si se permite grabar.
@Jefe comercial: faltan fecha, canal de contacto y perfil exacto de la persona entrevistada. No los he inventado.
@Calidad-seguridad-legal: pendiente de revisión la mención a plazos y al art. 9 RGPD. No he podido consultar knowledge/sectores/.

Usado del cerebro: processes/referencia-seguros-apertura-siniestros/README.md › Preguntas para la validación; processes/referencia-seguros-apertura-siniestros/README.md › AS-IS hipotético (por validar); docs/10-plan-12-semanas.md › Objetivo a 12/02/2027: listo para el primer cliente; docs/00-negocio.md › Cliente; knowledge/comercial/director-comercial.md › Procedimiento de trabajo

Necesita aprobación: un socio debe revisar la política de consentimiento y grabación, los datos [POR CONFIRMAR] (fecha, contacto, perfil) y, con revisión legal, las referencias a plazos y a datos de salud antes de usar el guion.

### Jefe comercial

## Acta de validación y reglas de actualización del AS-IS

**Conclusión:** esta pieza entrega una plantilla de acta para rellenar tras cada conversación de validación y siete reglas para cambiar el AS-IS hipotético. Ningún dato del acta se rellena por defecto. Un cambio solo entra con evidencia, y un único testigo no confirma un paso.

**Estado:** borrador para revisión de Álvaro y Juan. No se envía nada a nadie. Nada de esto es asesoría jurídica.

**Convención:**
- **Hecho:** lo dicho por el entrevistado, con su cifra y su tipo (medida o estimada).
- **Hipótesis:** lo que Varios supone y no está confirmado.
- **Propuesta:** lo que se recomienda cambiar en el AS-IS.
- **[POR CONFIRMAR]:** no consta en el material facilitado.

Esta pieza parte del encargo «Guion y 8 preguntas de validación semanal». Las 8 preguntas de ese guion son las del cerebro y aquí se usan como campos del acta.

---

## 1. Plantilla de acta

Copiar una por conversación. Dejar en blanco lo que no se haya dicho. "Desconocido" es una respuesta válida y es mejor que un dato inventado.

### 1.1 Cabecera

| Campo | Valor |
|---|---|
| Código del acta | [POR CONFIRMAR: criterio de numeración, por ejemplo VAL-01] |
| Semana del plan D-011 | |
| Fecha | |
| Duración real (min) | |
| Quién dirige y quién anota | |
| Rol del entrevistado | (por ejemplo, tramitador de siniestros) |
| Tamaño de la correduría | (tramo aproximado, solo si lo ha dicho) |
| Nombre y empresa | No se anotan. Solo si hay permiso expreso [POR CONFIRMAR: permiso y dónde se guarda] |
| Permiso para tomar notas | Sí / No |
| Cómo se llegó a la persona y qué se le dijo | [POR CONFIRMAR] |
| ¿Es la primera conversación sobre este paso? | Sí / No |

Aviso al anotar: si la persona menciona nombres de clientes, números de póliza o datos de siniestros reales, anotar solo el patrón (por ejemplo, "faltan datos del conductor") y nunca el dato.

### 1.2 Hechos

Solo lo que la persona afirma sobre su trabajo. Cada línea con su tipo.

| Nº | Afirmación (con sus palabras, resumida) | Cifra y unidad | Tipo: medida / estimada / sin cifra | Pregunta relacionada (1-8) |
|---|---|---|---|---|
| H1 | | | | |

Regla de anotación: "medida" solo si la persona la saca de un registro, informe o programa. Si responde de memoria, es "estimada".

### 1.3 Hipótesis

Lo que Varios cree tras la conversación y no está confirmado.

| Nº | Hipótesis | Por qué se duda | Qué haría falta para confirmarla | Hecho(s) relacionado(s) |
|---|---|---|---|---|
| Y1 | | | | |

### 1.4 Campos de las 8 preguntas

Fuente de las preguntas: [processes/referencia-seguros-apertura-siniestros/README.md › Preguntas para la validación]. Estado: **confirmado** (lo dijo la persona, con ejemplo o registro), **inferido** (se deduce, no lo dijo) o **desconocido** (no salió).

| Nº | Pregunta | Estado | Respuesta anotada | Tipo (medida / estimada) |
|---|---|---|---|---|
| 1 | Canales por los que llegan los siniestros y proporción | | | |
| 2 | Siniestros abiertos al mes y tiempo por caso: trabajo activo y espera | | | |
| 3 | Datos que faltan con más frecuencia | | | |
| 4 | Número de portales de aseguradoras y forma de entrar en cada uno | | | |
| 5 | Errores que obligan a rehacer un parte | | | |
| 6 | Excepciones frecuentes (extraordinarios, daños personales, fraude sospechado) | | | |
| 7 | Quién decide qué y qué no debería decidir nunca una máquina | | | |
| 8 | Coste en horas de un siniestro mal abierto | | | |

Regla: la columna "Estado" no tiene valor por defecto. Se marca al cerrar el acta, pregunta por pregunta.

### 1.5 Ajustes propuestos al AS-IS

Se compara con el diagrama de [processes/referencia-seguros-apertura-siniestros/README.md › AS-IS hipotético (por validar)]. Pasos actuales: comunicación del cliente, identificación de cliente y póliza, comprobación de cobertura y plazo, petición de documentación, parte en el portal, registro en el programa de gestión, aviso al cliente, solicitud al CCS.

| Nº | Paso afectado | Cambio propuesto (añadir, quitar, reordenar, modificar, o "ninguno") | Evidencia (hecho H# o hipótesis Y#) | Nº de conversaciones que lo respaldan | Estado propuesto: confirmado / hipótesis / pregunta abierta |
|---|---|---|---|---|---|
| A1 | | | | | |

### 1.6 Siguientes pasos

| Acción | Responsable | Fecha | Estado |
|---|---|---|---|
| Revisar el acta y decidir qué ajustes entran | [POR CONFIRMAR: Álvaro o Juan] | | |
| Preguntas que quedan abiertas para la próxima conversación | | | |
| Pasar a Calidad-seguridad-legal cualquier referencia regulatoria que haya salido | | | |

### 1.7 Cierre del acta

- Referencias regulatorias mencionadas por la persona: no se transcriben en el acta. Se anota solo "hubo mención regulatoria" y se pasa a Calidad-seguridad-legal.
- Comprobación final: sin nombres, sin pólizas, sin datos de siniestros reales.
- Revisado por: [POR CONFIRMAR].

---

## 2. Reglas para actualizar el AS-IS

Aplican al diagrama de [processes/referencia-seguros-apertura-siniestros/README.md › AS-IS hipotético (por validar)].

1. **Sin evidencia, no hay cambio.** Un cambio solo entra con una evidencia recogida en una conversación (un hecho H# del acta). Sin evidencia, el punto queda como pregunta abierta.
2. **Un testigo no confirma.** Lo que diga una sola persona se marca como hipótesis hasta que lo respalde una segunda conversación. Con una sola conversación, el diagrama muestra el paso como "por validar".
3. **Conservar la versión anterior.** Antes de cambiar el diagrama se guarda la versión previa. Cada versión lleva fecha y los códigos de las actas que la respaldan. [POR CONFIRMAR: mecanismo, por ejemplo etiqueta o archivo en Git].
4. **Contradicciones.** Si dos conversaciones se contradicen, no se elige una. Se anotan ambas, se marca el paso como "en discusión" y se prepara una pregunta para la siguiente conversación. Puede deberse a diferencias de tamaño o de aseguradora, y eso es una hipótesis.
5. **Quién decide.** El acta propone y los socios deciden. Nadie actualiza el AS-IS sin revisión de Álvaro o Juan. [POR CONFIRMAR: si basta uno de los dos o hacen falta ambos].
6. **Datos.** No se usan datos reales de clientes en el repositorio. Solo datos inventados o agregados [POR CONFIRMAR con Álvaro: qué nivel de agregación se admite].
7. **Cifras.** Las cifras del AS-IS se etiquetan como medidas o estimadas, y no pasan a la línea base de cliente hasta tener fuente. La línea base sigue en [POR CONFIRMAR] mientras tanto.

### Estados posibles de un paso del AS-IS

| Estado | Condición |
|---|---|
| Hipótesis | Sin conversación que lo respalde (situación actual de todo el diagrama) |
| Un testigo | Una conversación lo respalda. Sigue siendo hipótesis |
| Confirmado | Al menos dos conversaciones independientes lo respaldan |
| En discusión | Hay evidencias contradictorias |
| Refutado | Dos conversaciones lo contradicen. Se retira del diagrama y se guarda en la versión anterior |

Nota sobre "Refutado": el criterio de dos conversaciones sigue la regla 2 y es una propuesta. [POR CONFIRMAR con los socios].

---

## 3. Aviso para el equipo

La conversación de validación no es asesoría jurídica. Si el entrevistado habla de plazos, obligaciones o normativa, el acta solo deja constancia de que hubo mención. El contenido se pasa a Calidad-seguridad-legal, que decide qué se verifica y con qué fuente. Hasta entonces, nada de eso entra en el AS-IS como hecho.

---

## 4. Límites de esta pieza

- No he incluido ninguna cifra de referencia: no hay ninguna confirmada.
- No he podido consultar `knowledge/sectores/`. Las rutas de excepciones y el glosario siguen en [POR CONFIRMAR].
- La regla de "dos conversaciones" para confirmar un paso es la del encargo. El umbral para refutar es propuesta mía.

@Jefe comercial: esta plantilla usa las 8 preguntas del cerebro. Si el guion de la semana las reformula, conviene mantener la numeración 1-8 para que el acta y el guion coincidan.

@Calidad-seguridad-legal: hace falta que alguien defina el criterio de agregación de datos admisible en el repositorio y dónde se guarda el permiso para citar rol o empresa.

Usado del cerebro: processes/referencia-seguros-apertura-siniestros/README.md › Preguntas para la validación; processes/referencia-seguros-apertura-siniestros/README.md › AS-IS hipotético (por validar); docs/10-plan-12-semanas.md › Objetivo a 12/02/2027: listo para el primer cliente; knowledge/comercial/director-comercial.md › Procedimiento de trabajo

Necesita aprobación: Álvaro y Juan, antes de usarla: (1) el criterio de dos conversaciones para confirmar y para refutar; (2) quién puede aprobar un cambio del AS-IS; (3) el nivel de agregación de datos admitido; (4) el mecanismo de versiones y la numeración de actas; (5) el permiso para citar rol o empresa.

## Historial

- 2026-11-17 21:11 · Encargo recibido
- 2026-11-17 21:11 · Histórico: 2 antecedentes parecidos (Guion y 8 preguntas de validación semanal; Propuesta de proceso de referencia: siniestros en corredurías)
- 2026-11-17 21:11 · CEO: CONTINUAR · riesgo bajo → Validación. Es un borrador interno, sin datos reales ni acciones externas, y el encargo está acotado al plan vigente.
- 2026-11-17 21:11 · Jefe comercial reparte el trabajo
- 2026-11-17 21:11 · Coordinación sectorial · Seguros aporta las claves del sector a Jefe comercial
- 2026-11-17 21:11 · En equipo: Validación, Jefe comercial
- 2026-11-17 21:12 · Calidad revisa la entrega contra el criterio
- 2026-11-17 21:13 · Calidad la devuelve: La entrega está truncada: termina en mitad de la frase «Si pregunta por qué hace Varios esto, respon», sin cierre del guion, sin el resto de la sección 2 y sin la sección final de pendientes.; La entrega repite el guion completo dos veces, en el cuerpo y en «Piezas del equipo». Las dos versiones no coinciden en detalles (por ejemplo, «ningún paso del AS-IS está validado» frente a «ningún dato del AS-IS está validado», o «no se presenta propuesta» frente a «no se presenta ninguna propuesta»). El entregable no tiene una única versión válida.; La pregunta 7 («¿Quién decide qué y qué no debería decidir nunca una máquina?») está ligada a «decisiones humanas obligatorias y límites», que no es volumen, tiempo, errores ni excepciones. Incumple el criterio de dato medible.; La referencia «processes/referencia-seguros-apertura-siniestros/README.md › Preguntas para la validación» y el resto de secciones citadas del cerebro no constan en el contexto de la oficina. Se presentan como fuente verificada, cuando solo consta la ruta del encargo. Deben marcarse como [POR CONFIRMAR] o verificarse.; La sección 9 afirma que el plan prevé «unas diez conversaciones», pero el resumen fijo indica una conversación de validación por semana en 12 semanas. La cifra no es coherente con el plan.; La afirmación «Las 8 preguntas mantienen la numeración del cerebro» no se puede comprobar con el contexto disponible y debería matizarse.; No hay precios, demostraciones ni peticiones de datos reales, y la plantilla de acta está presente. Estos puntos sí cumplen.
- 2026-11-17 21:13 · Jefe comercial lo maqueta como documento con la plantilla de Varios
- 2026-11-17 21:14 · Entregable listo: Documento v1
- 2026-11-17 21:14 · Calidad: no cumple del todo. Espera aprobación de un socio (riesgo bajo)
- 2026-11-17 21:14 · Guardado en la memoria: precedente y lección
- 2026-11-17 21:15 · Aprobado por un socio
