# -*- coding: utf-8 -*-
# Fuente única de los diagramas de Varios. Genera la web (site/js/atlas-data.js) y el repositorio (docs/atlas/*.md).

INIT = "%%{init: {'theme':'base','themeVariables':{'fontFamily':'Instrument Sans, Helvetica, Arial, sans-serif','fontSize':'15px','primaryColor':'#FFFBF3','primaryBorderColor':'#B9A88A','primaryTextColor':'#22171A','lineColor':'#6A5A55','edgeLabelBackground':'#F6EFE1','clusterBkg':'#FBF6EC','clusterBorder':'#E4D6BC','tertiaryColor':'#FFFFFF'},'flowchart':{'curve':'basis','padding':14,'nodeSpacing':38,'rankSpacing':46}}}%%"

CLASSES = """
classDef ia fill:#DDEFEA,stroke:#0B7A78,stroke-width:1.6px,color:#22171A
classDef re fill:#FFFBF3,stroke:#B9A88A,stroke-width:1.4px,color:#22171A
classDef pe fill:#F3E2E1,stroke:#7A1F2E,stroke-width:1.6px,color:#22171A
classDef dec fill:#F8EBCF,stroke:#8A5A0C,stroke-width:1.6px,color:#22171A
classDef bad fill:#F6DEDF,stroke:#A8283A,stroke-width:1.6px,color:#22171A
classDef ok fill:#E1F0E4,stroke:#1D6B3E,stroke-width:1.6px,color:#22171A
classDef core fill:#22171A,stroke:#22171A,color:#F6EFE1
classDef wine fill:#7A1F2E,stroke:#7A1F2E,color:#FFFFFF
"""

M = []

def add(**k):
    M.append(k)

# ---------------------------------------------------------------- 0
add(id="arquitectura", num="00", grupo="Visión general",
 titulo="Arquitectura del cerebro digital",
 sub="Las capas del sistema, de arriba (personas) a abajo (datos), con la seguridad cruzándolo todo.",
 fuente="Imagen de WhatsApp del 16/11/2026 + Atlas Evolución v1.1, apartado 2",
 simple="Piensa en un edificio de cuatro plantas. Arriba trabajan las personas. Debajo está la dirección (el CEO digital), que entiende el encargo y lo reparte. El motor de procesos lleva el control de cada tarea. Los departamentos hacen el trabajo y solo tocan los programas del cliente a través de una puerta vigilada. En el sótano están los datos y el conocimiento. La seguridad atraviesa todas las plantas.",
 mermaid="""flowchart TB
U["Personas<br/><small>piden, revisan y aprueban</small>"]:::pe
U --> CEO["CEO digital<br/><small>entiende, clasifica, planifica, reparte</small>"]:::core
U -. "leen y editan" .-> OB["Obsidian<br/><small>ventana al conocimiento</small>"]:::re
OB -. "versiona" .-> GIT[("GitHub privado<br/><small>wiki no confidencial y código</small>")]:::re
CEO <-- "consulta con permisos" --> KAPI["API de conocimiento<br/><small>permisos antes de buscar</small>"]:::ia
KAPI --> IDX["Índice de búsqueda"]:::re
KAPI --> RAW[("Originales RAW<br/><small>evidencias y versiones</small>")]:::re
CEO --> PD["Descubrimiento de procesos<br/><small>AS-IS, excepciones, KPI, TO-BE</small>"]:::ia
CEO --> PE["Motor de procesos<br/><small>estados, reglas, plazos, aprobaciones</small>"]:::core
PD --> PE
PE --> PG[("PostgreSQL<br/><small>estados, permisos, auditoría</small>")]:::re
PE --> OI["Inteligencia operativa<br/><small>tiempo, coste, errores, ROI</small>"]:::ia
PE --> CAP["Departamentos + especialistas de sector"]:::re
CAP --> HUB["Centro de integraciones<br/>y puerta de herramientas"]:::dec
HUB --> SYS["Sistemas del cliente<br/><small>CRM, ERP, correo, gestor</small>"]:::re
CAP --> QA["Calidad y aprobaciones"]:::pe
QA --> OUT["Entrega con evidencias"]:::ok
OUT ~~~ SEC["Seguridad y gobierno en todas las capas<br/><small>aislamiento por cliente · permisos · secretos · cifrado · registros · copias · supervisión humana</small>"]:::wine
SYS ~~~ SEC
""",
 pasos=["La petición entra por las personas o por un canal.","El CEO la entiende y decide: si hace falta, primero se descubre el proceso real.","El motor de procesos ejecuta las tareas con reglas y plazos.","Los departamentos trabajan y solo tocan sistemas del cliente a través de la puerta de herramientas.","Calidad y personas revisan antes de entregar.","Todo lo que pasa queda en PostgreSQL; el conocimiento validado, en la wiki."],
 excepciones=["Si el conocimiento no tiene permiso, no se recupera, aunque exista.","Obsidian no es la base de datos ni el sistema de permisos: solo es la ventana para leer y escribir."],
 artefactos=["Mapa de módulos con responsables","Lista de qué vive en PostgreSQL, qué en Git y qué en almacenamiento privado"],
 correcciones=["El original tenía texto que se salía de las cajas y una flecha larga que cruzaba todo el dibujo. Ahora cada flecha va de una caja a la siguiente.","Se añaden los módulos que pide el Atlas de Evolución: descubrimiento de procesos, motor de procesos, centro de integraciones e inteligencia operativa."])

# ---------------------------------------------------------------- 1
add(id="organizacion", num="01", grupo="Visión general",
 titulo="Organización: modelo matricial",
 sub="Dos ejes que se combinan por proyecto, más las personas que responden del resultado.",
 fuente="Guía v1.4, diagrama 2 + Atlas Evolución v1.1, apartados 4 y 4.1",
 simple="No hay un robot para cada combinación. Hay departamentos que sirven para cualquier sector y especialistas de sector que se llaman cuando hace falta. Para cada cliente se forma un equipo a medida. Y siempre hay personas que responden: el responsable del despliegue y el ingeniero que trabaja con el cliente.",
 mermaid="""flowchart TB
CEO["CEO digital<br/><small>prioriza y asigna</small>"]:::core
CEO --> F["Eje funcional<br/><small>Legal y privacidad · Finanzas · Comercial · Operaciones<br/>Tecnología · Datos e IA · Ciberseguridad · PMO · Calidad · RR. HH.</small>"]:::re
CEO --> S["Eje sectorial<br/><small>Seguros y peritaje · Banca · Salud · Construcción · Industria<br/>Logística · Retail · Inmobiliario · Servicios profesionales</small>"]:::ia
F --> EQ["Equipo de proyecto a medida<br/><small>solo las capacidades necesarias</small>"]:::dec
S --> EQ
subgraph H["Personas que responden"]
  direction LR
  DL["Responsable del despliegue<br/><small>resultado, alcance, riesgos, ROI</small>"]:::pe
  FDE["Ingeniero desplegado<br/><small>integra y construye con el cliente</small>"]:::pe
  PA["Arquitecto de procesos<br/><small>AS-IS, TO-BE, reglas, métricas</small>"]:::pe
end
EQ --> H
EQ --> EX["Ejemplo: siniestros<br/><small>Seguros + Operaciones + Tecnología + Datos e IA + Legal + Calidad</small>"]:::ok
""",
 pasos=["El CEO identifica qué funciones y qué sector necesita el encargo.","Se combinan solo esas capacidades en un equipo de proyecto.","Una persona (responsable del despliegue) responde del resultado. La responsabilidad final nunca se delega en la IA."],
 excepciones=["Si falta una capacidad, se deriva a un profesional externo en lugar de improvisarla.","Un paquete sectorial no se lanza hasta tener un cliente con datos autorizados y una métrica de valor."],
 artefactos=["Catálogo de capacidades con responsable, versión, permisos y coste","Equipo y responsables de cada proyecto (matriz RACI)"],
 correcciones=["El Atlas de Evolución pedía añadir al mapa de organización el responsable del despliegue, el ingeniero desplegado y el arquitecto de procesos. No estaba hecho; ahora sí."])

# ---------------------------------------------------------------- 2
add(id="flujo-ceo", num="02", grupo="El CEO digital",
 titulo="Flujo completo del CEO digital",
 sub="De la petición a la entrega, con todos los desvíos: preguntar, rechazar, escalar, rehacer y aprobar.",
 fuente="Atlas · Mapa 2, versión 1.0",
 simple="Este es el camino de cualquier encargo. Lo importante son los rombos: en cada uno el CEO puede parar. Si falta información, pregunta. Si no está permitido, rechaza o deriva. Si la calidad falla, se rehace. Si el riesgo lo exige, una persona aprueba antes de entregar.",
 mermaid="""flowchart TB
A["Solicitud<br/><small>chat, formulario o integración</small>"]:::re --> B["Validar entrada<br/><small>identidad, formato, adjuntos</small>"]:::re
B --> C{"¿Entrada segura?"}:::dec
C -- "no" --> Q["Cuarentena y revisión<br/><small>no se ejecuta el adjunto</small>"]:::bad
C -- "sí" --> D["Clasificar<br/><small>intención, sector, proceso, riesgo</small>"]:::ia
D --> E{"¿Información suficiente?"}:::dec
E -- "no" --> F["Preguntar al solicitante"]:::ia
F -- "respuesta" --> D
E -- "sí" --> G{"¿Permitido y seguro?"}:::dec
G -- "no permitido" --> R["Rechazar o derivar<br/><small>con motivo registrado</small>"]:::bad
G -- "riesgo alto o dudoso" --> ES["Escalar a una persona"]:::pe
ES -- "autoriza" --> H
G -- "sí" --> H["Planificar<br/><small>tareas, dependencias, criterios, coste</small>"]:::ia
H --> I["Ejecutar con el motor de procesos<br/><small>departamentos y herramientas autorizadas</small>"]:::re
I --> J["Control de calidad y evidencias"]:::re
J --> K{"¿Supera QA?"}:::dec
K -- "no" --> L["Rehacer o replanificar<br/><small>con defectos concretos</small>"]:::dec
L --> I
K -- "sí" --> M{"¿Requiere aprobación?"}:::dec
M -- "sí" --> N["Aprobación humana"]:::pe
N -- "denegada" --> O["Detener y registrar decisión"]:::bad
N -- "aprobada" --> P["Entregar<br/><small>formato acordado y trazabilidad</small>"]:::ok
M -- "no" --> P
P --> Z["Cerrar y proponer aprendizaje<br/><small>como borrador, nunca autoaprobado</small>"]:::ok
""",
 pasos=["Registrar solicitud, solicitante, cliente, fecha y adjuntos.","Validar identidad, formato, adjuntos y autorización.","Clasificar intención, sector, proceso, sensibilidad, riesgo y confianza.","Si falta información esencial, preguntar.","Comprobar alcance, política y permisos antes de planificar.","Crear el plan con responsables, dependencias y criterios de éxito.","Ejecutar con herramientas autorizadas.","Validar resultados contra fuentes y criterios.","Pedir aprobación humana si corresponde.","Entregar, registrar y cerrar; el aprendizaje se propone aparte."],
 excepciones=["Entrada sospechosa: cuarentena; nunca se ejecuta el adjunto.","Baja confianza: preguntar, no forzar la clasificación.","Fuera de alcance: rechazar o proponer una alternativa segura.","Fallo de tarea: reintento limitado o escalado.","QA no superado: vuelve a ejecución con defectos concretos.","Aprobación denegada: se detiene la acción y se registra."],
 artefactos=["Solicitud normalizada","Ficha de clasificación y riesgo","Plan de ejecución","Registro de aprobaciones","Paquete de entrega y cierre"],
 correcciones=["En el original, la entrega iba antes de la aprobación humana, al revés de lo que dice su propio texto (paso 9 aprobar, paso 10 entregar). Corregido: primero se aprueba y después se entrega.","Faltaban en el dibujo los caminos de rechazar, escalar y cuarentena que el texto sí describe.","Las etiquetas \"no / respuesta\" y \"baja confianza\" se pisaban. Ahora cada flecha tiene su etiqueta."])

# ---------------------------------------------------------------- 3
add(id="decisiones-ceo", num="03", grupo="El CEO digital",
 titulo="Las cinco decisiones del CEO",
 sub="La clasificación no es una etiqueta: termina siempre en una decisión auditable.",
 fuente="Guía v1.4, Anexo III apartados 2 y 2.2 + diagrama 11",
 simple="Después de entender un encargo, el CEO solo puede hacer una de cinco cosas: seguir, preguntar, escalar a una persona, rechazar o derivar a otro profesional. Siempre deja escrito por qué. La confianza que diga la IA es una pista, nunca un permiso.",
 mermaid="""flowchart TB
A["Petición<br/><small>objetivo, datos, restricciones</small>"]:::re --> B["Ficha normalizada<br/><small>hechos, supuestos y preguntas separados</small>"]:::ia
B --> C["Detectar límites<br/><small>alcance, política, datos sensibles</small>"]:::re
C --> D{"¿Está permitido?"}:::dec
D -- "prohibido o no autorizado" --> RE["RECHAZAR<br/><small>explica el límite</small>"]:::bad
D -- "necesita otro profesional" --> DE["DERIVAR<br/><small>pasa el contexto mínimo</small>"]:::pe
D -- "sí" --> E{"¿Datos suficientes?"}:::dec
E -- "falta algo que cambia la solución" --> PR["PREGUNTAR<br/><small>pausa las tareas dependientes</small>"]:::ia
PR -- "nueva información" --> B
E -- "sí" --> F{"Riesgo según reglas fijas"}:::dec
F -- "alto, dudoso o excepción" --> ESC["ESCALAR<br/><small>revisa una persona identificada</small>"]:::pe
F -- "dentro de política" --> CO["CONTINUAR<br/><small>crea el plan y las tareas</small>"]:::ok
ESC -- "autoriza" --> CO
""",
 pasos=["Recepción con identidad y cliente.","Normalización: separa hechos, supuestos y preguntas. El usuario puede corregirla.","Detección de límites: alcance, política, datos sensibles, conflicto de interés.","Clasificación con razones y campos desconocidos marcados.","Suficiencia: ¿hay datos para planificar?","Riesgo y autonomía con reglas fijas.","Equipo y plan versionado.","Supervisión: si cambia algo importante, se pausa y se replanifica."],
 excepciones=["Cada campo se marca como confirmado, inferido o desconocido. No se usa un umbral tipo \"80 % de confianza\" sin calibrarlo antes.","Seguridad, permisos, pagos, comunicaciones externas y efectos irreversibles nunca se habilitan por la puntuación del modelo."],
 artefactos=["Registro de la decisión con su motivo","Política de parada por criticidad"],
 correcciones=["El diagrama original tenía flechas que salían de la misma caja con etiquetas superpuestas. Se rehace con las cinco decisiones con nombre propio, tal como las define el texto."])

# ---------------------------------------------------------------- 4
add(id="ejecucion", num="04", grupo="Ejecución",
 titulo="Ejecución: motor de procesos, agentes y herramientas",
 sub="El plan se convierte en tareas controladas por estados. Ningún agente actúa libremente.",
 fuente="Atlas · Mapa 4 + Atlas Evolución v1.1, apartado 3.2",
 simple="Cuando el plan está aprobado, el motor de procesos lo convierte en tareas. Cada tarea va a un agente con lo justo para trabajar. Si el agente quiere usar una herramienta, tiene que pedir permiso en una puerta. El resultado se comprueba, y si falla se reintenta con límite o se escala. Todo queda registrado.",
 mermaid="""flowchart TB
A["Plan aprobado<br/><small>objetivo, tareas, criterios, límites</small>"]:::re --> B["Motor de procesos<br/><small>estados, dependencias, plazos</small>"]:::core
B --> C["Asignador<br/><small>capacidad, carga, riesgo, coste</small>"]:::re
C --> D["Agente acotado<br/><small>contexto mínimo autorizado</small>"]:::ia
D -- "pide una acción" --> E{"Puerta de políticas<br/>¿autorizado?"}:::dec
E -- "no" --> X["Bloquear y alertar"]:::bad
E -- "sí" --> F["Puerta de herramientas<br/><small>valida argumentos, límites, sandbox</small>"]:::dec
F --> G["Herramienta<br/><small>permisos mínimos y aislada</small>"]:::re
G --> H{"¿Resultado válido?<br/><small>esquema y criterios</small>"}:::dec
H -- "sí" --> I["Control de calidad"]:::pe
H -- "no" --> J["Reintento limitado o escalado"]:::dec
J -- "replanifica" --> B
I --> K["Estado final<br/><small>terminada, fallida, bloqueada o espera aprobación</small>"]:::ok
B -. "registra" .-> L[("Auditoría<br/><small>quién, qué, cuándo, con qué permiso</small>")]:::re
F -. "registra" .-> L
""",
 pasos=["El motor crea tareas con identificador y estado.","El asignador elige capacidad y modelo según política.","Se prepara el contexto mínimo autorizado.","La puerta valida identidad, argumentos, alcance y presupuesto.","La herramienta se ejecuta con permisos mínimos.","El resultado se valida contra esquema y criterios.","Se registra traza y coste.","Si falla: reintento limitado, compensación o escalado.","QA y aprobación antes de entregar."],
 excepciones=["Tiempo agotado: cancelar si es seguro y reintentar con espera creciente.","Respuesta mal formada: se rechaza y no se propaga.","Herramienta no autorizada: se bloquea y se avisa.","Efecto duplicado: claves de idempotencia y conciliación.","Agente en bucle o coste excesivo: límites y botón de parada."],
 artefactos=["Catálogo de herramientas","Máquina de estados","Política de reintentos e idempotencia","Registro de ejecuciones y costes","Evaluaciones de agentes"],
 correcciones=["Se añade el motor de procesos y la salida \"bloquear\" de la puerta de políticas, que pedía el Atlas de Evolución.","La flecha \"replanifica\" cruzaba toda la imagen por encima de otras cajas. Ahora vuelve limpia al motor."])

# ---------------------------------------------------------------- 5
add(id="gateway", num="05", grupo="Ejecución",
 titulo="Puerta de herramientas",
 sub="Ningún agente tiene contraseñas ni acceso directo: pide la acción a una puerta que decide.",
 fuente="Guía v1.4, diagrama 12 y Anexo III apartado 5",
 simple="Es como el control de acceso de un edificio. El agente pide hacer algo. La puerta comprueba quién lo pide, para qué cliente y si está permitido. Si es algo serio (enviar, pagar, borrar), espera a que una persona lo apruebe. Solo entonces se hace, aislado y registrado.",
 mermaid="""flowchart LR
A["Agente o CEO<br/><small>propone una acción</small>"]:::ia -- "solicitud estructurada" --> B["Puerta de herramientas<br/><small>identidad, cliente, política</small>"]:::dec
B --> C{"¿Autorizada?"}:::dec
C -- "no" --> D["Denegar y alertar"]:::bad
C -- "sí" --> E["Alcance mínimo<br/><small>cliente, recurso, operación</small>"]:::re
E --> F{"¿Requiere aprobación?"}:::dec
F -- "preautorizada" --> G["Ejecución aislada<br/><small>secretos fuera del prompt, límites</small>"]:::re
F -- "sí: externa o irreversible" --> H["Aprobación humana<br/><small>sobre el contenido exacto</small>"]:::pe
H -- "aprobada" --> G
H -- "denegada" --> D
G --> I[("Registro y evidencia<br/><small>quién, qué, cuándo, resultado</small>")]:::ok
""",
 pasos=["Catálogo: cada herramienta declara finalidad, responsable, entradas, permisos, riesgos y límites.","Denegar por defecto; lista cerrada de operaciones.","Credenciales distintas por entorno y alcance mínimo.","Sandbox cuando se ejecuta código o contenido no confiable.","Validar parámetros: tamaños, rutas, dominios.","Aprobación vinculada al contenido exacto para acciones externas, financieras o destructivas.","Registro completo con parámetros redactados.","Botón de parada por herramienta, proyecto, cliente y sistema."],
 excepciones=["Las instrucciones que aparezcan dentro de un documento o correo nunca pueden activar una herramienta.","No se reintentan errores de permisos ni de política."],
 artefactos=["Catálogo de herramientas","Matriz de aprobaciones por tipo de acción"],
 correcciones=["En el original las flechas de \"no autorizada\" y \"autorizada\" salían del mismo punto y casi se tocaban. Ahora la decisión es un rombo con dos salidas claras."])

# ---------------------------------------------------------------- 6
add(id="fallos", num="06", grupo="Ejecución",
 titulo="Fallos, reintentos y recuperación",
 sub="Nada se reintenta para siempre. Lo dudoso no se propaga.",
 fuente="Guía v1.4, diagrama 13 y Anexo III apartado 4.1",
 simple="Si algo sale mal, el sistema distingue: un fallo pasajero se reintenta unas pocas veces; si se agotan los intentos, se prueba otra vía o se pasa a una persona; si el resultado parece peligroso, se aparta y se abre una incidencia. Nunca se repite una acción que ya se hizo, como un pago.",
 mermaid="""flowchart LR
A["Tarea<br/><small>entrada validada</small>"]:::re --> B["Ejecutar<br/><small>tiempo máximo, límites, idempotencia</small>"]:::re
B --> C{"¿Resultado válido?"}:::dec
C -- "sí" --> OK["Aceptar resultado<br/><small>evidencia, estado, salida</small>"]:::ok
C -- "error pasajero" --> R["Reintento controlado<br/><small>límite, espera, sin duplicar</small>"]:::dec
R -- "quedan intentos" --> B
R -- "agotados" --> FB["Alternativa o escalado<br/><small>otro modelo aprobado o persona</small>"]:::pe
FB -- "validado" --> OK
FB -- "no recuperable" --> INC["Incidencia<br/><small>alerta, causa, corrección</small>"]:::bad
C -- "inseguro o inválido" --> BQ["Bloquear y cuarentena<br/><small>no propagar</small>"]:::bad
BQ --> INC
""",
 pasos=["Clasificar el error: pasajero, permanente, funcional, de permisos o de seguridad.","Tiempo máximo y número de intentos configurables, con espera creciente.","Antes de reintentar una acción externa, comprobar si ya se ejecutó.","Agotados los intentos: bloqueado o escalado, con evidencia y alternativa manual.","El estado persiste: reiniciar el sistema no pierde ni duplica tareas."],
 excepciones=["Los errores de permisos o de política no se reintentan nunca."],
 artefactos=["Política de reintentos","Claves de idempotencia","Procedimiento manual alternativo"],
 correcciones=["El original tenía la etiqueta \"Sí\" lejos de su flecha y una línea de vuelta que pasaba por debajo de otras cajas."])

# ---------------------------------------------------------------- 7
add(id="conocimiento", num="07", grupo="Conocimiento",
 titulo="Motor de conocimiento con Obsidian",
 sub="Cómo entra un documento, cómo se convierte en conocimiento aprobado y cómo se consulta con permisos.",
 fuente="Atlas · Mapa 3 + Guía v1.4, diagrama 5 y Anexo III apartado 6",
 simple="Arriba, el camino de entrada: el documento pasa por una aduana, se guarda el original intacto y la IA propone fichas que una persona aprueba. Abajo, el camino de consulta: antes de buscar se comprueban los permisos, y la respuesta siempre dice de dónde sale.",
 mermaid="""flowchart TB
subgraph IN["Entrada"]
  direction TB
  F["Fuentes<br/><small>PDF, Word, Excel, web autorizada</small>"]:::re --> CU["Cuarentena<br/><small>huella, malware, tipo, permisos</small>"]:::dec
  CU --> RAW[("RAW<br/><small>original intacto y versionado</small>")]:::re
  CU --> EX["Extraer texto y metadatos"]:::re
  EX --> PR["Proponer fichas<br/><small>con citas a la fuente</small>"]:::ia
  PR --> LI["Revisión automática<br/><small>campos, enlaces, duplicados</small>"]:::re
  LI --> HU{"Revisión humana<br/>según sensibilidad"}:::pe
  HU -- "aprobada" --> WI["Wiki en Markdown<br/><small>Obsidian + Git</small>"]:::ok
  HU -- "contradice otra fuente" --> DI["En disputa<br/><small>se muestran ambas</small>"]:::dec
  HU -- "rechazada" --> DESC["Se descarta"]:::bad
end
subgraph OUT["Consulta"]
  direction TB
  CEO["CEO o agente"]:::core --> API["API de consulta"]:::ia
  API --> PERM{"¿Permisos?<br/><small>identidad, cliente, proyecto</small>"}:::dec
  PERM -- "no" --> NO["Denegar"]:::bad
  PERM -- "sí" --> IDX["Índice de búsqueda<br/><small>texto primero; semántica si compensa</small>"]:::re
  IDX --> RES["Fragmentos con cita<br/><small>fuente, versión, fecha</small>"]:::ok
  RES --> CEO
end
WI --> IDX
""",
 pasos=["Recibir el documento en cuarentena.","Calcular huella, analizar tipo, malware y permisos.","Extraer texto y metadatos sin perder el vínculo al original.","Proponer fichas en Markdown con citas.","Revisión automática: campos obligatorios, enlaces, duplicados.","Revisión humana según sensibilidad.","Publicar en la wiki y versionar en Git si la clasificación lo permite.","Indexar solo lo autorizado.","Recuperar fragmentos con referencias.","Tras cada proyecto, proponer mejoras; nunca autoaprobarlas."],
 excepciones=["Extracción incompleta: calidad baja y revisión manual.","Fuentes contradictorias: estado en disputa.","Fuente obsoleta: deprecada, sin borrar la evidencia histórica.","Sin permiso: se deniega aunque exista en el índice.","Datos confidenciales de un cliente: nunca en la wiki común."],
 artefactos=["Plantillas Markdown y metadatos","Política de clasificación y estados","Proceso de ingesta y revisión","Índice y política de recuperación","Registro de procedencia"],
 correcciones=["La flecha \"conserva original\" cruzaba en diagonal por encima de tres cajas, y las de \"indexa\" y \"versiona\" se cortaban. Se separa en dos caminos, entrada y consulta, que no se cruzan."])

# ---------------------------------------------------------------- 8
add(id="seguridad", num="08", grupo="Seguridad",
 titulo="Seguridad, identidad y aislamiento de clientes",
 sub="La autorización ocurre en el servidor. No se confía en instrucciones a la IA, carpetas ni filtros de pantalla.",
 fuente="Atlas · Mapa 5 + Guía v1.4, diagrama 6 y Anexo III apartado 7",
 simple="Cada petición lleva una identidad verificada. De ella sale de qué cliente es y qué puede ver, y eso no lo puede cambiar ni el usuario ni la IA. Con ese pase se consulta la base de datos, los archivos y las herramientas. A la IA le llega solo lo mínimo. Todo acceso, y todo intento denegado, queda registrado.",
 mermaid="""flowchart TB
ID["Identidad<br/><small>usuario, servicio o agente · doble factor</small>"]:::re --> AU["Autenticación<br/><small>sesión, token, caducidad</small>"]:::re
AU --> AZ["Autorización<br/><small>rol + cliente + proyecto</small>"]:::dec
AZ --> CTX["Contexto de seguridad<br/><small>cliente, proyecto, rol, finalidad · no se puede cambiar</small>"]:::core
CTX --> PEF{"Aplicación de políticas<br/>en el servidor"}:::dec
PEF -- "lectura o escritura" --> DAL["Capa de acceso a datos<br/><small>consultas filtradas</small>"]:::re
DAL --> DB[("PostgreSQL con RLS<br/><small>segunda barrera</small>")]:::re
DAL --> OS[("Almacenamiento privado<br/><small>enlaces temporales</small>")]:::re
PEF -- "contexto para la IA" --> MG["Puerta de contexto del modelo<br/><small>minimizar y ocultar datos</small>"]:::ia
PEF -- "acción" --> TP["Permisos de herramientas<br/><small>lista cerrada y sandbox</small>"]:::dec
PEF -- "sin cliente resuelto" --> DENY["Denegar por defecto"]:::bad
DB -.-> AUD[("Auditoría y alertas<br/><small>accesos, exportaciones, denegaciones</small>")]:::re
OS -.-> AUD
TP -.-> AUD
AUD -- "alerta" --> IR["Respuesta a incidentes"]:::bad
subgraph T["Lo que ve cada uno"]
  direction LR
  CO["Corporativo<br/><small>conocimiento común aprobado</small>"]:::ok
  CA["Cliente A<br/><small>aislado</small>"]:::ia
  CB["Cliente B<br/><small>aislado</small>"]:::ia
end
DB --- T
""",
 pasos=["Autenticar usuario o servicio.","Resolver cliente y permisos desde la identidad.","Construir un contexto de seguridad que no se puede modificar.","Autorizar cada lectura, escritura, exportación y herramienta.","RLS y controles de almacenamiento como segunda barrera.","Minimizar el contexto antes de enviarlo a un modelo externo.","Registrar accesos y denegaciones sin volcar secretos.","Detectar y gestionar incidentes."],
 excepciones=["Cliente no resuelto: denegar por defecto.","Token caducado: rechazar y volver a autenticar.","RLS mal configurada: no se despliega hasta pasar las pruebas.","Fuga o acceso cruzado: revocar, contener, preservar evidencias.","Proveedor o modelo no aprobado: no se le envían datos confidenciales."],
 artefactos=["Modelo de amenazas","Matriz de acceso","Políticas RLS y pruebas negativas","Inventario de datos y proveedores","Plan de respuesta a incidentes"],
 correcciones=["El original tenía cinco flechas diagonales que salían del mismo punto y se cruzaban sobre \"PostgreSQL RLS\", con etiquetas ilegibles como \"archivo\" y \"tool scope\" superpuestas. Se reorganiza en un árbol de decisión."],
 prueba="Prueba de aceptación: dos clientes de prueba con datos señuelo únicos. Se intenta leer, buscar, exportar y usar herramientas de uno desde el otro. Cualquier fuga bloquea el lanzamiento.")

# ---------------------------------------------------------------- 9
add(id="calidad", num="09", grupo="Calidad y gobierno",
 titulo="Calidad, evaluación y aprobación humana",
 sub="No se confunde una respuesta convincente con un resultado correcto y autorizado.",
 fuente="Atlas · Mapa 6 + Guía v1.4, diagrama 8 y Anexo III apartado 9",
 simple="Los criterios de \"bien hecho\" se escriben antes de empezar. Primero comprueban las reglas automáticas; después, si el riesgo lo pide, una persona. Lo que falla vuelve a rehacerse. Y cada error que se encuentra se convierte en una prueba nueva para que no se repita.",
 mermaid="""flowchart TB
RQ["Criterios de aceptación<br/><small>se fijan antes de ejecutar</small>"]:::pe --> RA["Resultado del agente<br/><small>análisis, documento, acción propuesta</small>"]:::ia
RA --> QA["QA automático<br/><small>esquema, cálculos, fuentes, pruebas</small>"]:::re
QA --> D1{"¿Supera?"}:::dec
D1 -- "no" --> RT["Rehacer<br/><small>corregir, pedir datos o escalar</small>"]:::bad
RT --> RA
D1 -- "sí" --> D2{"¿El riesgo exige revisión humana?"}:::dec
D2 -- "sí" --> HR["Revisión humana<br/><small>persona, rol, fecha, versión exacta</small>"]:::pe
HR -- "corregir" --> RT
HR -- "aprobar" --> OK["Supera<br/><small>entrega o acción con registro</small>"]:::ok
D2 -- "no" --> OK
OK --> MT["Métricas<br/><small>acierto, errores, coste, tiempo, escalados</small>"]:::re
MT --> DS["Nuevos casos de prueba<br/><small>cada fallo relevante se convierte en prueba</small>"]:::ia
DS -. "alimenta" .-> QA
""",
 pasos=["Definir aceptación, nivel de riesgo y revisor.","Validaciones automáticas fijas.","Evaluar calidad y fundamentación con pruebas controladas.","Revisión humana para tareas de riesgo.","Registrar decisión, versión y evidencias.","Medir calidad, coste, tiempo, fallos y escalados.","Convertir fallos en nuevos casos de prueba."],
 excepciones=["Sin criterio de aceptación no se marca como terminado.","Evaluadores no calibrados: no se automatiza la aprobación.","Regresión detectada: se bloquea la versión y se revierte.","Desacuerdo entre evaluadores: decide un experto humano.","El agente que propone nunca se aprueba a sí mismo."],
 artefactos=["Conjunto de pruebas con versión (normales, límite y ataques)","Umbrales por caso de uso","Registro de aprobaciones"],
 correcciones=["El original mezclaba en un solo dibujo el control de cada resultado y el control de cambios del sistema, con cuatro flechas diagonales cruzadas (\"mide\", \"registra\", \"añade casos\"). Se separan: este mapa es el control de cada resultado; el de cambios va en el mapa 10."])

# ---------------------------------------------------------------- 10
add(id="cambios-modelos", num="10", grupo="Calidad y gobierno",
 titulo="Cambios y elección de modelos de IA",
 sub="Ningún cambio de modelo, instrucción o herramienta llega a producción sin volver a pasar las pruebas.",
 fuente="Guía v1.4, diagrama 14 y Anexo III apartado 8 + Atlas · Mapa 6",
 simple="Cada tipo de tarea tiene un modelo de IA aprobado. Si queremos cambiarlo, o cambiar sus instrucciones, se vuelve a examinar con las mismas pruebas. Si no aprueba, no se usa. Si un modelo en uso empeora, se detecta y se vuelve a evaluar.",
 mermaid="""flowchart LR
T["Tipo de tarea<br/><small>riesgo, sensibilidad, complejidad</small>"]:::re --> RR["Reglas de enrutamiento<br/><small>privacidad, calidad mínima, coste</small>"]:::dec
RR --> MA["Modelo aprobado<br/><small>versión fija y límites</small>"]:::re
MA --> EV{"Evaluación<br/><small>pruebas, casos límite, regresión</small>"}:::dec
EV -- "supera" --> AP["Apto para producción"]:::ok
EV -- "no supera" --> NA["No apto<br/><small>alternativa aprobada o revisión humana</small>"]:::bad
AP --> MO["Monitorización<br/><small>calidad, coste, tiempo, deriva</small>"]:::re
MO -- "empeora o hay propuesta de cambio" --> CC["Cambio controlado<br/><small>prompt, modelo, herramienta, esquema</small>"]:::pe
CC -- "nueva evaluación" --> EV
AP -.-> RB["Reversión preparada<br/><small>siempre se puede volver atrás</small>"]:::re
""",
 pasos=["Registro de modelos: proveedor, versión, región, condiciones, retención, usos autorizados.","Enrutamiento por política, no a elección del CEO.","Alternativas solo hacia modelos ya evaluados para ese nivel de datos.","Instrucciones (prompts) versionadas en Git y con pruebas de regresión.","Cambiar de proveedor obliga a revisar privacidad, contrato y salida.","Presupuesto por proyecto y cliente con corte automático."],
 excepciones=["Si no hay modelo alternativo aprobado, se pausa o se degrada de forma segura."],
 artefactos=["Registro de modelos","Instrucciones versionadas","Informe de evaluación por versión"],
 correcciones=["Reúne la parte de \"cambios controlados\" del mapa 6 original, que estaba enredada con el control de resultados."])

# ---------------------------------------------------------------- 11
add(id="infraestructura", num="11", grupo="Infraestructura",
 titulo="Infraestructura, desarrollo y portabilidad",
 sub="Empezar gratis y con piezas sustituibles, sin depender del Mac.",
 fuente="Atlas · Mapa 7",
 simple="El código se escribe en el Mac, pero vive en GitHub. Desde ahí se despliega a la nube. La aplicación usa una base de datos estándar, un almacén de archivos y un adaptador para el modelo de IA, de forma que cualquier pieza se puede cambiar. Las copias de seguridad se prueban restaurándolas de verdad.",
 mermaid="""flowchart LR
subgraph DEV["Desarrollo"]
  direction LR
  MAC["Mac<br/><small>VS Code, Python, Claude</small>"]:::re --> GL["Git local<br/><small>ramas, commits, tests</small>"]:::re
  GL -- "push" --> GH["GitHub privado<br/><small>repositorio, CI, versiones</small>"]:::ia
end
GH -- "despliegue" --> DP["Despliegue reproducible<br/><small>secretos fuera del código, aprobación</small>"]:::dec
DP --> API["API y procesos<br/><small>FastAPI</small>"]:::core
subgraph RUN["Ejecución"]
  direction TB
  API --> PG[("PostgreSQL estándar")]:::re
  API --> OS[("Almacén de archivos<br/><small>compatible S3</small>")]:::re
  API --> MA["Adaptador de modelos<br/><small>Claude al inicio, cambiable</small>"]:::ia
  API --> OB["Observabilidad<br/><small>logs, métricas, alertas</small>"]:::re
end
PG -- "copia" --> BK[("Copias<br/><small>base y archivos por separado</small>")]:::re
OS -- "copia" --> BK
BK -- "prueba" --> RT["Prueba de restauración<br/><small>periódica y documentada</small>"]:::pe
RT -- "valida" --> MP["Camino de migración<br/><small>Docker, variables, migraciones, exportación</small>"]:::ok
""",
 pasos=["Repositorio privado con estructura reproducible.","Desarrollo local con tests y dependencias fijadas.","PostgreSQL local o gestionado.","Demo en la nube solo cuando aporte valor.","Adaptador de modelos y almacenamiento desacoplados.","Exportar base y archivos; probar restauración en un entorno limpio.","Antes de datos reales, pasar a un plan de producción."],
 excepciones=["El proveedor gratuito pausa o borra: se recrea desde código, migraciones y copias.","Límite de cuota: alertar y degradar con control.","Región no adecuada: no se cargan datos.","Migración fallida: mantener origen y restaurar."],
 artefactos=["Docker Compose y migraciones","Guía de despliegue y recuperación","Inventario de proveedores y regiones"],
 correcciones=["La flecha \"publica\" cruzaba en diagonal todo el dibujo y las etiquetas \"archivos\" e \"inferencias\" se pisaban. Se agrupa por zonas: desarrollo, ejecución y copias."])

# ---------------------------------------------------------------- 12
add(id="ciclo-proyecto", num="12", grupo="Clientes",
 titulo="Ciclo de vida de un proyecto con cliente",
 sub="Fases D0 a D6, con su control de paso, y cómo se aprende sin mezclar clientes.",
 fuente="Atlas · Mapa 8 + Atlas Evolución v1.1, apartado 3.5 + Guía v1.4, diagramas 7 y 9",
 simple="Así avanza un cliente: se califica la oportunidad, se descubre el proceso, se diseña, se prueba en pequeño, se pilota y se pasa a producción. En cada paso hay una puerta (G0 a G6). Al cerrar, se aprende, pero lo aprendido se limpia de datos del cliente y lo aprueba una persona antes de reutilizarlo.",
 mermaid="""flowchart TB
D0["D0 · Calificación<br/><small>problema, sponsor, éxito</small>"]:::re -- "G0" --> D1["D1 · Descubrimiento<br/><small>AS-IS, excepciones, línea base</small>"]:::ia
D1 -- "G1" --> D2["D2 · Diseño<br/><small>TO-BE, controles, RACI, coste</small>"]:::ia
D2 -- "G2" --> D3["D3 · Prototipo<br/><small>flujo acotado, datos controlados</small>"]:::re
D3 -- "G3" --> D4["D4 · Piloto<br/><small>usuarios reales limitados</small>"]:::dec
D4 -- "G4" --> D5["D5 · Producción<br/><small>contrato, SLA, soporte</small>"]:::ok
D5 -- "G5" --> D6["D6 · Operar y mejorar<br/><small>ROI, incidencias, cambios</small>"]:::ok
D6 -- "G6 · escalar" --> NX["Nuevo caso o cliente"]:::core
D2 -. "cambio de alcance" .-> CR["Petición de cambio<br/><small>reestimar</small>"]:::dec
CR -.-> D2
D6 --> PM["Post-mortem interno"]:::pe
PM --> SAFE["Extracción segura<br/><small>anonimizar y generalizar</small>"]:::pe
SAFE --> WP["Propuesta para la wiki<br/><small>borrador</small>"]:::ia
WP --> VA{"Validación<br/><small>fuente, permiso, aprobación</small>"}:::dec
VA -- "aprobada" --> REU["Se reutiliza en futuros proyectos"]:::ok
VA -- "no demostrada o identificable" --> DSC["Se descarta o queda aislada"]:::bad
""",
 pasos=["Registrar oportunidad y solicitante.","Descubrimiento con supuestos y lagunas documentados.","Propuesta y plan con riesgos y responsables.","Aprobación de alcance y ejecución.","Ejecución con evidencias.","QA y aceptación del cliente.","Entrega y cierre con métricas.","Post-mortem interno.","Extraer patrones no confidenciales.","Proponer y validar antes de publicar en la wiki."],
 excepciones=["Cambia el alcance: petición de cambio y reestimación.","El cliente no acepta: registrar defectos y plan de corrección.","Datos no reutilizables: se descarta el aprendizaje o se mantiene aislado.","Lección no demostrada: no se publica como método."],
 artefactos=["Ficha de oportunidad","Mapa AS-IS y TO-BE","Métrica de éxito firmada","Informe de cierre"],
 correcciones=["El original tenía una flecha \"reutiliza en futuros proyectos\" que cruzaba \"completa\" y \"QA\" en diagonal. Se integran las fases D0–D6 del Atlas de Evolución, que el mapa 8 debía incluir y no incluía."])

# ---------------------------------------------------------------- 13
add(id="ciclo-dato", num="13", grupo="Seguridad",
 titulo="Ciclo de vida de un dato",
 sub="Cada dato entra con una finalidad, se usa con control y se borra cuando ya no hace falta.",
 fuente="Guía v1.4, diagrama 15 y Anexo III apartado 10",
 simple="Un dato no se guarda \"por si acaso\". Al entrar se sabe para qué es y cuánto tiempo puede quedarse. Se usa lo mínimo y con permiso. Periódicamente se revisa: si ya no hace falta, se borra o se anonimiza, también en copias y derivados, y queda constancia.",
 mermaid="""flowchart LR
CA["Captura<br/><small>finalidad, origen, base jurídica</small>"]:::re --> CL["Clasificar<br/><small>cliente, sensibilidad, retención</small>"]:::dec
CL --> AL[("Almacenar<br/><small>cifrado, separado, con acceso</small>")]:::re
AL --> US["Uso controlado<br/><small>mínimo, con permisos y trazas</small>"]:::ia
US --> RV{"Revisión periódica<br/><small>exactitud, vigencia, necesidad</small>"}:::dec
RV -- "sigue siendo necesario" --> CO["Conservar<br/><small>plazo definido y justificado</small>"]:::ok
RV -- "no necesario o plazo vencido" --> EL["Eliminar o anonimizar<br/><small>incluye copias e índices</small>"]:::bad
CO --> EV[("Evidencia<br/><small>registro de accesos y borrado</small>")]:::re
EL --> EV
""",
 pasos=["Alta: minimizar, clasificar, finalidad, permisos y retención.","Uso: acceso por necesidad, registro, cifrado.","Compartición: revisar destinatario, contrato y autorización.","Rectificación: corregir también wiki, índices y derivados.","Borrado: sistemas activos y plazos de las copias documentados.","Incidente: preservar evidencias y evaluar notificación."],
 excepciones=["No conservar indefinidamente por comodidad.","Retención legal cuando proceda."],
 artefactos=["Ficha de tratamiento por categoría de datos","Registro de borrados"],
 correcciones=["En el original, las flechas de \"necesario\" y \"no necesario\" salían juntas y la etiqueta quedaba lejos de su flecha."])

# ---------------------------------------------------------------- 14
add(id="incidentes", num="14", grupo="Seguridad",
 titulo="Operación y respuesta a incidentes",
 sub="Detectar, contener sin borrar pruebas, recuperar y aprender.",
 fuente="Guía v1.4, diagrama 16 + Marco legal, apartado 10",
 simple="Cuando algo raro pasa, primero se aísla para que no vaya a más, sin destruir pruebas. Después se mira a quién afecta y si hay que avisar a alguien por ley (cada norma tiene su reloj). Luego se arregla, se recupera desde una copia limpia y se escribe qué falló para que no vuelva a pasar.",
 mermaid="""flowchart TB
OB["Observabilidad<br/><small>logs, métricas, trazas, costes</small>"]:::re --> DT["Detección<br/><small>alertas, anomalías, umbrales</small>"]:::re
DT --> TR{"Triaje<br/><small>severidad y alcance</small>"}:::dec
TR -- "confirmado" --> CT["Contener<br/><small>revocar, aislar, pausar agente</small>"]:::bad
TR -- "falsa alarma" --> AJ["Ajustar detección"]:::re
CT --> PE["Preservar evidencias<br/><small>logs, copias, cadena de custodia</small>"]:::pe
PE --> NO{"¿Hay que notificar?<br/><small>RGPD 72 h · NIS2 · DORA · contrato</small>"}:::dec
NO --> ER["Erradicar causa<br/><small>parchear, rotar secretos</small>"]:::re
ER --> RC["Recuperar<br/><small>desde copia limpia y probada</small>"]:::ok
RC --> PM["Post-mortem<br/><small>causa, acciones, responsable</small>"]:::pe
PM --> PP["Pruebas periódicas<br/><small>restauración, permisos, continuidad</small>"]:::re
PP -. "mejoras" .-> OB
""",
 pasos=["Registrar la hora de detección y nombrar responsable.","Contener sin destruir evidencias.","Preservar registros y copias.","Determinar sistemas, clientes, datos y periodo afectados.","Activar privacidad y legal; evaluar cada régimen por separado.","Erradicar la causa.","Recuperar desde una copia limpia.","Comunicar con veracidad.","Informe posterior con acciones y responsables."],
 excepciones=["Crítica: fuga entre clientes, ransomware, toma de control. Activar crisis.","Alta: acceso no autorizado limitado o proveedor comprometido.","Media: error de permisos sin explotación.","Baja: evento bloqueado sin impacto."],
 artefactos=["Runbooks","Matriz de relojes de notificación por norma y cliente","Registro de incidentes"],
 correcciones=["El original no mostraba la preservación de evidencias ni la evaluación de notificaciones legales, que el Marco legal sí exige. Añadidas."])

# ---------------------------------------------------------------- 15
add(id="componentes", num="15", grupo="Infraestructura",
 titulo="Conversación entre componentes",
 sub="Qué pieza llama a cuál, en qué orden y qué se guarda. Se lee de arriba abajo.",
 fuente="Atlas · Mapa 9",
 simple="Es la misma petición vista por dentro, como una conversación entre las piezas del sistema. Lo importante: todo se guarda antes de actuar, y cada paso deja un rastro en el registro de auditoría.",
 mermaid="""sequenceDiagram
autonumber
participant UI as Canal
participant API as API
participant CEO as CEO
participant WF as Motor de procesos
participant KN as Conocimiento
participant WK as Agente
participant TG as Puerta de herramientas
participant QA as Calidad
participant AU as Auditoría
UI->>API: Petición con identidad
API->>API: Valida formato, identidad y límites
API->>CEO: Petición + contexto de seguridad
CEO->>KN: Consulta con permisos
KN-->>CEO: Fragmentos con citas
CEO->>WF: Clasificación y plan estructurado
WF->>WF: Guarda plan y tareas antes de ejecutar
WF->>WK: Despacha tarea
WK->>TG: Pide herramienta
TG-->>WK: Resultado autorizado
WK->>WF: Resultado
WF->>QA: Validar
QA-->>WF: Supera o rehacer
WF-->>UI: Pide aprobación si hace falta
WF->>AU: Eventos de cada paso
WF-->>UI: Cierre con resultado y trazabilidad
""",
 pasos=["El canal envía la petición con identidad.","La API valida formato, identidad y límites.","El CEO devuelve clasificación y plan estructurado.","Se guardan el plan y las tareas antes de ejecutar.","Se consulta el conocimiento con contexto autorizado.","La tarea va a un agente, que pide herramientas a la puerta.","Se guarda el resultado y los eventos de auditoría.","Calidad valida y se actualiza el estado.","Se pide aprobación cuando hace falta.","Se cierra con resultado y trazabilidad."],
 excepciones=["Contrato inválido: error 400/422 con mensaje claro.","No autorizado: 403 sin revelar datos.","Dependencia caída: tiempo máximo, reintento acotado y estado bloqueado.","Evento duplicado: se descarta por su identificador.","Resultado perdido: se reconstruye con artefactos y registros."],
 artefactos=["Contratos versionados entre módulos","Lista de eventos","Entidades de datos (ver Procesos)"],
 correcciones=["El original tenía etiquetas rotas (\"artifact ref/vent\", \"approval / status\" encima de una caja) y una flecha de la puerta de herramientas a auditoría que cruzaba todo el dibujo. Un diagrama de secuencia lo muestra sin cruces."])

# ---------------------------------------------------------------- 16
add(id="estados", num="16", grupo="Ejecución",
 titulo="Estados de un encargo",
 sub="Por dónde puede pasar un encargo y quién puede moverlo de un estado a otro.",
 fuente="Guía v1.4, Anexo I (estados mínimos) y Anexo III apartado 4",
 simple="Un encargo siempre está en un único estado. Solo puede pasar a los estados que marcan las flechas, y cada cambio deja escrito quién lo hizo, cuándo y por qué. Así nunca se pierde el hilo de un caso.",
 mermaid="""stateDiagram-v2
direction TB
state "Recibido" as Recibido
state "En clasificación" as EnClasificacion
state "Pendiente de información" as PendienteInfo
state "Planificado" as Planificado
state "Escalado" as Escalado
state "Rechazado" as Rechazado
state "En ejecución" as EnEjecucion
state "Bloqueado" as Bloqueado
state "Cancelado" as Cancelado
state "En QA" as EnQA
state "Retrabajo" as Retrabajo
state "Pendiente de aprobación" as PendienteAprobacion
state "Entregado" as Entregado
state "Cerrado" as Cerrado
state "Reabierto" as Reabierto
[*] --> Recibido
Recibido --> EnClasificacion: identidad y cliente validados
EnClasificacion --> PendienteInfo: falta un dato
PendienteInfo --> EnClasificacion: llega la respuesta
EnClasificacion --> Planificado: decisión CONTINUAR
EnClasificacion --> Escalado: riesgo alto
EnClasificacion --> Rechazado: no permitido
Escalado --> Planificado: persona autoriza
Planificado --> EnEjecucion: plan aprobado
EnEjecucion --> Bloqueado: dependencia o error
Bloqueado --> EnEjecucion: causa resuelta
Bloqueado --> Cancelado
EnEjecucion --> EnQA
EnQA --> Retrabajo: no supera
Retrabajo --> EnEjecucion
EnQA --> PendienteAprobacion: riesgo lo exige
EnQA --> Entregado: no requiere aprobación
PendienteAprobacion --> Entregado: aprobado
PendienteAprobacion --> Retrabajo: corregir
Entregado --> Cerrado: aceptado
Cerrado --> Reabierto: con motivo y autorización
Reabierto --> EnClasificacion
Rechazado --> [*]
Cancelado --> [*]
Cerrado --> [*]
""",
 pasos=["Recibido → En clasificación: se validan identidad y cliente.","En clasificación → Pendiente de información / Planificado / Escalado / Rechazado: decisión del CEO con motivo.","Planificado → En ejecución: plan aprobado según riesgo y presupuesto.","En ejecución → Bloqueado / En QA.","En QA → Retrabajo / Pendiente de aprobación / Entregado.","Entregado → Cerrado; Cerrado → Reabierto solo con motivo y autorización."],
 excepciones=["QA no puede aprobar lo que no ha comprobado.","Quien aprueba debe ver la versión exacta; si cambia después, hay que volver a aprobar."],
 artefactos=["Tabla de transiciones permitidas en el código (no texto libre)"],
 correcciones=["Había tres listas de estados que se mezclaban: la del encargo (en español), la de la tarea (en inglés: queued, running…) y la de la instancia de proceso. Se separan: este es el encargo. Las tareas usan sus siete estados y se explican en Procesos."])

ORDER_GROUPS = ["Visión general","El CEO digital","Ejecución","Conocimiento","Seguridad","Calidad y gobierno","Infraestructura","Clientes"]
