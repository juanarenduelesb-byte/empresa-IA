<!-- Generado por tools/brain_build.py (tools/grafo.py). No editar a mano. -->
# Informe del grafo de conocimiento

Cómo está conectado el cerebro de Varios: qué sostiene todo, qué temas forman grupos, qué conecta temas distintos, qué falta y qué preguntas conviene hacerse. Se regenera con el cerebro (D-018); no forma parte del grafo.

## Resumen

- 3814 nodos: seccion 3251, documento 284, fuente 68, habilidad 65, proceso 38, especialista 34, agente 34, decision 21, puerta 12, departamento 7.
- 4774 relaciones: 70 % EXTRACTADAS (escritas en la fuente), 30 % INFERIDAS (temas compartidos, con puntuación) y 0 AMBIGUAS (para revisar).
- 14 comunidades de temas.

## Nodos centrales

Lo que más cosas conecta. Si cambia, cambia mucho.

1. **Registro de fuentes** (`knowledge/fuentes/registro.md`) · 132 conexiones
2. **Índice del conocimiento de Varios** (`knowledge/INDEX.md`) · 117 conexiones
3. **Registro de decisiones** (`DECISIONS.md`) · 86 conexiones
4. **Guia de Arranque Proyecto v1.4 Diseno Cerrado** (`docs/fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md`) · 82 conexiones
5. **Catálogo de procesos P01–P38** (`processes/catalog/README.md`) · 82 conexiones
6. **Habilidades de los agentes** (`claude/habilidades/README.md`) · 68 conexiones
7. **P22 · Gestión de errores y reintentos** · 61 conexiones
8. **P28 · Gestión de incidentes** · 61 conexiones
9. **CEO digital** (`knowledge/direccion/ceo-digital.md`) · 52 conexiones
10. **Varios · empresa-ia** (`CLAUDE.md`) · 51 conexiones
11. **Especialista en ciberseguridad** (`knowledge/seguridad-legal/ciberseguridad.md`) · 50 conexiones
12. **Arquitecto de procesos** (`knowledge/procesos/arquitecto-procesos.md`) · 48 conexiones

## Puentes entre temas

Nodos por los que pasa el camino entre comunidades distintas (intermediación).

- **Registro de fuentes** · intermediación 0.163 · une la comunidad 5 con 1, 2, 3, 4, 6, 7
- **Habilidades de los agentes** · intermediación 0.109 · une la comunidad 1 con 0, 2, 7, 10, 11
- **Registro de decisiones** · intermediación 0.098 · une la comunidad 8 con 1, 2, 3, 5, 6, 7
- **Índice del conocimiento de Varios** · intermediación 0.064 · une la comunidad 13 con 2, 3, 4, 5, 6, 7
- **Guia de Arranque Proyecto v1.4 Diseno Cerrado** · intermediación 0.056 · une la comunidad 3 con 0, 2, 4, 5, 6, 7
- **L2 (puerta técnica)** · intermediación 0.027 · une la comunidad 1 con 2, 4, 6, 7, 8, 9
- **P31 · Calificación de oportunidad** · intermediación 0.026 · une la comunidad 7 con 0, 1, 2, 3, 4, 5
- **CEO digital** · intermediación 0.022 · une la comunidad 12 con 1, 2, 3, 4, 5, 6
- **Administración** · intermediación 0.022 · une la comunidad 1 con 0, 5, 7, 10, 11
- **Experto en asesorías y despachos** · intermediación 0.022 · une la comunidad 1 con 0, 3, 5, 7, 10, 11

## Conexiones sorprendentes

Secciones de carpetas y comunidades distintas que tratan lo mismo y no se enlazan. Relación INFERIDA: compruébala.

- `DECISIONS.md` › D-005 — Aislamiento multi-cliente  ↔  `docs/06-seguridad-y-gobierno.md` › Multi-tenancy  [INFERIDA 0.85]
- `claude/habilidades/contrato-de-tarea.md` › Pasos  ↔  `docs/03-ceo-digital-y-orquestacion.md` › Contrato de tarea  [INFERIDA 0.75]
- `claude/habilidades/cualificacion-oportunidad.md` › Cualificación de oportunidad  ↔  `knowledge/comercial/director-comercial.md` › Responsabilidades  [INFERIDA 0.75]
- `claude/habilidades/decision-registro.md` › Pasos  ↔  `knowledge/plantillas/entrada-decision.md` › D-0XX — Título  [INFERIDA 0.75]
- `knowledge/agentes/seg.md` › Coordinación sectorial · Seguros  ↔  `processes/referencia-seguros-apertura-siniestros/README.md` › Seguros · Apertura de siniestros en corredurías (proceso de referencia)  [INFERIDA 0.75]
- `knowledge/direccion/README.md` › Dirección y gobierno  ↔  `processes/diagrams/dependencias.md` › Dependencias entre procesos  [INFERIDA 0.75]
- `knowledge/direccion/ceo-digital.md` › Límites de actuación  ↔  `processes/catalog/P10-aprobacion-humana.md` › 7. Decisiones y reglas  [INFERIDA 0.75]
- `knowledge/ingenieria/evaluacion-ia.md` › Especialista en evaluación de IA  ↔  `processes/catalog/P23-evaluacion-de-agentes-y-modelos.md` › 20. Pruebas necesarias  [INFERIDA 0.75]
- `claude/habilidades/ficha-proveedor.md` › Pasos  ↔  `knowledge/plantillas/ficha-proveedor.md` › Proveedor: <nombre>  [INFERIDA 0.75]
- `knowledge/sectores/priorizacion.md` › Priorización de sectores  ↔  `processes/templates/proceso-cliente.md` › <sector> · <proceso>  [INFERIDA 0.75]

## Comunidades

### 0 · claude/habilidades · Legal y privacidad y Arquitecto de procesos

Cohesión 0.05 · 109 nodos: Legal y privacidad; Arquitecto de procesos; Seguridad; Coordinación sectorial · Seguros; Director financiero; Jefe comercial; Separar hecho, hipótesis y propuesta; Arquitecto técnico (y 101 más)

### 1 · claude/habilidades · Habilidades de los agentes y Administración

Cohesión 0.11 · 85 nodos: Habilidades de los agentes; Administración; Experto en asesorías y despachos; L2 (puerta técnica); Backend; Agentes de la oficina; Jefe comercial; Contabilidad y facturación (y 77 más)

### 2 · knowledge/ingenieria · Dependencias entre procesos y Especialista en ciberseguridad

Cohesión 0.16 · 57 nodos: Dependencias entre procesos; Especialista en ciberseguridad; Procesos y estados; Arquitecto de datos e IA; Biblioteca de precedentes; Especialista en automatización; Especialista en calidad y riesgos; Arquitecto técnico (y 49 más)

### 3 · docs/atlas · Guia de Arranque Proyecto v1.4 Diseno Cerrado y Flujo ceo

Cohesión 0.22 · 46 nodos: Guia de Arranque Proyecto v1.4 Diseno Cerrado; Flujo ceo; Ejecucion agentes; Atlas Evolucion v1.1 Modelo Operativo Procesos y Despliegue; Motor conocimiento obsidian; Comunicaciones estados; 12 · Ciclo de vida de un proyecto con cliente; Seguridad clientes (y 38 más)

### 4 · processes/catalog · P22 · Gestión de errores y reintentos y Catálogo de procesos P01–P38

Cohesión 0.41 · 40 nodos: P22 · Gestión de errores y reintentos; Catálogo de procesos P01–P38; P28 · Gestión de incidentes; P22 · Gestión de errores y reintentos; P27 · Gestión de proveedores y dependencias; P05 · Diseño del plan; P02 · Clasificación y triaje; P11 · Entrega y cierre (y 32 más)

### 5 · knowledge/administracion-finanzas · Registro de fuentes y Experto en asesorías, gestorías y despachos

Cohesión 0.18 · 37 nodos: Registro de fuentes; Experto en asesorías, gestorías y despachos; Especialista en contabilidad y facturación; Director financiero (CFO); P29 · Gestión de costes y capacidad; Especialista en costes y proveedores; P27 · Gestión de proveedores y dependencias; Especialista administrativo (y 29 más)

### 6 · knowledge/sectores · Coordinación sectorial y seguros y Experto en sanidad privada

Cohesión 0.18 · 37 nodos: Coordinación sectorial y seguros; Experto en sanidad privada; Experto en servicios financieros no bancarios; Experto en logística y transporte; P32 · Descubrimiento de procesos; Experto en industria manufacturera; P02 · Clasificación y triaje; P33 · Diseño y validación TO-BE (y 29 más)

### 7 · knowledge/comercial · Varios · empresa-ia y P38 · Gestión de despliegue por cliente

Cohesión 0.16 · 37 nodos: Varios · empresa-ia; P38 · Gestión de despliegue por cliente; Director comercial; P31 · Calificación de oportunidad; Especialista en éxito de cliente; INT-ATLAS · Atlas Evolución v1.1 · modelo operativo, procesos y despliegue; P37 · Medición de rendimiento y valor; Responsable de implantación de clientes (y 29 más)

### 8 · docs · Registro de decisiones y 17 · Cerebro, conocimiento y procesos: auditoría e informe

Cohesión 0.12 · 32 nodos: Registro de decisiones; 17 · Cerebro, conocimiento y procesos: auditoría e informe; Plan de construcción · 18/11/2026 → 12/02/2027; Obsidian: el cerebro abierto en tu equipo; L0 (puerta técnica); Glosario; Inicio · cerebro de Varios; L4 (puerta técnica) (y 24 más)

### 9 · processes/catalog · Arquitecto de procesos y P33 · Diseño y validación TO-BE

Cohesión 0.24 · 23 nodos: Arquitecto de procesos; P33 · Diseño y validación TO-BE; P32 · Descubrimiento de procesos; P38 · Gestión de despliegue por cliente; P37 · Medición de rendimiento y valor; P31 · Calificación de oportunidad; P34 · Gestión de definiciones de proceso; P34 · Gestión de definiciones de proceso (y 15 más)

### 10 · claude/habilidades · Responsable de cumplimiento normativo y Especialista legal y privacidad

Cohesión 0.2 · 18 nodos: Responsable de cumplimiento normativo; Especialista legal y privacidad; Diseñador de producto y experiencia (UX); Cumplimiento normativo; Responsable de cumplimiento normativo; UE-RIA-OMNIBUS · Reglamento (UE) 2026/1744 (ómnibus digital sobre IA), que modifica el Reglamento (UE) 2024/1689; LEY-ACCESIBILIDAD-11-2023 · Ley 11/2023 (accesibilidad de productos y servicios, transpone la Directiva (UE) 2019/882); NIS2-ES · Estado de la transposición de NIS2 en España (y 10 más)

### 11 · claude/habilidades · Ingeniero de plataforma y operaciones (DevOps/SRE) y Plataforma y operaciones

Cohesión 0.21 · 14 nodos: Ingeniero de plataforma y operaciones (DevOps/SRE); Plataforma y operaciones; Ingeniero de plataforma y operaciones (DevOps/SRE); ENS-RD311 · Real Decreto 311/2022, Esquema Nacional de Seguridad; ISO-27001 · ISO/IEC 27001:2022 (transición desde 2013 terminada el 31/10/2025); OTEL-GENAI · OpenTelemetry: convenciones semánticas para IA generativa; DORA-DEVOPS · Métricas DORA de entrega de software (DevOps Research and Assessment); GOOGLE-SRE · Site Reliability Engineering (libros de Google SRE) (y 6 más)

### 12 · knowledge/direccion · CEO digital y Responsable de decisiones y seguimiento

Cohesión 0.36 · 14 nodos: CEO digital; Responsable de decisiones y seguimiento; Bibliotecario / responsable de conocimiento; P11 · Entrega y cierre; P01 · Alta y recepción de petición; P05 · Diseño del plan; Dirección y gobierno; CEO digital (y 6 más)

### 13 · knowledge/plantillas · Índice del conocimiento de Varios y Plantillas

Cohesión 0.27 · 12 nodos: Índice del conocimiento de Varios; Plantillas; Catálogo de integraciones; Protocolo: consultar el histórico antes de empezar; Protocolo: guardar el conocimiento; Metodologías transversales; Proveedor: <nombre>; <título> (y 4 más)

## Huecos

- **Documentos sin ninguna relación** (2): `precedents/projects/2026-11-oficina-de-agentes.md`; `precedents/solutions/busqueda-texto-cerebro.md`
- **Decisiones que no cita ninguna sección** (3): D-008, D-016, D-020
- **Procesos sin especialista responsable** (0): ninguno
- **Fuentes registradas que nadie cita** (0): ninguna
- **Referencias rotas** (se citan pero no existen): ninguna
- **Enlaces ambiguos** (un nombre de archivo con varios destinos): 0

## Preguntas sugeridas

_Preguntas que este grafo ayuda a responder o que conviene decidir:_

- **¿Por qué «Registro de fuentes» conecta la comunidad 5 con las comunidades 1, 2, 3, 4?**
  _Intermediación alta (0.163): es un puente entre temas._
- **¿Por qué «Habilidades de los agentes» conecta la comunidad 1 con las comunidades 0, 2, 7, 10?**
  _Intermediación alta (0.109): es un puente entre temas._
- **¿Por qué «Registro de decisiones» conecta la comunidad 8 con las comunidades 1, 2, 3, 5?**
  _Intermediación alta (0.098): es un puente entre temas._
- **¿Se aprueba D-014 · Adelantar un prototipo mínimo del motor de procesos? Sigue en propuesta y la citan 3 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-018 · El cerebro pasa a ser un grafo de conocimiento con relaciones explicadas? Sigue en propuesta y la citan 3 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-021 · El cerebro se abre en Obsidian: el repositorio es el vault? Sigue en propuesta y la citan 3 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Deberían enlazarse «DECISIONS.md» y «docs/06-seguridad-y-gobierno.md»?**
  _Tratan lo mismo (relación INFERIDA 0.85) pero no se citan._
- **¿Deberían enlazarse «claude/habilidades/contrato-de-tarea.md» y «docs/03-ceo-digital-y-orquestacion.md»?**
  _Tratan lo mismo (relación INFERIDA 0.75) pero no se citan._
- **¿Siguen vigentes D-008, D-016, D-020? Ningún documento las cita.**
  _Decisiones que nadie menciona._

## Cómo usarlo

- En la oficina, cada agente recibe las secciones que encajan con su encargo **y lo conectado a ellas** (decisiones, procesos, fuentes y secciones relacionadas), con la etiqueta de confianza de cada relación.
- En local: `python3 tools/grafo.py consulta "pregunta"`, `camino "A" "B"` y `explica "X"`.
- Las relaciones INFERIDAS son pistas, no hechos: si una es buena, conviértela en un enlace en el documento y pasará a EXTRACTADA.
