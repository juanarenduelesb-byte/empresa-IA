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
- Decisión: Claude trabaja de noche sobre una lista que Juan elige cada día ([docs/21-trabajo-nocturno.md](docs/21-trabajo-nocturno.md)) y deja un informe a las 07:50 en docs/informes/. El plan hasta el 28/02/2027, el ritual diario y el formato del informe están en [docs/22-plan-hasta-febrero.md](docs/22-plan-hasta-febrero.md). Solo se programan las tandas de la noche siguiente, nunca semanas por adelantado. Lo nocturno entra directamente en main, por petición de Juan; esta excepción a D-012 no se aplica a CLAUDE.md ni a decisiones aprobadas.
- Motivo: avanzar el plan de 12 semanas y los cinco pilares (producto, oficina, cerebro, entregables, web y empresa) con horas de Claude que no compiten con las de los socios.
- Riesgo: trabajo sin revisión que se acumula o se aleja del plan. Mitigación: cada tarea tiene un «hecho cuando» y sus pruebas, el informe dice qué comprobar y lo que falla, y Juan elige cada día.
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
