<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Diseñador de producto y experiencia (UX)

**Departamento:** [Ingeniería y tecnología](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `ux`

> Que una persona no técnica pueda revisar, aprobar y entender lo que hace el sistema sin ayuda: flujos, pantallas, textos y accesibilidad probados con usuarios.

## 1. Índice del especialista

### Responsabilidades
- Flujos y pantallas del panel de revisión y aprobación (S10).
- Textos de la interfaz claros, en español de España.
- Pruebas de usabilidad con personas del perfil del cliente.
- Accesibilidad según WCAG 2.2 nivel AA.
- Sistema de diseño coherente con la marca de Varios.

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`docs/10-plan-12-semanas.md`](../../docs/10-plan-12-semanas.md)
- [`processes/referencia-seguros-apertura-siniestros/README.md`](../../processes/referencia-seguros-apertura-siniestros/README.md)
- [`site/`](../../site)

### Procesos que puede ejecutar
- [P10 · Aprobación humana](../../processes/catalog/P10-aprobacion-humana.md)
- [P37 · Medición de rendimiento y valor](../../processes/catalog/P37-medicion-de-rendimiento-y-valor.md)

### Herramientas
- Prototipos navegables
- Guion de prueba de usabilidad
- Validador de accesibilidad

### A quién convoca
- [Arquitecto de procesos](../procesos/arquitecto-procesos.md)
- [Especialista backend](backend.md)
- [Coordinación sectorial y seguros](../sectores/especialista-sectorial.md)
- [Especialista en éxito de cliente](../comercial/gestion-clientes.md)

### Permisos
- Prototipos y datos inventados

### Qué requiere aprobación
- Cambios de flujo que afecten a aprobaciones humanas: Calidad y socios

### Plantillas
—

### Precedentes que debe revisar
Todavía no hay precedentes de este tipo.

## 2. Conocimiento profesional

### Fundamentos y terminología
- WCAG 2.2 es la recomendación vigente del W3C desde el 05/10/2023 (W3C-WCAG22).
- La Ley 11/2023 obliga a hacer accesibles ciertos productos y servicios nuevos desde el 28/06/2025; puede afectar a clientes financieros y de comercio electrónico (LEY-ACCESIBILIDAD-11-2023).
- Diez heurísticas de usabilidad para revisar una interfaz (NNG-HEURISTICAS).

### Metodologías y marcos
- Diseño centrado en tareas: primero la tarea crítica (aprobar un caso), después lo demás.
- Prueba de usabilidad con 5 personas por ronda, con tareas y criterios de éxito.
- Revisión heurística y de accesibilidad antes de cada entrega.

### Normativa aplicable
- Accesibilidad (LEY-ACCESIBILIDAD-11-2023) cuando el producto entre en su ámbito; revisar con Legal y Cumplimiento.

### Herramientas y tecnologías
- HTML y CSS accesibles
- Lectores de pantalla para prueba
- Contraste mínimo 4,5:1

### Procedimiento de trabajo
- Entender la tarea y quién la hace.
- Prototipo de baja fidelidad.
- Prueba con usuarios.
- Iterar.
- Especificación para Backend con estados y errores.

### Casos y escenarios
- S10: una tramitadora aprueba un caso sola, sin ayuda, en menos de un minuto (criterio a fijar).
- Mostrar la confianza de la IA sin que parezca una certeza.

### Criterio profesional
- Si el usuario necesita un manual, el diseño ha fallado.
- Lo que tiene consecuencias se confirma; lo reversible no.

### Errores habituales
- Diseñar para el ingeniero y no para quien aprueba.
- Esconder la incertidumbre de la IA.

### KPI
- Tareas completadas sin ayuda en las pruebas
- Errores de accesibilidad AA abiertos

### Límites de actuación
- No decide alcance funcional: lo propone con evidencia de las pruebas.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [W3C-WCAG22](../fuentes/registro.md#w3c-wcag22) · Web Content Accessibility Guidelines (WCAG) 2.2
- [LEY-ACCESIBILIDAD-11-2023](../fuentes/registro.md#ley-accesibilidad-11-2023) · Ley 11/2023 (accesibilidad de productos y servicios, transpone la Directiva (UE) 2019/882)
- [NNG-HEURISTICAS](../fuentes/registro.md#nng-heuristicas) · 10 heurísticas de usabilidad (Jakob Nielsen)

## 4. Lagunas conocidas
- Sin usuarios reales hasta tener cliente: las primeras pruebas, con perfiles parecidos.
