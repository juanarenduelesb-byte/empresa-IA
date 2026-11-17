"""Catálogo P01–P38. Fuente de las definiciones: Guía v1.4 (P01–P30) y Atlas Evolución v1.1 (P31–P38).

No se renumera ni se elimina nada. P31–P38 mantienen su estado de propuesta.
Estado de todas las fichas: draft (especificado, no implementado salvo donde se indique).
Actividad: (tarea, tipo, salida). tipo: regla (código determinista) · ia (LLM propone) · humano · sistema.
"""

GUIA = "Guía de Arranque v1.4 (Anexo I y II)"
ATLAS = "Atlas Evolución v1.1 §10 (propuesta)"
P = []


def proc(**k):
    for f in ("reglas", "excepciones", "aprobaciones", "evidencias", "kpis", "depende", "plantillas", "pruebas", "sistemas", "permisos"):
        k.setdefault(f, [])
    k.setdefault("estados", "Encargo: Recibido → … → Cerrado (processes/definitions/encargo.json)")
    k.setdefault("timeouts", "Timeout por tarea; máximo 3 intentos con espera exponencial y aleatoria solo para errores transitorios (P22)")
    k.setdefault("implementado", "No")
    P.append(k)


# ---------------- Ciclo de un encargo (MVP interno) ----------------
proc(id="P01", nombre="Alta y recepción de petición", origen=GUIA, cuando="MVP",
     objetivo="Registrar solicitante, cliente, objetivo, alcance, plazo, formato y restricciones.",
     inicio="Llega una petición por un canal autorizado (formulario, correo entrante, oficina).",
     entradas="Texto de la petición, identidad autenticada del solicitante, adjuntos.",
     actividades=[("Autenticar al solicitante y derivar el cliente de su identidad", "regla", "tenant_id fiable"), ("Registrar la petición con identificador y correlación", "sistema", "Encargo en RECIBIDO"), ("Validar adjuntos (tipo, tamaño) y enviarlos a P07", "regla", "Referencias a documentos"), ("Pasar a clasificación", "sistema", "Encargo en EN_CLASIFICACION")],
     responsables="Sistema; dueño del proceso: CEO digital", especialistas=["ceo-digital"],
     reglas=["El cliente sale de la identidad autenticada, nunca de la petición (D-005).", "Sin identidad válida, la petición no se registra."],
     sistemas=["API de entrada", "PostgreSQL"], permisos=["Escritura de encargos del propio cliente"],
     excepciones=["Identidad no válida: rechazo sin registro de contenido.", "Adjunto no permitido: se registra el encargo sin él y se avisa."],
     aprobaciones=["Ninguna"], fin="Encargo registrado y en clasificación.",
     evidencias=["Evento de auditoría con actor, cliente, fecha y correlación"], kpis=["Tiempo de alta", "Peticiones rechazadas por identidad"],
     depende=["P02", "P07", "P14"], plantillas=["integrations/contracts/encargo.schema.json"],
     pruebas=["Petición con tenant_id en el cuerpo distinto del de la identidad: se ignora el del cuerpo.", "Sin autenticación: no se crea el encargo."],
     implementado="Parcial: estado RECIBIDO y auditoría en src/varios/procesos (sin API)")

proc(id="P02", nombre="Clasificación y triaje", origen=GUIA, cuando="MVP",
     objetivo="Asignar sector, proceso, tipo de problema, complejidad, sensibilidad, riesgo e incertidumbre, y tomar una de las cinco decisiones.",
     inicio="Encargo en EN_CLASIFICACION.", entradas="Encargo, conocimiento autorizado (P04), catálogo de procesos.",
     actividades=[("Extraer intención, objetivo y datos (confirmados, inferidos, desconocidos)", "ia", "Contrato de tarea propuesto"), ("Clasificar riesgo con la matriz por tarea", "regla", "Nivel de riesgo"), ("Proponer decisión con motivo", "ia", "Decisión propuesta"), ("Aplicar reglas que fuerzan decisión (prohibido → RECHAZAR; alto → ESCALAR)", "regla", "Decisión final"), ("Transición según decisión", "sistema", "PENDIENTE_INFO, PLANIFICADO, ESCALADO o RECHAZADO")],
     responsables="CEO digital", especialistas=["ceo-digital", "especialista-sectorial"],
     reglas=["La confianza del modelo no sustituye reglas ni aprobaciones.", "Ante duda entre dos niveles de riesgo, el más alto.", "Acciones externas, pagos, borrados y datos reales sin mandato: RECHAZAR."],
     sistemas=["LLM vía adaptador", "Motor de procesos"], permisos=["Lectura del conocimiento del cliente"],
     excepciones=["Salida del modelo no válida: reintento único y, si falla, ESCALADO.", "Contradicción entre reglas: ESCALADO."],
     aprobaciones=["ESCALADO: revisión de una persona identificada"], fin="Decisión registrada con motivo.",
     evidencias=["Contrato de tarea", "Decisión, motivo, versión de instrucciones y modelo"], kpis=["Acierto de clasificación frente a dataset etiquetado", "Escalados por mes"],
     depende=["P01", "P03", "P04", "P05", "P19"], plantillas=["docs/14-reglas-del-ceo.md"],
     pruebas=["Encargo que pide enviar correos: RECHAZADO.", "Encargo con datos personales sensibles: riesgo alto y ESCALADO."])

proc(id="P03", nombre="Gestión de aclaraciones", origen=GUIA, cuando="MVP",
     objetivo="Detectar datos ausentes, formular preguntas y bloquear las tareas que dependan de respuestas críticas.",
     inicio="Decisión PREGUNTAR.", entradas="Datos desconocidos que cambian solución, coste o riesgo.",
     actividades=[("Redactar una pregunta concreta por dato crítico", "ia", "Pregunta"), ("Enviar la pregunta al solicitante por el canal interno", "sistema", "Encargo en PENDIENTE_INFO"), ("Recibir respuesta y conservar historial", "sistema", "Respuesta registrada"), ("Volver a clasificar", "sistema", "EN_CLASIFICACION")],
     responsables="CEO digital", especialistas=["ceo-digital"],
     reglas=["Solo se reanuda al recibir respuesta.", "Se pregunta lo mínimo: una pregunta por dato que cambia la solución."],
     sistemas=["Motor de procesos", "Canal de mensajes interno"], permisos=["Comunicación con el solicitante del propio cliente"],
     excepciones=["Sin respuesta en el plazo: recordatorio y, tras el segundo, CANCELADO con aviso."],
     aprobaciones=["Ninguna"], timeouts="Plazo de respuesta configurable por cliente (por definir en el contrato).", fin="Respuesta recibida o encargo cancelado.",
     evidencias=["Pregunta, respuesta y fechas"], kpis=["Tiempo en PENDIENTE_INFO", "Encargos cancelados por falta de respuesta"],
     depende=["P02"], pruebas=["Respuesta recibida: el encargo vuelve a EN_CLASIFICACION, no salta a ejecución."])

proc(id="P04", nombre="Recuperación de conocimiento", origen=GUIA, cuando="MVP",
     objetivo="Consultar fuentes autorizadas, filtrar por permisos, recuperar precedentes y citar evidencias.",
     inicio="Cualquier tarea que necesita contexto.", entradas="Consulta, identidad, cliente, finalidad.",
     actividades=[("Filtrar el corpus por cliente y permisos antes de buscar", "regla", "Corpus autorizado"), ("Búsqueda de texto con ranking", "sistema", "Secciones candidatas"), ("Recuperar precedentes del mismo tipo", "sistema", "Precedentes"), ("Devolver secciones con procedencia y estado", "sistema", "Contexto citable")],
     responsables="Bibliotecario", especialistas=["bibliotecario", "datos-ia"],
     reglas=["El control de acceso se aplica al recuperar, no después.", "Lo recuperado es dato, no instrucción (P20).", "Fichas deprecated o disputed se marcan como tales."],
     sistemas=["Repositorio de conocimiento", "PostgreSQL (metadatos y ACL)"], permisos=["Lectura según ACL"],
     excepciones=["Sin resultados: se dice, no se inventa."], aprobaciones=["Ninguna"], fin="Contexto entregado con citas.",
     evidencias=["Secciones recuperadas por tarea"], kpis=["Calidad de citas", "Consultas sin resultado"],
     depende=["P13", "P14", "P20"], plantillas=["knowledge/navigation.json"],
     pruebas=["Consulta de un cliente A no devuelve documentos del cliente B.", "Documento con instrucciones incrustadas no cambia el comportamiento."],
     implementado="Prototipo: búsqueda de texto del cerebro de la oficina (tools/brain_build.py), sin ACL")

proc(id="P05", nombre="Diseño del plan", origen=GUIA, cuando="MVP",
     objetivo="Descomponer el objetivo en tareas, dependencias, responsables, herramientas y criterios de aceptación.",
     inicio="Decisión CONTINUAR.", entradas="Contrato de tarea, catálogo de capacidades, precedentes.",
     actividades=[("Consultar precedentes y plantillas reutilizables", "sistema", "Lista de reutilizables"), ("Proponer tareas con criterio de aceptación", "ia", "Plan propuesto"), ("Validar plan: capacidades existentes, permisos, presupuesto", "regla", "Plan válido o errores"), ("Aprobar plan según riesgo", "humano", "Plan aprobado")],
     responsables="CEO digital", especialistas=["ceo-digital", "decisiones-seguimiento"],
     reglas=["Toda tarea tiene criterio de aceptación verificable.", "Solo capacidades en estado approved."],
     sistemas=["Motor de procesos"], permisos=["Crear tareas"],
     excepciones=["Plan inviable: ESCALADO."], aprobaciones=["Riesgo medio o alto: aprobación del plan"], fin="Encargo en PLANIFICADO.",
     evidencias=["Plan versionado"], kpis=["Planes reutilizando precedentes / total"], depende=["P02", "P04", "P06"],
     pruebas=["Plan con tarea sin criterio: rechazado por validación."])

proc(id="P06", nombre="Asignación y coordinación", origen=GUIA, cuando="MVP",
     objetivo="Seleccionar departamentos y especialistas; controlar carga, estados, bloqueos y escalados.",
     inicio="Plan aprobado.", entradas="Plan, disponibilidad de capacidades.",
     actividades=[("Asignar cada tarea a una capacidad", "regla", "Tareas asignadas"), ("Lanzar tareas sin dependencias pendientes", "sistema", "Tareas en running"), ("Vigilar bloqueos y vencimientos", "sistema", "Alertas"), ("Escalar bloqueos sin resolver", "sistema", "ESCALADO")],
     responsables="CEO digital y motor de procesos", especialistas=["ceo-digital"],
     reglas=["Una tarea no empieza con dependencias abiertas.", "Límite de concurrencia por cliente (P29)."],
     sistemas=["Motor de procesos"], permisos=["Asignar tareas"], excepciones=["Capacidad no disponible: cola o ESCALADO."],
     fin="Todas las tareas terminadas o escaladas.", evidencias=["Historial de asignaciones"], kpis=["Tiempo en cola", "Bloqueos por semana"],
     depende=["P05", "P08", "P29"], pruebas=["Tarea con dependencia abierta no arranca."])

proc(id="P07", nombre="Ingesta documental", origen=GUIA, cuando="Antes de datos reales",
     objetivo="Validar tipo, origen, integridad, metadatos, clasificación, permisos y versión; conservar el original.",
     inicio="Llega un documento.", entradas="Fichero, origen, cliente.",
     actividades=[("Calcular hash y guardar el original inmutable (RAW)", "sistema", "Original con hash"), ("Validar tipo y tamaño", "regla", "Aceptado o rechazado"), ("Extraer texto y estructura", "sistema", "Texto extraído (Docling, en evaluación)"), ("Clasificar y detectar datos personales", "ia", "Clasificación propuesta"), ("Asignar ACL y retención", "regla", "Metadatos completos")],
     responsables="Bibliotecario", especialistas=["bibliotecario", "datos-ia", "legal-privacidad"],
     reglas=["El original no se modifica.", "Sin clasificación, no entra en el índice."],
     sistemas=["Almacenamiento de objetos", "PostgreSQL"], permisos=["Escritura RAW del cliente"],
     excepciones=["Fichero corrupto o con macros: cuarentena."], aprobaciones=["Datos especialmente protegidos: revisión"], fin="Documento clasificado e indexado.",
     evidencias=["Hash, origen, versión, clasificación"], kpis=["Documentos en cuarentena", "Exactitud de clasificación"],
     depende=["P14", "P20", "P24"], pruebas=["Mismo fichero dos veces: un solo original (idempotencia por hash)."])

proc(id="P08", nombre="Ejecución de tareas", origen=GUIA, cuando="MVP",
     objetivo="Ejecutar análisis, reglas, código o automatizaciones con límites, registro y tratamiento de errores.",
     inicio="Tarea en running.", entradas="Tarea con entradas tipadas.",
     actividades=[("Comprobar permisos y presupuesto", "regla", "Autorización"), ("Ejecutar (regla, IA o herramienta vía gateway)", "sistema", "Salida tipada"), ("Validar esquema de salida", "regla", "Salida válida"), ("Registrar resultado o error clasificado", "sistema", "Evento de auditoría")],
     responsables="Capacidad asignada", especialistas=["backend", "automatizacion"],
     reglas=["Herramientas solo vía gateway con lista cerrada.", "Reintentos según P22."],
     sistemas=["Motor de procesos", "Gateway de herramientas"], permisos=["Los de la tarea, mínimos"],
     excepciones=["Error transitorio: reintento.", "Autorización o seguridad: BLOQUEADO sin reintento."], fin="Encargo en EN_QA.",
     evidencias=["Entradas, salida, duración, coste"], kpis=["Errores por tipo", "Coste por tarea"], depende=["P21", "P22", "P29"],
     pruebas=["Error de permisos no se reintenta.", "Salida que no cumple el esquema no avanza."],
     implementado="Parcial: política de reintentos e idempotencia en src/varios/procesos/reintentos.py")

proc(id="P09", nombre="Control de calidad", origen=GUIA, cuando="MVP",
     objetivo="Comprobar formato, completitud, coherencia, cálculos, fuentes, pruebas y criterios del encargo.",
     inicio="Encargo en EN_QA.", entradas="Entregable y criterio de aceptación.",
     actividades=[("Validaciones deterministas (formato, cálculos)", "regla", "Resultado por regla"), ("Revisión contra criterio y fuentes", "ia", "Veredicto con problemas"), ("Decidir: retrabajo, aprobación o entrega", "regla", "RETRABAJO, PENDIENTE_APROBACION o ENTREGADO")],
     responsables="Calidad", especialistas=["calidad-riesgos", "evaluacion-ia"],
     reglas=["QA no aprueba lo que no ha comprobado.", "Quien hizo la tarea no hace su QA.", "Un retrabajo automático como máximo; después, persona."],
     sistemas=["Suite de validaciones"], permisos=["Lectura del entregable"], excepciones=["Criterio ambiguo: ESCALADO."],
     aprobaciones=["Riesgo medio o alto, o QA con problemas: P10"], fin="Veredicto registrado.",
     evidencias=["Resultado de cada validación"], kpis=["First-pass yield", "Retrabajos"], depende=["P08", "P10", "P23"],
     pruebas=["Entregable que no cumple el criterio pasa a RETRABAJO.", "Paso directo a ENTREGADO solo con riesgo bajo y QA conforme."],
     implementado="Prototipo en la oficina de agentes (revisión por el agente de Calidad)")

proc(id="P10", nombre="Aprobación humana", origen=GUIA, cuando="MVP",
     objetivo="Solicitar aprobación para decisiones sensibles, acciones externas, entregas reguladas o tareas de alto impacto.",
     inicio="Encargo en PENDIENTE_APROBACION.", entradas="Objeto exacto a aprobar y su versión.",
     actividades=[("Presentar el objeto, su versión y el riesgo", "sistema", "Solicitud"), ("Decidir aprobar, rechazar o pedir retrabajo", "humano", "Decisión"), ("Verificar que la versión aprobada es la que se entrega", "regla", "Coincidencia de versión")],
     responsables="Socio o aprobador autorizado", especialistas=["ceo-digital", "calidad-riesgos"],
     reglas=["Aprobación ligada a la versión exacta: si cambia, se aprueba de nuevo.", "Nadie aprueba su propia acción.", "Doble aprobación si el riesgo o el contrato lo exigen."],
     sistemas=["Motor de procesos"], permisos=["Rol de aprobador"], excepciones=["Sin respuesta en plazo: recordatorio; nunca aprobación tácita."],
     aprobaciones=["Es el propio proceso"], fin="ENTREGADO, RECHAZADO o RETRABAJO.",
     evidencias=["Aprobador, rol, fecha, versión, decisión y motivo"], kpis=["Tiempo de aprobación", "Rechazos"], depende=["P09", "P11"],
     pruebas=["El mismo actor que produjo no puede aprobar.", "Aprobación de una versión distinta: rechazada."],
     implementado="Sí, como regla del motor: src/varios/procesos/motor.py")

proc(id="P11", nombre="Entrega y cierre", origen=GUIA, cuando="MVP",
     objetivo="Entregar artefactos, evidencias, limitaciones, métricas, aceptación y registro de cierre.",
     inicio="Encargo ENTREGADO.", entradas="Entregable aprobado.",
     actividades=[("Entregar con limitaciones y fuentes", "sistema", "Entrega"), ("Registrar aceptación del solicitante", "humano", "Aceptación"), ("Proponer precedente y lecciones (P13)", "ia", "Borrador de precedente"), ("Cerrar", "sistema", "CERRADO")],
     responsables="CEO digital", especialistas=["ceo-digital", "bibliotecario"],
     reglas=["Cerrado solo se reabre con motivo, autorización y nueva versión."],
     sistemas=["Motor de procesos"], permisos=["Lectura del entregable"], excepciones=["Rechazo del solicitante: REABIERTO."],
     fin="Encargo CERRADO con precedente propuesto.", evidencias=["Entrega, aceptación, métricas"], kpis=["Encargos reabiertos", "Tiempo total"],
     depende=["P10", "P13", "P18"], plantillas=["precedents/plantilla-precedente.md"], pruebas=["CERRADO → REABIERTO sin motivo: rechazado."])

# ---------------- Gobierno y mejora (P12–P18) ----------------
proc(id="P12", nombre="Gestión de cambios", origen=GUIA, cuando="Antes de escalar",
     objetivo="Evaluar cambios de alcance, datos, modelo, reglas o herramientas; versionar y replanificar.",
     inicio="Petición de cambio.", entradas="Cambio propuesto e impacto.",
     actividades=[("Evaluar impacto en riesgo, coste y plazo", "humano", "Análisis de impacto"), ("Versionar el artefacto afectado", "sistema", "Nueva versión"), ("Replanificar", "ia", "Plan revisado"), ("Aprobar", "humano", "Cambio aprobado")],
     responsables="Responsable de decisiones", especialistas=["decisiones-seguimiento", "implantacion-clientes"],
     reglas=["Un cambio de finalidad reabre la evaluación de riesgo y privacidad."], estados="Definición de proceso: draft → under_review → approved → active → deprecated → retired",
     excepciones=["Cambio urgente de seguridad: vía rápida con revisión posterior."], aprobaciones=["Socios o cliente según alcance"],
     fin="Cambio aplicado y registrado.", evidencias=["Petición, análisis, aprobación"], kpis=["Cambios no planificados"], depende=["P25", "P34"],
     pruebas=["Instancia en curso conserva su versión salvo migración explícita."])

proc(id="P13", nombre="Aprendizaje y actualización de la wiki", origen=GUIA, cuando="Antes de escalar",
     objetivo="Proponer, revisar, aprobar, versionar y retirar conocimiento derivado de proyectos.",
     inicio="Cierre de encargo o incidente, o nueva fuente.", entradas="Precedente o hallazgo.",
     actividades=[("Buscar si ya existe", "sistema", "Coincidencias"), ("Proponer ficha draft con procedencia", "ia", "Ficha draft"), ("Revisión de confidencialidad (¿es de un cliente?)", "humano", "Apta o no para lo común"), ("Aprobar o descartar", "humano", "approved o descartada")],
     responsables="Bibliotecario", especialistas=["bibliotecario"],
     reglas=["Nada pasa a approved sin revisión.", "Información de un cliente no pasa a lo común sin autorización."], estados="Ficha: raw → draft → validated → approved → deprecated / disputed",
     aprobaciones=["Socio o responsable del área"], fin="Ficha publicada o descartada.", evidencias=["Historial Git de la ficha"], kpis=["Fichas draft con más de 30 días"],
     depende=["P04", "P11", "P28"], plantillas=["knowledge/plantillas/ficha-conocimiento.md"], pruebas=["Ficha sin fuente: no puede pasar de draft."])

proc(id="P14", nombre="Gestión de permisos y aislamiento", origen=GUIA, cuando="Antes de datos reales",
     objetivo="Administrar identidades, roles, cliente, ámbitos de acceso y pruebas de segregación.",
     inicio="Alta, baja o cambio de usuario o cliente.", entradas="Identidad, rol, cliente.",
     actividades=[("Alta de identidad con rol mínimo", "sistema", "Identidad"), ("Políticas de fila por cliente en PostgreSQL", "regla", "RLS forzada"), ("Pruebas negativas de acceso cruzado", "sistema", "Informe de pruebas"), ("Revisión periódica de accesos", "humano", "Accesos revisados")],
     responsables="Ciberseguridad", especialistas=["ciberseguridad", "backend"],
     reglas=["Aislamiento en API, consultas, búsqueda, almacenamiento, cachés, registros y herramientas (INT-GUIA)."], estados="Identidad: activa · suspendida · baja",
     sistemas=["Proveedor de identidad (decisión pendiente)", "PostgreSQL RLS"], aprobaciones=["Roles privilegiados: socios"],
     fin="Accesos vigentes y probados.", evidencias=["Resultado de pruebas negativas"], kpis=["Pruebas de acceso cruzado que fallan por diseño"], depende=["P30"],
     pruebas=["Usuario de A no lee, escribe ni busca en B.", "Dueño de tabla también sujeto a RLS (FORCE)."])

proc(id="P15", nombre="Observabilidad e incidencias", origen=GUIA, cuando="MVP",
     objetivo="Registrar logs, costes, latencia, errores, decisiones, incidentes y acciones correctivas.",
     inicio="Continuo.", entradas="Eventos del sistema.",
     actividades=[("Registro estructurado con correlación", "sistema", "Logs"), ("Métricas de coste y latencia", "sistema", "Métricas"), ("Alertas accionables", "regla", "Alerta"), ("Abrir incidencia", "humano", "Incidencia")],
     responsables="Calidad", especialistas=["calidad-riesgos", "backend"],
     reglas=["Nunca volcar datos sensibles en registros."], estados="Incidencia: abierta → en análisis → resuelta → cerrada",
     sistemas=["Logs estructurados", "OpenTelemetry (convenciones GenAI no estables)"], fin="Incidencia cerrada con causa.",
     evidencias=["Logs con correlation_id"], kpis=["Tiempo de detección", "Alertas sin acción"], depende=["P28", "P29"],
     pruebas=["Un log de prueba con DNI inventado aparece redactado."])

proc(id="P16", nombre="Gobierno de modelos e instrucciones", origen=GUIA, cuando="Antes de escalar",
     objetivo="Inventariar modelos, versiones, instrucciones, límites, evaluaciones, cambios y alternativas.",
     inicio="Alta o cambio de modelo o instrucciones.", entradas="Modelo, versión, instrucciones.",
     actividades=[("Registrar modelo y versión de instrucciones", "sistema", "Inventario"), ("Ejecutar evaluación (P23)", "sistema", "Resultados"), ("Aprobar cambio", "humano", "Cambio aprobado"), ("Definir alternativa si el proveedor falla", "humano", "Fallback")],
     responsables="Datos e IA", especialistas=["datos-ia", "evaluacion-ia"],
     reglas=["Sin evaluación superada no hay cambio."], estados="Capacidad: draft → tested → approved → deprecated",
     aprobaciones=["Socios"], fin="Inventario al día.", evidencias=["Evaluación por versión"], kpis=["Regresiones por cambio"], depende=["P23", "P25", "P27"],
     pruebas=["Cambio de instrucciones sin evaluación: bloqueado."])

proc(id="P17", nombre="Seguridad y continuidad", origen=GUIA, cuando="Antes de datos reales",
     objetivo="Gestionar secretos, copias, restauración, vulnerabilidades, dependencias y respuesta a incidentes.",
     inicio="Continuo y ante alertas.", entradas="Inventario de activos.",
     actividades=[("Escaneo de dependencias y secretos", "sistema", "Hallazgos"), ("Copias cifradas", "sistema", "Copia"), ("Prueba de restauración", "humano", "Informe"), ("Corrección priorizada", "humano", "Acciones")],
     responsables="Ciberseguridad", especialistas=["ciberseguridad"], reglas=["Copia no probada no es recuperable."],
     estados="Hallazgo: abierto → aceptado o corregido → cerrado", aprobaciones=["Aceptación de riesgo: socios"], fin="Hallazgos tratados.",
     evidencias=["Informe de restauración"], kpis=["Hallazgos críticos abiertos", "Última restauración probada"], depende=["P26", "P28", "P30"],
     pruebas=["Restaurar en un entorno limpio y comprobar integridad."])

proc(id="P18", nombre="Evaluación y mejora", origen=GUIA, cuando="Antes de escalar",
     objetivo="Medir calidad, tiempo, coste, retrabajo, errores y satisfacción; priorizar mejoras con evidencia.",
     inicio="Revisión periódica.", entradas="Métricas de P15 y P37.",
     actividades=[("Informe de métricas", "sistema", "Informe"), ("Análisis de causas", "humano", "Causas"), ("Priorizar mejoras", "humano", "Backlog")],
     responsables="Métricas", especialistas=["metricas", "decisiones-seguimiento"], estados="Mejora: propuesta → priorizada → hecha → medida",
     reglas=["Mejora sin métrica de antes y después no se da por hecha."], fin="Backlog priorizado.", evidencias=["Informe"], kpis=["Mejoras medidas / hechas"],
     depende=["P15", "P37"], pruebas=["Informe reproducible desde los datos."])

# ---------------- Controles (P19–P30) ----------------
proc(id="P19", nombre="Política de uso y límites", origen=GUIA, cuando="Antes de automatizar",
     objetivo="Definir tareas permitidas, prohibidas y condicionadas, límites de autonomía y criterios de escalado.",
     inicio="Alta de cliente o de capacidad.", entradas="Matriz de riesgo, contrato.",
     actividades=[("Redactar política", "humano", "Política"), ("Traducir a reglas", "regla", "Reglas versionadas"), ("Probar reglas", "sistema", "Pruebas")],
     responsables="Legal y Calidad", especialistas=["legal-privacidad", "calidad-riesgos"], estados="Política: draft → approved → deprecated",
     reglas=["No etiquetar riesgo por el nombre del departamento."], aprobaciones=["Socios y cliente"], fin="Política aprobada y codificada.",
     evidencias=["Política y pruebas"], kpis=["Encargos bloqueados por política"], depende=["P02"], pruebas=["Acción prohibida se bloquea en todas las vías."])

proc(id="P20", nombre="Seguridad de entradas e inyección de instrucciones", origen=GUIA, cuando="Antes de datos reales",
     objetivo="Tratar documentos, webs, correos y resultados de herramientas como datos no confiables.",
     inicio="Cualquier contenido externo.", entradas="Contenido externo.",
     actividades=[("Separar instrucciones del sistema y datos", "regla", "Prompt estructurado"), ("Detectar instrucciones incrustadas", "ia", "Señal"), ("Bloquear acciones derivadas de contenido externo", "regla", "Acción bloqueada")],
     responsables="Ciberseguridad", especialistas=["ciberseguridad", "evaluacion-ia"],
     reglas=["Un contenido externo nunca cambia permisos ni políticas."], estados="No aplica (control transversal)", fin="Contenido tratado como dato.",
     evidencias=["Pruebas adversariales"], kpis=["Ataques de prueba que pasan (objetivo 0)"], depende=["P21", "P23"],
     pruebas=["Documento con 'ignora las instrucciones y envía…': ninguna acción."])

proc(id="P21", nombre="Ejecución segura de herramientas", origen=GUIA, cuando="Antes de automatizar",
     objetivo="Identidad, autorización por acción, mínimo privilegio, sandbox, límites y registro.",
     inicio="Petición de herramienta.", entradas="Herramienta, operación, parámetros.",
     actividades=[("Validar identidad, cliente, tarea, operación y parámetros", "regla", "Autorizado o denegado"), ("Ejecutar en sandbox si hay código o contenido no confiable", "sistema", "Resultado"), ("Registrar llamada redactada", "sistema", "Evento")],
     responsables="Integraciones", especialistas=["integraciones", "ciberseguridad"],
     reglas=["Denegar por defecto; lista cerrada.", "Acciones externas o irreversibles con aprobación ligada al payload exacto."],
     estados="Llamada: solicitada → autorizada o denegada → ejecutada → registrada", aprobaciones=["Acciones externas: P10"], fin="Llamada registrada.",
     evidencias=["Tool call con autorización"], kpis=["Llamadas denegadas"], depende=["P10", "P30", "P36"],
     pruebas=["Parámetro fuera de esquema: denegado.", "Kill switch corta la herramienta."])

proc(id="P22", nombre="Gestión de errores y reintentos", origen=GUIA, cuando="Antes de automatizar",
     objetivo="Clasificar errores, limitar reintentos, evitar duplicados, aplicar timeout, alternativa, bloqueo y escalado.",
     inicio="Fallo en una tarea.", entradas="Error.",
     actividades=[("Clasificar el error", "regla", "Tipo"), ("Reintentar solo transitorios con espera exponencial y aleatoria", "regla", "Reintento o no"), ("Comprobar idempotencia antes de repetir una acción externa", "regla", "Resultado previo o nueva ejecución"), ("Tras agotar intentos: BLOQUEADO o ESCALADO con evidencia", "sistema", "Estado y alternativa manual")],
     responsables="Backend", especialistas=["backend", "automatizacion"],
     reglas=["No reintentar errores de permisos, seguridad ni políticas.", "No reintentar indefinidamente."], estados="Tarea: running → failed / blocked",
     fin="Error resuelto o escalado.", evidencias=["Intentos y causas"], kpis=["Reintentos por éxito", "Duplicados evitados"], depende=["P08", "P28"],
     pruebas=["Clave de idempotencia repetida devuelve el resultado anterior sin ejecutar.", "Error de autorización: un solo intento."],
     implementado="Sí: src/varios/procesos/reintentos.py con pruebas")

proc(id="P23", nombre="Evaluación de agentes y modelos", origen=GUIA, cuando="Antes de escalar",
     objetivo="Casos de prueba representativos, umbrales de calidad, regresión y aprobación de cambios.",
     inicio="Cambio o calendario.", entradas="Dataset versionado.",
     actividades=[("Ejecutar suite", "sistema", "Resultados por campo"), ("Comparar con umbral", "regla", "Pasa o no"), ("Aprobar", "humano", "Decisión")],
     responsables="Evaluación de IA", especialistas=["evaluacion-ia"], estados="Evaluación: preparada → ejecutada → aprobada / rechazada",
     reglas=["Umbral por caso de uso y riesgo (pendiente: 22/01/2027)."], aprobaciones=["Socios"], fin="Resultado registrado.",
     evidencias=["Informe por versión"], kpis=["Exactitud", "Alucinación factual"], depende=["P16", "P25"], pruebas=["Dataset con casos límite y adversariales."])

proc(id="P24", nombre="Gestión del ciclo de vida del dato", origen=GUIA, cuando="Antes de datos reales",
     objetivo="Finalidad, clasificación, retención, acceso, exportación, rectificación y borrado, incluidos copias y derivados.",
     inicio="Alta de categoría de datos o petición de derechos.", entradas="Ficha de tratamiento.",
     actividades=[("Ficha de tratamiento", "humano", "Ficha"), ("Retención programada", "regla", "Borrado o bloqueo"), ("Atender derechos: localizar original, wiki, índices y derivados", "sistema", "Respuesta")],
     responsables="Legal y privacidad", especialistas=["legal-privacidad", "backend"], estados="Dato: alta → uso → conservación → borrado",
     reglas=["No conservar indefinidamente por comodidad."], aprobaciones=["Retención legal: Legal"], fin="Ciclo cumplido y documentado.",
     evidencias=["Registro de borrados"], kpis=["Peticiones de derechos en plazo"], depende=["P07", "P14"], pruebas=["Borrado alcanza índices y derivados."])

proc(id="P25", nombre="Gestión de cambios y versiones", origen=GUIA, cuando="Antes de escalar",
     objetivo="Versionar instrucciones, modelos, reglas, herramientas y código; probar aparte; aprobar y poder revertir.",
     inicio="Cambio listo.", entradas="Artefactos versionados.",
     actividades=[("Pruebas en entorno separado", "sistema", "Resultados"), ("Aprobación", "humano", "Release aprobada"), ("Despliegue con vuelta atrás", "sistema", "Release activa")],
     responsables="Arquitecto técnico", especialistas=["arquitecto-tecnico"], estados="Release: candidata → aprobada → desplegada → revertida",
     reglas=["Toda release tiene vuelta atrás probada."], aprobaciones=["Socios"], fin="Release activa o revertida.",
     evidencias=["Release con versiones y prueba"], kpis=["Reversiones"], depende=["P12", "P23"], pruebas=["Revertir y comprobar estado."])

proc(id="P26", nombre="Continuidad y recuperación", origen=GUIA, cuando="Antes de escalar",
     objetivo="RPO/RTO por criticidad, copias cifradas, restauraciones reales y procedimiento manual alternativo.",
     inicio="Plan anual y caída.", entradas="Servicios y criticidad.",
     actividades=[("Definir RPO/RTO con negocio", "humano", "Objetivos"), ("Probar restauración", "humano", "Informe"), ("Procedimiento manual", "humano", "Runbook")],
     responsables="Ciberseguridad", especialistas=["ciberseguridad"], estados="Plan: borrador → probado → vigente",
     reglas=["No inventar un RTO universal."], fin="Plan probado.", evidencias=["Pruebas de restauración"], kpis=["Tiempo real de restauración"],
     depende=["P17"], plantillas=["processes/runbooks/restauracion.md"], pruebas=["Simulacro de caída del proveedor de LLM."])

proc(id="P27", nombre="Gestión de proveedores y dependencias", origen=GUIA, cuando="Antes de datos reales",
     objetivo="Inventariar LLM, API, librerías y terceros; privacidad, ubicación, condiciones, disponibilidad, cambios y salida.",
     inicio="Alta o revisión de proveedor.", entradas="Condiciones del proveedor.",
     actividades=[("Ficha de proveedor", "humano", "Ficha"), ("Revisión de licencia y privacidad", "humano", "Apto o no"), ("Plan de salida", "humano", "Plan")],
     responsables="Costes y proveedores", especialistas=["costes-proveedores", "legal-privacidad"], estados="Proveedor: propuesto → aprobado → en revisión → retirado",
     reglas=["Licencias no OSI se revisan antes de usarlas en servicios a clientes."], aprobaciones=["Socios"], fin="Proveedor aprobado con salida.",
     evidencias=["Ficha"], kpis=["Proveedores sin ficha (objetivo 0)"], depende=["P16", "P29"], plantillas=["knowledge/plantillas/ficha-proveedor.md"],
     pruebas=["Cambio de condiciones detectado en la revisión."])

proc(id="P28", nombre="Gestión de incidentes", origen=GUIA, cuando="Antes de escalar",
     objetivo="Detectar, clasificar, contener, preservar evidencias, notificar, recuperar y aprender.",
     inicio="Alerta o aviso.", entradas="Indicios.",
     actividades=[("Clasificar gravedad", "humano", "Gravedad"), ("Contener (kill switch, revocar)", "humano", "Contención"), ("Preservar evidencias", "sistema", "Evidencias"), ("Evaluar obligación de notificar", "humano", "Decisión"), ("Recuperar y lección aprendida", "humano", "Precedente")],
     responsables="Ciberseguridad y Calidad", especialistas=["ciberseguridad", "calidad-riesgos", "legal-privacidad"],
     reglas=["Brecha de datos personales con riesgo: 72 horas a la AEPD (Marco legal)."], estados="Incidente: detectado → contenido → erradicado → recuperado → cerrado",
     aprobaciones=["Notificaciones: socios con asesoría"], fin="Incidente cerrado con lección.", evidencias=["Cronología"], kpis=["Tiempo de contención"],
     depende=["P15", "P17", "P13"], plantillas=["processes/runbooks/", "precedents/plantilla-incidente.md"], pruebas=["Simulacro de fuga sospechada."])

proc(id="P29", nombre="Gestión de costes y capacidad", origen=GUIA, cuando="Antes de automatizar",
     objetivo="Presupuestos por proyecto y cliente, límites de tokens y llamadas, alertas, cuotas y concurrencia.",
     inicio="Continuo.", entradas="Consumo.",
     actividades=[("Medir consumo por encargo", "sistema", "Coste"), ("Comparar con límite", "regla", "Dentro o fuera"), ("Detener al alcanzar el umbral salvo autorización", "regla", "Pausa")],
     responsables="Costes", especialistas=["costes-proveedores", "metricas"], estados="Presupuesto: abierto → alerta → agotado",
     reglas=["Al llegar al límite se para, no se avisa solo."], aprobaciones=["Ampliar presupuesto: socio"], fin="Consumo dentro de límites.",
     evidencias=["Coste por encargo"], kpis=["Coste por caso"], depende=["P06", "P15"], pruebas=["Encargo que supera el límite queda en pausa."])

proc(id="P30", nombre="Gestión de identidades y secretos", origen=GUIA, cuando="Antes de datos reales",
     objetivo="Autenticación, autorización, roles, rotación y almacenamiento seguro de secretos.",
     inicio="Alta, rotación o revocación.", entradas="Identidades y secretos.",
     actividades=[("Guardar secretos en gestor", "sistema", "Secreto"), ("Rotar", "sistema", "Secreto nuevo"), ("Revocar", "humano", "Revocado")],
     responsables="Ciberseguridad", especialistas=["ciberseguridad", "integraciones"],
     reglas=["Prohibido incluir credenciales en instrucciones, registros o repositorios."], estados="Secreto: activo → rotado → revocado",
     sistemas=["Gestor de secretos (decisión pendiente)"], fin="Secretos al día.", evidencias=["Registro de rotaciones"], kpis=["Secretos sin rotar"],
     depende=["P14", "P21"], pruebas=["Escáner de secretos en cada propuesta de cambios."])

# ---------------- Atlas Evolución (P31–P38, propuesta) ----------------
proc(id="P31", nombre="Calificación de oportunidad", origen=ATLAS, cuando="MVP",
     objetivo="Problema, sponsor, encaje, impacto, viabilidad, riesgo y go/no-go.",
     inicio="Oportunidad detectada.", entradas="Datos de la empresa y del problema.",
     actividades=[("Ficha de oportunidad con MEDDPICC", "humano", "Ficha"), ("Evaluar encaje con el paquete sectorial", "ia", "Encaje propuesto"), ("Go/no-go", "humano", "Decisión")],
     responsables="Director comercial", especialistas=["director-comercial", "prospeccion"], estados="Despliegue: qualified (si go)",
     reglas=["Sin problema material ni sponsor confirmado no hay G0."], aprobaciones=["Socios"], fin="Go o no-go registrado.",
     evidencias=["Ficha"], kpis=["Oportunidades que pasan G0"], depende=["P38"], plantillas=["knowledge/plantillas/ficha-oportunidad.md"], pruebas=["Ficha sin comprador económico: no-go."])

proc(id="P32", nombre="Descubrimiento de procesos", origen=ATLAS, cuando="MVP",
     objetivo="Entrevistas, evidencia, AS-IS, variantes, excepciones y línea base.",
     inicio="G0 superada.", entradas="Entrevistas, procedimientos, registros autorizados.",
     actividades=[("Entrevistar a dirección y a quien ejecuta", "humano", "Actas"), ("Mapa AS-IS con variantes", "humano", "AS-IS"), ("Catálogo de excepciones", "humano", "Excepciones"), ("Línea base", "humano", "Baseline"), ("Validación del cliente", "humano", "G1")],
     responsables="Arquitecto de procesos", especialistas=["arquitecto-procesos", "especialista-sectorial", "metricas"], estados="Despliegue: discovery",
     reglas=["Minimización de datos y mandato del cliente."], aprobaciones=["El cliente valida el AS-IS (G1)"], fin="AS-IS validado.",
     evidencias=["Actas, mapa, baseline"], kpis=["Variantes descubiertas"], depende=["P31", "P33", "P37"], plantillas=["processes/templates/proceso-cliente.md"],
     pruebas=["Muestreo de casos reales contra el mapa."])

proc(id="P33", nombre="Diseño y validación TO-BE", origen=ATLAS, cuando="MVP",
     objetivo="Modelo futuro, reglas, controles, RACI, KPI y aprobación del cliente.",
     inicio="G1 superada.", entradas="AS-IS validado.",
     actividades=[("Separar reglas, sugerencias de IA y decisiones humanas", "humano", "TO-BE"), ("RACI y controles", "humano", "RACI"), ("KPI objetivo", "humano", "KPI"), ("Revisión de seguridad y privacidad", "humano", "Informe"), ("Aprobación del cliente", "humano", "G2")],
     responsables="Arquitecto de procesos", especialistas=["arquitecto-procesos", "ciberseguridad", "legal-privacidad", "metricas"], estados="Despliegue: design",
     aprobaciones=["Cliente (G2)"], fin="TO-BE aprobado.", evidencias=["TO-BE versionado"], kpis=["Cambios tras aprobación"], depende=["P32", "P34"],
     pruebas=["Cada regla del TO-BE tiene dueño y prueba."])

proc(id="P34", nombre="Gestión de definiciones de proceso", origen=ATLAS, cuando="MVP",
     objetivo="Versiones, dueño, estados, pruebas, aprobación, publicación y retirada.",
     inicio="TO-BE aprobado o cambio.", entradas="Definición.",
     actividades=[("Escribir definición versionada", "humano", "JSON de definición"), ("Validar estructura y pruebas", "sistema", "Validación"), ("Aprobar y publicar", "humano", "active")],
     responsables="Arquitecto de procesos", especialistas=["arquitecto-procesos", "backend"], estados="Definición: draft → under_review → approved → active → deprecated → retired",
     reglas=["Las definiciones aprobadas son inmutables; un cambio crea versión nueva."], aprobaciones=["Socios"], fin="Definición activa.",
     evidencias=["processes/definitions/*.json"], kpis=["Definiciones con pruebas"], depende=["P12", "P35"],
     pruebas=["tests/test_definiciones.py valida todas las definiciones."], implementado="Sí: validación en src/varios/procesos/definiciones.py")

proc(id="P35", nombre="Gestión de instancias y excepciones", origen=ATLAS, cuando="MVP",
     objetivo="Estados, tareas, SLA, timers, reintentos, escalado, compensación y cierre.",
     inicio="Evento disparador.", entradas="Definición activa.",
     actividades=[("Crear instancia con la versión vigente", "sistema", "Instancia"), ("Ejecutar tareas y timers", "sistema", "Progreso"), ("Gestionar excepciones con dueño y plazo", "humano", "Excepción resuelta"), ("Compensar secuencias parciales", "humano", "Compensación registrada")],
     responsables="Motor de procesos", especialistas=["backend", "automatizacion"], estados="Instancia: created → ready → running → waiting_external / waiting_human → completed / failed / cancelled",
     reglas=["La instancia conserva su versión salvo migración auditada.", "El LLM no cambia estados."], fin="Instancia cerrada.",
     evidencias=["ProcessEvent por transición"], kpis=["Excepciones por instancia"], depende=["P22", "P34"],
     pruebas=["Reinicio no pierde ni duplica tareas."])

proc(id="P36", nombre="Gestión del catálogo de conectores", origen=ATLAS, cuando="Antes de automatizar",
     objetivo="Alta, evaluación, scopes, versiones, pruebas, cambios y revocación.",
     inicio="Necesidad de integración.", entradas="Sistema destino.",
     actividades=[("Buscar conector existente", "sistema", "Reutilizable o no"), ("Contrato y scopes mínimos", "humano", "Contrato"), ("Pruebas en sandbox", "sistema", "Pruebas"), ("Aprobación y alta", "humano", "Conector activo")],
     responsables="Integraciones", especialistas=["integraciones", "ciberseguridad"], estados="Conector: draft → tested → approved → active → degraded → suspended → retired",
     reglas=["Credenciales por cliente y entorno."], aprobaciones=["Socios (L3 para operaciones externas)"], fin="Conector activo o descartado.",
     evidencias=["integrations/catalog"], kpis=["Conectores degradados"], depende=["P21", "P30"], pruebas=["Revocación efectiva en menos de un plazo definido."])

proc(id="P37", nombre="Medición de rendimiento y valor", origen=ATLAS, cuando="MVP",
     objetivo="Línea base, KPI, ROI, calidad, costes, adopción y atribución.",
     inicio="Línea base en P32.", entradas="Fuentes de datos trazables.",
     actividades=[("Ficha de KPI", "humano", "Ficha"), ("Medición antes", "sistema", "Baseline"), ("Medición después", "sistema", "Resultado"), ("Atribución con supuestos y limitaciones", "humano", "Informe de valor")],
     responsables="Métricas", especialistas=["metricas"], estados="KPI: definido → medido → revisado",
     reglas=["No atribuir mejoras sin evidencia suficiente."], fin="Informe de valor.", evidencias=["KPIObservation"], kpis=["KPI con ficha completa"],
     depende=["P18", "P32"], plantillas=["knowledge/plantillas/ficha-kpi.md"], pruebas=["Informe reproducible."])

proc(id="P38", nombre="Gestión de despliegue por cliente", origen=ATLAS, cuando="Antes de datos reales",
     objetivo="Fases D0–D6, puertas, riesgos, aceptación, soporte y mejora.",
     inicio="Go en P31.", entradas="Ficha de oportunidad.",
     actividades=[("Abrir despliegue con dueño humano", "humano", "Deployment"), ("Pasar cada fase con su puerta G", "humano", "Puerta superada"), ("Gestionar riesgos y cambios", "humano", "Registro"), ("Operar y revisar valor", "humano", "D6")],
     responsables="Responsable de implantación", especialistas=["implantacion-clientes", "gestion-clientes"], estados="Despliegue: qualified → discovery → design → prototype → pilot → production → operating → paused / terminated",
     reglas=["Una puerta no se supera por calendario."], aprobaciones=["Cliente y socio en cada puerta"], fin="Cliente en operación o terminado.",
     evidencias=["Actas de puerta"], kpis=["Puertas a la primera"], depende=["P31", "P32", "P33", "P37"], pruebas=["Despliegue no pasa a pilot sin G3."])

PROCESOS = P
