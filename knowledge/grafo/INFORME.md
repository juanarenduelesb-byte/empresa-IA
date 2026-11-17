<!-- Generado por tools/brain_build.py (tools/grafo.py). No editar a mano. -->
# Informe del grafo de conocimiento

Cómo está conectado el cerebro de Varios: qué sostiene todo, qué temas forman grupos, qué conecta temas distintos, qué falta y qué preguntas conviene hacerse. Se regenera con el cerebro (D-018); no forma parte del grafo.

## Resumen

- 3813 nodos: seccion 3247, documento 288, fuente 68, habilidad 65, proceso 38, especialista 34, agente 34, decision 20, puerta 12, departamento 7.
- 4771 relaciones: 70 % EXTRACTADAS (escritas en la fuente), 30 % INFERIDAS (temas compartidos, con puntuación) y 0 AMBIGUAS (para revisar).
- 13 comunidades de temas.

## Nodos centrales

Lo que más cosas conecta. Si cambia, cambia mucho.

1. **Registro de fuentes** (`knowledge/fuentes/registro.md`) · 133 conexiones
2. **Índice del conocimiento de Varios** (`knowledge/INDEX.md`) · 117 conexiones
3. **Registro de decisiones** (`DECISIONS.md`) · 83 conexiones
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

- **Registro de fuentes** · intermediación 0.166 · une la comunidad 5 con 1, 2, 3, 4, 6, 7
- **Habilidades de los agentes** · intermediación 0.107 · une la comunidad 1 con 0, 3, 4, 8, 9, 11
- **Registro de decisiones** · intermediación 0.087 · une la comunidad 2 con 1, 3, 4, 5, 7, 8
- **Índice del conocimiento de Varios** · intermediación 0.065 · une la comunidad 4 con 2, 3, 5, 6, 7, 8
- **Guia de Arranque Proyecto v1.4 Diseno Cerrado** · intermediación 0.057 · une la comunidad 7 con 0, 2, 3, 4, 5, 6
- **L2 (puerta técnica)** · intermediación 0.028 · une la comunidad 1 con 2, 3, 4, 5, 6, 9
- **CEO digital** · intermediación 0.025 · une la comunidad 10 con 1, 2, 3, 4, 5, 6
- **P31 · Calificación de oportunidad** · intermediación 0.025 · une la comunidad 4 con 1, 2, 3, 5, 6, 10
- **Experto en asesorías y despachos** · intermediación 0.022 · une la comunidad 1 con 0, 4, 5, 7, 9, 11
- **Administración** · intermediación 0.022 · une la comunidad 1 con 0, 4, 5, 8, 9, 11

## Conexiones sorprendentes

Secciones de carpetas y comunidades distintas que tratan lo mismo y no se enlazan. Relación INFERIDA: compruébala.

- `claude/habilidades/contrato-de-tarea.md` › Pasos  ↔  `docs/03-ceo-digital-y-orquestacion.md` › Contrato de tarea  [INFERIDA 0.75]
- `claude/habilidades/decision-registro.md` › Pasos  ↔  `knowledge/plantillas/entrada-decision.md` › D-0XX — Título  [INFERIDA 0.75]
- `knowledge/agentes/seg.md` › Coordinación sectorial · Seguros  ↔  `processes/referencia-seguros-apertura-siniestros/README.md` › Seguros · Apertura de siniestros en corredurías (proceso de referencia)  [INFERIDA 0.75]
- `knowledge/direccion/README.md` › Dirección y gobierno  ↔  `processes/diagrams/dependencias.md` › Dependencias entre procesos  [INFERIDA 0.75]
- `knowledge/direccion/ceo-digital.md` › Límites de actuación  ↔  `processes/catalog/P10-aprobacion-humana.md` › 7. Decisiones y reglas  [INFERIDA 0.75]
- `claude/habilidades/ficha-metrica.md` › Pasos  ↔  `knowledge/plantillas/ficha-kpi.md` › KPI: <nombre>  [INFERIDA 0.75]
- `claude/habilidades/ficha-metrica.md` › Pasos  ↔  `knowledge/procesos/metricas.md` › Responsabilidades  [INFERIDA 0.75]
- `knowledge/ingenieria/evaluacion-ia.md` › Especialista en evaluación de IA  ↔  `processes/catalog/P23-evaluacion-de-agentes-y-modelos.md` › 20. Pruebas necesarias  [INFERIDA 0.75]
- `claude/habilidades/ficha-proveedor.md` › Pasos  ↔  `knowledge/plantillas/ficha-proveedor.md` › Proveedor: <nombre>  [INFERIDA 0.75]
- `knowledge/sectores/priorizacion.md` › Priorización de sectores  ↔  `processes/templates/proceso-cliente.md` › <sector> · <proceso>  [INFERIDA 0.75]

## Comunidades

### 0 · claude/habilidades · Legal y privacidad y Arquitecto de procesos

Cohesión 0.05 · 107 nodos: Legal y privacidad; Arquitecto de procesos; Seguridad; Coordinación sectorial · Seguros; Director financiero; Jefe comercial; Separar hecho, hipótesis y propuesta; Arquitecto técnico (y 99 más)

### 1 · claude/habilidades · Habilidades de los agentes y Administración

Cohesión 0.12 · 83 nodos: Habilidades de los agentes; Administración; Experto en asesorías y despachos; L2 (puerta técnica); Backend; Agentes de la oficina; Jefe comercial; Contabilidad y facturación (y 75 más)

### 2 · docs · Registro de decisiones y Varios · empresa-ia

Cohesión 0.08 · 63 nodos: Registro de decisiones; Varios · empresa-ia; Atlas Evolucion v1.1 Modelo Operativo Procesos y Despliegue; 17 · Cerebro, conocimiento y procesos: auditoría e informe; P01 · Alta y recepción de petición; Registro de correcciones a los documentos recibidos el 17/11/2026; Varios — repositorio maestro; G0 (puerta de cliente) (y 55 más)

### 3 · knowledge/ingenieria · Dependencias entre procesos y Especialista en ciberseguridad

Cohesión 0.16 · 56 nodos: Dependencias entre procesos; Especialista en ciberseguridad; Procesos y estados; Arquitecto de datos e IA; Biblioteca de precedentes; Especialista en automatización; Especialista en calidad y riesgos; Arquitecto técnico (y 48 más)

### 4 · processes/catalog · Índice del conocimiento de Varios y Arquitecto de procesos

Cohesión 0.13 · 56 nodos: Índice del conocimiento de Varios; Arquitecto de procesos; P38 · Gestión de despliegue por cliente; Director comercial; P33 · Diseño y validación TO-BE; Especialista en éxito de cliente; P31 · Calificación de oportunidad; P32 · Descubrimiento de procesos (y 48 más)

### 5 · knowledge/sectores · Registro de fuentes y Experto en sanidad privada

Cohesión 0.17 · 48 nodos: Registro de fuentes; Experto en sanidad privada; Coordinación sectorial y seguros; Experto en asesorías, gestorías y despachos; Experto en logística y transporte; Experto en servicios financieros no bancarios; P32 · Descubrimiento de procesos; Experto en industria manufacturera (y 40 más)

### 6 · processes/catalog · P22 · Gestión de errores y reintentos y Catálogo de procesos P01–P38

Cohesión 0.42 · 39 nodos: P22 · Gestión de errores y reintentos; Catálogo de procesos P01–P38; P28 · Gestión de incidentes; P22 · Gestión de errores y reintentos; P27 · Gestión de proveedores y dependencias; P05 · Diseño del plan; P02 · Clasificación y triaje; P11 · Entrega y cierre (y 31 más)

### 7 · docs/atlas · Guia de Arranque Proyecto v1.4 Diseno Cerrado y Flujo ceo

Cohesión 0.34 · 32 nodos: Guia de Arranque Proyecto v1.4 Diseno Cerrado; Flujo ceo; Ejecucion agentes; Motor conocimiento obsidian; Comunicaciones estados; 12 · Ciclo de vida de un proyecto con cliente; Seguridad clientes; Ciclo vida proyecto (y 24 más)

### 8 · knowledge/administracion-finanzas · Especialista en contabilidad y facturación y Director financiero (CFO)

Cohesión 0.21 · 24 nodos: Especialista en contabilidad y facturación; Director financiero (CFO); P29 · Gestión de costes y capacidad; Especialista en costes y proveedores; P27 · Gestión de proveedores y dependencias; Especialista financiero; Especialista en contabilidad y facturación; Especialista en costes y proveedores (y 16 más)

### 9 · claude/habilidades · Responsable de cumplimiento normativo y Especialista legal y privacidad

Cohesión 0.16 · 23 nodos: Responsable de cumplimiento normativo; Especialista legal y privacidad; Diseñador de producto y experiencia (UX); P19 · Política de uso y límites; Cumplimiento normativo; Responsable de cumplimiento normativo; Especialista legal y privacidad; UE-RIA-OMNIBUS · Reglamento (UE) 2026/1744 (ómnibus digital sobre IA), que modifica el Reglamento (UE) 2024/1689 (y 15 más)

### 10 · knowledge/direccion · CEO digital y Responsable de decisiones y seguimiento

Cohesión 0.35 · 15 nodos: CEO digital; Responsable de decisiones y seguimiento; Bibliotecario / responsable de conocimiento; P11 · Entrega y cierre; P04 · Recuperación de conocimiento; P13 · Aprendizaje y actualización de la wiki; P05 · Diseño del plan; Dirección y gobierno (y 7 más)

### 11 · claude/habilidades · Ingeniero de plataforma y operaciones (DevOps/SRE) y Plataforma y operaciones

Cohesión 0.21 · 14 nodos: Ingeniero de plataforma y operaciones (DevOps/SRE); Plataforma y operaciones; Ingeniero de plataforma y operaciones (DevOps/SRE); ENS-RD311 · Real Decreto 311/2022, Esquema Nacional de Seguridad; ISO-27001 · ISO/IEC 27001:2022 (transición desde 2013 terminada el 31/10/2025); OTEL-GENAI · OpenTelemetry: convenciones semánticas para IA generativa; DORA-DEVOPS · Métricas DORA de entrega de software (DevOps Research and Assessment); GOOGLE-SRE · Site Reliability Engineering (libros de Google SRE) (y 6 más)

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

- **¿Por qué «Registro de fuentes» conecta la comunidad 5 con las comunidades 1, 2, 3, 4?**
  _Intermediación alta (0.166): es un puente entre temas._
- **¿Por qué «Habilidades de los agentes» conecta la comunidad 1 con las comunidades 0, 3, 4, 8?**
  _Intermediación alta (0.107): es un puente entre temas._
- **¿Por qué «Registro de decisiones» conecta la comunidad 2 con las comunidades 1, 3, 4, 5?**
  _Intermediación alta (0.087): es un puente entre temas._
- **¿Se aprueba D-014 · Adelantar un prototipo mínimo del motor de procesos? Sigue en propuesta y la citan 4 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-013 · Conocimiento y catálogo de procesos generados desde datos? Sigue en propuesta y la citan 3 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Deberían enlazarse «claude/habilidades/contrato-de-tarea.md» y «docs/03-ceo-digital-y-orquestacion.md»?**
  _Tratan lo mismo (relación INFERIDA 0.75) pero no se citan._
- **¿Deberían enlazarse «claude/habilidades/decision-registro.md» y «knowledge/plantillas/entrada-decision.md»?**
  _Tratan lo mismo (relación INFERIDA 0.75) pero no se citan._
- **¿Siguen vigentes D-008, D-016, D-020? Ningún documento las cita.**
  _Decisiones que nadie menciona._

## Cómo usarlo

- En la oficina, cada agente recibe las secciones que encajan con su encargo **y lo conectado a ellas** (decisiones, procesos, fuentes y secciones relacionadas), con la etiqueta de confianza de cada relación.
- En local: `python3 tools/grafo.py consulta "pregunta"`, `camino "A" "B"` y `explica "X"`.
- Las relaciones INFERIDAS son pistas, no hechos: si una es buena, conviértela en un enlace en el documento y pasará a EXTRACTADA.
