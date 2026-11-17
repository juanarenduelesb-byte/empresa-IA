<!-- Generado por tools/brain_build.py (tools/grafo.py). No editar a mano. -->
# Informe del grafo de conocimiento

Cómo está conectado el cerebro de Varios: qué sostiene todo, qué temas forman grupos, qué conecta temas distintos, qué falta y qué preguntas conviene hacerse. Se regenera con el cerebro (D-018); no forma parte del grafo.

## Resumen

- 3406 nodos: seccion 2922, documento 252, fuente 53, habilidad 45, proceso 38, especialista 30, agente 28, decision 19, puerta 12, departamento 7.
- 4199 relaciones: 70 % EXTRACTADAS (escritas en la fuente), 30 % INFERIDAS (temas compartidos, con puntuación) y 0 AMBIGUAS (para revisar).
- 13 comunidades de temas.

## Nodos centrales

Lo que más cosas conecta. Si cambia, cambia mucho.

1. **Índice del conocimiento de Varios** (`knowledge/INDEX.md`) · 113 conexiones
2. **Registro de fuentes** (`knowledge/fuentes/registro.md`) · 113 conexiones
3. **Guia de Arranque Proyecto v1.4 Diseno Cerrado** (`docs/fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md`) · 83 conexiones
4. **Catálogo de procesos P01–P38** (`processes/catalog/README.md`) · 82 conexiones
5. **Registro de decisiones** (`DECISIONS.md`) · 77 conexiones
6. **P22 · Gestión de errores y reintentos** · 61 conexiones
7. **P28 · Gestión de incidentes** · 58 conexiones
8. **Especialista en ciberseguridad** (`knowledge/seguridad-legal/ciberseguridad.md`) · 49 conexiones
9. **Habilidades de los agentes** (`claude/habilidades/README.md`) · 48 conexiones
10. **CEO digital** (`knowledge/direccion/ceo-digital.md`) · 48 conexiones
11. **Varios · empresa-ia** (`CLAUDE.md`) · 47 conexiones
12. **P22 · Gestión de errores y reintentos** (`processes/catalog/P22-gestion-de-errores-y-reintentos.md`) · 47 conexiones

## Puentes entre temas

Nodos por los que pasa el camino entre comunidades distintas (intermediación).

- **Registro de fuentes** · intermediación 0.15 · une la comunidad 3 con 1, 2, 4, 5, 6, 7
- **Registro de decisiones** · intermediación 0.09 · une la comunidad 2 con 1, 3, 5, 6, 7, 9
- **Habilidades de los agentes** · intermediación 0.082 · une la comunidad 1 con 2, 6, 7, 8
- **Índice del conocimiento de Varios** · intermediación 0.074 · une la comunidad 6 con 2, 3, 4, 5, 7, 8
- **Guia de Arranque Proyecto v1.4 Diseno Cerrado** · intermediación 0.068 · une la comunidad 5 con 2, 3, 4, 6, 7, 8
- **L2 (puerta técnica)** · intermediación 0.029 · une la comunidad 1 con 2, 3, 7, 8, 10
- **P31 · Calificación de oportunidad** · intermediación 0.028 · une la comunidad 6 con 1, 2, 3, 4, 7, 8
- **Arquitecto de procesos** · intermediación 0.024 · une la comunidad 0 con 1, 6, 10, 11
- **CEO digital** · intermediación 0.024 · une la comunidad 9 con 1, 2, 3, 4, 5, 6
- **Administración** · intermediación 0.023 · une la comunidad 1 con 0, 3, 11

## Conexiones sorprendentes

Secciones de carpetas y comunidades distintas que tratan lo mismo y no se enlazan. Relación INFERIDA: compruébala.

- `claude/habilidades/ficha-metrica.md` › Pasos  ↔  `knowledge/plantillas/ficha-kpi.md` › KPI: <nombre>  [INFERIDA 0.85]
- `docs/fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md` › 4.1 Reintentos y operaciones duplicadas  ↔  `processes/catalog/P22-gestion-de-errores-y-reintentos.md` › 9. Entradas y salidas de cada tarea  [INFERIDA 0.85]
- `claude/habilidades/decision-registro.md` › Pasos  ↔  `knowledge/plantillas/entrada-decision.md` › D-0XX — Título  [INFERIDA 0.75]
- `knowledge/agentes/seg.md` › Coordinación sectorial · Seguros  ↔  `processes/referencia-seguros-apertura-siniestros/README.md` › Seguros · Apertura de siniestros en corredurías (proceso de referencia)  [INFERIDA 0.75]
- `knowledge/direccion/README.md` › Dirección y gobierno  ↔  `processes/diagrams/dependencias.md` › Dependencias entre procesos  [INFERIDA 0.75]
- `knowledge/direccion/ceo-digital.md` › Límites de actuación  ↔  `processes/catalog/P10-aprobacion-humana.md` › 7. Decisiones y reglas  [INFERIDA 0.75]
- `claude/habilidades/ficha-metrica.md` › Pasos  ↔  `knowledge/procesos/metricas.md` › Responsabilidades  [INFERIDA 0.75]
- `claude/habilidades/ficha-proveedor.md` › Pasos  ↔  `knowledge/plantillas/ficha-proveedor.md` › Proveedor: <nombre>  [INFERIDA 0.75]
- `knowledge/sectores/priorizacion.md` › Priorización de sectores  ↔  `processes/templates/proceso-cliente.md` › <sector> · <proceso>  [INFERIDA 0.75]
- `knowledge/seguridad-legal/legal-privacidad.md` › Responsabilidades  ↔  `processes/templates/proceso-cliente.md` › 4. Riesgo  [INFERIDA 0.75]

## Comunidades

### 0 · Habilidades · Legal y privacidad y Arquitecto de procesos

Cohesión 0.06 · 79 nodos: Legal y privacidad; Arquitecto de procesos; Seguridad; Coordinación sectorial · Seguros; Jefe comercial; CEO digital; IA y evaluación; Arquitecto técnico (y 71 más)

### 1 · claude/habilidades · Habilidades de los agentes y Administración

Cohesión 0.13 · 74 nodos: Habilidades de los agentes; Administración; Experto en asesorías y despachos; L2 (puerta técnica); Backend; Agentes de la oficina; Jefe comercial; Arquitecto de procesos (y 66 más)

### 2 · docs · Registro de decisiones y Atlas Evolucion v1.1 Modelo Operativo Procesos y Despliegue

Cohesión 0.07 · 61 nodos: Registro de decisiones; Atlas Evolucion v1.1 Modelo Operativo Procesos y Despliegue; 17 · Cerebro, conocimiento y procesos: auditoría e informe; P01 · Alta y recepción de petición; Varios — repositorio maestro; Roadmap y decisiones; Plantillas; Plan de construcción · 18/11/2026 → 12/02/2027 (y 53 más)

### 3 · knowledge/sectores · Registro de fuentes y Experto en sanidad privada

Cohesión 0.14 · 58 nodos: Registro de fuentes; Experto en sanidad privada; Coordinación sectorial y seguros; Experto en asesorías, gestorías y despachos; Experto en logística y transporte; Especialista legal y privacidad; Experto en servicios financieros no bancarios; P32 · Descubrimiento de procesos (y 50 más)

### 4 · processes/catalog · P22 · Gestión de errores y reintentos y Catálogo de procesos P01–P38

Cohesión 0.48 · 36 nodos: P22 · Gestión de errores y reintentos; Catálogo de procesos P01–P38; P28 · Gestión de incidentes; P22 · Gestión de errores y reintentos; P27 · Gestión de proveedores y dependencias; P05 · Diseño del plan; P11 · Entrega y cierre; P02 · Clasificación y triaje (y 28 más)

### 5 · docs/atlas · Guia de Arranque Proyecto v1.4 Diseno Cerrado y Ejecucion agentes

Cohesión 0.33 · 34 nodos: Guia de Arranque Proyecto v1.4 Diseno Cerrado; Ejecucion agentes; Flujo ceo; Motor conocimiento obsidian; Comunicaciones estados; Seguridad clientes; 12 · Ciclo de vida de un proyecto con cliente; Registro de correcciones a los documentos recibidos el 17/11/2026 (y 26 más)

### 6 · knowledge/comercial · Índice del conocimiento de Varios y Varios · empresa-ia

Cohesión 0.26 · 29 nodos: Índice del conocimiento de Varios; Varios · empresa-ia; P38 · Gestión de despliegue por cliente; Director comercial; P31 · Calificación de oportunidad; INT-ATLAS · Atlas Evolución v1.1 · modelo operativo, procesos y despliegue; Responsable de implantación de clientes; P11 · Entrega y cierre (y 21 más)

### 7 · knowledge/ingenieria · Especialista en ciberseguridad y Arquitecto de datos e IA

Cohesión 0.2 · 27 nodos: Especialista en ciberseguridad; Arquitecto de datos e IA; Arquitecto técnico; Especialista en calidad y riesgos; Biblioteca de precedentes; Especialista backend; Especialista en evaluación de IA; Especialista en integraciones (y 19 más)

### 8 · processes/runbooks · Dependencias entre procesos y Procesos y estados

Cohesión 0.29 · 26 nodos: Dependencias entre procesos; Procesos y estados; P21 · Ejecución segura de herramientas; P30 · Gestión de identidades y secretos; P10 · Aprobación humana; P15 · Observabilidad e incidencias; P07 · Ingesta documental; P08 · Ejecución de tareas (y 18 más)

### 9 · knowledge/direccion · CEO digital y Responsable de decisiones y seguimiento

Cohesión 0.26 · 19 nodos: CEO digital; Responsable de decisiones y seguimiento; Bibliotecario / responsable de conocimiento; P04 · Recuperación de conocimiento; P13 · Aprendizaje y actualización de la wiki; P12 · Gestión de cambios; P05 · Diseño del plan; P25 · Gestión de cambios y versiones (y 11 más)

### 10 · processes/catalog · Arquitecto de procesos y P33 · Diseño y validación TO-BE

Cohesión 0.31 · 19 nodos: Arquitecto de procesos; P33 · Diseño y validación TO-BE; P32 · Descubrimiento de procesos; P38 · Gestión de despliegue por cliente; P37 · Medición de rendimiento y valor; P31 · Calificación de oportunidad; P34 · Gestión de definiciones de proceso; P34 · Gestión de definiciones de proceso (y 11 más)

### 11 · knowledge/administracion-finanzas · Especialista en automatización y P29 · Gestión de costes y capacidad

Cohesión 0.27 · 16 nodos: Especialista en automatización; P29 · Gestión de costes y capacidad; Especialista en costes y proveedores; P27 · Gestión de proveedores y dependencias; Especialista financiero; Especialista en automatización; Especialista en costes y proveedores; Administración y finanzas (y 8 más)

### 12 · precedents/projects · Caso de práctica · Atalaya Correduría de Seguros (ficticia) y Ficha del cliente · Atalaya Correduría de Seguros (FICTICIA)

Cohesión 1.0 · 4 nodos: Caso de práctica · Atalaya Correduría de Seguros (ficticia); Ficha del cliente · Atalaya Correduría de Seguros (FICTICIA); Notas de la sesión de arranque · proceso actual de apertura de siniestros (FICTICIO); Sistemas, datos y restricciones · Atalaya (FICTICIO)

## Huecos

- **Documentos sin ninguna relación** (2): `precedents/projects/2026-11-oficina-de-agentes.md`; `precedents/solutions/busqueda-texto-cerebro.md`
- **Decisiones que no cita ninguna sección** (2): D-008, D-016
- **Procesos sin especialista responsable** (0): ninguno
- **Fuentes registradas que nadie cita** (0): ninguna
- **Referencias rotas** (se citan pero no existen): ninguna
- **Enlaces ambiguos** (un nombre de archivo con varios destinos): 0

## Preguntas sugeridas

_Preguntas que este grafo ayuda a responder o que conviene decidir:_

- **¿Por qué «Registro de fuentes» conecta la comunidad 3 con las comunidades 1, 2, 4, 5?**
  _Intermediación alta (0.15): es un puente entre temas._
- **¿Por qué «Registro de decisiones» conecta la comunidad 2 con las comunidades 1, 3, 5, 6?**
  _Intermediación alta (0.09): es un puente entre temas._
- **¿Por qué «Habilidades de los agentes» conecta la comunidad 1 con las comunidades 2, 6, 7, 8?**
  _Intermediación alta (0.082): es un puente entre temas._
- **¿Se aprueba D-014 · Adelantar un prototipo mínimo del motor de procesos? Sigue en propuesta y la citan 3 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Deberían enlazarse «claude/habilidades/ficha-metrica.md» y «knowledge/plantillas/ficha-kpi.md»?**
  _Tratan lo mismo (relación INFERIDA 0.85) pero no se citan._
- **¿Deberían enlazarse «docs/fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md» y «processes/catalog/P22-gestion-de-errores-y-reintentos.md»?**
  _Tratan lo mismo (relación INFERIDA 0.85) pero no se citan._
- **¿Siguen vigentes D-008, D-016? Ningún documento las cita.**
  _Decisiones que nadie menciona._

## Cómo usarlo

- En la oficina, cada agente recibe las secciones que encajan con su encargo **y lo conectado a ellas** (decisiones, procesos, fuentes y secciones relacionadas), con la etiqueta de confianza de cada relación.
- En local: `python3 tools/grafo.py consulta "pregunta"`, `camino "A" "B"` y `explica "X"`.
- Las relaciones INFERIDAS son pistas, no hechos: si una es buena, conviértela en un enlace en el documento y pasará a EXTRACTADA.
