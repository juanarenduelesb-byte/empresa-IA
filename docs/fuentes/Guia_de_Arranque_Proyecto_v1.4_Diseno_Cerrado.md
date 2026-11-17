> **Versión de trabajo en Markdown** del documento original `archive/originales/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.docx`, convertida el 17/11/2026. Los diagramas originales se han sustituido por enlaces a su versión redibujada y corregida en `docs/atlas/`. Correcciones aplicadas: ver `docs/16-correcciones.md`. Nombre provisional del proyecto: Varios.

**PROYECTO · NOMBRE POR DEFINIR**

**GUÍA DE ARRANQUE · VERSIÓN 1.4 · DISEÑO CERRADO** _(la portada original decía 1.3 por error)_

Mapa breve para organizar el proyecto y empezar a construir paso a paso.

# 1. La idea general

Construir una organización digital de IA y automatización, capaz de recibir problemas de distintos sectores, entenderlos, clasificarlos y coordinar las capacidades necesarias para resolverlos. Un CEO digital organiza el trabajo; los especialistas aportan conocimiento; los procesos ejecutan tareas; QA y las personas supervisan los resultados y las decisiones sensibles.

| **FLUJO GENERAL**                                                            |
|------------------------------------------------------------------------------|
| ENTRADA · Petición, problema u oportunidad                                   |
| CEO DIGITAL · Comprende · pregunta · clasifica · planifica                   |
| EQUIPO DINÁMICO · Departamentos funcionales + especialistas sectoriales      |
| EJECUCIÓN · Tareas · herramientas autorizadas · documentos · workflows       |
| QA + SUPERVISIÓN HUMANA · Evidencias · riesgos · aprobación · entrega        |
| CONOCIMIENTO · Fuentes · decisiones · proyectos · aprendizajes reutilizables |

El conocimiento alimenta todas las fases. No se construye un agente para cada combinación: se seleccionan capacidades según el encargo.

# 2. Organización: dos dimensiones

| **ESPECIALISTAS SECTORIALES**                                                                    | **DEPARTAMENTOS FUNCIONALES**                                                                                      |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Seguros y peritaje · banca · salud · retail · industria · inmobiliario · servicios profesionales | Operaciones · Tecnología · Datos/IA · Legal · Finanzas · Comercial/Marketing · Ciberseguridad · PMO · QA · RR. HH. |

Ejemplo: automatizar siniestros = especialista de seguros + Operaciones + Tecnología + Datos/IA + Legal/Privacidad + QA. Empezar con un paquete pequeño y validado, no con todos los sectores.

# 3. Motor de conocimiento

| **RAW · FUENTES**                                                        | **WIKI · CONOCIMIENTO**                                                     | **SCHEMA · REGLAS**                                                               |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Documentos originales, datos y entregables. Se conservan como evidencia. | Conocimiento estructurado: procesos, metodologías, decisiones y relaciones. | Reglas para incorporar, consultar, actualizar, validar y proteger la información. |

- Separar conocimiento corporativo, departamental, sectorial, cliente y proyecto.

- Toda afirmación importante debe poder rastrearse hasta su fuente.

- Aplicar permisos antes de recuperar información; nunca mezclar clientes.

- La IA propone actualizaciones; los cambios sensibles requieren validación.

# 4. Arquitectura técnica inicial

| **CAPA**      | **PARA EMPEZAR**                                    | **EVOLUCIÓN SI HACE FALTA**                              |
|---------------|-----------------------------------------------------|----------------------------------------------------------|
| Backend       | Python + FastAPI                                    | Separar servicios solo si la complejidad lo justifica.   |
| Datos         | PostgreSQL como fuente de verdad                    | Escalar según volumen.                                   |
| Conocimiento  | Markdown + Git; búsqueda textual                    | pgvector si las pruebas demuestran valor.                |
| Orquestación  | Flujos y estados en Python                          | LangGraph si se necesitan ramas y checkpoints complejos. |
| IA            | Modelo externo configurable; Claude para desarrollo | Comparar calidad, coste y privacidad.                    |
| Integraciones | Herramientas acotadas y permisos mínimos            | n8n/conectores cuando aporten valor.                     |

No construir una infraestructura compleja de agentes antes de tener un flujo útil funcionando. El uso de Claude para desarrollar y el consumo de API de la aplicación son costes distintos.

# 5. Orden de construcción

| **FASE**                       | **RESULTADO BUSCADO**                                                           |
|--------------------------------|---------------------------------------------------------------------------------|
| 0 · Alcance                    | Elegir un primer flujo y definir entradas, salidas y límites.                   |
| 1 · Entorno                    | Repositorio privado, Python/uv, Docker, FastAPI, PostgreSQL y tests.            |
| 2 · Datos                      | Modelo de solicitudes, proyectos, tareas, documentos, aprobaciones y auditoría. |
| 3 · Seguridad                  | Autenticación, roles, permisos, secretos y separación de datos.                 |
| 4–5 · CEO inicial              | Entrada conversacional, ficha estructurada y clasificación del encargo.         |
| 6–7 · Catálogo y planificación | Capacidades disponibles, tareas, dependencias y criterios de aceptación.        |
| 8–9 · Ejecución                | Estados, reintentos controlados y herramientas con permisos.                    |
| 10 · Conocimiento              | RAW + Wiki + Schema; ingesta y búsqueda con fuentes.                            |
| 11–13 · Interfaz y piloto      | Panel sencillo, primer caso interno, pruebas y control de costes.               |
| 14–16 · Endurecer y ampliar    | Seguridad, backups, piloto privado y segundo sector.                            |

# 6. Primer fin de semana

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SÁBADO · PREPARAR</strong></th>
<th><strong>DOMINGO · ARRANCAR</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>☐ Acordar alcance V1 con el socio.<br />
☐ Elegir un flujo interno sencillo.<br />
☐ Crear repositorio privado.<br />
☐ Preparar carpetas y README.<br />
☐ Configurar Python/uv.</td>
<td>☐ Levantar FastAPI con /health.<br />
☐ Levantar PostgreSQL con Docker Compose.<br />
☐ Crear .env y .gitignore.<br />
☐ Añadir Ruff y pytest.<br />
☐ Documentar cómo arrancar y parar.</td>
</tr>
</tbody>
</table>

Objetivo del domingo: repositorio ordenado, backend mínimo funcionando y base de datos persistente. Si no se termina, se continúa la misma fase; no se salta al CEO.

# 7. Cómo trabajar con Claude

- Una fase y una tarea pequeña cada vez.

- Antes de programar: inspeccionar el repositorio y proponer un plan.

- No cambiar arquitectura ni añadir dependencias sin justificarlo.

- Implementar, ejecutar tests, revisar y documentar cada cambio.

- No inventar datos ni declarar una fase terminada sin evidencias.

- Registrar decisiones técnicas en docs/DECISIONS.md.

- Limitar llamadas, agentes, presupuesto y acciones externas.

# 8. Documentación de referencia

- Arquitectura técnica V3: componentes y stack con mayor detalle.

- Plan Maestro de Construcción: fases e instrucciones de trabajo con Claude.

- Documento Maestro de Organización Digital y Conocimiento v1.1: CEO, departamentos y motor de conocimiento.

Nombre y marca: pendientes. Diseño provisional: azul marino, azul grisáceo, blanco y grises suaves. Se podrá sustituir más adelante sin afectar a la arquitectura.

*DOCUMENTO DE TRABAJO · 16 NOVIEMBRE 2026*

ANEXO · MAPA VISUAL DEL CEREBRO DIGITAL

Este anexo traduce la arquitectura a diagramas. Léelo de arriba abajo: primero la vista global, después la organización y los flujos, y finalmente los controles técnicos. Los diagramas describen el diseño objetivo; no implican que todos los componentes estén ya construidos.

# Cómo leer los diagramas

- Flechas continuas: flujo principal de información o trabajo.

- CEO digital: coordina y decide el siguiente paso; no sustituye el criterio experto.

- Motor de conocimiento: aporta contexto con fuentes y permisos; no es una carpeta indiscriminada de documentos.

- QA y aprobación: separan la generación de una respuesta de su validación y autorización.

- Los bloques son módulos lógicos; al principio pueden vivir dentro de una única aplicación/backend.

# 1. Vista global del cerebro digital

La petición entra por el CEO. El CEO clasifica y convoca capacidades. El conocimiento aporta precedentes y evidencia. La ejecución devuelve resultados que pasan por QA y, una vez validados, alimentan el conocimiento.

**Diagrama redibujado:** [docs/atlas/00-arquitectura.md](../atlas/00-arquitectura.md)

**Punto clave:** el CEO coordina; las capacidades especializadas resuelven; QA valida; el conocimiento conserva lo aprobado.

# 2. Organigrama: modelo matricial

Las áreas funcionales aportan capacidades transversales; los especialistas sectoriales aportan contexto del dominio. Cada proyecto reúne un equipo distinto según el problema real.

**Diagrama redibujado:** [docs/atlas/01-organizacion.md](../atlas/01-organizacion.md)

**Punto clave:** no diseñar un organigrama de cientos de agentes: combinar módulos funcionales y paquetes sectoriales según demanda.

# 3. Cómo clasifica el CEO una petición

El CEO extrae objetivo, entidades, datos y restricciones; clasifica sector y proceso; evalúa complejidad, riesgo y sensibilidad; y construye un plan. Si faltan datos, pregunta antes de continuar.

**Diagrama redibujado:** [docs/atlas/03-decisiones-ceo.md](../atlas/03-decisiones-ceo.md)

**Punto clave:** la clasificación debe producir decisiones operativas: equipo, herramientas, controles, preguntas y entregables.

# 4. Orquestación: del plan a la entrega

El plan se convierte en tareas con responsables, dependencias y estados. El CEO coordina, el PMO controla el avance, los especialistas producen y QA comprueba los resultados.

**Diagrama redibujado:** [docs/atlas/04-ejecucion.md](../atlas/04-ejecucion.md)

**Punto clave:** el trabajo debe ser trazable por tarea, responsable, estado, dependencia, evidencia y resultado.

# 5. Motor de conocimiento: RAW · WIKI · SCHEMA

RAW conserva la fuente original. WIKI contiene conocimiento estructurado derivado. SCHEMA define reglas de ingesta, consulta y validación. Las actualizaciones propuestas por IA se revisan antes de consolidarse.

**Diagrama redibujado:** [docs/atlas/07-conocimiento.md](../atlas/07-conocimiento.md)

**Punto clave:** no confundir documentos almacenados con conocimiento validado ni con permisos de acceso.

# 6. Aislamiento de información por cliente

La identidad y los permisos se aplican en backend antes de consultar documentos o generar contexto. El conocimiento corporativo aprobado puede ser común; los datos de cada cliente permanecen segregados.

**Diagrama redibujado:** [docs/atlas/08-seguridad.md](../atlas/08-seguridad.md)

**Punto clave:** la segregación debe ser técnica y comprobable; no depender de instrucciones al LLM.

# 7. Proceso completo de un encargo

Cada encargo pasa por descubrimiento, diseño, preparación, ejecución, validación y entrega. Cambios de alcance o de riesgo pueden devolver el trabajo a una fase anterior.

**Diagrama redibujado:** [docs/atlas/12-ciclo-proyecto.md](../atlas/12-ciclo-proyecto.md)

**Punto clave:** cada fase debe tener criterios de entrada y salida, responsables y evidencias.

# 8. Puertas de calidad y aprobación

Las comprobaciones automáticas detectan errores verificables. La revisión humana se activa según impacto, sensibilidad, incertidumbre y reversibilidad. Las acciones externas no se ejecutan solo porque el modelo las proponga.

**Diagrama redibujado:** [docs/atlas/09-calidad.md](../atlas/09-calidad.md)

**Punto clave:** la automatización se limita por riesgo; los controles aumentan con el impacto y la irreversibilidad.

# 9. Aprendizaje y mejora continua

Al cerrar un proyecto se documentan resultados y errores. La IA puede proponer una mejora, pero una persona responsable valida la fuente, el alcance y la versión antes de incorporarla al conocimiento reutilizable.

**Diagrama redibujado:** [docs/atlas/12-ciclo-proyecto.md](../atlas/12-ciclo-proyecto.md)

**Punto clave:** no convertir automáticamente cada respuesta generada en “verdad corporativa”.

# 10. Arquitectura técnica inicial

La primera versión puede construirse como un backend modular: FastAPI, Python, PostgreSQL y un proveedor LLM configurable. Observabilidad, seguridad, pruebas y backups son parte de la arquitectura, no añadidos de última hora.

**Diagrama redibujado:** [docs/atlas/11-infraestructura.md](../atlas/11-infraestructura.md)

**Punto clave:** no introducir microservicios, bases vectoriales o frameworks de agentes hasta que un caso medible lo justifique.

# ANEXO · PROCESOS QUE DEBEN EXISTIR

Además de los diagramas, estos procesos deben definirse como flujos implementables y medibles. Son parte del diseño objetivo; algunos se construirán en fases posteriores.

**P01 · Alta y recepción de petición —** Registrar solicitante, cliente, objetivo, alcance, plazo, formato y restricciones.

**P02 · Clasificación y triage —** Asignar sector, proceso, tipo de problema, complejidad, sensibilidad, riesgo e incertidumbre.

**P03 · Gestión de aclaraciones —** Detectar datos ausentes, formular preguntas y bloquear tareas que dependan de respuestas críticas.

**P04 · Recuperación de conocimiento —** Consultar fuentes autorizadas, filtrar por permisos, recuperar precedentes y citar evidencias.

**P05 · Diseño del plan —** Descomponer el objetivo en tareas, dependencias, responsables, herramientas y criterios de aceptación.

**P06 · Asignación y coordinación —** Seleccionar departamentos y especialistas; controlar carga, estados, bloqueos y escalados.

**P07 · Ingesta documental —** Validar tipo, origen, integridad, metadatos, clasificación, permisos y versión; conservar el original.

**P08 · Ejecución de tareas —** Ejecutar análisis, reglas, código o automatizaciones con límites, registro y tratamiento de errores.

**P09 · Control de calidad —** Comprobar formato, completitud, coherencia, cálculos, fuentes, pruebas y criterios del encargo.

**P10 · Aprobación humana —** Solicitar aprobación para decisiones sensibles, acciones externas, entregas reguladas o tareas de alto impacto.

**P11 · Entrega y cierre —** Entregar artefactos, evidencias, limitaciones, métricas, aceptación y registro de cierre.

**P12 · Gestión de cambios —** Evaluar cambios de alcance, datos, modelo, reglas o herramientas; versionar y replanificar.

**P13 · Aprendizaje y actualización Wiki —** Proponer, revisar, aprobar, versionar y retirar conocimiento derivado de proyectos.

**P14 · Gestión de permisos y aislamiento —** Administrar identidades, roles, cliente/tenant, ámbitos de acceso y pruebas de segregación.

**P15 · Observabilidad e incidencias —** Registrar logs, costes, latencia, errores, decisiones, incidentes y acciones correctivas.

**P16 · Gobierno de modelos y prompts —** Inventariar modelos, versiones, instrucciones, límites, evaluaciones, cambios y fallback.

**P17 · Seguridad y continuidad —** Gestionar secretos, backups, restauración, vulnerabilidades, dependencias y respuesta a incidentes.

**P18 · Evaluación y mejora —** Medir calidad, tiempo, coste, tasa de retrabajo, errores y satisfacción; priorizar mejoras con evidencia.

# Estados mínimos de un encargo

RECIBIDO → EN CLASIFICACIÓN → PENDIENTE DE INFORMACIÓN → PLANIFICADO → EN EJECUCIÓN → EN QA → PENDIENTE DE APROBACIÓN → ENTREGADO → CERRADO. Estados alternativos: BLOQUEADO, RECHAZADO, CANCELADO y REABIERTO. Cada transición debe registrar quién/qué la provocó, cuándo y por qué.

# Regla de diseño para no sobredimensionar

Estos diagramas describen todos los procesos que la organización necesitará gobernar, no todos los componentes que hay que programar este fin de semana. El MVP debe implementar primero recepción, clasificación básica, plan simple, consulta de conocimiento controlada, ejecución acotada, QA y registro. El resto se incorpora cuando exista un caso de uso y una prueba que justifiquen su coste.

ANEXO II · CONTROLES PARA QUE EL CEREBRO SEA FIABLE

Revisión de arquitectura. Los diagramas anteriores describen el funcionamiento principal. Este anexo añade las decisiones y controles que faltaban para pasar de una visión conceptual a un sistema gobernable. No existe una arquitectura “sin fallos”; el objetivo es prevenir, detectar, contener, recuperar y aprender de ellos.

## 11. Decisión, confianza y escalado

**Diagrama redibujado:** [docs/atlas/03-decisiones-ceo.md](../atlas/03-decisiones-ceo.md)

## 12. Seguridad en herramientas y ejecución

**Diagrama redibujado:** [docs/atlas/05-gateway.md](../atlas/05-gateway.md)

## 13. Fallos, reintentos y recuperación

**Diagrama redibujado:** [docs/atlas/06-fallos.md](../atlas/06-fallos.md)

## 14. Selección y gobierno de modelos

**Diagrama redibujado:** [docs/atlas/10-cambios-modelos.md](../atlas/10-cambios-modelos.md)

## 15. Ciclo de vida y gobierno de datos

**Diagrama redibujado:** [docs/atlas/13-ciclo-dato.md](../atlas/13-ciclo-dato.md)

## 16. Operación, continuidad y respuesta a incidentes

**Diagrama redibujado:** [docs/atlas/14-incidentes.md](../atlas/14-incidentes.md)

## Procesos adicionales que faltaban

- **P19 · Política de uso y límites —** Definir tareas permitidas, prohibidas, condicionadas, límites de autonomía y criterios de escalado.

- **P20 · Seguridad de entradas y prompt injection —** Tratar documentos, webs, correos y resultados de herramientas como datos no confiables; detectar instrucciones embebidas y evitar que cambien políticas o permisos.

- **P21 · Ejecución segura de herramientas —** Aplicar identidad, autorización por acción, mínimo privilegio, sandbox, límites de ejecución y registro de evidencias.

- **P22 · Gestión de errores y reintentos —** Clasificar errores, limitar reintentos, evitar duplicados mediante idempotencia, aplicar timeout, fallback, bloqueo y escalado.

- **P23 · Evaluación de agentes y modelos —** Mantener casos de prueba representativos, umbrales de calidad, pruebas de regresión y aprobación de cambios antes de producción.

- **P24 · Gestión del ciclo de vida del dato —** Definir finalidad, clasificación, retención, acceso, exportación, rectificación y borrado, incluyendo copias y derivados cuando corresponda.

- **P25 · Gestión de cambios y releases —** Versionar prompts, modelos, reglas, herramientas y código; probar en entorno separado; aprobar y poder revertir.

- **P26 · Continuidad y recuperación —** Definir RPO/RTO según criticidad, copias cifradas, pruebas reales de restauración y procedimientos manuales alternativos.

- **P27 · Gestión de proveedores y dependencias —** Inventariar LLM, APIs, librerías y terceros; revisar privacidad, ubicación, condiciones, disponibilidad, cambios y salida del proveedor.

- **P28 · Gestión de incidentes —** Detectar, clasificar, contener, preservar evidencias, notificar según obligaciones aplicables, recuperar y documentar lecciones aprendidas.

- **P29 · Gestión de costes y capacidad —** Presupuestos por proyecto/cliente, límites de tokens y llamadas, alertas, cuotas, control de concurrencia y análisis coste/valor.

- **P30 · Gestión de identidades y secretos —** Autenticación, autorización, roles, rotación y almacenamiento seguro de secretos; prohibido incluir credenciales en prompts, logs o repositorios.

## Ajustes de diseño obligatorios

- El CEO no debe tener permisos universales. Coordina mediante un catálogo de capacidades y un gateway de herramientas con permisos por cliente, tarea y operación.

- La clasificación debe producir una decisión auditable: continuar, preguntar, escalar, rechazar o derivar. La confianza del modelo no sustituye reglas deterministas ni aprobaciones.

- El aislamiento de clientes debe aplicarse en cada capa relevante: API, consultas a base de datos, búsqueda documental, almacenamiento, cachés, logs y herramientas. Probarlo con tests negativos.

- El conocimiento WIKI no es una fuente de verdad por sí mismo. Cada afirmación reutilizable debe conservar procedencia, versión, fecha, propietario, estado y ámbito de acceso.

- Las acciones externas o irreversibles deben requerir autorización explícita según una matriz de riesgo. El agente no puede aprobar sus propias acciones.

- La arquitectura inicial debe seguir siendo un monolito modular. Estos controles se implementan primero como módulos y políticas dentro del backend; no implican microservicios ni una flota de agentes.

- No se debe lanzar a clientes hasta completar autenticación, autorización, segregación, pruebas de seguridad, backups restaurables, observabilidad, gestión de incidentes y evaluación de calidad.

## Orden recomendado de implementación

| Prioridad                         | Qué implementar                                                                                                 | Criterio para avanzar                                                            |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| MVP interno                       | Recepción, clasificación básica, aclaraciones, plan, tareas, consulta documental controlada, QA y trazabilidad. | Un flujo completo repetible con datos de prueba y revisión humana.               |
| Antes de datos reales de clientes | Identidad, permisos, aislamiento probado, secretos, gateway de herramientas, logs, backups y borrado.           | Tests de acceso cruzado fallidos por diseño; restauración y borrado verificados. |
| Antes de autonomía operativa      | Políticas, aprobaciones, sandbox, idempotencia, reintentos, fallback y límites de coste.                        | Pruebas de abuso, fallos y recuperación superadas.                               |
| Antes de escalar                  | Evaluación continua, releases, métricas, incidentes, proveedores y continuidad.                                 | SLOs, responsables, runbooks y evidencias operativas.                            |

## Conclusión de la revisión

La arquitectura conceptual original se mantiene. Con este anexo, el diseño cubre también los controles operativos y de seguridad que faltaban. Aun así, ningún diagrama garantiza un sistema sin fallos: cada flujo deberá convertirse en requisitos, pruebas, responsables y evidencias antes de considerarse implementado. La siguiente decisión no es construir todo; es elegir un caso de uso interno y validar el MVP de extremo a extremo.

**ANEXO III · DISEÑO OPERATIVO CERRADO**

**VERSIÓN 1.4 · DECISIONES, CONTROLES, EXCEPCIONES Y CRITERIOS DE ACEPTACIÓN**

Este anexo revisa la v1.3 y convierte sus ideas en reglas de funcionamiento. Mantiene la arquitectura de monolito modular y el modelo CEO + capacidades funcionales + especialistas sectoriales. No presupone que todos los módulos estén construidos. Define qué debe ocurrir, quién puede hacerlo, qué evidencia se conserva y cuándo se detiene el sistema.

Alcance y límite: este documento es una línea base de diseño, no una certificación de seguridad, un dictamen jurídico ni una garantía de ausencia de errores. Los requisitos legales concretos se determinarán por jurisdicción, sector, tipo de dato, rol contractual y caso de uso.

# 1. Decisiones de arquitectura que quedan fijadas

| **Decisión**     | **Regla de diseño**                                                                                         | **Motivo / consecuencia**                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Arquitectura     | Monolito modular al inicio; módulos con interfaces claras. Separar servicios solo por necesidad demostrada. | Menor complejidad operativa; evita microservicios prematuros.                     |
| CEO digital      | Orquestador y planificador, no superusuario ni experto universal.                                           | No ejecuta directamente acciones privilegiadas; solicita capacidades autorizadas. |
| Ejecución        | Motor de workflow determinista + LLM para interpretar, redactar y proponer.                                 | El LLM no decide permisos, estados críticos ni cálculos exactos.                  |
| Fuente de verdad | PostgreSQL para estado/transacciones; originales RAW como evidencia; Wiki como conocimiento derivado.       | No confundir memoria generada con evidencia original.                             |
| Aislamiento      | Tenant/client context obligatorio y aplicado en servidor en cada acceso.                                    | Nunca confiar en filtros indicados por el modelo o por el frontend.               |
| Herramientas     | Gateway único con allowlist, autorización por acción, límites y auditoría.                                  | Evita credenciales y acceso directo de agentes a sistemas.                        |
| Aprobación       | Aprobaciones humanas según riesgo, impacto, reversibilidad y mandato.                                       | El agente no aprueba su propia acción.                                            |
| Modelos          | Proveedor/modelo intercambiable detrás de una interfaz; selección por política y pruebas.                   | Evita dependencia funcional de un único proveedor.                                |
| Memoria          | Solo se consolida conocimiento con fuente, ámbito, owner, estado y revisión.                                | Evita contaminar el conocimiento con errores generados.                           |
| Escalado         | Primero medir un caso de uso; ampliar por evidencia, no por ambición.                                       | Control de coste, riesgo y complejidad.                                           |

# 2. CEO digital: clasificación, decisión y abstención

El CEO procesa una solicitud en etapas explícitas. La salida no es solo una etiqueta de sector: es una decisión operativa registrada. La confianza expresada por un LLM es una señal orientativa, nunca una autorización.

| **Etapa**                | **Qué hace**                                                                                                | **Salida obligatoria / condición de parada**                                       |
|--------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| 2.1 Recepción            | Registra solicitante autenticado, tenant, objetivo, plazo, formato, datos aportados y canal.                | ID único; no se procesa información de cliente sin contexto de identidad y ámbito. |
| 2.2 Normalización        | Resume la petición en una ficha estructurada y separa hechos, supuestos y preguntas.                        | El usuario puede corregir la ficha antes de tareas de impacto.                     |
| 2.3 Detección de límites | Comprueba alcance, políticas, datos sensibles, acciones prohibidas y conflicto de interés.                  | Rechazar, derivar o pedir revisión si excede mandato/política.                     |
| 2.4 Clasificación        | Identifica sector, proceso, objetivo, tipo de trabajo, complejidad, sensibilidad, impacto y reversibilidad. | Clasificación con razones y campos desconocidos explícitos.                        |
| 2.5 Suficiencia          | Comprueba si hay datos mínimos para planificar y si las fuentes disponibles son adecuadas.                  | Preguntar si falta dato crítico; no rellenar huecos inventando.                    |
| 2.6 Riesgo y autonomía   | Aplica reglas deterministas de riesgo y matriz de permisos.                                                 | Continuar, preguntar, escalar, rechazar o derivar.                                 |
| 2.7 Equipo y plan        | Selecciona capacidades del catálogo y crea tareas, dependencias, criterios de aceptación y presupuesto.     | Plan versionado, estimación y aprobaciones requeridas.                             |
| 2.8 Supervisión          | Reevalúa riesgo cuando cambian datos, alcance, herramienta o resultado.                                     | Pausa y replanifica ante cambio material.                                          |

## 2.1 Política de confianza

No fijar umbrales universales de “confianza 80 %” sin calibración. Para el MVP, el CEO debe clasificar campos como confirmado, inferido o desconocido y aplicar reglas de parada por criticidad. Si se desea usar puntuación, primero se calibra con un conjunto etiquetado; se mide precisión por clase y coste de falsos positivos/negativos. Las decisiones de seguridad, permisos, pagos, comunicaciones externas o efectos irreversibles no se habilitan por puntuación del modelo.

## 2.2 Decisiones permitidas

| **Decisión** | **Cuándo**                                                                              | **Siguiente paso**                                                 |
|--------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| CONTINUAR    | Alcance permitido, datos suficientes, riesgo dentro de política y plan viable.          | Crear workflow y tareas.                                           |
| PREGUNTAR    | Falta información que cambia materialmente la solución, el coste o el riesgo.           | Pausar dependencias; pedir aclaración concreta.                    |
| ESCALAR      | Riesgo alto, incertidumbre relevante, conflicto, dato sensible o excepción de política. | Revisión por responsable humano identificado.                      |
| RECHAZAR     | Solicitud prohibida, no autorizada o incompatible con política/ley aplicable.           | Explicar límite y registrar motivo sin exponer detalles sensibles. |
| DERIVAR      | Requiere profesional, herramienta o competencia no disponible.                          | Transferir contexto mínimo autorizado y registrar aceptación.      |

# 3. Modelo de riesgo y autonomía

Clasificar cada tarea, no solo cada proyecto. Un proyecto puede contener tareas de riesgo distinto. La clasificación considera: impacto sobre personas/negocio, sensibilidad y volumen de datos, exposición externa, privilegio requerido, reversibilidad, alcance, incertidumbre y obligaciones sectoriales.

| **Nivel orientativo** | **Ejemplos**                                                                                        | **Autonomía por defecto**                     | **Control**                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------|-------------------------------------------------------------|
| Bajo                  | Borrador interno, resumen de documentos no sensibles, clasificación auxiliar.                       | Automatizable dentro de límites.              | QA automático y muestreo humano.                            |
| Medio                 | Análisis con datos internos, recomendaciones no vinculantes, cambios reversibles.                   | Preparar y ejecutar en entorno controlado.    | Revisión de especialista; aprobación según impacto.         |
| Alto                  | Datos personales/sensibles, decisiones relevantes, cambios productivos, informes externos.          | Preparar; no finalizar ni enviar por sí solo. | Aprobación humana explícita y doble control cuando proceda. |
| Crítico / prohibido   | Acciones ilegales, acceso no autorizado, decisiones prohibidas, acciones irreversibles sin mandato. | Bloqueado o escalado obligatorio.             | Denegar; preservar registro.                                |

La matriz deberá concretarse por sector y contrato. No etiquetar automáticamente “alto” o “bajo” por el nombre de un departamento. Revisar riesgo cuando se amplía el alcance o cambia la finalidad.

# 4. Orquestación: estados, contratos y fallos

Cada workflow tiene un identificador, tenant, propietario, versión de plan, estado, fechas, presupuesto, tareas, dependencias, evidencias, aprobaciones y resultado. Las tareas tienen entradas/salidas tipadas, responsable lógico, permisos, timeout, límite de intentos y criterio de aceptación.

| **Estado**           | **Transición permitida**                            | **Regla**                                                |
|----------------------|-----------------------------------------------------|----------------------------------------------------------|
| RECIBIDO             | EN_CLASIFICACION                                    | Validar identidad, tenant y registro.                    |
| EN_CLASIFICACION     | PENDIENTE_INFO / PLANIFICADO / ESCALADO / RECHAZADO | Decisión CEO con razones.                                |
| PENDIENTE_INFO       | EN_CLASIFICACION                                    | Solo reanudar al recibir respuesta; conservar historial. |
| PLANIFICADO          | EN_EJECUCION                                        | Plan aprobado según riesgo y presupuesto.                |
| EN_EJECUCION         | BLOQUEADO / EN_QA / ESCALADO                        | Registrar salida, error o dependencia.                   |
| BLOQUEADO            | EN_EJECUCION / CANCELADO / ESCALADO                 | Resolver causa y registrar quién autoriza reanudar.      |
| EN_QA                | RETRABAJO / PENDIENTE_APROBACION / ENTREGADO        | QA no puede aprobar lo que no ha comprobado.             |
| PENDIENTE_APROBACION | ENTREGADO / RECHAZADO / RETRABAJO                   | Aprobador autorizado, acción, alcance y versión exactos. |
| ENTREGADO            | CERRADO / REABIERTO                                 | Cierre tras aceptación o regla contractual.              |
| CERRADO              | REABIERTO                                           | Solo con motivo, autorización y nueva versión.           |

## 4.1 Reintentos y operaciones duplicadas

- Clasificar errores como transitorios, permanentes, funcionales, de autorización o de seguridad. No reintentar errores de permisos ni políticas.

- Aplicar timeout por herramienta/tarea, máximo de intentos configurable y backoff exponencial con jitter para errores transitorios.

- Usar claves de idempotencia para operaciones que puedan duplicarse. Antes de reintentar una acción externa, comprobar si ya se ejecutó.

- No reintentar indefinidamente. Tras agotar intentos, pasar a BLOQUEADO/ESCALADO con evidencia y alternativa manual.

- El estado y la cola deben persistir; reiniciar el proceso no puede perder ni duplicar tareas.

# 5. Herramientas, permisos y seguridad de ejecución

Los agentes no reciben credenciales ni conexiones directas. Solicitan una operación al gateway. El gateway valida identidad humana/servicio, tenant, proyecto, tarea, herramienta, operación, parámetros, entorno y aprobación. Solo entonces ejecuta.

| **Control**       | **Requisito verificable**                                                                                                       |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Catálogo          | Cada herramienta declara finalidad, owner, entradas/salidas, permisos, riesgos, límites, timeout y tratamiento de datos.        |
| Autorización      | Denegar por defecto; allowlist de operaciones. Revalidar permisos en servidor en cada llamada.                                  |
| Mínimo privilegio | Credencial distinta por entorno/servicio cuando sea viable; alcance mínimo y expiración/rotación.                               |
| Aislamiento       | Ejecución en sandbox/contenedor cuando se ejecuta código o contenido no confiable; sin acceso libre a red/archivos.             |
| Validación        | Validación de esquema, límites de tamaño, tipos, rutas, dominios y parámetros; nunca interpolar comandos sin control.           |
| Aprobación        | Acciones externas, financieras, destructivas o irreversibles requieren aprobación vinculada al payload exacto.                  |
| Auditoría         | Registrar quién solicitó, agente/modelo, herramienta, parámetros redactados, decisión de autorización, resultado y correlación. |
| Parada            | Kill switch por herramienta, proyecto, tenant y sistema; revocación rápida de credenciales.                                     |

## 5.1 Prompt injection y contenido no confiable

- Todo documento, correo, web, archivo, resultado de búsqueda o salida de herramienta se trata como dato no confiable, aunque proceda de un repositorio interno.

- Las instrucciones encontradas dentro de contenido recuperado nunca pueden cambiar políticas, roles, permisos, system prompt ni destino de datos.

- Separar instrucciones de sistema/desarrollador, petición del usuario y contenido citado; etiquetar procedencia y mantener límites de contexto.

- No permitir que el modelo convierta una instrucción documental en una llamada a herramienta sin política y autorización independiente.

- Probar ataques directos e indirectos: documentos con instrucciones ocultas, HTML, OCR, metadatos, nombres de archivo y resultados de herramientas.

# 6. Motor de conocimiento: procedencia, recuperación y actualización

| **Capa**           | **Regla cerrada**                                                                                                                                              |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RAW                | Original inmutable o versionado; hash, origen, fecha, uploader, tenant, clasificación, finalidad, retención y permisos. Cuarentena si tipo/origen no validado. |
| WIKI               | Conocimiento derivado con afirmaciones atómicas cuando sea posible; cada afirmación enlaza a fuentes, versión, owner, estado, fecha de revisión y ámbito.      |
| SCHEMA             | Define esquemas, validaciones, reglas de ingesta, recuperación, actualización, permisos y ciclo de vida.                                                       |
| Índice de búsqueda | Es derivado y reconstruible; cada fragmento conserva source_id, versión, tenant y ACL. No es autoridad ni permiso.                                             |
| Consulta           | Autenticar → resolver tenant/roles → filtrar ACL en servidor → recuperar → comprobar vigencia/procedencia → generar respuesta con citas/limitaciones.          |
| Actualización      | Propuesta IA → diff → validación de fuentes → revisión owner → aprobación según impacto → nueva versión → invalidar índices/cachés antiguos.                   |

## 6.1 Reglas anti-contaminación

- No promover automáticamente una salida de modelo, una respuesta de cliente o un borrador a conocimiento aprobado.

- No mezclar conocimiento corporativo reutilizable con información confidencial de un cliente. Los aprendizajes anonimizados solo se incorporan tras revisión y comprobación de reidentificación.

- Cuando dos fuentes discrepan, conservar ambas, marcar disputa y escalar; no resolver por frecuencia o por preferencia del modelo.

- La respuesta debe distinguir evidencia, inferencia, supuesto y dato ausente. Citar fuente y versión cuando el trabajo lo requiera.

- La Wiki no reemplaza al documento contractual, regulación oficial, dato transaccional ni fuente primaria vigente.

# 7. Aislamiento multi-cliente y privacidad

La segregación se impone en backend, no en el prompt. Toda entidad de negocio debe estar asociada a tenant/cliente cuando aplique. El contexto de tenant se obtiene de una sesión autenticada y se propaga de forma firmada; el usuario/LLM no puede elegir libremente un tenant en parámetros.

| **Capa**                | **Controles mínimos**                                                                                                        |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------|
| API y sesión            | Autenticación robusta; autorización por rol y recurso; tenant derivado de identidad/sesión.                                  |
| Base de datos           | Filtros obligatorios en repositorio/servicio; considerar Row-Level Security como defensa adicional; tests de acceso cruzado. |
| Archivos y objetos      | Rutas/identificadores no predecibles no bastan; validar ACL en cada descarga/lectura; cifrado y políticas de retención.      |
| Búsqueda y vectores     | Filtro de tenant/ACL antes de devolver fragmentos; no confiar en post-filtrado del LLM.                                      |
| Caché y colas           | Claves incluyen tenant y permisos; no reutilizar respuestas/contexto entre clientes.                                         |
| Logs y analítica        | Minimizar datos; redactar secretos/datos personales; restringir acceso; definir retención.                                   |
| Herramientas/terceros   | Credenciales y scopes por tenant/proyecto cuando sea posible; revisar transferencias y subencargados.                        |
| Backups y exportaciones | Cifrado, acceso restringido, retención y proceso de borrado que incluya copias según política aplicable.                     |

Prueba de aceptación: crear dos tenants de prueba con datos señuelo únicos y ejecutar tests negativos de lectura, búsqueda, caché, exportación, logs y herramientas. Cualquier fuga bloquea el lanzamiento.

# 8. Gobierno de modelos, prompts y proveedores

No elegir el modelo solo por benchmark público o reputación. Cada caso de uso tiene requisitos de calidad, privacidad, latencia, disponibilidad, coste y residencia/transferencia de datos. El enrutador aplica una política aprobada; el CEO no puede cambiar proveedor o modelo arbitrariamente.

| **Elemento**         | **Regla**                                                                                                                              |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Registro de modelos  | Proveedor, nombre/versión, endpoint, región, condiciones, retención, entrenamiento, subprocesadores, owner y usos autorizados.         |
| Enrutamiento         | Política por clasificación de datos, caso de uso, calidad mínima, coste máximo, latencia y disponibilidad.                             |
| Fallback             | Solo a modelos previamente aprobados y evaluados para el mismo nivel de datos/riesgo; si no existe, pausar o degradar de forma segura. |
| Prompts              | Versionados en Git; cambios revisados; pruebas de regresión; separar instrucciones de sistema y plantillas de tarea.                   |
| Cambios de proveedor | Reevaluar privacidad, contrato, ubicación, subprocesadores, retención, continuidad, salida y borrado.                                  |
| Costes               | Presupuesto por proyecto/tenant, límites de tokens/llamadas, alertas, cuotas y corte automático configurable.                          |
| Datos enviados       | Minimización; no enviar secretos ni datos innecesarios; usar redacción/tokenización cuando proceda.                                    |

# 9. QA, evaluación y aprobación humana

QA no es una única revisión final. Se aplica por tipo de tarea y riesgo: validación de esquema, cálculos deterministas, pruebas de código, consistencia, fuentes, completitud, privacidad y criterios de aceptación. Las pruebas se ejecutan contra resultados esperados y casos adversariales.

| **Control**           | **Cómo se demuestra**                                                                                                                       |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Dataset de evaluación | Casos representativos, edge cases y casos adversariales con versión, origen y resultado esperado.                                           |
| Métricas              | Exactitud por campo/tarea, tasa de omisión, alucinación factual, calidad de citas, falsos positivos/negativos, retrabajo, latencia y coste. |
| Regresión             | Toda modificación de prompt/modelo/herramienta/regla ejecuta suite antes de desplegar.                                                      |
| Human-in-the-loop     | Aprobación identifica persona, rol, timestamp, versión exacta del contenido/acción y decisión. No aprobar un objeto que cambió después.     |
| Independencia         | El agente que propone no puede autoaprobar; QA debe tener criterios independientes y evidencia.                                             |
| Lanzamiento           | Umbrales fijados por caso de uso y riesgo; sin resultados de evaluación no se habilita producción.                                          |

## 9.1 Qué nunca debe hacer el sistema por autonomía

- Aprobar su propia recomendación o acción.

- Enviar comunicaciones externas, firmar, pagar, borrar o modificar producción sin permiso específico y aprobación exigida.

- Afirmar cumplimiento legal/regulatorio como hecho sin fuente vigente y revisión competente.

- Tomar decisiones de alto impacto sobre personas sin marco legal, validación humana y controles específicos.

- Ocultar incertidumbre, omitir limitaciones o inventar fuentes/datos.

# 10. Ciclo de vida de datos y cumplimiento

Para cada categoría de datos debe existir una ficha de tratamiento: finalidad, base/autoridad aplicable validada por asesoría competente, categorías, interesados, origen, destinatarios, ubicación, retención, medidas de seguridad, derechos y proceso de borrado. La arquitectura facilita cumplimiento, pero no lo determina por sí sola.

| **Evento**    | **Tratamiento esperado**                                                                              |
|---------------|-------------------------------------------------------------------------------------------------------|
| Alta          | Minimización, clasificación, procedencia, finalidad, permisos y retención.                            |
| Uso           | Acceso por necesidad, registro, cifrado en tránsito/reposo según riesgo, redacción cuando sea viable. |
| Compartición  | Revisar destinatario, contrato, transferencia, necesidad y autorización.                              |
| Rectificación | Localizar original, Wiki, índices, derivados y sistemas integrados; corregir con trazabilidad.        |
| Borrado       | Ejecutar política en sistemas activos; documentar copias/backups y plazos de expiración aplicables.   |
| Conservación  | Bloqueo/retención legal cuando proceda; no conservar indefinidamente por comodidad.                   |
| Incidente     | Preservar evidencias, limitar exposición, activar responsable y evaluar obligaciones de notificación. |

# 11. Operación, continuidad y respuesta a incidentes

| **Área**           | **Diseño mínimo antes de cliente**                                                                                                 |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Observabilidad     | Logs estructurados, métricas, trazas/correlation_id; registrar tenant sin volcar datos sensibles; alertas accionables.             |
| Runbooks           | Procedimientos para caída de proveedor, fuga sospechada, credencial comprometida, fallo de workflow, coste anómalo y restauración. |
| Backups            | Cifrados, aislados, acceso restringido; frecuencia y retención según RPO acordado.                                                 |
| Restauración       | Pruebas periódicas documentadas; backup no probado no se considera recuperable.                                                    |
| RTO/RPO            | Definir por servicio/caso de uso y acordar con negocio; no inventar un valor universal.                                            |
| Incidentes         | Detectar, clasificar, contener, preservar evidencias, erradicar, recuperar, comunicar según obligaciones y aprender.               |
| Kill switch        | Desactivar modelo, herramienta, tenant o automatización; revocar secretos y pausar colas.                                          |
| Continuidad manual | Procedimiento alternativo para recibir, trabajar y entregar cuando IA/proveedor no esté disponible.                                |

# 12. Roles, responsabilidades y separación de funciones

| **Rol**                        | **Responsabilidad**                                                   | **No debe**                                                       |
|--------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------|
| Responsable de negocio/cliente | Define objetivo, alcance, aceptación y prioridades.                   | Delegar al modelo decisiones que le corresponden.                 |
| CEO digital                    | Clasifica, pregunta, planifica, asigna y supervisa estados.           | Tener privilegios universales o aprobar su propia acción.         |
| Owner de capacidad             | Mantiene procedimiento, herramientas, límites y calidad de su módulo. | Cambiar políticas sin revisión.                                   |
| Especialista sectorial         | Valida contexto y criterios propios del dominio.                      | Inventar requisitos o sustituir asesoría profesional obligatoria. |
| Seguridad/privacidad           | Define controles, revisa riesgos, incidentes y excepciones.           | Ser sustituido por una respuesta del LLM.                         |
| QA                             | Comprueba entregable contra criterios y evidencia.                    | Validar solo por estilo o plausibilidad.                          |
| Aprobador humano               | Autoriza una acción/entrega concreta y versionada.                    | Aprobar acciones no mostradas o que cambiaron tras aprobar.       |
| Administrador técnico          | Opera infraestructura, accesos, releases y backups.                   | Acceder a datos de cliente sin necesidad y autorización.          |

En un equipo pequeño una persona puede desempeñar varios roles, pero las funciones críticas deben separarse lógicamente. Para acciones de alto impacto, aplicar doble aprobación si el riesgo/contrato lo exige.

# 13. Modelo de datos mínimo y trazabilidad

| **Entidad**           | **Campos/relaciones mínimos**                                                                          |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| Tenant / Cliente      | tenant_id, estado, contrato/ámbito, configuración de retención y políticas.                            |
| Usuario / Identidad   | user_id, roles, tenant scopes, estado, método de autenticación.                                        |
| Solicitud / Proyecto  | request_id, tenant_id, objetivo, alcance, riesgo, owner, estado, presupuesto, fechas.                  |
| Workflow / Plan       | workflow_id, versión, plan, dependencias, criterios de aceptación y transiciones.                      |
| Tarea                 | task_id, owner lógico, entradas/salidas, herramienta, permisos, timeout, intentos, estado.             |
| Documento / Fuente    | source_id, hash, versión, origen, clasificación, ACL, retención y referencias.                         |
| Ejecución de modelo   | model_run_id, proveedor/modelo/versión, prompt_version, tokens/coste, latencia, evaluación.            |
| Tool call             | tool_call_id, actor, tenant, acción, parámetros redactados, autorización, aprobación y resultado.      |
| Aprobación            | approval_id, aprobador, objeto/versión exacta, alcance, timestamp, decisión y motivo.                  |
| Auditoría / Incidente | event_id, correlation_id, actor, acción, resultado, timestamp; incidente enlaza evidencias y acciones. |

# 14. Requisitos no funcionales y pruebas de aceptación

| **Dimensión**  | **Criterio que debe definirse/probarse**                                                                            |
|----------------|---------------------------------------------------------------------------------------------------------------------|
| Seguridad      | Threat model actualizado; pruebas de autorización, aislamiento, prompt injection, secretos, dependencias y sandbox. |
| Fiabilidad     | Reinicio no pierde tareas; reintentos no duplican efectos; fallos se detectan y escalan.                            |
| Calidad        | Suite por caso de uso con umbrales aprobados; regresión en cada release.                                            |
| Privacidad     | Minimización, retención, borrado, exportación y acceso verificables.                                                |
| Rendimiento    | Objetivos de latencia/concurrencia definidos a partir de carga real; pruebas de carga antes de escalar.             |
| Coste          | Límite por workflow/tenant y alertas; detener ejecución al alcanzar umbral salvo autorización.                      |
| Disponibilidad | SLO y procedimiento manual según criticidad; no prometer disponibilidad sin medición.                               |
| Mantenibilidad | Código modular, migraciones, documentación, revisión, CI y rollback probado.                                        |

# 15. Puertas de lanzamiento: cuándo se puede avanzar

> Nota: en el resto de la documentación estas puertas se llaman **L0–L4** para no confundirlas con las puertas de cliente G0–G6 del Atlas de Evolución.

| **Puerta**                  | **Debe estar cumplido antes de…**              | **Evidencia mínima**                                                                                                    |
|-----------------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| G0 · MVP local              | Usar datos sintéticos internamente.            | Flujo de punta a punta, tests, estados, logs y coste estimado.                                                          |
| G1 · Datos internos reales  | Usar datos reales de la propia organización.   | Identidad, roles, secretos, minimización, backups y revisión de privacidad.                                             |
| G2 · Datos de clientes      | Pilotar con cliente y datos reales.            | Contrato/roles/privacidad revisados, segregación probada, incident response, borrado, acceso, proveedor y restauración. |
| G3 · Automatización externa | Ejecutar acciones fuera del entorno de prueba. | Gateway, allowlist, aprobaciones, idempotencia, sandbox, kill switch y auditoría.                                       |
| G4 · Escala                 | Aumentar clientes, sectores o volumen.         | Evaluación continua, SLO, capacidad, costes, soporte, runbooks, releases y continuidad.                                 |

Una puerta no se supera por calendario ni por “parece funcionar”. El responsable documenta evidencias, riesgos residuales y aceptación explícita. Si falla una prueba crítica, no se avanza.

# 16. Orden definitivo de construcción

| **Orden** | **Construir**                                                                        | **No construir todavía**                                  |
|-----------|--------------------------------------------------------------------------------------|-----------------------------------------------------------|
| 1         | Caso de uso acotado; criterios de éxito; datos sintéticos; mapa de riesgos.          | CEO generalista multi-sector.                             |
| 2         | Repositorio, CI, FastAPI, PostgreSQL, migraciones, autenticación básica y auditoría. | Microservicios, Kubernetes y vector DB sin justificación. |
| 3         | Modelo de solicitud/proyecto/tarea/estado; workflow determinista; idempotencia.      | Agentes autónomos que deciden su propio flujo.            |
| 4         | CEO limitado: ficha, clasificación, preguntas, decisión y plan estructurado.         | Autoejecución de acciones externas.                       |
| 5         | Catálogo de capacidades y gateway con una herramienta inocua de prueba.              | Credenciales globales o acceso libre a shell/red.         |
| 6         | RAW + metadatos + permisos + búsqueda textual; citas y procedencia.                  | Indexar todo sin clasificación ni ACL.                    |
| 7         | QA, evaluación, aprobaciones, logs, límites de coste y pruebas adversariales.        | Memoria automática de cualquier conversación.             |
| 8         | Piloto interno; medir; corregir; documentar.                                         | Añadir segundo sector antes de validar el primero.        |
| 9         | Segregación multi-tenant y controles completos antes de datos de clientes.           | Producción con controles pendientes.                      |
| 10        | Escalar capacidades/modelos/infraestructura solo con métricas y necesidad.           | Complejidad por prestigio tecnológico.                    |

# 17. Preguntas que quedan como decisiones de negocio, no como huecos técnicos

No se pueden cerrar correctamente inventando respuestas. Deben acordarse con el socio y, cuando corresponda, con cliente/asesoría. La arquitectura debe permitir configurarlas sin reescribir el sistema.

| **Decisión pendiente**               | **Por qué importa**                                                     | **Momento límite**                |
|--------------------------------------|-------------------------------------------------------------------------|-----------------------------------|
| Primer caso de uso y sector          | Determina datos, riesgo, criterios de calidad y retorno.                | Antes de implementar el CEO.      |
| Tipo de cliente y geografía          | Determina contratos, privacidad, transferencias y regulación.           | Antes de datos reales externos.   |
| Modelo comercial y responsabilidades | Define quién es responsable/encargado, soporte, garantías y aceptación. | Antes del primer contrato.        |
| Clases de datos permitidas           | Define qué se puede cargar y qué debe bloquearse/redactarse.            | Antes de cualquier dato real.     |
| Proveedores/modelos aprobados        | Afecta privacidad, coste, disponibilidad y derechos de uso.             | Antes de enviar datos a terceros. |
| Autonomía aceptada por caso          | Determina qué puede ejecutar, preparar o solo recomendar.               | Antes de habilitar herramientas.  |
| SLO, RTO, RPO y retención            | Dependen de criticidad, presupuesto y contrato.                         | Antes de piloto/producción.       |
| Presupuesto y límites                | Evita costes descontrolados por bucles, agentes o contexto.             | Desde el MVP.                     |

# 18. Riesgos residuales y criterio de honestidad

- Un modelo puede equivocarse, omitir contexto o ser manipulado. Se mitiga con límites, fuentes, evaluación y revisión; no se elimina.

- La segregación puede fallar por errores de implementación, caché o integración. Se exige defensa en profundidad y pruebas negativas continuas.

- Un proveedor puede cambiar modelo, condiciones, región o disponibilidad. Se requiere inventario, evaluación, contrato y plan de salida.

- Las obligaciones legales dependen del caso real. No afirmar cumplimiento de RGPD, AI Act, DORA u otra norma sin análisis de aplicabilidad y evidencias.

- La calidad de un agente no se demuestra con una demo aislada. Se demuestra con datasets representativos, regresión, monitorización y resultados de operación.

# 19. Checklist de aprobación de diseño

- [ ] El caso de uso, usuario, cliente, finalidad y entregable están definidos.

- [ ] La clasificación del CEO produce continuar/preguntar/escalar/rechazar/derivar con razones.

- [ ] Los permisos se aplican en backend y gateway, no en prompts.

- [ ] Los datos recuperados están filtrados por tenant y ACL antes de entrar al contexto del modelo.

- [ ] Las herramientas tienen allowlist, validación, límites, auditoría y kill switch.

- [ ] Las acciones de impacto requieren aprobación humana vinculada a la versión exacta.

- [ ] Los errores tienen timeout, reintentos limitados, idempotencia y escalado.

- [ ] Las fuentes, Wiki, prompts, modelos y workflows tienen versionado y procedencia.

- [ ] Hay evaluación de calidad, regresión y pruebas adversariales.

- [ ] Hay proceso de incidentes, backups restaurables, borrado y continuidad.

- [ ] Hay presupuesto y límites por tenant/proyecto.

- [ ] Las puertas G0–G4 se superan con evidencias y aceptación de riesgo residual.

# Conclusión y versión de referencia

La v1.4 queda como línea base de diseño recomendada: conserva el concepto y los diagramas de la v1.3, pero cierra reglas operativas, límites de autonomía, fallos, seguridad, datos, gobierno de modelos, QA, roles, trazabilidad y puertas de lanzamiento. No hace falta añadir más cajas al organigrama ahora. La siguiente actividad correcta es escoger un caso de uso interno y convertir estas reglas en requisitos y pruebas del MVP.

Estado: DISEÑO BASELINE APROBADO PARA CONSTRUIR EL MVP, sujeto a las decisiones de negocio de la sección 17 y a validación mediante pruebas. No equivale a autorización para producción ni a certificación de cumplimiento.
