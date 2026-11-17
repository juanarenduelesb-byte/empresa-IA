> **Versión de trabajo en Markdown** del documento original `archive/originales/07_07_infraestructura_portabilidad.docx`, convertida el 17/11/2026. Los diagramas originales se han sustituido por enlaces a su versión redibujada y corregida en `docs/atlas/`. Correcciones aplicadas: ver `docs/16-correcciones.md`. Nombre provisional del proyecto: Varios.

**ATLAS DE ARQUITECTURA DIGITAL**

Mapa 7 · Infraestructura, desarrollo y portabilidad

Construcción gratuita inicial, servicios reemplazables y migración sin dependencia del Mac

Documento de diseño · versión 1.0 · noviembre 2026

# 1. Objetivo y alcance

Separar desarrollo, ejecución, datos, conocimiento y proveedores para que el proyecto pueda trasladarse a otra máquina o nube.

Este mapa define el comportamiento objetivo y las responsabilidades de los componentes. No implica que todos estén implementados en el MVP.

# 2. Diagrama de flujo

**Diagrama redibujado:** [docs/atlas/11-infraestructura.md](../atlas/11-infraestructura.md)

# 3. Reglas de diseño

- El Mac es entorno de desarrollo, nunca la única ubicación del código o datos.

- Mantener PostgreSQL estándar, migraciones versionadas y exportación probada.

- Separar secretos de código y configurar cada entorno mediante variables/secret manager.

- Los planes gratuitos son para construcción y demos; no garantizan SLA, backups ni continuidad.

- Verificar regiones, subprocesadores, términos, límites y retención antes de cargar datos reales.

- Mantener documentación de despliegue y recuperación reproducible.

# 4. Flujo operativo paso a paso

1.  Crear repositorio privado y estructura reproducible.

2.  Desarrollar localmente con tests y dependencias fijadas.

3.  Ejecutar PostgreSQL local o entorno de desarrollo gestionado.

4.  Desplegar demo cloud solo cuando aporte valor.

5.  Mantener adapter de modelos y capa de almacenamiento desacoplados.

6.  Exportar DB y objetos; probar restauración en entorno limpio.

7.  Migrar a plan/ proveedor de producción antes de datos reales y compromisos de servicio.

# 5. Excepciones y tratamiento de fallos

- Proveedor gratuito pausa o elimina recursos: recrear desde IaC, migraciones y backups.

- Límite de cuota: alertar y degradar de forma controlada.

- Región no adecuada: no cargar datos; seleccionar región compatible.

- Migración falla: mantener origen, restaurar backup y ejecutar reconciliación.

# 6. Artefactos que deben existir

- README de desarrollo

- Dockerfile / Compose

- Migraciones Alembic

- Configuración por entorno

- Runbook de backup y restore

- Inventario de proveedores y regiones

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
