> **Versión de trabajo en Markdown** del documento original `archive/originales/04_04_ejecucion_agentes.docx`, convertida el 17/11/2026. Los diagramas originales se han sustituido por enlaces a su versión redibujada y corregida en `docs/atlas/`. Correcciones aplicadas: ver `docs/16-correcciones.md`. Nombre provisional del proyecto: Varios.

**ATLAS DE ARQUITECTURA DIGITAL**

Mapa 4 · Ejecución, agentes, herramientas y workflows

Ejecución controlada por estados, con permisos mínimos, idempotencia, límites y trazabilidad

Documento de diseño · versión 1.0 · noviembre 2026

# 1. Objetivo y alcance

Mostrar cómo el CEO convierte un plan en tareas ejecutables sin permitir que los agentes actúen libremente.

Este mapa define el comportamiento objetivo y las responsabilidades de los componentes. No implica que todos estén implementados en el MVP.

# 2. Diagrama de flujo

**Diagrama redibujado:** [docs/atlas/04-ejecucion.md](../atlas/04-ejecucion.md)

# 3. Reglas de diseño

- El agente no elige ni amplía sus permisos; el backend aplica autorización.

- Toda herramienta tiene esquema de entrada/salida, allowlist, timeout, límites y logging.

- Usar idempotency keys para evitar duplicar efectos en reintentos.

- Separar planificación del CEO de ejecución efectiva de herramientas.

- Acciones destructivas, financieras, externas o irreversibles requieren aprobación humana.

- No ejecutar código o archivos no confiables fuera de sandbox.

# 4. Flujo operativo paso a paso

1.  El workflow crea tareas con IDs únicos y estados definidos.

2.  El asignador elige agente/capacidad y modelo según política.

3.  Se genera contexto mínimo y autorizado para la tarea.

4.  Tool Gateway valida identidad, argumentos, alcance y presupuesto.

5.  La herramienta se ejecuta con permisos mínimos y aislamiento.

6.  El resultado se valida contra esquema y criterios.

7.  Se registra traza y consumo; workflow avanza o falla.

8.  Ante fallo: retry limitado, compensación o escalado.

9.  QA y aprobación preceden a la entrega.

# 5. Excepciones y tratamiento de fallos

- Timeout: cancelar si es seguro y reintentar con backoff limitado.

- Respuesta malformada: rechazar salida y registrar; no propagarla.

- Herramienta no autorizada: bloquear y alertar.

- Efecto duplicado: idempotencia y reconciliación.

- Agente en bucle o coste excesivo: límite de pasos/tokens/tiempo y kill switch.

# 6. Artefactos que deben existir

- Catálogo de herramientas

- Máquina de estados de workflows

- Política de reintentos e idempotencia

- Registro de ejecuciones y costes

- Evaluaciones de agentes

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
