<!-- Generado por tools/brain_build.py (tools/grafo.py). No editar a mano. -->
# Informe del grafo de conocimiento

Cómo está conectado el cerebro de Varios: qué sostiene todo, qué temas forman grupos, qué conecta temas distintos, qué falta y qué preguntas conviene hacerse. Se regenera con el cerebro (D-018); no forma parte del grafo.

## Resumen

- 4585 nodos: seccion 3961, documento 343, fuente 68, habilidad 65, proceso 38, especialista 34, agente 34, decision 23, puerta 12, departamento 7.
- 6145 relaciones: 60 % EXTRACTADAS (escritas en la fuente), 40 % INFERIDAS (temas compartidos, con puntuación) y 0 AMBIGUAS (para revisar).
- 12 comunidades de temas.

## Nodos centrales

Lo que más cosas conecta. Si cambia, cambia mucho.

1. **Registro de fuentes** (`knowledge/fuentes/registro.md`) · 137 conexiones
2. **Índice del conocimiento de Varios** (`knowledge/INDEX.md`) · 117 conexiones
3. **Registro de decisiones** (`DECISIONS.md`) · 99 conexiones
4. **Guia de Arranque Proyecto v1.4 Diseno Cerrado** (`docs/fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md`) · 85 conexiones
5. **Catálogo de procesos P01–P38** (`processes/catalog/README.md`) · 82 conexiones
6. **Habilidades de los agentes** (`claude/habilidades/README.md`) · 68 conexiones
7. **P22 · Gestión de errores y reintentos** · 62 conexiones
8. **P28 · Gestión de incidentes** · 61 conexiones
9. **L2 (puerta técnica)** · 60 conexiones
10. **CEO digital** (`knowledge/direccion/ceo-digital.md`) · 58 conexiones
11. **Varios · empresa-ia** (`CLAUDE.md`) · 57 conexiones
12. **Arquitecto de procesos** (`knowledge/procesos/arquitecto-procesos.md`) · 50 conexiones

## Puentes entre temas

Nodos por los que pasa el camino entre comunidades distintas (intermediación).

- **Registro de fuentes** · intermediación 0.161 · une la comunidad 2 con 1, 3, 4, 5, 6, 7
- **Registro de decisiones** · intermediación 0.107 · une la comunidad 5 con 1, 2, 3, 4, 6, 8
- **Habilidades de los agentes** · intermediación 0.097 · une la comunidad 1 con 3, 4, 6
- **Índice del conocimiento de Varios** · intermediación 0.059 · une la comunidad 6 con 2, 3, 4, 5, 7, 8
- **L2 (puerta técnica)** · intermediación 0.054 · une la comunidad 10 con 1, 2, 3, 4, 5, 6
- **Guia de Arranque Proyecto v1.4 Diseno Cerrado** · intermediación 0.047 · une la comunidad 8 con 1, 2, 3, 5, 6, 7
- **CEO digital** · intermediación 0.024 · une la comunidad 3 con 1, 2, 5, 6, 7, 8
- **D-011 · Construir primero, clientes desde el 15/02/2027** · intermediación 0.022 · une la comunidad 4 con 1, 2, 5, 6, 10, 11
- **P31 · Calificación de oportunidad** · intermediación 0.021 · une la comunidad 6 con 1, 2, 3, 5, 7, 11
- **Experto en asesorías y despachos** · intermediación 0.019 · une la comunidad 1 con 0, 2, 8, 10

## Conexiones sorprendentes

Secciones de carpetas y comunidades distintas que tratan lo mismo y no se enlazan. Relación INFERIDA: compruébala.

- `claude/habilidades/contrato-de-tarea.md` › Pasos  ↔  `docs/03-ceo-digital-y-orquestacion.md` › Contrato de tarea  [INFERIDA 0.75]
- `knowledge/agentes/ingj.md` › Reglas del puesto  ↔  `processes/catalog/P01-alta-y-recepcion-de-peticion.md` › 7. Decisiones y reglas  [INFERIDA 0.75]
- `knowledge/agentes/kpi.md` › Reglas del puesto  ↔  `precedents/oficina/conversaciones/2026-11/2026-11-17-ceo-digital-a-metricas-sj6cp.md` › CEO digital → Métricas  [INFERIDA 0.75]
- `knowledge/agentes/proj.md` › Con quién trabaja  ↔  `precedents/oficina/conversaciones/2026-11/2026-11-17-metricas-a-coordinacion-sectorial-seguros-utv9x.md` › Métricas → Coordinación sectorial · Seguros  [INFERIDA 0.75]
- `claude/habilidades/decision-registro.md` › Pasos  ↔  `knowledge/plantillas/entrada-decision.md` › D-0XX — Título  [INFERIDA 0.75]
- `knowledge/agentes/seg.md` › Reglas del puesto  ↔  `precedents/oficina/encargos/2026-11/2026-11-17-propuesta-de-proceso-de-referencia-siniestros-en-c-tcpkm.md` › 7. Qué distingue práctica habitual de norma legal  [INFERIDA 0.75]
- `knowledge/direccion/bibliotecario.md` › Bibliotecario / responsable de conocimiento  ↔  `processes/catalog/P13-aprendizaje-y-actualizacion-de-la-wiki.md` › 20. Pruebas necesarias  [INFERIDA 0.75]
- `knowledge/direccion/ceo-digital.md` › Qué requiere aprobación  ↔  `precedents/oficina/chats/ceo-digital.md` › 2. Hechos  [INFERIDA 0.75]
- `knowledge/direccion/ceo-digital.md` › Qué requiere aprobación  ↔  `precedents/oficina/encargos/2026-11/2026-11-17-acta-de-proteccion-de-la-ia-y-examen-de-50-casos-6sxjn.md` › 2. Hechos  [INFERIDA 0.75]
- `claude/habilidades/ficha-metrica.md` › Pasos  ↔  `knowledge/plantillas/ficha-kpi.md` › KPI: <nombre>  [INFERIDA 0.75]

## Comunidades

### 0 · Habilidades · Legal y privacidad y Arquitecto de procesos

Cohesión 0.05 · 106 nodos: Legal y privacidad; Arquitecto de procesos; Seguridad; Coordinación sectorial · Seguros; Director financiero; Jefe comercial; Separar hecho, hipótesis y propuesta; Arquitecto técnico (y 98 más)

### 1 · claude/habilidades · Habilidades de los agentes y Administración

Cohesión 0.09 · 98 nodos: Habilidades de los agentes; Administración; Experto en asesorías y despachos; Backend; Agentes de la oficina; Arquitecto de procesos; Jefe comercial; Director financiero (y 90 más)

### 2 · knowledge/sectores · Registro de fuentes y Responsable de cumplimiento normativo

Cohesión 0.11 · 73 nodos: Registro de fuentes; Responsable de cumplimiento normativo; Coordinación sectorial y seguros; Experto en sanidad privada; Ingeniero de plataforma y operaciones (DevOps/SRE); Experto en servicios financieros no bancarios; Experto en asesorías, gestorías y despachos; Especialista legal y privacidad (y 65 más)

### 3 · knowledge/direccion · Dependencias entre procesos y CEO digital

Cohesión 0.14 · 70 nodos: Dependencias entre procesos; CEO digital; Especialista en ciberseguridad; Procesos y estados; Responsable de decisiones y seguimiento; Bibliotecario / responsable de conocimiento; Especialista en automatización; Especialista backend (y 62 más)

### 4 · precedents/oficina · Propuesta de proceso de referencia: siniestros en corredurías y Conversaciones con Coordinación sectorial · Seguros

Cohesión 0.16 · 58 nodos: Propuesta de proceso de referencia: siniestros en corredurías; Conversaciones con Coordinación sectorial · Seguros; Guion de validación semanal: apertura de siniestros; Conversaciones con Arquitecto de procesos; Memoria de la oficina; Línea base y fichas de métricas · Atalaya; D-011 · Construir primero, clientes desde el 15/02/2027; Claves del sector seguros para Atalaya (y 50 más)

### 5 · docs · Registro de decisiones y Varios · empresa-ia

Cohesión 0.1 · 54 nodos: Registro de decisiones; Varios · empresa-ia; Arquitecto de datos e IA; Atlas Evolucion v1.1 Modelo Operativo Procesos y Despliegue; 17 · Cerebro, conocimiento y procesos: auditoría e informe; Arquitecto técnico; Plan de construcción · 18/11/2026 → 12/02/2027; Varios — repositorio maestro (y 46 más)

### 6 · processes/catalog · Índice del conocimiento de Varios y Arquitecto de procesos

Cohesión 0.15 · 54 nodos: Índice del conocimiento de Varios; Arquitecto de procesos; P32 · Descubrimiento de procesos; Director comercial; P33 · Diseño y validación TO-BE; P38 · Gestión de despliegue por cliente; Biblioteca de precedentes; P31 · Calificación de oportunidad (y 46 más)

### 7 · processes/catalog · P22 · Gestión de errores y reintentos y Catálogo de procesos P01–P38

Cohesión 0.46 · 39 nodos: P22 · Gestión de errores y reintentos; Catálogo de procesos P01–P38; P28 · Gestión de incidentes; P22 · Gestión de errores y reintentos; P27 · Gestión de proveedores y dependencias; P05 · Diseño del plan; P11 · Entrega y cierre; P02 · Clasificación y triaje (y 31 más)

### 8 · docs/atlas · Guia de Arranque Proyecto v1.4 Diseno Cerrado y Ejecucion agentes

Cohesión 0.29 · 37 nodos: Guia de Arranque Proyecto v1.4 Diseno Cerrado; Ejecucion agentes; Flujo ceo; Motor conocimiento obsidian; 12 · Ciclo de vida de un proyecto con cliente; Calidad gobierno; Comunicaciones estados; Registro de correcciones a los documentos recibidos el 17/11/2026 (y 29 más)

### 9 · knowledge/administracion-finanzas · Director financiero (CFO) y P29 · Gestión de costes y capacidad

Cohesión 0.27 · 17 nodos: Director financiero (CFO); P29 · Gestión de costes y capacidad; Especialista en costes y proveedores; P27 · Gestión de proveedores y dependencias; Especialista financiero; Especialista en costes y proveedores; PGC-PYMES · Real Decreto 1515/2007, Plan General de Contabilidad de Pymes; Administración y finanzas (y 9 más)

### 10 · precedents/oficina · Acta de protección de la IA y examen de 50 casos y Conversaciones con IA y evaluación

Cohesión 0.5 · 12 nodos: Acta de protección de la IA y examen de 50 casos; L2 (puerta técnica); Conversaciones con IA y evaluación; Reunión: IA y evaluación y Seguridad; Conversaciones con CEO digital; Conversaciones con Plan y seguimiento; Conversaciones con Registro de decisiones; Conversaciones con Bibliotecario (y 4 más)

### 11 · integrations · Integraciones y Contratos de datos

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

- **¿Por qué «Registro de fuentes» conecta la comunidad 2 con las comunidades 1, 3, 4, 5?**
  _Intermediación alta (0.161): es un puente entre temas._
- **¿Por qué «Registro de decisiones» conecta la comunidad 5 con las comunidades 1, 2, 3, 4?**
  _Intermediación alta (0.107): es un puente entre temas._
- **¿Por qué «Habilidades de los agentes» conecta la comunidad 1 con las comunidades 3, 4, 6?**
  _Intermediación alta (0.097): es un puente entre temas._
- **¿Se aprueba D-013 · Conocimiento y catálogo de procesos generados desde datos? Sigue en propuesta y la citan 12 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-017 · La oficina se vuelca cada noche a GitHub y las automatizaciones van por GitHub Actions? Sigue en propuesta y la citan 10 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Se aprueba D-014 · Adelantar un prototipo mínimo del motor de procesos? Sigue en propuesta y la citan 6 secciones.**
  _Una decisión en propuesta que ya sostiene mucho contenido._
- **¿Deberían enlazarse «claude/habilidades/contrato-de-tarea.md» y «docs/03-ceo-digital-y-orquestacion.md»?**
  _Tratan lo mismo (relación INFERIDA 0.75) pero no se citan._
- **¿Deberían enlazarse «knowledge/agentes/ingj.md» y «processes/catalog/P01-alta-y-recepcion-de-peticion.md»?**
  _Tratan lo mismo (relación INFERIDA 0.75) pero no se citan._
- **¿Siguen vigentes D-008, D-016, D-020? Ningún documento las cita.**
  _Decisiones que nadie menciona._

## Cómo usarlo

- En la oficina, cada agente recibe las secciones que encajan con su encargo **y lo conectado a ellas** (decisiones, procesos, fuentes y secciones relacionadas), con la etiqueta de confianza de cada relación.
- En local: `python3 tools/grafo.py consulta "pregunta"`, `camino "A" "B"` y `explica "X"`.
- Las relaciones INFERIDAS son pistas, no hechos: si una es buena, conviértela en un enlace en el documento y pasará a EXTRACTADA.
