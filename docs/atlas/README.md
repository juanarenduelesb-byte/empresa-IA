# Atlas de diagramas

Fuente única: `tools/atlas_data.py` (genera la web y estos archivos). GitHub dibuja los diagramas Mermaid directamente.

Leyenda de colores: turquesa = IA · blanco = reglas fijas · burdeos claro = persona · ocre = decisión · rojo = parada o error · verde = resultado.

| Nº | Mapa | Grupo |
|---|---|---|
| 00 | [Arquitectura del cerebro digital](00-arquitectura.md) | Visión general |
| 01 | [Organización: modelo matricial](01-organizacion.md) | Visión general |
| 02 | [Flujo completo del CEO digital](02-flujo-ceo.md) | El CEO digital |
| 03 | [Las cinco decisiones del CEO](03-decisiones-ceo.md) | El CEO digital |
| 04 | [Ejecución: motor de procesos, agentes y herramientas](04-ejecucion.md) | Ejecución |
| 05 | [Puerta de herramientas](05-gateway.md) | Ejecución |
| 06 | [Fallos, reintentos y recuperación](06-fallos.md) | Ejecución |
| 07 | [Motor de conocimiento con Obsidian](07-conocimiento.md) | Conocimiento |
| 08 | [Seguridad, identidad y aislamiento de clientes](08-seguridad.md) | Seguridad |
| 09 | [Calidad, evaluación y aprobación humana](09-calidad.md) | Calidad y gobierno |
| 10 | [Cambios y elección de modelos de IA](10-cambios-modelos.md) | Calidad y gobierno |
| 11 | [Infraestructura, desarrollo y portabilidad](11-infraestructura.md) | Infraestructura |
| 12 | [Ciclo de vida de un proyecto con cliente](12-ciclo-proyecto.md) | Clientes |
| 13 | [Ciclo de vida de un dato](13-ciclo-dato.md) | Seguridad |
| 14 | [Operación y respuesta a incidentes](14-incidentes.md) | Seguridad |
| 15 | [Conversación entre componentes](15-componentes.md) | Infraestructura |
| 16 | [Estados de un encargo](16-estados.md) | Ejecución |

## Criterios comunes a todos los mapas

Los mapas originales 2 a 9 repetían el mismo texto en sus apartados 7, 8 y 9. Se consolida aquí una sola vez:

- El flujo se puede ejecutar de extremo a extremo en un entorno de pruebas.
- Entradas, salidas, responsables, estados y decisiones quedan registrados.
- Se prueban los casos de error y denegación, no solo el camino feliz.
- Los permisos se verifican en el servidor y se prueban con identidades distintas.
- Hay documentación suficiente para que otra persona mantenga y despliegue el componente.

**Prioridad:** MVP = recorrido mínimo con estados guardados. Antes de datos reales de clientes = seguridad, privacidad, copias, recuperación, evaluación y contratos de proveedores. Escalado = colas, observabilidad avanzada y redundancia cuando el uso lo justifique.
