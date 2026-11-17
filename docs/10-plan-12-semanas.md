# Plan de construcción · 18/11/2026 → 12/02/2027

Versión visual con lista maestra marcable: `site/planning.html`. Decisión: D-011.

## Objetivo a 12/02/2027: listo para el primer cliente

- **Producto:** proceso de referencia (apertura de siniestros en corredurías, por confirmar en S0) funcionando de principio a fin con datos inventados; puerta técnica L0 superada con evidencias; lista fechada de lo que falta para L2.
- **Empresa y legal:** acuerdo de socios firmado; forma de facturar resuelta; contrato marco y encargo de tratamiento (DPA) revisados por un profesional.
- **Comercial:** demo grabada y en vivo; propuesta de diagnóstico con precio; web actualizada; lista de 40 contactos.

Desde el 15/02/2027: clientes.

**Riesgo principal:** construir algo que nadie pague. **Protección:** validación ligera, una conversación por semana desde S2 con alguien que haga el proceso, sin vender (unas 10 en total).

**Supuestos:** Juan programa; Álvaro lleva proceso, datos de prueba, legal y comercial. 10–15 h/semana cada uno. Si hay menos horas se recorta lo marcado "si da tiempo", nunca las pruebas. Ningún dato real de nadie en todo el periodo.

## Controles de paso

| Fecha | Control | Sí si | Si no |
|---|---|---|---|
| Vie 18/12/2026 | A · El CEO decide | 20 casos + 5 trampas acaban en la decisión correcta o en una pregunta, guardado; tests de separación en verde | Usar S5–S6 para terminar; recortar "si da tiempo" de enero |
| Vie 15/01/2027 | B · Proceso de punta a punta | 20 siniestros inventados recorren lectura, extracción, reglas, revisión humana, apertura simulada y registro | Reducir panel y métricas de S10 a lo mínimo; proteger S9 |
| Vie 12/02/2027 | C · Listo para el primer cliente | Objetivo cumplido y lista maestra completa | Retrospectiva y replanificar |

## Semana a semana

| Semana | Fechas | Fase (Guía v1.4) | Juan | Álvaro | Hecho cuando | Si da tiempo |
|---|---|---|---|---|---|---|
| S0 Arranque | 18–22 nov | Decisiones §17 | Contratar Claude, pasos 1–5 del cerebro, aceptar el PR, instalar Git, uv, Docker, VS Code | Acuerdo de socios escrito; confirmar proceso de referencia; leer la web juntos | Acuerdo escrito, proceso confirmado, proyecto de Claude creado | — |
| S1 Entorno | 23–29 nov | Fase 1 | FastAPI /health, PostgreSQL en Docker Compose, .env/.gitignore, Ruff, pytest, CI, escáner de secretos, README | Ficha AS-IS del proceso; empezar 20 siniestros inventados; definir qué es un buen resultado | Cualquiera arranca el proyecto con el README y el CI está en verde | Plantilla de PR y rama protegida |
| S2 Datos | 30 nov–6 dic | Fase 2 | Modelo de datos con Alembic (cliente, usuario, solicitud, plan, tarea, documento, aprobación, auditoría, ejecución de modelo, uso de herramienta); auditoría | Terminar los 20 casos con resultado esperado; 1.ª conversación; glosario del sector | Migraciones desde cero y tests en verde; casos en el repo | Datos de ejemplo automáticos |
| S3 Seguridad | 7–13 dic (8 festivo) | Fase 3 | Autenticación, roles, cliente deducido de la identidad, dos clientes señuelo y tests de acceso cruzado, secretos en entorno | Política de uso (P19); matriz de aprobaciones; 2.ª conversación | Acceso cruzado falla siempre por diseño | RLS en PostgreSQL |
| S4 CEO limitado | 14–20 dic | Fases 4–5 | Adaptador de modelos (simulado + Claude API); ficha; clasificación confirmado/inferido/desconocido; 5 decisiones con motivo; límite de coste | Probar con los casos; 5 peticiones trampa; 3.ª conversación | **Control A** | Plan con tareas y dependencias |
| S5 Motor | 21–27 dic (25 festivo) | Fases 8–9 (ligera) | Estados con transiciones permitidas; reintentos con límite; idempotencia; plan → tareas | Gestor: forma jurídica y facturación; pedir presupuesto a abogado | Reinicio sin perder ni duplicar tareas | Plazos y avisos |
| S6 Puerta | 28 dic–3 ene (1 festivo) | Orden 5 (ligera) | Catálogo de capacidades; puerta de herramientas con lista cerrada; tarea humana de aprobación; botón de parada | Descanso; iniciar trámites | Acción no autorizada bloqueada; aprobación pausa y reanuda | Sandbox |
| S7 Conocimiento | 4–10 ene (6 festivo) | Fase 10 | RAW con huella y permisos; ingesta con cuarentena básica; búsqueda de texto con permisos y citas; estados de ficha | 10 fichas de conocimiento con fuente; 4.ª conversación | Búsqueda desde A nunca devuelve nada de B; todo con cita | Duplicados y enlaces rotos |
| S8 Punta a punta | 11–17 ene | Piloto interno | Extracción con IA + esquema; reglas de póliza; desvío de lesiones; revisión humana; apertura simulada vía puerta | Hacer de tramitador; 5.ª conversación con capturas | **Control B** | Fotos además del PDF |
| S9 Calidad | 18–24 ene | Fase 7 | Examen de 50 casos; acierto por campo, omisiones, coste; pruebas de instrucciones escondidas; cada fallo → test | 30 casos nuevos; fijar umbral de acierto; empezar propuesta | Informe de evaluación con cifras reales; seguridad en verde | Comparar dos modelos |
| S10 Panel | 25–31 ene | Fases 11–13 | Panel de revisión y aprobación; métricas de tiempo, % sin corregir, coste, escalados; alertas | Probar el panel como cliente; precio de diagnóstico y piloto; 6.ª conversación | Alguien no técnico aprueba un caso solo | Informe en PDF |
| S11 Puesta a punto | 1–7 feb | Fase 14 | Copias y restauración probada; demo en la nube con datos inventados; runbooks; inventario de IA y proveedores | Revisión del abogado; propuesta con precio; web; 40 contactos | Restauración real hecha y demo en una URL | Simulacro de incidente |
| S12 Cierre | 8–14 feb | Control C | Todas las pruebas; L0 con evidencias; lista fechada para L2; documentación | Demo grabada de 5 min; plan comercial; retrospectiva | **Control C** | — |

## Lista maestra a 12/02/2027

**Empresa:** acuerdo de socios · forma jurídica · forma de facturar · Claude contratado y proyecto conectado.

**Producto:** entorno reproducible con CI y escáner de secretos · modelo de datos con auditoría · autenticación y cliente desde la identidad · tests de separación · CEO con cinco decisiones · motor con estados, reintentos e idempotencia · puerta de herramientas con aprobaciones y parada · conocimiento con permisos y citas · proceso de referencia de punta a punta · examen de 50 casos superado · pruebas de instrucciones escondidas · panel usable por no técnicos · métricas · copias con restauración probada · demo desplegada con datos inventados · L0 cerrada · lista para L2.

**Seguridad y legal:** política de uso y aprobaciones · inventario de IA y proveedores · runbooks · contrato y DPA revisados · ningún dato real usado.

**Comercial:** proceso confirmado con conversaciones · propuesta con precio · demo grabada · web · 40 contactos · plan comercial.

## Rutinas

- **Lunes (20 min):** partir la semana en tareas pequeñas en el repo.
- **Cada tarea:** Claude Code inspecciona y propone, implementa, pasa tests, documenta; entra por pull request.
- **Viernes (45 min):** demo entre los dos, revisar "hecho cuando", actualizar este plan y DECISIONS.md.

Festivos nacionales: 8/12, 25/12, 1/1, 6/1. Revisar autonómicos y locales.
