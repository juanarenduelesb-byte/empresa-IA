> **Versión de trabajo en Markdown** del documento original `archive/originales/06_06_calidad_gobierno.docx`, convertida el 17/11/2026. Los diagramas originales se han sustituido por enlaces a su versión redibujada y corregida en `docs/atlas/`. Correcciones aplicadas: ver `docs/16-correcciones.md`. Nombre provisional del proyecto: Varios.

**ATLAS DE ARQUITECTURA DIGITAL**

Mapa 6 · Calidad, evaluación y gobierno humano

No se confunde una respuesta convincente con un resultado correcto y autorizado

Documento de diseño · versión 1.0 · noviembre 2026

# 1. Objetivo y alcance

Definir cómo se mide la calidad, cómo se aprueban acciones y cómo se gobiernan cambios de prompts, modelos y agentes.

Este mapa define el comportamiento objetivo y las responsabilidades de los componentes. No implica que todos estén implementados en el MVP.

# 2. Diagrama de flujo

**Diagrama redibujado:** [docs/atlas/09-calidad.md](../atlas/09-calidad.md)

# 3. Reglas de diseño

- Definir criterios antes de ejecutar; no inventarlos al ver el resultado.

- Separar pruebas unitarias, integración, evaluación LLM y revisión humana.

- Evaluar con casos representativos, límites y ataques; conservar versiones de datasets.

- Cada cambio de modelo, prompt, herramienta o esquema requiere pruebas de regresión.

- La aprobación humana debe ser explícita, atribuible y registrada.

- No usar feedback de cliente para entrenar o cambiar conocimiento sin autorización y validación.

# 4. Flujo operativo paso a paso

1.  Definir aceptación, nivel de riesgo y revisor.

2.  Ejecutar validaciones automáticas deterministas.

3.  Evaluar calidad semántica y fundamentación con pruebas controladas.

4.  Solicitar revisión humana para tareas/acciones de riesgo.

5.  Registrar decisión, versión y evidencias.

6.  Medir calidad, coste, latencia, fallos y escalados.

7.  Proponer mejoras y convertir fallos relevantes en nuevos casos de prueba.

# 5. Excepciones y tratamiento de fallos

- No existe criterio de aceptación: no marcar como completado.

- Evaluadores no calibrados: no automatizar aprobación.

- Regresión detectada: bloquear release y revertir.

- Desacuerdo entre evaluadores: escalar a experto humano.

- Feedback no autorizado: no incorporarlo al conocimiento.

# 6. Artefactos que deben existir

- Catálogo de criterios de aceptación

- Dataset de evaluación versionado

- Matriz de aprobación por riesgo

- Registro de cambios y releases

- Panel de métricas

# 7. Criterios de aceptación

- El flujo puede ejecutarse de extremo a extremo en un entorno de pruebas.

- Las entradas, salidas, responsables, estados y decisiones quedan registrados.

- Los casos de error y denegación están probados, no solo el camino exitoso.

- Los permisos se verifican en backend y se prueban con identidades distintas.

- Existe documentación suficiente para que otra persona pueda mantener y desplegar el componente.

# 8. Prioridad de implantación

MVP: implementar el recorrido mínimo y persistir estados. Antes de datos reales de clientes: completar controles de seguridad, privacidad, backups, recuperación, evaluación y contratos de proveedores. Escalado: incorporar colas, observabilidad avanzada y redundancia cuando el uso lo justifique.

# 9. Decisiones aún pendientes

Deben decidirse con evidencia antes del hito correspondiente: sector y caso de uso inicial; roles concretos y matriz RACI; proveedores y regiones definitivos; retención y clasificación de datos; modelo de amenazas detallado; presupuesto y umbrales de coste; objetivos de disponibilidad, RPO/RTO; obligaciones contractuales y regulatorias aplicables.
