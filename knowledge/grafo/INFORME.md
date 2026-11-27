<!-- Generado por tools/brain_build.py (tools/grafo.py). No editar a mano. -->
# Informe del grafo de conocimiento

Cómo está conectado el cerebro de Varios: qué sostiene todo, qué temas forman grupos, qué conecta temas distintos, qué falta y qué preguntas conviene hacerse. Se regenera con el cerebro (D-018); no forma parte del grafo.

## Resumen

- 5096 nodos: seccion 4373, documento 383, fuente 122, habilidad 65, proceso 38, especialista 34, agente 34, decision 28, puerta 12, departamento 7.
- 7201 relaciones: 63 % EXTRACTADAS (escritas en la fuente), 37 % INFERIDAS (temas compartidos, con puntuación) y 39 AMBIGUAS (para revisar).
- 14 comunidades de temas.

## Nodos centrales

Lo que más cosas conecta. Si cambia, cambia mucho.

1. **Registro de fuentes** (`knowledge/fuentes/registro.md`) · 216 conexiones
2. **Registro de decisiones** (`DECISIONS.md`) · 123 conexiones
3. **Índice del conocimiento de Varios** (`knowledge/INDEX.md`) · 119 conexiones
4. **Guia de Arranque Proyecto v1.4 Diseno Cerrado** (`docs/fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md`) · 85 conexiones
5. **Catálogo de procesos P01–P38** (`processes/catalog/README.md`) · 83 conexiones
6. **L2 (puerta técnica)** · 69 conexiones
7. **Habilidades de los agentes** (`claude/habilidades/README.md`) · 69 conexiones
8. **Varios · empresa-ia** (`CLAUDE.md`) · 66 conexiones
9. **P22 · Gestión de errores y reintentos** · 64 conexiones
10. **P28 · Gestión de incidentes** · 63 conexiones
11. **Auditoría de agentes y habilidades frente a los procesos (M-040)** (`docs/28-auditoria-agentes.md`) · 63 conexiones
12. **CEO digital** (`knowledge/direccion/ceo-digital.md`) · 60 conexiones

## Puentes entre temas

Nodos por los que pasa el camino entre comunidades distintas (intermediación).

- **Registro de fuentes** · intermediación 0.138 · une la comunidad 2 con 0, 3, 4, 5, 6, 7
- **Registro de decisiones** · intermediación 0.049 · une la comunidad 3 con 0, 2, 4, 5, 7, 8
- **Habilidades de los agentes** · intermediación 0.042 · une la comunidad 0 con 4, 5, 7, 9, 10, 12
- **L2 (puerta técnica)** · intermediación 0.026 · une la comunidad 11 con 0, 2, 3, 4, 5, 6
- **Índice del conocimiento de Varios** · intermediación 0.022 · une la comunidad 7 con 0, 2, 3, 4, 5, 6
- **Guia de Arranque Proyecto v1.4 Diseno Cerrado** · intermediación 0.017 · une la comunidad 8 con 0, 3, 4, 6, 9, 13
- **Estudios** · intermediación 0.017 · une la comunidad 13 con 0, 2, 3, 4, 5, 6
- **D-011 · Construir primero, clientes desde el 15/02/2027** · intermediación 0.011 · une la comunidad 5 con 0, 2, 3, 4, 7, 11
- **CEO digital** · intermediación 0.01 · une la comunidad 9 con 0, 2, 3, 4, 6, 7
- **Administración** · intermediación 0.01 · une la comunidad 0 con 1, 2, 7, 10, 11, 12

## Conexiones sorprendentes

Secciones de carpetas y comunidades distintas que tratan lo mismo y no se enlazan. Relación INFERIDA: compruébala.

- `DECISIONS.md` › D-005 — Aislamiento multi-cliente  ↔  `docs/06-seguridad-y-gobierno.md` › Multi-tenancy  [INFERIDA 0.85]
- `knowledge/plantillas/entregables/02-informe-diagnostico.md` › 3.5 Riesgo  ↔  `processes/templates/proceso-cliente.md` › 4. Riesgo  [INFERIDA 0.85]
- `docs/26-web-clientes.md` › 4. Requisitos legales de la web  ↔  `knowledge/fuentes/registro.md` › LSSI-34-2002  [INFERIDA 0.85]
- `docs/28-auditoria-agentes.md` › Criterio  ↔  `knowledge/fuentes/registro.md` › ANTHROPIC-AGENTES  [INFERIDA 0.85]
- `docs/29-autonomia.md` › Niveles  ↔  `knowledge/fuentes/registro.md` › KNIGHT-NIVELES-AUTONOMIA  [INFERIDA 0.85]
- `governance/legal/borradores/01-contrato-marco-servicios.md` › Anexo 1 · Modelo de pedido (resumen)  ↔  `knowledge/plantillas/entregables/01-propuesta-diagnostico.md` › 7. Condiciones, fuentes y anexos  [INFERIDA 0.75]
- `governance/legal/borradores/03-acuerdo-confidencialidad.md` › Acuerdo de confidencialidad (mutuo) · BORRADOR PARA ABOGADO  ↔  `knowledge/plantillas/entregables/01-propuesta-diagnostico.md` › 6. Siguientes pasos  [INFERIDA 0.75]
- `governance/legal/borradores/04-anexo-uso-ia.md` › 1. Qué sistema es y para qué se usa  ↔  `knowledge/agentes/proj.md` › Reglas del puesto  [INFERIDA 0.75]
- `governance/legal/borradores/05-matriz-aprobaciones.md` › 4. Reglas de la aprobación  ↔  `knowledge/fuentes/registro.md` › ZAPIER-HITL  [INFERIDA 0.75]
- `governance/socios/01-marca-esclusa-o-varios.md` › Búsqueda de anterioridades (sin hacer)  ↔  `knowledge/fuentes/registro.md` › OEPM-LOCALIZADOR  [INFERIDA 0.75]

## Comunidades

### 0 · claude/habilidades · Habilidades de los agentes y Administración

Cohesión 0.08 · 109 nodos: Habilidades de los agentes; Administración; Experto en asesorías y despachos; Experto en asesorías, gestorías y despachos; Especialista en contabilidad y facturación; Backend; Director financiero (CFO); Agentes de la oficina (y 101 más)

### 1 · Habilidades · Legal y privacidad y Arquitecto de procesos

Cohesión 0.05 · 101 nodos: Legal y privacidad; Arquitecto de procesos; Seguridad; Coordinación sectorial · Seguros; Director financiero; Jefe comercial; Separar hecho, hipótesis y propuesta; Arquitecto técnico (y 93 más)

### 2 · knowledge/sectores · Registro de fuentes y Coordinación sectorial y seguros

Cohesión 0.07 · 95 nodos: Registro de fuentes; Coordinación sectorial y seguros; Experto en sanidad privada; Responsable de cumplimiento normativo; Experto en servicios financieros no bancarios; Especialista legal y privacidad; Experto en logística y transporte; Catálogo de excepciones al abrir un siniestro (y 87 más)

### 3 · docs · Registro de decisiones y Trabajo nocturno de Claude

Cohesión 0.08 · 93 nodos: Registro de decisiones; Trabajo nocturno de Claude; Varios · empresa-ia; Atlas Evolucion v1.1 Modelo Operativo Procesos y Despliegue; Plan maestro: la empresa completa, sin que se escape nada; Informe de la mañana · 26/11/2026; 17 · Cerebro, conocimiento y procesos: auditoría e informe; Plan de construcción · 18/11/2026 → 12/02/2027 (y 85 más)

### 4 · processes/runbooks · Auditoría de agentes y habilidades frente a los procesos (M-040) y Dependencias entre procesos

Cohesión 0.18 · 67 nodos: Auditoría de agentes y habilidades frente a los procesos (M-040); Dependencias entre procesos; Mapa de autonomía por proceso, A0–A4 (M-045); Procesos y estados; P32 · Descubrimiento de procesos; P02 · Clasificación y triaje; P33 · Diseño y validación TO-BE; P10 · Aprobación humana (y 59 más)

### 5 · precedents/oficina · Propuesta de proceso de referencia: siniestros en corredurías y Conversaciones con Coordinación sectorial · Seguros

Cohesión 0.15 · 59 nodos: Propuesta de proceso de referencia: siniestros en corredurías; Conversaciones con Coordinación sectorial · Seguros; Guion de validación semanal: apertura de siniestros; Conversaciones con Arquitecto de procesos; Memoria de la oficina; D-011 · Construir primero, clientes desde el 15/02/2027; CCS · Consorcio de Compensación de Seguros: riesgos extraordinarios; Línea base y fichas de métricas · Atalaya (y 51 más)

### 6 · processes/catalog · P22 · Gestión de errores y reintentos y Catálogo de procesos P01–P38

Cohesión 0.41 · 45 nodos: P22 · Gestión de errores y reintentos; Catálogo de procesos P01–P38; P28 · Gestión de incidentes; P22 · Gestión de errores y reintentos; P27 · Gestión de proveedores y dependencias; P33 · Diseño y validación TO-BE; P05 · Diseño del plan; P13 · Aprendizaje y actualización de la wiki (y 37 más)

### 7 · knowledge/comercial · Índice del conocimiento de Varios y Arquitecto de procesos

Cohesión 0.14 · 39 nodos: Índice del conocimiento de Varios; Arquitecto de procesos; P38 · Gestión de despliegue por cliente; P31 · Calificación de oportunidad; Director comercial; Especialista en éxito de cliente; INT-ATLAS · Atlas Evolución v1.1 · modelo operativo, procesos y despliegue; Responsable de implantación de clientes (y 31 más)

### 8 · docs/atlas · Guia de Arranque Proyecto v1.4 Diseno Cerrado y Flujo ceo

Cohesión 0.31 · 35 nodos: Guia de Arranque Proyecto v1.4 Diseno Cerrado; Flujo ceo; Ejecucion agentes; Motor conocimiento obsidian; Marco Integral Legal Ciberseguridad IA Espana UE 2026-11-16; 12 · Ciclo de vida de un proyecto con cliente; Calidad gobierno; Comunicaciones estados (y 27 más)

### 9 · knowledge/ingenieria · CEO digital y Especialista en ciberseguridad

Cohesión 0.15 · 35 nodos: CEO digital; Especialista en ciberseguridad; Arquitecto de datos e IA; Responsable de decisiones y seguimiento; Bibliotecario / responsable de conocimiento; Biblioteca de precedentes; Especialista en automatización; Arquitecto técnico (y 27 más)

### 10 · claude/habilidades · Ingeniero de plataforma y operaciones (DevOps/SRE) y Plataforma y operaciones

Cohesión 0.19 · 15 nodos: Ingeniero de plataforma y operaciones (DevOps/SRE); Plataforma y operaciones; Ingeniero de plataforma y operaciones (DevOps/SRE); ENS-RD311 · Real Decreto 311/2022, Esquema Nacional de Seguridad; ISO-27001 · ISO/IEC 27001:2022 (transición desde 2013 terminada el 31/10/2025); OTEL-GENAI · OpenTelemetry: convenciones semánticas para IA generativa; Copias y restauración probada; Observabilidad y alertas (y 7 más)

### 11 · precedents/oficina · Acta de protección de la IA y examen de 50 casos y Conversaciones con IA y evaluación

Cohesión 0.55 · 11 nodos: Acta de protección de la IA y examen de 50 casos; L2 (puerta técnica); Conversaciones con IA y evaluación; Reunión: IA y evaluación y Seguridad; Conversaciones con CEO digital; Conversaciones con Plan y seguimiento; Conversaciones con Registro de decisiones; Conversaciones con Bibliotecario (y 3 más)

### 12 · claude/habilidades · Diseñador de producto y experiencia (UX) y Diseño y experiencia

Cohesión 0.33 · 9 nodos: Diseñador de producto y experiencia (UX); Diseño y experiencia; LEY-ACCESIBILIDAD-11-2023 · Ley 11/2023 (accesibilidad de productos y servicios, transpone la Directiva (UE) 2019/882); Diseñador de producto y experiencia (UX); Flujo y pantallas de una tarea; NNG-HEURISTICAS · 10 heurísticas de usabilidad (Jakob Nielsen); W3C-WCAG22 · Web Content Accessibility Guidelines (WCAG) 2.2; Prueba de usabilidad (y 1 más)

### 13 · knowledge/estudios · Estudios y Integraciones

Cohesión 0.43 · 8 nodos: Estudios; Integraciones; Motor de conocimiento; Contratos de datos; Estudio de prospectos: automatización para pymes (Álvaro, noviembre de 2026); Pruebas de integración; Conectores; Conocimiento

## Huecos

- **Documentos sin ninguna relación** (2): `precedents/projects/2026-11-oficina-de-agentes.md`; `precedents/solutions/busqueda-texto-cerebro.md`
- **Decisiones que no cita ninguna sección** (2): D-008, D-016
- **Procesos sin especialista responsable** (0): ninguno
- **Fuentes registradas que nadie cita** (0): ninguna
- **Referencias rotas** (se citan pero no existen): ninguna
- **Enlaces ambiguos** (un nombre de archivo con varios destinos): 20
  - `knowledge/estudios/README.md` → `README.md`
  - `knowledge/estudios/README.md` → `claude/habilidades/README.md`
  - `knowledge/estudios/README.md` → `docs/atlas/README.md`
  - `knowledge/estudios/README.md` → `docs/informes/README.md`
  - `knowledge/estudios/README.md` → `governance/README.md`
  - `knowledge/estudios/README.md` → `governance/legal/borradores/README.md`
  - `knowledge/estudios/README.md` → `governance/socios/README.md`
  - `knowledge/estudios/README.md` → `integrations/README.md`
  - `knowledge/estudios/README.md` → `integrations/catalog/README.md`
  - `knowledge/estudios/README.md` → `integrations/connectors/README.md`

## Preguntas sugeridas

_Preguntas que este grafo ayuda a responder o que conviene decidir:_

- **¿Por qué «Registro de fuentes» conecta la comunidad 2 con las comunidades 0, 3, 4, 5?**
  _Intermediación alta (0.138): es un puente entre temas._
- **¿Por qué «Registro de decisiones» conecta la comunidad 3 con las comunidades 0, 2, 4, 5?**
  _Intermediación alta (0.049): es un puente entre temas._
- **¿Por qué «Habilidades de los agentes» conecta la comunidad 0 con las comunidades 4, 5, 7, 9?**
  _Intermediación alta (0.042): es un puente entre temas._
- **¿Se aprueba D-019 · Calidad exigente, todo pasa por un socio y cada rechazo se rehace aprendiendo? Sigue en propuesta y la citan 16 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-013 · Conocimiento y catálogo de procesos generados desde datos? Sigue en propuesta y la citan 12 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-017 · La oficina se vuelca cada noche a GitHub y las automatizaciones van por GitHub Actions? Sigue en propuesta y la citan 11 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Deberían enlazarse «DECISIONS.md» y «docs/06-seguridad-y-gobierno.md»?**
  _Tratan lo mismo (relación INFERIDA 0.85) pero no se citan._
- **¿Deberían enlazarse «knowledge/plantillas/entregables/02-informe-diagnostico.md» y «processes/templates/proceso-cliente.md»?**
  _Tratan lo mismo (relación INFERIDA 0.85) pero no se citan._
- **¿Siguen vigentes D-008, D-016? Ningún documento las cita.**
  _Decisiones que nadie menciona._

## Cómo usarlo

- En la oficina, cada agente recibe las secciones que encajan con su encargo **y lo conectado a ellas** (decisiones, procesos, fuentes y secciones relacionadas), con la etiqueta de confianza de cada relación.
- En local: `python3 tools/grafo.py consulta "pregunta"`, `camino "A" "B"` y `explica "X"`.
- Las relaciones INFERIDAS son pistas, no hechos: si una es buena, conviértela en un enlace en el documento y pasará a EXTRACTADA.
