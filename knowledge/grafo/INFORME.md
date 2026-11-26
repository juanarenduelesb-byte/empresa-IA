<!-- Generado por tools/brain_build.py (tools/grafo.py). No editar a mano. -->
# Informe del grafo de conocimiento

Cómo está conectado el cerebro de Varios: qué sostiene todo, qué temas forman grupos, qué conecta temas distintos, qué falta y qué preguntas conviene hacerse. Se regenera con el cerebro (D-018); no forma parte del grafo.

## Resumen

- 5022 nodos: seccion 4311, documento 376, fuente 117, habilidad 65, proceso 38, especialista 34, agente 34, decision 28, puerta 12, departamento 7.
- 7085 relaciones: 63 % EXTRACTADAS (escritas en la fuente), 37 % INFERIDAS (temas compartidos, con puntuación) y 38 AMBIGUAS (para revisar).
- 12 comunidades de temas.

## Nodos centrales

Lo que más cosas conecta. Si cambia, cambia mucho.

1. **Registro de fuentes** (`knowledge/fuentes/registro.md`) · 209 conexiones
2. **Índice del conocimiento de Varios** (`knowledge/INDEX.md`) · 119 conexiones
3. **Registro de decisiones** (`DECISIONS.md`) · 118 conexiones
4. **Guia de Arranque Proyecto v1.4 Diseno Cerrado** (`docs/fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md`) · 85 conexiones
5. **Catálogo de procesos P01–P38** (`processes/catalog/README.md`) · 83 conexiones
6. **Habilidades de los agentes** (`claude/habilidades/README.md`) · 69 conexiones
7. **L2 (puerta técnica)** · 68 conexiones
8. **P22 · Gestión de errores y reintentos** · 64 conexiones
9. **Auditoría de agentes y habilidades frente a los procesos (M-040)** (`docs/28-auditoria-agentes.md`) · 64 conexiones
10. **P28 · Gestión de incidentes** · 63 conexiones
11. **Varios · empresa-ia** (`CLAUDE.md`) · 63 conexiones
12. **CEO digital** (`knowledge/direccion/ceo-digital.md`) · 60 conexiones

## Puentes entre temas

Nodos por los que pasa el camino entre comunidades distintas (intermediación).

- **Registro de fuentes** · intermediación 0.135 · une la comunidad 1 con 2, 3, 4, 5, 6, 7
- **Registro de decisiones** · intermediación 0.049 · une la comunidad 2 con 1, 3, 4, 5, 6, 7
- **Habilidades de los agentes** · intermediación 0.045 · une la comunidad 3 con 0, 4, 5, 6, 7, 11
- **L2 (puerta técnica)** · intermediación 0.025 · une la comunidad 10 con 1, 2, 3, 4, 5, 6
- **Índice del conocimiento de Varios** · intermediación 0.023 · une la comunidad 7 con 1, 2, 4, 5, 6, 8
- **Estudios** · intermediación 0.019 · une la comunidad 11 con 1, 2, 3, 4, 5, 6
- **Guia de Arranque Proyecto v1.4 Diseno Cerrado** · intermediación 0.018 · une la comunidad 9 con 2, 3, 4, 5, 8
- **CEO digital** · intermediación 0.01 · une la comunidad 5 con 1, 2, 3, 4, 7, 8
- **Administración** · intermediación 0.01 · une la comunidad 3 con 0, 1, 5, 10
- **D-011 · Construir primero, clientes desde el 15/02/2027** · intermediación 0.01 · une la comunidad 6 con 1, 2, 3, 4, 5, 7

## Conexiones sorprendentes

Secciones de carpetas y comunidades distintas que tratan lo mismo y no se enlazan. Relación INFERIDA: compruébala.

- `DECISIONS.md` › D-005 — Aislamiento multi-cliente  ↔  `docs/06-seguridad-y-gobierno.md` › Multi-tenancy  [INFERIDA 0.85]
- `docs/26-web-clientes.md` › 4. Requisitos legales de la web  ↔  `knowledge/fuentes/registro.md` › LSSI-34-2002  [INFERIDA 0.85]
- `docs/28-auditoria-agentes.md` › Criterio  ↔  `knowledge/fuentes/registro.md` › ANTHROPIC-AGENTES  [INFERIDA 0.85]
- `docs/29-autonomia.md` › Niveles  ↔  `knowledge/fuentes/registro.md` › KNIGHT-NIVELES-AUTONOMIA  [INFERIDA 0.85]
- `governance/legal/borradores/03-acuerdo-confidencialidad.md` › Acuerdo de confidencialidad (mutuo) · BORRADOR PARA ABOGADO  ↔  `knowledge/plantillas/entregables/01-propuesta-diagnostico.md` › 6. Siguientes pasos  [INFERIDA 0.75]
- `governance/legal/borradores/04-anexo-uso-ia.md` › 1. Qué sistema es y para qué se usa  ↔  `knowledge/agentes/proj.md` › Reglas del puesto  [INFERIDA 0.75]
- `governance/legal/borradores/04-anexo-uso-ia.md` › 4. Clasificación del riesgo  ↔  `knowledge/fuentes/registro.md` › RIA-2024-1689  [INFERIDA 0.75]
- `governance/legal/borradores/05-matriz-aprobaciones.md` › 4. Reglas de la aprobación  ↔  `knowledge/fuentes/registro.md` › ZAPIER-HITL  [INFERIDA 0.75]
- `integrations/tests/README.md` › Pruebas de integración  ↔  `knowledge/ingenieria/integraciones.md` › Especialista en integraciones  [INFERIDA 0.75]
- `claude/habilidades/contrato-de-tarea.md` › Pasos  ↔  `docs/03-ceo-digital-y-orquestacion.md` › Contrato de tarea  [INFERIDA 0.75]

## Comunidades

### 0 · claude/habilidades · Legal y privacidad y Arquitecto de procesos

Cohesión 0.05 · 107 nodos: Legal y privacidad; Arquitecto de procesos; Seguridad; Coordinación sectorial · Seguros; Director financiero; Jefe comercial; Separar hecho, hipótesis y propuesta; Arquitecto técnico (y 99 más)

### 1 · knowledge/sectores · Registro de fuentes y Coordinación sectorial y seguros

Cohesión 0.07 · 100 nodos: Registro de fuentes; Coordinación sectorial y seguros; Experto en sanidad privada; Experto en asesorías, gestorías y despachos; Experto en servicios financieros no bancarios; Experto en logística y transporte; Especialista en contabilidad y facturación; P33 · Diseño y validación TO-BE (y 92 más)

### 2 · docs · Registro de decisiones y Trabajo nocturno de Claude

Cohesión 0.07 · 93 nodos: Registro de decisiones; Trabajo nocturno de Claude; Atlas Evolucion v1.1 Modelo Operativo Procesos y Despliegue; Informe de la mañana · 26/11/2026; 17 · Cerebro, conocimiento y procesos: auditoría e informe; Plan maestro: la empresa completa, sin que se escape nada; Plan de construcción · 18/11/2026 → 12/02/2027; G0 (puerta de cliente) (y 85 más)

### 3 · claude/habilidades · Habilidades de los agentes y Administración

Cohesión 0.1 · 93 nodos: Habilidades de los agentes; Administración; Experto en asesorías y despachos; Backend; Agentes de la oficina; Arquitecto de procesos; Director financiero; Jefe comercial (y 85 más)

### 4 · processes/runbooks · Auditoría de agentes y habilidades frente a los procesos (M-040) y Dependencias entre procesos

Cohesión 0.19 · 62 nodos: Auditoría de agentes y habilidades frente a los procesos (M-040); Dependencias entre procesos; Mapa de autonomía por proceso, A0–A4 (M-045); Procesos y estados; P02 · Clasificación y triaje; P10 · Aprobación humana; P29 · Gestión de costes y capacidad; P21 · Ejecución segura de herramientas (y 54 más)

### 5 · knowledge/ingenieria · CEO digital y Varios · empresa-ia

Cohesión 0.1 · 61 nodos: CEO digital; Varios · empresa-ia; Especialista en ciberseguridad; Responsable de cumplimiento normativo; Ingeniero de plataforma y operaciones (DevOps/SRE); Especialista legal y privacidad; Arquitecto de datos e IA; Responsable de decisiones y seguimiento (y 53 más)

### 6 · precedents/oficina · Propuesta de proceso de referencia: siniestros en corredurías y Conversaciones con Coordinación sectorial · Seguros

Cohesión 0.16 · 58 nodos: Propuesta de proceso de referencia: siniestros en corredurías; Conversaciones con Coordinación sectorial · Seguros; Guion de validación semanal: apertura de siniestros; Conversaciones con Arquitecto de procesos; Memoria de la oficina; D-011 · Construir primero, clientes desde el 15/02/2027; Línea base y fichas de métricas · Atalaya; CCS · Consorcio de Compensación de Seguros: riesgos extraordinarios (y 50 más)

### 7 · processes/catalog · Índice del conocimiento de Varios y Arquitecto de procesos

Cohesión 0.16 · 48 nodos: Índice del conocimiento de Varios; Arquitecto de procesos; P32 · Descubrimiento de procesos; P38 · Gestión de despliegue por cliente; P31 · Calificación de oportunidad; P33 · Diseño y validación TO-BE; Director comercial; P37 · Medición de rendimiento y valor (y 40 más)

### 8 · processes/catalog · P22 · Gestión de errores y reintentos y Catálogo de procesos P01–P38

Cohesión 0.52 · 36 nodos: P22 · Gestión de errores y reintentos; Catálogo de procesos P01–P38; P28 · Gestión de incidentes; P22 · Gestión de errores y reintentos; P27 · Gestión de proveedores y dependencias; P05 · Diseño del plan; P11 · Entrega y cierre; P13 · Aprendizaje y actualización de la wiki (y 28 más)

### 9 · docs/atlas · Guia de Arranque Proyecto v1.4 Diseno Cerrado y Flujo ceo

Cohesión 0.32 · 35 nodos: Guia de Arranque Proyecto v1.4 Diseno Cerrado; Flujo ceo; Ejecucion agentes; Motor conocimiento obsidian; Marco Integral Legal Ciberseguridad IA Espana UE 2026-11-16; 12 · Ciclo de vida de un proyecto con cliente; Calidad gobierno; Comunicaciones estados (y 27 más)

### 10 · precedents/oficina · Acta de protección de la IA y examen de 50 casos y Conversaciones con IA y evaluación

Cohesión 0.55 · 11 nodos: Acta de protección de la IA y examen de 50 casos; L2 (puerta técnica); Conversaciones con IA y evaluación; Reunión: IA y evaluación y Seguridad; Conversaciones con CEO digital; Conversaciones con Plan y seguimiento; Conversaciones con Registro de decisiones; Conversaciones con Bibliotecario (y 3 más)

### 11 · knowledge/estudios · Estudios y Integraciones

Cohesión 0.9 · 5 nodos: Estudios; Integraciones; Contratos de datos; Pruebas de integración; Conectores

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
  - `knowledge/estudios/README.md` → `integrations/README.md`
  - `knowledge/estudios/README.md` → `integrations/catalog/README.md`
  - `knowledge/estudios/README.md` → `integrations/connectors/README.md`
  - `knowledge/estudios/README.md` → `integrations/contracts/README.md`

## Preguntas sugeridas

_Preguntas que este grafo ayuda a responder o que conviene decidir:_

- **¿Por qué «Registro de fuentes» conecta la comunidad 1 con las comunidades 2, 3, 4, 5?**
  _Intermediación alta (0.135): es un puente entre temas._
- **¿Por qué «Registro de decisiones» conecta la comunidad 2 con las comunidades 1, 3, 4, 5?**
  _Intermediación alta (0.049): es un puente entre temas._
- **¿Por qué «Habilidades de los agentes» conecta la comunidad 3 con las comunidades 0, 4, 5, 6?**
  _Intermediación alta (0.045): es un puente entre temas._
- **¿Se aprueba D-019 · Calidad exigente, todo pasa por un socio y cada rechazo se rehace aprendiendo? Sigue en propuesta y la citan 14 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-013 · Conocimiento y catálogo de procesos generados desde datos? Sigue en propuesta y la citan 12 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-017 · La oficina se vuelca cada noche a GitHub y las automatizaciones van por GitHub Actions? Sigue en propuesta y la citan 11 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Deberían enlazarse «DECISIONS.md» y «docs/06-seguridad-y-gobierno.md»?**
  _Tratan lo mismo (relación INFERIDA 0.85) pero no se citan._
- **¿Deberían enlazarse «docs/26-web-clientes.md» y «knowledge/fuentes/registro.md»?**
  _Tratan lo mismo (relación INFERIDA 0.85) pero no se citan._
- **¿Siguen vigentes D-008, D-016? Ningún documento las cita.**
  _Decisiones que nadie menciona._

## Cómo usarlo

- En la oficina, cada agente recibe las secciones que encajan con su encargo **y lo conectado a ellas** (decisiones, procesos, fuentes y secciones relacionadas), con la etiqueta de confianza de cada relación.
- En local: `python3 tools/grafo.py consulta "pregunta"`, `camino "A" "B"` y `explica "X"`.
- Las relaciones INFERIDAS son pistas, no hechos: si una es buena, conviértela en un enlace en el documento y pasará a EXTRACTADA.
