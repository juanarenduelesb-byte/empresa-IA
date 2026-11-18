<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Conversaciones con Bibliotecario

**Bibliotecario** · 2026-11-17 21:22

**Pieza para CEO digital**

## Revisión del acta «Protección de la IA y examen de 50 casos»: contradicciones, huecos y fichas

**Estado:** borrador. No aprobado. Pendiente de revisión de un socio. Nada de esto es asesoría jurídica.

**Convención:** Hecho = consta en las secciones facilitadas (se cita la ruta). Hipótesis = razonable, sin validar. Propuesta = lo que recomienda este borrador. [POR CONFIRMAR] = no consta en el material.

**Sobre las fuentes:** solo he visto los extractos facilitados para este encargo, no los archivos completos. Si un dato no aparece en los extractos, no lo doy por inexistente en el repositorio. Lo marco como [POR CONFIRMAR].

---

## 1. Resumen

**Conclusión:** el acta tiene cuatro problemas que conviene resolver antes de que los socios la aprueben. Dos son de calendario y responsabilidad (umbral y condición previa a L2) y dos son de diseño (el test de contexto no está en el criterio de S3 y la defensa de aislamiento depende de capas opcionales).

- La fecha límite del umbral del examen no coincide: el acta apunta al control A (18/12/2026) y DECISIONS.md al 22/01/2027.
- El umbral y la condición previa a L2 no tienen responsable claro en las decisiones pendientes.
- El test del contexto enviado al modelo no figura en «Hecho cuando» de S3, y no hay fecha de control que lo exija.
- La defensa de aislamiento del acta descansa en capas que el plan deja como opcionales («Si da tiempo»: RLS en PostgreSQL).
- Propongo dos fichas de conocimiento en borrador: defensa por capas y caso adverso.

---

## 2. Tabla de hallazgos

| # | Hallazgo | Fuentes | Gravedad | Acción propuesta |
|---|---|---|---|---|
| 1 | **Fecha del umbral contradictoria.** El acta (siguiente paso 5) lo sitúa «antes del control A (18/12/2026) [POR CONFIRMAR]». DECISIONS.md fija «Umbral de acierto del examen» antes del 22/01/2027. Hay 35 días de diferencia. El control A usa 20 casos y 5 trampas, y el examen de 50 casos es S9. | Acta (siguientes pasos, nº 5); `DECISIONS.md › Decisiones pendientes`; `docs/10-plan-12-semanas.md › Semana a semana` (S4, S9) | Alta | Los socios deciden si hay un umbral para el control A y otro para el examen de S9, o uno solo. Propuesta: mantener el 22/01/2027 para el umbral del examen de 50 casos y añadir una decisión aparte, con fecha antes del 18/12/2026, para los criterios de las 5 trampas. No cambiar ninguna fecha sin registrarlo en DECISIONS.md. |
| 2 | **Hay un solapamiento de significado.** El acta mezcla el umbral del examen de 50 casos con el del control A. El plan solo describe el control A como hito de S4 («Probar con los casos; 5 peticiones trampa») y no define criterio de aprobación. | Acta (tema, decisión 1); `docs/10-plan-12-semanas.md › Semana a semana` (S4) | Media | Definir por separado qué significa «aprobar» el control A. [POR CONFIRMAR]: si el plan completo lo define en otro apartado. |
| 3 | **Sin responsable claro en pendientes.** DECISIONS.md lista «Umbral de acierto del examen» con «Los dos» como responsable, pero la condición previa a L2 (prueba de aislamiento con dos clientes ficticios) no aparece como decisión pendiente. Solo hay «Proveedor de identidad para producción: Juan, antes de L2». En el acta, el siguiente paso 5 asigna a «Juan y Álvaro» ambas cosas, sin fecha firme. | Acta (siguientes pasos, nº 5); `DECISIONS.md › Decisiones pendientes` | Alta | Añadir a DECISIONS.md, como propuesta, una fila «Condición previa a L2: prueba de aislamiento con dos clientes ficticios». Responsable, fecha y criterio: [POR CONFIRMAR]. Sugerencia: un responsable técnico nombrado (Juan, por ser producto y construcción) y revisión de Álvaro. Es una hipótesis de reparto, no un hecho. |
| 4 | **Responsable difuso en el umbral.** «Los dos» no indica quién prepara la propuesta ni quién la ejecuta. En el acta, Seguridad y IA y evaluación aparecen como departamentos, no como personas. | `DECISIONS.md › Decisiones pendientes`; acta (desacuerdos, siguientes pasos) | Media | Anotar quién redacta el borrador de umbral (propuesta: Seguridad, como ya hace en el acta) y quién lo decide (los socios). |
| 5 | **El test de contexto de S3 no está en «Hecho cuando».** El acta propone un test que construya el contexto exacto enviado al modelo para el cliente A y falle si aparece un identificador del cliente B. En el plan, S3 dice «Acceso cruzado falla siempre por diseño» y lista «tests de acceso cruzado», pero no menciona el contexto enviado al modelo. Además, el adaptador de modelos no llega hasta S4, así que en S3 aún no existe el punto donde se construye ese contexto. | Acta (decisión 3, siguiente paso 3); `docs/10-plan-12-semanas.md › Semana a semana` (S3, S4) | Alta | Dos opciones, a decidir por los socios. (a) Mover el test a S4, junto al adaptador, y añadirlo al criterio de Control A. (b) Mantenerlo en S3 con un constructor de contexto mínimo y simulado, y añadirlo a «Hecho cuando» de S3. Propuesta: (b) para el diseño y (a) para la comprobación con el adaptador real. Cualquier cambio del plan se registra en DECISIONS.md. |
| 6 | **La defensa de aislamiento depende de capas opcionales.** El acta sostiene que la protección real es que el modelo no pueda ver datos de otro cliente. En el plan, RLS en PostgreSQL figura en «Si da tiempo» de S3. Lo que sí es obligatorio: cliente deducido de la identidad, dos clientes señuelo y tests de acceso cruzado. Además, la puerta de herramientas es S6, tres semanas después de S3, y el acta no dice qué protege entre medias. | Acta (desacuerdo 1, decisión 5); `docs/10-plan-12-semanas.md › Semana a semana` (S3, S6); `CLAUDE.md › Reglas` (cliente desde la identidad) | Alta | Declarar qué capas son obligatorias y cuáles refuerzo. Propuesta: obligatorias = cliente desde la identidad, filtrado en código, tests de acceso cruzado y test de contexto. RLS queda como refuerzo, y el acta no debe presentarlo como parte de la defensa mientras siga en «Si da tiempo». |
| 7 | **«Hasta L2 solo datos inventados» y «prueba antes de L2» pueden chocar.** Hasta L2 todo es inventado, y la prueba con dos clientes ficticios es compatible. Pero el acta no dice quién cierra la puerta L1→L2 ni con qué evidencia. La lista maestra solo dice «L0 cerrada · lista para L2». | Acta (hechos, decisión 2); `docs/10-plan-12-semanas.md › Lista maestra a 12/02/2027`; contexto de Varios (puertas L0-L4) | Media | Añadir a la lista maestra, como propuesta, «prueba de aislamiento con dos clientes ficticios superada» como requisito de «lista para L2». Los socios lo aprueban. |
| 8 | **El registro de llamadas al modelo carece de fecha firme.** El acta lo asigna a S2 [POR CONFIRMAR]. El modelo de datos de S2 incluye «ejecución de modelo» y «auditoría», lo que encaja. Pero el adaptador llega en S4. | Acta (acuerdo 4, siguiente paso 6); `docs/10-plan-12-semanas.md › Semana a semana` (S2, S4) | Baja | Confirmar que «ejecución de modelo» cubre versión de instrucciones, modelo y resultado. Si no, ampliar el modelo de datos en S2. [POR CONFIRMAR]. |
| 9 | **Casos adversos sin fecha ni reparto firme.** Siguientes pasos 2 y 4 llevan [POR CONFIRMAR]. El plan cubre «5 peticiones trampa» en S4 (Álvaro) y el examen de 50 casos en S9, pero no asigna quién redacta los adversos. El acta propone que Álvaro revise el realismo, mientras que la lista del plan ya le carga con casos y conversaciones. | Acta (desacuerdo 4, siguientes pasos 2 y 4); `docs/10-plan-12-semanas.md › Semana a semana` (S4, S9) | Media | Fijar fecha para la ampliación de trampas, antes del 18/12/2026 para las 5 y antes de S9 para el resto. Valorar la carga de Álvaro. |
| 10 | **Amenazas en S3 y control A en S4.** La lista de amenazas se entrega «en S3» y las trampas se prueban en S4, con poco margen para convertirlas en casos. | Acta (siguientes pasos 1 y 2); `docs/10-plan-12-semanas.md › Semana a semana` (S3, S4) | Media | Pedir la lista a mitad de S3 si se quiere que las trampas del control A la reflejen. Si no, aceptar que las 5 trampas son una primera versión. |
| 11 | **Secretos en regist
