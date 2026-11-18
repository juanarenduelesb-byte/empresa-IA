<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Conversaciones con Jefe comercial

**Jefe comercial** · 2026-11-17 21:12

**Pieza para Jefe comercial**

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

@Calidad-seguridad-legal: hace falta que algu

**Jefe comercial** · 2026-11-17 21:14

**Entrega: Guion de validación semanal: apertura de siniestros**

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
- *
