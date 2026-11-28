<!-- Generado por tools/brain_build.py (tools/grafo.py). No editar a mano. -->
# Informe del grafo de conocimiento

Cómo está conectado el cerebro de Varios: qué sostiene todo, qué temas forman grupos, qué conecta temas distintos, qué falta y qué preguntas conviene hacerse. Se regenera con el cerebro (D-018); no forma parte del grafo.

## Resumen

- 5249 nodos: seccion 4490, documento 390, fuente 146, habilidad 65, proceso 38, especialista 34, agente 34, decision 33, puerta 12, departamento 7.
- 7587 relaciones: 64 % EXTRACTADAS (escritas en la fuente), 35 % INFERIDAS (temas compartidos, con puntuación) y 40 AMBIGUAS (para revisar).
- 14 comunidades de temas.

## Nodos centrales

Lo que más cosas conecta. Si cambia, cambia mucho.

1. **Registro de fuentes** (`knowledge/fuentes/registro.md`) · 254 conexiones
2. **Registro de decisiones** (`DECISIONS.md`) · 143 conexiones
3. **Índice del conocimiento de Varios** (`knowledge/INDEX.md`) · 123 conexiones
4. **Guia de Arranque Proyecto v1.4 Diseno Cerrado** (`docs/fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md`) · 85 conexiones
5. **Catálogo de procesos P01–P38** (`processes/catalog/README.md`) · 83 conexiones
6. **Trabajo nocturno de Claude** (`docs/21-trabajo-nocturno.md`) · 78 conexiones
7. **L2 (puerta técnica)** · 75 conexiones
8. **Varios · empresa-ia** (`CLAUDE.md`) · 71 conexiones
9. **Habilidades de los agentes** (`claude/habilidades/README.md`) · 69 conexiones
10. **Mapa de autonomía por proceso, A0–A4 (M-045)** (`docs/29-autonomia.md`) · 67 conexiones
11. **Auditoría de agentes y habilidades frente a los procesos (M-040)** (`docs/28-auditoria-agentes.md`) · 65 conexiones
12. **P22 · Gestión de errores y reintentos** · 64 conexiones

## Puentes entre temas

Nodos por los que pasa el camino entre comunidades distintas (intermediación).

- **Registro de fuentes** · intermediación 0.156 · une la comunidad 2 con 1, 3, 4, 5, 6, 7
- **Registro de decisiones** · intermediación 0.052 · une la comunidad 3 con 1, 2, 4, 5, 6, 7
- **Habilidades de los agentes** · intermediación 0.039 · une la comunidad 1 con 0, 4, 5, 6, 7, 13
- **L2 (puerta técnica)** · intermediación 0.027 · une la comunidad 12 con 1, 2, 3, 4, 6, 7
- **Índice del conocimiento de Varios** · intermediación 0.022 · une la comunidad 5 con 1, 2, 3, 4, 6, 7
- **Guia de Arranque Proyecto v1.4 Diseno Cerrado** · intermediación 0.016 · une la comunidad 9 con 1, 3, 4, 5, 7, 8
- **Estudios** · intermediación 0.016 · une la comunidad 13 con 1, 2, 3, 4, 5, 6
- **D-011 · Construir primero, clientes desde el 15/02/2027** · intermediación 0.01 · une la comunidad 6 con 1, 2, 3, 4, 5, 10
- **Trabajo nocturno de Claude** · intermediación 0.01 · une la comunidad 3 con 2, 4, 5, 6, 10, 11
- **CEO digital** · intermediación 0.009 · une la comunidad 7 con 1, 2, 3, 4, 5, 8

## Conexiones sorprendentes

Secciones de carpetas y comunidades distintas que tratan lo mismo y no se enlazan. Relación INFERIDA: compruébala.

- `DECISIONS.md` › D-005 — Aislamiento multi-cliente  ↔  `docs/06-seguridad-y-gobierno.md` › Multi-tenancy  [INFERIDA 0.85]
- `docs/26-web-clientes.md` › 4. Requisitos legales de la web  ↔  `knowledge/fuentes/registro.md` › LSSI-34-2002  [INFERIDA 0.85]
- `docs/28-auditoria-agentes.md` › Criterio  ↔  `knowledge/fuentes/registro.md` › ANTHROPIC-AGENTES  [INFERIDA 0.85]
- `docs/29-autonomia.md` › Niveles  ↔  `knowledge/fuentes/registro.md` › KNIGHT-NIVELES-AUTONOMIA  [INFERIDA 0.85]
- `docs/fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md` › 4.1 Reintentos y operaciones duplicadas  ↔  `processes/catalog/P22-gestion-de-errores-y-reintentos.md` › 9. Entradas y salidas de cada tarea  [INFERIDA 0.85]
- `docs/fuentes/Marco_Integral_Legal_Ciberseguridad_IA_Espana_UE_2026-11-16.md` › 2.5 Encargados y subencargados  ↔  `governance/legal/borradores/02-encargo-tratamiento.md` › 7. Comprobación del art. 28.3 RGPD  [INFERIDA 0.75]
- `docs/fuentes/Marco_Integral_Legal_Ciberseguridad_IA_Espana_UE_2026-11-16.md` › 8.1 LSSI-CE, web y comercio electrónico  ↔  `knowledge/fuentes/registro.md` › LSSI-34-2002  [INFERIDA 0.75]
- `governance/legal/borradores/03-acuerdo-confidencialidad.md` › Acuerdo de confidencialidad (mutuo) · BORRADOR PARA ABOGADO  ↔  `knowledge/plantillas/entregables/01-propuesta-diagnostico.md` › 6. Siguientes pasos  [INFERIDA 0.75]
- `governance/legal/borradores/04-anexo-uso-ia.md` › 1. Qué sistema es y para qué se usa  ↔  `knowledge/agentes/proj.md` › Reglas del puesto  [INFERIDA 0.75]
- `governance/legal/borradores/04-anexo-uso-ia.md` › 4. Clasificación del riesgo  ↔  `knowledge/fuentes/registro.md` › RIA-2024-1689  [INFERIDA 0.75]

## Comunidades

### 0 · claude/habilidades · Legal y privacidad y Arquitecto de procesos

Cohesión 0.05 · 108 nodos: Legal y privacidad; Arquitecto de procesos; Seguridad; Coordinación sectorial · Seguros; Director financiero; Jefe comercial; Separar hecho, hipótesis y propuesta; Arquitecto técnico (y 100 más)

### 1 · claude/habilidades · Habilidades de los agentes y Administración

Cohesión 0.09 · 96 nodos: Habilidades de los agentes; Administración; Experto en asesorías y despachos; Backend; Agentes de la oficina; Arquitecto de procesos; Jefe comercial; Director financiero (y 88 más)

### 2 · knowledge/sectores · Registro de fuentes y Coordinación sectorial y seguros

Cohesión 0.07 · 89 nodos: Registro de fuentes; Coordinación sectorial y seguros; Experto en sanidad privada; Experto en servicios financieros no bancarios; P33 · Diseño y validación TO-BE; Catálogo de excepciones al abrir un siniestro; Experto en logística y transporte; Normas para abrir un siniestro en una correduría (y 81 más)

### 3 · docs · Registro de decisiones y Trabajo nocturno de Claude

Cohesión 0.08 · 83 nodos: Registro de decisiones; Trabajo nocturno de Claude; Varios · empresa-ia; Base de datos (D-023, propuesta); Informe de la mañana · 27/11/2026; Plan maestro: la empresa completa, sin que se escape nada; Informe de la mañana · 26/11/2026; Política de uso de inteligencia artificial de Varios · BORRADOR PARA ABOGADO (y 75 más)

### 4 · processes/runbooks · Auditoría de agentes y habilidades frente a los procesos (M-040) y Dependencias entre procesos

Cohesión 0.18 · 64 nodos: Auditoría de agentes y habilidades frente a los procesos (M-040); Dependencias entre procesos; Mapa de autonomía por proceso, A0–A4 (M-045); Procesos y estados; P02 · Clasificación y triaje; P10 · Aprobación humana; P29 · Gestión de costes y capacidad; P37 · Medición de rendimiento y valor (y 56 más)

### 5 · processes/catalog · Índice del conocimiento de Varios y Arquitecto de procesos

Cohesión 0.12 · 60 nodos: Índice del conocimiento de Varios; Arquitecto de procesos; P32 · Descubrimiento de procesos; P38 · Gestión de despliegue por cliente; P31 · Calificación de oportunidad; P33 · Diseño y validación TO-BE; Director comercial; P32 · Descubrimiento de procesos (y 52 más)

### 6 · precedents/oficina · Propuesta de proceso de referencia: siniestros en corredurías y Conversaciones con Coordinación sectorial · Seguros

Cohesión 0.15 · 59 nodos: Propuesta de proceso de referencia: siniestros en corredurías; Conversaciones con Coordinación sectorial · Seguros; Guion de validación semanal: apertura de siniestros; D-011 · Construir primero, clientes desde el 15/02/2027; Conversaciones con Arquitecto de procesos; Memoria de la oficina; Línea base y fichas de métricas · Atalaya; CCS · Consorcio de Compensación de Seguros: riesgos extraordinarios (y 51 más)

### 7 · knowledge/ingenieria · CEO digital y Responsable de cumplimiento normativo

Cohesión 0.11 · 46 nodos: CEO digital; Responsable de cumplimiento normativo; Especialista en ciberseguridad; Ingeniero de plataforma y operaciones (DevOps/SRE); Especialista legal y privacidad; Arquitecto de datos e IA; Responsable de decisiones y seguimiento; Bibliotecario / responsable de conocimiento (y 38 más)

### 8 · processes/catalog · P22 · Gestión de errores y reintentos y Catálogo de procesos P01–P38

Cohesión 0.5 · 37 nodos: P22 · Gestión de errores y reintentos; Catálogo de procesos P01–P38; P28 · Gestión de incidentes; P22 · Gestión de errores y reintentos; P27 · Gestión de proveedores y dependencias; P05 · Diseño del plan; P13 · Aprendizaje y actualización de la wiki; P25 · Gestión de cambios y versiones (y 29 más)

### 9 · docs/atlas · Guia de Arranque Proyecto v1.4 Diseno Cerrado y Flujo ceo

Cohesión 0.34 · 33 nodos: Guia de Arranque Proyecto v1.4 Diseno Cerrado; Flujo ceo; Ejecucion agentes; Motor conocimiento obsidian; Marco Integral Legal Ciberseguridad IA Espana UE 2026-11-16; 12 · Ciclo de vida de un proyecto con cliente; Comunicaciones estados; Calidad gobierno (y 25 más)

### 10 · knowledge/plantillas · Atlas Evolucion v1.1 Modelo Operativo Procesos y Despliegue y Matriz de aprobaciones · BORRADOR

Cohesión 0.2 · 33 nodos: Atlas Evolucion v1.1 Modelo Operativo Procesos y Despliegue; L0 (puerta técnica); Matriz de aprobaciones · BORRADOR; Plantillas de entregables al cliente (E1); Propuesta de diagnóstico · Atalaya Correduría de Seguros (FICTICIA); G2 (puerta de cliente); G6 (puerta de cliente); Rúbrica de calidad de entregables y listas de comprobación (C3) (y 25 más)

### 11 · knowledge/administracion-finanzas · Experto en asesorías, gestorías y despachos y Especialista en contabilidad y facturación

Cohesión 0.19 · 30 nodos: Experto en asesorías, gestorías y despachos; Especialista en contabilidad y facturación; Director financiero (CFO); Especialista administrativo; Finanzas: forma jurídica, facturación, precio y caja (D2); Especialista financiero; VERIFACTU-RDL43 · Real Decreto-ley 43/2026: aplazamiento de la adaptación de los sistemas informáticos de facturación (Verifactu); Experto en asesorías, gestorías y despachos (y 22 más)

### 12 · precedents/oficina · Acta de protección de la IA y examen de 50 casos y Conversaciones con IA y evaluación

Cohesión 0.52 · 12 nodos: Acta de protección de la IA y examen de 50 casos; L2 (puerta técnica); Conversaciones con IA y evaluación; Reunión: IA y evaluación y Seguridad; Conversaciones con CEO digital; Conversaciones con Registro de decisiones; Conversaciones con Plan y seguimiento; Conversaciones con Bibliotecario (y 4 más)

### 13 · knowledge/estudios · Estudios y Integraciones

Cohesión 0.52 · 7 nodos: Estudios; Integraciones; Contratos de datos; Estudio de prospectos: automatización para pymes (Álvaro, noviembre de 2026); Pruebas de integración; Conocimiento; Conectores

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

- **¿Por qué «Registro de fuentes» conecta la comunidad 2 con las comunidades 1, 3, 4, 5?**
  _Intermediación alta (0.156): es un puente entre temas._
- **¿Por qué «Registro de decisiones» conecta la comunidad 3 con las comunidades 1, 2, 4, 5?**
  _Intermediación alta (0.052): es un puente entre temas._
- **¿Por qué «Habilidades de los agentes» conecta la comunidad 1 con las comunidades 0, 4, 5, 6?**
  _Intermediación alta (0.039): es un puente entre temas._
- **¿Se aprueba D-019 · Calidad exigente, todo pasa por un socio y cada rechazo se rehace aprendiendo? Sigue en propuesta y la citan 22 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-024 · Paquete de dominio de seguros con un archivo máquina como fuente de las reglas? Sigue en propuesta y la citan 16 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-027 · Cada proceso tiene un nivel de autonomía A0–A4 con techo y criterio? Sigue en propuesta y la citan 14 secciones.**
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
