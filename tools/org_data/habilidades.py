"""Biblioteca de habilidades de los agentes de la oficina de Varios.

Una habilidad es una forma de trabajar que se puede repetir y revisar: cuándo se usa, los pasos,
la forma del resultado y la lista de control. Varios agentes pueden compartir la misma.
Es método, no hechos: cuando una habilidad necesita un dato externo, manda a buscarlo con fuente.
Estado: draft hasta que un socio la revise.
"""

H = []


def hab(**k):
    H.append(k)


# ---------------------------------------------------------------- transversales
hab(id="marca-varios", nombre="Voz y formato de Varios",
    cuando="En cualquier texto que vaya a leer un socio o, más adelante, un cliente.",
    pasos=["Escribe la conclusión en la primera frase; el razonamiento después.",
           "Frases cortas, voz activa, español de España. Tutea en textos comerciales; usted solo si el cliente lo usa.",
           "Cifras en formato español (6.500 €, 62 %, 12/02/2027) y siempre con su fuente o marcadas como ejemplo o hipótesis.",
           "Quita adjetivos que no se pueden medir (revolucionario, disruptivo, potenciar, sinergias, de vanguardia).",
           "Promete solo lo que se mide y di cómo se mide.",
           "Sin emojis ni exclamaciones. Títulos de sección con ##, listas cuando el lector va a comparar."],
    salida="El mismo contenido, más corto y verificable.",
    control=["¿La primera frase dice la conclusión?", "¿Cada cifra tiene fuente o etiqueta?", "¿Hay alguna promesa que no se pueda medir?"])

hab(id="hecho-hipotesis-propuesta", nombre="Separar hecho, hipótesis y propuesta",
    cuando="Siempre que se mezclen datos, suposiciones y recomendaciones (casi siempre).",
    pasos=["Marca cada afirmación como HECHO (con fuente: ruta del cerebro, documento del proyecto o fuente externa con fecha), HIPÓTESIS (lo que creemos y cómo lo comprobaríamos) o PROPUESTA (lo que recomendamos y por qué).",
           "Lo que falta y cambia la conclusión va como [POR CONFIRMAR] con quién puede confirmarlo.",
           "Nunca conviertas una hipótesis en hecho por repetirla."],
    salida="Texto con las tres capas distinguibles y una lista final de lo que está [POR CONFIRMAR].",
    control=["¿Hay algún número sin fuente que no esté marcado?", "¿La recomendación depende de una hipótesis no dicha?"])

hab(id="citar-cerebro", nombre="Leer y citar el cerebro",
    cuando="Antes de empezar cualquier encargo.",
    pasos=["Lee las secciones del cerebro que te pasa la oficina y busca precedentes parecidos en la memoria.",
           "Cita entre corchetes la ruta de cada sección que uses, por ejemplo [docs/10-plan-12-semanas.md].",
           "Si el cerebro contradice el encargo, dilo en la primera línea y no sigas a ciegas.",
           "Si una decisión de DECISIONS.md afecta al encargo, respétala o propón cambiarla de forma explícita."],
    salida="Una línea final «Usado del cerebro:» con las rutas.",
    control=["¿Hay rutas citadas?", "¿Se ha respetado lo decidido en DECISIONS.md?"])

hab(id="acta-reunion", nombre="Acta de reunión",
    cuando="Tras una reunión entre agentes, con un socio o con un interlocutor del cliente.",
    pasos=["Asistentes, fecha y objetivo de la reunión.",
           "Acuerdos (lo que se hará), decisiones (marcadas como propuesta si las deben aprobar los socios) y desacuerdos abiertos.",
           "Siguientes pasos: qué, quién, para cuándo.",
           "Lo que se dijo pero no se acordó no va como acuerdo."],
    salida="Acta de una página: Asistentes · Objetivo · Acuerdos · Decisiones propuestas · Desacuerdos · Siguientes pasos (tabla qué/quién/cuándo).",
    control=["¿Cada siguiente paso tiene responsable y fecha?", "¿Hay decisiones presentadas como tomadas sin serlo?"])

hab(id="decision-registro", nombre="Entrada de DECISIONS.md",
    cuando="Cuando algo cambia la estructura, el alcance, la tecnología, el precio o la forma de trabajar.",
    pasos=["Una decisión por entrada, con el siguiente código libre (D-0xx).",
           "Fecha, decisión en una frase, motivo, alternativas descartadas, riesgo y mitigación, alcance.",
           "Estado: propuesta salvo que un socio la haya aprobado de forma explícita.",
           "Si sustituye a otra, dilo y enlázala."],
    salida="Bloque Markdown listo para pegar en DECISIONS.md.",
    control=["¿Está marcada como propuesta?", "¿Dice qué alternativas se descartaron?"])

hab(id="contrato-de-tarea", nombre="Contrato de tarea",
    cuando="Al recibir un encargo, antes de planificar (docs/03).",
    pasos=["Objetivo en una frase y para quién es.",
           "Entradas autorizadas y datos: confirmados, inferidos y desconocidos.",
           "Proceso del catálogo (P01–P38) que aplica y riesgo de la tarea (bajo, medio, alto, crítico).",
           "Salida esperada, formato y criterio de aceptación verificable.",
           "Aprobaciones necesarias, límites y evidencias que se guardan."],
    salida="Ficha del encargo con esos campos.",
    control=["¿El criterio de aceptación se puede comprobar sin opinar?", "¿Lo desconocido que cambia la solución está preguntado?"])

hab(id="cinco-decisiones", nombre="Las cinco decisiones del CEO",
    cuando="Al decidir qué hacer con un encargo (docs/14).",
    pasos=["CONTINUAR si el objetivo está claro, el riesgo es aceptable y hay quien lo haga.",
           "PREGUNTAR si un dato desconocido cambia la solución, el coste o el riesgo: una sola pregunta concreta.",
           "ESCALAR si el riesgo es alto o hay una acción externa, financiera, legal o contractual.",
           "RECHAZAR si contradice CLAUDE.md, DECISIONS.md o la ley, o pide datos reales antes de L2.",
           "DERIVAR si lo debe hacer un profesional externo (abogado, gestor, asesor).",
           "Registra el motivo. Ante la duda entre dos riesgos, el más alto."],
    salida="Decisión + motivo + (si procede) la pregunta o el destinatario.",
    control=["¿El motivo es comprobable?", "¿Se ha elegido el riesgo más alto en caso de duda?"])

hab(id="plan-con-criterio", nombre="Plan con responsables y criterio",
    cuando="Para cualquier trabajo de más de un paso o más de un agente.",
    pasos=["Divide en entregables, no en actividades.",
           "Cada entregable: responsable, quién revisa, dependencias, fecha y criterio de aceptación.",
           "Ordena por dependencias; marca el camino crítico.",
           "Reserva tiempo para Calidad y para la aprobación de los socios."],
    salida="Tabla de plan: entregable · responsable · revisa · depende de · fecha · criterio.",
    control=["¿Hay algún entregable sin criterio?", "¿Se ve el camino crítico?"])

hab(id="consultar-historico", nombre="Consultar el histórico antes de hacer",
    cuando="Antes de cualquier entregable que se parezca a algo ya hecho.",
    pasos=["Busca en la memoria encargos, entregables, lecciones y correcciones parecidos.",
           "Reutiliza estructura y aprendizajes; nunca copies datos de otro cliente o proyecto.",
           "Di en el entregable qué reutilizas y qué cambias."],
    salida="Párrafo «Antecedentes» al principio del trabajo.",
    control=["¿Se ha aplicado la corrección que un socio hizo la última vez?"])

# ---------------------------------------------------------------- dirección
hab(id="plan-semanal", nombre="Seguimiento semanal del plan",
    cuando="Cada lunes y viernes del plan de 12 semanas (docs/10).",
    pasos=["Compara lo hecho con el «hecho cuando» de la semana.",
           "Semáforo por línea (producto, empresa y legal, comercial) con el motivo.",
           "Si hay retraso: qué se recorta de «si da tiempo», nunca las pruebas.",
           "Riesgos nuevos y quién los lleva."],
    salida="Nota de una página: estado, semáforos, recortes propuestos, riesgos, próximos pasos.",
    control=["¿Se ha propuesto recortar pruebas? (no debe)", "¿Cada riesgo tiene dueño?"])

hab(id="raid", nombre="Registro RAID",
    cuando="Al arrancar un proyecto y en cada revisión.",
    pasos=["Riesgos (probabilidad, impacto, mitigación, dueño).", "Supuestos (cómo y cuándo se validan).",
           "Incidencias abiertas (impacto y siguiente paso).", "Dependencias (de quién, para cuándo)."],
    salida="Cuatro tablas cortas.",
    control=["¿Algún supuesto lleva más de dos semanas sin validar?"])

hab(id="analisis-opciones", nombre="Análisis de opciones para decidir",
    cuando="Cuando los socios deben elegir entre alternativas.",
    pasos=["Define la pregunta y los criterios con su peso antes de mirar las opciones.",
           "Dos a cuatro opciones reales, incluida «no hacer nada».",
           "Coste, riesgo, reversibilidad y plazo de cada una, con fuente.",
           "Recomendación con la razón principal y qué haría cambiarla."],
    salida="Tabla de opciones y recomendación en cinco líneas.",
    control=["¿Los criterios se fijaron antes de puntuar?", "¿Está la opción de no hacer nada?"])

hab(id="ficha-conocimiento", nombre="Ficha de conocimiento",
    cuando="Al convertir algo aprendido en conocimiento reutilizable (knowledge/plantillas/ficha-conocimiento.md).",
    pasos=["Título, ámbito, estado (draft) y fecha de revisión.", "Contenido en afirmaciones cortas, cada una con fuente.",
           "Excepciones y caducidad (cuándo deja de valer).", "Enlaces a fichas relacionadas y a la que sustituye."],
    salida="Ficha en Markdown en estado draft.",
    control=["¿Cada afirmación tiene fuente?", "¿Hay fecha de caducidad o de revisión?"])

hab(id="contraste-fuentes", nombre="Contraste de fuentes",
    cuando="Cuando una afirmación es crítica (legal, cifra de mercado, fecha de entrada en vigor).",
    pasos=["Busca la fuente primaria (norma en el BOE o el DOUE, organismo oficial, documento del propio emisor).",
           "Comprueba fecha, vigencia y si hay modificaciones posteriores.",
           "Si las fuentes discrepan, muéstralo y no elijas en silencio.",
           "Registra la fuente en knowledge/fuentes con su fecha de consulta."],
    salida="Afirmación + fuente primaria + fecha + nivel de confianza.",
    control=["¿La fuente es primaria?", "¿Se ha comprobado si hay una versión posterior?"])

# ---------------------------------------------------------------- comercial
hab(id="cualificacion-oportunidad", nombre="Cualificación de oportunidad",
    cuando="Antes de dedicar horas a una cuenta (P31, knowledge/plantillas/ficha-oportunidad.md).",
    pasos=["Problema concreto y quién lo sufre.", "Volumen y coste actual del proceso (o cómo medirlo).",
           "Quién decide, quién paga y quién lo usa.", "Datos disponibles y restricciones regulatorias.",
           "Encaje con la oferta en cuatro fases y con el sector priorizado.", "Veredicto: seguir, esperar o descartar, con motivo."],
    salida="Ficha de oportunidad con veredicto.",
    control=["¿El problema lo ha dicho el cliente o lo suponemos?", "¿Se sabe quién decide?"])

hab(id="entrevista-descubrimiento", nombre="Entrevista de descubrimiento",
    cuando="Conversaciones de validación con quien hace el proceso (docs/10: una por semana desde S2).",
    pasos=["Objetivo: entender, no vender. 30 minutos.",
           "Cómo es hoy el proceso, paso a paso, con un caso reciente concreto.",
           "Volumen al mes, tiempo por caso, errores y retrabajos, excepciones.",
           "Herramientas, quién decide y qué pasa cuando sale mal.",
           "Cierre: qué cambiaría primero y si podemos volver a hablar."],
    salida="Guion con preguntas abiertas y, tras la conversación, notas con citas literales y cifras dichas.",
    control=["¿Hay alguna pregunta que sugiera la respuesta?", "¿Se ha hablado de producto? (no debe)"])

hab(id="sintesis-entrevistas", nombre="Síntesis de entrevistas",
    cuando="Tras tres o más conversaciones.",
    pasos=["Agrupa lo dicho por temas (dolor, volumen, excepciones, herramientas, decisor).",
           "Cuenta cuántas personas dijeron cada cosa; separa lo dicho de lo interpretado.",
           "Contradicciones y sorpresas.", "Qué hipótesis se confirman, cuáles caen y qué preguntar después."],
    salida="Tabla tema · quién lo dijo · cita · implicación; y lista de hipótesis con su estado.",
    control=["¿Se ha contado a cuántas personas les pasa?", "¿Las citas son literales?"])

hab(id="icp", nombre="Cliente ideal (ICP)",
    cuando="Para decidir a quién se contacta.",
    pasos=["Criterios medibles: sector, tamaño, regulación, proceso con volumen, madurez digital.",
           "Señales observables públicas para cada criterio.", "Criterios de exclusión.",
           "Puntuación sencilla y umbral."],
    salida="Tabla de criterios con señal, fuente y peso.",
    control=["¿Cada criterio se puede comprobar con una fuente pública?"])

hab(id="investigacion-cuenta", nombre="Investigación previa de una cuenta",
    cuando="Antes de una primera conversación.",
    pasos=["Solo fuentes públicas: web, registros oficiales, memoria anual, notas de prensa.",
           "Qué hace, tamaño, novedades, posible proceso con volumen.", "Hipótesis de dolor y pregunta de apertura.",
           "Fuente y fecha de cada dato. Nada de datos personales que no sean cargos públicos."],
    salida="Ficha de una página con fuentes.",
    control=["¿Algún dato sin fuente?", "¿Datos personales innecesarios?"])

hab(id="propuesta-diagnostico", nombre="Propuesta de diagnóstico",
    cuando="Cuando hay una oportunidad cualificada.",
    pasos=["Contexto del cliente con sus palabras.", "Objetivo y pregunta que responde el diagnóstico.",
           "Alcance: qué entra y qué no.", "Entregables y calendario de 3 semanas.",
           "Lo que necesitamos del cliente (personas, datos, accesos).",
           "Precio cerrado si está decidido; si no, [PRECIO POR DECIDIR].", "Siguiente paso y validez."],
    salida="Propuesta de dos o tres páginas con la marca de Varios.",
    control=["¿Hay algún precio inventado?", "¿El alcance dice lo que no entra?"])

hab(id="business-case", nombre="Caso de negocio",
    cuando="Para justificar un piloto o una fase ante quien paga.",
    pasos=["Línea base del proceso: volumen, tiempo, coste por caso, errores (medido o marcado como estimación).",
           "Escenario con el cambio: qué se automatiza y qué no.",
           "Ahorro y costes (licencias, construcción, operación) con fórmulas visibles.",
           "Tres escenarios (prudente, base, optimista) y punto de equilibrio.",
           "Supuestos en una tabla aparte."],
    salida="Hoja de cálculo con supuestos, cálculos y resumen; nunca cifras sin fórmula.",
    control=["¿Los supuestos están separados de los cálculos?", "¿El escenario base es defendible con datos?"])

hab(id="mensaje-posicionamiento", nombre="Mensaje y posicionamiento",
    cuando="Web, LinkedIn, presentación comercial.",
    pasos=["Para quién, qué problema, qué resultado medible, por qué nosotros, qué prueba lo respalda.",
           "Una idea por pieza.", "Prueba: demo, cifra medida o caso real con permiso; nunca testimonios inventados."],
    salida="Mensaje principal y tres variantes por canal.",
    control=["¿Hay alguna prueba inventada?", "¿Se entiende en diez segundos?"])

# ---------------------------------------------------------------- procesos
hab(id="mapeo-as-is", nombre="Mapa del proceso actual (AS-IS)",
    cuando="En la fase Diagnosticar.",
    pasos=["Evento de inicio y de fin.", "Pasos por rol (carriles), sistemas y documentos que se usan.",
           "Tiempos, volúmenes y esperas medidos o estimados (marcados).", "Excepciones y retrabajos con su frecuencia.",
           "Puntos de control y riesgos regulatorios."],
    salida="Diagrama de carriles + tabla de pasos (rol, sistema, entrada, salida, tiempo, problemas).",
    control=["¿Están las excepciones, no solo el camino feliz?", "¿Cada tiempo dice si es medido o estimado?"])

hab(id="diseno-to-be", nombre="Diseño del proceso nuevo (TO-BE)",
    cuando="En la fase Diseñar.",
    pasos=["Parte del AS-IS y del objetivo medible.",
           "Para cada paso decide: regla (código), IA (lenguaje y ambigüedad), persona (juicio y aprobación) o sistema.",
           "Dónde se aprueba, qué se registra y qué pasa si la IA duda.",
           "Rutas de excepción y vuelta atrás.", "Métrica de éxito y cómo se medirá."],
    salida="Diagrama TO-BE + matriz paso · quién lo hace · por qué · control.",
    control=["¿Algún paso con consecuencias lo decide la IA sola?", "¿La métrica es la firmada?"])

hab(id="matriz-ia-regla-persona", nombre="Matriz IA · regla · persona",
    cuando="Al decidir qué se automatiza.",
    pasos=["Regla si es determinista y verificable (cálculos, plazos, coberturas).",
           "IA si hay lenguaje o ambigüedad, siempre con confianza y salida estructurada.",
           "Persona si hay juicio, responsabilidad legal o impacto en el cliente final.",
           "Justifica cada asignación en una frase."],
    salida="Tabla de pasos con la asignación y su motivo.",
    control=["¿Se ha usado IA donde bastaba una regla?"])

hab(id="informe-as-is-to-be", nombre="Informe AS-IS / TO-BE",
    cuando="Al cerrar el diagnóstico o el diseño.",
    pasos=["Resumen ejecutivo de una página con la recomendación.", "AS-IS con cifras y dolores.",
           "TO-BE con la matriz IA · regla · persona.", "Riesgos, requisitos legales y de datos.",
           "Métrica, línea base y objetivo.", "Plan y siguiente fase."],
    salida="Documento de 8 a 12 páginas.",
    control=["¿El resumen se entiende sin leer el resto?"])

hab(id="casos-sinteticos", nombre="Casos de prueba inventados",
    cuando="Para construir el examen del sistema (docs/10: 20 casos + 30 nuevos).",
    pasos=["Todos ficticios y marcados como tales; nombres, pólizas y matrículas imposibles de confundir con reales.",
           "Reparto: casos normales, variantes frecuentes, casos límite y trampas (instrucciones escondidas, documentos que no cuadran).",
           "Para cada caso, el resultado esperado campo a campo y la decisión correcta.",
           "Etiqueta qué regla o excepción prueba cada caso."],
    salida="Tabla o JSON de casos con entrada, resultado esperado y etiqueta.",
    control=["¿Algún caso podría ser real?", "¿Hay trampas?", "¿Cada caso tiene resultado esperado?"])

hab(id="ficha-metrica", nombre="Ficha de métrica",
    cuando="Para cada métrica que se promete o se mide (knowledge/plantillas/ficha-kpi.md).",
    pasos=["Nombre, pregunta que responde y dueño.", "Fórmula exacta, unidades, fuente del dato y frecuencia.",
           "Exclusiones y cómo se tratan los casos raros.", "Línea base, objetivo y umbral de alerta."],
    salida="Ficha de métrica.",
    control=["¿Dos personas calcularían el mismo número?"])

hab(id="linea-base", nombre="Línea base",
    cuando="Antes de cambiar un proceso.",
    pasos=["Define el periodo y la muestra.", "Mide o estima con método explícito (muestreo, registros, cronometraje).",
           "Da el valor con su margen de error.", "Guarda los datos de origen."],
    salida="Tabla de línea base con método.",
    control=["¿Se ha dicho cómo se midió?"])

# ---------------------------------------------------------------- ingeniería
hab(id="spec-tecnica", nombre="Especificación para Claude Code",
    cuando="Cada tarea de construcción del plan.",
    pasos=["Objetivo y «hecho cuando».", "Archivos que se tocan y los que no.", "Pasos pequeños, cada uno con su test.",
           "Datos inventados que se usan.", "Riesgos de seguridad y cómo se prueba que no ocurren."],
    salida="Especificación de una página.",
    control=["¿Cada paso tiene un test?", "¿Usa solo el stack decidido?"])

hab(id="adr", nombre="Decisión de arquitectura",
    cuando="Al elegir una tecnología, un patrón o un cambio de modelo de datos.",
    pasos=["Contexto y fuerza que obliga a decidir.", "Opciones y consecuencias.", "Decisión y cómo se revierte.",
           "Registrarla también en DECISIONS.md si añade tecnología."],
    salida="ADR corto.",
    control=["¿Se puede revertir? ¿A qué coste?"])

hab(id="modelo-datos", nombre="Modelo de datos",
    cuando="Al diseñar tablas, migraciones o esquemas.",
    pasos=["Entidades y relaciones; cliente (tenant) en cada tabla de negocio.", "Auditoría: quién, qué, cuándo, desde dónde.",
           "Datos personales: minimización, retención y borrado.", "Migración reversible y probada desde cero."],
    salida="Diagrama, definición de tablas y migración.",
    control=["¿El tenant sale de la identidad, nunca del usuario?", "¿Hay retención definida?"])

hab(id="pruebas", nombre="Pruebas antes que código",
    cuando="Siempre en ingeniería.",
    pasos=["Escribe primero los tests del «hecho cuando».", "Incluye tests negativos (acceso cruzado, permisos, entradas malas).",
           "Cada fallo encontrado se convierte en test.", "CI en verde antes de pedir revisión."],
    salida="Tests en tests/ y su resultado.",
    control=["¿Hay tests negativos?"])

hab(id="evaluacion-modelos", nombre="Evaluación de modelos",
    cuando="Antes de elegir modelo o cambiar instrucciones (P23).",
    pasos=["Conjunto de examen fijo y versionado.", "Métricas: acierto por campo, omisiones, invenciones, coste y latencia.",
           "Compara contra la versión anterior; no cambies dos cosas a la vez.",
           "Pruebas de instrucciones escondidas (P20)."],
    salida="Informe de evaluación con tabla de métricas y decisión.",
    control=["¿El examen es el mismo que la vez anterior?"])

hab(id="ficha-integracion", nombre="Ficha de integración",
    cuando="Antes de conectar cualquier sistema.",
    pasos=["Qué sistema, qué operaciones (lectura o escritura) y por qué.", "Autenticación y dónde viven los secretos.",
           "Lista cerrada de acciones permitidas en la puerta de herramientas.", "Errores, reintentos, idempotencia y límites.",
           "Qué acción necesita aprobación humana."],
    salida="Ficha de integración.",
    control=["¿Deniega por defecto?", "¿Alguna escritura sin aprobación?"])

# ---------------------------------------------------------------- calidad, seguridad, legal
hab(id="criterio-aceptacion", nombre="Criterio de aceptación",
    cuando="Al abrir cualquier entregable.",
    pasos=["Qué tiene que contener y en qué formato.", "Cómo se comprueba sin opinar (lista de verificación).",
           "Qué lo invalida (dato inventado, promesa externa, falta de fuente)."],
    salida="Lista de verificación de 4 a 8 puntos.",
    control=["¿Se puede marcar sí o no en cada punto?"])

hab(id="revision-entregable", nombre="Revisión de un entregable",
    cuando="Antes de que un entregable llegue a los socios (P09).",
    pasos=["Compara con el criterio de aceptación punto por punto.", "Busca datos inventados, fuentes ausentes y promesas externas.",
           "Comprueba coherencia con DECISIONS.md y el plan.", "Devuelve con problemas concretos y cómo arreglarlos, o aprueba."],
    salida="Veredicto (cumple / no cumple) y lista de problemas.",
    control=["¿Cada problema dice dónde está y cómo se arregla?"])

hab(id="modelo-amenazas", nombre="Modelo de amenazas",
    cuando="Al diseñar una funcionalidad o integración.",
    pasos=["Activos, actores y fronteras de confianza.", "Amenazas por categoría (suplantación, manipulación, fuga, denegación, escalada, inyección de instrucciones).",
           "Controles existentes y huecos.", "Pruebas que demuestran cada control."],
    salida="Tabla amenaza · impacto · control · prueba.",
    control=["¿Se ha considerado la fuga entre clientes?", "¿Y la inyección de instrucciones en documentos?"])

hab(id="revision-riesgo-ia", nombre="Revisión de riesgo de IA y datos",
    cuando="Cuando un proceso usa IA sobre datos de personas o decisiones con efecto.",
    pasos=["Uso previsto y si encaja en algún supuesto de alto riesgo del Reglamento de IA (comprobar el anexo III con la fuente del cerebro).",
           "Datos personales y base jurídica a evaluar (RGPD); si hay categorías especiales.",
           "Supervisión humana, transparencia y registros.",
           "Preguntas concretas para el abogado.", "Aviso: orientativo, no es asesoría jurídica."],
    salida="Nota de riesgo de una o dos páginas con preguntas para el abogado.",
    control=["¿Se ha dicho que no es asesoría jurídica?", "¿Cada afirmación legal cita la norma?"])

hab(id="mapa-obligaciones", nombre="Mapa de obligaciones",
    cuando="Al entrar en un sector o un cliente regulado.",
    pasos=["Normas aplicables con referencia exacta y vigencia.", "Obligación concreta, a quién aplica (cliente o Varios) y evidencia que la demuestra.",
           "Fechas de entrada en vigor y periodos transitorios.", "Lo que está en tramitación, marcado aparte."],
    salida="Tabla norma · artículo · obligación · sujeto · evidencia · fecha.",
    control=["¿Se distingue lo vigente de lo anunciado?"])

# ---------------------------------------------------------------- administración
hab(id="preguntas-profesional", nombre="Preguntas para un profesional externo",
    cuando="Cuando algo lo debe decidir un gestor, abogado o asesor.",
    pasos=["Contexto mínimo necesario, sin datos innecesarios.", "Preguntas cerradas y numeradas.",
           "Qué documentos llevar.", "Qué decisión depende de cada respuesta."],
    salida="Lista de preguntas lista para enviar (la envía un socio).",
    control=["¿Las preguntas se pueden responder con sí, no o una cifra?"])

hab(id="coste-unitario", nombre="Coste unitario",
    cuando="Para saber cuánto cuesta un caso procesado o un cliente.",
    pasos=["Componentes: modelo (tokens), nube, licencias, horas de revisión humana.", "Precio de cada componente con fuente y fecha.",
           "Coste por caso en tres volúmenes.", "Límite de gasto y alerta."],
    salida="Hoja de cálculo con fórmulas.",
    control=["¿Cada precio tiene fuente y fecha?"])

hab(id="ficha-proveedor", nombre="Ficha de proveedor",
    cuando="Antes de usar un proveedor nuevo (knowledge/plantillas/ficha-proveedor.md).",
    pasos=["Qué servicio, qué datos tratará y dónde (región).", "Si usa los datos para entrenar y retención.",
           "Contrato de encargo de tratamiento y subencargados.", "Salida: cómo se recuperan los datos y se cambia de proveedor."],
    salida="Ficha de proveedor.",
    control=["¿Se ha comprobado el uso para entrenamiento en la fuente del proveedor?"])

# ---------------------------------------------------------------- sectores
hab(id="claves-sector", nombre="Claves del sector para un encargo",
    cuando="Cuando un encargo toca un sector (el experto habla antes que el agente).",
    pasos=["Vocabulario que el cliente usará y su significado.", "Normas que aplican, con fuente del cerebro (knowledge/sectores/) o [POR CONFIRMAR].",
           "Cómo se hace hoy habitualmente (práctica) frente a lo que exige la norma.",
           "Excepciones frecuentes y trampas.", "Lo que la IA no debe decidir en este sector."],
    salida="Nota de 10 a 20 líneas para el agente.",
    control=["¿Se distingue práctica de norma?", "¿Hay alguna obligación sin fuente?"])

hab(id="glosario-sector", nombre="Glosario del sector",
    cuando="Al empezar a trabajar un sector o un cliente.",
    pasos=["Término, definición corta, sinónimos del cliente, fuente.", "Términos que se confunden entre sí."],
    salida="Tabla de glosario.",
    control=["¿Hay definiciones con fuente?"])

HABILIDADES = H
