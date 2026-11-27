# Plan maestro: la empresa completa, sin que se escape nada

Estado: propuesta de Claude (26/11/2026). Es el mapa de todo lo que una consultora como la que queréis construir necesita tener: qué existe hoy, qué falta y en qué orden llega hasta el 28/02/2027. El calendario semanal y el ritual diario están en [22-plan-hasta-febrero.md](22-plan-hasta-febrero.md); este documento es el **qué**. Claude lo revisa cada noche y marca lo que avanza.

Prioridades:
- **P0:** sin esto no hay empresa o hay riesgo serio.
- **P1:** necesario para el primer cliente.
- **P2:** mejora clara, pero puede esperar.

Responsables:
- **Noche:** Claude, trabajo nocturno.
- **Juan** o **Álvaro:** solo lo puede hacer un socio.
- **Abogado** o **gestor:** profesional externo.

---

## 1. Mi diagnóstico, sin suavizar

Lo que está bien: el repositorio está mejor pensado que el de la mayoría de empresas que ya facturan.
- La oferta en cuatro fases tiene precio por fase y pago al resultado en el piloto.
- Las decisiones están registradas.
- Hay 38 procesos con su ficha.
- Hay un marco legal de 16 capítulos.
- Hay un plan semanal con controles de paso.
- Desde esta noche, una base de datos que separa clientes por diseño.

Lo que me preocupa, de más a menos grave:

1. **Tu contrato con Álvarez & Marsal.** Montar una consultora de IA y ciberseguridad para empresas reguladas mientras trabajas en otra del mismo sector puede chocar con:
   - la concurrencia desleal o un pacto de plena dedicación o de no competencia (artículo 21 del Estatuto de los Trabajadores);
   - el deber de confidencialidad;
   - quién es dueño de lo que crees.

   No digo que haya problema; digo que **hay que comprobarlo con un abogado laboralista antes de captar el primer cliente**, y no usar nunca material, contactos ni conocimiento confidencial de A&M ni de sus clientes. Lo mismo vale para Álvaro con su empleo actual, si lo tiene. Es el riesgo que puede tumbar la empresa entera y no depende de la IA. (M-001)
2. **Dos marcas para lo mismo.** «Esclusa» ya tiene:
   - web (esclusa.eu);
   - sistema de diseño;
   - mascota;
   - boletín semanal;
   - comité de especialistas.

   «Varios» es el nombre provisional del repositorio con Álvaro (D-007). Dos marcas dividen el esfuerzo y confunden al cliente. Mi recomendación es una sola. **Corregido el 26/11 por la noche (S1):** no recomiendo Esclusa salvo que Juan la traspase a la sociedad, porque Juan la ha convertido en su web personal, que no debe presentarse como consultora, y está a su nombre. Comparativa y búsqueda de anterioridades en [governance/socios/](../governance/socios/01-marca-esclusa-o-varios.md). Es decisión de los dos socios. (M-002)
3. **Decisiones vencidas el 22/11:** el acuerdo de socios, el plan de Claude y el proceso de referencia. Sin acuerdo de socios no hay empresa que automatizar: reparto, dedicación, propiedad del código y de la marca, y qué pasa si uno se va. (M-003 a M-005)
4. **Agentes antes que procesos.** Hay 34 agentes y 65 habilidades, y ningún proceso funcionando de punta a punta. Un agente que no está unido a un proceso medido es una ficha bonita, no capacidad. La auditoría de la semana 2 decide qué se queda. **Hecha el 26/11 (N2, [docs/28](28-auditoria-agentes.md)):** propone quedarse con 22 agentes y 56 habilidades, cada uno con su proceso y su métrica; falta que la aprobéis (D-026). (M-040)
5. **La oficina vive en el navegador.** El artefacto de la oficina guarda en su propio almacén, así que no es todavía un sistema: no tiene identidad, ni auditoría central, ni copias. Tiene que apoyarse en la API y en la base de datos de esta noche (semanas 2–5). **Desde el 26/11 (N3a y N3b),** servida desde la API guarda los encargos y las aprobaciones en PostgreSQL con auditoría; **desde el 27/11 (N3c)** también posponer, la caducidad de las aprobaciones y las piezas, y se puede decidir desde otra oficina. Como artefacto sigue como antes. Falta la identidad real (M-047) y la memoria. (M-041)
6. **La validación va por detrás de la construcción.** El riesgo principal del plan es construir algo que nadie pague. Las conversaciones semanales con tramitadores son la única defensa, y no las puede hacer Claude. (M-010)
7. **Vuestras horas son el cuello de botella, no las de Claude.** Con 10–15 horas por socio a la semana, y varios proyectos personales en marcha (golf, gimnasio, nutrición, Odontina y otros), lo que no se pueda hacer de noche tiene que caber en esas horas. Lo que no cabe se recorta conscientemente; no se aplaza sin más.
8. **«Sustituir personas» en un sector regulado.** La responsabilidad legal sigue siendo vuestra. Por eso hay niveles de autonomía y aprobación humana en lo externo, legal y financiero (22-plan, «Autonomía con pruebas»), y un seguro de responsabilidad civil profesional antes de firmar con clientes. (M-020)

---

## 1 bis. No reinventar la rueda

Antes de construir cualquier pieza, la tanda que la construye busca cómo la resuelve alguien que ya lo hace bien. Lo cita con su fuente, lo adapta y explica en el registro qué ha copiado y por qué. Las referencias de partida, que se amplían cada noche:

| Pieza | Dónde mirar primero |
|---|---|
| Orquestación de agentes | Los patrones de [Building effective agents de Anthropic](https://www.anthropic.com/engineering/building-effective-agents): flujos de trabajo antes que agentes autónomos, el orquestador que reparte el trabajo y el evaluador que corrige |
| Portal interno | Productos de gestión de trabajo con éxito (Linear, Asana, Notion, Jira): qué ponen en la pantalla de inicio, cómo muestran lo que espera a alguien y cómo navegan con teclado |
| Web para clientes | Consultoras boutique de IA y de procesos que venden a empresas medianas: estructura, pruebas de confianza, llamada a la acción |
| Método de consultoría | Marcos públicos de gestión de proyectos y de calidad (PMI, ISO 9001) y las prácticas de las grandes consultoras que se puedan citar |
| Seguridad y cumplimiento | Marcos ya citados en el marco legal: ENS, ISO/IEC 27001 y 42001, NIST AI RMF, OWASP para LLM |
| Operación del servicio | Prácticas de gestión de servicios (acuerdos de nivel, incidentes, cambios) al estilo ITIL |

Y una regla para todo el trabajo: **si al construir algo nuevo se detecta que algo anterior estaba mal, se arregla en la misma tarea y se dice en el registro y en el informe.**

---

## 2. Mapa de la empresa completa

Cada fila es una capacidad que una consultora seria tiene que tener. «Hoy» describe lo que hay en el repositorio a 27/11/2026 (repasado por la tanda de la 01:00).

### 2.1 Empresa, socios y gobierno

| ID | Capacidad | Hoy | Objetivo 28/02 | P | Quién |
|---|---|---|---|---|---|
| M-001 | Compatibilidad con el empleo actual de cada socio | Sin revisar | Revisada por un laboralista y por escrito | P0 | Juan, Álvaro, abogado |
| M-002 | Una sola marca y nombre (Esclusa o Varios) | Dos marcas. Comparativa y recomendación hechas (S1, [governance/socios](../governance/socios/01-marca-esclusa-o-varios.md)); falta buscar anterioridades | Decidida, con dominio y marca registrada en la OEPM o la EUIPO tras buscar anterioridades | P0 | Los dos; Noche prepara la comparativa |
| M-003 | Acuerdo de socios: roles, horas, reparto, salida, propiedad intelectual y no competencia entre socios | Pendiente desde el 22/11. Lista de 14 puntos con opciones (S1) | Firmado | P0 | Los dos, abogado; Noche hace un borrador de puntos a decidir |
| M-004 | Forma jurídica y alta (SL o autónomos) | Pendiente (08/01). Comparativa y propuesta para el gestor en [docs/27](27-finanzas.md) (D2) | Decidida con el gestor | P0 | Álvaro, gestor; Noche hace la comparativa con fuentes (D2) |
| M-005 | Proceso de referencia confirmado | Por defecto, siniestros en corredurías | Confirmado tras la 2.ª conversación | P0 | Los dos |
| M-006 | Gobierno: reunión semanal, decisiones, riesgos | DECISIONS.md y viernes de 45 minutos | Registro de riesgos vivo y revisión mensual de objetivos | P1 | Noche prepara la plantilla y los socios la usan |
| M-007 | Objetivos medibles por trimestre | No existen | Tres o cuatro objetivos con su métrica para el primer trimestre de 2027 | P1 | Los dos; Noche hace la propuesta |

### 2.2 Comercial y cliente

| ID | Capacidad | Hoy | Objetivo 28/02 | P | Quién |
|---|---|---|---|---|---|
| M-010 | Validación: 10 conversaciones con quien hace el proceso | Guion de preguntas en el proceso de referencia, cuestionario por puertas y guion semanal (B3) | Seis o más hechas y resumidas, AS-IS validado | P0 | Álvaro; Noche prepara guiones y resúmenes (B3) |
| M-011 | Perfil de cliente ideal y nicho | Candidato: corredurías medianas. Segunda línea: el [estudio de Álvaro](../knowledge/estudios/2026-11-26-prospectos-pymes-alvaro/README.md) con 75 pymes de 5 sectores (26/11) | Decidido con criterios y 40 empresas que encajan | P1 | Los dos; Noche investiga fuentes públicas |
| M-012 | Precio de cada fase | Por decidir. Hoja `precio-y-caja.xlsx` con los parámetros vacíos (D2) | Precio de diagnóstico y piloto con su cálculo de coste y margen | P1 | Los dos; Noche hace el modelo (D2) |
| M-013 | Propuesta de diagnóstico | Plantilla (E1) y ejemplo de Atalaya puntuado con la rúbrica (N6); faltan precio y fechas | Plantilla con precio, alcance, exclusiones y condiciones | P1 | Noche (E1), revisión de los socios |
| M-014 | CRM: contactos, oportunidades, seguimiento | No existe | Tabla de oportunidades en la base de datos o en una hoja, unida a la oficina | P1 | Noche |
| M-015 | Web para clientes | `site/` interno, web de Esclusa y maqueta en `web/maqueta/` (F2); inventario de `site/` en [docs/30](30-inventario-web.md) (N5) | Una web pública con oferta, método, sectores, contacto, aviso legal, privacidad y cookies, hecha a partir de referencias de éxito | P1 | Noche (F2); los socios aprueban los textos y la marca (M-002) |
| M-016 | Contenido y presencia: LinkedIn, boletín | Boletín semanal de Esclusa | Calendario de contenidos alineado con el nicho | P2 | Noche hace borradores y Juan publica |
| M-017 | Demo grabada de 5 minutos | No existe | Grabada con datos inventados | P1 | Juan (S12) |
| M-018 | Alta de cliente: contrato, accesos, arranque | No existe | Lista de alta y acta de arranque | P1 | Noche |

### 2.3 Legal y cumplimiento

El marco completo ya existe en [el marco legal](fuentes/Marco_Integral_Legal_Ciberseguridad_IA_Espana_UE_2026-11-16.md). Lo que falta es convertirlo en documentos firmables y en evidencias. Todo lo que redacte Claude es un borrador para abogado.

| ID | Obligación o documento | Hoy | Objetivo 28/02 | P | Quién |
|---|---|---|---|---|---|
| M-020 | Seguro de responsabilidad civil profesional y de ciberriesgos | No existe. Preguntas para el corredor (S1) | Presupuestos comparados y contratado antes del primer piloto | P0 | Álvaro; Noche prepara las preguntas para el corredor |
| M-021 | Contrato marco de servicios y anexo por fase (SOW) | Borrador para abogado con pedido por fase (D1) | Revisado por un abogado | P0 | Noche hace el borrador (D1) y lo revisa el abogado |
| M-022 | Encargo de tratamiento (art. 28 RGPD) y lista de subencargados (proveedores de IA, nube) | Borrador para abogado sobre las cláusulas tipo de la Comisión (D1) | Revisado; lista de subencargados con su ubicación y garantías | P0 | Noche (D1) y abogado |
| M-023 | Acuerdo de confidencialidad | Borrador para abogado (D1) | Plantilla revisada | P1 | Noche (D1) |
| M-024 | Cláusulas para clientes sujetos a DORA (proveedor de servicios TIC a entidades financieras) | Anexo DORA opcional en el borrador del contrato marco (D1) | Anexo DORA por si el cliente es aseguradora o entidad financiera | P1 | Noche |
| M-025 | Reglamento de IA: nuestro papel por proyecto (proveedor o implantador), obligaciones de transparencia y alfabetización del art. 4 | Marco legal, cap. 3 | Ficha de clasificación por caso de uso dentro del diagnóstico y curso de alfabetización como producto | P1 | Noche |
| M-026 | Protección de datos propia: registro de actividades, información a contactos, ejercicio de derechos | Marco legal, cap. 2 | Registro de tratamientos de la empresa y textos de la web | P1 | Noche hace el borrador y revisa el abogado |
| M-027 | Evaluación de impacto (EIPD) por proyecto cuando toque | Marco legal, cap. 2.6 | Plantilla y criterio de cuándo hace falta | P1 | Noche |
| M-028 | Web: aviso legal, privacidad, cookies (LSSI-CE) | Esclusa tiene páginas legales | Revisadas para la marca elegida | P1 | Noche |
| M-029 | Propiedad intelectual: qué es del cliente y qué nuestro (método, código reutilizable) | Cláusula en el borrador del contrato marco, pendiente del abogado (D1) | Cláusula en el contrato marco | P0 | Noche (D1) y abogado |
| M-030 | Matriz de cumplimiento: obligación → evidencia → responsable → estado | Capítulo 11 del marco legal | Viva en el repositorio y revisada cada mes | P1 | Noche |
| M-031 | Facturación electrónica y Verifactu | Requisitos en [docs/27](27-finanzas.md) (D2); el RDL 43/2026 aplaza Verifactu, pendiente de convalidación | Requisitos y fechas verificadas, y herramienta elegida | P1 | Noche (D2) y gestor |

### 2.4 Método de entrega y entregables

| ID | Capacidad | Hoy | Objetivo 28/02 | P | Quién |
|---|---|---|---|---|---|
| M-035 | Catálogo de entregables por fase con plantilla, rúbrica y ejemplo (sección 3) | Seis plantillas (E1) y rúbrica con listas por tipo (C3); ejemplo de la propuesta (N6) | Los 20 entregables de la sección 3 con plantilla y rúbrica | P1 | Noche (E1, C3) |
| M-036 | Puertas G0–G6 con su lista de comprobación | Definidas en la Guía v1.4 | Una lista por puerta, usada en la oficina | P1 | Noche |
| M-037 | Marca aplicada a todos los entregables | Generador de entregables en la oficina (D-015) | Misma plantilla en Word, PowerPoint, Excel y PDF | P1 | Noche |
| M-038 | Revisión de calidad antes de entregar | Rúbrica en código (C3), usada en el ejemplo de Atalaya (N6); falta llevarla a la oficina | Rúbrica automática previa a la revisión del socio | P1 | Noche |

### 2.5 Oficina interna (la máquina)

| ID | Capacidad | Hoy | Objetivo 28/02 | P | Quién |
|---|---|---|---|---|---|
| M-040 | Auditoría de agentes y procesos: qué sobra, qué falta ([docs/28](28-auditoria-agentes.md), D-026 propuesta) | Auditoría hecha (N2, D-026 propuesta): 22 agentes se quedan, 5 se fusionan y 7 se retiran | Cada agente unido a procesos, con métrica y nivel de autonomía; los que no lo estén, fusionados o retirados | P0 | Noche (semana 2) |
| M-041 | La oficina sobre la API y la base de datos (API de encargos, tareas y aprobaciones en N3a, adaptador de la oficina en N3b, 26/11; posponer, caducar, piezas como tareas y decidir desde otra oficina en N3c, 27/11, D-031, [docs/24](24-base-de-datos.md); falta la memoria) | Encargos, aprobaciones, aplazamientos, caducidad y piezas de la oficina en PostgreSQL con auditoría cuando se sirve desde la API; reglas, memoria, proyectos y entregables siguen en el navegador | Encargos, tareas, aprobaciones y memoria en PostgreSQL con auditoría | P1 | Noche (semanas 2–5) |
| M-042 | Chat con el CEO: clasificar, preguntar, planificar y repartir | CEO limitado con reglas fijas y banco de 25 encargos con modelo simulado (C2) | CEO limitado de S4 con las cinco decisiones y el banco de 25 encargos | P1 | Noche (semana 4) |
| M-043 | Agentes que colaboran: plan → tareas → agentes → calidad → aprobación | Modo «En equipo» | Sobre el motor persistente, con dependencias y reintentos | P1 | Noche (semana 5) |
| M-044 | Bucle de mejora diaria: histórico → lecciones → reglas → pruebas | Memoria y lecciones (D-019) | Cada regla nueva entra con su prueba; puntuación del examen por semana | P1 | Noche (semanas 4 y 9) |
| M-049 | Evolución de instrucciones contra examen, al estilo de GEPA (D-030, propuesta) | Nada: falta el examen (Control A, semana 4) | Instrucciones versionadas con nota (semana 4); primera ronda con casos reservados sobre el CEO y la apertura de siniestros (semana 9); ronda semanal desde febrero, siempre aprobada por un socio | P1 | Noche (semanas 4, 9 y 13) |
| M-045 | Mapa de autonomía por proceso (A0–A4) ([docs/29](29-autonomia.md), D-027 propuesta) | Mapa hecho (N1, D-027 propuesta): los 39 procesos en A0 | Nivel de cada proceso y criterio para subirlo | P1 | Noche (semana 2) |
| M-046 | Coste de IA por encargo y por cliente, con límite | Tabla `ejecucion_modelo` creada | Panel de coste y alerta | P2 | Noche |
| M-047 | Entrada de los socios con identidad real (no contraseñas en el artefacto) | No existe | Autenticación de S3 | P1 | Noche |
| M-048 | Portal interno claro y bien distribuido | Oficina 3D con panel de encargos | La pantalla de inicio responde en 10 segundos a qué espera mi OK, qué está en marcha, qué se ha entregado y qué viene. Secciones para encargos, proyectos, clientes, cerebro, calendario y agentes, con la vista 3D como una vista más | P1 | Noche (F1) |

### 2.6 Producto (proceso de referencia)

El plan de 12 semanas manda: [10-plan-12-semanas.md](10-plan-12-semanas.md). Lo hecho esta noche:
- **A1–A4:** base de datos, aislamiento y datos de ejemplo ([24-base-de-datos.md](24-base-de-datos.md)).

Lo siguiente:
- autenticación (S3);
- CEO limitado (S4);
- motor persistente (S5);
- puerta de herramientas (S6);
- conocimiento con permisos (S7);
- punta a punta (S8);
- examen (S9);
- panel (S10).

### 2.7 Conocimiento (el cerebro)

| ID | Capacidad | Hoy | Objetivo 28/02 | P | Quién |
|---|---|---|---|---|---|
| M-050 | Paquete de seguros y corredurías con normas verificadas | Paquete `knowledge/sectores/seguros/` (B2); 37 de 39 fichas con fuente externa (K1) | Paquete completo con fuente oficial (B2) | P0 | Noche |
| M-051 | Fichas de `knowledge/` cargadas en la base de datos con citas | Carga manual con `varios.db.carga_conocimiento` (B1) | Carga automática en cada cambio (B1) | P1 | Noche |
| M-052 | Ficha de cliente y memoria por cliente | Esquema, plantilla y cuestionario (B3); falta la memoria por cliente | Esquema, plantilla y cuestionario (B3) | P1 | Noche |
| M-053 | Vigilancia normativa: cambios en normas que afectan a clientes | Boletín de Esclusa | Revisión semanal unida a las fichas, que marca lo que caduca | P2 | Noche |
| M-054 | Precedentes: cada proyecto deja lecciones y plantillas reutilizables | `precedents/` | Plantilla de cierre de proyecto | P2 | Noche |

### 2.8 Finanzas y administración

| ID | Capacidad | Hoy | Objetivo 28/02 | P | Quién |
|---|---|---|---|---|---|
| M-060 | Cuenta bancaria de empresa y separación de gastos | Desconocido | Abierta tras elegir la forma jurídica | P0 | Socios |
| M-061 | Facturación y cobros | No existe | Herramienta conforme con Verifactu, numeración y plantilla | P1 | Gestor; Noche compara opciones |
| M-062 | Presupuesto de gastos fijos: IA, nube, dominios, seguros, asesoría | Hoja `precio-y-caja.xlsx` con parámetros vacíos (D2) | Hoja con parámetros (sin cifras inventadas) | P1 | Noche (D2) |
| M-063 | Previsión de caja por escenarios | Caja a 18 meses en tres escenarios, con parámetros vacíos (D2) | Tres escenarios con supuestos explícitos | P1 | Noche (D2) |
| M-064 | Ayudas públicas y financiación (ENISA, CDTI, ayudas autonómicas) | Sin estudiar | Lista verificada de lo que aplica y sus plazos | P2 | Noche |

### 2.9 Tecnología y seguridad interna

| ID | Capacidad | Hoy | Objetivo 28/02 | P | Quién |
|---|---|---|---|---|---|
| M-070 | Cuentas de empresa: correo con dominio, GitHub de la organización, Claude | Cuentas personales | Organización de GitHub, correo de empresa, segundo factor en todo | P0 | Juan |
| M-071 | Gestor de contraseñas compartido y política de secretos | Secretos fuera del repositorio | Gestor elegido y en uso | P0 | Juan |
| M-072 | Copias con restauración probada | Plan S11 | Restauración real hecha | P1 | Noche y Juan |
| M-073 | Inventario de proveedores e IA (P27) | Fuentes y fichas de proveedor | Inventario con contrato, datos que tratan y región | P1 | Noche |
| M-074 | Rama main protegida y CI obligatoria | CI sin protección | main protegida; lo nocturno entra por PR automático si los socios lo prefieren | P2 | Juan |

---

## 3. Catálogo de entregables al cliente

Cada uno necesita plantilla, rúbrica, ejemplo con datos inventados y su lugar en la oficina. Hoy no hay ninguno completo.

| Fase | Entregable | Para qué | Puerta |
|---|---|---|---|
| Venta | Propuesta de diagnóstico | Alcance, precio, condiciones | G0 |
| Venta | Contrato marco + anexo de fase + encargo de tratamiento | Base legal del trabajo | G0 |
| Diagnosticar | Acta de arranque y plan de trabajo | Quién, qué, cuándo | G1 |
| Diagnosticar | Cuestionario y guion de entrevistas | Descubrir el proceso | G1 |
| Diagnosticar | Mapa AS-IS con volúmenes y tiempos | Línea base medible | G1 |
| Diagnosticar | Casos de uso puntuados y clasificación de riesgo (IA, datos) | Qué merece la pena | G2 |
| Diagnosticar | Informe de diagnóstico con caso de negocio y hoja de ruta a 12 meses | Decisión de seguir | G2 |
| Diseñar | Diseño TO-BE: qué hace la regla, la IA o la persona | El proceso nuevo | G2 |
| Diseñar | Evaluación de riesgos y, si toca, EIPD y clasificación según el Reglamento de IA | Cumplir | G2 |
| Diseñar | Métrica de éxito firmada y plan de piloto | Pago 50/50 | G2 |
| Construir | Especificación y plan de pruebas | Qué se construye y cómo se comprueba | G3 |
| Construir | Informe de evaluación con cifras reales | Acierto, coste, errores | G4 |
| Construir | Manual de uso y formación (art. 4) | Adopción | G5 |
| Construir | Acta de aceptación del piloto | Cobrar la segunda mitad | G5 |
| Operar | Acuerdo de nivel de servicio | Qué garantizamos | G6 |
| Operar | Informe mensual de operación | Valor y salud | G6 |
| Operar | Revisión trimestral | Escalar, ajustar o parar | G6 |
| Operar | Informe de incidente | Transparencia | — |
| Transversal | Actas de reunión y registro de decisiones | Trazabilidad | — |
| Transversal | Cierre de proyecto y lecciones | Aprender | — |

---

## 4. Herramientas: mi opinión

Regla: cada herramienta necesita una decisión que diga qué problema resuelve, cómo se mide y qué pasa si se quita. Lo que pongo aquí es opinión. Los datos (licencia, precio, región de datos) los verifican las tandas con fuente antes de decidir.

| Herramienta | Mi opinión | Por qué |
|---|---|---|
| **n8n / Activepieces** | **Todavía no.** Revisar en la semana 5 | Hoy no hay ninguna automatización que Python y GitHub Actions no cubran. Añade un servicio que mantener y asegurar. Además, la licencia de n8n restringe ciertos usos comerciales: hay que leerla antes de ofrecerla a clientes. Tendrá sentido cuando un cliente necesite automatizaciones que su equipo pueda tocar sin programar |
| **Conectores de Claude que ya tienes** (Gmail, Calendar, Drive, Figma, Cloudflare) | **Sí, ya** | Están conectados. La oficina puede preparar borradores de correo, citas y documentos sin herramientas nuevas, siempre con aprobación antes de enviar |
| **GitHub Projects** | **Sí, semana 2** | Es gratuito con el repositorio y convierte este plan en un tablero con fechas sin otra herramienta |
| **Obsidian** | **Sí, ya está** (D-021) | No ampliar. Es la ventana para leer el cerebro, no el cerebro |
| **Langfuse o similar** (trazas y coste de IA) | **Semana 4, si hace falta** | La tabla `ejecucion_modelo` ya guarda coste y resultado. Primero medir con lo que hay |
| **promptfoo** (evaluaciones) | **Semana 9, a valorar** | Un banco de pruebas en pytest puede bastar. Solo si se queda corto |
| **pgvector** | **Semana 7, solo si la búsqueda de texto falla** | Mismo PostgreSQL, sin servicio nuevo. Primero hay que medir si hace falta |
| **CRM externo** (HubSpot y similares) | **No** | Con 40 contactos, una tabla en la base de datos o una hoja basta. Un CRM es otra fuente de verdad |
| **Más agentes o más modelos** | **No, hasta la auditoría** | El cuello de botella es la validación, no la capacidad |

---

## 5. Cómo debería quedar la oficina (diseño objetivo)

1. **Entrada única.** Un chat donde un socio escribe un encargo o reenvía un correo.
2. **CEO limitado.** Clasifica el encargo (intención, riesgo, incertidumbre) y elige una de cinco decisiones con su motivo: continuar, preguntar, escalar, rechazar o derivar. Antes de planificar, consulta el histórico parecido.
3. **Plan con tareas, responsables y criterio de aceptación.** Cada tarea va a una capacidad, y cada capacidad está unida a un proceso del catálogo.
4. **Ejecución con herramientas de lista cerrada.** Lo externo, legal o financiero se pausa y espera la aprobación de un socio.
5. **Control de calidad automático con la rúbrica del entregable.** Si falla, se rehace aprendiendo (D-019).
6. **Entrega y registro.** Auditoría, coste, lecciones y precedente.
7. **Cada noche:** las lecciones repetidas se proponen como reglas. Cada regla entra con su prueba, y el informe de la mañana dice si el examen mejora.

---

## 6. Lo que necesito de vosotros (por orden)

1. **M-001 · Compatibilidad con vuestros empleos.** Esta semana, con un laboralista.
2. **M-002 · Una sola marca.** Varios o un nombre nuevo, tras buscar anterioridades; Esclusa solo si Juan la traspasa a la sociedad ([comparativa](../governance/socios/01-marca-esclusa-o-varios.md)). Decidid antes de la web y de la marca registrada.
3. **M-003 · Acuerdo de socios.** Lista de 14 puntos a decidir, con opciones: [governance/socios/](../governance/socios/02-acuerdo-de-socios-puntos.md). La redacción final es del abogado.
   - **M-020 · Seguro de RC profesional y ciberriesgos.** Preguntas para el corredor: [governance/socios/](../governance/socios/03-preguntas-seguro-rc-y-ciber.md).
4. **M-005 · Proceso de referencia confirmado.** Por defecto, siniestros en corredurías.
5. **M-010 · Primera conversación de validación** antes del 06/12.
6. **M-070 / M-071 · Cuentas de empresa, segundo factor y gestor de contraseñas.** Una tarde.
7. **Elegir cada día las tareas de la noche** a partir del informe de la mañana.
