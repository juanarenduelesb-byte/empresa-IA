# Portal interno: auditoría de la oficina y distribución propuesta (F1)

**Estado:** propuesta (D-025) · **Fecha:** 26/11/2026 · **Alcance:** `oficina/` (artefacto «Varios · Oficina de agentes»). No toca el producto del piloto.

## 1. Qué hay hoy (auditoría)
Lo que funciona y no se toca: la planta en 2D y 3D con los 34 agentes y su estado, el encargo rápido en el panel lateral, proyectos con documentos y entregables, el cerebro con el grafo, el calendario con rutinas, las decisiones, la memoria, el flujo de calidad (D-019) y el volcado nocturno a GitHub (D-017).

| # | Hallazgo | Por qué importa | Referencia |
|---|---|---|---|
| 1 | La pantalla de entrada es la planta de agentes. Lo que espera a un socio está en un panel lateral pequeño y, en 2D, solo como filtro del listado. | Lo primero que tiene que ver un socio es lo que necesita su OK, no a los agentes. | Inicio orientado a la acción de Basecamp ([BASECAMP-5](../knowledge/fuentes/registro.md#basecamp-5)); «revisión pedida» como filtro por defecto en GitHub ([GITHUB-NOTIF-INBOX](../knowledge/fuentes/registro.md#github-notif-inbox)) |
| 2 | Las vistas a pantalla completa tapaban la barra superior. Para pasar del Tablero al Calendario había que cerrar con Esc y volver a abrir. | La navegación oculta hace las tareas al menos un 39 % más lentas. | [NNG-HIDDEN-NAV](../knowledge/fuentes/registro.md#nng-hidden-nav) |
| 3 | Once botones del mismo peso mezclaban destinos (Proyectos, Cerebro) con acciones (Nuevo proyecto, Reunión). | Las pestañas son para navegar, no para acciones; de 3 a 7 destinos. | [APPLE-HIG-TAB-BARS](../knowledge/fuentes/registro.md#apple-hig-tab-bars) |
| 4 | «Tu OK» y «Decisiones» enseñaban un 0 permanente. | Los avisos numéricos se reservan para información crítica; un 0 fijo enseña a ignorarlos. | [APPLE-HIG-TAB-BARS](../knowledge/fuentes/registro.md#apple-hig-tab-bars) |
| 5 | No había vista de clientes: el cliente solo era un campo del proyecto. | El 15/02/2027 llegan clientes reales; hace falta verlos con su trabajo. | Plan maestro, M-014 |
| 6 | «Tu OK» contaba solo aprobaciones, no las preguntas de los agentes, que también bloquean. | Una pregunta sin responder para el trabajo igual que una aprobación. | Triage de Linear ([LINEAR-TRIAGE](../knowledge/fuentes/registro.md#linear-triage)) |
| 7 | La cola de aprobación no permite editar antes de aprobar, posponer ni poner caducidad con una acción segura por defecto. | Es el patrón de aprobación humana de Zapier y Power Automate. | [ZAPIER-HITL](../knowledge/fuentes/registro.md#zapier-hitl) |
| 8 | No hay paleta de órdenes (Cmd/Ctrl+K) para ir a cualquier sitio. | Acelerador opcional común en Linear y Basecamp. | [LINEAR-TRIAGE](../knowledge/fuentes/registro.md#linear-triage), [BASECAMP-5](../knowledge/fuentes/registro.md#basecamp-5) |
| 9 | Los datos de uso viven en el almacén del artefacto o en el navegador, no en la API ni en PostgreSQL. | Sin identidad, auditoría central ni copias. | Plan maestro, M-041 |

## 2. Distribución propuesta
Barra de secciones siempre visible, con texto y siete destinos, en este orden:

1. **Inicio**: lo que necesita a un socio, primero. Contiene:
   - «Te esperan»: aprobaciones y preguntas, de la más antigua a la más nueva, con «Dar el OK» o «Revisar» en la misma fila;
   - rutinas que tocaba ejecutar;
   - lo que está en curso y lo que se ha hecho hoy;
   - lo próximo del calendario;
   - las decisiones pendientes ordenadas por fecha límite.

   El aviso numérico aparece solo si hay algo.
2. **Encargos**: el tablero por estados (antes «Tablero»).
3. **Proyectos**.
4. **Clientes**: cada cliente con sus proyectos, encargos, entregables y lo que espera. Se agrupa por el campo Cliente del proyecto. La ficha completa llega con B3.
5. **Cerebro**.
6. **Calendario**.
7. **Agentes**: la planta en 2D o 3D, como una vista más.

Separadas de la navegación quedan las acciones (Nuevo proyecto, Decisiones, Reunión, foco y tema). Decisiones queda junto a las acciones porque se usa poco y lleva aviso. Tampoco cambian las teclas que ya había. Las nuevas son I (inicio), L (clientes) y A (agentes).

## 3. Aplicado esta noche
- Inicio como vista de entrada, con la casilla «Abrir la oficina aquí» para quien prefiera entrar por la planta.
- Vista Clientes.
- Barra de secciones con estado activo (`aria-current`) y visible encima de las vistas: se puede pasar de una sección a otra sin cerrar.
- Avisos numéricos solo cuando hay algo. El de Inicio cuenta también las preguntas.
- Encargos sustituye a Tablero.

Prueba de humo con Chromium: cada sección abre, la barra marca la sección activa, Esc vuelve a Agentes, las teclas I, B y L funcionan, el caso Atalaya aparece en Clientes, no hay desbordamiento horizontal a 390 px y no hay errores de JavaScript.

No se ha publicado el artefacto. Los archivos de `oficina/` quedan listos, y publicarlos es de un socio: la oficina publicada tiene datos en su almacén y conviene que la pruebe quien la usa.

## 4. Siguiente (por orden)
1. ~~Cola de aprobación con «editar antes de aprobar», «posponer» y caducidad que nunca continúa lo externo, legal o financiero (hallazgo 7).~~ **Hecho en N4 (26/11/2026):** «Editar y aprobar» guarda la original y la corrección en la memoria; «Posponer» oculta el encargo de Inicio hasta el día siguiente a las 9:00 sin parar la caducidad (vale para aprobaciones y preguntas, también las caducadas; se pierde cuando el encargo cambia de estado; arreglado el 27/11: en las preguntas no funcionaba); una aprobación sin decidir caduca a las 72 horas (plazo propuesto, lo ajustan los socios) y la acción por defecto es siempre la segura para todo, no solo para lo externo, legal o financiero: no continúa y vuelve a Inicio como pregunta, porque D-019 pide el OK de un socio para todo. Prueba de humo en Chromium sin errores.
3. ~~La oficina sobre la API~~ Primera parte hecha en N3a y N3b ([docs/24](24-base-de-datos.md)).
2. Paleta Cmd/Ctrl+K para ir a cualquier sección, proyecto, agente o documento del cerebro (hallazgo 8).
4. Ficha de cliente (B3) dentro de Clientes.
