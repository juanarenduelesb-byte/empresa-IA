> **Versión de trabajo en Markdown** del documento original `archive/originales/Marco_Integral_Legal_Ciberseguridad_IA_Espana_UE_2026-11-16.docx`, convertida el 17/11/2026. Los diagramas originales se han sustituido por enlaces a su versión redibujada y corregida en `docs/atlas/`. Correcciones aplicadas: ver `docs/16-correcciones.md`. Nombre provisional del proyecto: Varios.

**MARCO INTEGRAL**

**LEGAL, REGULATORIO,  
PRIVACIDAD Y CIBERSEGURIDAD**

Organización digital multisectorial con IA, agentes, automatización y servicios de terceros

| **VERSIÓN** | **FECHA DE CORTE** | **ÁMBITO**             | **ESTADO**                         |
|-------------|--------------------|------------------------|------------------------------------|
| 1.0         | 16/11/2026         | España + Unión Europea | Línea base para validar y ejecutar |

Documento complementario a la Guía de Arranque v1.4 y al Atlas de Arquitectura Digital. No sustituye asesoramiento jurídico, auditoría, evaluación de impacto ni certificación.

Objetivo: convertir el marco legal y de seguridad en un programa verificable, con responsables, controles técnicos, evidencias y puertas de lanzamiento.

# 0. Cómo utilizar este documento

Advertencia esencial: no existe una lista universal de «todas las normas que hay que cumplir» sin conocer el producto, los sectores, los datos, los países, el papel contractual y el tamaño/actividad de la empresa. Este documento identifica el universo razonablemente relevante y distingue obligaciones aplicables, condicionales, contractuales y buenas prácticas. Antes de operar con clientes debe cerrarse una matriz de aplicabilidad con asesoría legal.

- No todas las normas citadas aplican automáticamente a una startup tecnológica.

- La aplicabilidad se determina por actividad real, no por el nombre comercial ni por utilizar IA.

- Los contratos de clientes pueden imponernos obligaciones adicionales aunque una ley no nos aplique directamente.

- La seguridad de un proveedor no elimina nuestra responsabilidad sobre configuración, credenciales, datos, integraciones, selección, supervisión y continuidad.

- No es posible garantizar que no ocurra absolutamente nada. El objetivo es prevenir, detectar, contener, recuperar y demostrar diligencia.

## 0.1 Supuestos de partida

- Empresa establecida inicialmente en España; prestación potencial de servicios a empresas en España y UE.

- Plataforma propia de coordinación de IA/LLM, agentes, automatizaciones, bases de datos, almacenamiento y conectores SaaS.

- Uso inicial de modelos de terceros; no se presupone entrenamiento de un modelo fundacional propio.

- Actividad multisectorial con potencial acceso a información empresarial, datos personales, documentación confidencial y, eventualmente, datos regulados.

- En muchos proyectos actuaremos como proveedor tecnológico/encargado; en otros podríamos ser responsables o corresponsables.

- No se presupone que seamos entidad financiera, operador esencial, fabricante de producto digital ni proveedor de IA de alto riesgo.

## 0.2 Etiquetas de aplicabilidad

| **Etiqueta**        | **Significado**                                                                                        | **Tratamiento**                      |
|---------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------|
| A · Probable        | Obligación normalmente aplicable por operar en España/UE y tratar datos o prestar servicios digitales. | Diseñar desde el inicio.             |
| C · Condicional     | Depende de sector, tamaño, rol, función, cliente, producto o datos.                                    | Evaluar por servicio y cliente.      |
| K · Contractual     | Exigencia del cliente, licitación o cadena de suministro.                                              | Incorporar a contratos y evidencias. |
| BP · Buena práctica | Marco voluntario salvo obligación contractual/regulatoria.                                             | Adoptar proporcionalmente.           |
| F · Futuro          | Norma aprobada con aplicación escalonada.                                                              | Preparar calendario y owner.         |

## 0.3 Datos que faltan para cerrar aplicabilidad

- Forma societaria, estructura de grupo y países donde se contratará.

- Primeros sectores y casos de uso concretos.

- Si venderemos SaaS propio, desarrollo a medida, consultoría, decisiones automatizadas o servicios gestionados.

- Datos personales, especiales, financieros, sanitarios, laborales, penales, menores o de infraestructuras críticas.

- Quién determina fines y medios en cada tratamiento: responsable, encargado o corresponsable.

- Si algún sistema encaja en categorías de alto riesgo del AI Act.

- Si comercializaremos software descargable/producto con elementos digitales relevante para CRA.

- Tamaño, sector y posición en cadena de suministro para NIS2 u obligaciones sectoriales.

# 1. Mapa normativo

| **Norma / marco**                      | **Aplicabilidad inicial**                                             | **Impacto para nosotros**                                                                            |
|----------------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| RGPD (UE) 2016/679                     | A si tratamos datos personales de personas en UE.                     | Base jurídica, transparencia, derechos, seguridad, contratos, brechas, DPIA y transferencias.        |
| LOPDGDD 3/2018                         | A complementaria en España.                                           | Reglas nacionales, derechos digitales y régimen español.                                             |
| LSSI-CE 34/2002                        | A si ofrecemos servicios de sociedad de la información/web comercial. | Aviso legal, comunicaciones comerciales, contratación electrónica y cookies.                         |
| AI Act (UE) 2024/1689 y modificaciones | A/C según rol y finalidad de cada sistema.                            | Alfabetización, prácticas prohibidas, transparencia, clasificación de riesgo y obligaciones por rol. |
| NIS2 (UE) 2022/2555 y ley española     | C por sector, tamaño, entidad y cadena de suministro.                 | Gobierno, riesgos, incidentes, continuidad y cadena de suministro.                                   |
| DORA (UE) 2022/2554                    | C/K en servicios TIC a entidades financieras.                         | Cláusulas, auditoría, incidentes, continuidad, subcontratación, localización y salida.               |
| Cyber Resilience Act (UE) 2024/2847    | C si ponemos en mercado productos con elementos digitales.            | Seguridad por diseño, vulnerabilidades, soporte, documentación y reporting.                          |
| Data Act (UE) 2023/2854                | C/A según servicio cloud/tratamiento de datos y acceso/uso de datos.  | Cambio de proveedor, portabilidad, interoperabilidad y cláusulas.                                    |
| ePrivacy / cookies                     | C/A según tracking y comunicaciones electrónicas.                     | Consentimiento y confidencialidad de comunicaciones.                                                 |
| Propiedad intelectual / secretos       | A en la operativa empresarial.                                        | Licencias, titularidad, confidencialidad y protección del know-how.                                  |
| Consumo / contratación                 | C si vendemos a consumidores o usuarios no profesionales.             | Información precontractual, desistimiento, garantías y reclamaciones.                                |
| Normativa sectorial                    | C por sector y función prestada.                                      | Finanzas, salud, seguros, empleo, telecomunicaciones, administración.                                |
| ENS / contratación pública             | C/K si trabajamos para sector público o sistemas en su ámbito.        | Categoría, medidas ENS, auditoría y evidencias.                                                      |
| Accesibilidad (EAA / Ley 11/2023)      | C según servicio/producto y excepciones.                              | Accesibilidad de servicios digitales y comercio electrónico.                                         |
| Fiscal, laboral y societario           | A como empresa; fuera del núcleo técnico.                             | Facturación, conservación, contratos laborales y gobierno.                                           |

Esta tabla debe convertirse en un registro de aplicabilidad por producto, cliente, país y versión del servicio.

# 2. Protección de datos: RGPD y LOPDGDD

## 2.1 Roles: decidir quién es quién

- Responsable: determina fines y medios. Si definimos por qué y cómo se usan datos para fines propios, podemos ser responsables.

- Encargado: trata datos siguiendo instrucciones documentadas del cliente; requiere contrato del artículo 28 RGPD.

- Corresponsables: dos o más partes determinan conjuntamente fines y medios; acuerdo del artículo 26.

- No aceptar automáticamente la etiqueta contractual del cliente: analizar la realidad del tratamiento.

- Por cada flujo, registrar responsable, encargado, subencargados, destinatarios y quién atiende derechos e incidentes.

## 2.2 Inventario y registro de tratamientos

- Inventariar onboarding, usuarios, soporte, facturación, logs, analítica, IA, grabaciones, documentos, CRM, RR. HH., marketing y seguridad.

- Documentar finalidad, interesados/datos, base jurídica, destinatarios, transferencias, conservación y medidas.

- Mantener Registro de Actividades cuando sea exigible; aunque concurra excepción para organizaciones pequeñas, conservar inventario operativo.

- Separar tratamiento propio y tratamiento por cuenta del cliente.

- Asignar owner de privacidad y revisar trimestralmente y ante nuevos usos.

## 2.3 Principios y bases jurídicas

- Finalidad determinada: no reutilizar datos para entrenar modelos, benchmarking o marketing sin base jurídica y transparencia adecuadas.

- Minimización: enviar al LLM solo campos necesarios; redactar identificadores y secretos cuando sea viable.

- Exactitud y actualización; propagar rectificaciones a índices, cachés y sistemas derivados.

- Limitación de conservación: plazos por categoría, borrado verificable y tratamiento de backups.

- Integridad, confidencialidad, responsabilidad proactiva y privacidad desde diseño y por defecto.

- Elegir base jurídica por finalidad: contrato, obligación legal, interés legítimo documentado, consentimiento u otra base válida.

## 2.4 Transparencia y derechos

- Avisos por canal/finalidad: identidad, contacto, finalidades, bases, destinatarios, transferencias, plazos, derechos y reclamación ante AEPD.

- Procedimiento para acceso, rectificación, supresión, oposición, limitación, portabilidad y retirada del consentimiento.

- Verificación de identidad proporcionada; registrar solicitud y buscar en sistemas, documentos, logs, proveedores e índices.

- Responder normalmente en un mes bajo RGPD, con extensión justificada cuando proceda.

- Explicar si el usuario interactúa con IA y cuándo hay decisiones automatizadas relevantes.

## 2.5 Encargados y subencargados

- Firmar DPA antes de cargar datos personales en proveedores que actúen como encargados.

- Incluir objeto, duración, naturaleza, finalidad, tipos de datos, interesados e instrucciones documentadas.

- Exigir confidencialidad, seguridad, asistencia en derechos, brechas, DPIA, auditorías y cumplimiento.

- Autorizar subencargados según mecanismo acordado; mantener lista, ubicación, función, cambios y derecho de objeción/terminación.

- Al terminar, devolver o suprimir datos y copias salvo obligación legal.

- Verificar si el proveedor usa prompts/inputs para entrenamiento, revisión humana, retención, telemetría y si esas funciones pueden desactivarse.

## 2.6 EIPD y DPO

- Realizar screening EIPD antes de tratamientos probablemente de alto riesgo: gran escala de datos sensibles, vigilancia sistemática, perfiles/decisiones significativas, población vulnerable o combinación intensiva de fuentes.

- La EIPD debe describir tratamiento, necesidad/proporcionalidad, riesgos para derechos y libertades y medidas previstas.

- Si queda riesgo alto no mitigado, consultar a autoridad antes de iniciar conforme al RGPD.

- Designar DPO cuando concurra obligación legal (p. ej. ciertos organismos, observación habitual y sistemática a gran escala o categorías especiales a gran escala) o voluntariamente con independencia y recursos.

## 2.7 Brechas de datos personales

- Canal interno para reportar sospechas; formar a empleados y proveedores.

- Encargado comunica al responsable sin dilación indebida; contractualizar plazo interno corto (p. ej. 12–24 h) para permitir evaluación.

- Responsable notifica a AEPD en máximo 72 h desde que tiene constancia cuando exista riesgo para derechos y libertades; documentar incluso si no notifica.

- Comunicar a afectados sin dilación indebida si el riesgo es alto, salvo excepciones.

- Preservar evidencias, cronología, alcance, datos, medidas y comunicaciones; notificar por fases si procede.

- No esperar a concluir la investigación para iniciar el cómputo: documentar cuándo se tuvo constancia.

## 2.8 Transferencias internacionales

- Mapear ubicación de datos, soporte remoto, acceso administrativo, subencargados, backups y telemetría; no basta con región de almacenamiento UE.

- Comprobar adecuación o mecanismo válido (p. ej. SCC), evaluación de transferencia y medidas suplementarias cuando proceda.

- Revisar acceso desde terceros países, legislación local, claves, y respuesta a solicitudes gubernamentales.

- Mantener inventario de transferencias y reevaluar ante cambios de proveedor/región.

# 3. Reglamento de Inteligencia Artificial (AI Act)

A 16/11/2026 existen obligaciones ya aplicables y otras escalonadas. Integrar Claude u otro modelo no nos convierte automáticamente en proveedor de IA de alto riesgo: se analiza quién pone el sistema en mercado/servicio, quién lo modifica, finalidad prevista y rol de cada parte.

## 3.1 Roles posibles

| **Rol**                 | **Cuándo puede encajar**                                                                   | **Implicación**                                                 |
|-------------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| Proveedor de sistema IA | Desarrollamos o mandamos desarrollar y lo ponemos en mercado/servicio bajo nuestro nombre. | Obligaciones según clase de riesgo y transparencia.             |
| Desplegador             | Usamos sistema IA bajo nuestra autoridad profesional.                                      | Uso según instrucciones, supervisión y obligaciones aplicables. |
| Importador/distribuidor | Introducimos o distribuimos sistemas de terceros en mercado UE.                            | Verificaciones y obligaciones según rol.                        |
| Proveedor GPAI          | Desarrollamos y ponemos en mercado modelo de propósito general.                            | Obligaciones específicas GPAI; integrar API ajena no basta.     |
| Integrador/modificador  | Cambiamos finalidad o modificamos sustancialmente sistema.                                 | Puede cambiar rol y obligaciones; análisis previo.              |

## 3.2 Programa de cumplimiento

- Inventario de sistemas IA: finalidad, proveedor/modelo, versión, owner, datos, usuarios, sector, rol legal, riesgo y revisión.

- Clasificar frente a prácticas prohibidas, alto riesgo (Anexos III/I), transparencia y riesgo limitado/minimalista; repetir ante cambio de finalidad.

- No desplegar prácticas prohibidas del artículo 5: manipulación/explotación dañina, puntuación social prohibida, determinados usos biométricos, reconocimiento de emociones prohibido y otros supuestos concretos.

- Alfabetización IA para personal y personas que operan sistemas, adecuada a conocimientos y contexto.

- Transparencia: informar interacción con IA cuando no sea evidente; etiquetar/declarar contenido sintético o deepfakes en los supuestos y plazos aplicables.

- Supervisión humana real: entender límites, ignorar/revertir resultados, detener sistema y escalar.

- Documentar finalidad, instrucciones, limitaciones, pruebas, métricas, incidentes, cambios y evidencias.

- Para alto riesgo, cuando entren en aplicación las obligaciones: gestión de riesgos, gobernanza de datos, documentación técnica, logs, precisión, robustez, ciberseguridad, supervisión humana, evaluación de conformidad, registro y monitorización, según rol.

- No convertir herramienta general en selección laboral, scoring crediticio, acceso a servicios esenciales, diagnóstico o decisión de alto impacto sin evaluación legal/técnica.

- Evitar decisiones exclusivamente automatizadas con efectos jurídicos o similares sobre personas; evaluar art. 22 RGPD, AI Act y norma sectorial.

## 3.3 Calendario verificado a fecha de corte

| **Fecha**        | **Hito**                                                                                                                                             |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2 febrero 2025   | Definiciones, alfabetización IA y prohibiciones iniciales aplicables.                                                                                |
| 2 agosto 2025    | Gobernanza y obligaciones de proveedores de modelos GPAI aplicables.                                                                                 |
| 2 agosto 2026    | Reglas generales aplicables, transparencia del art. 50 y enforcement de obligaciones aplicables.                                                     |
| 2 diciembre 2026 | Nuevas prohibiciones y transición de etiquetado para determinados sistemas generadores de contenido sintético ya comercializados antes del 2/8/2026. |
| 2 diciembre 2027 | Obligaciones para sistemas alto riesgo del Anexo III conforme al calendario modificado.                                                              |
| 2 agosto 2028    | Obligaciones para IA alto riesgo integrada en productos regulados del Anexo I.                                                                       |

El calendario se modificó por el paquete AI Omnibus. Revalidar texto consolidado y guías oficiales antes de lanzamiento/cambio de finalidad.

## 3.4 Seguridad específica de IA

- Prompt injection directa e indirecta en PDF, correo, web, repositorios y documentos recuperados.

- Exfiltración RAG: aplicar permisos antes de recuperar fragmentos; nunca confiar en que el modelo respete instrucciones de confidencialidad.

- Exceso de agencia: agentes sin permisos globales, credenciales maestras ni acceso libre a shell, navegador, correo, pagos o producción.

- Validar salidas con esquema; no ejecutar código, SQL, comandos o HTML generado sin validación y sandbox.

- Gateway de herramientas: allowlist, scopes mínimos, autorización, límites, rate limits, timeouts e idempotencia.

- Envenenamiento de conocimiento: fuentes confiables, hashes, procedencia, revisión, estados draft/approved/deprecated y rollback.

- Prevenir divulgación de secretos con redacción, DLP y pruebas de salida.

- Evaluar alucinaciones, sesgos, jailbreaks, fuga entre tenants, abuso de herramientas y degradación por cambio de modelo.

- Registrar modelo, versión, prompt/política, herramientas, contexto y aprobaciones con protección de datos.

- Fallback: desactivar modelo/herramienta, degradar a lectura/manual, cambiar versión y recuperar servicio.

# 4. Programa corporativo de ciberseguridad

Estructurar el programa con NIST CSF 2.0: Govern, Identify, Protect, Detect, Respond, Recover. ISO/IEC 27001 puede servir como referencia de sistema de gestión. No afirmar certificación ni conformidad hasta auditar alcance y evidencias.

## 4.1 Gobierno y políticas

- Nombrar responsable ejecutivo de riesgo/seguridad y owners técnicos, privacidad, continuidad y proveedores. En equipo pequeño se pueden acumular roles, pero debe haber revisión cruzada.

- Aprobar políticas: seguridad, clasificación, accesos, uso aceptable, desarrollo seguro, cambios, vulnerabilidades, incidentes, backups, continuidad, proveedores, privacidad, IA y retención.

- Registro de riesgos con owner, probabilidad, impacto, controles, residual, fecha y aceptación formal.

- Definir apetito de riesgo y criterios de bloqueo; no aceptar riesgo crítico por conveniencia comercial sin aprobación ejecutiva.

- Revisar políticas anualmente y ante incidentes, cambios normativos, proveedores, sectores o arquitectura.

## 4.2 Identidad y acceso

- MFA resistente a phishing para correo, cloud, repositorios, VPN, consolas y administradores; preferir passkeys/FIDO2.

- SSO cuando sea viable; cuentas individuales; prohibir cuentas compartidas salvo excepción controlada.

- RBAC/ABAC, mínimo privilegio y separación de admin/developer/operador/usuario; acceso temporal JIT.

- Altas, cambios y bajas formales; retirar accesos inmediatamente al terminar relación/cambiar función.

- Revisión trimestral de privilegios, accesos a clientes, cuentas de servicio y tokens.

- Sesiones con expiración/revocación, protección CSRF/XSS y detección de accesos anómalos.

## 4.3 Cloud, red e infraestructura

- Separar desarrollo, pruebas y producción; no usar datos reales en desarrollo por defecto.

- No exponer PostgreSQL, Redis, paneles administrativos ni servicios internos directamente a Internet.

- Red privada, firewall restrictivo, security groups, WAF/API gateway y protección DDoS según exposición.

- TLS en tránsito y cifrado en reposo; gestión de claves, rotación y separación por entorno/cliente cuando proceda.

- Buckets privados, bloqueo de acceso público, URLs firmadas cortas y autorización en cada descarga.

- Infraestructura como código, configuración versionada, revisión y detección de drift.

- Containers hardenizados, no-root, filesystem mínimo, capacidades restringidas y escaneo de imágenes.

- Documentar región, resiliencia, backups, soporte y subprocesadores; región UE no elimina por sí sola riesgos de transferencia.

## 4.4 Desarrollo seguro (SSDLC)

- Threat modelling por flujo: activos, actores, límites de confianza, amenazas y mitigaciones.

- Revisión de código en cambios críticos; ramas protegidas, MFA y secretos bloqueados en CI.

- SAST, SCA, escaneo de secretos, DAST y pruebas API según madurez.

- Dependencias fijadas/actualizadas; verificar origen, firmas y vulnerabilidades; SBOM cuando proceda.

- Tests unitarios, integración, autorización, multi-tenant, fuzzing de parsers y tests negativos.

- Cambios con aprobación, staging, rollback, migraciones seguras y registro de release.

- No introducir datos/credenciales de clientes en repositorios, tickets o herramientas IA sin autorización y controles.

## 4.5 Datos y conocimiento

- Clasificar público, interno, confidencial y restringido; identificar datos personales/sensibles.

- Etiquetar tenant, owner, finalidad, sensibilidad, retención, jurisdicción, fuente y permisos.

- Cifrar, restringir exportación/descarga e incorporar auditoría de acceso a información sensible.

- Aplicar ACL antes de búsqueda semántica/keyword, no después; incluir tenant/permisos en claves de caché y colas.

- Separar RAW, Wiki y Schema; no elevar respuestas IA a conocimiento validado sin revisión y procedencia.

- Pseudonimización sigue siendo dato personal; comprobar reidentificación antes de reutilizar aprendizajes.

## 4.6 Logs, detección y monitorización

- Centralizar logs de autenticación, permisos, cambios, acciones de agentes, herramientas, administración, infraestructura y seguridad.

- No registrar contraseñas, tokens, claves, contenido completo sensible ni prompts personales sin necesidad/base.

- Sincronizar relojes; proteger integridad; limitar acceso y definir retención.

- Alertar sobre login anómalo, MFA fatigue, escalada, descarga masiva, consultas cross-tenant, cambios IAM, secretos expuestos, uso API y picos de coste.

- Asignar responsable, horario, severidad y runbook; probar alertas, no basta con tener panel.

## 4.7 Vulnerabilidades y pruebas

- Inventario de activos/software; escaneo continuo o periódico según exposición/criticidad.

- Priorizar por explotabilidad, exposición, criticidad del activo e impacto; CVSS es input, no decisión única.

- Objetivos internos: crítica explotada/expuesta, mitigación inmediata; alta, plan urgente; media/baja según riesgo y ventana aprobada.

- Parches, excepciones temporales aprobadas, mitigación compensatoria y evidencia de cierre.

- Pentest independiente antes de producción sensible y tras cambios materiales; retest.

- Pruebas adversariales IA: prompt injection, exfiltración, cross-tenant, tool abuse, SSRF, RCE y bypass de autorización.

## 4.8 Criptografía, secretos y endpoints

- Secret manager; nunca .env/credenciales en repositorios o logs.

- Separar claves por entorno y cliente cuando proceda; scopes mínimos, expiración y rotación.

- Usar algoritmos/bibliotecas mantenidos; no diseñar criptografía propia.

- Backups cifrados y claves de recuperación protegidas.

- Portátiles con cifrado completo, bloqueo automático, EDR/antimalware, firewall y parches.

- MDM si existe flota; inventario, borrado remoto y políticas BYOD.

- Gestor de contraseñas, no reutilización, MFA y formación de phishing.

## 4.9 Continuidad y recuperación

- Definir RTO/RPO por servicio/cliente; no inventarlos: aprobarlos según impacto y contratos.

- Backups automáticos y cifrados de DB, documentos, configuración, repositorios y claves necesarias.

- Separar cuenta/credenciales de backup de producción; inmutabilidad/versionado si es viable.

- Probar restauración completa y parcial; no basta con comprobar que el job acabó.

- Plan para pérdida de región, proveedor caído, cuenta comprometida, ransomware, corrupción, fallo modelo y conectividad.

- Runbooks, contactos, dependencias, failover, comunicación y retorno a normalidad.

- Ejercicios al menos anuales y tras cambios relevantes.

# 5. Seguridad de agentes, automatizaciones y herramientas

| **Control**        | **Requisito de diseño**                                                                                                           |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Identidad agente   | Cada agente/worker tiene identidad propia y permisos limitados; no hereda admin.                                                  |
| Tool gateway       | Toda llamada pasa por gateway con allowlist, validación, autorización y registro.                                                 |
| Aprobación humana  | Enviar correo externo, publicar, borrar, pagar, cambiar producción o acceder a datos restringidos requiere aprobación por riesgo. |
| Sandbox            | Código/archivos no confiables aislados, sin secretos ni red salvo autorización.                                                   |
| Límites            | Cuotas, timeouts, rate limits, coste, pasos, tamaño de archivos y recursión.                                                      |
| Idempotencia       | Acciones repetibles con claves idempotentes y control de duplicados.                                                              |
| Estados            | queued, running, blocked, needs_approval, succeeded, failed, cancelled; transiciones auditables.                                  |
| Kill switch        | Pausar agente, revocar tokens, bloquear herramienta y pasar a modo manual.                                                        |
| Sin autoaprobación | Salida LLM nunca concede permisos ni valida su propia acción.                                                                     |
| Segregación        | Contexto, colas, cachés, embeddings y archivos separados por tenant/permisos.                                                     |

# 6. Terceros y cadena de suministro

La seguridad del proveedor cubre solo una parte. Nosotros controlamos selección, contrato, configuración, identidades, datos, integraciones, permisos, supervisión y salida.

## 6.1 Due diligence previa

- Identidad legal, ubicación, jurisdicciones, solvencia y función del proveedor.

- Verificar ISO/SOC: alcance, fecha, excepciones, entidad certificada, sistemas incluidos y opinión; un logo no basta.

- DPA/SCC/adecuación, subencargados, ubicación de datos/soporte, retención, borrado, entrenamiento, telemetría y acceso humano.

- Cifrado, IAM/MFA, segregación, logs, vulnerabilidades, pentest, SDLC, continuidad, backup y respuesta.

- SLA, disponibilidad, soporte, RTO/RPO, notificación, auditoría/evidencias, cooperación y terminación.

- Portabilidad/salida: exportación utilizable, formatos, plazos, costes, borrado certificado y asistencia.

- Cambios de condiciones, modelos, subprocesadores, regiones, funcionalidades o uso de datos.

## 6.2 Cláusulas contractuales mínimas

- Servicio, alcance, responsabilidades y matriz RACI.

- Confidencialidad, propiedad de datos y uso limitado a prestar servicio.

- DPA, subencargados, transferencias y asistencia RGPD.

- Medidas técnicas/organizativas, certificaciones y alcance de auditoría.

- Notificación de incidentes en plazo suficientemente corto para obligaciones legales y del cliente.

- Ubicación y cambios; retención, devolución y borrado.

- SLA, continuidad, recuperación, soporte y portabilidad.

- Derechos de auditoría/inspección razonables y cooperación con reguladores/clientes.

- Responsabilidad, indemnización, límites, seguros y terminación revisados por abogado.

- No entrenamiento/reutilización de datos del cliente salvo autorización expresa, válida y separada.

## 6.3 Matriz de proveedores

| **Capa**                  | **Riesgo**                                                                  | **Mitigación propia**                                                        |
|---------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------|
| LLM/modelo                | Retención, entrenamiento, revisión humana, región, cambio de modelo, caída. | DPA/condiciones, minimización, redacción, versionado, fallback y evaluación. |
| Cloud/hosting             | Cuenta comprometida, región, IAM, caída, lock-in.                           | MFA, IaC, backups externos, segmentación, exportación y salida.              |
| DB/storage                | Exposición pública, ACL errónea, borrado, fuga tenant.                      | Red privada, RLS/ACL backend, tests, cifrado y backups.                      |
| Automatización/conectores | Scopes excesivos, tokens y acciones externas.                               | Scopes mínimos, aprobación, vault, auditoría y revocación.                   |
| Correo/identidad          | Phishing, toma de cuenta, reglas maliciosas.                                | MFA resistente, alertas, sesión y recuperación.                              |
| Repositorios/paquetes     | Dependencia maliciosa y secretos.                                           | Branch protection, SCA, secret scanning, pinning y SBOM.                     |
| Logs/soporte              | Exposición de datos y credenciales.                                         | Redacción, minimización, acceso y retención.                                 |

# 7. Ciberseguridad sectorial y normas condicionales

## 7.1 NIS2

- No convierte automáticamente a toda startup tecnológica en entidad esencial/importante; revisar sectores, tamaño, excepciones, criterios nacionales y cadena de suministro.

- Clientes regulados pueden exigir controles NIS2-flowdown aunque no seamos entidad directamente incluida.

- Si aplica: gobierno de riesgos, incidentes, continuidad/crisis, cadena de suministro, seguridad de desarrollo/mantenimiento, eficacia de controles, higiene, formación, criptografía, acceso y MFA.

- NIS2 prevé notificación escalonada de incidentes significativos; autoridades/canales/plazos dependen de transposición y régimen sectorial.

- La ficha de Comisión consultada para España reflejaba un procedimiento por falta de notificación de transposición completa en mayo de 2025; ese dato histórico no determina por sí solo la situación jurídica española a noviembre de 2026. Verificar BOE y autoridad competente.

## 7.2 DORA

- DORA se aplica directamente a entidades financieras dentro de su ámbito, no automáticamente a cualquier proveedor SaaS.

- Si prestamos servicios TIC a entidades financieras, contratos y auditorías pueden exigir controles flowdown: inventario, subcontratación, ubicación, SLA, incidentes, continuidad, pruebas, auditoría, acceso, salida y cooperación.

- Si el servicio apoya funciones críticas/importantes, requisitos contractuales y de supervisión pueden ser más exigentes.

- Preparar paquete de evidencias DORA para clientes financieros; no afirmar que somos entidad DORA-regulada salvo que corresponda.

## 7.3 Cyber Resilience Act

- Analizar si ponemos en mercado bajo nuestra marca producto con elementos digitales, software descargable, agente instalable, componente embebido o producto comercializado.

- No clasificar automáticamente SaaS remoto como producto sujeto al CRA; analizar alcance, componentes y forma de comercialización.

- A fecha de corte, reporting del art. 14 sobre vulnerabilidades explotadas e incidentes graves aplica desde 11/09/2026; aplicación general prevista desde 11/12/2027.

- Si aplica: proceso de vulnerabilidades, soporte, actualizaciones seguras, SBOM/documentación, evaluación de riesgos, mantenimiento y conformidad.

## 7.4 Data Act

- Evaluar si prestamos servicio de tratamiento de datos/cloud incluido y obligaciones de cambio de proveedor/portabilidad.

- Diseñar exportación de datos y activos del cliente, formatos, APIs y asistencia de salida; revisar cláusulas de switching y costes.

- Distinguir datos personales (RGPD) de no personales; Data Act no desplaza RGPD.

## 7.5 ENS y sector público

- Relevante si el servicio/sistema entra en su ámbito por prestar servicios/soluciones al sector público o por contrato.

- Determinar categoría del sistema con cliente y alcance; definir declaración/certificación que corresponda.

- Revisar cadena suministro, auditorías, incidentes, continuidad, personal, operación y medidas del RD 311/2022.

## 7.6 Sectores que requieren análisis propio

| **Sector/uso**                    | **Normativa y riesgos a analizar**                                                                                                                 |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Banca/pagos/fintech               | DORA, PSD2/PSD3/PSR según estado, AML si realizamos función sujeta, secreto bancario, outsourcing, EBA/ECB, consumidores y decisiones crediticias. |
| Seguros                           | Solvencia II, IDD, distribución, outsourcing, siniestros, decisiones automatizadas, datos salud y requisitos aseguradoras.                         |
| Salud                             | RGPD categorías especiales, Ley 41/2002, MDR/IVDR si software es producto sanitario, AI Act alto riesgo, seguridad clínica.                        |
| RR. HH./empleo                    | AI Act Anexo III según uso, RGPD, Estatuto Trabajadores, igualdad, no discriminación, transparencia y negociación aplicable.                       |
| Administración                    | ENS, contratación pública, interoperabilidad, protección de datos, transparencia y archivo.                                                        |
| Telecom/plataformas               | Código Europeo Comunicaciones, ePrivacy, DSA si somos intermediario/plataforma en ámbito.                                                          |
| Educación/menores                 | RGPD, protección menores, AI Act según uso, normativa educativa y controles reforzados.                                                            |
| Industria/infraestructura crítica | NIS2, normativa sectorial, OT/ICS, seguridad física, continuidad y cadena de suministro.                                                           |

# 8. Web, contratación, IP y empresa

## 8.1 LSSI-CE, web y comercio electrónico

- Aviso legal accesible con identidad del prestador, domicilio/datos registrales cuando proceda, NIF y contacto eficaz.

- Información clara de servicios, precios/impuestos, condiciones, pasos de contratación, corrección de errores, idioma y confirmación.

- Comunicaciones comerciales identificables y consentimiento/base válida; baja sencilla y listas de supresión.

- Cookies no necesarias: consentimiento previo válido, granular y revocable; rechazar tan fácil como aceptar cuando corresponda.

- Contratos B2B/B2C separados; revisar responsabilidad, IP, confidencialidad, datos, SLA y limitaciones.

## 8.2 Propiedad intelectual y secretos

- Inventario de licencias de código, librerías, modelos, datasets, imágenes y documentación; revisar copyleft y obligaciones de distribución.

- Definir titularidad de código, prompts, workflows, documentación, entregables y outputs; no asumir exclusividad o protección de toda salida IA.

- No cargar documentos de terceros/secretos en herramientas sin autorización y evaluación de confidencialidad.

- NDA, control de acceso, clasificación y registro de divulgaciones para preservar secreto empresarial.

- Contrato regula licencia de plataforma, entregables, datos preexistentes, desarrollos a medida, mejoras genéricas y conocimiento anonimizado.

## 8.3 Consumo y accesibilidad

- Si vendemos a consumidores, revisar TRLGDCU, información precontractual, desistimiento, contenido/servicio digital, conformidad, garantías, renovaciones y reclamaciones.

- Analizar Ley 11/2023 y European Accessibility Act para servicios/productos digitales incluidos, excepciones y umbrales de microempresa.

- WCAG como criterio técnico; no confundir cumplimiento técnico con dictamen de aplicabilidad.

## 8.4 Laboral, fiscal y societario

- Contratos laborales/mercantiles, confidencialidad, IP, prevención, seguridad social y políticas de uso de equipos.

- Si IA afecta contratación, evaluación o productividad, revisar información, consulta, privacidad, igualdad y AI Act.

- Facturación, impuestos, conservación documental y obligaciones contables con asesoría fiscal.

# 9. Arquitectura técnica: controles no negociables

| **Componente** | **Controles mínimos antes de datos reales de clientes**                                                          |
|----------------|------------------------------------------------------------------------------------------------------------------|
| Identidad/API  | OIDC/OAuth correctamente configurado, MFA admins, autorización por recurso, rate limit y validación input.       |
| Tenant         | Tenant derivado de identidad verificada; nunca confiar en tenant_id enviado por usuario/LLM; tests cross-tenant. |
| PostgreSQL     | Red privada, roles separados, migraciones, cifrado, backups, ACL/RLS defensa en profundidad.                     |
| Object storage | Buckets privados, políticas tenant, cifrado, URLs temporales, análisis de ficheros y borrado.                    |
| RAG/índices    | ACL antes de recuperar; filtro tenant en indexación/query/caché/logs; borrado de embeddings.                     |
| Agentes        | Identidad propia, allowlist, límites, aprobaciones, sandbox, kill switch y trazabilidad.                         |
| Modelos        | DPA/condiciones revisadas, minimización, no entrenamiento contractual, versionado, evaluación y fallback.        |
| Secretos       | Secret manager, rotación, scopes mínimos, detección de exposición y revocación.                                  |
| CI/CD          | Branch protection, revisión, tests, SAST/SCA/secrets, artefactos trazables y rollback.                           |
| Observabilidad | Logs protegidos, alertas, retención, no registrar secretos ni exceso de datos personales.                        |
| Backup/DR      | Copias cifradas e independientes, pruebas de restauración y RTO/RPO aprobados.                                   |
| Administración | Acceso JIT, auditoría, doble aprobación para acciones críticas y cuentas break-glass.                            |

# 10. Gestión de incidentes

| **Severidad** | **Ejemplos**                                                                                             | **Respuesta mínima**                                                                             |
|---------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Crítica       | Fuga cross-tenant, ransomware, toma admin, exfiltración masiva, claves raíz comprometidas.               | Activar crisis, aislar, revocar, preservar evidencias, legal/privacidad, evaluar notificaciones. |
| Alta          | Acceso no autorizado limitado, vulnerabilidad explotada, indisponibilidad grave, proveedor comprometido. | Contención urgente, alcance, mitigación, comunicación contractual.                               |
| Media         | Malware contenido, error permiso sin explotación, exposición limitada reversible.                        | Remediar, evaluar impacto, documentar y verificar.                                               |
| Baja          | Evento bloqueado o anomalía sin impacto demostrado.                                                      | Registrar, ajustar detección y revisar tendencias.                                               |

## 10.1 Runbook de respuesta

1.  Detectar, registrar hora de detección/constancia y asignar incident commander.

2.  Contener sin destruir evidencias: aislar workload, revocar token, bloquear integración, suspender agente o deshabilitar credencial.

3.  Preservar logs, snapshots, hashes y cadena de custodia.

4.  Determinar sistemas, clientes, datos, personas, regiones, proveedores y período afectados.

5.  Activar privacidad/legal y evaluar RGPD, NIS2, DORA, CRA, contratos y autoridades; los relojes son distintos.

6.  Erradicar causa raíz, parchear, rotar secretos, revisar persistencia e integridad.

7.  Recuperar desde backup limpio, monitorizar y confirmar antes de cierre.

8.  Comunicar coordinadamente y con veracidad; evitar especulación/promesas no verificadas.

9.  Informe post-incidente: causa, impacto, controles fallidos, acciones, owners, fechas y prueba de eficacia.

## 10.2 No mezclar relojes de notificación

- RGPD: 72 horas para autoridad cuando exista riesgo para derechos/libertades; encargado al responsable sin dilación indebida.

- NIS2: régimen escalonado para entidades en ámbito; confirmar transposición y reglas sectoriales.

- DORA: entidades financieras tienen clasificación/plazos propios; el proveedor debe avisar rápido por contrato.

- CRA: desde 11/09/2026 reporting del artículo 14 para fabricantes/productos dentro de alcance.

- Contrato: puede exigir plazos menores; mantener matriz por régimen y cliente.

# 11. Evidencias y registros que mantener

| **Registro**         | **Contenido mínimo**                                                              | **Owner**        | **Revisión**       |
|----------------------|-----------------------------------------------------------------------------------|------------------|--------------------|
| Matriz legal         | Norma, artículo, aplicabilidad, justificación, owner, evidencia, revisión.        | Legal/Compliance | Trimestral/cambio  |
| Tratamientos         | Finalidad, rol, datos, base, destinatarios, retención, transferencias, controles. | Privacidad       | Trimestral         |
| Proveedores          | Servicio, riesgo, ubicación, DPA, subprocesadores, certificaciones, salida.       | Procurement/Sec  | Anual/cambio       |
| Inventario IA        | Modelo, sistema, finalidad, rol AI Act, riesgo, versión, pruebas, supervisión.    | AI Governance    | Cada cambio        |
| Activos              | Activos, owner, exposición, criticidad, dependencia y versión.                    | IT/Sec           | Mensual            |
| Riesgos              | Amenaza, impacto, control, residual, aceptación y tratamiento.                    | Management       | Mensual            |
| Políticas            | Versión, aprobación, alcance, formación y excepciones.                            | Management       | Anual              |
| Evidencias seguridad | Escaneos, pentests, revisiones, pruebas acceso y restauración.                    | Security         | Según plan         |
| Incidentes           | Cronología, decisiones, datos afectados, notificaciones y acciones.               | Incident lead    | Por evento         |
| Continuidad          | BIA, RTO/RPO, runbooks, ejercicios y resultados.                                  | Operations       | Anual              |
| Formación            | Temario, asistentes, evaluación y fecha.                                          | People/Security  | Anual              |
| Contratos            | MSA, DPA, SCC, SLA, NDA y anexos de seguridad.                                    | Legal            | Antes firma/cambio |

# 12. Implantación paso a paso

| **Fase**           | **Trabajo**                                                                                                | **Puerta de salida**                                                |
|--------------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| 0 · Alcance        | Definir servicios, sectores, países, usuarios, datos, roles, flujos y responsabilidades.                   | Mapa producto/servicio y matriz aplicabilidad aprobados.            |
| 1 · Gobierno       | Owners, política base, registro de riesgos y proceso de excepciones.                                       | Responsables, políticas y apetito de riesgo documentados.           |
| 2 · Privacidad     | Tratamientos, roles, bases, avisos, DPA, retención, transferencias y screening EIPD.                       | No entran datos personales reales sin base, información y contrato. |
| 3 · Proveedores    | Due diligence de cloud, DB, modelos, automatización, correo, repositorio y soporte.                        | Proveedor aprobado, contrato/DPA, ubicación y salida.               |
| 4 · Seguridad base | MFA, IAM, entornos, secretos, cifrado, red privada, logs, backups y hardening.                             | Tests de configuración y restore superados.                         |
| 5 · Multi-tenant   | Aislamiento API, DB, RAG, caché, colas, archivos, exportación y logs.                                      | Tests cross-tenant sin fugas; cualquier fallo bloquea.              |
| 6 · IA/agentes     | Inventario AI Act, clasificación, alfabetización, transparencia, gateway, sandbox, evaluación y approvals. | Pruebas adversariales y permisos superados.                         |
| 7 · SSDLC          | CI/CD, SAST/SCA/secrets, DAST, pentest, correcciones y retest.                                             | Críticos/altos cerrados o lanzamiento bloqueado.                    |
| 8 · Incidentes/DR  | Runbooks, contactos, relojes legales, simulacro, backup/restore y RTO/RPO.                                 | Ejercicio completo y recuperación demostrada.                       |
| 9 · Piloto         | Datos limitados, alcance acotado, revisión humana, métricas, soporte y salida.                             | Aceptación piloto y plan de mejora.                                 |
| 10 · Producción    | Auditoría, SLA, soporte, monitorización, revisiones y cumplimiento sectorial.                              | Aprobación negocio, tecnología, seguridad y legal.                  |

## 12.1 Prioridades inmediatas

- No incorporar datos reales de clientes mientras no estén resueltos roles RGPD, contratos, accesos y borrado.

- Elegir primer caso de uso/sector; sin ello no se puede cerrar NIS2, DORA, AI Act alto riesgo, ENS ni regulación sectorial.

- Elegir proveedores y revisar entrenamiento/retención, ubicación, subencargados, DPA y salida.

- Implementar identidad, permisos, aislamiento probado, secretos, logs y backups antes de abrir acceso cliente.

- Crear inventario IA y programa de alfabetización desde ahora.

- Preparar respuesta a incidentes y matriz de notificación con owner legal/privacidad.

- Mantener desarrollo con datos sintéticos y mocks hasta completar baseline.

# 13. Checklist de autorización de producción

- [ ] Alcance, país, sector, rol contractual y matriz legal aprobados.

- [ ] Inventario de datos/tratamientos, bases jurídicas y avisos definidos.

- [ ] DPA, subencargados y transferencias internacionales revisados.

- [ ] Screening EIPD y EIPD realizada cuando proceda.

- [ ] Inventario IA y clasificación AI Act; transparencia y alfabetización cubiertas.

- [ ] Proveedores evaluados; uso de datos, retención, región y salida aceptables.

- [ ] MFA, RBAC, mínimo privilegio y acceso privilegiado revisados.

- [ ] Segregación multi-tenant probada en API, DB, RAG, caché, colas, archivos, logs y backups.

- [ ] Secret manager, rotación, cifrado y gestión de claves operativos.

- [ ] SSDLC, revisión código, SAST/SCA/secrets y gestión vulnerabilidades operativos.

- [ ] Pruebas de seguridad/pentest proporcionados al riesgo completados; críticos cerrados.

- [ ] Agentes con gateway, allowlist, sandbox, límites, aprobaciones y kill switch.

- [ ] Logs/alertas, incidentes, contactos y escalado probados.

- [ ] Backups y restauración probados; RTO/RPO definidos y aprobados.

- [ ] Contratos, SLA, soporte, continuidad, portabilidad y borrado definidos.

- [ ] Documentación, owners, formación y evidencias disponibles.

- [ ] Aprobación formal de negocio, tecnología, seguridad y legal; riesgos residuales aceptados.

# 14. Límites, riesgos residuales y advertencias

Este marco no garantiza ausencia de incidentes, errores, sanciones o reclamaciones. Ningún proveedor ni certificación garantiza seguridad absoluta. Los riesgos residuales deben identificarse, asignarse a un owner y aceptarse por quien tenga autoridad.

- La calificación cambia al incorporar sector regulado o cliente con obligaciones específicas.

- La calificación AI Act depende de finalidad y rol; cambiar uso puede cambiar régimen.

- Transferencias internacionales pueden producirse por soporte, telemetría o subencargados aunque el almacenamiento esté en UE.

- Controles del proveedor no cubren errores de configuración, credenciales comprometidas, integración insegura o uso indebido de agentes.

- Marcos voluntarios no sustituyen la ley ni una auditoría de conformidad.

- Revisar textos/plazos en fuente oficial antes de decisiones relevantes.

# 15. Fuentes oficiales y marcos de referencia

- RGPD — Reglamento (UE) 2016/679 — https://eur-lex.europa.eu/eli/reg/2016/679

- AEPD — medidas de cumplimiento RGPD — https://www.aepd.es/preguntas-frecuentes/2-tus-obligaciones-como-responsable-del-tratamiento/3-que-obligaciones-establece-el-rgpd-para-los-responsables/FAQ-0219-que-medidas-tengo-que-adoptar-para-cumplir-con-la-normativa

- AEPD — seguridad de los tratamientos — https://www.aepd.es/derechos-y-deberes/cumple-tus-deberes/medidas-de-cumplimiento/seguridad-de-los-tratamientos

- AEPD — contenido mínimo EIPD — https://www.aepd.es/preguntas-frecuentes/2-tus-obligaciones-como-responsable-del-tratamiento/10-evaluacion-de-impacto/FAQ-0229-que-debe-incluir-una-evaluacion-de-impacto-de-proteccion-de-datos

- AI Act — texto consolidado EUR-Lex — https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng

- Comisión — calendario AI Act — https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline

- Consejo UE — calendario AI Act 2026 — https://www.consilium.europa.eu/en/policies/artificial-intelligence-act/timeline-artificial-intelligence/

- NIS2 — Directiva (UE) 2022/2555 — https://eur-lex.europa.eu/eli/dir/2022/2555/oj

- Comisión — estado NIS2 España — https://digital-strategy.ec.europa.eu/en/policies/nis2-directive-spain

- DORA — Reglamento (UE) 2022/2554 — https://eur-lex.europa.eu/eli/reg/2022/2554/oj

- ESMA — DORA — https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/digital-operational-resilience-act-dora

- CRA — Reglamento (UE) 2024/2847 — https://eur-lex.europa.eu/legal-content/ES/ALL/?uri=CELEX:32024R2847

- Comisión — CRA reporting 11/09/2026 — https://commission.europa.eu/news-and-media/news/safer-and-more-secure-digital-products-2026-09-11_en

- Data Act — Reglamento (UE) 2023/2854 — https://eur-lex.europa.eu/eli/reg/2023/2854/oj

- LSSI-CE — Ley 34/2002 BOE — https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758

- LOPDGDD — Ley Orgánica 3/2018 BOE — https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673

- ENS — Real Decreto 311/2022 BOE — https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191

- NIST Cybersecurity Framework 2.0 — https://www.nist.gov/cyberframework

- OWASP Top 10 for LLM Applications — https://owasp.org/www-project-top-10-for-large-language-model-applications/

- ISO/IEC 27001 — https://www.iso.org/standard/27001

- ISO/IEC 42001 — https://www.iso.org/standard/42001

# 16. Gobierno de versiones y relación con arquitectura

Versión 1.0 — línea base de trabajo fechada el 16/11/2026. La siguiente iteración debe incorporar primer sector/caso de uso, proveedores y contratos concretos, flujos reales de datos, roles RGPD/AI Act, análisis NIS2/DORA/CRA/ENS según alcance y revisión de abogado y especialista de seguridad.

Propietario: dirección del proyecto. Revisión trimestral y extraordinaria ante cambio normativo, nuevo sector/proveedor/tratamiento, incidente o cambio material.

Relación documental: complementa —no sustituye ni duplica— Guía de Arranque v1.4 y Atlas. La arquitectura ya contempla aislamiento multi-cliente, permisos backend, gateway de herramientas, aprobaciones humanas, backups, observabilidad y respuesta a fallos; este documento desarrolla cumplimiento, evidencias y gobierno.
