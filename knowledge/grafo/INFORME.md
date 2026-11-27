<!-- Generado por tools/brain_build.py (tools/grafo.py). No editar a mano. -->
# Informe del grafo de conocimiento

Cómo está conectado el cerebro de Varios: qué sostiene todo, qué temas forman grupos, qué conecta temas distintos, qué falta y qué preguntas conviene hacerse. Se regenera con el cerebro (D-018); no forma parte del grafo.

## Resumen

- 5102 nodos: seccion 4378, documento 383, fuente 122, habilidad 65, proceso 38, especialista 34, agente 34, decision 29, puerta 12, departamento 7.
- 7252 relaciones: 63 % EXTRACTADAS (escritas en la fuente), 37 % INFERIDAS (temas compartidos, con puntuación) y 39 AMBIGUAS (para revisar).
- 13 comunidades de temas.

## Nodos centrales

Lo que más cosas conecta. Si cambia, cambia mucho.

1. **Registro de fuentes** (`knowledge/fuentes/registro.md`) · 217 conexiones
2. **Registro de decisiones** (`DECISIONS.md`) · 124 conexiones
3. **Índice del conocimiento de Varios** (`knowledge/INDEX.md`) · 120 conexiones
4. **Guia de Arranque Proyecto v1.4 Diseno Cerrado** (`docs/fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md`) · 85 conexiones
5. **Catálogo de procesos P01–P38** (`processes/catalog/README.md`) · 83 conexiones
6. **L2 (puerta técnica)** · 70 conexiones
7. **Habilidades de los agentes** (`claude/habilidades/README.md`) · 69 conexiones
8. **Varios · empresa-ia** (`CLAUDE.md`) · 65 conexiones
9. **Mapa de autonomía por proceso, A0–A4 (M-045)** (`docs/29-autonomia.md`) · 65 conexiones
10. **P22 · Gestión de errores y reintentos** · 64 conexiones
11. **Auditoría de agentes y habilidades frente a los procesos (M-040)** (`docs/28-auditoria-agentes.md`) · 64 conexiones
12. **P28 · Gestión de incidentes** · 63 conexiones

## Puentes entre temas

Nodos por los que pasa el camino entre comunidades distintas (intermediación).

- **Registro de fuentes** · intermediación 0.134 · une la comunidad 3 con 0, 2, 4, 5, 6, 7
- **Registro de decisiones** · intermediación 0.046 · une la comunidad 2 con 0, 3, 4, 5, 7, 8
- **Habilidades de los agentes** · intermediación 0.044 · une la comunidad 0 con 4, 5, 7, 8, 9, 11
- **L2 (puerta técnica)** · intermediación 0.028 · une la comunidad 12 con 0, 2, 3, 4, 5, 6
- **Índice del conocimiento de Varios** · intermediación 0.02 · une la comunidad 7 con 0, 2, 3, 4, 5, 6
- **Estudios** · intermediación 0.018 · une la comunidad 9 con 0, 2, 3, 4, 5, 6
- **Guia de Arranque Proyecto v1.4 Diseno Cerrado** · intermediación 0.016 · une la comunidad 10 con 0, 2, 3, 4, 6, 8
- **Arquitecto de procesos** · intermediación 0.011 · une la comunidad 0 con 1, 2, 3, 5, 7, 8
- **D-011 · Construir primero, clientes desde el 15/02/2027** · intermediación 0.01 · une la comunidad 5 con 0, 2, 3, 4, 7, 9
- **CEO digital** · intermediación 0.01 · une la comunidad 8 con 0, 2, 3, 4, 6, 7

## Conexiones sorprendentes

Secciones de carpetas y comunidades distintas que tratan lo mismo y no se enlazan. Relación INFERIDA: compruébala.

- `knowledge/plantillas/entregables/02-informe-diagnostico.md` › 3.5 Riesgo  ↔  `processes/templates/proceso-cliente.md` › 4. Riesgo  [INFERIDA 0.85]
- `docs/26-web-clientes.md` › 4. Requisitos legales de la web  ↔  `knowledge/fuentes/registro.md` › LSSI-34-2002  [INFERIDA 0.85]
- `docs/28-auditoria-agentes.md` › Criterio  ↔  `knowledge/fuentes/registro.md` › ANTHROPIC-AGENTES  [INFERIDA 0.85]
- `docs/29-autonomia.md` › Niveles  ↔  `knowledge/fuentes/registro.md` › KNIGHT-NIVELES-AUTONOMIA  [INFERIDA 0.85]
- `governance/legal/borradores/01-contrato-marco-servicios.md` › Anexo 1 · Modelo de pedido (resumen)  ↔  `knowledge/plantillas/entregables/01-propuesta-diagnostico.md` › 7. Condiciones, fuentes y anexos  [INFERIDA 0.75]
- `governance/legal/borradores/03-acuerdo-confidencialidad.md` › Acuerdo de confidencialidad (mutuo) · BORRADOR PARA ABOGADO  ↔  `knowledge/plantillas/entregables/01-propuesta-diagnostico.md` › 6. Siguientes pasos  [INFERIDA 0.75]
- `governance/legal/borradores/04-anexo-uso-ia.md` › 1. Qué sistema es y para qué se usa  ↔  `knowledge/agentes/proj.md` › Reglas del puesto  [INFERIDA 0.75]
- `governance/legal/borradores/05-matriz-aprobaciones.md` › 4. Reglas de la aprobación  ↔  `knowledge/fuentes/registro.md` › ZAPIER-HITL  [INFERIDA 0.75]
- `governance/socios/01-marca-esclusa-o-varios.md` › Búsqueda de anterioridades (sin hacer)  ↔  `knowledge/fuentes/registro.md` › OEPM-LOCALIZADOR  [INFERIDA 0.75]
- `governance/socios/02-acuerdo-de-socios-puntos.md` › Conclusión  ↔  `knowledge/fuentes/registro.md` › UC3M-PACTOS  [INFERIDA 0.75]

## Comunidades

### 0 · claude/habilidades · Habilidades de los agentes y Administración

Cohesión 0.08 · 108 nodos: Habilidades de los agentes; Administración; Experto en asesorías y despachos; Especialista en contabilidad y facturación; Backend; Director financiero (CFO); Agentes de la oficina; Arquitecto de procesos (y 100 más)

### 1 · Habilidades · Legal y privacidad y Arquitecto de procesos

Cohesión 0.05 · 102 nodos: Legal y privacidad; Arquitecto de procesos; Seguridad; Coordinación sectorial · Seguros; Director financiero; Jefe comercial; Separar hecho, hipótesis y propuesta; Arquitecto técnico (y 94 más)

### 2 · docs · Registro de decisiones y Trabajo nocturno de Claude

Cohesión 0.08 · 94 nodos: Registro de decisiones; Trabajo nocturno de Claude; Varios · empresa-ia; Atlas Evolucion v1.1 Modelo Operativo Procesos y Despliegue; Plan maestro: la empresa completa, sin que se escape nada; 17 · Cerebro, conocimiento y procesos: auditoría e informe; Informe de la mañana · 26/11/2026; Varios — repositorio maestro (y 86 más)

### 3 · knowledge/sectores · Registro de fuentes y Coordinación sectorial y seguros

Cohesión 0.07 · 84 nodos: Registro de fuentes; Coordinación sectorial y seguros; Responsable de cumplimiento normativo; Especialista legal y privacidad; Catálogo de excepciones al abrir un siniestro; Normas para abrir un siniestro en una correduría; Diseñador de producto y experiencia (UX); Marco Integral Legal Ciberseguridad IA Espana UE 2026-11-16 (y 76 más)

### 4 · processes/runbooks · Auditoría de agentes y habilidades frente a los procesos (M-040) y Dependencias entre procesos

Cohesión 0.18 · 64 nodos: Auditoría de agentes y habilidades frente a los procesos (M-040); Dependencias entre procesos; Mapa de autonomía por proceso, A0–A4 (M-045); Procesos y estados; P02 · Clasificación y triaje; P10 · Aprobación humana; P29 · Gestión de costes y capacidad; P37 · Medición de rendimiento y valor (y 56 más)

### 5 · precedents/oficina · Propuesta de proceso de referencia: siniestros en corredurías y Conversaciones con Coordinación sectorial · Seguros

Cohesión 0.15 · 59 nodos: Propuesta de proceso de referencia: siniestros en corredurías; Conversaciones con Coordinación sectorial · Seguros; Guion de validación semanal: apertura de siniestros; Conversaciones con Arquitecto de procesos; Memoria de la oficina; D-011 · Construir primero, clientes desde el 15/02/2027; CCS · Consorcio de Compensación de Seguros: riesgos extraordinarios; Línea base y fichas de métricas · Atalaya (y 51 más)

### 6 · processes/catalog · P22 · Gestión de errores y reintentos y Catálogo de procesos P01–P38

Cohesión 0.42 · 44 nodos: P22 · Gestión de errores y reintentos; Catálogo de procesos P01–P38; P28 · Gestión de incidentes; P22 · Gestión de errores y reintentos; P27 · Gestión de proveedores y dependencias; P33 · Diseño y validación TO-BE; P05 · Diseño del plan; P13 · Aprendizaje y actualización de la wiki (y 36 más)

### 7 · knowledge/comercial · Índice del conocimiento de Varios y Arquitecto de procesos

Cohesión 0.14 · 40 nodos: Índice del conocimiento de Varios; Arquitecto de procesos; P38 · Gestión de despliegue por cliente; P31 · Calificación de oportunidad; Director comercial; Especialista en éxito de cliente; INT-ATLAS · Atlas Evolución v1.1 · modelo operativo, procesos y despliegue; Responsable de implantación de clientes (y 32 más)

### 8 · knowledge/ingenieria · CEO digital y Especialista en ciberseguridad

Cohesión 0.15 · 36 nodos: CEO digital; Especialista en ciberseguridad; Arquitecto de datos e IA; Responsable de decisiones y seguimiento; Bibliotecario / responsable de conocimiento; Biblioteca de precedentes; Especialista en automatización; Arquitecto técnico (y 28 más)

### 9 · knowledge/sectores · Experto en sanidad privada y P32 · Descubrimiento de procesos

Cohesión 0.19 · 34 nodos: Experto en sanidad privada; P32 · Descubrimiento de procesos; Experto en servicios financieros no bancarios; Experto en asesorías, gestorías y despachos; Experto en logística y transporte; P33 · Diseño y validación TO-BE; Experto en industria manufacturera; Priorización de sectores (y 26 más)

### 10 · docs/atlas · Guia de Arranque Proyecto v1.4 Diseno Cerrado y Flujo ceo

Cohesión 0.38 · 31 nodos: Guia de Arranque Proyecto v1.4 Diseno Cerrado; Flujo ceo; Ejecucion agentes; Motor conocimiento obsidian; 12 · Ciclo de vida de un proyecto con cliente; Calidad gobierno; Comunicaciones estados; Registro de correcciones a los documentos recibidos el 17/11/2026 (y 23 más)

### 11 · claude/habilidades · Ingeniero de plataforma y operaciones (DevOps/SRE) y Plataforma y operaciones

Cohesión 0.19 · 15 nodos: Ingeniero de plataforma y operaciones (DevOps/SRE); Plataforma y operaciones; Ingeniero de plataforma y operaciones (DevOps/SRE); ENS-RD311 · Real Decreto 311/2022, Esquema Nacional de Seguridad; ISO-27001 · ISO/IEC 27001:2022 (transición desde 2013 terminada el 31/10/2025); OTEL-GENAI · OpenTelemetry: convenciones semánticas para IA generativa; Copias y restauración probada; Observabilidad y alertas (y 7 más)

### 12 · precedents/oficina · Acta de protección de la IA y examen de 50 casos y Conversaciones con IA y evaluación

Cohesión 0.55 · 11 nodos: Acta de protección de la IA y examen de 50 casos; L2 (puerta técnica); Conversaciones con IA y evaluación; Reunión: IA y evaluación y Seguridad; Conversaciones con CEO digital; Conversaciones con Plan y seguimiento; Conversaciones con Registro de decisiones; Conversaciones con Bibliotecario (y 3 más)

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

- **¿Por qué «Registro de fuentes» conecta la comunidad 3 con las comunidades 0, 2, 4, 5?**
  _Intermediación alta (0.134): es un puente entre temas._
- **¿Por qué «Registro de decisiones» conecta la comunidad 2 con las comunidades 0, 3, 4, 5?**
  _Intermediación alta (0.046): es un puente entre temas._
- **¿Por qué «Habilidades de los agentes» conecta la comunidad 0 con las comunidades 4, 5, 7, 8?**
  _Intermediación alta (0.044): es un puente entre temas._
- **¿Se aprueba D-019 · Calidad exigente, todo pasa por un socio y cada rechazo se rehace aprendiendo? Sigue en propuesta y la citan 17 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-013 · Conocimiento y catálogo de procesos generados desde datos? Sigue en propuesta y la citan 12 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-017 · La oficina se vuelca cada noche a GitHub y las automatizaciones van por GitHub Actions? Sigue en propuesta y la citan 11 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Deberían enlazarse «knowledge/plantillas/entregables/02-informe-diagnostico.md» y «processes/templates/proceso-cliente.md»?**
  _Tratan lo mismo (relación INFERIDA 0.85) pero no se citan._
- **¿Deberían enlazarse «docs/26-web-clientes.md» y «knowledge/fuentes/registro.md»?**
  _Tratan lo mismo (relación INFERIDA 0.85) pero no se citan._
- **¿Siguen vigentes D-008, D-016? Ningún documento las cita.**
  _Decisiones que nadie menciona._

## Cómo usarlo

- En la oficina, cada agente recibe las secciones que encajan con su encargo **y lo conectado a ellas** (decisiones, procesos, fuentes y secciones relacionadas), con la etiqueta de confianza de cada relación.
- En local: `python3 tools/grafo.py consulta "pregunta"`, `camino "A" "B"` y `explica "X"`.
- Las relaciones INFERIDAS son pistas, no hechos: si una es buena, conviértela en un enlace en el documento y pasará a EXTRACTADA.
