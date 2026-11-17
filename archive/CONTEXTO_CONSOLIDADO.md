# Contexto consolidado

El objetivo es una organización digital multisectorial con CEO digital que coordina departamentos, especialistas, procesos, conocimiento, herramientas y QA.

Acuerdos: modelo matricial; CEO como punto de entrada y orquestador; conocimiento RAW/WIKI/SCHEMA; Obsidian como interfaz humana y PostgreSQL como fuente operativa; Python/FastAPI, Pydantic, Docker y GitHub privado; Full Text Search primero y pgvector si se justifica; Process Engine explícito antes de orquestación compleja; Integration Hub desacoplado; Tool Gateway; aislamiento de clientes antes de recuperación; aprobación humana según riesgo; calidad mediante pruebas, evaluaciones, revisión y rollback; infraestructura remota para acceso móvil.

Análisis Sapira/Pharo: se tomó inspiración del enfoque de procesos completos, descubrimiento, conocimiento operativo, integración y despliegue junto al cliente. La arquitectura interna no es pública y las afirmaciones comerciales no se asumieron como métricas auditadas.

Coste: empezar con herramientas gratuitas y datos sintéticos; mocks antes de consumir API; no usar free tiers en producción ni con datos reales sin revisión; no comprar hardware adicional ni montar servidor doméstico al inicio.

Camino recomendado: elegir un proceso real, documentar AS-IS, diseñar TO-BE, fijar KPI y controles, construir motor mínimo, integrar un sistema, probar, pilotar y medir.

Otros proyectos personales y experimentos no deben mezclarse automáticamente con el núcleo ni con datos de clientes.