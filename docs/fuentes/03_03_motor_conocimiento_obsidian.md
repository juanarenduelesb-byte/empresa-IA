> **Versión de trabajo en Markdown** del documento original `archive/originales/03_03_motor_conocimiento_obsidian.docx`, convertida el 17/11/2026. Los diagramas originales se han sustituido por enlaces a su versión redibujada y corregida en `docs/atlas/`. Correcciones aplicadas: ver `docs/16-correcciones.md`. Nombre provisional del proyecto: Varios.

**ATLAS DE ARQUITECTURA DIGITAL**

Mapa 3 · Motor de conocimiento con Obsidian

Obsidian es la interfaz de conocimiento; el backend aplica permisos, indexa y recupera

Documento de diseño · versión 1.0 · noviembre 2026

# 1. Objetivo y alcance

Definir cómo entran, se validan, se relacionan, se recuperan y se actualizan los conocimientos sin confundir notas con fuente de verdad operativa.

Este mapa define el comportamiento objetivo y las responsabilidades de los componentes. No implica que todos estén implementados en el MVP.

# 2. Diagrama de flujo

**Diagrama redibujado:** [docs/atlas/07-conocimiento.md](../atlas/07-conocimiento.md)

# 3. Reglas de diseño

- Obsidian no es la base de datos transaccional ni el motor de permisos.

- El backend filtra por identidad, cliente, proyecto y clasificación antes de recuperar contenido.

- Cada afirmación relevante debe poder rastrearse a una fuente, versión y ubicación.

- Estados de conocimiento: raw, draft, validated, approved, deprecated, disputed.

- La IA puede proponer cambios; el contenido de alto impacto requiere aprobación humana.

- No almacenar secretos ni documentos confidenciales de clientes en el vault corporativo compartido.

# 4. Flujo operativo paso a paso

1.  Recibir documento en zona de cuarentena.

2.  Calcular hash, analizar tipo, malware y permisos.

3.  Extraer texto y metadatos conservando vínculo al original.

4.  Proponer notas Markdown con plantilla y citas a fuentes.

5.  Ejecutar lint: campos obligatorios, enlaces rotos, duplicados y consistencia.

6.  Revisión humana según sensibilidad y criticidad.

7.  Publicar en vault y versionar en Git según clasificación permitida.

8.  Indexar contenido autorizado; mantener filtros de acceso en cada consulta.

9.  Recuperar fragmentos con referencias para el CEO.

10. Proponer actualizaciones tras proyectos; no autoaprobar.

# 5. Excepciones y tratamiento de fallos

- Extracción incompleta: marcar calidad baja y solicitar revisión/manual OCR.

- Fuente contradictoria: estado disputed y mostrar ambas fuentes.

- Fuente obsoleta: deprecated; no eliminar evidencia histórica.

- Permiso insuficiente: denegar retrieval aunque exista índice o enlace.

- Confidencialidad cliente: vault/repositorio aislado o almacenamiento específico; nunca copiar a Wiki global.

# 6. Artefactos que deben existir

- Plantillas Markdown y esquema de propiedades

- Política de clasificación y estados

- Pipeline de ingesta y lint

- Índice de búsqueda y política de retrieval

- Registro de procedencia y versiones

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
