<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Conversaciones con Arquitecto de procesos

**Arquitecto de procesos** · 2026-11-17 20:04

**Pieza para Arquitecto de procesos**

# Apertura de siniestros en corredurías

**Estado:** borrador para revisión. Fecha límite: 22/11/2026. No validado con ningún responsable de correduría.
**Ruta prevista:** `processes/seguros-apertura-siniestros/README.md`

Convención de este documento:
- **Hecho (repositorio):** lo que consta en el cerebro. Se cita la ruta.
- **Hipótesis:** lo que parece razonable pero no está validado.
- **Propuesta:** lo que Varios recomienda decidir.
- **[POR CONFIRMAR]:** no está en el repositorio. No se inventa.

## Conclusión

El proceso es un buen candidato a proceso de referencia. Tiene riesgo medio y un flujo claro (correo, póliza, cobertura, apertura). Además los partes con lesiones salen del flujo automático por contener datos de salud. La IA solo lee y extrae. Las reglas comprueban póliza y cobertura. El tramitador aprueba cada apertura. Todo el AS-IS está por confirmar, porque aún no hay conversaciones de validación. Se trabaja solo con datos inventados.

## Hechos del repositorio

- El proceso es el de referencia del plan D-011, "por confirmar en S0" [docs/10-plan-12-semanas.md › Objetivo a 12/02/2027].
- Caso A: correduría, siniestros por correo, riesgo medio. La IA lee y extrae. Las reglas comprueban póliza y cobertura. Los partes con lesiones salen del flujo automático. El tramitador aprueba cada apertura. Una fecha ambigua se marca para revisión [docs/12-simulacion.md › Casos].
- Estado: 0 clientes, 0 líneas de código. Ningún dato real en todo el periodo [CLAUDE.md › Contexto rápido].
- Control B (15/01/2027): 20 siniestros inventados recorren lectura, extracción, reglas, revisión humana, apertura simulada y registro [docs/10-plan-12-semanas.md › Controles de paso].
- Este proceso figura como "primer candidato (ejemplo, sin validar)" [processes/README.md › Catálogo de procesos].

## Proceso y sector

- **Proceso:** apertura de siniestros a partir de comunicaciones recibidas por correo.
- **Sector:** seguros, correduría.
- **Tipos de siniestro cubiertos:** [POR CONFIRMAR] (hipótesis: empezar por un solo ramo sin lesiones, por ejemplo hogar o comercio).
- **Aseguradoras con las que se trabaja:** [POR CONFIRMAR]. Hay que saber si la apertura se hace en el portal de cada aseguradora, por correo o por otra vía.

## Responsable en el cliente

[POR CONFIRMAR]. Hipótesis: el responsable de siniestros o el tramitador jefe. Hay que identificarlo en la primera conversación de validación (una por semana desde S2, sin vender).

## AS-IS

**Estado:** el repositorio no describe el proceso actual. Los pasos siguientes son una **hipótesis de trabajo** para guiar las conversaciones de validación. Ninguno está confirmado.

### Pasos (hipótesis)

| # | Paso actual | Quién (hipótesis) | Estado |
|---|---|---|---|
| 1 | Llega un correo del cliente o del asegurado con la comunicación del siniestro | Persona | [POR CONFIRMAR] |
| 2 | Alguien lee el correo y los adjuntos (fotos, partes, facturas) | Persona | [POR CONFIRMAR] |
| 3 | Se identifica al asegurado y la póliza | Persona | [POR CONFIRMAR] |
| 4 | Se comprueba que la póliza está en vigor y que la cobertura aplica | Persona | [POR CONFIRMAR] |
| 5 | Se piden datos o documentos que faltan | Persona | [POR CONFIRMAR] |
| 6 | Se abre el siniestro en el sistema de la correduría o de la aseguradora | Persona | [POR CONFIRMAR] |
| 7 | Se avisa al asegurado y se archiva el expediente | Persona | [POR CONFIRMAR] |

### Cifras actuales

| Dato | Valor |
|---|---|
| Volumen de siniestros al mes | [POR CONFIRMAR] |
| Porcentaje que llega por correo | [POR CONFIRMAR] |
| Tiempo por caso (de la recepción a la apertura) | [POR CONFIRMAR] |
| Tiempo de trabajo efectivo por caso | [POR CONFIRMAR] |
| Porcentaje de casos con datos incompletos | [POR CONFIRMAR] |
| Errores frecuentes | [POR CONFIRMAR] |
| Número de tramitadores | [POR CONFIRMAR] |

### Excepciones (hipótesis a validar)

- Partes con lesiones o datos de salud. Esta excepción sí consta como regla del caso A [docs/12-simulacion.md › Casos].
- Fechas ambiguas del siniestro. Consta como regla del caso A [docs/12-simulacion.md › Casos].
- Póliza no localizada, caducada o con impago: [POR CONFIRMAR].
- Cobertura dudosa: [POR CONFIRMAR].
- Siniestro duplicado: [POR CONFIRMAR].
- Correo sin adjuntos o con adjuntos ilegibles: [POR CONFIRMAR].
- Correo que no es un siniestro: [POR CONFIRMAR].

## TO-BE (propuesta)

Sigue los 12 pasos [docs/12-simulacion.md › Los 12 pasos], aplicados al caso A.

| # | Paso | Quién | Qué pasa en este proceso |
|---|---|---|---|
| 1 | Entra la petición | **Reglas** | Llega el correo. Se identifica el remitente y de qué cliente (correduría) es. Si no se reconoce, se pregunta o se rechaza. |
| 2 | Entender | **IA** | Lee el correo y los adjuntos. Extrae intención, tipo de siniestro, fecha, datos del asegurado y número de póliza. Cada campo se marca como confirmado, inferido o desconocido. |
| 3 | Preguntar lo que falta | **IA** (redacta) y **persona** (envía) | Prepara la petición de datos que faltan. No inventa ninguno. El envío al asegurado lo aprueba el tramitador. |
| 4 | Clasificar y riesgo | **Reglas + IA** | Las reglas detectan indicios de lesiones y datos de salud. Si los hay, el caso sale del flujo automático y pasa a una persona. Una fecha ambigua se marca para revisión. Riesgo del caso: medio. |
| 5 | Consultar conocimiento | **Reglas** | Se comprueban los permisos antes de buscar. Solo se consulta el conocimiento de esa correduría. Los datos de otros clientes quedan bloqueados. |
| 6 | Hacer el plan | **IA** | Propone las tareas con sus dependencias. Cada una va marcada como IA, reglas o persona. |
| 7 | Asignar | **Reglas** | Asigna al departamento de siniestros y a los especialistas de sector, con las herramientas mínimas. |
| 8 | Aprobaciones | **Persona** | El tramitador aprueba cada apertura. Nada se abre sin esa aprobación. |
| 9 | Ejecutar | **Motor de procesos** | En cola, en marcha, espera persona, terminada o bloqueada. La póliza y la cobertura las comprueban las reglas. En la demo, la apertura es simulada. |
| 10 | Control de calidad | **Reglas + persona** | Si algo falla, no se corrige a ciegas: se marca. Hay muestreo de revisión humana [POR CONFIRMAR el porcentaje]. |
| 11 | Entregar | **Reglas** | Se entrega el resultado con evidencias y límites: qué se extrajo, qué se comprobó y qué quedó pendiente. |
| 12 | Registro y aprendizaje | **Reglas + persona** | Todo queda auditado. Lo aprendido entra como borrador y lo aprueba una persona. |

### Reparto resumido

- **IA:** leer y extraer, redactar preguntas, proponer el plan.
- **Reglas:** identificar al cliente, comprobar póliza y cobertura, detectar lesiones, controlar permisos, asignar, registrar.
- **Persona:** aprobar cada apertura, enviar comunicaciones externas, resolver fechas ambiguas, tramitar los partes con lesiones.

### Casos que salen del flujo automático

1. Partes con lesiones o datos de salud. Los trata una persona fuera del flujo automático [hecho: docs/12-simulacion.md › Casos].
2. Fecha ambigua. Queda marcada para revisión [hecho].
3. Póliza no encontrada o cobertura dudosa. Propuesta: pasa a persona.
4. Campos críticos desconocidos tras preguntar. Propuesta: el CEO decide ESCALAR o DERIVAR.

## Riesgo

| Aspecto | Valoración |
|---|---|
| Nivel del caso | Medio [hecho: docs/12-simulacion.md › Casos]. Aprobación según impacto. |
| Datos sensibles | Datos personales de asegurados. Datos de salud en partes con lesiones, que salen del flujo [hecho]. Otros datos especiales: [POR CONFIRMAR]. |
| Datos en esta fase | Solo inventados. Ningún dato real antes de L2 [hecho: CLAUDE.md]. |
| Reglamento Europeo de IA | **Hipótesis orientativa:** no parece encajar en alto riesgo del anexo III por la función descrita. Requiere revisión profesional. No se afirma cumplimiento. Alto riesgo del anexo III aplica desde 02/12/2027 [hecho: contexto legal]. |
| RGPD y LOPDGDD | Aplican. Hay que revisar la base jurídica y el encargo de tratami

**Arquitecto de procesos** · 2026-11-17 20:07

**Entrega: Propuesta de proceso de referencia: siniestros en corredurías**

# Apertura de siniestros en corredurías: propuesta para decidir el proceso de referencia

**Estado:** borrador para decisión de los socios antes del 22/11/2026. No validado con ningún responsable de correduría. La revisión de Calidad está pendiente: este documento no la da por hecha. Nada de esto es asesoría jurídica.
**Ruta prevista:** `processes/seguros-apertura-siniestros/README.md`

Convención:
- **Hecho:** consta en las secciones del repositorio facilitadas para este encargo. Se cita la ruta.
- **Hipótesis:** razonable, sin validar.
- **Propuesta:** lo que Varios recomienda decidir.
- **[POR CONFIRMAR]:** no consta en el material facilitado. No se inventa.

## Conclusión

La apertura de siniestros es un buen candidato a proceso de referencia. Tiene riesgo medio y un flujo claro: correo, póliza, cobertura, apertura. La IA lee y extrae. Las reglas comprueban póliza y cobertura. El tramitador aprueba cada apertura. Los partes con lesiones salen del flujo automático.

Hoy no hay ninguna cifra ni paso actual confirmado. El AS-IS es una hipótesis para las conversaciones de validación. La línea base de cliente está entera en [POR CONFIRMAR]. Todo el trabajo se hace con datos inventados.

## Decisión que se pide a los socios

1. Confirmar este proceso como referencia (D-011, "por confirmar en S0").
2. Decidir el ramo de partida [POR CONFIRMAR]. Hipótesis: un solo ramo sin lesiones, por ejemplo hogar o comercio. Los casos cubren varios ramos para probar las trampas. Si se elige un ramo único, hay que ajustarlos.
3. Revisar el reparto IA, reglas y persona (condiciona el CEO limitado de S4).
4. Fijar los umbrales de métricas marcados [POR CONFIRMAR].
5. Decidir el criterio ante póliza caducada: escalar o rechazar [POR CONFIRMAR].

## Hechos del repositorio

Constan en las secciones del cerebro facilitadas para este encargo:

- Proceso de referencia por confirmar en S0 [docs/10-plan-12-semanas.md › Objetivo a 12/02/2027].
- Caso A: correduría, siniestros por correo, riesgo medio. La IA lee y extrae. Las reglas comprueban póliza y cobertura. Los partes con lesiones salen del flujo automático. El tramitador aprueba cada apertura. Una fecha ambigua se marca para revisión [docs/12-simulacion.md › Casos].
- Control A (18/12/2026) y control B (15/01/2027), con sus criterios [docs/10-plan-12-semanas.md › Controles de paso].
- Los 12 pasos del CEO [docs/12-simulacion.md › Los 12 pasos].
- Estado: 0 clientes, 0 líneas de código. Ningún dato real en todo el periodo [CLAUDE.md › Contexto rápido].
- El proceso figura como "primer candidato (ejemplo, sin validar)" [processes/README.md › Catálogo de procesos].

**Nota para Calidad:** las rutas anteriores proceden del resumen del cerebro incluido en el encargo. Calidad indica que no las encuentra en su material de referencia. Hasta que se verifique su contenido literal en el repositorio, los controles A y B (20 casos, 5 trampas, tests de separación en verde, 20 siniestros recorriendo el flujo) deben leerse como **[POR CONFIRMAR]** en sus detalles. Lo mismo vale para el examen de 50 casos en S9 y su umbral de aprobación, que está por decidir.

## Proceso, sector y responsable

- **Proceso:** apertura de siniestros a partir de comunicaciones recibidas por correo.
- **Sector:** seguros, correduría.
- **Ramos cubiertos:** [POR CONFIRMAR].
- **Aseguradoras y vía de apertura** (portal, correo u otra): [POR CONFIRMAR].
- **Responsable en el cliente:** [POR CONFIRMAR]. Hipótesis: el responsable de siniestros o el tramitador jefe.

## AS-IS (hipótesis, sin validar)

El repositorio no describe el proceso actual. Los pasos guían las conversaciones de validación. Ninguno está confirmado.

| # | Paso actual | Quién (hipótesis) | Estado |
|---|---|---|---|
| 1 | Llega un correo con la comunicación del siniestro | Persona | [POR CONFIRMAR] |
| 2 | Alguien lee el correo y los adjuntos | Persona | [POR CONFIRMAR] |
| 3 | Se identifica al asegurado y la póliza | Persona | [POR CONFIRMAR] |
| 4 | Se comprueba vigencia y cobertura | Persona | [POR CONFIRMAR] |
| 5 | Se piden los datos o documentos que faltan | Persona | [POR CONFIRMAR] |
| 6 | Se abre el siniestro en el sistema de la correduría o de la aseguradora | Persona | [POR CONFIRMAR] |
| 7 | Se avisa al asegurado y se archiva | Persona | [POR CONFIRMAR] |

**Cifras actuales:** volumen mensual, porcentaje por correo, tiempo por caso, tiempo activo, porcentaje de datos incompletos, errores frecuentes, porcentaje con lesiones y número de tramitadores. Todo [POR CONFIRMAR].

**Excepciones:**
- Constan en el caso A: partes con lesiones y fecha ambigua.
- Hipótesis, todas [POR CONFIRMAR]: póliza no localizada, caducada o con impago; cobertura dudosa; duplicado; correo sin adjuntos o ilegible; correo que no es un siniestro; varios hechos o datos contradictorios; comunicante sin legitimación.

## TO-BE (propuesta)

Sigue los 12 pasos [docs/12-simulacion.md › Los 12 pasos].

| # | Paso | Quién | Qué pasa |
|---|---|---|---|
| 1 | Entra la petición | Reglas | Llega el correo. Se identifica remitente y correduría. Si no se reconoce, se pregunta o se rechaza. Marca de hora de entrada. |
| 2 | Entender | IA | Extrae intención, tipo de siniestro, fecha, asegurado y póliza. Cada campo se marca como confirmado, inferido o desconocido. |
| 3 | Preguntar lo que falta | IA redacta, persona envía | No inventa datos. El tramitador aprueba el envío. |
| 4 | Clasificar y riesgo | Reglas + IA | Las reglas detectan indicios de lesiones y apartan el caso. Una fecha ambigua se marca. Riesgo del caso: medio. |
| 5 | Consultar conocimiento | Reglas | Permisos antes de buscar. Otros clientes, bloqueados. |
| 6 | Hacer el plan | IA | Tareas con dependencias, cada una marcada IA, reglas o persona. |
| 7 | Asignar | Reglas | Departamento de siniestros, especialista de sector y herramientas mínimas. |
| 8 | Aprobaciones | Persona | El tramitador aprueba cada apertura. |
| 9 | Ejecutar | Motor de procesos | Póliza y cobertura, por reglas. En la demo, la apertura es simulada. Marca de hora de apertura. |
| 10 | Control de calidad | Reglas + persona | Si algo falla, se marca, no se corrige a ciegas. Muestreo humano [POR CONFIRMAR el porcentaje]. |
| 11 | Entregar | Reglas | Resultado con evidencias y límites: qué se extrajo, qué se comprobó, qué queda pendiente. |
| 12 | Registro y aprendizaje | Reglas + persona | Todo auditado. Lo aprendido entra como borrador y lo aprueba una persona. |

**Ajuste de diseño (propuesta, para que lo revise Juan).** Las lesiones deben detectarse antes de que la IA lea los adjuntos. Si no, la IA ya habría procesado datos de salud al apartar el caso. La detección es una regla previa, sobre asunto, texto y tipo de adjunto. Un caso con indicios de lesiones no se lee con IA y no se guarda texto clínico en el registro. Si se conserva el correo original y dónde: [POR CONFIRMAR].

**Reparto:**
- **IA:** leer y extraer, redactar preguntas, proponer el plan.
- **Reglas:** identificar al cliente, comprobar póliza y cobertura, detectar lesiones, controlar permisos, asignar, registrar.
- **Persona:** aprobar cada apertura, enviar comunicaciones externas, resolver fechas ambiguas, tramitar los partes con lesiones, decidir los casos escalados.

### Reglas de negocio del TO-BE

| # | Regla | Origen |
|---|---|---|
| 1 | La IA lee y extrae. No decide la cobertura. | Hecho (caso A) |
| 2 | Las reglas, no la IA, comprueban póliza y cobertura. | Hecho (caso A) |
| 3 | Un parte con lesiones o datos de salud sale del flujo automático. | Hecho (caso A) |
| 4 | Una fecha ambigua se marca para revisión y no se infiere. | Hecho (caso A) |
| 5 | Sin número de póliza o no localizada: PREGUNTAR. | Hipótesis |
| 6 | Fecha fuera de vigencia: revisión, no apertura automática. | Hipótesis |
| 7 | Póliza suspendida, anulada o con prima pendiente: revisión. | Hipótesis |
| 8 | Hecho que no encaja en una garantía o toca una exclusión: revisión. | 

**Arquitecto de procesos** · 2026-11-17 22:23

**Entrega: AS-IS de apertura de siniestros · Atalaya**

## Mapa AS-IS · Apertura de siniestros · Atalaya (ficticia)

**Estado:** borrador para revisión de un socio y de Calidad. No enviado. Nada de esto es asesoría jurídica. Todo dato de Atalaya es inventado (D-011).

## Resumen

**Conclusión:** el proceso actual tiene ocho pasos (P0 a P7) y ocho actores. El tiempo total lo dicen las personas de Atalaya (25 a 40 minutos de trabajo activo, más 2 o 3 días de espera por documentación). Ningún tiempo por paso está medido. El dolor se concentra en pedir documentación (ir y volver), copiar al portal de cada aseguradora y avisar al cliente.

Hay siete excepciones catalogadas (E1 a E7). Cinco tienen ruta nombrada en las notas: E1, E2, E3, E4 y E6. E5 aparece con ejemplos, pero las notas no dicen quién la decide ni qué ruta sigue. Los duplicados (E7) no constan en el material: su ruta y su frecuencia son DESCONOCIDAS.

**Convención:**
- **DICHO:** lo afirma una persona de Atalaya en las notas o la ficha, con su ruta. No es medición.
- **ESTIMADO:** cálculo propio con base declarada. En este borrador no hay ninguno.
- **DESCONOCIDO:** no consta.
- **HECHO / HIPÓTESIS / PROPUESTA / [POR CONFIRMAR]:** como en entregas anteriores.

**Sobre las fuentes:** solo he leído los extractos facilitados en este encargo. Su literalidad frente al repositorio es [POR CONFIRMAR]. La muestra de 15 siniestros (`03-muestra-de-siniestros.csv`) llega cortada en AT-0009, así que los ejemplos son solo los que constan. No calculo frecuencias sobre la muestra: 15 casos inventados no representan nada.

Las entregas «Claves del sector seguros para Atalaya», «Mapa de obligaciones RGPD, IA y corredor» y «Guiones de diagnóstico de apertura de siniestros (Atalaya)» constan en el histórico del encargo. No tengo su ruta en el repositorio y no las uso como fuente de datos. Las menciono solo como destino de lo que queda [POR CONFIRMAR].

## 1. Inicio, fin y objetivo

| Elemento | Contenido | Estado y fuente |
|---|---|---|
| Evento de inicio | El cliente comunica un siniestro (teléfono, correo, WhatsApp, portal o comercial) | HECHO. `02-notas-del-proceso-actual.md › Cómo llegan los siniestros` |
| Evento de fin | Número de siniestro de la aseguradora registrado, expediente abierto y cliente avisado | HECHO. `02-notas-del-proceso-actual.md › Pasos que describen las tramitadoras`, pasos 6 y 7 |
| Objetivo medible | Reducir el tiempo de apertura y los partes rehechos | PROPUESTA. Métrica y objetivo: [POR CONFIRMAR] con Métricas y con el contrato firmado |
| Volumen | Unos 320 al mes, con picos de más de 600 tras temporales | DICHO. `01-ficha-del-cliente.md › El problema, contado por la dirección` |
| Canales | Teléfono 40 %, correo 35 %, WhatsApp 15 %, portal 5 %, comercial 5 % | DICHO por la directora. `02-notas-del-proceso-actual.md › Cómo llegan los siniestros`. No medido. No se usa como objetivo |
| Alcance | Autos, hogar, comercio, flotas y RC. Recepción hasta aviso al cliente | HECHO. Ficha del proyecto |
| Fuera de alcance | Tramitación posterior, peritaciones, pagos, cobertura o rehúse, lesionados y salud | HECHO. Ficha del proyecto |

## 2. Carriles

| Carril | Quién es | Qué hace en el proceso | Fuente |
|---|---|---|---|
| Cliente | Tomador o asegurado | Comunica, aporta documentación, recibe el aviso | Notas, pasos 1 a 7 |
| Tramitador | Persona del departamento de siniestros (9 personas, DICHO) | Lleva la apertura en el camino normal | `01-ficha-del-cliente.md › Quiénes son`; notas, pasos |
| Tramitador senior | Tramitadora senior | Recibe siempre los lesionados | Notas › Excepciones |
| Directora de siniestros | Dueña del proceso | Decide en sospecha de fraude | Notas › Excepciones; ficha del proyecto |
| Cartera | Departamento de cartera y emisión (8 personas, DICHO) | Se consulta antes de abrir si hay impago o baja | Notas › Excepciones; ficha › Quiénes son |
| Aseguradora | Seis aseguradoras principales, «A» a «F», y una docena ocasionales (DICHO) | Recibe el alta y devuelve número de siniestro o rechazo | `01-ficha-del-cliente.md › Quiénes son`. Que devuelva número o rechazo: notas, pasos 5 y 6, y «Lo que les duele» |
| Programa de gestión | Producto comercial genérico de la correduría | Clientes, pólizas, recibos, expedientes | `04-sistemas-y-restricciones.md › Sistemas que usan hoy` |
| Portal | Portal web de cada aseguradora | Alta y seguimiento. Sin API conocida | `04-sistemas-y-restricciones.md › Sistemas que usan hoy` |

Otros sistemas: buzón compartido «siniestros@», WhatsApp Business (una línea, sin integración) y centralita (sin grabación). Fuente: `04-sistemas-y-restricciones.md › Sistemas que usan hoy`.

## 3. Diagrama por carriles (texto para maquetar)

```
Cliente          : [Comunica] ------------------------------> [Aporta lo que falta (P4)] -------------------> [Recibe aviso (P7)]
Tramitador       : P0 Recepción -> P1 Identificar -> P2 Vigencia/garantía -> P3 Plazo -> P4 Pedir docs -> P5 Alta portal -> P6 Registrar -> P7 Avisar
Programa gestión :                 (P1 búsqueda)     (P2 condiciones)                                     (P5 origen)       (P6 expediente)
Portal           :                                                                                         (P5 destino)
Aseguradora      :                                                                                         (nº siniestro o rechazo)
Cartera          :                                   [E4 impago/baja: se habla antes de abrir]
Tramitador senior: [E1 lesionados: recibe el caso]   [E6 empresa varios implicados: quien conoce la cuenta]
Directora        : [E3 sospecha de fraude: decide]
```

Decisiones en el camino:
- **D1 tras P1:** ¿se identifica cliente y póliza? Si no, se vuelve a pedir datos al cliente (hipótesis de flujo; las notas solo dicen que a veces cuesta encontrarla).
- **D2 tras P2:** ¿póliza en vigor y garantía existe? Con impago o baja, se habla con cartera (E4). Si la garantía no existe: [POR CONFIRMAR] quién decide y qué se comunica. Las notas no lo dicen.
- **D3 tras P3:** ¿en plazo? Si no, se anota (notas, paso 3). Qué pasa después: [POR CONFIRMAR].
- **D4 tras P4:** ¿documentación completa? Si no, se repite la petición (hipótesis de flujo derivada de «ir y volver»).
- **D5 tras P5:** ¿la aseguradora acepta el alta? Si devuelve el parte rechazado por un dato mal puesto, se rehace (notas › Lo que les duele; ficha).

## 4. Tabla de pasos

Todos los tiempos por paso son **DESCONOCIDO** salvo que se indique otra cosa. Atalaya reconoce que no los mide (`02-notas-del-proceso-actual.md › Lo que no saben`). El tiempo total es DICHO: 25 a 40 minutos de trabajo activo, más 2 o 3 días de espera por documentación (`01-ficha-del-cliente.md › El problema`).

| Paso | Rol | Sistema | Entrada | Salida | Tiempo | Problemas | Ruta |
|---|---|---|---|---|---|---|---|
| P0 Recepción del aviso | Tramitador (o comercial que reenvía) | Centralita, buzón «siniestros@», WhatsApp Business, portal del cliente | Aviso del cliente en cualquier canal | Notas del aviso. Por teléfono, en papel o documento; WhatsApp, reenviado a mano al correo | DESCONOCIDO | Correo con adjuntos torcidos o solo «me han dado un golpe, llamadme» (DICHO, notas › Cómo llegan). Notas en papel que luego se pasan al programa (DICHO, ídem). Centralita sin grabación (`04`). Tras un temporal, «los lunes entramos a 140 correos» (DICHO, notas › Lo que les duele) | Camino normal. Excepciones desde aquí: E1 a E7 |
| P1 Identificar cliente y póliza | Tramitador | Programa de gestión | Nombre, DNI, matrícula o número de póliza | Cliente y póliza localizados | DICHO: «a veces tardamos 5 minutos solo en encontrarla» si el cliente no da la póliza (notas, paso 1). Resto: DESCONOCIDO | El cliente no siempre da la póliza (AT-0001: da la matrícula, no la póliza). Posibles duplicados de cliente o de siniestro: DESCONOCIDO | Si no se localiza: volver al cliente (hipótesis). Duplicado: E7 |
| P2 Comprobar vigencia y garantía | Tramitador | Pro
