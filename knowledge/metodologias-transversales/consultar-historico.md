# Protocolo: consultar el histórico antes de empezar

**No reinventes la rueda.** Antes de empezar, busca si la organización ya hizo algo parecido.

1. **Comprende la petición:** objetivo, cliente y criterio de aceptación.
2. **Busca trabajos anteriores** en [`precedents/`](../../precedents/README.md): proyectos, soluciones, incidentes y lecciones.
3. **Revisa lo entregado:** en la oficina de agentes, el cerebro guarda qué leyó y qué entregó cada encargo.
4. **Consulta las decisiones** en [`DECISIONS.md`](../../DECISIONS.md).
5. **Revisa lo reutilizable:** plantillas en [`knowledge/plantillas/`](../plantillas/README.md), definiciones en [`processes/definitions/`](../../processes/definitions/README.md), código en `src/` y conectores en [`integrations/`](../../integrations/catalog/README.md).
6. **Comprueba errores pasados:** incidencias, retrabajo y correcciones ([`docs/16-correcciones.md`](../../docs/16-correcciones.md)).
7. **Decide qué se reutiliza tal cual.**
8. **Decide qué hay que adaptar** al caso nuevo.
9. **Decide qué hay que crear desde cero**, y por qué.
10. **Registra** en el entregable qué reutilizaste, qué adaptaste y por qué.

## Qué no se reutiliza sin más
- **Configuraciones de un cliente:** son suyas.
- **Información confidencial de un cliente:** nunca pasa al conocimiento común sin autorización y revisión de confidencialidad.
- **Soluciones antiguas:** antes de copiarlas, comprueba que siguen siendo válidas (norma vigente, versión de la herramienta, decisión no sustituida).

## Cómo buscar
- **Texto:** `grep -ri "palabra" knowledge processes precedents docs`.
- **Por tipo de tarea:** [`knowledge/navigation.json`](../navigation.json).
- **Desde la oficina:** el buscador del cerebro (tecla G), que usa el mismo repositorio.
