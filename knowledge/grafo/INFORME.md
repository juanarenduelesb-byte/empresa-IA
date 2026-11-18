<!-- Generado por tools/brain_build.py (tools/grafo.py). No editar a mano. -->
# Informe del grafo de conocimiento

Cómo está conectado el cerebro de Varios: qué sostiene todo, qué temas forman grupos, qué conecta temas distintos, qué falta y qué preguntas conviene hacerse. Se regenera con el cerebro (D-018); no forma parte del grafo.

## Resumen

- 3827 nodos: seccion 3258, documento 290, fuente 68, habilidad 65, proceso 38, especialista 34, agente 34, decision 21, puerta 12, departamento 7.
- 4799 relaciones: 70 % EXTRACTADAS (escritas en la fuente), 30 % INFERIDAS (temas compartidos, con puntuación) y 0 AMBIGUAS (para revisar).
- 15 comunidades de temas.

## Nodos centrales

Lo que más cosas conecta. Si cambia, cambia mucho.

1. **Registro de fuentes** (`knowledge/fuentes/registro.md`) · 133 conexiones
2. **Índice del conocimiento de Varios** (`knowledge/INDEX.md`) · 117 conexiones
3. **Registro de decisiones** (`DECISIONS.md`) · 86 conexiones
4. **Guia de Arranque Proyecto v1.4 Diseno Cerrado** (`docs/fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md`) · 83 conexiones
5. **Catálogo de procesos P01–P38** (`processes/catalog/README.md`) · 82 conexiones
6. **Habilidades de los agentes** (`claude/habilidades/README.md`) · 68 conexiones
7. **P22 · Gestión de errores y reintentos** · 61 conexiones
8. **P28 · Gestión de incidentes** · 61 conexiones
9. **Varios · empresa-ia** (`CLAUDE.md`) · 57 conexiones
10. **CEO digital** (`knowledge/direccion/ceo-digital.md`) · 54 conexiones
11. **Especialista en ciberseguridad** (`knowledge/seguridad-legal/ciberseguridad.md`) · 50 conexiones
12. **Arquitecto de procesos** (`knowledge/procesos/arquitecto-procesos.md`) · 48 conexiones

## Puentes entre temas

Nodos por los que pasa el camino entre comunidades distintas (intermediación).

- **Registro de fuentes** · intermediación 0.165 · une la comunidad 3 con 1, 2, 4, 5, 6, 7
- **Habilidades de los agentes** · intermediación 0.107 · une la comunidad 1 con 0, 3, 4, 6, 8, 9
- **Registro de decisiones** · intermediación 0.095 · une la comunidad 2 con 1, 3, 4, 6, 7, 8
- **Índice del conocimiento de Varios** · intermediación 0.065 · une la comunidad 11 con 1, 2, 3, 4, 5, 6
- **Guia de Arranque Proyecto v1.4 Diseno Cerrado** · intermediación 0.057 · une la comunidad 7 con 0, 1, 2, 3, 4, 5
- **L2 (puerta técnica)** · intermediación 0.028 · une la comunidad 1 con 2, 3, 4, 6, 8, 9
- **P31 · Calificación de oportunidad** · intermediación 0.025 · une la comunidad 6 con 0, 1, 2, 3, 4, 5
- **CEO digital** · intermediación 0.025 · une la comunidad 10 con 1, 2, 3, 4, 5, 6
- **Experto en asesorías y despachos** · intermediación 0.022 · une la comunidad 1 con 0, 3, 6, 7, 8, 9
- **Administración** · intermediación 0.022 · une la comunidad 1 con 0, 3, 6, 8, 9, 10

## Conexiones sorprendentes

Secciones de carpetas y comunidades distintas que tratan lo mismo y no se enlazan. Relación INFERIDA: compruébala.

- `claude/habilidades/decision-registro.md` › Pasos  ↔  `knowledge/plantillas/entrada-decision.md` › D-0XX — Título  [INFERIDA 0.75]
- `knowledge/agentes/seg.md` › Coordinación sectorial · Seguros  ↔  `processes/referencia-seguros-apertura-siniestros/README.md` › Seguros · Apertura de siniestros en corredurías (proceso de referencia)  [INFERIDA 0.75]
- `knowledge/direccion/README.md` › Dirección y gobierno  ↔  `processes/diagrams/dependencias.md` › Dependencias entre procesos  [INFERIDA 0.75]
- `knowledge/direccion/ceo-digital.md` › Límites de actuación  ↔  `processes/catalog/P10-aprobacion-humana.md` › 7. Decisiones y reglas  [INFERIDA 0.75]
- `claude/habilidades/ficha-metrica.md` › Pasos  ↔  `knowledge/plantillas/ficha-kpi.md` › KPI: <nombre>  [INFERIDA 0.75]
- `claude/habilidades/ficha-metrica.md` › Pasos  ↔  `knowledge/procesos/metricas.md` › Responsabilidades  [INFERIDA 0.75]
- `knowledge/ingenieria/evaluacion-ia.md` › Especialista en evaluación de IA  ↔  `processes/catalog/P23-evaluacion-de-agentes-y-modelos.md` › 20. Pruebas necesarias  [INFERIDA 0.75]
- `claude/habilidades/ficha-proveedor.md` › Pasos  ↔  `knowledge/plantillas/ficha-proveedor.md` › Proveedor: <nombre>  [INFERIDA 0.75]
- `knowledge/sectores/priorizacion.md` › Priorización de sectores  ↔  `processes/templates/proceso-cliente.md` › <sector> · <proceso>  [INFERIDA 0.75]
- `claude/habilidades/revision-entregable.md` › Pasos  ↔  `docs/18-flujo-de-calidad-y-aprendizaje.md` › El flujo, sin huecos  [INFERIDA 0.75]

## Comunidades

### 0 · claude/habilidades · Legal y privacidad y Arquitecto de procesos

Cohesión 0.06 · 94 nodos: Legal y privacidad; Arquitecto de procesos; Seguridad; Coordinación sectorial · Seguros; Director financiero; Jefe comercial; Separar hecho, hipótesis y propuesta; Arquitecto técnico (y 86 más)

### 1 · claude/habilidades · Habilidades de los agentes y Administración

Cohesión 0.09 · 86 nodos: Habilidades de los agentes; Administración; Experto en asesorías y despachos; L2 (puerta técnica); Especialista en contabilidad y facturación; Director comercial; Backend; Especialista en éxito de cliente (y 78 más)

### 2 · docs · Registro de decisiones y Varios · empresa-ia

Cohesión 0.09 · 58 nodos: Registro de decisiones; Varios · empresa-ia; Atlas Evolucion v1.1 Modelo Operativo Procesos y Despliegue; 17 · Cerebro, conocimiento y procesos: auditoría e informe; Registro de correcciones a los documentos recibidos el 17/11/2026; Varios — repositorio maestro; G0 (puerta de cliente); Plan de construcción · 18/11/2026 → 12/02/2027 (y 50 más)

### 3 · knowledge/sectores · Registro de fuentes y Coordinación sectorial y seguros

Cohesión 0.14 · 54 nodos: Registro de fuentes; Coordinación sectorial y seguros; Experto en sanidad privada; Experto en asesorías, gestorías y despachos; Experto en servicios financieros no bancarios; Experto en logística y transporte; P32 · Descubrimiento de procesos; Experto en industria manufacturera (y 46 más)

### 4 · processes/runbooks · Dependencias entre procesos y Procesos y estados

Cohesión 0.2 · 38 nodos: Dependencias entre procesos; Procesos y estados; Especialista en automatización; P30 · Gestión de identidades y secretos; P21 · Ejecución segura de herramientas; P10 · Aprobación humana; Ingeniería y tecnología; Especialista en integraciones (y 30 más)

### 5 · processes/catalog · P22 · Gestión de errores y reintentos y Catálogo de procesos P01–P38

Cohesión 0.47 · 37 nodos: P22 · Gestión de errores y reintentos; Catálogo de procesos P01–P38; P28 · Gestión de incidentes; P22 · Gestión de errores y reintentos; P27 · Gestión de proveedores y dependencias; P05 · Diseño del plan; P02 · Clasificación y triaje; P11 · Entrega y cierre (y 29 más)

### 6 · processes/catalog · Arquitecto de procesos y P38 · Gestión de despliegue por cliente

Cohesión 0.18 · 36 nodos: Arquitecto de procesos; P38 · Gestión de despliegue por cliente; P33 · Diseño y validación TO-BE; P31 · Calificación de oportunidad; P32 · Descubrimiento de procesos; P38 · Gestión de despliegue por cliente; INT-ATLAS · Atlas Evolución v1.1 · modelo operativo, procesos y despliegue; P37 · Medición de rendimiento y valor (y 28 más)

### 7 · docs/atlas · Guia de Arranque Proyecto v1.4 Diseno Cerrado y Flujo ceo

Cohesión 0.32 · 33 nodos: Guia de Arranque Proyecto v1.4 Diseno Cerrado; Flujo ceo; Ejecucion agentes; Motor conocimiento obsidian; Comunicaciones estados; 12 · Ciclo de vida de un proyecto con cliente; Seguridad clientes; Ciclo vida proyecto (y 25 más)

### 8 · claude/habilidades · Director financiero (CFO) y P29 · Gestión de costes y capacidad

Cohesión 0.15 · 27 nodos: Director financiero (CFO); P29 · Gestión de costes y capacidad; Especialista en costes y proveedores; P27 · Gestión de proveedores y dependencias; Director financiero; Especialista financiero; Costes; Especialista en costes y proveedores (y 19 más)

### 9 · knowledge/ingenieria · Especialista en ciberseguridad y Responsable de decisiones y seguimiento

Cohesión 0.22 · 26 nodos: Especialista en ciberseguridad; Responsable de decisiones y seguimiento; Arquitecto de datos e IA; Biblioteca de precedentes; Especialista en calidad y riesgos; Arquitecto técnico; Especialista backend; INT-GUIA · Guía de Arranque v1.4 (diseño cerrado) (y 18 más)

### 10 · knowledge/direccion · CEO digital y Bibliotecario / responsable de conocimiento

Cohesión 0.23 · 19 nodos: CEO digital; Bibliotecario / responsable de conocimiento; P01 · Alta y recepción de petición; P11 · Entrega y cierre; CEO digital; P05 · Diseño del plan; Dirección y gobierno; CEO digital (y 11 más)

### 11 · knowledge/plantillas · Índice del conocimiento de Varios y Plantillas

Cohesión 0.18 · 17 nodos: Índice del conocimiento de Varios; Plantillas; Integraciones; Catálogo de integraciones; Protocolo: consultar el histórico antes de empezar; Protocolo: guardar el conocimiento; Contratos de datos; Metodologías transversales (y 9 más)

### 12 · claude/habilidades · Responsable de cumplimiento normativo y Especialista legal y privacidad

Cohesión 0.21 · 17 nodos: Responsable de cumplimiento normativo; Especialista legal y privacidad; Legal y privacidad; Cumplimiento normativo; Responsable de cumplimiento normativo; UE-RIA-OMNIBUS · Reglamento (UE) 2026/1744 (ómnibus digital sobre IA), que modifica el Reglamento (UE) 2024/1689; Contraste de fuentes; NIS2-ES · Estado de la transposición de NIS2 en España (y 9 más)

### 13 · claude/habilidades · Ingeniero de plataforma y operaciones (DevOps/SRE) y Plataforma y operaciones

Cohesión 0.21 · 14 nodos: Ingeniero de plataforma y operaciones (DevOps/SRE); Plataforma y operaciones; Ingeniero de plataforma y operaciones (DevOps/SRE); ENS-RD311 · Real Decreto 311/2022, Esquema Nacional de Seguridad; ISO-27001 · ISO/IEC 27001:2022 (transición desde 2013 terminada el 31/10/2025); OTEL-GENAI · OpenTelemetry: convenciones semánticas para IA generativa; DORA-DEVOPS · Métricas DORA de entrega de software (DevOps Research and Assessment); GOOGLE-SRE · Site Reliability Engineering (libros de Google SRE) (y 6 más)

### 14 · claude/habilidades · Diseñador de producto y experiencia (UX) y Diseño y experiencia

Cohesión 0.25 · 11 nodos: Diseñador de producto y experiencia (UX); Diseño y experiencia; LEY-ACCESIBILIDAD-11-2023 · Ley 11/2023 (accesibilidad de productos y servicios, transpone la Directiva (UE) 2019/882); Diseñador de producto y experiencia (UX); Flujo y pantallas de una tarea; NNG-HEURISTICAS · 10 heurísticas de usabilidad (Jakob Nielsen); W3C-WCAG22 · Web Content Accessibility Guidelines (WCAG) 2.2; Prueba de usabilidad (y 3 más)

## Huecos

- **Documentos sin ninguna relación** (2): `precedents/projects/2026-11-oficina-de-agentes.md`; `precedents/solutions/busqueda-texto-cerebro.md`
- **Decisiones que no cita ninguna sección** (3): D-008, D-016, D-020
- **Procesos sin especialista responsable** (0): ninguno
- **Fuentes registradas que nadie cita** (0): ninguna
- **Referencias rotas** (se citan pero no existen): ninguna
- **Enlaces ambiguos** (un nombre de archivo con varios destinos): 0

## Preguntas sugeridas

_Preguntas que este grafo ayuda a responder o que conviene decidir:_

- **¿Por qué «Registro de fuentes» conecta la comunidad 3 con las comunidades 1, 2, 4, 5?**
  _Intermediación alta (0.165): es un puente entre temas._
- **¿Por qué «Habilidades de los agentes» conecta la comunidad 1 con las comunidades 0, 3, 4, 6?**
  _Intermediación alta (0.107): es un puente entre temas._
- **¿Por qué «Registro de decisiones» conecta la comunidad 2 con las comunidades 1, 3, 4, 6?**
  _Intermediación alta (0.095): es un puente entre temas._
- **¿Se aprueba D-014 · Adelantar un prototipo mínimo del motor de procesos? Sigue en propuesta y la citan 4 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-013 · Conocimiento y catálogo de procesos generados desde datos? Sigue en propuesta y la citan 3 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-018 · El cerebro pasa a ser un grafo de conocimiento con relaciones explicadas? Sigue en propuesta y la citan 3 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Deberían enlazarse «claude/habilidades/decision-registro.md» y «knowledge/plantillas/entrada-decision.md»?**
  _Tratan lo mismo (relación INFERIDA 0.75) pero no se citan._
- **¿Deberían enlazarse «knowledge/agentes/seg.md» y «processes/referencia-seguros-apertura-siniestros/README.md»?**
  _Tratan lo mismo (relación INFERIDA 0.75) pero no se citan._
- **¿Siguen vigentes D-008, D-016, D-020? Ningún documento las cita.**
  _Decisiones que nadie menciona._

## Cómo usarlo

- En la oficina, cada agente recibe las secciones que encajan con su encargo **y lo conectado a ellas** (decisiones, procesos, fuentes y secciones relacionadas), con la etiqueta de confianza de cada relación.
- En local: `python3 tools/grafo.py consulta "pregunta"`, `camino "A" "B"` y `explica "X"`.
- Las relaciones INFERIDAS son pistas, no hechos: si una es buena, conviértela en un enlace en el documento y pasará a EXTRACTADA.
