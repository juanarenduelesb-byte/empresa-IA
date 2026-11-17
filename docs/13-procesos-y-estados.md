# Procesos y estados

Versión visual e interactiva: `site/procesos.html`.

## Catálogo P01–P38

P01–P18 y P19–P30 vienen de la Guía v1.4; P31–P38 del Atlas de Evolución v1.1. La columna "Cuándo" sigue el orden recomendado de implementación de la Guía v1.4 y el backlog del Atlas de Evolución.

| ID | Proceso | Qué hace | Cuándo |
|---|---|---|---|
| P01 | Alta y recepción de petición | Registrar solicitante, cliente, objetivo, alcance, plazo, formato y restricciones | MVP |
| P02 | Clasificación y triaje | Sector, proceso, tipo de problema, complejidad, sensibilidad, riesgo e incertidumbre | MVP |
| P03 | Gestión de aclaraciones | Detectar datos que faltan, preguntar y bloquear tareas dependientes | MVP |
| P04 | Recuperación de conocimiento | Fuentes autorizadas, filtro por permisos, citas | MVP |
| P05 | Diseño del plan | Tareas, dependencias, responsables, herramientas y criterios | MVP |
| P06 | Asignación y coordinación | Departamentos y especialistas; carga, estados, bloqueos, escalados | MVP |
| P07 | Ingesta documental | Tipo, origen, integridad, metadatos, clasificación, permisos, versión; original conservado | Antes de datos reales |
| P08 | Ejecución de tareas | Análisis, reglas, código o automatizaciones con límites y registro | MVP |
| P09 | Control de calidad | Formato, completitud, coherencia, cálculos, fuentes, pruebas, criterios | MVP |
| P10 | Aprobación humana | Decisiones sensibles, acciones externas, entregas reguladas, alto impacto | MVP |
| P11 | Entrega y cierre | Artefactos, evidencias, limitaciones, métricas, aceptación | MVP |
| P12 | Gestión de cambios | Alcance, datos, modelo, reglas o herramientas; versionar y replanificar | Antes de escalar |
| P13 | Aprendizaje y wiki | Proponer, revisar, aprobar, versionar y retirar conocimiento | Antes de escalar |
| P14 | Permisos y aislamiento | Identidades, roles, cliente, ámbitos, pruebas de separación | Antes de datos reales |
| P15 | Observabilidad e incidencias | Registros, costes, tiempos, errores, decisiones, incidentes | MVP |
| P16 | Gobierno de modelos y prompts | Inventario, versiones, instrucciones, límites, evaluaciones, alternativas | Antes de escalar |
| P17 | Seguridad y continuidad | Secretos, copias, restauración, vulnerabilidades, dependencias | Antes de datos reales |
| P18 | Evaluación y mejora | Calidad, tiempo, coste, retrabajo, satisfacción | Antes de escalar |
| P19 | Política de uso y límites | Permitido, prohibido, condicionado; límites de autonomía | Antes de automatizar |
| P20 | Entradas seguras y prompt injection | Todo contenido externo es dato no confiable | Antes de datos reales |
| P21 | Ejecución segura de herramientas | Autorización por acción, mínimo privilegio, sandbox | Antes de automatizar |
| P22 | Errores y reintentos | Clasificar, limitar, idempotencia, alternativa, escalado | Antes de automatizar |
| P23 | Evaluación de agentes y modelos | Casos de prueba, umbrales, regresión | Antes de escalar |
| P24 | Ciclo de vida del dato | Finalidad, retención, rectificación, borrado incluso en copias | Antes de datos reales |
| P25 | Cambios y versiones | Versionar todo, probar aparte, aprobar, revertir | Antes de escalar |
| P26 | Continuidad y recuperación | RPO/RTO, copias cifradas, restauraciones reales, procedimiento manual | Antes de escalar |
| P27 | Proveedores y dependencias | Privacidad, ubicación, condiciones, salida | Antes de datos reales |
| P28 | Gestión de incidentes | Detectar, contener, preservar, notificar, recuperar, aprender | Antes de escalar |
| P29 | Costes y capacidad | Presupuestos, límites, alertas, cuotas | Antes de automatizar |
| P30 | Identidades y secretos | Autenticación, roles, rotación; nunca secretos en prompts, logs o repos | Antes de datos reales |
| P31 | Calificación de oportunidad | Problema, sponsor, encaje, impacto, riesgo, go/no-go | MVP |
| P32 | Descubrimiento de procesos | Entrevistas, AS-IS, variantes, excepciones, línea base | MVP |
| P33 | Diseño y validación TO-BE | Modelo futuro, reglas, controles, RACI, KPI, aprobación cliente | MVP |
| P34 | Definiciones de proceso | Versiones, responsable, estados, pruebas, publicación | MVP |
| P35 | Instancias y excepciones | Estados, plazos, reintentos, escalado, compensación | MVP |
| P36 | Catálogo de conectores | Alta, permisos, versiones, pruebas, revocación | Antes de automatizar |
| P37 | Medición de rendimiento y valor | Línea base, KPI, ROI, adopción, atribución | MVP |
| P38 | Despliegue por cliente | Fases D0–D6, puertas, riesgos, aceptación | Antes de datos reales |

## Estados (separados por objeto)

Los documentos originales mezclaban tres listas. Se separan así:

| Objeto | Camino normal | Alternativos |
|---|---|---|
| Encargo | Recibido → En clasificación → Pendiente de información → Planificado → En ejecución → En QA → Pendiente de aprobación → Entregado → Cerrado | Bloqueado, Escalado, Retrabajo, Rechazado, Cancelado, Reabierto |
| Tarea | queued → running → needs_approval → succeeded | blocked, failed, cancelled |
| Instancia de proceso | created → ready → running → waiting_external / waiting_human → completed | exception, failed, cancelled |
| Definición de proceso | draft → under_review → approved → active → deprecated → retired | — |
| Conector | draft → tested → approved → active → retired | degraded, suspended |
| Despliegue en cliente | qualified → discovery → design → prototype → pilot → production → operating | paused, terminated |
| Ficha de conocimiento | raw → draft → validated → approved → deprecated | disputed |
| Capacidad | draft → tested → approved → deprecated | — |

Diagrama del encargo: `docs/atlas/16-estados.md`. Implementar como enums con transiciones autorizadas, no como texto libre.
