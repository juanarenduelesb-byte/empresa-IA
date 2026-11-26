<!-- Generado por tools/brain_build.py (tools/grafo.py). No editar a mano. -->
# Informe del grafo de conocimiento

Cómo está conectado el cerebro de Varios: qué sostiene todo, qué temas forman grupos, qué conecta temas distintos, qué falta y qué preguntas conviene hacerse. Se regenera con el cerebro (D-018); no forma parte del grafo.

## Resumen

- 4831 nodos: seccion 4148, documento 362, fuente 106, habilidad 65, proceso 38, especialista 34, agente 34, decision 25, puerta 12, departamento 7.
- 6517 relaciones: 61 % EXTRACTADAS (escritas en la fuente), 39 % INFERIDAS (temas compartidos, con puntuación) y 0 AMBIGUAS (para revisar).
- 13 comunidades de temas.

## Nodos centrales

Lo que más cosas conecta. Si cambia, cambia mucho.

1. **Registro de fuentes** (`knowledge/fuentes/registro.md`) · 190 conexiones
2. **Índice del conocimiento de Varios** (`knowledge/INDEX.md`) · 117 conexiones
3. **Registro de decisiones** (`DECISIONS.md`) · 104 conexiones
4. **Guia de Arranque Proyecto v1.4 Diseno Cerrado** (`docs/fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md`) · 84 conexiones
5. **Catálogo de procesos P01–P38** (`processes/catalog/README.md`) · 82 conexiones
6. **Habilidades de los agentes** (`claude/habilidades/README.md`) · 68 conexiones
7. **L2 (puerta técnica)** · 64 conexiones
8. **P22 · Gestión de errores y reintentos** · 62 conexiones
9. **P28 · Gestión de incidentes** · 61 conexiones
10. **Varios · empresa-ia** (`CLAUDE.md`) · 61 conexiones
11. **CEO digital** (`knowledge/direccion/ceo-digital.md`) · 60 conexiones
12. **Arquitecto de procesos** (`knowledge/procesos/arquitecto-procesos.md`) · 50 conexiones

## Puentes entre temas

Nodos por los que pasa el camino entre comunidades distintas (intermediación).

- **Registro de fuentes** · intermediación 0.254 · une la comunidad 1 con 2, 3, 4, 5, 6, 7
- **Registro de decisiones** · intermediación 0.098 · une la comunidad 6 con 1, 2, 3, 4, 5, 7
- **Habilidades de los agentes** · intermediación 0.082 · une la comunidad 2 con 3, 4, 5, 11
- **Índice del conocimiento de Varios** · intermediación 0.052 · une la comunidad 4 con 1, 3, 5, 6, 7, 8
- **L2 (puerta técnica)** · intermediación 0.052 · une la comunidad 6 con 1, 2, 3, 4, 5, 8
- **Guia de Arranque Proyecto v1.4 Diseno Cerrado** · intermediación 0.041 · une la comunidad 7 con 2, 3, 4, 6, 8, 9
- **CEO digital** · intermediación 0.025 · une la comunidad 3 con 1, 2, 4, 6, 7, 8
- **D-011 · Construir primero, clientes desde el 15/02/2027** · intermediación 0.023 · une la comunidad 5 con 1, 2, 4, 6, 7, 12
- **Administración** · intermediación 0.02 · une la comunidad 2 con 0, 1, 6, 9, 11
- **Experto en asesorías y despachos** · intermediación 0.019 · une la comunidad 2 con 0, 1, 6, 7, 11

## Conexiones sorprendentes

Secciones de carpetas y comunidades distintas que tratan lo mismo y no se enlazan. Relación INFERIDA: compruébala.

- `DECISIONS.md` › D-005 — Aislamiento multi-cliente  ↔  `docs/06-seguridad-y-gobierno.md` › Multi-tenancy  [INFERIDA 0.85]
- `integrations/tests/README.md` › Pruebas de integración  ↔  `knowledge/ingenieria/integraciones.md` › Especialista en integraciones  [INFERIDA 0.75]
- `claude/habilidades/contrato-de-tarea.md` › Pasos  ↔  `docs/03-ceo-digital-y-orquestacion.md` › Contrato de tarea  [INFERIDA 0.75]
- `knowledge/agentes/dat.md` › Reglas del puesto  ↔  `precedents/oficina/encargos/2026-11/2026-11-17-examen-de-25-casos-ficticios-para-atalaya-qq164.md` › Contrato de tarea del CEO  [INFERIDA 0.75]
- `knowledge/agentes/ingj.md` › Reglas del puesto  ↔  `processes/catalog/P01-alta-y-recepcion-de-peticion.md` › 7. Decisiones y reglas  [INFERIDA 0.75]
- `knowledge/agentes/kpi.md` › Reglas del puesto  ↔  `precedents/oficina/conversaciones/2026-11/2026-11-17-ceo-digital-a-metricas-sj6cp.md` › CEO digital → Métricas  [INFERIDA 0.75]
- `claude/habilidades/decision-registro.md` › Pasos  ↔  `knowledge/plantillas/entrada-decision.md` › D-0XX — Título  [INFERIDA 0.75]
- `knowledge/agentes/proj.md` › Con quién trabaja  ↔  `precedents/oficina/conversaciones/2026-11/2026-11-17-metricas-a-coordinacion-sectorial-seguros-utv9x.md` › Métricas → Coordinación sectorial · Seguros  [INFERIDA 0.75]
- `knowledge/agentes/seg.md` › Reglas del puesto  ↔  `precedents/oficina/encargos/2026-11/2026-11-17-propuesta-de-proceso-de-referencia-siniestros-en-c-tcpkm.md` › 7. Qué distingue práctica habitual de norma legal  [INFERIDA 0.75]
- `knowledge/direccion/bibliotecario.md` › Bibliotecario / responsable de conocimiento  ↔  `processes/catalog/P13-aprendizaje-y-actualizacion-de-la-wiki.md` › 20. Pruebas necesarias  [INFERIDA 0.75]

## Comunidades

### 0 · Habilidades · Legal y privacidad y Arquitecto de procesos

Cohesión 0.05 · 102 nodos: Legal y privacidad; Arquitecto de procesos; Seguridad; Coordinación sectorial · Seguros; Director financiero; Jefe comercial; Separar hecho, hipótesis y propuesta; Arquitecto técnico (y 94 más)

### 1 · knowledge/sectores · Registro de fuentes y Coordinación sectorial y seguros

Cohesión 0.07 · 99 nodos: Registro de fuentes; Coordinación sectorial y seguros; Experto en sanidad privada; Experto en servicios financieros no bancarios; Experto en asesorías, gestorías y despachos; Experto en logística y transporte; Especialista en contabilidad y facturación; Experto en industria manufacturera (y 91 más)

### 2 · claude/habilidades · Habilidades de los agentes y Administración

Cohesión 0.1 · 93 nodos: Habilidades de los agentes; Administración; Experto en asesorías y despachos; Backend; Agentes de la oficina; Arquitecto de procesos; Director financiero; Jefe comercial (y 85 más)

### 3 · knowledge/ingenieria · Dependencias entre procesos y CEO digital

Cohesión 0.14 · 75 nodos: Dependencias entre procesos; CEO digital; Especialista en ciberseguridad; Procesos y estados; P02 · Clasificación y triaje; Arquitecto de datos e IA; Responsable de decisiones y seguimiento; Bibliotecario / responsable de conocimiento (y 67 más)

### 4 · processes/catalog · Índice del conocimiento de Varios y Arquitecto de procesos

Cohesión 0.13 · 61 nodos: Índice del conocimiento de Varios; Arquitecto de procesos; P32 · Descubrimiento de procesos; P33 · Diseño y validación TO-BE; Director comercial; P38 · Gestión de despliegue por cliente; Biblioteca de precedentes; P31 · Calificación de oportunidad (y 53 más)

### 5 · precedents/oficina · Propuesta de proceso de referencia: siniestros en corredurías y Conversaciones con Coordinación sectorial · Seguros

Cohesión 0.15 · 60 nodos: Propuesta de proceso de referencia: siniestros en corredurías; Conversaciones con Coordinación sectorial · Seguros; Guion de validación semanal: apertura de siniestros; Conversaciones con Arquitecto de procesos; Memoria de la oficina; D-011 · Construir primero, clientes desde el 15/02/2027; Línea base y fichas de métricas · Atalaya; CCS · Consorcio de Compensación de Seguros: riesgos extraordinarios (y 52 más)

### 6 · docs · Acta de protección de la IA y examen de 50 casos y Registro de decisiones

Cohesión 0.13 · 52 nodos: Acta de protección de la IA y examen de 50 casos; L2 (puerta técnica); Registro de decisiones; Conversaciones con IA y evaluación; Varios · empresa-ia; Reunión: IA y evaluación y Seguridad; Conversaciones con CEO digital; 17 · Cerebro, conocimiento y procesos: auditoría e informe (y 44 más)

### 7 · docs/atlas · Guia de Arranque Proyecto v1.4 Diseno Cerrado y Atlas Evolucion v1.1 Modelo Operativo Procesos y Despliegue

Cohesión 0.22 · 46 nodos: Guia de Arranque Proyecto v1.4 Diseno Cerrado; Atlas Evolucion v1.1 Modelo Operativo Procesos y Despliegue; Ejecucion agentes; Flujo ceo; Motor conocimiento obsidian; Marco Integral Legal Ciberseguridad IA Espana UE 2026-11-16; Varios — repositorio maestro; Comunicaciones estados (y 38 más)

### 8 · processes/catalog · P22 · Gestión de errores y reintentos y Catálogo de procesos P01–P38

Cohesión 0.44 · 40 nodos: P22 · Gestión de errores y reintentos; Catálogo de procesos P01–P38; P28 · Gestión de incidentes; P22 · Gestión de errores y reintentos; P27 · Gestión de proveedores y dependencias; P05 · Diseño del plan; P11 · Entrega y cierre; P13 · Aprendizaje y actualización de la wiki (y 32 más)

### 9 · knowledge/administracion-finanzas · Director financiero (CFO) y P29 · Gestión de costes y capacidad

Cohesión 0.27 · 17 nodos: Director financiero (CFO); P29 · Gestión de costes y capacidad; Especialista en costes y proveedores; P27 · Gestión de proveedores y dependencias; Especialista financiero; Especialista en costes y proveedores; PGC-PYMES · Real Decreto 1515/2007, Plan General de Contabilidad de Pymes; Administración y finanzas (y 9 más)

### 10 · knowledge/seguridad-legal · Responsable de cumplimiento normativo y Especialista legal y privacidad

Cohesión 0.25 · 16 nodos: Responsable de cumplimiento normativo; Especialista legal y privacidad; Diseñador de producto y experiencia (UX); P19 · Política de uso y límites; Responsable de cumplimiento normativo; Especialista legal y privacidad; UE-RIA-OMNIBUS · Reglamento (UE) 2026/1744 (ómnibus digital sobre IA), que modifica el Reglamento (UE) 2024/1689; LEY-ACCESIBILIDAD-11-2023 · Ley 11/2023 (accesibilidad de productos y servicios, transpone la Directiva (UE) 2019/882) (y 8 más)

### 11 · claude/habilidades · Ingeniero de plataforma y operaciones (DevOps/SRE) y Plataforma y operaciones

Cohesión 0.17 · 16 nodos: Ingeniero de plataforma y operaciones (DevOps/SRE); Plataforma y operaciones; Ingeniero de plataforma y operaciones (DevOps/SRE); ENS-RD311 · Real Decreto 311/2022, Esquema Nacional de Seguridad; OTEL-GENAI · OpenTelemetry: convenciones semánticas para IA generativa; Observabilidad y alertas; DORA-DEVOPS · Métricas DORA de entrega de software (DevOps Research and Assessment); GOOGLE-SRE · Site Reliability Engineering (libros de Google SRE) (y 8 más)

### 12 · integrations · Integraciones y Contratos de datos

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
  _Intermediación alta (0.254): es un puente entre temas._
- **¿Por qué «Registro de decisiones» conecta la comunidad 6 con las comunidades 1, 2, 3, 4?**
  _Intermediación alta (0.098): es un puente entre temas._
- **¿Por qué «Habilidades de los agentes» conecta la comunidad 2 con las comunidades 3, 4, 5, 11?**
  _Intermediación alta (0.082): es un puente entre temas._
- **¿Se aprueba D-013 · Conocimiento y catálogo de procesos generados desde datos? Sigue en propuesta y la citan 12 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-017 · La oficina se vuelca cada noche a GitHub y las automatizaciones van por GitHub Actions? Sigue en propuesta y la citan 11 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-019 · Calidad exigente, todo pasa por un socio y cada rechazo se rehace aprendiendo? Sigue en propuesta y la citan 7 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Deberían enlazarse «DECISIONS.md» y «docs/06-seguridad-y-gobierno.md»?**
  _Tratan lo mismo (relación INFERIDA 0.85) pero no se citan._
- **¿Deberían enlazarse «integrations/tests/README.md» y «knowledge/ingenieria/integraciones.md»?**
  _Tratan lo mismo (relación INFERIDA 0.75) pero no se citan._
- **¿Siguen vigentes D-008, D-016, D-020? Ningún documento las cita.**
  _Decisiones que nadie menciona._

## Cómo usarlo

- En la oficina, cada agente recibe las secciones que encajan con su encargo **y lo conectado a ellas** (decisiones, procesos, fuentes y secciones relacionadas), con la etiqueta de confianza de cada relación.
- En local: `python3 tools/grafo.py consulta "pregunta"`, `camino "A" "B"` y `explica "X"`.
- Las relaciones INFERIDAS son pistas, no hechos: si una es buena, conviértela en un enlace en el documento y pasará a EXTRACTADA.
