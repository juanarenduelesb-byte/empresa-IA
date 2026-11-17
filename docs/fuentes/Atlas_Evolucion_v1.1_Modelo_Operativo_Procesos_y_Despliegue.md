> **Versión de trabajo en Markdown** del documento original `archive/originales/Atlas_Evolucion_v1.1_Modelo_Operativo_Procesos_y_Despliegue.docx`, convertida el 17/11/2026. Los diagramas originales se han sustituido por enlaces a su versión redibujada y corregida en `docs/atlas/`. Correcciones aplicadas: ver `docs/16-correcciones.md`. Nombre provisional del proyecto: Varios.

**ATLAS DE ARQUITECTURA DIGITAL**

**EVOLUCIÓN V1.1  
MODELO OPERATIVO, MOTOR DE PROCESOS  
Y DESPLIEGUE EMPRESARIAL**

Evolución a partir del análisis público de Sapira / Pharo, manteniendo las decisiones válidas de la Guía de Arranque v1.4 y del Atlas v1.0.

| **VERSIÓN** | **FECHA**  | **DOCUMENTOS BASE**                                             | **ESTADO**                             |
|-------------|------------|-----------------------------------------------------------------|----------------------------------------|
| 1.1         | 17/11/2026 | Guía v1.4 · Atlas v1.0 · Documento Maestro de Conocimiento v1.1 | Propuesta de evolución para aprobación |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>DECISIÓN CENTRAL<br />
Pasar de una arquitectura centrada en coordinar agentes a una plataforma centrada en descubrir, diseñar, ejecutar, medir y mejorar procesos empresariales completos.</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Este documento es un addendum. No sustituye ni reescribe la documentación existente: define cambios concretos que deben incorporarse al backlog y a los mapas del Atlas.

# 0. Resumen ejecutivo

La principal lección del posicionamiento público de Sapira / Pharo es que el valor empresarial no está en tener muchos agentes, sino en resolver procesos completos que atraviesan personas, departamentos y sistemas. Nuestra arquitectura ya tiene CEO, capacidades funcionales, especialistas sectoriales, conocimiento, ejecución, QA y gobierno. La evolución consiste en hacer explícitos el descubrimiento de procesos, un motor de procesos operativos y una disciplina de despliegue por cliente.

## 0.1 Qué mantenemos

- CEO digital como coordinador, clasificador y planificador; no como superusuario ni experto universal.

- Modelo matricial: departamentos funcionales + especialistas sectoriales seleccionados dinámicamente.

- Monolito modular inicial con Python/FastAPI, PostgreSQL y proveedor LLM configurable.

- RAW + Wiki + Schema; Obsidian como interfaz humana, backend como autoridad de permisos y recuperación.

- Workflow determinista para estados y acciones; LLM para interpretación, síntesis y propuestas.

- Gateway de herramientas, mínimo privilegio, aislamiento por tenant, QA, aprobación humana y trazabilidad.

- Despliegue incremental, MVP acotado y no escalar antes de validar un caso real.

## 0.2 Qué añadimos

- Process Discovery: descubrir procesos reales, no limitarse a recibir requisitos o documentos.

- Process Engine: representar y ejecutar procesos empresariales de extremo a extremo con estados, reglas, SLA, excepciones y aprobaciones.

- Integration Hub: catálogo de conectores y adaptadores reutilizables para sistemas del cliente.

- Operational Intelligence: medir tiempo, coste, calidad, excepciones, retrabajo y ROI antes/después.

- Client Deployment Management: gestionar diagnóstico, prototipo, despliegue, adopción y mejora continua por cliente.

- Deployment Lead y Forward Deployed Engineer como funciones humanas de responsabilidad sobre resultado e integración.

## 0.3 Qué no cambiamos

- No creamos un agente permanente por cada combinación de sector y departamento.

- No sustituimos PostgreSQL, RAW/Wiki/Schema ni el backend de permisos por memoria opaca del LLM.

- No introducimos microservicios, Kubernetes, Neo4j, BPM pesado ni vector DB sin evidencia de necesidad.

- No habilitamos autonomía general ni acceso libre a sistemas del cliente.

- No asumimos que la arquitectura interna de Pharo es exactamente la que inferimos de sus páginas públicas.

# 1. Aprendizajes del análisis de Sapira / Pharo

| **Señal pública**                               | **Lectura estratégica**                                        | **Decisión para nuestra arquitectura**                                |
|-------------------------------------------------|----------------------------------------------------------------|-----------------------------------------------------------------------|
| Plataforma central y capacidades reutilizables  | Base común; soluciones compuestas por cliente.                 | Catálogo de módulos, conectores, workflows y paquetes sectoriales.    |
| Captura de conocimiento antes de automatizar    | Los procedimientos formales no reflejan todas las excepciones. | Process Discovery con entrevistas, observación, eventos y validación. |
| Prototipo temprano y despliegue posterior       | Validar valor antes de industrializar.                         | Gates de diagnóstico, prototipo, piloto y producción.                 |
| Agentes, RPA, IDP y orquestación                | La ejecución cruza IA, reglas y sistemas existentes.           | Motor de procesos que combine reglas, LLM, APIs y RPA.                |
| Especialistas de despliegue próximos al cliente | El éxito requiere conexión entre negocio e ingeniería.         | Deployment Lead y Forward Deployed Engineer.                          |
| Memoria operativa acumulativa                   | El conocimiento debe mejorar ejecuciones futuras.              | Telemetría y aprendizaje gobernado; nunca autoaprobar conocimiento.   |
| Promesa de impacto operativo                    | El valor se mide en resultados, no en agentes.                 | Operational Intelligence con baseline, KPI y ROI verificable.         |

Límite de evidencia: recoge el posicionamiento público de Sapira/Pharo y nuestra interpretación. No acredita su arquitectura interna, controles, resultados auditados ni ausencia de debilidades.

# 2. Arquitectura objetivo evolucionada

Se conservan las capas del Atlas. Se añade descubrimiento y modelado de procesos antes del diseño, y un motor de procesos que gobierna la ejecución. El CEO coordina la demanda; el Process Engine controla el ciclo operativo.

| **CANALES Y USUARIOS — Chat, portal, API, usuarios cliente y operadores internos.** |
|-------------------------------------------------------------------------------------|

| **CEO DIGITAL Y GOBIERNO DE ENCARGOS — Intake, clasificación, límites, planificación y selección de capacidades.** |
|--------------------------------------------------------------------------------------------------------------------|

| **PROCESS DISCOVERY & DESIGN — AS-IS, entrevistas, eventos, reglas, excepciones, KPI, TO-BE y aprobación del cliente.** |
|-------------------------------------------------------------------------------------------------------------------------|

| **KNOWLEDGE ENGINE — RAW, Wiki, Schema, fuentes, versiones, permisos y precedentes.** |
|---------------------------------------------------------------------------------------|

| **PROCESS ENGINE / WORKFLOW RUNTIME — Estados, reglas, tareas, dependencias, SLA, timers, excepciones, compensación y human tasks.** |
|--------------------------------------------------------------------------------------------------------------------------------------|

| **CAPACIDADES FUNCIONALES + ESPECIALIZACIÓN SECTORIAL — Finanzas, Legal, Operaciones, Tecnología, Datos/IA, Ciberseguridad, PMO, QA y sectores.** |
|---------------------------------------------------------------------------------------------------------------------------------------------------|

| **INTEGRATION HUB + EXECUTION GATEWAY — APIs, ERP, CRM, correo, almacenamiento, IDP, RPA y herramientas autorizadas.** |
|------------------------------------------------------------------------------------------------------------------------|

| **SISTEMAS Y DATOS DEL CLIENTE — Sistemas existentes, documentos, eventos, bases de datos y usuarios.** |
|---------------------------------------------------------------------------------------------------------|

| **CONTROL TRANSVERSAL — Seguridad, privacidad, aislamiento tenant, auditoría, evaluación IA, QA, costes, observabilidad y continuidad.** |
|------------------------------------------------------------------------------------------------------------------------------------------|

Nota: diagrama funcional. En el MVP los bloques pueden ser módulos del mismo backend. Las cajas no representan todavía contratos API ni despliegues físicos.

# 3. Nuevos módulos funcionales

## 3.1 Process Discovery & Design

Propósito: comprender el proceso real antes de automatizarlo. Convierte entrevistas, observación, documentos y datos autorizados en un modelo de proceso validado.

| **Entrada**                                                                                    | **Trabajo**                                                                                                           | **Salida / control**                                                                              |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Objetivo, entrevistas, SOP, formularios, tickets, emails, logs/eventos autorizados y métricas. | Mapear actores, triggers, pasos, decisiones, variantes, excepciones, esperas, retrabajo, sistemas, controles y datos. | AS-IS validado; pain points; baseline KPI; riesgos; oportunidades; TO-BE; aprobación del cliente. |

- Artefactos: ficha de proceso, mapa AS-IS, catálogo de excepciones, RACI, sistemas, diccionario de datos, baseline, riesgos, TO-BE y criterios de aceptación.

- Contrastar entrevistas directivas con usuarios que ejecutan el proceso y evidencia operativa.

- No automatizar una actividad que incumple política o control interno sin resolver antes el problema de gobierno.

- Registrar variantes por unidad, país, producto o tipo de caso; no forzar una ruta única.

- El cliente valida AS-IS y TO-BE antes de construir automatizaciones que cambien su operativa.

## 3.2 Process Engine

Propósito: ejecutar procesos con estados y reglas explícitos. El LLM interpreta entradas o propone decisiones; el motor conserva el control determinista de transiciones y permisos.

| **Elemento**       | **Definición obligatoria**                                                  |
|--------------------|-----------------------------------------------------------------------------|
| Process Definition | ID, versión, owner, propósito, alcance, evento disparador y resultado.      |
| State              | Estados válidos, transiciones y condiciones de entrada/salida.              |
| Task               | Tipo, responsable lógico, input/output, timeout, retry y criterio de éxito. |
| Rule               | Condición determinista, versión, fuente/owner y efecto.                     |
| Decision           | Datos, alternativas, evidencia, incertidumbre y autoridad aprobadora.       |
| Exception          | Tipo, severidad, responsable, plazo, ruta alternativa y reanudación.        |
| Human Task         | Persona/rol, información, decisión permitida y aprobación registrada.       |
| SLA/Timer          | Reloj, vencimiento, escalado, pausa y notificación.                         |
| Compensation       | Reversión o compensación ante secuencia parcial fallida.                    |
| Audit Event        | Actor, tenant, versión, transición, timestamp, correlación y evidencia.     |

## 3.3 Integration Hub

- Catálogo de conectores por sistema, operación, versión, scopes, límites, dependencias y owner.

- API como primera opción; RPA solo cuando no exista interfaz fiable o sea justificable.

- Credenciales por cliente y entorno en secret manager; nunca compartidas entre tenants.

- Contratos de entrada/salida validados con Pydantic/JSON Schema y pruebas contractuales.

- Rate limits, paginación, webhooks, idempotencia, retries, timeouts y circuit breaker.

- Registro de llamadas, autorización, objeto afectado, resultado y correlación con workflow.

- Sandbox y cuenta de prueba antes de operaciones productivas.

- Procedimiento de cambio de API, revocación y retirada del conector.

## 3.4 Operational Intelligence

Propósito: demostrar si el proceso mejora. No basta con medir respuestas del LLM ni contar automatizaciones.

| **Dimensión**  | **KPI**                                             | **Regla de medición**                                                    |
|----------------|-----------------------------------------------------|--------------------------------------------------------------------------|
| Tiempo         | Lead time y cycle time                              | Definir inicio/fin; separar espera y trabajo activo.                     |
| Coste          | Coste por caso/proceso                              | Incluir licencias, API, infraestructura, operación humana y excepciones. |
| Calidad        | First-pass yield, errores, defectos y retrabajo     | Definir defecto y severidad.                                             |
| Automatización | Porcentaje straight-through                         | Denominador: casos elegibles; publicar exclusiones.                      |
| Excepciones    | Tasa, causas, tiempo de resolución y backlog        | Taxonomía estable y owner.                                               |
| Servicio       | SLA, disponibilidad y tiempo de respuesta           | Medición desde sistemas y contratos.                                     |
| Valor          | Ahorro neto, capacidad liberada o pérdidas evitadas | Baseline, período y control de factores externos.                        |
| Adopción       | Uso, overrides, abandono y satisfacción             | Usuarios activos no equivalen a valor.                                   |

Toda cifra comercial debe mostrar baseline, período, alcance, método, supuestos y limitaciones. No atribuir al sistema mejoras debidas a cambios organizativos externos.

## 3.5 Client Deployment Management

| **Fase**             | **Entregables**                                                 | **Gate**                                 |
|----------------------|-----------------------------------------------------------------|------------------------------------------|
| D0 Calificación      | Problema, sponsor, alcance, sistemas, presupuesto y éxito.      | Problema material y sponsor confirmados. |
| D1 Discovery         | AS-IS, entrevistas, excepciones, baseline, riesgos y datos.     | Cliente valida proceso y datos.          |
| D2 Solution Design   | TO-BE, arquitectura, RACI, seguridad, privacidad, plan y coste. | Diseño y riesgos aprobados.              |
| D3 Prototype         | Flujo acotado, datos controlados, pruebas y demo.               | Criterios del prototipo superados.       |
| D4 Pilot             | Usuarios limitados, revisión humana, runbooks y medición.       | Riesgos aceptables y KPI alcanzados.     |
| D5 Production        | Segregación, contrato, SLA, soporte, continuidad y formación.   | Aprobación formal y gates de producción. |
| D6 Operate & Improve | SLO, incidentes, releases, cambios, ROI y backlog.              | Revisión de valor y expansión.           |

# 4. Modelo organizativo y responsabilidades

Son funciones de responsabilidad, no necesariamente puestos permanentes ni agentes separados. En cada implantación con cliente debe existir un owner humano.

| **Función**                 | **Responsabilidad**                                                                            | **Límite**                                         |
|-----------------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------|
| CEO digital                 | Intake, clasificación, priorización, plan, capacidades, escalado y comunicación.               | Sin credenciales universales ni autoaprobación.    |
| Deployment Lead (humano)    | Accountability de resultado, alcance, sponsor, aceptación, riesgos y ROI.                      | La responsabilidad final no se delega al LLM.      |
| Forward Deployed Engineer   | Descubrir detalle técnico, integrar, construir adaptadores/workflows, desplegar y generalizar. | No incorporar lógica cliente al core sin revisión. |
| Process Architect / Analyst | AS-IS/TO-BE, reglas, excepciones, controles, RACI y métricas.                                  | No diseñar desde supuestos no validados.           |
| Platform & AI Engineering   | Core, runtime, modelos, RAG, SDK, observabilidad y reutilización.                              | Evitar forks permanentes por cliente.              |
| Domain Specialist           | Validar lenguaje, regulación, decisiones y excepciones sectoriales.                            | No sustituir asesoría profesional cualificada.     |
| Security & Privacy Owner    | Threat model, privacidad, proveedores, controles, incidentes y gates.                          | No limitarse a cuestionarios comerciales.          |
| QA / Evaluation             | Pruebas, datasets, aceptación, regresión y defectos.                                           | No validar solo con demo feliz.                    |

## 4.1 Equipo matricial por proyecto

| **Caso: automatizar siniestros** | **Participación**                                                        |
|----------------------------------|--------------------------------------------------------------------------|
| Discovery                        | Process Architect + especialista seguros + tramitadores del cliente.     |
| Diseño                           | Operaciones + Tecnología + Datos/IA + Legal/Privacidad + Seguridad + QA. |
| Construcción                     | Forward Deployed Engineer + Integration Hub + IDP + Process Engine.      |
| Validación                       | Tramitadores expertos + QA + Security/Privacy + sponsor.                 |
| Operación                        | Deployment Lead + soporte + owner operativo del cliente.                 |

# 5. Catálogo de capacidades y paquetes sectoriales

Un paquete sectorial no es un agente gigante: es una combinación versionada de procesos, reglas, plantillas, conocimiento, conectores, pruebas y controles.

| **Paquete**             | **Procesos candidatos**                                                                                        | **Dependencias / límites**                                              |
|-------------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| Seguros/peritaje        | Apertura expediente, extracción documental, clasificación, asignación, seguimiento, inconsistencias e informe. | Datos personales y salud; cobertura/indemnización con autoridad humana. |
| Banca/finanzas          | Onboarding, apoyo documental KYC, conciliación, incidencias y reporting.                                       | DORA, secreto, AML y crédito según función; análisis legal específico.  |
| Industria               | Compras, homologación, órdenes, calidad, incidencias y mantenimiento.                                          | Integración ERP/OT; separar IT/OT.                                      |
| Logística               | Incidencias, documentación, seguimiento, asignación y excepciones.                                             | Integridad de eventos, APIs, geolocalización y continuidad.             |
| Servicios profesionales | Propuestas, expedientes, entregables, revisión documental y plazos.                                            | Confidencialidad y aprobación del experto.                              |
| Retail                  | Atención, devoluciones, inventario, pedidos y demanda.                                                         | Datos consumidores, pagos y consumo.                                    |

- No lanzar todos los paquetes a la vez: elegir uno con usuarios, sponsor, datos autorizados y métrica de valor.

- Cada capacidad tendrá ID, owner, versión, inputs, outputs, permisos, herramientas, riesgos, coste, timeout y evaluación.

- Estados de publicación: draft, tested, approved, deprecated. Capacidades draft no se invocan en producción.

- Reglas del cliente separadas del código común y versionadas como configuración.

# 6. Modelo de datos y contratos entre módulos

La v1.4 ya contempla Tenant, Usuario, Solicitud/Proyecto, Workflow/Plan, Tarea, Documento/Fuente, ejecución de modelo, Tool Call, Aprobación y Auditoría/Incidente. Se amplía sin sustituir esas entidades.

| **Entidad nueva**    | **Campos mínimos**                                                                 | **Relaciones**                                             |
|----------------------|------------------------------------------------------------------------------------|------------------------------------------------------------|
| ProcessDefinition    | process_id, version, tenant_scope, owner, trigger, purpose, risk, status           | Tiene instancias y tareas definidas.                       |
| ProcessInstance      | instance_id, process/version, tenant, business_key, status, started/ended, outcome | Agrupa tareas, eventos, decisiones y KPI.                  |
| TaskDefinition       | type, schemas, handler, permission_policy, timeout, retry, acceptance              | Pertenece a definición.                                    |
| ProcessEvent         | event_id, instance_id, type, actor, timestamp, correlation_id, payload_ref         | Dispara transición y auditoría.                            |
| DecisionRecord       | alternatives, evidence_refs, rule/model_version, uncertainty, approver             | Vinculada a instancia/tarea.                               |
| ExceptionCase        | category, severity, owner, due_at, resolution, resume_condition                    | Bloquea o deriva instancia.                                |
| IntegrationConnector | id, version, provider, scopes, operations, schema, status, owner                   | Asociado a tenant/entorno.                                 |
| KPIObservation       | metric_id, process_instance, value, unit, timestamp, source, definition_version    | Alimenta Operational Intelligence.                         |
| Deployment           | deployment_id, client, phase, owner, scope, gates, risks, KPI_baseline             | Agrupa procesos y releases.                                |
| Release              | artifact_versions, test_run, approver, rollback_ref, deployed_at                   | Versiona workflows, reglas, prompts, conectores y modelos. |

## 6.1 Reglas técnicas no negociables

- Definiciones de proceso aprobadas son inmutables; cualquier cambio crea nueva versión.

- Una instancia conserva la versión con la que comenzó salvo migración explícita y auditada.

- El Process Engine valida transiciones; el LLM no cambia estados directamente.

- Reglas críticas deterministas, testeables y con owner.

- Todo efecto externo idempotente o con detección/compensación de duplicados.

- Eventos con datos mínimos y referencias a objetos protegidos por ACL.

- Tenant y permisos derivados de identidad/contrato en backend, nunca del prompt.

- Conectores con identidad técnica y scopes limitados por cliente/entorno.

- Métricas con definición versionada, fuente y fórmula.

# 7. Seguridad, privacidad y gobierno

| **Superficie**           | **Amenaza**                                              | **Control**                                                                                |
|--------------------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Discovery                | Captura excesiva de datos/secretos.                      | Minimización, base jurídica/mandato, clasificación, retención y acceso.                    |
| Process Model            | Regla errónea o excepción omitida.                       | Validación del owner cliente, procedencia, pruebas de variantes y sign-off.                |
| Process Engine           | Transición inválida, bucle o duplicado.                  | Máquina de estados, invariantes, idempotencia, límites, timeout, compensación y auditoría. |
| Integration Hub          | Token excesivo, API comprometida o fuga tenant.          | Credenciales por tenant, scopes mínimos, vault, gateway, tests y revocación.               |
| Operational Intelligence | Métrica manipulada, atribución errónea o fuga dashboard. | Definiciones versionadas, linaje, ACL, agregación y revisión de baseline.                  |
| Deployment               | Cambio de alcance/riesgo inadvertido.                    | Change control y reevaluación privacidad/AI Act/seguridad.                                 |

- El Process Engine no eleva autonomía: aplica matriz de riesgo, reversibilidad, impacto y aprobación de v1.4.

- Agentes no acceden directamente a ERP/CRM; invocan operaciones concretas mediante gateway.

- Preferir API a RPA; vigilar cambios de interfaz y bloquear ejecución si el UI cambia inesperadamente.

- ROI incluye revisión humana, excepciones, mantenimiento y coste de plataforma.

- Aprendizaje de cliente no se promueve a conocimiento común sin revisar confidencialidad y autorización.

# 8. Modelo de entrega y comercialización

| **Oferta**           | **Incluye**                                                                | **Modelo económico (sin fijar precio)**          |
|----------------------|----------------------------------------------------------------------------|--------------------------------------------------|
| Diagnóstico          | Discovery, baseline, AS-IS/TO-BE, riesgos y business case.                 | Fee fijo por alcance.                            |
| Prototipo            | Proceso acotado, datos de prueba/limitados, integración controlada y demo. | Fee por prototipo y aceptación.                  |
| Implantación         | Integraciones, workflows, controles, formación y producción.               | Fee por hitos.                                   |
| Operación gestionada | Soporte, monitorización, evaluación, continuidad y mejoras.                | Cuota recurrente por servicio/volumen/SLA.       |
| Componente por valor | Variable si métrica atribuible, auditable y acordada.                      | Variable limitada con baseline y método pactado. |

- No fijar aún precios ni márgenes: dependen de integración, volumen, SLA, soporte, riesgo y responsabilidad.

- Vender resultados operativos con alcance y métricas, no número de agentes.

- No prometer porcentajes de ahorro sin baseline, autonomía total, cero errores ni disponibilidad no medida.

- Separar responsabilidad por software, configuración, datos del cliente, decisión profesional y operación humana.

- Definir soporte, mantenimiento, cambios, terceros, subprocesadores y salida.

# 9. Métricas y cuadro de mando

| **Nivel**         | **Indicadores**                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------------|
| Plataforma        | Disponibilidad, latencia, errores, coste por tenant/workflow, uso y fallos de conectores/modelos. |
| Proceso           | Casos, cycle time, lead time, straight-through rate, excepciones, SLA, retrabajo y abandono.      |
| Calidad           | Exactitud por campo/tarea, defectos materiales, falsos positivos/negativos y overrides humanos.   |
| Seguridad         | Accesos denegados, intentos cross-tenant, incidentes, vulnerabilidades vencidas y backups.        |
| Cliente           | Adopción real, satisfacción, valor neto, tiempo de resolución y tickets.                          |
| Economía unitaria | Coste de implantación/operación, margen bruto, reutilización y soporte por cliente.               |

Cada KPI requiere fórmula, owner, fuente, frecuencia, baseline, objetivo y regla de exclusión. No comparar procesos distintos sin normalización.

# 10. Procesos nuevos P31–P38

Se conservan los IDs P01–P30 de la Guía v1.4. Esta extensión no renumera procesos existentes.

| **ID** | **Proceso**                         | **Resultado / control**                                                    |
|--------|-------------------------------------|----------------------------------------------------------------------------|
| P31    | Calificación de oportunidad         | Problema, sponsor, fit, impacto, viabilidad, riesgo y go/no-go.            |
| P32    | Process Discovery                   | Entrevistas, evidencia, AS-IS, variantes, excepciones y baseline.          |
| P33    | Diseño y validación TO-BE           | Modelo futuro, reglas, controles, RACI, KPI y aprobación cliente.          |
| P34    | Gestión de definiciones de proceso  | Versiones, owner, estados, pruebas, aprobación, publicación y retirada.    |
| P35    | Gestión de instancias y excepciones | Estados, tareas, SLA, timers, reintentos, escalado, compensación y cierre. |
| P36    | Gestión del catálogo de conectores  | Alta, evaluación, scopes, versiones, pruebas, cambios y revocación.        |
| P37    | Medición de rendimiento y valor     | Baseline, KPI, ROI, calidad, costes, adopción y atribución.                |
| P38    | Gestión de despliegue por cliente   | Fases D0–D6, gates, riesgos, aceptación, soporte y mejora.                 |

## 10.1 Estados adicionales

| **Objeto**         | **Estados propuestos**                                                                                    |
|--------------------|-----------------------------------------------------------------------------------------------------------|
| Definición proceso | draft → under_review → approved → active → deprecated → retired                                           |
| Instancia proceso  | created → ready → running → waiting_external / waiting_human → exception → completed / failed / cancelled |
| Conector           | draft → tested → approved → active → degraded → suspended → retired                                       |
| Despliegue cliente | qualified → discovery → design → prototype → pilot → production → operating → paused / terminated         |

Implementar como enums y transiciones autorizadas, no como texto libre. Los nombres finales se fijan en los contratos de software.

# 11. Backlog de implementación actualizado

| **Prioridad** | **Trabajo**                  | **Criterio de aceptación**                                                        |
|---------------|------------------------------|-----------------------------------------------------------------------------------|
| P0            | Elegir primer sector/proceso | Sponsor, usuarios, datos autorizados, baseline y alcance acotado.                 |
| P0            | Process Discovery asistido   | AS-IS, variantes, excepciones, KPI y TO-BE validados.                             |
| P0            | Process Definition schema    | Definición versionada con trigger, estados, tareas, reglas, permisos y criterios. |
| P0            | Process Engine mínimo        | Flujo determinista con tareas, estados, persistencia, fallos y auditoría.         |
| P0            | Human Task / Approval        | Pausa, notificación, decisión autenticada y reanudación.                          |
| P0            | KPI baseline                 | Mide tiempo, coste, error y excepción desde fuentes trazables.                    |
| P1            | Integration Hub mínimo       | Un conector sandbox con scopes, schema, idempotencia, logs y revocación.          |
| P1            | Deployment Management        | Tablero de fase, owner, entregables, riesgos, gates y aceptación.                 |
| P1            | IDP documental               | Ingesta segura, extracción validada, confianza por campo y revisión.              |
| P1            | RPA controlada               | Solo caso justificado, sandbox, detección de cambio UI, aprobación y fallback.    |
| P2            | Process mining               | Solo con event logs suficientes, calidad de datos y business case.                |
| P2            | Segundo paquete sectorial    | Solo tras demostrar reutilización del primero.                                    |
| P2            | Analítica predictiva         | Solo con dataset, evaluación, drift y beneficio demostrable.                      |

## 11.1 Secuencia del MVP

1.  Elegir un proceso repetitivo, documental y de excepciones acotadas; identificar sponsor y usuarios.

2.  Documentar AS-IS, variantes, excepciones, baseline y riesgos; validar con quienes ejecutan el proceso.

3.  Diseñar TO-BE y separar reglas deterministas, sugerencias LLM y decisiones humanas.

4.  Implementar Process Definition, instancia, tareas, eventos y transiciones en el monolito modular.

5.  Crear un conector no crítico en sandbox y un flujo de aprobación humana.

6.  Medir antes/después e incluir coste humano, técnico y de excepciones.

7.  Probar fallos, duplicados, timeout, permisos, prompt injection, rollback y recuperación.

8.  Convertir en paquete reutilizable solo tras validar; luego evaluar segundo cliente/sector.

# 12. Puertas de decisión actualizadas

| **Gate**               | **Condición**                                                     | **Evidencia**                                                  |
|------------------------|-------------------------------------------------------------------|----------------------------------------------------------------|
| G0 · Caso elegido      | Problema, owner, sponsor, alcance, datos y KPI definidos.         | Ficha oportunidad y baseline planificado.                      |
| G1 · Proceso entendido | AS-IS y excepciones confirmados por usuarios.                     | Sign-off del cliente sobre mapa y datos.                       |
| G2 · Diseño aceptado   | TO-BE, reglas, responsabilidades, controles y KPI aprobados.      | Process Definition versionada y revisión seguridad/privacidad. |
| G3 · Prototipo         | Flujo acotado y testeable.                                        | Pruebas y criterios de aceptación.                             |
| G4 · Piloto seguro     | Permisos, aislamiento, contratos, incidentes, rollback y soporte. | Aprobación de negocio, tecnología, seguridad y cliente.        |
| G5 · Producción        | Operación, SLO/SLA, continuidad, monitorización y soporte.        | Gate de producción v1.4 + checklist cumplimiento.              |
| G6 · Escalado          | Valor y reutilización demostrados; soporte sostenible.            | Unit economics, capacidad y pruebas multi-tenant.              |

# 13. Riesgos nuevos a vigilar

| **Riesgo**                       | **Por qué importa**                                    | **Mitigación**                                           |
|----------------------------------|--------------------------------------------------------|----------------------------------------------------------|
| Automatizar proceso mal diseñado | Acelera errores, incumplimientos y controles débiles.  | Discovery, TO-BE validado y process owner.               |
| Variantes no descubiertas        | Workflow rígido falla ante excepciones reales.         | Muestreo de casos y catálogo de excepciones.             |
| Dependencia de integraciones     | Cambios API/UI interrumpen operación.                  | Contract tests, versionado, circuit breaker y fallback.  |
| Métricas sin baseline            | ROI ficticio y claims indefendibles.                   | Definiciones, período, fuente, exclusiones y validación. |
| Forks por cliente                | Mantenimiento costoso y divergencia del core.          | Configuración versionada y extensiones gobernadas.       |
| Ejecución duplicada              | Doble pago, alta, comunicación o estado inconsistente. | Idempotencia, business key y reconciliación.             |
| Autonomía excesiva               | Acciones no autorizadas o irreversibles.               | Matriz riesgo/acción, aprobación, scopes y kill switch.  |
| Contaminación de conocimiento    | Regla particular se convierte en regla general.        | Aislamiento, procedencia y aprobación de promoción.      |

# 14. Decisiones que siguen abiertas

- Primer sector, primer cliente objetivo y primer proceso.

- Tipo de servicio y responsabilidad: SaaS, implantación, consultoría u operación gestionada.

- Sponsor y process owner del lado del cliente.

- Sistemas y datos disponibles y permisos aplicables.

- Proveedores y conectores aprobados.

- Autonomía permitida por tipo de acción.

- SLA/SLO, RTO/RPO, retención, soporte y presupuesto.

- KPI y método de atribución del ROI.

- Funciones cubiertas por equipo propio y funciones de partners.

# 15. Relación con documentación existente

| **Documento**             | **Tratamiento**                                                                                                                                       |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Guía de Arranque v1.4     | Se mantiene como baseline de decisiones, límites, seguridad, P01–P30 y gates G0–G4. Añadir referencia a P31–P38 y gates de despliegue.                |
| Atlas v1.0                | Se mantiene como mapa base; actualizar mapa maestro con Discovery, Process Engine, Integration Hub, Operational Intelligence y Deployment Management. |
| Mapa 1 · Organización     | Añadir Deployment Lead, Forward Deployed Engineer y Process Architect como funciones.                                                                 |
| Mapa 2 · CEO              | CEO clasifica y coordina; entrega gestión de instancias al Process Engine.                                                                            |
| Mapa 3 · Knowledge Engine | Mantener RAW/Wiki/Schema; enlazar definiciones de proceso, reglas y KPI versionados.                                                                  |
| Mapa 4 · Ejecución        | Añadir Process Engine, human tasks, excepciones, SLA, compensación e Integration Hub.                                                                 |
| Mapa 5 · Seguridad        | Aplicar identidad, scopes, tenant y auditoría a conectores e instancias.                                                                              |
| Mapa 6 · QA/Gobierno      | Añadir evaluación por proceso, KPI, baseline, variantes y sign-off.                                                                                   |
| Mapa 7 · Infraestructura  | Mantener monolito modular; módulos nuevos dentro del backend al inicio.                                                                               |
| Mapa 8 · Ciclo de vida    | Ampliar con D0–D6 y medición de valor por proceso/cliente.                                                                                            |
| Mapa 9 · Contratos        | Añadir entidades ProcessDefinition, ProcessInstance, ProcessEvent, ExceptionCase, Connector, KPIObservation y Deployment.                             |

# 16. Decisión recomendada

No copiamos Pharo ni rehacemos nuestro sistema. Evolucionamos el Atlas desde una organización digital coordinada por un CEO hacia una plataforma de automatización de procesos empresariales, manteniendo la base segura y modular ya definida.

La primera construcción no debe ser un CEO omnisciente ni una colección de agentes. Debe ser un proceso real, descubierto con usuarios, modelado con estados y reglas, ejecutado con un conector limitado, revisado por humanos y medido con KPI.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ORDEN DE TRABAJO<br />
1. Elegir proceso y sponsor → 2. Descubrir AS-IS → 3. Diseñar TO-BE → 4. Construir Process Engine mínimo → 5. Integrar un sistema → 6. Medir y validar → 7. Reutilizar.</strong></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Estado: propuesta de evolución v1.1. Requiere aprobación de los socios y selección del primer proceso antes de convertirse en especificación de implementación. No certifica cumplimiento ni describe la arquitectura privada de Sapira/Pharo.
