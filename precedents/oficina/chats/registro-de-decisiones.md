<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Conversaciones con Registro de decisiones

**Registro de decisiones** · 2026-11-17 21:21

**Pieza para CEO digital**

## Borrador de entradas para DECISIONS.md: protección de la IA y examen de 50 casos

**Estado:** borrador para revisión de los socios. No enviado ni publicado. Nada de esto es asesoría jurídica.

**Conclusión:** cinco propuestas del acta «Reunión: IA y evaluación y Seguridad», todas en estado «propuesta pendiente de socios». Ninguna está aprobada. Además, el umbral de acierto del examen cambia de fecha límite en la lista de pendientes. Ese cambio también queda pendiente de Juan y Álvaro.

**Convención:**
- **Hecho:** consta en el material facilitado. Se cita la ruta.
- **Hipótesis:** razonable, sin validar.
- **Propuesta:** lo que recomienda este borrador.
- **[POR CONFIRMAR]:** no consta en el material.

**Aviso sobre códigos:** el material solo muestra D-011 y D-012. Los códigos de abajo (D-013 a D-017) son provisionales y siguen esa numeración. Hay que comprobar en DECISIONS.md que no estén ya usados. **[POR CONFIRMAR]**

---

## 1. Entradas propuestas

### D-013 · Umbral de aprobación del examen

- **Fecha:** [POR CONFIRMAR]
- **Decisión (propuesta):** cero fallos en los casos de aislamiento entre clientes y de acciones prohibidas. En el resto de casos, cada fallo se analiza y se corrige antes del control.
- **Motivo:** con 50 casos no se puede prometer un porcentaje general de robustez. Un fallo en aislamiento o en acciones prohibidas es de gravedad distinta al resto. Es la posición de Seguridad. Ingeniería la dejó como [POR CONFIRMAR].
- **Impacto:** fija el criterio de paso del control A (18/12/2026) y del examen de 50 casos (S9). El examen informa de qué casos pasan y cuáles no, sin porcentaje global. Afecta a la decisión pendiente «Umbral de acierto del examen».
- **Estado:** propuesta pendiente de socios.

### D-014 · Condición previa a L2: prueba de aislamiento con dos clientes ficticios

- **Fecha:** [POR CONFIRMAR]
- **Decisión (propuesta):** no se pasa a L2 sin una prueba de aislamiento equivalente con datos de dos clientes ficticios.
- **Motivo:** hasta L2 solo hay datos inventados, y con ellos el examen no prueba la fuga de datos reales. Ingeniería lo dejaba como riesgo abierto. Seguridad pide convertirlo en condición.
- **Impacto:** añade una condición de entrada a L2 (datos de clientes). Se enlaza con la decisión pendiente «Proveedor de identidad para producción», también fijada «antes de L2» (ver sección 2). La lista maestra ya incluye «lista para L2» entre los entregables de producto a 12/02/2027.
- **Estado:** propuesta pendiente de socios.

### D-015 · Test automático del contexto enviado al modelo

- **Fecha:** [POR CONFIRMAR]
- **Decisión (propuesta):** en S3, un test automático construye el contexto exacto que recibe el modelo para el cliente A y falla si aparece cualquier identificador del cliente B.
- **Motivo:** un fallo de aislamiento en el contexto del modelo no se vería en PostgreSQL. Los tests de acceso cruzado de S3 cubren la base de datos, no lo que se envía al modelo.
- **Impacto:** amplía el criterio de S3 («el acceso cruzado falla siempre por diseño») al contexto del modelo. Especificación para Claude Code a cargo de IA y evaluación en S3. Coste de tiempo en S3: [POR CONFIRMAR].
- **Estado:** propuesta pendiente de socios.

### D-016 · Reparto de los casos adversos

- **Fecha:** [POR CONFIRMAR]
- **Decisión (propuesta):** Seguridad redacta los casos adversos, Ingeniería los ejecuta y Álvaro revisa su realismo desde el lado de la correduría.
- **Motivo:** separa quien escribe el ataque de quien lo ejecuta y de quien valida que sea creíble en el sector. Ingeniería pidió a Seguridad la lista y un validador.
- **Impacto:** carga de revisión para Álvaro. El acta deja en [POR CONFIRMAR] la fecha de esa revisión y la de ampliar las 5 trampas del control A.
- **Estado:** propuesta pendiente de socios.

### D-017 · Defensa por capas como principio de diseño

- **Fecha:** [POR CONFIRMAR]
- **Decisión (propuesta):** el adaptador de modelos impone la separación entre dato e instrucción, pero la protección principal es limitar lo que el modelo puede hacer y ver.
- **Motivo:** Seguridad sostiene que una regla impuesta por el adaptador no basta, porque la inyección puede colarse. **Hipótesis de Seguridad, a validar. No es un hecho.** Es coherente con las reglas del CEO («la confianza del modelo no es un permiso») y con la puerta de herramientas de S6.
- **Impacto:** orienta el diseño del CEO, el adaptador y la puerta de herramientas. Los acuerdos 1 a 3 del acta (texto externo como dato, modelo que propone, salida validada contra esquema) se aplican en este marco. Es un principio de diseño. Si se aprueba, conviene revisar si exige otra decisión estructural. **[POR CONFIRMAR]**
- **Estado:** propuesta pendiente de socios.

---

## 2. Lista de decisiones pendientes (actualizada)

Cambios respecto a la tabla de DECISIONS.md. El resto de filas no cambia.

| Decisión | Quién | Antes de | Nota |
|---|---|---|---|
| Umbral de acierto del examen | Los dos | **22/01/2027 (vigente en DECISIONS.md).** El acta pide confirmarlo antes del control A (18/12/2026) | **Cambio de fecha pendiente de decisión de Juan y Álvaro.** No se modifica la fecha hasta que decidan. Contenido en D-013 |
| Proveedor de identidad para producción | Juan | Antes de L2 | Vinculada a D-014: la prueba de aislamiento con dos clientes ficticios es condición previa a L2 |
| D-013 a D-017 (propuestas del acta) | Los dos | [POR CONFIRMAR] | Pendientes de aprobación. El acta fija el paso 5 «antes del control A (18/12/2026)» con [POR CONFIRMAR] |

**Hecho:** la fecha del 22/01/2027 consta en [DECISIONS.md › Decisiones pendientes]. La del 18/12/2026 consta en el acta como paso 5 con [POR CONFIRMAR].

**Observación (hipótesis):** si el umbral se confirma el 22/01/2027, el control A (18/12/2026) se pasaría sin umbral decidido y el examen de 50 casos (S9) quedaría después. Adelantar la fecha evitaría medir las 5 trampas sin criterio acordado. Lo deciden los socios.

**Vínculo L2 e identidad:** ambas decisiones son «antes de L2». Se propone revisarlas juntas al abrir L2. Hecho: la lista de pendientes ya fija el proveedor de identidad antes de L2. Propuesta: que D-014 sea condición explícita en esa revisión.

---

## 3. Qué falta

- Fechas de las cinco entradas y de la reunión: [POR CONFIRMAR].
- Códigos definitivos: comprobar el último código usado en DECISIONS.md.
- Fecha de revisión de Álvaro y de ampliación de las 5 trampas: [POR CONFIRMAR].
- Tras aceptar cualquier entrada, regenerar el cerebro con `python3 tools/brain_build.py oficina/brain.json`, según CLAUDE.md.

---

@CEO digital: mi pieza depende de que los socios confirmen D-013 a D-017 y la nueva fecha del umbral. Hasta entonces, nada figura como decidido.
@Seguridad: la hipótesis sobre el valor de la regla del adaptador (D-017) queda marcada como no probada. Si tienes una forma de validarla antes del control A, indícala para anotarla en el motivo.

Usado del cerebro: [DECISIONS.md › Decisiones pendientes (con fecha límite)]; [docs/10-plan-12-semanas.md › Semana a semana]; [docs/10-plan-12-semanas.md › Lista maestra a 12/02/2027]; [CLAUDE.md › Reglas]; encargo «Reunión: IA y evaluación y Seguridad».
Necesita aprobación: Juan y Álvaro deben decidir si aprueban D-013 a D-017 y si el umbral del examen se adelanta del 22/01/2027 a antes del 18/12/2026. Un socio debe confirmar los códigos y las fechas antes de pasarlo a DECISIONS.md.
