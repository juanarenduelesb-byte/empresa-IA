<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Conversaciones con CEO digital

**CEO digital** · 2026-11-17 21:25

**Entrega: Acta de protección de la IA y examen de 50 casos**

## Acta de reunión y aplicación a Varios: protección de la IA y examen de 50 casos

**Estado:** borrador. No se ha enviado, publicado ni aplicado. Pendiente de revisión de Juan y Álvaro. Nada de esto es asesoría jurídica.

**Convención:**
- **Hecho:** consta en las secciones del cerebro facilitadas para este encargo. Se cita la ruta entre corchetes.
- **Hipótesis:** razonable, sin validar.
- **Propuesta:** lo que recomienda este borrador. Ninguna propuesta es una decisión tomada.
- **[POR CONFIRMAR]:** no consta en el material o no se ha podido contrastar.

**Sobre las fuentes:** el material facilitado incluye las secciones de `docs/10-plan-12-semanas.md`, `DECISIONS.md`, `docs/12-simulacion.md`, `CLAUDE.md` y `docs/11-cerebro-en-claude.md` como extractos. No se han abierto los archivos completos. Lo que no aparece en un extracto se marca [POR CONFIRMAR], sin darlo por inexistente.

## Resumen

- Las propuestas del acta parecen caber en el plan D-011 sin mover los controles. El mayor impacto recae en S3 y en el control A (18/12/2026).
- Hay cinco puntos que los socios deben resolver antes de aprobar nada:
  1. Fecha del umbral: el acta lo pide antes del control A y `DECISIONS.md` lo fija antes del 22/01/2027.
  2. Test de contexto: el acta lo sitúa en S3, pero el adaptador de modelos llega en S4 según la fila de S4 del plan, por lo que en S3 aún no existe el punto donde se construye ese contexto (hipótesis).
  3. Capas obligatorias frente a refuerzo.
  4. Condición previa a L2: no consta como decisión pendiente.
  5. Qué impide acciones entre S4 y S6, antes de que exista la puerta de herramientas.
- Ninguna propuesta está aprobada. Los socios no asistieron. Si las aprueban, se anota una línea por decisión en `DECISIONS.md`.
- Las fechas de S3 a S6 que figuran abajo proceden del extracto del plan. Hay que contrastarlas con el documento original.

## 1. Datos de la reunión

- **Fecha:** [POR CONFIRMAR]
- **Ruta sugerida en el repositorio:** [POR CONFIRMAR]
- **Asistentes:** IA y evaluación (Ingeniería) y Seguridad (Calidad-seguridad-legal). Juan y Álvaro no asistieron.
- **Tema:** cómo proteger la IA del producto (CEO digital, adaptador de modelos y puerta de herramientas) y cómo medirlo con el examen de 50 casos (S9) y las 5 trampas del control A (18/12/2026).

## 2. Hechos

Los hechos de la reunión proceden del acta. Los del plan y de las decisiones pendientes se citan con su ruta.

**Del acta**
- El plan vigente (D-011) fija el control A el 18/12/2026 (20 casos + 5 trampas), la seguridad y el aislamiento de clientes en S3, la puerta de herramientas en S6 y el examen de 50 casos en S9.
- Hasta L2 solo se usan datos inventados.
- Con 50 casos no se puede prometer un porcentaje de robustez general. Solo se informa de qué casos pasan y cuáles no.

**Del extracto del plan** [docs/10-plan-12-semanas.md › Semana a semana]
- S2 (30 nov–6 dic): modelo de datos con "ejecución de modelo" y auditoría. Álvaro termina los 20 casos con resultado esperado.
- S3 (7–13 dic, con festivo el 8): para Juan, autenticación, roles, cliente deducido de la identidad, dos clientes señuelo, tests de acceso cruzado y secretos en entorno. Para Álvaro, política de uso, matriz de aprobaciones y 2.ª conversación. "Hecho cuando": "Acceso cruzado falla siempre por diseño". "Si da tiempo": RLS en PostgreSQL.
- S4 (14–20 dic): para Juan, adaptador de modelos (simulado + Claude API), clasificación confirmado/inferido/desconocido, cinco decisiones con motivo y límite de coste. Para Álvaro, probar con los casos y 5 peticiones trampa. "Hecho cuando": Control A.
- S6 (28 dic–3 ene): catálogo de capacidades y puerta de herramientas con lista cerrada. La fila del extracto está incompleta: [POR CONFIRMAR] contra el original.
- La fecha de S9 no consta en el extracto: [POR CONFIRMAR].

**Lista maestra** [docs/10-plan-12-semanas.md › Lista maestra a 12/02/2027]
- Ya figuran "tests de separación", "pruebas de instrucciones escondidas", "examen de 50 casos superado" y "lista para L2".
- No figuran un umbral explícito ni una prueba de aislamiento previa a L2.

**Decisiones pendientes** [DECISIONS.md › Decisiones pendientes (con fecha límite)]
- "Umbral de acierto del examen": los dos socios, antes del 22/01/2027.
- "Proveedor de identidad para producción": Juan, antes de L2.

**Reglas** [CLAUDE.md › Reglas]
- Solo datos inventados en pruebas.
- El cliente se obtiene de la identidad autenticada, nunca de un dato del usuario.
- Cualquier acción externa, financiera, legal o contractual requiere aprobación humana.
- Toda decisión estructural se registra en `DECISIONS.md`.

**Simulación** [docs/12-simulacion.md › Casos]
- Caso A: los partes con lesiones (datos de salud) salen del flujo automático y el tramitador aprueba cada apertura.

## 3. Acuerdos entre departamentos

No son decisiones de los socios. Son la base de trabajo de Ingeniería y Seguridad.

1. El texto externo (correos, PDFs de siniestros) se trata como dato y no como instrucción. Las instrucciones del sistema van aparte.
2. El modelo propone y no ejecuta. La puerta de herramientas decide y ninguna acción se aprueba a sí misma.
3. La salida se valida contra un esquema estricto (campos confirmados, inferidos o desconocidos). Si no valida, el CEO pregunta o escala.
4. Cada llamada al modelo se registra en auditoría (versión de instrucciones, modelo, resultado) para poder repetir cualquier examen.
5. El examen completo se repite ante cada cambio de modelo o de instrucciones.
6. El examen incluye una parte adversa: inyección en documentos, intentos de saltar el aislamiento entre clientes y peticiones de acciones prohibidas. Las 5 trampas del control A son su primera versión.
7. Solo se informa de qué casos pasan y cuáles no, sin prometer un porcentaje general.

## 4. Desacuerdos abiertos

| Tema | Posición de IA y evaluación | Posición de Seguridad | Estado |
|---|---|---|---|
| Valor de la regla del adaptador | La impone el adaptador de modelos | No basta: la inyección puede colarse. La defensa real es que el modelo no pueda ejecutar nada ni ver datos de otro cliente | Abierto. Hipótesis de Seguridad, no validada |
| Umbral de aprobación | [POR CONFIRMAR] con Seguridad | Cero fallos en aislamiento y acciones prohibidas. En el resto, análisis y corrección antes del control | Abierto. Lo deciden los socios |
| Riesgo de L2 | Riesgo abierto: con datos inventados no se prueba la fuga real | No se pasa a L2 sin prueba de aislamiento con dos clientes ficticios | Abierto |
| Realismo de los casos adversos | Pide a Seguridad la lista y un validador | Seguridad redacta, Ingeniería ejecuta, Álvaro revisa el realismo desde la correduría | Abierto. Fecha [POR CONFIRMAR] |

## 5. Cómo aplicarlo a Varios

Todo lo de esta sección es propuesta, salvo lo marcado como hecho.

### 5.1 Umbral: separar control A y examen de S9

- **Hecho:** el extracto del plan describe el control A como hito de S4 ("Probar con los casos; 5 peticiones trampa"). No muestra criterio de aprobación. [POR CONFIRMAR] si el plan completo lo define en otro apartado.
- **Hecho:** "Umbral de acierto del examen" tiene fecha límite 22/01/2027. El acta propone confirmarlo antes del 18/12/2026.
- **Propuesta:** dos criterios.
  - Criterio del control A: cero fallos en los casos de aislamiento y de acciones prohibidas. En el resto, cada fallo se analiza y se corrige. Lo deciden los socios antes del 18/12/2026.
  - Umbral general del examen de 50 casos: se mantiene la fecha del 22/01/2027 hasta que los socios decidan otra cosa. El criterio del control A se enlaza con esa decisión, no la sustituye.
- No se cambia ninguna fecha de `DECISIONS.md` hasta que Juan y Álvaro lo decidan.

### 5.2 Test del contexto enviado al modelo

- El test construye el contexto exacto que recibe el modelo para el cliente A y falla si aparece cualquier identificador del cliente B. Cubre lo que PostgreSQL no vería.
- **Problema:** según el extracto, el adapt
