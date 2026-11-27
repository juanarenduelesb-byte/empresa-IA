# 17 · Cerebro, conocimiento y procesos: auditoría e informe

**Fecha:** 17/11/2026 · **Estado:** draft · **Encargo:** «Prompt maestro: construcción del cerebro, investigación, conocimiento y automatización».

Este documento dice qué había, qué se ha construido y qué falta. Separa hecho, hipótesis y propuesta.

> **Actualización del 17/11/2026 (tarde):**
> - Nuevo departamento de [Sectores](../knowledge/sectores/README.md) con seis expertos y una [priorización](../knowledge/sectores/priorizacion.md) en estado de propuesta. Ahora son 30 especialistas en 7 departamentos.
> - 13 fuentes más, 53 en total. La de factura electrónica B2B ya tiene calendario oficial.
> - La oficina de agentes tiene proyectos, entregables en archivos reales, memoria y lectura de Google Drive (D-015, propuesta).
> - Las cifras de abajo son las del primer informe.
>
> **Nota del 27/11/2026:** este informe describe el 17/11. Lo que dicen §9 y §10 del motor «en memoria», sin PostgreSQL, RLS, API ni identidad, está superado: desde el 26/11 hay PostgreSQL con RLS forzada, auditoría inmutable, una API con identidad por token firmado (provisional, D-028) y pruebas contra PostgreSQL real, también de acceso cruzado entre clientes ([24-base-de-datos.md](24-base-de-datos.md)). Las demás limitaciones de §10 siguen en pie.

## 1. Estado antes
- **Documentación:** 52 documentos y 12 decisiones (D-001 a D-012).
- **Oficina de agentes:** artifact con su cerebro (`oficina/brain.json`).
- **Carpetas casi vacías:** `knowledge/` solo tenía principios y plantillas, y `processes/` un README.
- **No existían:** `integrations/` ni `precedents/`.
- **Código:** 0 líneas.

## 2. Estado después (hechos comprobables en el repositorio)
| Pieza | Dónde | Cantidad |
|---|---|---|
| Fichas de especialistas | `knowledge/<departamento>/` | 25 en 6 departamentos |
| Índice y navegación por tipo de tarea | `knowledge/INDEX.md`, `knowledge/navigation.json` | 13 tipos de tarea |
| Registro de fuentes con metadatos | `knowledge/fuentes/` | 40 fuentes |
| Protocolos | `knowledge/metodologias-transversales/` | consultar histórico, investigar, contrastar, guardar |
| Plantillas | `knowledge/plantillas/` | 7 |
| Fichas de proceso con 20 apartados y diagrama | `processes/catalog/` | 38 (P01–P38) |
| Definiciones ejecutables | `processes/definitions/` | 3 JSON |
| Runbooks | `processes/runbooks/` | 6 (sin ensayar) |
| Proceso de referencia | `processes/referencia-seguros-apertura-siniestros/` | AS-IS hipotético y preguntas |
| Catálogo de integraciones y software libre | `integrations/catalog/` | 6 conectores previstos, 8 proyectos evaluados |
| Contratos de datos | `integrations/contracts/` | 2 JSON Schema |
| Precedentes | `precedents/` | 4 entradas y 2 plantillas |
| Motor mínimo | `src/varios/procesos/` | estados, motor, reintentos, definiciones |
| Pruebas | `tests/` | 36, todas pasan |
| Comprobador del repositorio | `tools/check_repo.py` | enlaces, fichas, fuentes, secretos |

## 3. Especialistas
Seis departamentos: dirección, comercial, procesos, ingeniería, seguridad y legal, y administración y finanzas. Cada ficha tiene:
- **Índice (10 campos):** misión, responsabilidades, qué consulta, procesos, herramientas, a quién convoca, permisos, aprobación, plantillas y precedentes.
- **Conocimiento (12 apartados):** fundamentos, metodologías, normativa, herramientas, procedimiento, casos, criterio de calidad, errores frecuentes, KPI, límites y lagunas, más sus fuentes.

Tres especialistas no tienen puesto en la oficina (gestión de clientes, implantación y cumplimiento), porque hoy no hay clientes.

**Hipótesis:** 25 especialistas son más de los que dos socios pueden mantener. Es probable que en el piloto actúen 6–8.

## 4. Fuentes
Hay 40 fuentes con organismo, URL, versión, autoridad, vigencia y estado. **Calendario de Verifactu:** estuvo disputado (VERIFACTU-2028) hasta que el RDL 43/2026, publicado el 25/11/2026, fijó el 06/10/2028 (VERIFACTU-RDL43, pendiente de convalidación). Las fuentes de software libre se consultaron el 17/11/2026.

## 5. Procesos P01–P38
- **P01–P30** salen de la Guía v1.4. **P31–P38** salen del Atlas de Evolución y siguen como propuesta.
- **Implementado en código:** P10 (aprobación), P22 (reintentos e idempotencia) y P34 (validación de definiciones).
- **Parcial:** P01 y P08, solo como transiciones del motor.
- **El resto:** solo documentación.

## 6. Hallazgos de la auditoría
1. **La tabla de estados de la Guía §4 tiene huecos.** No dice cómo se sale de PENDIENTE_INFO sin respuesta, de RETRABAJO, de ESCALADO ni de REABIERTO. Se han añadido esas transiciones, marcadas como *añadida (confirmar)* en `encargo.json`.
2. **La lista de estados del encargo omite dos que usa la propia Guía.** Omite ESCALADO y RETRABAJO, aunque la tabla de la Guía sí los usa. Se ha seguido la tabla.
3. **`governance/README.md` dice que el marco legal está pendiente de incorporar,** pero ya está en `docs/fuentes/`. La corrección va en una propuesta aparte para un socio.
4. **`processes/README.md` mezclaba dos cosas distintas:** los procesos de Varios y los procesos de cliente. Ahora se distinguen (`catalog/` frente a una carpeta por proceso de cliente).
5. **No había contrato de datos ni de auditoría.** Ahora hay dos esquemas.

## 7. Conectores
No hay ninguno construido. Hay 6 previstos en el catálogo. Los portales de aseguradoras no tienen API pública conocida (**laguna**).

## 8. Software libre evaluado
- **Ninguno adoptado.**
- **n8n:** su licencia restringe ofrecerlo a terceros alojado por nosotros.
- **Camunda 8:** requiere licencia de pago en producción.
- **Langfuse:** la auditoría solo está en la edición Enterprise.
- **Presidio:** necesita configuración para español.
- **Pendiente:** revisar los avisos de seguridad (CVE) de cada proyecto.
- **Graphify** (Apache-2.0), revisado el 17/11/2026: no se adopta como dependencia (está pensado para código y necesita NetworkX, Leiden y un modelo para los documentos). Se reimplementan sus mejores ideas en `tools/grafo.py`, sin dependencias ni IA (D-018): relaciones con etiqueta de confianza, comunidades con etiqueta sin IA, nodos centrales, puentes, conexiones sorprendentes, preguntas sugeridas, informe del grafo, consulta con presupuesto y camino con la confianza del eslabón más débil.

## 9. Pruebas
Hay 36 pruebas automáticas que cubren:
- las transiciones;
- el aislamiento entre clientes en memoria;
- que nadie se aprueba a sí mismo, que un agente no aprueba y que la versión aprobada coincide;
- el QA directo solo con riesgo bajo;
- los reintentos solo con errores transitorios, y la idempotencia;
- la validación de definiciones;
- los enlaces internos, la completitud de las fichas, las fuentes, los secretos y que lo generado está al día.

Se ejecutan con `python3 -m pytest` y `ruff check src tests tools/check_repo.py`.

## 10. Errores y limitaciones
- **El motor vive en memoria.** No hay PostgreSQL, ni RLS, ni API, ni identidad real: el aislamiento solo está probado en memoria.
- **Nada está validado por una persona.** Todo el conocimiento está en draft.
- **Las fichas de seguridad y legal no son asesoría jurídica.**
- **Los runbooks no se han ensayado.**
- **El AS-IS del proceso de referencia es una hipótesis** hasta las entrevistas.
- **Ruff solo se aplica al código nuevo:** las herramientas antiguas (`tools/gen.py`, `tools/org_gen.py` y otras) tienen avisos de estilo pendientes.

## 11. Cambios publicados
- **Propuesta A (aceptada sola según D-012):** conocimiento, procesos, integraciones, precedentes, motor, pruebas, web, cerebro, D-013 y D-014 como propuestas.
- **Propuesta B (queda abierta para un socio):** las seis políticas de `governance/`, la corrección del README de gobierno y la estructura en CLAUDE.md.

## 12. Lagunas
- Volúmenes y tiempos reales del proceso de referencia.
- API de los programas de gestión de corredurías y de los portales de aseguradoras.
- Proveedor de identidad.
- Región de datos.
- Umbral del examen.
- Contenido sectorial fuera de seguros.
- CVE del software libre.

## 13. Prioridades propuestas
1. **Decidir el proceso de referencia** (vence el 22/11) y hacer la primera entrevista con las preguntas de su README.
2. **Revisar y aprobar o cambiar D-013 y D-014,** y fusionar la propuesta B.
3. **Plan, semanas 1 a 5:** llevar el motor a PostgreSQL con RLS y pruebas negativas de aislamiento.
4. **Reducir los especialistas activos** a los que usa el proceso de referencia.

## 14. Cómo mantenerlo
- Cambiar datos en `tools/org_data/`.
- Ejecutar `python3 tools/org_gen.py` y `python3 tools/agentes_gen.py`.
- Ejecutar `python3 tools/brain_build.py oficina/brain.json`: genera el cerebro con su grafo de conocimiento y el informe `knowledge/grafo/INFORME.md` (D-018). GitHub Actions lo hace solo cuando cambian documentos en `main`.
- Explorar el grafo: `python3 tools/grafo.py consulta "pregunta"`, `camino "A" "B"`, `explica "X"`.
- Ejecutar `python3 -m pytest`.

## Obsidian

El repositorio se abre como vault de Obsidian: notas por decisión y fuente, mapas del grafo y tablas de Bases, generados por `tools/obsidian_gen.py`. Montaje y reglas en [19-obsidian.md](19-obsidian.md) (D-021).
