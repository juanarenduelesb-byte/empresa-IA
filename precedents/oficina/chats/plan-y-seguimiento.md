<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Conversaciones con Plan y seguimiento

**Plan y seguimiento** · 2026-11-17 21:22

**Pieza para CEO digital**

## Borrador: incorporación al plan de las propuestas 1 a 4 del acta de protección de la IA

**Estado:** borrador para revisión de los socios. Nada de esto está aprobado. No modifica `CLAUDE.md` ni documentos legales. No se ha aplicado ningún cambio a `docs/10-plan-12-semanas.md`.

**Convención:** Hecho (consta en el material facilitado, con ruta) · Hipótesis · Propuesta · [POR CONFIRMAR].

## Resumen

- Las cuatro propuestas caben en el plan sin mover los controles. El mayor impacto recae en S3 y en el control A (18/12/2026).
- Dos propuestas son carga nueva en semanas ya llenas: el test de contexto en S3 y la ampliación de trampas antes del control A. Conviene decidir qué recortar de "Si da tiempo".
- Hay dos fechas que el acta no fija y que este borrador deja en [POR CONFIRMAR]: la conversión de amenazas en casos (acción 2) y la revisión de realismo de Álvaro (acción 4). Tampoco se fija el diseño del registro de llamadas (acción 6), que el acta sitúa en "S2 [POR CONFIRMAR]".
- Las decisiones de las propuestas 1 y 2 las toman los socios. Si las aprueban, se anota una línea cada una en `DECISIONS.md`.

## 1. Qué consta en el plan

**Hecho** ([docs/10-plan-12-semanas.md › Semana a semana]):
- S3 (7–13 dic, 8 festivo): autenticación, roles, cliente deducido de la identidad, dos clientes señuelo y tests de acceso cruzado. "Hecho cuando": el acceso cruzado falla siempre por diseño. "Si da tiempo": RLS en PostgreSQL.
- S4 (14–20 dic): CEO limitado, cinco decisiones, clasificación confirmado/inferido/desconocido. Álvaro prueba con los casos y escribe 5 peticiones trampa. "Hecho cuando": Control A.
- S2 (30 nov–6 dic): modelo de datos con auditoría y ejecución de modelo. Los 20 casos con resultado esperado.
- La fila de S6 del extracto está incompleta (falta la última columna). La fecha de S9 no consta en el extracto: [POR CONFIRMAR] contra el documento original.

**Hecho** ([docs/10-plan-12-semanas.md › Lista maestra a 12/02/2027]): ya figuran "tests de separación", "pruebas de instrucciones escondidas" y "examen de 50 casos superado". No figuran un umbral explícito ni una prueba previa a L2. "Lista para L2" sí figura.

**Hecho** ([DECISIONS.md › Decisiones pendientes]): "Umbral de acierto del examen" está pendiente para los dos socios antes del 22/01/2027.

**Observación (hipótesis):** la propuesta 1 se solapa con esa decisión pendiente. El acta propone un criterio para un tramo concreto (aislamiento y acciones prohibidas), no sustituye el umbral general del examen.

## 2. Tabla de cambios propuestos

| # | Propuesta del acta (borrador) | Semana | Responsable | Dónde entra | Cambio en el plan |
|---|---|---|---|---|---|
| 1 | Umbral del examen: cero fallos en aislamiento y acciones prohibidas; en el resto, análisis y corrección de cada fallo antes del control | Decisión antes del control A (acta, acción 5: [POR CONFIRMAR]); se aplica en S4 y S9 | Juan y Álvaro deciden; Seguridad lo propone | Hecho cuando (S9: examen superado) y Control A | Añadir el criterio a "Hecho cuando" de S9 y al control A. Enlazar con la decisión "Umbral de acierto del examen" (22/01/2027) |
| 2 | Condición previa a L2: prueba de aislamiento con datos de dos clientes ficticios | Antes de L2; fecha [POR CONFIRMAR] | Juan y Álvaro deciden; Ingeniería ejecuta | Hecho cuando, en la lista maestra ("lista para L2") | Añadir a la lista maestra, en Producto, como requisito de "lista para L2". Sin efecto en S3 a S9 |
| 3 | Test automático que construye el contexto exacto enviado al modelo para el cliente A y falla si aparece cualquier identificador del cliente B | S3 (especificación, acción 3); construcción [POR CONFIRMAR] | IA y evaluación | Hecho cuando de S3, con una condición: que no desplace los tests de acceso cruzado | Ampliar "Hecho cuando" de S3: el acceso cruzado falla siempre, también en el contexto enviado al modelo |
| 4 | Reparto de casos adversos: Seguridad redacta, Ingeniería ejecuta, Álvaro revisa el realismo | Redacción desde S3 (lista de amenazas); ejecución y revisión [POR CONFIRMAR] | Seguridad, Ingeniería (IA y evaluación) y Álvaro | Hecho cuando de S4 (las 5 trampas) | Las 5 trampas de S4 pasan a ser primera versión de la parte adversa. Ampliarlas es "Si da tiempo" |

## 3. Impacto por semana y control

| Elemento | Efecto | Riesgo de retraso (hipótesis) |
|---|---|---|
| **S3** | Se suman la lista de amenazas de Seguridad, la especificación del test de contexto y su implementación. Semana corta por el festivo del 8 | Alto. Juan ya lleva autenticación, roles, señuelos y tests de acceso cruzado |
| **S4** | Las 5 trampas pasan a ser la primera versión de los casos adversos. Los socios deben haber confirmado el umbral | Medio. Depende de que la lista de S3 llegue a tiempo |
| **S9** | El examen de 50 casos incluye la parte adversa y se juzga con el umbral de la propuesta 1. Se repite ante cada cambio de modelo o instrucciones (acuerdo 5 del acta) | Medio. El detalle de S9 no consta en el extracto: [POR CONFIRMAR] |
| **Control A (18/12/2026)** | Se evalúa con el umbral propuesto. Las 5 trampas deben incluir al menos un caso de aislamiento y uno de acción prohibida (propuesta mía, para que el umbral sea comprobable ese día) | Medio. Necesita decisión de socios antes del 18/12 |

## 4. Qué recortar si S3 se aprieta

Propuesta, por orden de sacrificio. Primero lo marcado "Si da tiempo", después alcance:

1. Aplazar RLS en PostgreSQL (ya es "Si da tiempo"). El test de contexto es una defensa distinta y no depende de él.
2. Aplazar la ampliación de las 5 trampas (acción 2) a después del control A, hasta S9.
3. Mantener el test de contexto en versión mínima: un cliente señuelo y una comprobación de identificadores. Ampliarlo en S4–S5.

No recortaría el test de contexto completo ni los tests de acceso cruzado: son el "Hecho cuando" de S3.

## 5. Fechas que el acta no fija

| Acción del acta | Fecha en el acta | En este borrador |
|---|---|---|
| 2. Convertir amenazas en casos y ampliar las 5 trampas | [POR CONFIRMAR] | [POR CONFIRMAR]. Sugerencia: después de la lista de S3 y antes del control A |
| 4. Revisión de realismo de Álvaro | [POR CONFIRMAR] | [POR CONFIRMAR]. Sugerencia: coordinada con su tarea de S4 (probar con casos y 5 trampas) |
| 6. Diseño del registro de llamadas al modelo | S2 [POR CONFIRMAR] | S2 [POR CONFIRMAR]. Encaja con "ejecución de modelo" y auditoría de S2 |

Además, la fecha del acta y su ruta en el repositorio siguen en [POR CONFIRMAR].

## 6. Texto propuesto para el plan (no aplicado)

- **S3, Hecho cuando:** "Acceso cruzado falla siempre por diseño, también en el contexto enviado al modelo."
- **S4, Hecho cuando:** "Control A, con 5 trampas que incluyen aislamiento y acción prohibida."
- **S9, Hecho cuando:** "Examen de 50 casos con cero fallos en aislamiento y acciones prohibidas [si los socios aprueban]."
- **Lista maestra, Seguridad y legal:** "Prueba de aislamiento con dos clientes ficticios superada antes de L2 [si los socios aprueban]."

## 7. Riesgos y límites

- Con 50 casos solo se informa de qué casos pasan, sin porcentaje general (hecho del acta).
- Con datos inventados hasta L2, el examen no prueba fuga real. La propuesta 2 lo mitiga, no lo elimina.
- La defensa por capas (propuesta 5) queda fuera de este encargo. Su valor frente a la regla del adaptador es una hipótesis de Seguridad, no validada.
- Si los socios aprueban, `DECISIONS.md` y la web de `site/` deberán revisarse según `CLAUDE.md`. No lo he hecho.

Nada de esto es asesoría jurídica.

@CEO digital: mi pieza depende de que los socios confirmen el umbral antes del 18/12/2026. Sin esa decisión, el control A no tiene criterio de paso para aislamiento y acciones prohibidas.
@Seguridad: necesito la lista de amenazas en S3 para fijar la fecha de la acción 2.
@IA y evaluación: confirma si el test de contexto cabe en S3 con la semana del festivo del 8.
@Álvaro: tu revisión de realismo no tiene fecha en el acta. Propón una.

Usado del cerebro: docs/10-plan-
