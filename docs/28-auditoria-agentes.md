<!-- Generado por tools/auditoria_gen.py desde tools/org_data/auditoria.py. No editar a mano. -->
# Auditoría de agentes y habilidades frente a los procesos (M-040)

**Estado:** propuesta (D-026), pendiente de los socios. **No se ha borrado ni cambiado ningún agente:** `tools/org_data/agentes.py` y `tools/org_data/habilidades.py` siguen igual hasta que se apruebe. Fecha: 26/11/2026 (tanda de las 22:00).

## Conclusión

De 34 agentes se proponen mantener 22, fusionar 5 y retirar 7. De 65 habilidades, mantener 56, fusionar 3 y retirar 6. Lo que se retira no sirve hoy a ningún proceso del catálogo ni al proceso de referencia: los cinco expertos de sectores que no son seguros, y la administración y la contabilidad de una sociedad que aún no existe. Lo que se fusiona son pares que comparten la misma ficha de conocimiento y el mismo proceso. Cada agente y cada habilidad que se queda tiene al menos un proceso y una métrica que diría si lo hace bien.

## Criterio

1. **Proceso antes que agente** ([CLAUDE.md](../CLAUDE.md)). Un agente existe porque un proceso de [P01–P38](13-procesos-y-estados.md) o el [proceso de referencia](../processes/referencia-seguros-apertura-siniestros/README.md) lo necesita; si no, es una ficha, no capacidad ([plan maestro, punto 4](23-plan-maestro.md)).
2. **Lo más simple que funcione.** La guía de Anthropic sobre agentes eficaces recomienda «find the simplest solution possible, and only increasing complexity when needed» y distingue los flujos de trabajo, donde el modelo y las herramientas siguen «predefined code paths», de los agentes que deciden sus propios pasos ([ANTHROPIC-AGENTES](../knowledge/fuentes/registro.md#anthropic-agentes)). Nuestros puestos son, en sus términos, trabajadores de un orquestador (el CEO limitado): cada uno más es una ruta más que probar.
3. **Métrica o nada.** Cada agente y habilidad que se queda dice qué número mostraría que lo hace bien. Varias métricas aún no se pueden medir (no hay clientes): se miden con los casos inventados hasta el 15/02/2027.
4. **Fusionar si comparten ficha y proceso; retirar si no hay proceso.** Al retirar se conserva la ficha de conocimiento y se dice qué tendría que pasar para recuperarlo.

## Agentes

| Agente | Departamento | Veredicto | Procesos · métrica, o motivo |
|---|---|---|---|
| CEO digital (`ceo`) | Dirección | mantener | P01, P02, P03, P05, P06, P11 · Acierto de decisión en el banco del Control A (25 encargos de processes/ceo-control-a/; umbral pendiente del 22/01/2027) · Solo el CEO limitado que pide el proceso de referencia (D-006). |
| Plan y seguimiento (`pmo`) | Dirección | mantener | P05, P12, P38 · Semanas del plan con su «hecho cuando» cumplido y con evidencia en el repositorio · Absorbe el registro de decisiones (P12). |
| Registro de decisiones (`dec`) | Dirección | fusionar | Con **pmo**. Comparte con Plan y seguimiento la misma ficha de conocimiento (decisiones-seguimiento) y su único proceso (P12) lo puede llevar el PMO. Con dos socios a 10–15 h semanales, dos agentes para el mismo cuaderno duplican la coordinación. |
| Bibliotecario (`bib`) | Dirección | mantener | P04, P07, P11, P13 · Porcentaje de fichas de conocimiento con fuente externa (29,1 % el 26/11/2026 con la medida corregida en K1; `carga_conocimiento.medir()`) y respuestas con cita que existe |
| Jefe comercial (`comj`) | Comercial y clientes | mantener | P31, P32 · Oportunidades con decisión de seguir o no (go/no-go) registrada y motivo · Absorbe Validación y Contenido. |
| Validación (`val`) | Comercial y clientes | fusionar | Con **comj**. Las conversaciones de validación alimentan la cualificación (P31) y usan el mismo método que el descubrimiento (P32, The Mom Test). Juan decidió el 26/11 que Claude no haga por ahora la primera conversación (M-010): un agente propio no tiene trabajo hasta entonces. |
| Prospección (`pros`) | Comercial y clientes | mantener | P31 · Cuentas que pasan a cualificadas tras la primera conversación |
| Propuestas (`prop`) | Comercial y clientes | mantener | P31, P38 · Propuestas que cumplen la rúbrica de C3 (src/varios/calidad/rubrica.py) a la primera, y tasa de aceptación |
| Contenido (`cont`) | Comercial y clientes | fusionar | Con **comj**. Ningún proceso del catálogo produce contenido de web o LinkedIn, lo publican los socios y la web para clientes espera a la marca (M-002). La habilidad de posicionamiento se retira hasta entonces. |
| Arquitecto de procesos (`proj`) | Procesos | mantener | P32, P33, P34, REF-SIN · Casos del proceso que pasan sin corrección humana y pasos eliminados frente al AS-IS |
| Datos de prueba (`dat`) | Procesos | mantener | P23, REF-SIN · Excepciones del catálogo EX-01–EX-15 con al menos un caso inventado y resultado esperado (15 de 15 el 26/11/2026) · Separado de IA y evaluación a propósito: quien escribe el examen no es quien ajusta el modelo para aprobarlo. |
| Métricas (`kpi`) | Procesos | mantener | P18, P32, P37 · Métricas prometidas con ficha completa y línea base medida antes del cambio |
| Arquitecto técnico (`ingj`) | Ingeniería | mantener | P25, P34 · Cambios en main con CI en verde y que se pueden revertir |
| Backend (`back`) | Ingeniería | mantener | P01, P08, P14, P22, P24, P35 · Pruebas de aislamiento entre clientes en verde contra PostgreSQL real |
| IA y evaluación (`ia`) | Ingeniería | mantener | P02, P09, P16, P23 · Acierto por campo de la extracción frente a los «hechos» de los 20 casos, y tasa de invenciones |
| Integraciones (`int`) | Ingeniería | mantener | P21, P30, P36 · Acciones no autorizadas bloqueadas y reintentos sin duplicados |
| Calidad y riesgo (`calj`) | Calidad, seguridad y legal | mantener | P09, P10, P15, P19 · Entregables devueltos por Calidad y defectos que encuentran los socios después de Calidad |
| Seguridad (`sec`) | Calidad, seguridad y legal | mantener | P14, P17, P20, P26, P28, P30 · Pruebas de aislamiento e inyección en verde (trampas del Control A: 5 de 5) y hallazgos abiertos |
| Legal y privacidad (`leg`) | Calidad, seguridad y legal | mantener | P07, P19, P24, P27, P28 · Obligaciones mapeadas con fuente oficial y preguntas resueltas por el abogado · Absorbe Cumplimiento normativo. Todo lo suyo es borrador para abogado. |
| Administración (`admj`) | Administración | retirar | Ningún proceso del catálogo cubre trámites de la empresa y la sociedad aún no existe (forma jurídica antes del 08/01/2027, D2). Lo que hace hoy (preguntas al gestor) ya lo hace Legal con «preguntas-profesional». **Se recupera si:** Los socios eligen la forma jurídica y hay trámites recurrentes (altas, impuestos). |
| Costes (`fin`) | Administración | fusionar | Con **cfo**. Comparte con el Director financiero el coste por caso y el presupuesto (P29); dos agentes de dinero sin ingresos ni gastos reales es duplicar. |
| Proveedores (`prov`) | Administración | mantener | P27 · Proveedores en uso con ficha completa: ubicación de datos, condiciones y salida |
| Coordinación sectorial · Seguros (`seg`) | Sectores | mantener | P02, P32, P33, REF-SIN · Correcciones sectoriales de los socios por encargo (objetivo: bajan semana a semana) |
| Experto en sanidad privada (`sal`) | Sectores | retirar | El único proceso de cliente es de seguros (D-011) y no hay ninguna oportunidad de sanidad en P31. **Se recupera si:** Una oportunidad de sanidad privada pasa la cualificación (P31). La ficha de conocimiento se conserva. |
| Experto en asesorías y despachos (`ase`) | Sectores | retirar | No hay proceso ni oportunidad de asesorías o despachos; el estudio de prospectos de Álvaro aún no ha elegido nicho (12/02/2027). **Se recupera si:** Una oportunidad del sector pasa P31 o los socios eligen el nicho. La ficha de conocimiento se conserva. |
| Experto en servicios financieros (`fnz`) | Sectores | retirar | Sin proceso ni oportunidad de financiero no bancario; DORA ya lo cubre Legal para aseguradoras. **Se recupera si:** Una oportunidad del sector pasa P31. La ficha de conocimiento se conserva. |
| Experto en industria (`ind`) | Sectores | retirar | Sin proceso ni oportunidad de industria. **Se recupera si:** Una oportunidad del sector pasa P31. La ficha de conocimiento se conserva. |
| Experto en logística (`logi`) | Sectores | retirar | Sin proceso ni oportunidad de logística. **Se recupera si:** Una oportunidad del sector pasa P31. La ficha de conocimiento se conserva. |
| Director financiero (`cfo`) | Administración | mantener | P29, P31 · Coste por caso frente al presupuesto y margen por fase en cada propuesta · Absorbe Costes. La previsión de tesorería espera a la primera factura. |
| Contabilidad y facturación (`conta`) | Administración | retirar | No hay sociedad, ni facturas, ni cobros: ningún proceso del catálogo lo necesita antes del 15/02/2027. **Se recupera si:** Se constituye la sociedad y se firma el primer diagnóstico con factura. |
| Plataforma y operaciones (`ops`) | Ingeniería | mantener | P15, P17, P26, P28 · Tiempo de recuperación ensayado con una restauración real |
| Diseño y experiencia (`ux`) | Ingeniería | mantener | P03, P10 · Aprobaciones y preguntas que un socio resuelve sin ayuda y tiempo hasta decidir · La interfaz de aprobación es donde se juega P10; si no hay cliente con pantallas propias, no crece. |
| Éxito de cliente (`exito`) | Comercial y clientes | mantener | P37, P38 · Pilotos que cumplen la métrica firmada (pago 50/50) y retención en Operar · Sin cliente hasta el 15/02/2027: diseña el plan de éxito, no lo ejecuta. |
| Cumplimiento normativo (`cump`) | Calidad, seguridad y legal | fusionar | Con **leg**. Comparte la ficha de conocimiento «cumplimiento» con Legal y Calidad y sus procesos (P19, P24) ya los lleva Legal. Sin abogado ni cliente regulado, dos agentes legales producen dos borradores de lo mismo. Sus habilidades pasan a Legal. |

## Habilidades

| Habilidad | La usan hoy | Veredicto | Procesos · métrica, o motivo |
|---|---|---|---|
| Voz y formato de Varios (`marca-varios`) | pmo, comj, prop, cont, ux, exito | mantener | P11, P31 · Criterio de claridad de la rúbrica C3 en 4 o más en los entregables |
| Separar hecho, hipótesis y propuesta (`hecho-hipotesis-propuesta`) | ceo, dec, bib, comj, val, pros, prop, cont, dat, kpi, ia, calj, fin, seg, cfo, conta, ux | mantener | P02, P09, P13 · Cifras sin fuente ni etiqueta en entregables revisados (objetivo: 0; es bloqueante en la rúbrica C3) |
| Leer y citar el cerebro (`citar-cerebro`) | bib | mantener | P04 · Respuestas con al menos una cita a una ruta que existe · Hoy solo la tiene el Bibliotecario; la propuesta es que P04 la aplique a todos los encargos. |
| Acta de reunión (`acta-reunion`) | pmo, dec, val, exito | mantener | P12, P32 · Siguientes pasos con responsable y fecha (100 %) |
| Entrada de DECISIONS.md (`decision-registro`) | ceo, dec, ingj, admj | mantener | P12, P25 · Entradas de DECISIONS.md con motivo, alternativas y estado · Absorbe «adr». |
| Contrato de tarea (`contrato-de-tarea`) | ceo | mantener | P01, P02 · Encargos con contrato de tarea completo: confirmado, inferido y desconocido |
| Las cinco decisiones del CEO (`cinco-decisiones`) | ceo | mantener | P02 · Acierto de decisión en el banco del Control A |
| Plan con responsables y criterio (`plan-con-criterio`) | ceo, pmo, comj, proj, admj | mantener | P05 · Tareas del plan con criterio de aceptación comprobable |
| Consultar el histórico antes de hacer (`consultar-historico`) | ceo | mantener | P04, P05 · Encargos parecidos a uno anterior en los que se cita el precedente |
| Seguimiento semanal del plan (`plan-semanal`) | pmo | mantener | P05, P38 · Semanas con «hecho cuando» cumplido y con evidencia |
| Registro RAID (`raid`) | pmo | mantener | P05, P38 · Riesgos con dueño y fecha de revisión, y cerrados a tiempo |
| Análisis de opciones para decidir (`analisis-opciones`) | dec, cfo | mantener | P12, P33 · Decisiones que se presentan con al menos dos alternativas y lo que cuesta cada una |
| Ficha de conocimiento (`ficha-conocimiento`) | bib | mantener | P13 · Fichas con fuente, fecha y estado |
| Contraste de fuentes (`contraste-fuentes`) | bib, leg, prov, ase, fnz, cump | mantener | P04, P13 · Afirmaciones críticas (legales, plazos, cifras) con dos fuentes («validated») |
| Cualificación de oportunidad (`cualificacion-oportunidad`) | comj | mantener | P31 · Oportunidades con go/no-go y motivo |
| Entrevista de descubrimiento (`entrevista-descubrimiento`) | val | mantener | P32 · Conversaciones con al menos un hecho del pasado (no opiniones) por hipótesis |
| Síntesis de entrevistas (`sintesis-entrevistas`) | val | mantener | P32 · Hipótesis validadas o descartadas con su evidencia |
| Cliente ideal (ICP) (`icp`) | pros | mantener | P31 · Cuentas del ICP que pasan a cualificadas |
| Investigación previa de una cuenta (`investigacion-cuenta`) | pros | mantener | P31 · Primeras conversaciones con la ficha de la cuenta preparada y con fuentes |
| Propuesta de diagnóstico (`propuesta-diagnostico`) | prop | mantener | P31, P38 · Propuestas que cumplen la rúbrica C3 a la primera |
| Caso de negocio (`business-case`) | comj, prop, kpi, fin, cfo | mantener | P31, P37 · Casos de negocio con cada cifra marcada como medida, declarada o hipótesis |
| Mensaje y posicionamiento (`mensaje-posicionamiento`) | cont | retirar | Solo la usaba Contenido y ningún proceso del catálogo la necesita; los textos de la web (docs/26) esperan a la marca. **Se recupera si:** Los socios deciden la marca (M-002) y aprueban publicar la web. |
| Mapa del proceso actual (AS-IS) (`mapeo-as-is`) | proj | mantener | P32, REF-SIN · Mapas AS-IS validados por quien hace el proceso, con tiempos activo y de espera |
| Diseño del proceso nuevo (TO-BE) (`diseno-to-be`) | proj | mantener | P33, REF-SIN · Diseños TO-BE aprobados por el cliente en la puerta G2 (diseño aceptado) |
| Matriz IA · regla · persona (`matriz-ia-regla-persona`) | proj | mantener | P33 · Pasos con la decisión IA, regla o persona justificada; ninguna regla resuelta por IA |
| Informe AS-IS / TO-BE (`informe-as-is-to-be`) | proj | mantener | P32, P33 · Informes que cumplen la rúbrica C3 a la primera |
| Casos de prueba inventados (`casos-sinteticos`) | dat | mantener | P23, REF-SIN · Reglas y excepciones con caso y resultado esperado |
| Ficha de métrica (`ficha-metrica`) | kpi, exito | mantener | P37 · Métricas prometidas con ficha completa |
| Línea base (`linea-base`) | kpi | mantener | P32, P37 · Métricas con línea base medida antes del cambio |
| Especificación para Claude Code (`spec-tecnica`) | ingj, back, ia, ops | mantener | P08, P25 · Tareas de construcción que pasan la revisión sin rehacer |
| Decisión de arquitectura (`adr`) | ingj | fusionar | Con **decision-registro**. CLAUDE.md manda justificar cada tecnología nueva en DECISIONS.md: un formato aparte para las decisiones de arquitectura es un segundo registro de lo mismo. |
| Modelo de datos (`modelo-datos`) | back | mantener | P14, P24, P34 · Migraciones al día con los modelos (alembic check en CI) y RLS forzada en cada tabla con cliente |
| Pruebas antes que código (`pruebas`) | ingj, back, ia, int, sec | mantener | P08, P23, P25 · CI en verde y regla nueva con su prueba |
| Evaluación de modelos (`evaluacion-modelos`) | ia | mantener | P16, P23 · Cambios de modelo o instrucciones con evaluación antes y después |
| Ficha de integración (`ficha-integracion`) | int | mantener | P36 · Conectores con ficha, permisos mínimos y prueba de revocación |
| Criterio de aceptación (`criterio-aceptacion`) | calj | mantener | P05, P09 · Entregables con criterio de aceptación desde que se abren |
| Revisión de un entregable (`revision-entregable`) | calj, sec | mantener | P09 · Defectos que encuentran los socios después de Calidad |
| Modelo de amenazas (`modelo-amenazas`) | ingj, int, sec, ops | mantener | P14, P20, P21 · Amenazas con control y prueba |
| Revisión de riesgo de IA y datos (`revision-riesgo-ia`) | leg | mantener | P19, P24 · Usos de IA sobre datos de personas con revisión antes de construir |
| Mapa de obligaciones (`mapa-obligaciones`) | leg, seg, sal, ase, fnz, ind, logi, cump | mantener | P19, P33 · Obligaciones con fuente oficial, control y evidencia · Absorbe «matriz-cumplimiento». |
| Preguntas para un profesional externo (`preguntas-profesional`) | leg, admj, conta | mantener | P19, P27 · Preguntas al abogado o al gestor con respuesta y fecha |
| Coste unitario (`coste-unitario`) | fin, cfo | mantener | P29 · Coste por caso medido frente al presupuesto |
| Ficha de proveedor (`ficha-proveedor`) | prov | mantener | P27 · Proveedores en uso con ficha completa |
| Claves del sector para un encargo (`claves-sector`) | seg, sal, ase, fnz, ind, logi | mantener | P02, P32, REF-SIN · Encargos de un sector con sus claves antes de empezar y correcciones sectoriales de los socios |
| Glosario del sector (`glosario-sector`) | seg, sal, ase, ind, logi | mantener | P13, P32 · Términos del sector con definición y fuente (35 en seguros el 26/11/2026) |
| Cierre contable mensual (`cierre-mensual`) | conta | retirar | Solo la usa Contabilidad, que se propone retirar: no hay sociedad ni movimientos. **Se recupera si:** Se constituye la sociedad. |
| Facturación y cobro (`facturacion-cobro`) | conta | retirar | Solo la usa Contabilidad; no hay facturas hasta el primer diagnóstico. **Se recupera si:** Se firma el primer diagnóstico con factura. |
| Paquete trimestral para el gestor (`paquete-gestor`) | conta | retirar | Solo la usa Contabilidad; no hay trimestres que cerrar. **Se recupera si:** Se constituye la sociedad y empieza el primer trimestre con actividad. |
| Previsión de tesorería a 13 semanas (`prevision-tesoreria`) | cfo | retirar | La hoja precio-y-caja.xlsx (D2) ya cubre la caja a 18 meses sin ingresos; una previsión semanal no aporta hasta que haya cobros. **Se recupera si:** Se firma el primer diagnóstico y entran o salen pagos cada semana. |
| Margen por proyecto y fase (`margen-proyecto`) | cfo | mantener | P29, P31 · Propuestas con margen por fase calculado antes de enviarlas |
| Financiación pública y ventajas fiscales (`financiacion-publica`) | cfo | retirar | Ningún proceso del catálogo la usa y todavía no hay sociedad con la que pedir una ayuda. **Se recupera si:** Los socios eligen la forma jurídica (antes del 08/01/2027). |
| Integración continua (`integracion-continua`) | ops | mantener | P17, P25 · Duración de CI y fallos de CI arreglados antes de la siguiente subida |
| Copias y restauración probada (`copias-restauracion`) | ops | mantener | P26 · Restauraciones reales ensayadas y su tiempo |
| Runbook y gestión de incidentes (`runbook-incidente`) | ops | mantener | P15, P28 · Incidentes con runbook seguido y lección registrada |
| Observabilidad y alertas (`observabilidad`) | ops | mantener | P15 · Errores detectados por alerta antes que por un socio |
| Flujo y pantallas de una tarea (`flujo-pantallas`) | ux | mantener | P10, P33 · Tareas críticas con flujo dibujado antes de construir |
| Prueba de usabilidad (`prueba-usabilidad`) | ux | mantener | P10 · Tareas completadas sin ayuda en la prueba |
| Revisión de accesibilidad (`revision-accesibilidad`) | ux | mantener | P10, P11 · Errores de accesibilidad WCAG 2.2 AA abiertos al entregar |
| Plan de éxito del cliente (`plan-exito-cliente`) | exito | mantener | P38 · Clientes con plan de éxito firmado al empezar el diagnóstico o el piloto |
| Revisión de valor con el cliente (`revision-valor`) | exito | mantener | P37 · Revisiones con la métrica firmada medida frente a la línea base · Absorbe «salud-cuenta». |
| Salud de la cuenta (`salud-cuenta`) | exito | fusionar | Con **revision-valor**. Mide lo mismo que la revisión de valor con otra frecuencia (mensual frente a trimestral). Sin clientes, una sola habilidad con indicadores mensuales basta. |
| Inventario y clasificación de sistemas de IA (`inventario-ia`) | cump | mantener | P16, P19 · Usos de IA inventariados y clasificados por riesgo con fuente |
| Registro de actividades de tratamiento (`registro-tratamientos`) | cump | mantener | P24 · Tratamientos con finalidad, base y plazo de conservación |
| Programa de alfabetización en IA (`alfabetizacion-ia`) | cump | mantener | P19 · Personas de Varios con la formación del art. 4 registrada |
| Matriz obligación → control → evidencia (`matriz-cumplimiento`) | cump | fusionar | Con **mapa-obligaciones**. La matriz obligación → control → evidencia es el mapa de obligaciones con dos columnas más; mantener las dos crea dos listas que se desincronizan. |

## Cobertura de los procesos si se aprueba

Agentes que quedan en cada proceso. Ningún proceso se queda sin agente; los que solo tienen uno dependen de que ese agente funcione.

| Proceso | Cuándo | Agentes |
|---|---|---|
| P01 · Alta y recepción de petición | MVP | Backend, CEO digital |
| P02 · Clasificación y triaje | MVP | CEO digital, IA y evaluación, Coordinación sectorial · Seguros |
| P03 · Gestión de aclaraciones | MVP | CEO digital, Diseño y experiencia |
| P04 · Recuperación de conocimiento | MVP | Bibliotecario |
| P05 · Diseño del plan | MVP | CEO digital, Plan y seguimiento |
| P06 · Asignación y coordinación | MVP | CEO digital |
| P07 · Ingesta documental | Antes de datos reales | Bibliotecario, Legal y privacidad |
| P08 · Ejecución de tareas | MVP | Backend |
| P09 · Control de calidad | MVP | Calidad y riesgo, IA y evaluación |
| P10 · Aprobación humana | MVP | Calidad y riesgo, Diseño y experiencia |
| P11 · Entrega y cierre | MVP | Bibliotecario, CEO digital |
| P12 · Gestión de cambios | Antes de escalar | Plan y seguimiento |
| P13 · Aprendizaje y actualización de la wiki | Antes de escalar | Bibliotecario |
| P14 · Gestión de permisos y aislamiento | Antes de datos reales | Backend, Seguridad |
| P15 · Observabilidad e incidencias | MVP | Calidad y riesgo, Plataforma y operaciones |
| P16 · Gobierno de modelos e instrucciones | Antes de escalar | IA y evaluación |
| P17 · Seguridad y continuidad | Antes de datos reales | Plataforma y operaciones, Seguridad |
| P18 · Evaluación y mejora | Antes de escalar | Métricas |
| P19 · Política de uso y límites | Antes de automatizar | Calidad y riesgo, Legal y privacidad |
| P20 · Seguridad de entradas e inyección de instrucciones | Antes de datos reales | Seguridad |
| P21 · Ejecución segura de herramientas | Antes de automatizar | Integraciones |
| P22 · Gestión de errores y reintentos | Antes de automatizar | Backend |
| P23 · Evaluación de agentes y modelos | Antes de escalar | Datos de prueba, IA y evaluación |
| P24 · Gestión del ciclo de vida del dato | Antes de datos reales | Backend, Legal y privacidad |
| P25 · Gestión de cambios y versiones | Antes de escalar | Arquitecto técnico |
| P26 · Continuidad y recuperación | Antes de escalar | Plataforma y operaciones, Seguridad |
| P27 · Gestión de proveedores y dependencias | Antes de datos reales | Legal y privacidad, Proveedores |
| P28 · Gestión de incidentes | Antes de escalar | Legal y privacidad, Plataforma y operaciones, Seguridad |
| P29 · Gestión de costes y capacidad | Antes de automatizar | Director financiero |
| P30 · Gestión de identidades y secretos | Antes de datos reales | Integraciones, Seguridad |
| P31 · Calificación de oportunidad | MVP | Director financiero, Jefe comercial, Propuestas, Prospección |
| P32 · Descubrimiento de procesos | MVP | Jefe comercial, Métricas, Arquitecto de procesos, Coordinación sectorial · Seguros |
| P33 · Diseño y validación TO-BE | MVP | Arquitecto de procesos, Coordinación sectorial · Seguros |
| P34 · Gestión de definiciones de proceso | MVP | Arquitecto técnico, Arquitecto de procesos |
| P35 · Gestión de instancias y excepciones | MVP | Backend |
| P36 · Gestión del catálogo de conectores | Antes de automatizar | Integraciones |
| P37 · Medición de rendimiento y valor | MVP | Éxito de cliente, Métricas |
| P38 · Gestión de despliegue por cliente | Antes de datos reales | Éxito de cliente, Plan y seguimiento, Propuestas |
| REF-SIN · Apertura de siniestros en corredurías (proceso de cliente de referencia, D-011) | Proceso de cliente | Datos de prueba, Arquitecto de procesos, Coordinación sectorial · Seguros |

Procesos con un solo agente: P04, P06, P08, P12, P13, P16, P18, P20, P21, P22, P25, P29, P35, P36.

## Qué cambiaría en `agentes.py` si se aprueba

- **Registro de decisiones** pasa a **Plan y seguimiento**, que recibe `decision-registro`, `analisis-opciones`, `hecho-hipotesis-propuesta`.
- **Validación** pasa a **Jefe comercial**, que recibe `entrevista-descubrimiento`, `sintesis-entrevistas`, `acta-reunion`.
- **Contenido** pasa a **Jefe comercial**.
- **Cumplimiento normativo** pasa a **Legal y privacidad**, que recibe `inventario-ia`, `registro-tratamientos`, `alfabetizacion-ia`.
- **Costes** pasa a **Director financiero**.
- Se marcan como retirados, sin borrar su ficha: Administración, Contabilidad y facturación, Experto en sanidad privada, Experto en asesorías y despachos, Experto en servicios financieros, Experto en industria, Experto en logística.
- Las habilidades fusionadas se unen a su destino: `adr` en `decision-registro`; `salud-cuenta` en `revision-valor`; `matriz-cumplimiento` en `mapa-obligaciones`.
- D-020 (seis puestos nuevos) se revisa: de los seis, se quedan Director financiero, Éxito de cliente, Plataforma y operaciones y Diseño y experiencia; Contabilidad se retira y Cumplimiento se une a Legal.

## Cómo se mantiene

- La fuente es `tools/org_data/auditoria.py`; este documento se genera con `python3 tools/auditoria_gen.py`.
- `tests/test_auditoria_agentes.py` falla si se añade un agente o una habilidad sin entrada en la auditoría, si una entrada que se mantiene no tiene proceso existente o métrica, si una fusión apunta a algo que no se queda, si una retirada no dice cómo se recupera, si un proceso se queda sin agente o si este documento no está al día.
- El nivel de autonomía de cada proceso (A0–A4) sale de esta auditoría en N1 (M-045).
