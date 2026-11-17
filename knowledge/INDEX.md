<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Índice del conocimiento de Varios

Punto de entrada para cualquier especialista, humano o agente. Antes de empezar una tarea:

1. Lee [DECISIONS.md](../DECISIONS.md) y [CLAUDE.md](../CLAUDE.md).
2. Busca precedentes en [precedents/](../precedents/README.md) ([protocolo](metodologias-transversales/consultar-historico.md)).
3. Localiza tu tarea en la tabla y abre lo que indica.
4. Si investigas fuera, sigue [investigar.md](metodologias-transversales/investigar.md) y registra la fuente.

Versión para máquinas: [navigation.json](navigation.json).

## Por tipo de tarea

| Tarea | Responsable | Consultar a | Procesos | Leer | Regla cruzada |
|---|---|---|---|---|---|
| Preparar una propuesta o responder a un pliego | [Especialista en propuestas y licitaciones](comercial/propuestas-licitaciones.md), [Director comercial](comercial/director-comercial.md) | [Especialista legal y privacidad](seguridad-legal/legal-privacidad.md), [Especialista en ciberseguridad](seguridad-legal/ciberseguridad.md), [Especialista en costes y proveedores](administracion-finanzas/costes-proveedores.md) | [P31](../processes/catalog/P31-calificacion-de-oportunidad.md), [P38](../processes/catalog/P38-gestion-de-despliegue-por-cliente.md) | [`docs/00-negocio.md`](../docs/00-negocio.md)<br>[`knowledge/comercial/`](comercial)<br>[`knowledge/seguridad-legal/`](seguridad-legal) | Comercial consulta a Legal antes de cualquier cláusula contractual. |
| Preparar o resumir una conversación de validación | [Director comercial](comercial/director-comercial.md) | [Arquitecto de procesos](procesos/arquitecto-procesos.md), [Especialistas sectoriales](procesos/especialista-sectorial.md) | [P32](../processes/catalog/P32-descubrimiento-de-procesos.md) | [`processes/referencia-seguros-apertura-siniestros/README.md`](../processes/referencia-seguros-apertura-siniestros/README.md)<br>[`docs/10-plan-12-semanas.md`](../docs/10-plan-12-semanas.md) | Se escucha, no se vende (D-011). |
| Descubrir o diseñar un proceso de cliente | [Arquitecto de procesos](procesos/arquitecto-procesos.md) | [Especialistas sectoriales](procesos/especialista-sectorial.md), [Especialista en métricas](procesos/metricas.md), [Especialista legal y privacidad](seguridad-legal/legal-privacidad.md) | [P32](../processes/catalog/P32-descubrimiento-de-procesos.md), [P33](../processes/catalog/P33-diseno-y-validacion-to-be.md), [P34](../processes/catalog/P34-gestion-de-definiciones-de-proceso.md) | [`processes/templates/proceso-cliente.md`](../processes/templates/proceso-cliente.md)<br>[`knowledge/procesos/sectores.md`](procesos/sectores.md) | Validar con quien ejecuta el proceso. |
| Diseñar una automatización | [Especialista en automatización](procesos/automatizacion.md), [Arquitecto de procesos](procesos/arquitecto-procesos.md) | [Arquitecto técnico](ingenieria/arquitecto-tecnico.md), [Especialista en ciberseguridad](seguridad-legal/ciberseguridad.md) | [P08](../processes/catalog/P08-ejecucion-de-tareas.md), [P21](../processes/catalog/P21-ejecucion-segura-de-herramientas.md), [P22](../processes/catalog/P22-gestion-de-errores-y-reintentos.md), [P36](../processes/catalog/P36-gestion-del-catalogo-de-conectores.md) | [`integrations/catalog/README.md`](../integrations/catalog/README.md)<br>[`processes/definitions/`](../processes/definitions) | Procesos consulta a Ingeniería antes de diseñar una automatización. |
| Habilitar una integración o conector | [Especialista en integraciones](ingenieria/integraciones.md) | [Especialista en ciberseguridad](seguridad-legal/ciberseguridad.md), [Especialista legal y privacidad](seguridad-legal/legal-privacidad.md) | [P21](../processes/catalog/P21-ejecucion-segura-de-herramientas.md), [P30](../processes/catalog/P30-gestion-de-identidades-y-secretos.md), [P36](../processes/catalog/P36-gestion-del-catalogo-de-conectores.md) | [`integrations/catalog/README.md`](../integrations/catalog/README.md)<br>[`integrations/contracts/`](../integrations/contracts) | Ingeniería consulta a Seguridad antes de habilitar una integración. |
| Aprobar un plan o tomar una decisión | [CEO digital](direccion/ceo-digital.md), [Responsable de decisiones y seguimiento](direccion/decisiones-seguimiento.md) | [Especialista en calidad y riesgos](seguridad-legal/calidad-riesgos.md) | [P05](../processes/catalog/P05-diseno-del-plan.md), [P10](../processes/catalog/P10-aprobacion-humana.md) | [`DECISIONS.md`](../DECISIONS.md)<br>[`precedents/`](../precedents) | El CEO consulta precedentes y decisiones antes de aprobar un plan. |
| Investigar una obligación legal o regulatoria | [Especialista legal y privacidad](seguridad-legal/legal-privacidad.md), [Responsable de cumplimiento](seguridad-legal/cumplimiento.md) | [Especialistas sectoriales](procesos/especialista-sectorial.md), [Bibliotecario / responsable de conocimiento](direccion/bibliotecario.md) | [P19](../processes/catalog/P19-politica-de-uso-y-limites.md), [P24](../processes/catalog/P24-gestion-del-ciclo-de-vida-del-dato.md) | [`docs/fuentes/Marco_Integral_Legal_Ciberseguridad_IA_Espana_UE_2026-11-16.md`](../docs/fuentes/Marco_Integral_Legal_Ciberseguridad_IA_Espana_UE_2026-11-16.md)<br>[`knowledge/fuentes/registro.md`](fuentes/registro.md) | Fuente primaria y vigente; nunca afirmar cumplimiento. |
| Trabajo en el sector seguros | [Especialistas sectoriales](procesos/especialista-sectorial.md) | [Arquitecto de procesos](procesos/arquitecto-procesos.md), [Responsable de cumplimiento](seguridad-legal/cumplimiento.md) | [P02](../processes/catalog/P02-clasificacion-y-triaje.md), [P32](../processes/catalog/P32-descubrimiento-de-procesos.md), [P33](../processes/catalog/P33-diseno-y-validacion-to-be.md) | [`knowledge/procesos/sectores.md`](procesos/sectores.md)<br>[`processes/referencia-seguros-apertura-siniestros/README.md`](../processes/referencia-seguros-apertura-siniestros/README.md) | El especialista de seguros consulta también los procesos transversales. |
| Cambiar de modelo o de instrucciones | [Arquitecto de datos e IA](ingenieria/datos-ia.md), [Especialista en evaluación de IA](ingenieria/evaluacion-ia.md) | [Especialista en calidad y riesgos](seguridad-legal/calidad-riesgos.md) | [P16](../processes/catalog/P16-gobierno-de-modelos-e-instrucciones.md), [P23](../processes/catalog/P23-evaluacion-de-agentes-y-modelos.md), [P25](../processes/catalog/P25-gestion-de-cambios-y-versiones.md) | [`docs/atlas/10-cambios-modelos.md`](../docs/atlas/10-cambios-modelos.md)<br>[`processes/tests/README.md`](../processes/tests/README.md) | Sin evaluación superada no hay cambio. |
| Gestionar un incidente | [Especialista en ciberseguridad](seguridad-legal/ciberseguridad.md), [Especialista en calidad y riesgos](seguridad-legal/calidad-riesgos.md) | [Especialista legal y privacidad](seguridad-legal/legal-privacidad.md) | [P28](../processes/catalog/P28-gestion-de-incidentes.md), [P15](../processes/catalog/P15-observabilidad-e-incidencias.md), [P17](../processes/catalog/P17-seguridad-y-continuidad.md) | [`processes/runbooks/`](../processes/runbooks)<br>[`precedents/incidents/`](../precedents/incidents) | Preservar evidencias antes de corregir. |
| Añadir o actualizar conocimiento | [Bibliotecario / responsable de conocimiento](direccion/bibliotecario.md) | el dueño del tema | [P13](../processes/catalog/P13-aprendizaje-y-actualizacion-de-la-wiki.md), [P04](../processes/catalog/P04-recuperacion-de-conocimiento.md) | [`knowledge/metodologias-transversales/`](metodologias-transversales)<br>[`knowledge/fuentes/registro.md`](fuentes/registro.md) | Buscar antes de crear; draft hasta revisión. |
| Dar de alta un proveedor o herramienta | [Especialista en costes y proveedores](administracion-finanzas/costes-proveedores.md) | [Especialista legal y privacidad](seguridad-legal/legal-privacidad.md), [Especialista en ciberseguridad](seguridad-legal/ciberseguridad.md), [Arquitecto técnico](ingenieria/arquitecto-tecnico.md) | [P27](../processes/catalog/P27-gestion-de-proveedores-y-dependencias.md), [P29](../processes/catalog/P29-gestion-de-costes-y-capacidad.md) | [`integrations/catalog/README.md`](../integrations/catalog/README.md)<br>[`knowledge/plantillas/ficha-proveedor.md`](plantillas/ficha-proveedor.md) | Licencia, datos, región, retención, salida. |
| Facturar o preparar trámites | [Especialista administrativo](administracion-finanzas/administrativo.md), [Especialista financiero](administracion-finanzas/financiero.md) | — | [P11](../processes/catalog/P11-entrega-y-cierre.md) | [`knowledge/administracion-finanzas/`](administracion-finanzas) | Fechas de Verifactu y factura electrónica según norma vigente. |

## Por departamento

### [Dirección y gobierno](direccion/README.md)
Clasifica, decide, registra y mantiene el conocimiento.

- [CEO digital](direccion/ceo-digital.md)
- [Bibliotecario / responsable de conocimiento](direccion/bibliotecario.md)
- [Responsable de decisiones y seguimiento](direccion/decisiones-seguimiento.md)

### [Comercial y clientes](comercial/README.md)
Valida, prospecta, propone y cuida la relación.

- [Director comercial](comercial/director-comercial.md)
- [Especialista en prospección](comercial/prospeccion.md)
- [Especialista en marketing y contenido](comercial/marketing-contenido.md)
- [Especialista en propuestas y licitaciones](comercial/propuestas-licitaciones.md)
- [Especialista en gestión de clientes](comercial/gestion-clientes.md) · sin puesto en la oficina

### [Procesos y operaciones](procesos/README.md)
Descubre, diseña, implanta y mide procesos.

- [Arquitecto de procesos](procesos/arquitecto-procesos.md)
- [Responsable de implantación de clientes](procesos/implantacion-clientes.md) · sin puesto en la oficina
- [Especialista en automatización](procesos/automatizacion.md)
- [Especialista en métricas](procesos/metricas.md)
- [Especialistas sectoriales](procesos/especialista-sectorial.md)

### [Ingeniería y tecnología](ingenieria/README.md)
Construye la plataforma, la IA y las integraciones.

- [Arquitecto técnico](ingenieria/arquitecto-tecnico.md)
- [Especialista backend](ingenieria/backend.md)
- [Arquitecto de datos e IA](ingenieria/datos-ia.md)
- [Especialista en integraciones](ingenieria/integraciones.md)
- [Especialista en evaluación de IA](ingenieria/evaluacion-ia.md)

### [Seguridad, privacidad, legal y cumplimiento](seguridad-legal/README.md)
Que nada falle, se filtre ni incumpla.

- [Especialista en ciberseguridad](seguridad-legal/ciberseguridad.md)
- [Especialista legal y privacidad](seguridad-legal/legal-privacidad.md)
- [Responsable de cumplimiento](seguridad-legal/cumplimiento.md) · sin puesto en la oficina
- [Especialista en calidad y riesgos](seguridad-legal/calidad-riesgos.md)

### [Administración y finanzas](administracion-finanzas/README.md)
Empresa, costes, proveedores y facturación.

- [Especialista financiero](administracion-finanzas/financiero.md)
- [Especialista en costes y proveedores](administracion-finanzas/costes-proveedores.md)
- [Especialista administrativo](administracion-finanzas/administrativo.md)

## Transversal

- [Fuentes](fuentes/registro.md) · [Metodologías](metodologias-transversales/README.md) · [Plantillas](plantillas/README.md) · [Glosario](glosario/README.md)
- [Catálogo de procesos P01–P38](../processes/catalog/README.md) · [Integraciones](../integrations/catalog/README.md) · [Precedentes](../precedents/README.md) · [Gobierno](../governance/README.md)
