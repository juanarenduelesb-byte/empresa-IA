> **Versión de trabajo en Markdown** del documento original `archive/originales/02_02_flujo_ceo.docx`, convertida el 17/11/2026. Los diagramas originales se han sustituido por enlaces a su versión redibujada y corregida en `docs/atlas/`. Correcciones aplicadas: ver `docs/16-correcciones.md`. Nombre provisional del proyecto: Varios.

**ATLAS DE ARQUITECTURA DIGITAL**

Mapa 2 · Flujo completo del CEO digital

De la petición inicial a la entrega, con rutas de aclaración, rechazo, escalado y replanificación

Documento de diseño · versión 1.0 · noviembre 2026

# 1. Objetivo y alcance

Especificar el ciclo de vida de cada encargo y las decisiones que toma el CEO.

Este mapa define el comportamiento objetivo y las responsabilidades de los componentes. No implica que todos estén implementados en el MVP.

# 2. Diagrama de flujo

**Diagrama redibujado:** [docs/atlas/02-flujo-ceo.md](../atlas/02-flujo-ceo.md)

# 3. Reglas de diseño

- El CEO debe poder abstenerse: pedir aclaración, escalar o rechazar una petición fuera de alcance.

- La clasificación debe producir etiquetas, nivel de confianza, justificación y versión de política.

- El plan debe declarar entregables, dependencias, criterios de aceptación, presupuesto/coste estimado y riesgos.

- Las acciones externas, irreversibles o de alto impacto requieren aprobación humana explícita.

- No pasar a entrega final si QA falla; replanificar o explicar limitaciones.

# 4. Flujo operativo paso a paso

1.  Registrar solicitud, solicitante, cliente, fecha y adjuntos.

2.  Validar identidad, formato, malware y autorización de acceso.

3.  Clasificar intención, sector, proceso, sensibilidad, riesgo y confianza.

4.  Si falta información esencial, formular preguntas concretas.

5.  Comprobar alcance, política y permisos antes de planificar ejecución.

6.  Crear plan de tareas con responsables, dependencias y criterios de éxito.

7.  Ejecutar en entornos y herramientas autorizados.

8.  Validar resultados contra fuentes y criterios.

9.  Solicitar aprobación humana si corresponde.

10. Entregar, registrar y cerrar; proponer aprendizaje separado de la aprobación.

# 5. Excepciones y tratamiento de fallos

- Entrada maliciosa o sospechosa: cuarentena y revisión; no ejecutar contenido adjunto.

- Baja confianza: preguntar; no forzar clasificación.

- Fuera de alcance: rechazar o proponer alternativa segura.

- Fallo de tarea: estado fallido, diagnóstico y reintento limitado o escalado.

- QA no superado: devolver a ejecución con defectos concretos.

- Aprobación denegada: detener la acción y registrar decisión.

# 6. Artefactos que deben existir

- Solicitud normalizada

- Ficha de clasificación y riesgo

- Plan de ejecución

- Registro de aprobaciones

- Paquete de entrega y cierre

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
