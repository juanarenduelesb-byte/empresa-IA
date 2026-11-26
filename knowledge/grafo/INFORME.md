<!-- Generado por tools/brain_build.py (tools/grafo.py). No editar a mano. -->
# Informe del grafo de conocimiento

Cómo está conectado el cerebro de Varios: qué sostiene todo, qué temas forman grupos, qué conecta temas distintos, qué falta y qué preguntas conviene hacerse. Se regenera con el cerebro (D-018); no forma parte del grafo.

## Resumen

- 4962 nodos: seccion 4262, documento 372, fuente 113, habilidad 65, proceso 38, especialista 34, agente 34, decision 25, puerta 12, departamento 7.
- 6715 relaciones: 62 % EXTRACTADAS (escritas en la fuente), 38 % INFERIDAS (temas compartidos, con puntuación) y 0 AMBIGUAS (para revisar).
- 14 comunidades de temas.

## Nodos centrales

Lo que más cosas conecta. Si cambia, cambia mucho.

1. **Registro de fuentes** (`knowledge/fuentes/registro.md`) · 201 conexiones
2. **Índice del conocimiento de Varios** (`knowledge/INDEX.md`) · 118 conexiones
3. **Registro de decisiones** (`DECISIONS.md`) · 105 conexiones
4. **Guia de Arranque Proyecto v1.4 Diseno Cerrado** (`docs/fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md`) · 84 conexiones
5. **Catálogo de procesos P01–P38** (`processes/catalog/README.md`) · 82 conexiones
6. **Habilidades de los agentes** (`claude/habilidades/README.md`) · 68 conexiones
7. **L2 (puerta técnica)** · 66 conexiones
8. **P22 · Gestión de errores y reintentos** · 62 conexiones
9. **P28 · Gestión de incidentes** · 61 conexiones
10. **Varios · empresa-ia** (`CLAUDE.md`) · 61 conexiones
11. **CEO digital** (`knowledge/direccion/ceo-digital.md`) · 59 conexiones
12. **Arquitecto de procesos** (`knowledge/procesos/arquitecto-procesos.md`) · 50 conexiones

## Puentes entre temas

Nodos por los que pasa el camino entre comunidades distintas (intermediación).

- **Registro de fuentes** · intermediación 0.267 · une la comunidad 1 con 2, 3, 4, 5, 6, 7
- **Registro de decisiones** · intermediación 0.092 · une la comunidad 3 con 1, 2, 4, 5, 6, 8
- **Habilidades de los agentes** · intermediación 0.079 · une la comunidad 2 con 4, 5, 6, 10
- **L2 (puerta técnica)** · intermediación 0.053 · une la comunidad 11 con 1, 2, 3, 4, 5, 7
- **Índice del conocimiento de Varios** · intermediación 0.051 · une la comunidad 6 con 1, 3, 4, 5, 7, 8
- **Guia de Arranque Proyecto v1.4 Diseno Cerrado** · intermediación 0.04 · une la comunidad 8 con 2, 3, 4, 7, 9
- **CEO digital** · intermediación 0.023 · une la comunidad 4 con 1, 2, 3, 6, 7, 8
- **D-011 · Construir primero, clientes desde el 15/02/2027** · intermediación 0.021 · une la comunidad 5 con 1, 2, 3, 6, 11, 13
- **Administración** · intermediación 0.021 · une la comunidad 2 con 0, 1, 9, 10, 11
- **Experto en asesorías y despachos** · intermediación 0.02 · une la comunidad 2 con 0, 1, 8, 10, 11

## Conexiones sorprendentes

Secciones de carpetas y comunidades distintas que tratan lo mismo y no se enlazan. Relación INFERIDA: compruébala.

- `DECISIONS.md` › D-005 — Aislamiento multi-cliente  ↔  `docs/06-seguridad-y-gobierno.md` › Multi-tenancy  [INFERIDA 0.85]
- `governance/legal/borradores/03-acuerdo-confidencialidad.md` › Acuerdo de confidencialidad (mutuo) · BORRADOR PARA ABOGADO  ↔  `knowledge/plantillas/entregables/01-propuesta-diagnostico.md` › 6. Siguientes pasos  [INFERIDA 0.75]
- `governance/legal/borradores/04-anexo-uso-ia.md` › 1. Qué sistema es y para qué se usa  ↔  `knowledge/agentes/proj.md` › Reglas del puesto  [INFERIDA 0.75]
- `governance/legal/borradores/04-anexo-uso-ia.md` › 4. Clasificación del riesgo  ↔  `knowledge/fuentes/registro.md` › RIA-2024-1689  [INFERIDA 0.75]
- `governance/legal/borradores/05-matriz-aprobaciones.md` › 4. Reglas de la aprobación  ↔  `knowledge/fuentes/registro.md` › ZAPIER-HITL  [INFERIDA 0.75]
- `integrations/tests/README.md` › Pruebas de integración  ↔  `knowledge/ingenieria/integraciones.md` › Especialista en integraciones  [INFERIDA 0.75]
- `claude/habilidades/contrato-de-tarea.md` › Pasos  ↔  `docs/03-ceo-digital-y-orquestacion.md` › Contrato de tarea  [INFERIDA 0.75]
- `knowledge/agentes/dat.md` › Reglas del puesto  ↔  `precedents/oficina/encargos/2026-11/2026-11-17-examen-de-25-casos-ficticios-para-atalaya-qq164.md` › Contrato de tarea del CEO  [INFERIDA 0.75]
- `knowledge/agentes/ingj.md` › Reglas del puesto  ↔  `processes/catalog/P01-alta-y-recepcion-de-peticion.md` › 7. Decisiones y reglas  [INFERIDA 0.75]
- `knowledge/agentes/kpi.md` › Reglas del puesto  ↔  `precedents/oficina/conversaciones/2026-11/2026-11-17-ceo-digital-a-metricas-sj6cp.md` › CEO digital → Métricas  [INFERIDA 0.75]

## Comunidades

### 0 · Habilidades · Legal y privacidad y Arquitecto de procesos

Cohesión 0.05 · 104 nodos: Legal y privacidad; Arquitecto de procesos; Seguridad; Coordinación sectorial · Seguros; Director financiero; Jefe comercial; Separar hecho, hipótesis y propuesta; Arquitecto técnico (y 96 más)

### 1 · knowledge/sectores · Registro de fuentes y Coordinación sectorial y seguros

Cohesión 0.07 · 99 nodos: Registro de fuentes; Coordinación sectorial y seguros; Experto en sanidad privada; Experto en servicios financieros no bancarios; Experto en asesorías, gestorías y despachos; Experto en logística y transporte; Especialista en contabilidad y facturación; Experto en industria manufacturera (y 91 más)

### 2 · claude/habilidades · Habilidades de los agentes y Administración

Cohesión 0.1 · 93 nodos: Habilidades de los agentes; Administración; Experto en asesorías y despachos; Backend; Agentes de la oficina; Arquitecto de procesos; Director financiero; Jefe comercial (y 85 más)

### 3 · docs · Registro de decisiones y Varios · empresa-ia

Cohesión 0.1 · 76 nodos: Registro de decisiones; Varios · empresa-ia; Atlas Evolucion v1.1 Modelo Operativo Procesos y Despliegue; Trabajo nocturno de Claude; Informe de la mañana · 26/11/2026; 17 · Cerebro, conocimiento y procesos: auditoría e informe; Plan de construcción · 18/11/2026 → 12/02/2027; G0 (puerta de cliente) (y 68 más)

### 4 · knowledge/ingenieria · Dependencias entre procesos y CEO digital

Cohesión 0.14 · 75 nodos: Dependencias entre procesos; CEO digital; Especialista en ciberseguridad; Procesos y estados; P02 · Clasificación y triaje; Arquitecto de datos e IA; Responsable de decisiones y seguimiento; Bibliotecario / responsable de conocimiento (y 67 más)

### 5 · precedents/oficina · Propuesta de proceso de referencia: siniestros en corredurías y Conversaciones con Coordinación sectorial · Seguros

Cohesión 0.15 · 59 nodos: Propuesta de proceso de referencia: siniestros en corredurías; Conversaciones con Coordinación sectorial · Seguros; Guion de validación semanal: apertura de siniestros; Conversaciones con Arquitecto de procesos; Memoria de la oficina; D-011 · Construir primero, clientes desde el 15/02/2027; Línea base y fichas de métricas · Atalaya; CCS · Consorcio de Compensación de Seguros: riesgos extraordinarios (y 51 más)

### 6 · processes/catalog · Índice del conocimiento de Varios y Arquitecto de procesos

Cohesión 0.16 · 51 nodos: Índice del conocimiento de Varios; Arquitecto de procesos; P32 · Descubrimiento de procesos; P33 · Diseño y validación TO-BE; Director comercial; P38 · Gestión de despliegue por cliente; Biblioteca de precedentes; P31 · Calificación de oportunidad (y 43 más)

### 7 · processes/catalog · P22 · Gestión de errores y reintentos y Catálogo de procesos P01–P38

Cohesión 0.44 · 40 nodos: P22 · Gestión de errores y reintentos; Catálogo de procesos P01–P38; P28 · Gestión de incidentes; P22 · Gestión de errores y reintentos; P27 · Gestión de proveedores y dependencias; P05 · Diseño del plan; P11 · Entrega y cierre; P13 · Aprendizaje y actualización de la wiki (y 32 más)

### 8 · docs/atlas · Guia de Arranque Proyecto v1.4 Diseno Cerrado y Flujo ceo

Cohesión 0.29 · 37 nodos: Guia de Arranque Proyecto v1.4 Diseno Cerrado; Flujo ceo; Ejecucion agentes; Motor conocimiento obsidian; Marco Integral Legal Ciberseguridad IA Espana UE 2026-11-16; 12 · Ciclo de vida de un proyecto con cliente; Calidad gobierno; Comunicaciones estados (y 29 más)

### 9 · knowledge/administracion-finanzas · Responsable de cumplimiento normativo y Especialista legal y privacidad

Cohesión 0.16 · 30 nodos: Responsable de cumplimiento normativo; Especialista legal y privacidad; Director financiero (CFO); P29 · Gestión de costes y capacidad; Especialista en costes y proveedores; P27 · Gestión de proveedores y dependencias; P19 · Política de uso y límites; Especialista financiero (y 22 más)

### 10 · claude/habilidades · Ingeniero de plataforma y operaciones (DevOps/SRE) y Plataforma y operaciones

Cohesión 0.2 · 14 nodos: Ingeniero de plataforma y operaciones (DevOps/SRE); Plataforma y operaciones; Ingeniero de plataforma y operaciones (DevOps/SRE); ENS-RD311 · Real Decreto 311/2022, Esquema Nacional de Seguridad; OTEL-GENAI · OpenTelemetry: convenciones semánticas para IA generativa; Copias y restauración probada; Observabilidad y alertas; DORA-DEVOPS · Métricas DORA de entrega de software (DevOps Research and Assessment) (y 6 más)

### 11 · precedents/oficina · Acta de protección de la IA y examen de 50 casos y Conversaciones con IA y evaluación

Cohesión 0.55 · 11 nodos: Acta de protección de la IA y examen de 50 casos; L2 (puerta técnica); Conversaciones con IA y evaluación; Reunión: IA y evaluación y Seguridad; Conversaciones con CEO digital; Conversaciones con Plan y seguimiento; Conversaciones con Registro de decisiones; Conversaciones con Bibliotecario (y 3 más)

### 12 · knowledge/ingenieria · Diseñador de producto y experiencia (UX) y Diseñador de producto y experiencia (UX)

Cohesión 0.7 · 5 nodos: Diseñador de producto y experiencia (UX); LEY-ACCESIBILIDAD-11-2023 · Ley 11/2023 (accesibilidad de productos y servicios, transpone la Directiva (UE) 2019/882); Diseñador de producto y experiencia (UX); NNG-HEURISTICAS · 10 heurísticas de usabilidad (Jakob Nielsen); W3C-WCAG22 · Web Content Accessibility Guidelines (WCAG) 2.2

### 13 · integrations · Integraciones y Contratos de datos

Cohesión 0.83 · 4 nodos: Integraciones; Contratos de datos; Pruebas de integración; Conectores

## Huecos

- **Documentos sin ninguna relación** (2): `precedents/projects/2026-11-oficina-de-agentes.md`; `precedents/solutions/busqueda-texto-cerebro.md`
- **Decisiones que no cita ninguna sección** (3): D-008, D-016, D-020
- **Procesos sin especialista responsable** (0): ninguno
- **Fuentes registradas que nadie cita** (0): ninguna
- **Referencias rotas** (se citan pero no existen): ninguna
- **Enlaces ambiguos** (un nombre de archivo con varios destinos): 0

## Preguntas sugeridas

_Preguntas que este grafo ayuda a responder o que conviene decidir:_

- **¿Por qué «Registro de fuentes» conecta la comunidad 1 con las comunidades 2, 3, 4, 5?**
  _Intermediación alta (0.267): es un puente entre temas._
- **¿Por qué «Registro de decisiones» conecta la comunidad 3 con las comunidades 1, 2, 4, 5?**
  _Intermediación alta (0.092): es un puente entre temas._
- **¿Por qué «Habilidades de los agentes» conecta la comunidad 2 con las comunidades 4, 5, 6, 10?**
  _Intermediación alta (0.079): es un puente entre temas._
- **¿Se aprueba D-013 · Conocimiento y catálogo de procesos generados desde datos? Sigue en propuesta y la citan 12 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-017 · La oficina se vuelca cada noche a GitHub y las automatizaciones van por GitHub Actions? Sigue en propuesta y la citan 11 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-019 · Calidad exigente, todo pasa por un socio y cada rechazo se rehace aprendiendo? Sigue en propuesta y la citan 11 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Deberían enlazarse «DECISIONS.md» y «docs/06-seguridad-y-gobierno.md»?**
  _Tratan lo mismo (relación INFERIDA 0.85) pero no se citan._
- **¿Deberían enlazarse «governance/legal/borradores/03-acuerdo-confidencialidad.md» y «knowledge/plantillas/entregables/01-propuesta-diagnostico.md»?**
  _Tratan lo mismo (relación INFERIDA 0.75) pero no se citan._
- **¿Siguen vigentes D-008, D-016, D-020? Ningún documento las cita.**
  _Decisiones que nadie menciona._

## Cómo usarlo

- En la oficina, cada agente recibe las secciones que encajan con su encargo **y lo conectado a ellas** (decisiones, procesos, fuentes y secciones relacionadas), con la etiqueta de confianza de cada relación.
- En local: `python3 tools/grafo.py consulta "pregunta"`, `camino "A" "B"` y `explica "X"`.
- Las relaciones INFERIDAS son pistas, no hechos: si una es buena, conviértela en un enlace en el documento y pasará a EXTRACTADA.
