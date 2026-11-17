> **Versión de trabajo en Markdown** del documento original `archive/originales/05_05_seguridad_clientes.docx`, convertida el 17/11/2026. Los diagramas originales se han sustituido por enlaces a su versión redibujada y corregida en `docs/atlas/`. Correcciones aplicadas: ver `docs/16-correcciones.md`. Nombre provisional del proyecto: Varios.

**ATLAS DE ARQUITECTURA DIGITAL**

Mapa 5 · Seguridad, identidad y aislamiento de clientes

La autorización ocurre en backend; no se confía en prompts, carpetas ni filtros visuales

Documento de diseño · versión 1.0 · noviembre 2026

# 1. Objetivo y alcance

Asegurar que cada usuario, agente y proceso accede únicamente a los datos autorizados.

Este mapa define el comportamiento objetivo y las responsabilidades de los componentes. No implica que todos estén implementados en el MVP.

# 2. Diagrama de flujo

**Diagrama redibujado:** [docs/atlas/08-seguridad.md](../atlas/08-seguridad.md)

# 3. Reglas de diseño

- No confiar en tenant_id enviado por el cliente: derivarlo de una identidad y autorización verificadas.

- Aplicar aislamiento en backend y base de datos; RLS es defensa adicional, no sustituto del diseño de permisos.

- Separar credenciales de usuario, servicio y agente; secretos en gestor dedicado.

- Los modelos reciben solo el mínimo contexto necesario; revisar tratamiento del proveedor y retención.

- Los documentos son datos no confiables: prompt injection nunca debe otorgar autoridad.

- Probar sistemáticamente accesos cruzados entre tenants y exportaciones.

# 4. Flujo operativo paso a paso

1.  Autenticar usuario o servicio.

2.  Resolver tenant y permisos desde identidad confiable.

3.  Construir contexto de seguridad inmutable para la petición.

4.  Autorizar cada lectura, escritura, exportación y herramienta.

5.  Aplicar RLS/controles de almacenamiento como segunda barrera.

6.  Minimizar/redactar contexto antes de enviar a modelos externos.

7.  Registrar accesos y denegaciones sin volcar secretos.

8.  Detectar, contener y gestionar incidentes según plan.

# 5. Excepciones y tratamiento de fallos

- Tenant no resuelto: deny by default.

- Token expirado o inválido: rechazar y renovar autenticación.

- RLS mal configurada: bloquear despliegue hasta superar tests.

- Fuga o acceso cruzado: revocar credenciales, contener, preservar evidencias y activar respuesta.

- Proveedor/modelo no aprobado: no enviar datos confidenciales.

# 6. Artefactos que deben existir

- Modelo de amenazas

- Matriz de acceso

- Políticas RLS y pruebas negativas

- Inventario de datos/proveedores

- Plan de respuesta a incidentes

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
