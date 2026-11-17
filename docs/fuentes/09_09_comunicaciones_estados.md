> **Versión de trabajo en Markdown** del documento original `archive/originales/09_09_comunicaciones_estados.docx`, convertida el 17/11/2026. Los diagramas originales se han sustituido por enlaces a su versión redibujada y corregida en `docs/atlas/`. Correcciones aplicadas: ver `docs/16-correcciones.md`. Nombre provisional del proyecto: Varios.

**ATLAS DE ARQUITECTURA DIGITAL**

Mapa 9 · Comunicaciones, estados y contratos entre componentes

Qué componente llama a cuál, qué datos intercambia y cómo se registra el ciclo de vida

Documento de diseño · versión 1.0 · noviembre 2026

# 1. Objetivo y alcance

Convertir el mapa conceptual en contratos implementables entre módulos, evitando dependencias implícitas.

Este mapa define el comportamiento objetivo y las responsabilidades de los componentes. No implica que todos estén implementados en el MVP.

# 2. Diagrama de flujo

**Diagrama redibujado:** [docs/atlas/15-componentes.md](../atlas/15-componentes.md)

# 3. Reglas de diseño

- Cada interfaz debe tener contrato versionado: schema, autenticación, autorización, timeout y errores.

- Estados de tarea explícitos: queued, running, blocked, needs_approval, succeeded, failed, cancelled.

- Los eventos deben ser idempotentes o deduplicables; no confiar en entrega exactamente una vez.

- Persistir estado antes de emitir efectos externos; usar patrón outbox si la complejidad lo requiere.

- No enviar secretos ni contenido innecesario en eventos o logs.

- Las colas pueden incorporarse cuando haya concurrencia; al MVP puede bastar orquestación en proceso con estados persistidos.

# 4. Flujo operativo paso a paso

1.  UI envía petición con identidad.

2.  API valida formato, identidad y límites.

3.  CEO devuelve clasificación y plan estructurado.

4.  Persistir workflow y tareas antes de ejecución.

5.  Consultar Knowledge API con contexto autorizado.

6.  Despachar tarea a worker; worker solicita tools a través del gateway.

7.  Persistir resultado y eventos de auditoría.

8.  QA valida resultado; actualizar estado.

9.  Notificar y obtener aprobación cuando sea necesaria.

10. Cerrar workflow con resultado y trazabilidad.

# 5. Excepciones y tratamiento de fallos

- Contrato inválido: 400/422 y mensaje accionable.

- No autorizado: 403 sin filtrar datos.

- Dependencia caída: timeout, retry acotado y estado blocked.

- Evento duplicado: deduplicar mediante event_id/idempotency key.

- Resultado perdido: reconciliar estado con artefactos y logs.

# 6. Artefactos que deben existir

- OpenAPI schemas

- JSON schemas de tareas y resultados

- Catálogo de eventos

- Máquina de estados

- Política de idempotencia y errores

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
