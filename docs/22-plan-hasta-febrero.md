# Plan de trabajo diario · 26/11/2026 → 28/02/2027

Estado: propuesta (D-022). Amplía el plan de 12 semanas ([10-plan-12-semanas.md](10-plan-12-semanas.md)) con el trabajo que Claude hace de noche. No lo sustituye: los controles A, B y C siguen en las mismas fechas.

## A dónde llegamos el 28/02/2027

| Pilar | Listo cuando |
|---|---|
| **1. Producto** | El proceso de referencia (apertura de siniestros en corredurías) funciona de punta a punta con datos inventados y supera el Control C (12/02). |
| **2. Oficina interna** | Los socios escriben un encargo en un chat. El CEO lo clasifica (continuar, preguntar, escalar, rechazar o derivar), lo planifica y lo reparte. Los agentes trabajan entre ellos sobre la base de datos y el cerebro, pasan control de calidad y entregan. Lo que tiene riesgo espera la aprobación de un socio. |
| **3. Cerebro** | Conocimiento de empresa, sectores y procesos en la base de datos, con permisos, fuente citada y estado (borrador, validado, obsoleto). Cada cliente tiene su ficha y su memoria, separadas de las demás. |
| **4. Entregables** | Cada tipo de entregable tiene plantilla, rúbrica de calidad y revisión antes de salir, con la misma marca. |
| **5. Web para clientes** | Web pública con oferta, método, casos (inventados y marcados como tales hasta tener reales), contacto y aviso legal. |
| **6. Empresa** | Acuerdo de socios, forma jurídica y facturación resueltas; contrato marco, encargo de tratamiento y política de uso de IA revisados por un abogado. |

Del 15 al 28 de febrero, primeros clientes (D-011) y pulido con lo que digan.

## Cómo funciona cada día

1. **07:15 · informe.** La última tanda de la noche escribe el informe en `docs/informes/AAAA-MM-DD.md` y lo sube antes de las 07:50.
2. **Por la mañana · Juan lo lee (10 minutos).** Responde las preguntas y hace lo que le toca, que el informe pone en una lista aparte.
3. **Durante el día · Juan elige.** Escribe a Claude «esta noche: tareas X, Y, Z», sacadas del menú de la semana o nuevas.
4. **Claude prepara la noche.** Pone esas tareas en la lista de la noche ([21-trabajo-nocturno.md](21-trabajo-nocturno.md)) y programa **solo las tandas de esa noche**. Nada queda programado para otros días.
5. **De noche · Claude trabaja.** Empieza en la conversación y sigue en tandas. Cada tarea se sube a `main` con las pruebas en verde.

Si un día Juan no elige nada, no se programa nada esa noche.

## Formato del informe de la mañana

Siempre con estos apartados y en este orden, en español claro y sin jerga:

1. **En tres líneas.** Qué se ha conseguido esta noche y qué importa hoy.
2. **Hecho esta noche.** Tabla: tarea · qué se ha hecho · dónde está (enlace) · cómo comprobarlo en un minuto.
3. **Qué ha mejorado.** Antes y después, con datos medibles cuando los haya: pruebas, casos y cobertura.
4. **Lo que tienes que hacer tú hoy.** Acciones que solo puede hacer un socio, como crear una cuenta, aprobar algo, instalar algo o revisar un borrador legal. Cada una con el tiempo que lleva.
5. **Decisiones y preguntas.** Cada una con su recomendación y fecha límite.
6. **Herramientas recomendadas.** Para cada una: qué es, para qué nos sirve, si conviene ahora o más tarde, coste y licencia, y la fuente. Si no conviene, también se dice por qué.
7. **Ideas para mejorar.** Como mucho tres, priorizadas.
8. **Propuesta para la próxima noche.** De tres a seis tareas del menú de la semana, con lo que cuesta cada una, para que Juan elija.
9. **Problemas.** Lo que ha fallado o ha quedado a medias, sin maquillar.

## Calendario semana a semana

Cada semana lleva el tema del plan de 12 semanas más un menú de tareas nocturnas. Juan elige cada día del menú. Los socios hacen lo que dice la columna «Socios», que viene del plan de 12 semanas.

| Semana | Fechas | Tema | Menú de tareas nocturnas | Socios |
|---|---|---|---|---|
| 1 | 26–29 nov | Entorno y base de datos | Lista de la primera noche ([21-trabajo-nocturno.md](21-trabajo-nocturno.md)): base de datos, cerebro, casos, legal, finanzas y plantillas | Cerrar las decisiones vencidas del 22/11; ficha AS-IS del proceso |
| 2 | 30 nov–6 dic | Datos (S2) | Datos de ejemplo; la oficina guarda en la API y no en el navegador; inventario de la web actual y estructura de la web para clientes; glosario del sector | 20 casos revisados por Álvaro; 1.ª conversación de validación |
| 3 | 7–13 dic | Seguridad (S3) | Autenticación y roles; RLS en PostgreSQL; entrada a la oficina para los dos socios; política de uso (P19) y matriz de aprobaciones en borrador | 2.ª conversación |
| 4 | 14–20 dic | CEO limitado (S4) · **Control A** | Adaptador de modelos (simulado + Claude); las cinco decisiones con motivo; banco de 25 encargos; chat de la oficina conectado al CEO real | Probar el CEO con las trampas; 3.ª conversación |
| 5 | 21–27 dic | Motor persistente (S5) | Estados, reintentos e idempotencia en la base de datos; plan → tareas → agentes → calidad → aprobación en la oficina | Gestor: forma jurídica y facturación |
| 6 | 28 dic–3 ene | Puerta de herramientas (S6) | Catálogo de capacidades; lista cerrada de herramientas; aprobación que pausa y reanuda; botón de parada | Descanso |
| 7 | 4–10 ene | Conocimiento (S7) | Ingesta con huella y cuarentena; búsqueda con permisos y citas; el cerebro de la oficina pasa a la base de datos; ficha de cada cliente | 10 fichas con fuente; 4.ª conversación |
| 8 | 11–17 ene | Punta a punta (S8) · **Control B** | Extracción con IA y esquema; reglas de póliza; revisión humana; apertura simulada; plantillas de entregables con generador y marca | Hacer de tramitador; 5.ª conversación |
| 9 | 18–24 ene | Calidad (S9) | Examen de 50 casos; pruebas de instrucciones escondidas; rúbrica y evaluación de los agentes de la oficina | 30 casos nuevos; umbral de acierto |
| 10 | 25–31 ene | Panel (S10) | Panel de revisión y aprobación; métricas de tiempo, coste y correcciones; web para clientes: diseño y textos | Probar el panel como cliente; precio |
| 11 | 1–7 feb | Puesta a punto (S11) | Copias y restauración probada; demo en la nube; runbooks; web publicada; inventario de IA y proveedores | Abogado; propuesta con precio; 40 contactos |
| 12 | 8–14 feb | Cierre (S12) · **Control C** | Todas las pruebas; evidencias de L0; lista para L2; documentación | Demo grabada; plan comercial |
| 13–14 | 15–28 feb | Primeros clientes | Alta de cliente en la oficina; informe mensual de operación; ajustes de lo que digan los clientes; retrospectiva | Ventas y primeras reuniones |

**Si una semana se retrasa:** se recortan las tareas de la oficina y de la web, nunca las pruebas ni la seguridad, igual que en el plan de 12 semanas.

## Herramientas a estudiar

Ninguna entra sin una decisión en `DECISIONS.md`, como manda `CLAUDE.md`. Los informes las investigan con fuente, de una o dos en una, y dicen si conviene ahora, más tarde o nunca.

| Herramienta | Para qué podría servir | Cuándo mirarla |
|---|---|---|
| n8n o Activepieces | Automatizaciones sin código entre correo, calendario y CRM. Hay que revisar la licencia antes de ofrecerla a clientes | Semana 5 |
| GitHub Projects | Tablero de tareas unido a los issues y a este plan | Semana 2 |
| Langfuse u otra herramienta de observabilidad | Trazas, coste y calidad de cada llamada al modelo | Semana 4 |
| promptfoo | Evaluaciones automáticas y pruebas de instrucciones escondidas | Semana 9 |
| pgvector | Búsqueda por significado en PostgreSQL, sin otra base de datos | Semana 7 |
| Obsidian (ya en uso, D-021) | Editar y navegar el cerebro | Revisar en la semana 7 |
| Servidores MCP | Que los agentes lean el correo, el calendario y Drive con permisos | Semana 6 |
| Alojamiento de la demo y región de datos | Decisión pendiente para el 05/02 | Semana 10 |

## Riesgos de este plan

- **Más horas no sustituyen a la validación.** El cerebro sabrá de sectores y normas, pero de cada cliente solo sabrá algo cuando haya clientes y conversaciones.
- **La oficina puede comerse el producto.** Por eso cada semana el tema es el del plan de 12 semanas, y la oficina va en el menú, no delante.
- **Revisión.** Todo lo nocturno entra directo en `main` porque así lo decidió Juan el 26/11/2026. Si algo se rompe, el informe lo dice y se revierte por la mañana.
