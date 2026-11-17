> **Versión de trabajo en Markdown** del documento original `archive/originales/08_08_ciclo_vida_proyecto.docx`, convertida el 17/11/2026. Los diagramas originales se han sustituido por enlaces a su versión redibujada y corregida en `docs/atlas/`. Correcciones aplicadas: ver `docs/16-correcciones.md`. Nombre provisional del proyecto: Varios.

**ATLAS DE ARQUITECTURA DIGITAL**

Mapa 8 · Ciclo de vida de un proyecto y aprendizaje

Del descubrimiento al cierre; el aprendizaje se propone y valida, no se incorpora automáticamente

Documento de diseño · versión 1.0 · noviembre 2026

# 1. Objetivo y alcance

Definir el proceso de entrega repetible y cómo reutilizar resultados sin mezclar datos de clientes.

Este mapa define el comportamiento objetivo y las responsabilidades de los componentes. No implica que todos estén implementados en el MVP.

# 2. Diagrama de flujo

**Diagrama redibujado:** [docs/atlas/12-ciclo-proyecto.md](../atlas/12-ciclo-proyecto.md)

# 3. Reglas de diseño

- El proyecto tiene sponsor, alcance, owner, entregables y criterios de aceptación.

- No reutilizar datos, documentos ni aprendizajes identificables de un cliente en otro cliente.

- La generalización/anominización debe revisarse; eliminar nombres no siempre elimina reidentificación.

- La retroalimentación del cliente se usa solo según contrato y autorización.

- El aprendizaje se publica como draft y pasa validación y control de fuentes.

# 4. Flujo operativo paso a paso

1.  Registrar oportunidad y solicitante.

2.  Realizar discovery y documentar supuestos/lagunas.

3.  Crear propuesta y plan con riesgos y responsables.

4.  Obtener aprobación para alcance y ejecución.

5.  Ejecutar tareas y conservar evidencias autorizadas.

6.  Realizar QA y aceptación.

7.  Entregar y cerrar con métricas y feedback autorizado.

8.  Realizar post-mortem interno.

9.  Extraer patrones no confidenciales y generalizados.

10. Proponer actualización de Wiki y validar antes de publicar.

# 5. Excepciones y tratamiento de fallos

- Alcance cambia: change request y reestimación.

- Cliente no acepta: registrar defectos y plan de remediación.

- Datos no pueden reutilizarse: descartar aprendizaje específico o mantenerlo aislado.

- Lección no demostrada: no publicarla como metodología aprobada.

# 6. Artefactos que deben existir

- Project brief

- Discovery log

- Plan de trabajo

- Decision log

- Entregables y evidencias

- Post-mortem

- Propuesta de conocimiento

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
