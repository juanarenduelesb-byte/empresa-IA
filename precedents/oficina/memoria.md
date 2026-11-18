<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Memoria de la oficina

Lo que la oficina ha aprendido: precedentes, lecciones, correcciones y decisiones de los socios. Lo lee el cerebro.

## Correccion (2)

### 2026-11-17 · Cambio en «AS-IS · Apertura de siniestros · Atalaya (ficticia)»

El socio pidió: hazlo perfecto hasta que calidad de el okay

_Agente: Arquitecto de procesos_

### 2026-11-17 · Corrección a IA y evaluación: haz eso que propones

Encargo «Reunión: IA y evaluación y Seguridad». El socio pidió: haz eso que propones

_Agente: IA y evaluación_

## Decision (11)

### 2026-11-17 · Aprobado: AS-IS · Apertura de siniestros · Atalaya (ficticia)

Un socio aprobó el entregable «AS-IS · Apertura de siniestros · Atalaya (ficticia)» (Diagrama de proceso v2).

_Agente: Arquitecto de procesos_

### 2026-11-17 · Aprobado: Examen de 25 casos ficticios para Atalaya

Un socio aprobó la entrega.

_Agente: Datos de prueba_

### 2026-11-17 · Aprobado: Línea base y fichas de métricas · Atalaya

Un socio aprobó la entrega.

_Agente: Métricas_

### 2026-11-17 · Plan lanzado entero: Diagnóstico de apertura de siniestros · Atalaya (ficticia)

Los agentes se organizan por dependencias: cada uno hace un encargo a la vez y como mucho 4 a la vez.

_Agente: CEO digital_

### 2026-11-17 · Rechazado: AS-IS de apertura de siniestros · Atalaya

Un socio rechazó la entrega. Motivo: mejorar hasta que calidad no vea ningun problema

_Agente: Arquitecto de procesos_

### 2026-11-17 · Aprobado: Guiones de diagnóstico de apertura de siniestros (Atalaya)

Un socio aprobó la entrega.

_Agente: Validación_

### 2026-11-17 · Aprobado: Mapa de obligaciones RGPD, IA y corredor · Atalaya

Un socio aprobó la entrega.

_Agente: Legal y privacidad_

### 2026-11-17 · Aprobado: Claves del sector seguros para Atalaya

Un socio aprobó la entrega.

_Agente: Coordinación sectorial · Seguros_

### 2026-11-17 · Caso de práctica cargado: Diagnóstico de apertura de siniestros · Atalaya (ficticia)

Proyecto ficticio con 13 encargos en 4 fases. Datos inventados (D-011).

_Agente: CEO digital_

### 2026-11-17 · Aprobado: Acta de protección de la IA y examen de 50 casos

Un socio aprobó la entrega.

_Agente: CEO digital_

### 2026-11-17 · Aprobado: Guion de validación semanal: apertura de siniestros

Un socio aprobó la entrega.

_Agente: Jefe comercial_

## Leccion (9)

### 2026-11-17 · Lección: Examen de 25 casos ficticios para Atalaya

Antes de declarar un entregable completo, comprueba que cada caso tiene todos sus campos (entrada, datos esperados, decisión correcta y regla que prueba) dentro del texto entregado, y no des por hecho que una hoja o una tabla existe si no aparece. Describe solo lo que la entrega muestra de verdad, y marca como [POR CONFIRMAR] toda fuente, norma o plazo que no hayas leído en esta revisión.
Reutilizable: La convención de marcas (Hecho, Hipótesis, Propuesta, [POR CONFIRMAR] y los estados del resultado esperado: sin marca, inf., desc., confl.). La separación de la hoja de datos maestros en valores de prueba marcados como tales, con identificadores POL-FIC y matrículas FIC. El modelo de tipos de trampa tomado de la muestra (inyección, impago, no comunicar, duplicado, fuera de plazo). Y el enfoque de tabla de fuentes con columna de estado de verificación.
Evitar: No cierres una entrega truncada ni afirmes «25 filas en cada hoja» o «todos los casos con fuente» sin haberlo comprobado. No cites como leídas fuentes cuyo contenido no está en el contexto, ni des por cierto un texto legal citado de forma indirecta (LCS art. 16) ni el plazo de 7 días que de él deriva. No presentes el reparto de canales dicho de memoria como dato. No dejes reglas de rechazo o de plazo sin fuente de norma o de método marcada como tal.

_Agente: Datos de prueba_

### 2026-11-17 · Lección: Línea base y fichas de métricas · Atalaya

Antes de aceptar una corrección de Calidad, recalcula la cifra: en la pestaña 6 el intervalo de Wilson para 6 de 20 da aproximadamente 14,6 % a 51,9 %, así que el «15 % a 52 %» original era correcto y la corrección «13 % a 54 %» no lo era. Y no des por cerrada una entrega cuyo último texto queda cortado a mitad de frase.
Reutilizable: La estructura de la hoja: pestañas Supuestos, Volumen_canal, Volumen_ramo, Tiempo_paso, Esperas y Rehechos, con las columnas id, valor, unidad, tipo_dato (DICHO, ESTIMACIÓN, SUPUESTO, CALCULADO, CALCULADO con SUPUESTO, [POR CONFIRMAR]), fuente y quién confirma. La regla de que todo resultado que dependa de un SUPUESTO lleve la etiqueta «CALCULADO con SUPUESTO». Y el tratamiento de «más de 600» como suelo, con la etiqueta de pico indicando el suelo. Las fórmulas de carga mensual (=S01*S03/60, etc.) y el recuento explícito de cifras DICHO para la conclusión.
Evitar: No inventar cifras de coste por hora ni de mercado: se usa un SUPUESTO marcado (S08, S09) que se sustituye por el dato del cliente (S07). No presentar la media aritmética del rango como si fuera la media real. No afirmar que un ahorro es pequeño frente a un precio sin cifra ni precio cerrado; si no hay datos, va como HIPÓTESIS con [POR CONFIRMAR]. No escribir conclusiones con un recuento fijo de cifras ("solo tres") sin contar de verdad las etiquetas DICHO de la tabla. No entregar Markdown provisional como si fuera el .xlsx pedido, ni dejar métricas sin desarrollar: M3, M4 y M5 deben tener fórmula, fuente, exclusiones, línea base y objetivo propuesto antes de pasar a socios.

_Agente: Métricas_

### 2026-11-17 · Lección: AS-IS de apertura de siniestros · Atalaya

En mapas AS-IS sin medición, cada tiempo, dolor o frecuencia debe marcarse como DICHO, ESTIMADO o DESCONOCIDO con su fuente exacta, y un documento solo se da por terminado cuando tiene cierre, todas sus tablas completas y ninguna referencia a secciones inexistentes. Las citas a archivos que no se han podido verificar deben quedar [POR CONFIRMAR] en cada aparición.
Reutilizable: La convención de etiquetas DICHO / ESTIMADO / DESCONOCIDO / HECHO / HIPÓTESIS / PROPUESTA / [POR CONFIRMAR]; la estructura de ocho carriles con rol, sistema y fuente por actor; la tabla de pasos con columnas rol, sistema, entrada, salida, tiempo, problemas y ruta; el catálogo de excepciones con ruta nombrada o DESCONOCIDA; y la regla de no calcular frecuencias sobre muestras tan pequeñas como 15 casos.
Evitar: Presentar como hecho lo que solo consta como dicho (por ejemplo, que el dolor se concentra en pedir documentación, copiar al portal y avisar al cliente); dejar filas de tabla malformadas (celdas que no cuadran con la cabecera); remitir a secciones inexistentes; entregar sin sección de conclusiones ni lista de puntos por confirmar con responsable; y terminar el documento a mitad de la tabla de pasos.

_Agente: Arquitecto de procesos_

### 2026-11-17 · Lección: Guiones de diagnóstico de apertura de siniestros (Atalaya)

Un entregable de validación no puede marcar como HECHO ni citar como fuente algo que no tiene delante, ni afirmar que ha leído archivos que no se le han pasado. Antes de cerrar, hay que comprobar que el documento termina en su último apartado y que cada cifra tiene origen verificable o queda como HIPÓTESIS o [POR CONFIRMAR].
Reutilizable: La convención HECHO / HIPÓTESIS / PROPUESTA / [POR CONFIRMAR], con la columna de fuente o modo de comprobación. La estructura de guion de 30 minutos por bloques con minutos, pregunta y dato que mide. Las repreguntas neutras. La regla de no citar cifras durante la conversación y de no anotar datos personales ni números de póliza.
Evitar: Afirmar «solo he leído los extractos incluidos» sin adjuntarlos o marcarlos como pendientes. Atribuir cifras (25-40 min, 70 %, 40/35/15/5/5 %) a fuentes concretas sin que consten. Entregar con la tabla truncada. Contradecir el método de muestreo en el título y en la regla de corte. Usar «¿verdad que…?», «¿no sería mejor…?» o un cierre que proponga volver a hablar como siguiente paso comercial.

_Agente: Validación_

### 2026-11-17 · Lección: Mapa de obligaciones RGPD, IA y corredor · Atalaya

En un mapa de obligaciones, cada afirmación debe llevar fuente comprobada o la marca [POR CONFIRMAR], y el documento debe cerrarse con el número exacto de preguntas pedido antes de entregarlo. Un texto cortado o con citas no verificadas no pasa a socios aunque el contenido sea sólido.
Reutilizable: La convención Hecho / Hipótesis / Propuesta / [POR CONFIRMAR] con su definición al inicio; el aviso de que no es asesoría jurídica; la separación de fuentes directas (material recibido, con ruta) e indirectas (citadas por terceros, marcadas como no verificadas); la tabla por tema con columnas de análisis y estado; y el bloque de categorías especiales con motivos de exclusión, riesgo residual y pendientes.
Evitar: Citar rutas, cifras, casos o artículos que no se han abierto en el material; citar normas de memoria sin fuente primaria; dejar una norma sin ruta de fuente o sin marca [POR CONFIRMAR]; cerrar el documento sin terminar la última pregunta; y presentar un borrador sin revisar como listo para socios.

_Agente: Legal y privacidad_

### 2026-11-17 · Lección: Claves del sector seguros para Atalaya

Separa en filas distintas lo que consta en la fuente (hecho normativo) y lo que es práctica no contrastada, y atribuye cada definición o cifra solo a un documento que de verdad la contenga. Si no hay fuente, marca [POR CONFIRMAR]. Antes de entregar, comprueba que todos los casos y documentos citados se han leído o están marcados como pendientes de verificación.
Reutilizable: La convención Hecho / Hipótesis / Propuesta / [POR CONFIRMAR] con su leyenda al inicio. La tabla de norma con columnas 'Lo que dice el extracto', 'Fuente leída' y 'Estado'. La regla de que la columna de práctica de una correduría ficticia no es norma ni práctica del sector. La lista de lo que la IA no debe decidir (cobertura o rehúse, riesgo extraordinario, consecuencias de aviso tardío, envíos sin aprobación humana, datos de salud, consejo a asegurados, instrucciones incrustadas). La declaración de qué fuentes se han leído y cuáles no, con las anclas no enlazadas hasta confirmarlas.
Evitar: No mezclar una frase de práctica no sourced con un hecho normativo dentro de la misma celda. No atribuir definiciones de glosario a un extracto que solo trata otro punto (por ejemplo, LCS art. 16 para 'tomador' cuando solo recoge la comunicación del siniestro). No dar cifras internas sin citar el archivo y el apartado. No presentar como verificados casos o documentos que no se han abierto. No entregar un documento cortado a mitad de glosario sin indicarlo.

_Agente: Coordinación sectorial · Seguros_

### 2026-11-17 · Lección: Acta de protección de la IA y examen de 50 casos

Antes de entregar un acta, verifica que el texto está completo y que cada cita corresponde a material realmente facilitado; un extracto no basta para dar por cierto un hecho, y las fechas o decisiones que no puedas comprobar deben quedar como [POR CONFIRMAR]. Separa siempre hecho, hipótesis, propuesta y pendiente, como hizo la entrega.
Reutilizable: La convención de etiquetas (Hecho, Hipótesis, Propuesta, [POR CONFIRMAR]), la sección de acuerdos entre departamentos sin atribuirlos a los socios, la tabla de desacuerdos con posición y estado de cada parte, y la regla de informar qué casos pasan o no sin prometer un porcentaje general con 50 casos.
Evitar: Presentar como hechos citas a rutas de archivos que no se han abierto, inventar códigos de decisión (como D-013) antes de mirar DECISIONS.md, dar por buena una fecha que contradice el acta sin marcarla, suponer que un componente de S4 (el adaptador) puede usarse en S3, y entregar el texto truncado a mitad de frase.

_Agente: CEO digital_

### 2026-11-17 · Lección: Reunión: IA y evaluación y Seguridad

Al proteger un sistema de IA, la defensa principal es limitar lo que el modelo puede hacer y ver, no confiar en una regla de instrucciones. Los tests de aislamiento deben comprobar el contexto exacto que recibe el modelo, no solo la base de datos.
Reutilizable: Test automático que construye el contexto enviado al modelo para el cliente A y falla si aparece cualquier identificador del cliente B. Umbral de examen: cero fallos en aislamiento y acciones prohibidas, y en el resto análisis y corrección de cada fallo. Condición previa a datos reales: prueba de aislamiento con dos clientes ficticios. Registro de cada llamada al modelo (versión de instrucciones, modelo, resultado) para repetir exámenes. Salida validada contra esquema con campos confirmados, inferidos o desconocidos. Reparto de casos adversos: seguridad redacta, ingeniería ejecuta, negocio revisa el realismo. Plantilla de acta con estado de borrador, decisiones marcadas como propuesta y tabla de desacuerdos con hipótesis señaladas como no probadas.
Evitar: Prometer un porcentaje general de robustez con 50 casos; informar solo de qué casos pasan y cuáles no. Dar por suficiente una regla impuesta por el adaptador como defensa contra la inyección. Pasar a datos reales sin una prueba de aislamiento previa. Dejar tantos elementos [POR CONFIRMAR] sin responsable ni fecha, como fechas de reunión, ruta del repositorio, umbral y realismo de los casos. Presentar propuestas de los socios como decisiones tomadas antes de su aprobación.

_Agente: IA y evaluación_

### 2026-11-17 · Lección: Guion de validación semanal: apertura de siniestros

Al preparar un guion a partir de material de referencia, atribuye a la fuente solo lo que hayas visto literalmente en el material facilitado; si solo tienes un resumen, di que es un resumen y marca todo lo demás como [POR CONFIRMAR]. Cita el título del encargo tal como lo recibiste y marca como propuesta la duración y la estructura por bloques.
Reutilizable: La convención Hecho / Hipótesis / Propuesta / [POR CONFIRMAR] para separar lo verificado de lo supuesto. La tabla de 8 preguntas con tipo de dato, dato concreto buscado y forma de anotar. La regla de pedir ejemplos de un caso reciente antes que opiniones, y el criterio de anotar 'desconocido' como respuesta válida. La plantilla de acta con campos confirmado/inferido/desconocido y medida/estimada. Las normas de no pedir datos personales ni credenciales y de no afirmar plazos legales sin revisión.
Evitar: No presentar preguntas, pasos de un AS-IS ni repreguntas como si estuvieran tomados de un README del cerebro sin que su texto conste en el material. No declarar que las fuentes 'constan' cuando solo se ha visto un resumen. No dejar preguntas sobre qué decide la persona que puedan derivar en automatización (P7 y la 7), salvo que se reformulen para no vender. No presentar la duración de 30 minutos como dato del encargo.

_Agente: Jefe comercial_

## Precedente (9)

### 2026-11-17 · Examen de 25 casos ficticios para Atalaya

Encargo: Proyecto Atalaya (ficticio). Crea el examen del sistema: 20 siniestros inventados realistas (reparto por ramo y canal parecido al del cliente ficticio) y 5 trampas (instrucción escondida en el correo, fuera de plazo, póliza en impago, duplicado, petición de no comunicar a la aseguradora). Para cada caso: texto de entrada tal como llegaría, campos esperados (cliente, póliza, ramo, tipo, fecha de ocurrencia, aseguradora, datos que faltan), decisión correcta (abrir, pedir documentación, pasar a persona, Consorcio, rechazar instrucción) y qué regla prueba. Usa identificadores imposibles (POL-FIC-…).

Todo el caso es ficticio: no uses ni busques datos reales de ninguna correduría.
Objetivo: Crear un examen inventado de 20 siniestros y 5 trampas, con resultado esperado campo a campo, para el control A del plan.
Hecho por: Datos de prueba con el experto de Seguros y mediación
Calidad: no cumple: La entrega está truncada en la hoja «Resultado esperado», en mitad de la fila de N01 («…(inf. de «ay»). Faltan N01 completo y todas las filas de N02 a T05 en esa hoja. Arreglo: completar la hoja con los 25 casos, cada uno con sus campos esperados.; No hay decisión correcta ni regla que pruebe por caso dentro de la entrega. La conclusión dice que están en una hoja «Casos», pero esa hoja no aparece en el texto. El criterio exige estos dos campos para los 25 casos. Arreglo: incluir la tabla «Casos» completa (id, decision_correcta, regla_que_prueba, fuente o [POR CONFIRMAR]) dentro de la entrega.; La conclusión afirma «25 filas en cada hoja» y «todos los casos con su fuente o marcada», pero no es verificable en el texto recibido. Arreglo: cambiar la afirmación por lo que la entrega muestra de verdad, o completar las hojas antes de volver a revisar.; Las fuentes de ruta del cerebro (NOTAS-P, NOTAS-E, NOTAS-C, SIST, MUESTRA) y la guía «Guiones de diagnóstico» aparecen como leídas, pero su contenido no está en el contexto de esta revisión. No se puede comprobar que las citas sean literales. Arreglo: marcar en la tabla de fuentes «contenido no verificado en esta revisión» o adjuntar el extracto usado, y dejar la literalidad como [POR CONFIRMAR] con Calidad.; Las reglas que prueban los casos T01 a T05 (rechazo de instrucciones ocultas, plazo, impago, duplicado, petición de no comunicar) no tienen fuente de norma o de método dentro de la entrega. La única base citada es el art. 16 de la LCS, que no está contrastado. Arreglo: marcar cada regla como «regla de método interno» o «[POR CONFIRMAR] con Legal y privacidad».
Entregable: Hoja de cálculo «Proyecto Atalaya (ficticio) · Examen de 25 casos de apertura de siniestros» v1

_Agente: Datos de prueba_

### 2026-11-17 · Línea base y fichas de métricas · Atalaya

Encargo: Proyecto Atalaya (ficticio). Construye la hoja de línea base: volumen mensual por canal y ramo, tiempo activo por paso (rango dicho por el cliente), esperas, partes rehechos, coste de una hora de tramitador como supuesto marcado. Añade las fichas de las 5 métricas del piloto (tiempo activo por apertura, tiempo hasta el acuse al cliente, % de partes sin corrección, % que pasa a persona, coste por caso) con fórmula, fuente, exclusiones, línea base y objetivo propuesto. Distingue dato dicho, estimación y supuesto.

Todo el caso es ficticio: no uses ni busques datos reales de ninguna correduría.
Objetivo: Dejar una hoja de línea base con volumen, tiempos, esperas, rehechos y coste, y cinco fichas de métricas del piloto con fórmula, fuente, exclusiones y objetivo propuesto, sin datos reales.
Hecho por: Métricas con el experto de Seguros y mediación
Calidad: no cumple: Formato: el criterio pide una hoja .xlsx con cada cifra etiquetada y las fórmulas visibles. La entrega es Markdown provisional y el propio texto dice que el .xlsx queda pendiente. Arreglo: maquetar la hoja en la plantilla de Varios, con una pestaña por bloque y las columnas tipo_dato y fórmula en cada celda calculada.; Faltan tres de las cinco fichas de métrica. El criterio exige fórmula, fuente, exclusiones, línea base marcada y objetivo propuesto para M1 a M5. Solo están M1 y M2, y la pestaña 8 termina cortada a mitad de frase en el criterio de M2 (“el de esp”). Arreglo: escribir M3 (% de partes sin corrección), M4 (% que pasa a persona) y M5 (coste por caso), y completar M2.; Cálculo erróneo en la pestaña 6. Para 6 rehechos de 20 con el método de Wilson al 95 %, el intervalo es aproximadamente 13 % a 54 %, no 15 % a 52 %. El método de Wald da 10 % a 50 %, que sí coincide. Arreglo: corregir la cifra, mantener la etiqueta ESTIMACIÓN y citar la fórmula usada.; Afirmación sin fuente en la pestaña 7: «El ahorro posible en apertura… es pequeño frente a un precio de piloto». No hay precio cerrado (el texto dice [POR CONFIRMAR]) ni cifra de ahorro comparable. Arreglo: eliminar la frase o marcarla como HIPÓTESIS con el cálculo que la sostiene y [POR CONFIRMAR] con los socios.; Incoherencia en la conclusión: dice que «solo hay tres cifras dichas» (320 casos, 25 a 40 min y 30 % de rehechos), pero la tabla de supuestos marca también como DICHO S02, S05 y S11, además de los porcentajes de canal y los 9 empleados. Arreglo: reescribir la conclusión con el recuento real de cifras DICHO.; Tratamiento de cifras de 'más de 600' (S02): las fórmulas de pico usan 600 como valor fijo. Está aclarado como suelo, pero la etiqueta de los resultados debe llevar también «CALCULADO con SUPUESTO» o «con suelo DICHO», no solo «CALCULADO sobre DICHO». Arreglo: ajustar la etiqueta en esas cinco filas.; Fuentes no verificadas: las rutas de los extractos y la plantilla ficha-kpi.md están citadas pero no leídas. La entrega lo declara y lo deja como [POR CONFIRMAR], lo cual es correcto. Antes de pasar a socios, Calidad debe cotejar citas y textos literales contra el repositorio.
Entregable: Hoja de cálculo «Proyecto Atalaya (ficticio) · Hoja de línea base y fichas de métrica» v1

_Agente: Métricas_

### 2026-11-17 · AS-IS de apertura de siniestros · Atalaya

Encargo: Proyecto Atalaya (ficticio). Con las notas de la sesión de arranque y la muestra de siniestros del proyecto, dibuja el AS-IS por carriles (cliente, tramitador, tramitador senior, directora, cartera, aseguradora, programa de gestión, portal). Para cada paso: rol, sistema, entrada, salida, tiempo (dicho o estimado, marcado), problemas. Cataloga las excepciones con su ruta: lesionados, Consorcio, fraude, impago, varios implicados, instrucciones raras del cliente, duplicados.

Todo el caso es ficticio: no uses ni busques datos reales de ninguna correduría.
Objetivo: Dibujar por carriles cómo se abre hoy un siniestro en Atalaya, con tiempos marcados por su origen y excepciones con su ruta, para preparar el TO-BE y el diagnóstico.
Hecho por: Arquitecto de procesos con el experto de Seguros y mediación
Calidad: no cumple: La fila E7 del catálogo de excepciones está rota: tiene 6 celdas frente a las 7 columnas de la cabecera y faltan la ruta, el ejemplo y los problemas. Hay que completarla con 'Ruta actual: DESCONOCIDA', 'Ejemplo en la muestra: no consta' y 'Problemas: sin registros para medir frecuencia'.; El documento termina en la sección 5 y no tiene cierre. Falta una sección final de conclusiones y puntos [POR CONFIRMAR] con su responsable.; La sección 4 remite a 'la sección 7' para medir el retrabajo, pero la sección 7 no existe. Hay que crearla con la métrica y la línea base, o cambiar la referencia.; La conclusión del resumen dice que 'el dolor se concentra en pedir documentación, copiar al portal y avisar al cliente' como afirmación de hecho. Debe marcarse como DICHO o HIPÓTESIS con su fuente, porque se basa en las notas y no en una medición.; Las referencias a archivos (02-notas..., 03-muestra..., 04-sistemas...) no se pueden comprobar desde este encargo. El borrador lo reconoce en 'Sobre las fuentes', pero las citas por ruta deben quedar [POR CONFIRMAR] en cada aparición, o reemplazarse por la fuente exacta una vez verificada.
Entregable: Diagrama de proceso «AS-IS · Apertura de siniestros · Atalaya (ficticia)» v1

_Agente: Arquitecto de procesos_

### 2026-11-17 · Guiones de diagnóstico de apertura de siniestros (Atalaya)

Encargo: Proyecto Atalaya (ficticio). Prepara dos guiones de 30 minutos (tramitadora y directora de siniestros) para medir lo que no se sabe: tiempo por paso, partes que se rehacen, datos que faltan, excepciones y quién decide. Preguntas abiertas sobre un caso reciente concreto, sin vender. Añade una plantilla de toma de notas y cómo cronometrar 20 aperturas reales en una semana (para cuando haya cliente real).

Todo el caso es ficticio: no uses ni busques datos reales de ninguna correduría.
Objetivo: Medir con datos dónde se va el tiempo al abrir un siniestro, cuántos partes se rehacen y qué excepciones aparecen, sin vender y con datos inventados.
Hecho por: Validación con el experto de Seguros y mediación
Calidad: no cumple: La entrega está truncada: termina a mitad de la hoja de registro en la tabla («Aseguradora»). Faltan la fila completa de la hoja, el cierre del método y cualquier control final. Se completa la hoja de registro y se revisa que el documento termine en su último apartado.; La sección «Fuentes y verificación» dice «Solo he leído los extractos incluidos en este encargo», pero el encargo que recibe Calidad no incluye extractos de 01, 02 ni 04 ni del README de la referencia. Esa afirmación no se puede comprobar y es falsa en el material disponible. Se corrige con dos opciones: adjuntar los extractos literales al encargo, o decir que los extractos se citan de memoria del histórico y marcar todo su contenido como [POR CONFIRMAR].; Varias filas están marcadas como HECHO con fuente en archivos del caso (por ejemplo «Atalaya no mide el tiempo real de cada paso», «la centralita no graba», «4 h al mes», «la dirección pide excluir lesionados»). Sin el material delante, no se puede verificar el HECHO. Según las reglas de la oficina, un dato no verificado no puede presentarse como hecho. Se rebajan a HIPÓTESIS o se marcan [POR CONFIRMAR] hasta que alguien contraste la fuente.; Las cifras «25 a 40 minutos», «70 % del tiempo es buscar, copiar y pedir» y «40/35/15/5/5 %» aparecen como citas de fuentes concretas (estimación de la directora, frase de la sesión simulada) que no constan en el encargo. Se mantienen solo como HIPÓTESIS y se indica explícitamente que su origen es [POR CONFIRMAR] con el autor de la fuente.; Incumplimiento de la regla propia del documento: «Todas las preguntas empiezan por Cuéntame, ¿Cómo, ¿Qué, ¿Cuándo o ¿Quién». Las repreguntas «¿Y eso cuánto tardó?», «¿Cuántas horas supuso eso?» y «¿Dónde consta ese dato?» incumplen esa regla. Se reformulan con uno de los inicios permitidos, por ejemplo «¿Cuánto tardó eso?» o «Cuéntame cuántas horas supuso eso».; Contradicción de método: el apartado 4 se titula «cronometrar 20 aperturas reales en una semana», pero admite que, si no se alcanzan 20, «se sigue hasta completarlos aunque se pase de la semana». Hay que elegir: o la semana es el límite y se anota la muestra incompleta, o el periodo se amplía y el título cambia. Se corrige el título o la regla y se indica el criterio de corte.; El cierre del guion A pregunta «¿Cómo te vendría mejor que volviéramos a hablar…?» y el guion B pregunta por el canal de contacto. Con el criterio de «sin vender» y de no abrir una propuesta comercial, la petición de volver a hablar debe formularse como curiosidad y no como siguiente paso. Se reescribe sin proponer ni anticipar un piloto.
Entregable: Documento «Guiones de validación y método de medición» v1

_Agente: Validación_

### 2026-11-17 · Mapa de obligaciones RGPD, IA y corredor · Atalaya

Encargo: Proyecto Atalaya (ficticio). Haz el mapa de obligaciones del proceso de apertura de siniestros con IA: RGPD (bases jurídicas posibles, datos de terceros, categorías especiales y por qué quedan fuera), Reglamento de IA (si el uso encaja o no en alto riesgo, transparencia, supervisión humana), obligaciones del corredor que afecten al proceso y lo que pediría un cliente regulado a Varios como proveedor. Termina con 10 preguntas cerradas para el abogado. Aviso de que no es asesoría jurídica.

Todo el caso es ficticio: no uses ni busques datos reales de ninguna correduría.
Objetivo: Preparar un mapa de obligaciones del proceso de apertura de siniestros con IA y 10 preguntas cerradas para el abogado, sin afirmar cumplimiento legal.
Hecho por: Legal y privacidad con el experto de Seguros y mediación
Calidad: no cumple: La entrega está cortada a mitad de la pregunta 3 («¿Puede Atalaya tratar datos de terceros contrario») y no contiene las 10 preguntas cerradas que exige el criterio. Solo constan 2 completas y 1 incompleta. Arreglo: completar el documento hasta exactamente 10 preguntas cerradas (sí o no) y revisar que el texto termina en la última.; Muchas afirmaciones marcadas como Hecho citan documentos del caso Atalaya que no aparecen en el material que tengo a la vista (01-ficha-del-cliente.md, 04-sistemas-y-restricciones.md, 03-muestra-de-siniestros.csv, la entrega «Claves del sector seguros» y el README de referencia). Incluyen cifras (320 siniestros al mes, picos de más de 600, 4 horas al mes) y casos (AT-0003, AT-0005, AT-0006, AT-0008, AT-0013). No puedo confirmar su contenido. Arreglo: confirmar la ruta y el texto de cada cita con el repositorio antes de enviarlo, o marcar como [POR CONFIRMAR] lo que no se haya comprobado.; La fila de transparencia del Reglamento de IA no tiene ruta de fuente para la norma, aunque el criterio exige cita de ruta para cada norma. Arreglo: añadir la ruta de la fuente del material o marcar explícitamente que no consta ninguna fuente de la norma.; El bloque de RGPD y LOPDGDD cita solo el resumen fijo para RGPD y brechas. La LOPDGDD aparece en el encabezado sin ninguna ruta ni marca de verificación en el cuerpo. Arreglo: añadir su ruta de fuente o marcarla como [POR CONFIRMAR].
Entregable: Documento «Mapa de obligaciones: apertura de siniestros con IA» v1

_Agente: Legal y privacidad_

### 2026-11-17 · Claves del sector seguros para Atalaya

Encargo: Proyecto Atalaya (correduría ficticia). Prepara las claves del sector para el resto del equipo: vocabulario del tramitador (parte amistoso, convenios entre aseguradoras, riesgo extraordinario, tomador, asegurado, perjudicado…), qué dice la norma sobre el plazo de comunicación y el papel del mediador (cita el cerebro: processes/referencia-seguros-apertura-siniestros y knowledge/sectores), práctica habitual frente a norma, excepciones frecuentes y lo que la IA no debe decidir nunca. Incluye un glosario en tabla.

Todo el caso es ficticio: no uses ni busques datos reales de ninguna correduría.
Objetivo: Preparar un documento de claves del sector asegurador (vocabulario, plazos, papel del mediador, excepciones y límites de la IA) con glosario en tabla, sin datos reales y sin asesoría jurídica.
Hecho por: Coordinación sectorial · Seguros con el experto de Seguros y mediación
Calidad: no cumple: Sección 1, fila 'Riesgos extraordinarios': la frase 'en la práctica, suele llegar por agentes y corredores' se presenta bajo 'Hecho según el extracto', pero el extracto solo dice que el mediador puede presentar la solicitud. Hay que separar esa frase, marcarla como práctica no sourced (Desconocida o [POR CONFIRMAR]) y dejar como hecho solo lo que consta.; Glosario, fila 'Tomador': la definición 'Quien contrata la póliza' se atribuye a 'Extracto README (LCS art. 16)', pero ese extracto solo recoge que el tomador comunica el siniestro. Hay que atribuir la definición a 'Uso general [POR CONFIRMAR]' o citar la fuente que la contenga.; Sección 2, párrafo final: las cifras de Atalaya (320 siniestros al mes, 25-40 minutos, 30 % de partes rehechos) no llevan referencia al documento del caso que las contiene. Hay que citar el archivo y el apartado, o marcarlas [POR CONFIRMAR].; Las referencias a casos concretos (AT-0001, AT-0003, AT-0005, AT-0006, AT-0008, AT-0009) y a documentos 01 a 04 no se pueden verificar desde esta revisión, porque el propio documento reconoce que no ha abierto la muestra completa. Hay que indicar que su contenido se ha comprobado o marcarlo como pendiente de verificación.
Entregable: Documento «Claves del sector: seguros y mediación en la apertura de siniestros» v1

_Agente: Coordinación sectorial · Seguros_

### 2026-11-17 · Acta de protección de la IA y examen de 50 casos

Encargo: quiero que hagas esto y lo apliques a nosotros:

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
- El plan vigente (D-0
Objetivo: Dejar por escrito la propuesta de protección de la IA y del examen de 50 casos, pendiente de decisión de los socios.
Hecho por: CEO digital
Calidad: no cumple: La entrega está cortada a mitad de la frase de la sección 8 ("no prueb"). La sección de riesgos queda incompleta y falta el cierre del documento.; Los hechos de las secciones 2 y 5 citan rutas y textos de docs/10-plan-12-semanas.md, DECISIONS.md, docs/12-simulacion.md y CLAUDE.md (fechas de S2 a S6, decisiones pendientes con fecha 22/01/2027, caso A de simulación, reglas de CLAUDE.md). Esos extractos no constan en este encargo de revisión, así que no puedo verificarlos. Deben contrastarse con los archivos originales antes de pasar a los socios.; El acta de origen decía que el umbral se decidía antes del control A. La entrega lo traslada a una fecha de DECISIONS.md (22/01/2027) que no puedo comprobar. Como el umbral y el control se fijan con fechas distintas, esta divergencia debe marcarse [POR CONFIRMAR] hasta validarla.; El código de decisión propuesto (D-013 o similar) no consta. La entrega lo marca bien como [POR CONFIRMAR], pero conviene no sugerir números concretos hasta mirar DECISIONS.md.
Entregable: Documento «Protección de la IA y examen de 50 casos: acta y aplicación a Varios» v1

_Agente: CEO digital_

### 2026-11-17 · Reunión: IA y evaluación y Seguridad

Encargo: como proteger nuestra IA
Objetivo: Acta de la reunión sobre: como proteger nuestra IA
Hecho por: IA y evaluación
Calidad: sin revisión

_Agente: IA y evaluación_

### 2026-11-17 · Guion de validación semanal: apertura de siniestros

Encargo: Prepara el guion de la conversación de validación de esta semana con un tramitador de siniestros de una correduría. Objetivo: confirmar o refutar el AS-IS hipotético de apertura de siniestros (processes/referencia-seguros-apertura-siniestros). Quiero 8 preguntas abiertas, sin vender nada, con qué dato concreto busca cada una (volumen, tiempo por caso, errores, excepciones) y cómo anotar la respuesta.
Objetivo: Preparar la conversación sin venta con un tramitador para confirmar o refutar el AS-IS hipotético de apertura de siniestros.
Hecho por: Jefe comercial con el experto de Seguros y mediación
Calidad: no cumple: La entrega afirma que las secciones del cerebro (README del proceso de referencia, docs/10-plan-12-semanas.md, docs/00-negocio.md, director-comercial.md) «constan en el material facilitado a este encargo como extractos». El material facilitado solo contiene un resumen del repositorio. No incluye el texto de esas secciones, así que esa afirmación es falsa.; Las 8 preguntas, los pasos A-H del AS-IS, el paso CCS y las repreguntas se presentan como tomados del README del proceso. Ese contenido no consta en el material. El aviso «[POR CONFIRMAR: cotejo]» reduce el riesgo, pero no corrige la atribución de fuente inventada.; La cita del encargo como «Guion y 8 preguntas de validación semanal» no coincide con el encargo recibido.; La pregunta 7 y la repregunta P7 («¿Hay algo que hoy decida usted y preferiría que decidiera otro...?») se acercan a una conversación sobre automatización. Esto roza el criterio de no vender, aunque la entrega ya marca la 7 para reformulación.; La duración de 30 minutos y la estructura por bloques son propuesta del borrador, no un dato del encargo. Conviene marcarlas como propuesta en la conclusión.
Entregable: Documento «Guion de validación: apertura de siniestros en una correduría» v1

_Agente: Jefe comercial_
