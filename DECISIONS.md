# Registro de decisiones

## D-001 — Arquitectura orientada a procesos
- Fecha: 2026-11-17
- Decisión: evolucionar desde una visión centrada en CEO/agentes hacia procesos completos, con CEO como coordinador.
- Motivo: valor en completar procesos con controles, integraciones, medición y trazabilidad.
- Impacto: Process Discovery, Process Engine, Integration Hub, Operational Intelligence y Client Deployment Management.
- Estado: propuesta; validar con primer piloto.

## D-002 — Modelo matricial
Departamentos funcionales reutilizables + especialistas sectoriales activados según contexto. Evitar un agente por combinación. Estado: diseño.

## D-003 — Obsidian como interfaz humana
Obsidian edita y navega Markdown; backend y PostgreSQL gestionan permisos, operaciones y auditoría. Estado: diseño.

## D-004 — PostgreSQL como fuente operativa
PostgreSQL para datos operativos/metadatos; Markdown + Git para conocimiento versionado no confidencial. Estado: diseño.

## D-005 — Aislamiento multi-cliente
Tenant derivado de identidad autenticada y autorización antes de recuperar datos o invocar herramientas. Estado: requisito obligatorio.

## D-006 — Primer proceso piloto
No construir primero un CEO omnisciente; descubrir, diseñar, integrar y medir un proceso real. Estado: siguiente paso recomendado.
## D-007 — Nombre provisional: Varios
- Fecha: 2026-11-17
- Decisión: el proyecto pasa a llamarse "Varios" de forma provisional. Sustituye a ExcluSa / Esclusa / Cauce.
- Motivo: decisión de los socios.
- Impacto: web `site/`, documentos nuevos y la habilidad de marca anterior (hay que adaptarla o retirarla). Identidad visual: burdeos, turquesa y champán; tipografía Instrument Sans.
- Estado: provisional.

## D-008 — Repositorio como memoria oficial y web visual
- Fecha: 2026-11-17
- Decisión: este repositorio es la única fuente de verdad. Se añade `site/` (web visual con simulación), `CLAUDE.md` y `claude/instrucciones-proyecto.md` para dar contexto a una cuenta nueva de Claude.
- Motivo: tener una base de contexto antes de crear la cuenta de Claude del proyecto.
- Estado: aprobada.

## D-009 — Unificación de puertas y estados
- Fecha: 2026-11-17
- Decisión: G0–G6 son las puertas de cliente (una por fase D0–D6, según Atlas Evolución v1.1). Las puertas de lanzamiento de la Guía v1.4 pasan a llamarse L0–L4. Los estados se separan por objeto (encargo, tarea, instancia, definición, conector, despliegue, conocimiento, capacidad).
- Motivo: había tres juegos de puertas con el mismo nombre y listas de estados mezcladas.
- Impacto: `docs/08`, `docs/13`, web (Método, Procesos).
- Estado: aprobada como corrección documental; confirmar entre socios.

## D-010 — Diagramas como código
- Fecha: 2026-11-17
- Decisión: los diagramas viven como Mermaid en `tools/atlas_data.py`, que genera a la vez la web (`site/js/atlas-data.js`) y `docs/atlas/`. Las imágenes de los Word quedan solo como histórico en `archive/originales/`.
- Motivo: los PNG tenían errores y no se podían corregir ni versionar. GitHub dibuja Mermaid directamente.
- Uso: `python3 tools/gen.py site/js/atlas-data.js docs/atlas`
- Estado: aprobada.

## D-011 — Construir primero, clientes desde el 15/02/2027
- Fecha: 2026-11-17
- Decisión: hasta el 12/02/2027 se construye el sistema siguiendo el orden de la Guía v1.4 (§16), con un proceso de referencia y datos inventados. Los clientes empiezan el 15/02/2027.
- Motivo: decisión de los socios. Sustituye al plan anterior, que priorizaba entrevistas comerciales.
- Riesgo aceptado: construir algo que nadie pague. Mitigación: una conversación de validación por semana desde S2, sin vender.
- Impacto: `docs/10-plan-12-semanas.md`, `site/planning.html`.
- Estado: aprobada.

## D-012 — Las propuestas de cambios de Claude se aceptan solas
- Fecha: 2026-11-17
- Decisión: cuando Claude termina un trabajo en el repositorio, abre la propuesta de cambios (pull request) y la acepta él mismo en cuanto no tiene conflictos ni pruebas fallidas. La propuesta queda como registro de qué cambió y por qué.
- Motivo: decisión de los socios; revisar cada propuesta a mano frenaba el trabajo.
- Excepciones (se quedan esperando a un socio): marcar como aprobada una decisión de DECISIONS.md, cambiar CLAUDE.md, cambios en documentos legales (`governance/`, Marco legal) y cualquier cambio con datos reales de clientes o secretos, que además está prohibido.
- Riesgo aceptado: un error llega a la versión principal sin que nadie lo lea antes. Mitigación: cada cambio es una propuesta separada y se puede deshacer; Claude resume en el chat lo que ha aceptado.
- Estado: aprobada.

## D-013 — Conocimiento y catálogo de procesos generados desde datos
- Fecha: 2026-11-17
- Decisión: las fichas de especialistas (`knowledge/<departamento>/`), el índice de navegación, el registro de fuentes y las fichas P01–P38 se generan con `python3 tools/org_gen.py` desde `tools/org_data/`. No se editan a mano; `--check` falla si están desactualizadas.
- Motivo: 25 fichas, 38 procesos y 40 fuentes a mano se contradicen enseguida. Es el mismo patrón que D-010 para los diagramas.
- Riesgo: editar Python para cambiar un texto es menos cómodo. Mitigación: los textos libres (metodologías, plantillas, precedentes) siguen siendo Markdown normal.
- Estado: propuesta.

## D-014 — Adelantar un prototipo mínimo del motor de procesos
- Fecha: 2026-11-17
- Decisión: `src/varios/procesos/` contiene ya un motor en memoria (estados, transiciones, aprobación humana, QA, reintentos, idempotencia y validación de definiciones) con pruebas en `tests/`. Solo Python estándar, pytest y Ruff, que ya están en el stack. Sin FastAPI, PostgreSQL ni persistencia todavía.
- Motivo: fijar en código y pruebas las reglas que hoy solo están en documentos (nadie se aprueba a sí mismo, el tenant sale de la identidad, la IA no cambia estados). Las semanas 1–5 del plan lo sustituirán por la versión persistente.
- Riesgo: parecer más avanzado de lo que está. No es el piloto: no hay base de datos, ni API, ni aislamiento real entre clientes.
- Estado: propuesta.

## D-015 — Entregables en archivos reales, memoria y Google Drive en la oficina de agentes
- Fecha: 2026-11-17
- Decisión:
  - La oficina de agentes genera entregables en `.pptx`, `.xlsx`, `.docx` y diagramas de proceso, con una única plantilla de marca de Varios.
  - Guarda una memoria de encargos, lecciones, correcciones y decisiones que se consulta antes de cada encargo.
  - Puede leer (no escribir) carpetas de Google Drive con el conector del usuario.
  - Para generar y leer archivos usa cinco librerías de navegador sin modificar en `oficina/vendor/`: PptxGenJS, ExcelJS y docx (MIT), JSZip (MIT) y PDF.js (Apache-2.0). Se cargan solo cuando hacen falta.
- Motivo: los socios necesitan entregables utilizables, no solo texto, y que lo hecho sirva para lo siguiente. Las librerías son estándar, se ejecutan en local y no envían datos a terceros.
- Alcance: solo la oficina (artifact). No forman parte del stack del piloto (Python, FastAPI…); si el piloto necesita generar archivos, se decidirá aparte.
- Riesgo: un formato mal generado o una memoria con lecciones equivocadas. Mitigación: todo sale como borrador; los entregables tienen versiones y las entradas de memoria se pueden borrar. Drive solo lee y pide permiso la primera vez.
- Estado: propuesta.

## D-016 — Vista 3D de la oficina de agentes con Three.js
- Fecha: 2026-11-17
- Decisión:
  - La oficina de agentes tiene una vista 3D (botón 3D/2D) hecha sobre `oficina/office.js`, la escena de referencia que aportó Juan, sin reescribirla.
  - Usa Three.js r170 sin modificar en `oficina/vendor/three/` (MIT), solo los módulos que necesita. Se carga únicamente al abrir la vista 3D; si el navegador no tiene WebGL 2, queda el plano 2D.
  - Los agentes caminan entre mesas cuando hablan entre ellos de verdad (CEO que asigna, consulta al experto de sector, entrega a Calidad, piezas al jefe, reuniones). Las conversaciones muestran las líneas reales del trabajo. El botón «Simular conversación» es un ensayo marcado como simulación, sin datos reales.
- Motivo: los socios quieren ver la oficina como una oficina real: quién trabaja, quién espera su OK y quién habla con quién, sin que los textos tapen el plano.
- Alcance: solo la oficina (artifact). No forma parte del stack del piloto.
- Riesgo: rendimiento en equipos sin GPU y 0,8 MB más de librería. Mitigación: calidad adaptativa (sin oclusión ambiental y sombras más ligeras si baja de 45 FPS), carga bajo demanda y vuelta al 2D.
- Estado: propuesta.

## D-017 — La oficina se vuelca cada noche a GitHub y las automatizaciones van por GitHub Actions
- Fecha: 2026-11-17
- Decisión:
  - Cada noche, una tarea programada de Claude lee de la base de datos de la oficina solo lo nuevo (encargos, resultados, conversaciones entre agentes, chats con los socios, memoria, reglas, habilidades, proyectos y decisiones propuestas) y lo vuelca al repositorio con `tools/registro_oficina.py`: copia fiel en `oficina/registro/datos/` y versión legible en `precedents/oficina/`, que entra en el cerebro. Abre una propuesta de cambios y la acepta según D-012. Después publica el cerebro nuevo en la oficina. Instrucciones: `oficina/registro/VOLCADO.md`.
  - Lo que no necesita IA lo hace GitHub Actions: comprobaciones en cada cambio (`ci.yml`), regenerar el cerebro y las fichas cuando cambian documentos (`regenerar.yml`) y los avisos de cada lunes como issue (`avisos.yml`, con `tools/avisos.py`).
  - Las fichas de los 28 agentes y sus 45 habilidades se generan desde `tools/org_data/agentes.py` y `habilidades.py` (`tools/agentes_gen.py`) y la oficina las carga de `oficina/agentes.json`.
- Motivo: los socios quieren que lo que se habla y se hace en la oficina mejore el cerebro sin copiarlo a mano, y gastando los mínimos tokens. La oficina no puede escribir en GitHub por sí misma (no hay conector y no debe guardar credenciales).
- Alternativas descartadas: un token de GitHub dentro de la oficina (secreto expuesto en el navegador); exportar a mano un paquete cada día (se olvida).
- Privacidad: no se vuelca el texto de los documentos subidos, ni los proyectos marcados como confidenciales, ni nada que parezca un secreto. Antes de L2, con clientes reales, hay que revisar este volcado con Legal: el repositorio no es lugar para datos de clientes.
- Riesgo: un volcado con datos que no debían subir. Mitigación: filtros en el script, aceptación con revisión según D-012 y escáner de secretos en `check_repo.py`.
- Estado: propuesta.

## D-018 — El cerebro pasa a ser un grafo de conocimiento con relaciones explicadas
- Fecha: 2026-11-17
- Decisión:
  - `tools/brain_build.py` añade al cerebro un grafo (`tools/grafo.py`) con nodos tipados (documentos, secciones, decisiones, procesos, agentes, especialistas, habilidades, fuentes, puertas y departamentos) y relaciones con etiqueta de confianza: EXTRACTADA (escrita en la fuente, 1,0), INFERIDA (mismo tema; 0,85, 0,75 o 0,65) y AMBIGUA (varios destinos posibles, 0,5).
  - Calcula comunidades de temas (Louvain), nodos centrales, puentes, conexiones sorprendentes, huecos (decisiones que nadie cita, referencias rotas, procesos sin responsable) y preguntas sugeridas, y lo escribe en `knowledge/grafo/INFORME.md`.
  - La oficina da a cada agente, además de las secciones que encajan, lo que esas secciones citan (decisiones con su estado, procesos, fuentes) y hasta tres secciones relacionadas marcadas como INFERIDAS. La vista del cerebro enseña el informe y permite trazar el camino entre dos cosas con la confianza de su eslabón más débil.
- Motivo: la búsqueda por texto encontraba secciones sueltas, pero no lo que las sostiene (la decisión que las justifica, el proceso al que pertenecen). Las ideas vienen de Graphify (Apache-2.0); el código es propio.
- Alternativas descartadas: usar Graphify tal cual (orientado a código; necesita NetworkX, Leiden y un modelo para leer documentos, lo que añade dependencias y tokens); base de datos de grafos (no hace falta con 3.400 nodos).
- Tecnología nueva: ninguna. Python estándar.
- Riesgo: que una relación INFERIDA se tome como hecho. Mitigación: va etiquetada y con puntuación, y el agente recibe la instrucción de comprobarla.
- Estado: propuesta.

## D-019 — Calidad exigente, todo pasa por un socio y cada rechazo se rehace aprendiendo
- Fecha: 2026-11-17
- Decisión (oficina de agentes):
  - Calidad revisa cada entrega con una rúbrica de seis criterios (1 a 5). Cumple solo si todos tienen 4 o más, la media es de 4,5 o más y no queda ningún problema grave ni medio; lo calcula el código. Hasta 4 rondas de corrección.
  - Solo lo que pasa Calidad llega a un socio, y todo lo que la pasa espera su OK, sea cual sea el riesgo. Si no pasa tras 4 rondas, se escala como atasco.
  - Rechazar exige un motivo y relanza el encargo automáticamente con ese motivo y los rechazos anteriores; descartar es otra acción. Lo que dependía de un encargo rehecho se actualiza solo.
  - Aprendizaje: cada rechazo y cada atasco quedan en la memoria; los rechazos generales se vuelven reglas del agente; un mismo tipo de fallo de Calidad en dos encargos se vuelve regla «aprendida de Calidad».
  - Flujo completo en docs/18-flujo-de-calidad-y-aprendizaje.md.
- Motivo: los socios quieren recibir solo trabajo revisado a fondo y que cada corrección mejore la oficina.
- Alcance: la oficina interna. La matriz de aprobaciones por riesgo del producto (docs/14) no cambia.
- Riesgo: más coste en tokens y bucles si Calidad es demasiado dura. Mitigación: máximo 4 rondas por versión y escalado al socio.
- Estado: propuesta.

## D-020 — Seis puestos nuevos en la oficina: CFO, contabilidad, éxito de cliente, plataforma, diseño y cumplimiento
- Fecha: 2026-11-17
- Decisión: la oficina pasa de 28 a 34 agentes, cada uno con ficha senior, reglas, habilidades y ficha de conocimiento con fuentes:
  - Administración: Director financiero (caja, margen, precio, financiación) y Contabilidad y facturación (facturas, cobros, conciliación, cierre, paquete para el gestor).
  - Comercial: Éxito de cliente (plan de éxito, piloto medido, revisión de valor, renovación).
  - Ingeniería: Plataforma y operaciones (integración continua, copias con restauración probada, monitorización, incidentes) y Diseño y experiencia (panel usable por no técnicos, accesibilidad WCAG 2.2 AA).
  - Calidad, seguridad y legal: Cumplimiento normativo (inventario de IA, registro de tratamientos, alfabetización del art. 4, matriz de evidencias).
- Motivo: cubrir huecos del plan hasta el 12/02/2027 (forma jurídica y facturación, precio, CI y copias, panel de S10) y lo que necesitará el primer cliente regulado. Recursos humanos y alianzas se dejan para cuando haya contrataciones o nicho elegido.
- Riesgo: más agentes, más coordinación y más tokens. Mitigación: cada puesto tiene límites claros y el CEO solo los convoca cuando el encargo lo pide.
- Estado: propuesta.

## D-021 — El cerebro se abre en Obsidian: el repositorio es el vault
- Fecha: 2026-11-18
- Decisión: desarrolla D-003. El repositorio entero se abre como vault de Obsidian, sin copia aparte:
  - Las fichas generadas (agentes, habilidades, especialistas, procesos) llevan propiedades YAML planas (tipo, departamento, estado…).
  - tools/obsidian_gen.py, llamado desde tools/brain_build.py, escribe en knowledge/grafo/ una nota por decisión y por fuente con quién las cita, un mapa por comunidad del grafo, el Mapa del cerebro y seis vistas de Bases (tablas nativas de Obsidian 1.9 o posterior).
  - .obsidian/ versiona solo app.json, core-plugins.json y graph.json (colores por carpeta); el estado local de cada persona queda fuera por .gitignore.
  - Sincronización con el plugin de la comunidad Obsidian Git: traer cambios al abrir y cada pocos minutos; subir cambios a mano. La autenticación con GitHub la hace cada socio en su equipo; no se guarda ningún token en el repositorio.
  - Guía en docs/19-obsidian.md.
- Motivo: los socios quieren navegar y editar el cerebro con un editor cómodo y ver el grafo, sin un servicio nuevo ni coste de tokens.
- Tecnología nueva: Obsidian (aplicación de escritorio gratuita, ya instalada por un socio) y su plugin Obsidian Git. No entra en el stack del piloto ni en producción; los datos siguen siendo Markdown en Git.
- Riesgo: que alguien edite a mano un archivo generado y CI lo pise o falle. Mitigación: Inicio.md y cada nota generada dicen qué no se edita; CI comprueba que lo generado está al día.
- Estado: propuesta.

## D-022 — Trabajo nocturno de Claude con plan diario e informe de la mañana
- Fecha: 2026-11-26
- Decisión: Claude trabaja de noche sobre una lista que Juan elige cada día (`docs/21-trabajo-nocturno.md`) y deja un informe a las 07:50 en docs/informes/. El plan hasta el 28/02/2027, el ritual diario y el formato del informe están en `docs/22-plan-hasta-febrero.md`. Solo se programan las tandas de la noche siguiente, nunca semanas por adelantado. Lo nocturno entra directamente en main, por petición de Juan; esta excepción a D-012 no se aplica a CLAUDE.md ni a decisiones aprobadas.
- Motivo: avanzar el plan de 12 semanas y los cinco pilares (producto, oficina, cerebro, entregables, web y empresa) con horas de Claude que no compiten con las de los socios.
- Riesgo: trabajo sin revisión que se acumula o se aleja del plan. Mitigación: cada tarea tiene un «hecho cuando» y sus pruebas, el informe dice qué comprobar y lo que falla, y Juan elige cada día.
- Estado: aprobada (Juan, 26/11/2026, al fusionar la propuesta de cambios).

## D-023 — Base de datos real: PostgreSQL con RLS, auditoría inmutable y conocimiento con citas
- Fecha: 2026-11-26
- Decisión: adelanta S1–S2 del plan y parte de S3 y S7. Consiste en:
  - una API FastAPI con `/health`;
  - Docker Compose con PostgreSQL 16;
  - el modelo de datos de S2 con Alembic (`src/varios/db/`, `migrations/`);
  - RLS forzada en todas las tablas, con el cliente fijado por transacción;
  - el usuario de aplicación `varios_app`, sin privilegios;
  - auditoría que no se puede modificar ni borrar;
  - tablas de conocimiento (`fuente`, `ficha_conocimiento`) con búsqueda en español que exige fuente.

  Las pruebas corren contra PostgreSQL real, en CI como servicio. Detalle en `docs/24-base-de-datos.md`.
- Tecnología nueva dentro del stack ya decidido: SQLAlchemy 2 (base de Alembic), psycopg 3 (controlador de PostgreSQL), uvicorn (servidor de FastAPI) y pydantic-settings (configuración por entorno). No añaden servicios ni coste.
- Motivo: los socios pidieron una base de datos real esta noche, y el aislamiento entre clientes es la regla que más daño hace si falla. Mejor fijarla en la base de datos desde el primer día que añadirla después.
- Riesgo: adelantar código antes de validar el proceso. Mitigación: el modelo es genérico (encargos, tareas, aprobaciones) y no depende del sector. El motor en memoria (D-014) sigue igual hasta S5.
- Estado: aprobada (Juan, 26/11/2026, al fusionar la propuesta de cambios).

## D-024 — Paquete de dominio de seguros con un archivo máquina como fuente de las reglas
- Fecha: 2026-11-26
- Decisión: el conocimiento del sector del proceso de referencia vive en `knowledge/sectores/seguros/`: normas con artículo y fuente oficial, glosario, catálogo de excepciones y `dominio.json` con plazos, excepciones, campos mínimos del expediente y términos. El código fijo del proceso leerá los plazos y los disparadores de `dominio.json`; los Markdown son la explicación para personas, y una prueba (`tests/test_dominio_seguros.py`) comprueba que coinciden y que todo cita una fuente del registro. Mientras un abogado no fije la base jurídica, el proceso de referencia no guarda datos de salud.
- Motivo: «código fijo para reglas y cálculos». Una sola fuente de las reglas evita que el motor, las pruebas de C1 y la documentación digan cosas distintas.
- Riesgo: que una norma cambie y el archivo quede viejo. Mitigación: cada plazo lleva su fuente con fecha de lectura y las fuentes en `draft` están marcadas; revisar antes de usar con un cliente.
- Estado: aprobada (Juan, 26/11/2026, al fusionar la propuesta de cambios).

## D-025 — La oficina se organiza en siete secciones y se abre en Inicio
- Fecha: 2026-11-26
- Decisión: la oficina tiene una barra de secciones siempre visible: Inicio, Encargos, Proyectos, Clientes, Cerebro, Calendario y Agentes (la planta 2D/3D). Las acciones van aparte. Se abre en Inicio, con lo que espera a un socio primero, y quien lo prefiera puede entrar por la planta. Auditoría, referencias y siguientes pasos en `docs/25-portal-interno.md`.
- Motivo: lo primero que necesita un socio es lo que espera su OK. Además, la navegación oculta o tapada hace el trabajo más lento (NN/g), y las referencias de gestión de trabajo (Linear, Basecamp, GitHub) separan la bandeja de lo que pide atención del resto.
- Riesgo: cambiar la costumbre de entrada. Mitigación: no se quita nada, las teclas de antes siguen y la casilla «Abrir la oficina aquí» devuelve la entrada por la planta.
- Estado: propuesta.

## D-026 — Cada agente sirve a un proceso medido: de 34 se quedan 22
- Fecha: 2026-11-26
- Decisión: se mantienen 22 agentes, 5 se fusionan con otro (Registro de decisiones con Plan y seguimiento; Validación y Contenido con el Jefe comercial; Cumplimiento con Legal; Costes con el Director financiero) y 7 se retiran sin borrar su ficha (Administración, Contabilidad y los expertos de sanidad, despachos, financiero, industria y logística), cada uno con la condición para recuperarlo. De 65 habilidades se mantienen 56, se fusionan 3 y se retiran 6. Detalle, cobertura por proceso y métricas en `docs/28-auditoria-agentes.md`; fuente máquina en `tools/org_data/auditoria.py`. Revisa D-020.
- Motivo: «proceso antes que agente» (CLAUDE.md) y la recomendación de Anthropic de empezar por lo más simple y añadir complejidad solo cuando hace falta (fuente `ANTHROPIC-AGENTES`). Con 0 clientes y un solo proceso de referencia (D-011), un agente sin proceso no se puede medir ni probar.
- Alternativas descartadas: mantener los 34 (más rutas que probar y más tokens sin trabajo que hacer); retirar también Éxito de cliente y Diseño (P37, P38 y P10 los necesitan antes del primer piloto).
- Riesgo: perder conocimiento de sectores retirados. Mitigación: las fichas de knowledge/ se conservan y una oportunidad del sector que pase P31 los recupera. Una prueba (`tests/test_auditoria_agentes.py`) impide añadir un agente sin proceso y métrica.
- Estado: propuesta. Hasta que se apruebe no se toca `agentes.py`.

## D-027 — Cada proceso tiene un nivel de autonomía A0–A4 con techo y criterio
- Fecha: 2026-11-26
- Decisión: mapa de autonomía de los 38 procesos y del proceso de referencia en `processes/autonomia.json` (documento generado: `docs/29-autonomia.md`). Hoy todos están en A0; objetivo para el 12/02/2027 con datos inventados: 9 en A0, 21 en A1, 3 en A2 y 6 en A3. Los 23 que tocan algo externo, legal, financiero o contractual tienen el techo en A2 y la aprobación humana (P10) en A1. Los pasos que el catálogo da a una persona siguen siendo de una persona en cualquier nivel, y un proceso con pasos humanos no llega a A4 (corregido el 26/11 a las 23:40: P15 y P35 lo tenían). Se sube un nivel cada vez, si la métrica cumple el umbral 4 semanas seguidas sin fallos graves y lo aprueba un socio; se baja a A1 en el acto con un fallo grave.
- Motivo: docs/22 («La autonomía se gana con datos»), CLAUDE.md (aprobación humana en lo externo, financiero, legal y contractual) y la Guía v1.4 §3. Los niveles se inspiran en los cinco papeles del usuario de Feng, McDonald y Zhang (`KNIGHT-NIVELES-AUTONOMIA`), sin coincidir uno a uno (A2 no tiene equivalente y A4 conserva el muestreo humano que su L5 no tiene; corregido el 27/11, ver docs/29): la autonomía es una decisión de diseño, no una consecuencia de la capacidad.
- Alternativas descartadas: un nivel por agente en vez de por proceso (el riesgo está en la acción, no en quién la hace; Guía v1.4 §3: «clasificar cada tarea»).
- Riesgo: que un nivel suba por costumbre. Mitigación: `tests/test_autonomia.py` falla si algo sensible pasa de A2; el periodo de 4 semanas y el umbral los fijan los socios.
- Estado: propuesta.

## D-028 — La oficina guarda en la API: identidad por token firmado y PyJWT
- Fecha: 2026-11-26
- Decisión: la API expone encargos, tareas y aprobaciones sobre las tablas de D-023 (`src/varios/api/oficina.py`, rutas en `docs/24-base-de-datos.md`). Cada petición lleva un JWT firmado (HS256, con `exp`, `iss` y `aud` obligatorios) del que sale el usuario y el cliente; los roles y si es persona se leen de la base, no del token. Una sola transacción por petición con el cliente fijado (RLS): si una regla falla, no se guarda nada. Lo de otro cliente responde 404, igual que lo que no existe. Se añade la librería PyJWT. La API sirve también la oficina en `/oficina/` para que use la misma dirección (N3b, sin CORS).
- Motivo: CLAUDE.md (el cliente sale de la identidad autenticada) y las hojas de OWASP: la de FastAPI recomienda PyJWT con algoritmo fijo y `exp`, `iss` y `aud` obligatorios (`OWASP-FASTAPI`); la de IDOR, comprobar el acceso por objeto en cada petición y responder igual si no existe (`OWASP-IDOR`). PyJWT es lo que verificará también los tokens del proveedor de identidad (OIDC) cuando llegue: solo cambia `identidad.verificar`.
- Alternativas descartadas: cabeceras con el usuario y el cliente (son datos que envía el usuario); un token propio con hmac de la biblioteca estándar (reinventar JWT y rehacerlo con el proveedor real); esperar al proveedor de identidad (bloquea N3b y S5).
- Riesgo: un secreto compartido HS256 filtrado permite crear tokens. Mitigación: secreto solo en el entorno (`VARIOS_JWT_SECRETO`, mínimo 32 caracteres), tokens de 60 minutos, ningún dato real hasta L2 y sustitución por el proveedor de identidad antes de L2 (decisión pendiente de Juan).
- Estado: propuesta.

## D-029 — El trabajo nocturno de Claude sube directo a `main`, sin propuesta de cambios
- Fecha: 2026-11-27 (registra lo que Juan pidió el 26/11/2026; anotado por la tanda de las 04:00)
- Decisión: de noche Claude no abre propuestas de cambios ni crea ramas: cada tarea va en un commit a `main` con `bash tools/comprobar.sh` en verde, y se explica en el Registro de `docs/21-trabajo-nocturno.md` y en el informe de la mañana (`docs/21`, «Orden en GitHub»). Siguen fuera de este camino las mismas excepciones que en D-012: marcar una decisión como aprobada y cambiar `CLAUDE.md`. Falta decidir qué pasa con los documentos de `governance/`, que D-012 también deja esperando a un socio (pregunta 9 de `docs/21`).
- Motivo: Juan lo pidió el 26/11/2026 («los socios lo pidieron así», `docs/21`) para que las tandas no dejen ramas sueltas ni propuestas sin fusionar; con el borrado automático de ramas activado, las propuestas de una noche de seis tandas eran ruido. No estaba en DECISIONS.md, aunque cambia cómo se aplica D-012.
- Alternativas descartadas: una propuesta por tanda aceptada sola (D-012 tal cual), que dejaba ramas y no añadía revisión humana.
- Riesgo: un error llega a `main` sin que nadie lo lea. Mitigación: comprobaciones de CI en cada subida, la siguiente tanda arregla un CI en rojo antes de nada, repaso crítico al final de cada noche y el Registro con lo que cambió.
- Estado: propuesta.

## D-030 — La oficina mejora evolucionando sus instrucciones contra un examen, no sus modelos
- Fecha: 2026-11-27
- Decisión: amplía el bucle de mejora diaria (M-044). Además de convertir errores repetidos en reglas (D-019), la oficina evoluciona el texto que gobierna a cada agente y proceso (instrucciones, reglas y fichas) al estilo de GEPA (fuente `GEPA-2026`): genera varias versiones a partir de las trazas y de lo que falló, las examina todas con el mismo banco de casos y conserva las que mejoran sin empeorar nada. Reglas:
  1. Sin examen no hay evolución: solo se evoluciona lo que tiene su banco de casos (primero el Control A de la semana 4; después el examen de 50 casos de la semana 9).
  2. Un conjunto de casos reservado que el optimizador nunca ve decide si una versión gana, para no aprender a aprobar el examen.
  3. Varias métricas a la vez (calidad de la rúbrica, coste, tiempo y cero fallos de seguridad o de aislamiento); una versión que empeora la seguridad se descarta aunque suba la nota.
  4. Nunca se despliega sola: la versión ganadora es una propuesta que pasa por P16 y P23 y aprueba un socio; en procesos con techo A2 (D-027), los dos.
  5. Cada versión queda guardada con su nota, su examen y quién la aprobó, y se puede volver atrás.
- Motivo: los socios quieren que la oficina mejore cada día. La neuroevolución clásica (fuente `NEAT-2002`) evoluciona pesos y topología de redes neuronales, y Varios no entrena modelos: usa Claude por API. Lo que sí se puede mejorar es el texto que lo rodea, y es lo que GEPA ha mostrado que funciona.
- Tecnología: GEPA o DSPy serían nuevas. No entran con esta decisión: en la semana 9 se compara usar GEPA o DSPy con un bucle propio más simple y se propone en una decisión aparte.
- Alternativas descartadas: entrenar o ajustar un modelo propio (coste, datos reales que no tenemos y riesgo regulatorio); cambiar instrucciones a mano sin examen (no se sabe si mejora).
- Riesgo: sobreajuste a un banco pequeño (25 o 50 casos) y coste de las ejecuciones. Mitigación: casos reservados, presupuesto por ejecución (M-046) y aprobación humana.
- Estado: propuesta.

## D-031 — Posponer, caducar y tareas se guardan en la API; una aprobación caducada vuelve como pregunta
- Fecha: 2026-11-27 (tanda de las 22:00, N3c)
- Decisión: con la API, la oficina deja de tener estas reglas solo en el navegador:
  1. **Caducar.** Toda aprobación pedida en la API lleva `caduca_en` (72 h por defecto, `VARIOS_APROBACION_CADUCA_H`; plazo propuesto en N4, lo fijan los socios). Al vencer, la aprobación queda `caducada` sin aprobador y el encargo pasa de PENDIENTE_APROBACION a ESCALADO («una persona decide cómo seguir»): vuelve como pregunta y nunca se aprueba sola (P10: «nunca aprobación tácita»; D-019). Es una transición nueva de `encargo.json` (versión 1.1.0), marcada como añadida y por confirmar, y no se puede hacer con un cambio de estado libre: solo la hace la caducidad, firmada como `sistema:caducidad`.
  2. **Cómo se caduca.** Sin proceso aparte: al empezar cada petición de un cliente, en una transacción propia y con su RLS, se caducan sus aprobaciones vencidas (como la expiración pasiva de Redis, fuente `REDIS-EXPIRE`). Un cliente nunca caduca lo de otro. La oficina lo lee cada minuto.
  3. **Posponer.** `POST /encargos/{id}/posponer` guarda `pospuesto_hasta` con su evento. Solo una persona, solo si el encargo espera a alguien (PENDIENTE_APROBACION, PENDIENTE_INFO, ESCALADO o BLOQUEADO), como mucho 7 días (`VARIOS_POSPONER_MAX_DIAS`, propuesta). No para la caducidad y se pierde al cambiar de estado, como en la oficina.
  4. **Tareas.** `POST /tareas/{id}/estado` con la máquina de `objetos.json`; las piezas de un encargo en equipo se suben como tareas. Una tarea en `needs_approval` solo la da por buena una persona con rol de aprobación que no la puso a esperar.
  5. **Decidir desde otra oficina.** Lo que llega de la API se puede aprobar, devolver o descartar desde otra oficina del mismo cliente; la API sigue sin aceptar que decida quien la pidió o quien es autor.
- Motivo: N3c (resto de M-041). Hasta ahora, si una aprobación caducaba en la oficina, en la API seguía pendiente, y posponer y las piezas solo existían en un navegador.
- Tecnología: ninguna nueva (migración 0003 de Alembic).
- Alternativas descartadas: un proceso programado que caduque (otra pieza que desplegar y vigilar en el piloto; se puede añadir después con la misma función `caducar_vencidas`); caducar a RETRABAJO (sube la versión y pide rehacer algo que nadie ha rechazado); dejar la aprobación pendiente para siempre (es lo que pasaba y contradice P10).
- Riesgo: la caducidad solo ocurre cuando ese cliente hace alguna petición, así que la base puede guardar como pendiente algo ya vencido hasta entonces; nadie puede decidirlo porque decidir comprueba el plazo. Cada petición hace una consulta más (índice parcial sobre las pendientes).
- Estado: propuesta.

## D-032 — La cartera de pólizas del cliente se guarda en su propia tabla
- Fecha: 2026-11-27 (tanda de las 22:00, A5)
- Decisión: tabla `poliza` (número, ramo, aseguradora, efecto y vencimiento) por cliente, con RLS forzada como el resto (migración 0004). Es la copia de la cartera que usan las reglas fijas de apertura de siniestros (`varios.seguros.apertura`), que hasta ahora solo existía en `cartera.json`. Los siniestros del proceso de referencia se guardan como encargos (`solicitud`), sin tabla propia.
- Motivo: A5 pide cargar en la base las 11 pólizas inventadas repartidas entre los dos clientes, y no había dónde. Una tabla con columnas (no un JSON genérico) deja que la base compruebe la vigencia y que un cliente no repita número.
- Alternativas descartadas: una tabla genérica de «datos del cliente» en JSON (sin comprobaciones y más fácil de llenar de cualquier cosa); dejar la cartera en archivos (no es multicliente ni pasa por RLS).
- Riesgo: es la primera tabla de un sector concreto en el núcleo. Si Varios trabaja en otros sectores (pregunta 11), cada uno traerá las suyas; habrá que decidir si van en un esquema por sector.
- Tecnología: ninguna nueva.
- Estado: propuesta.

## D-033 — Identidad: Keycloak autoalojado para el piloto; los roles siguen en la base de Varios
- Fecha: 2026-11-27 (tanda de las 22:00, S3a)
- Decisión (propuesta, sin añadir nada todavía): comparativa en `docs/31-identidad.md`. Para el piloto, Keycloak autoalojado en el mismo Docker Compose, con su propia base en nuestro PostgreSQL, OpenID Connect y segundo factor obligatorio para los socios (passkey o TOTP). La API verificaría RS256 con las claves públicas del proveedor, con `exp`, `iss` y `aud` obligatorios. Con cualquier proveedor: el proveedor dice quién es; los roles se leen de la base de Varios y lo que diga el token sobre roles se ignora; el cliente sale del token y tiene que casar con un usuario activo de ese cliente; el sujeto del proveedor (`iss` + `sub`) se enlaza con el usuario de Varios con una columna nueva.
- Motivo: M-047 y S3; el token de hoy (HS256 con un secreto compartido, D-028) no vale para L2. Keycloak tiene licencia Apache 2.0, es proyecto de la CNCF, trae passkeys y TOTP y deja los datos en nuestro servidor (fuentes `KEYCLOAK-REPO`, `CNCF-KEYCLOAK`, `KEYCLOAK-ADMIN`).
- Alternativas: Microsoft Entra External ID (gratis hasta 50.000 usuarios activos al mes, sin servidor; región de datos y segundo factor sin confirmar; buena si ya usáis Microsoft 365, pregunta 12 de docs/21); Zitadel (AGPL 3.0 desde la v3: revisar con el abogado antes de ofrecerlo modificado a clientes); authentik (parte *enterprise* con licencia propia sin leer); Authlib con una cuenta que ya tengáis (no es un proveedor).
- Tecnología que entraría al aprobarla: Keycloak (contenedor) y el extra `crypto` de PyJWT (`cryptography`) para RS256. Ninguna se añade con esta propuesta.
- Riesgo: alrededor de 1,25 GB más de memoria en el servidor según la guía de Keycloak (`KEYCLOAK-SIZING`) y una pieza más que actualizar. Mitigación: imagen fijada por versión y copia de su base con las de Varios.
- Pruebas: `tests/db/test_identidad_proveedor.py` con un proveedor simulado (roles socio, agente y cliente; emisor, audiencia, caducidad, firma, `nbf` y `alg: none`).
- Estado: propuesta.

## Decisiones pendientes (con fecha límite)
| Decisión | Quién | Antes de |
|---|---|---|
| Acuerdo entre socios: roles, horas, reparto, salida | Los dos | 22/11/2026 |
| Plan de Claude | Juan | 22/11/2026 |
| Proceso de referencia (por defecto: siniestros en corredurías) | Los dos | 22/11/2026 |
| Forma jurídica y facturación | Álvaro, con gestor | 08/01/2027 |
| Umbral de acierto del examen | Los dos | 22/01/2027 |
| Precio del diagnóstico y del piloto | Los dos | 29/01/2027 |
| Alojamiento de la demo y región de datos | Juan | 05/02/2027 |
| Nicho comercial para salir a vender | Los dos | 12/02/2027 |
| Proveedor de identidad para producción | Juan | Antes de L2 |
