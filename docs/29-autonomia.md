<!-- Generado por tools/autonomia_gen.py desde processes/autonomia.json. No editar a mano. -->
# Mapa de autonomía por proceso, A0–A4 (M-045)

**Estado:** propuesta (D-027). Fecha: 26/11/2026. Fuente máquina: [processes/autonomia.json](../processes/autonomia.json). Sale de la [auditoría de agentes](28-auditoria-agentes.md) (N2): cada proceso tiene agentes que se quedan y una métrica.

## Conclusión

Hoy todos los procesos están en A0: ningún proceso funciona todavía de punta a punta (docs/23, punto 4). El objetivo de febrero es con datos inventados. Para el 12/02/2027 se propone: 9 en A0, 21 en A1, 2 en A2, 7 en A3. 22 de los 39 procesos tocan algo externo, legal, financiero o contractual y tienen el techo en A2 o por debajo; la aprobación humana (P10) no pasa nunca de A1.

## Niveles

| Nivel | Qué hace el sistema |
|---|---|
| A0 | Ayuda a una persona |
| A1 | Propone y una persona decide |
| A2 | Ejecuta con aprobación previa |
| A3 | Ejecuta y avisa |
| A4 | Autónomo con muestreo |

Los niveles son los de [docs/22](22-plan-hasta-febrero.md) («La autonomía se gana con datos»). Coinciden con los cinco papeles del usuario que proponen Feng, McDonald y Zhang (Knight First Amendment Institute, 2025): operador, colaborador, consultor, aprobador y observador. De ellos se toma la idea central: la autonomía «can instead be a deliberate design decision» independiente de la capacidad, de modo que un agente capaz puede trabajar con poca autonomía si debe consultar antes de cada acción ([KNIGHT-NIVELES-AUTONOMIA](../knowledge/fuentes/registro.md#knight-niveles-autonomia)). El techo de cada proceso sigue la tabla de riesgo de la [Guía v1.4](fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md) (§3: lo de riesgo alto se prepara pero no se finaliza ni se envía solo) y la regla de [CLAUDE.md](../CLAUDE.md): Lo externo, legal, financiero y contractual nunca pasa de A2.

## Cómo se sube y se baja (propuesta)

- **Subir un nivel** (nunca dos de golpe): la métrica del proceso cumple el umbral durante el periodo y lo aprueba un socio. El periodo propuesto para todos es «4 semanas seguidas sobre el banco de casos completo, sin ningún fallo grave»; el umbral es por decidir por los socios (umbral del examen, 22/01/2027).
- **Bajar:** Baja a A1 en el acto con un fallo grave (acción no autorizada, dato de otro cliente, cifra o fuente inventada); baja un nivel si la métrica queda por debajo del umbral dos semanas seguidas.
- **Nunca por encima del techo.** Subir el techo de un proceso sensible no es una mejora técnica: exige cambiar CLAUDE.md, y eso lo deciden los socios.
- Los periodos y la regla de bajada son una propuesta de esta noche, no un dato: los fijan los socios con D-027.

## Procesos

| Proceso | Toca | Hoy | Febrero | Techo | Métrica para subir | Agentes | Nota |
|---|---|---|---|---|---|---|---|
| P01 · Alta y recepción de petición | — | A0 | A3 | A4 | Peticiones registradas con el cliente sacado de la identidad (pruebas de acceso cruzado en verde) | ceo, back |  |
| P02 · Clasificación y triaje | — | A0 | A1 | A3 | Acierto de decisión en el banco del Control A frente al umbral que fijen los socios el 22/01/2027 | ceo, ia, seg | Las trampas (inyección, otro cliente, autoaprobación) las paran reglas fijas, no el nivel. |
| P03 · Gestión de aclaraciones | externo | A0 | A1 | A2 | Preguntas que el solicitante entiende a la primera (sin segunda aclaración) | ceo, ux | Preguntar al solicitante es comunicarse con el cliente. |
| P04 · Recuperación de conocimiento | — | A0 | A3 | A4 | Respuestas con cita que existe y consultas sin resultado | bib |  |
| P05 · Diseño del plan | — | A0 | A1 | A3 | Planes aprobados sin cambios por el socio | ceo, pmo |  |
| P06 · Asignación y coordinación | — | A0 | A2 | A3 | Tareas asignadas al agente correcto a la primera y bloqueos por semana | ceo |  |
| P07 · Ingesta documental | legal | A0 | A1 | A2 | Documentos bien clasificados y cuarentenas justificadas | bib, leg | Clasificar datos personales tiene efecto legal (RGPD). |
| P08 · Ejecución de tareas | externo | A0 | A1 | A2 | Tareas que pasan Calidad a la primera, errores por tipo y coste por tarea | back | Puede ejecutar acciones en sistemas del cliente. |
| P09 · Control de calidad | — | A0 | A3 | A3 | Defectos que encuentran los socios después de Calidad | ia, calj | Calidad avisa; la entrega sigue pasando por P10 (D-019). |
| P10 · Aprobación humana | externo, legal, financiero, contractual | A0 | A1 | A1 | Tiempo de aprobación y rechazos | ux, calj | Es el propio control humano: nunca sube de A1. |
| P11 · Entrega y cierre | externo, contractual | A0 | A1 | A2 | Entregas aceptadas sin reabrir | ceo, bib |  |
| P12 · Gestión de cambios | contractual | A0 | A1 | A2 | Cambios no planificados | pmo | Cambiar alcance o precio es contractual. |
| P13 · Aprendizaje y actualización de la wiki | — | A0 | A1 | A2 | Fichas en borrador con más de 30 días y lecciones que se convierten en regla con prueba | bib | Lo que entra en el conocimiento lo aprueba un socio (D-019). |
| P14 · Gestión de permisos y aislamiento | legal | A0 | A1 | A2 | Pruebas de acceso cruzado en verde | back, sec | Los roles privilegiados los dan los socios. |
| P15 · Observabilidad e incidencias | — | A0 | A3 | A4 | Tiempo de detección y alertas sin acción | ops, calj |  |
| P16 · Gobierno de modelos e instrucciones | — | A0 | A1 | A2 | Regresiones por cambio de modelo o instrucciones | ia | Cambiar de modelo lo aprueban los socios. |
| P17 · Seguridad y continuidad | legal | A0 | A1 | A2 | Hallazgos críticos abiertos y fecha de la última restauración probada | ops, sec | Aceptar un riesgo lo hacen los socios. |
| P18 · Evaluación y mejora | — | A0 | A1 | A3 | Mejoras medidas frente a mejoras hechas | kpi |  |
| P19 · Política de uso y límites | legal | A0 | A0 | A2 | Encargos bloqueados por política con motivo correcto | calj, leg | La política la escriben los socios con el abogado. |
| P20 · Seguridad de entradas e inyección de instrucciones | — | A0 | A3 | A4 | Ataques de prueba que pasan (objetivo 0) | sec |  |
| P21 · Ejecución segura de herramientas | externo | A0 | A1 | A2 | Llamadas no autorizadas denegadas | int |  |
| P22 · Gestión de errores y reintentos | — | A0 | A3 | A4 | Duplicados evitados y reintentos por éxito | back | Solo errores transitorios; una acción externa no se reintenta sin su aprobación (P21). |
| P23 · Evaluación de agentes y modelos | — | A0 | A2 | A2 | Exactitud e invenciones frente al banco de casos | dat, ia | Fijar el umbral lo deciden los socios. |
| P24 · Gestión del ciclo de vida del dato | legal | A0 | A0 | A2 | Peticiones de derechos atendidas en plazo | back, leg |  |
| P25 · Gestión de cambios y versiones | — | A0 | A1 | A2 | Reversiones | ingj | Las subidas nocturnas a main del repositorio de trabajo son otra cosa: decisión de Juan del 26/11. |
| P26 · Continuidad y recuperación | — | A0 | A1 | A3 | Tiempo real de restauración ensayado | ops, sec |  |
| P27 · Gestión de proveedores y dependencias | legal, financiero, contractual | A0 | A0 | A2 | Proveedores sin ficha (objetivo 0) | leg, prov |  |
| P28 · Gestión de incidentes | externo, legal | A0 | A0 | A2 | Tiempo de contención | ops, sec, leg | Notificar a la AEPD o al cliente es externo y legal. |
| P29 · Gestión de costes y capacidad | financiero | A0 | A1 | A2 | Coste por caso frente al presupuesto | cfo |  |
| P30 · Gestión de identidades y secretos | legal | A0 | A1 | A2 | Secretos sin rotar | int, sec |  |
| P31 · Calificación de oportunidad | contractual | A0 | A0 | A2 | Oportunidades que pasan G0 | comj, pros, prop, cfo | Seguir o no con una oportunidad lo deciden los socios. |
| P32 · Descubrimiento de procesos | externo | A0 | A0 | A2 | Variantes y excepciones descubiertas que el cliente confirma en G1 | comj, proj, kpi, seg | Se trabaja con personas del cliente. |
| P33 · Diseño y validación TO-BE | externo, contractual | A0 | A0 | A2 | Cambios tras la aprobación del diseño (G2) | proj, seg |  |
| P34 · Gestión de definiciones de proceso | — | A0 | A1 | A2 | Definiciones con pruebas | proj, ingj | Publicar una definición la aprueban los socios. |
| P35 · Gestión de instancias y excepciones | — | A0 | A3 | A4 | Excepciones por instancia resueltas en plazo | back |  |
| P36 · Gestión del catálogo de conectores | externo | A0 | A0 | A2 | Conectores degradados | int |  |
| P37 · Medición de rendimiento y valor | financiero, contractual | A0 | A1 | A2 | Métricas con ficha completa y línea base medida | kpi, exito | El pago 50/50 del piloto depende de la métrica: es financiero. |
| P38 · Gestión de despliegue por cliente | externo, contractual | A0 | A0 | A2 | Puertas pasadas a la primera | pmo, prop, exito |  |
| REF-SIN · Apertura de siniestros en corredurías (proceso de cliente de referencia, D-011) | externo, legal | A0 | A1 | A2 | Acierto por campo de la extracción frente a los «hechos» de los 20 casos y acciones correctas por caso | proj, dat, seg | Comunicar el siniestro a la aseguradora es externo y los plazos son legales (LCS art. 16). |

## Cómo se mantiene

- Se edita `processes/autonomia.json` y se regenera con `python3 tools/autonomia_gen.py`.
- `tests/test_autonomia.py` falla si falta un proceso, si un nivel no existe, si hoy o febrero superan el techo, si algo externo, legal, financiero o contractual pasa de A2, si P10 pasa de A1, si falta la métrica o el criterio de bajada, o si este documento no está al día.
