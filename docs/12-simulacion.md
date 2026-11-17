# Simulación del cerebro

Versión interactiva: `site/simulacion.html`. Los tres casos son **ejemplos inventados**; empresas, cifras y tiempos no son reales.

## Los 12 pasos

| # | Paso | Quién | Qué pasa |
|---|---|---|---|
| 1 | Entra la petición | Reglas | Se identifica quién pide y de qué cliente es |
| 2 | Entender | IA | Intención, objetivo, sector, proceso, resultado esperado |
| 3 | Preguntar lo que falta | IA | Se pregunta, no se inventa |
| 4 | Clasificar y riesgo | Reglas + IA | Complejidad, impacto, datos, leyes → nivel bajo / medio / alto |
| 5 | Consultar conocimiento | Reglas | Permisos antes de buscar; otros clientes bloqueados |
| 6 | Hacer el plan | IA | Tareas con dependencias; cada una marcada IA, reglas o persona |
| 7 | Asignar | Reglas | Departamento + perfil sectorial + herramientas mínimas |
| 8 | Aprobaciones | Persona | Según nivel de riesgo |
| 9 | Ejecutar | Motor de procesos | En cola → en marcha → espera persona → terminada (o bloqueada) |
| 10 | Control de calidad | Reglas + persona | Si algo falla, no se corrige a ciegas: se marca |
| 11 | Entregar | Reglas | Resultado + evidencias + límites |
| 12 | Registro y aprendizaje | Reglas + persona | Todo auditado; lo aprendido entra como borrador y lo aprueba una persona |

## Casos

**A · Correduría, siniestros por correo (riesgo medio).** IA lee y extrae; reglas comprueban póliza y cobertura; los partes con lesiones (datos de salud) salen del flujo automático; el tramitador aprueba cada apertura; una fecha ambigua se marca para revisión.

**B · Gestoría, conciliación de facturas (riesgo alto en dinero).** El cuadre exacto lo hacen reglas, nunca la IA. La IA solo lee facturas y propone pareja en dudosos con explicación. El sistema no tiene herramientas de pago ni de contabilidad.

**C · Clínica, resumen de historiales (riesgo alto, se para).** Sin evaluación de impacto de protección de datos no se procesa ningún dato real. Se trabaja con historiales inventados y revisión médica; la tarea con datos reales nace bloqueada. Entregable: informe de viabilidad, no sistema.
