# Oficina de agentes de Varios

Artefacto de Claude "Varios · Oficina de agentes": `index.html` más `brain.json`. Planta isométrica con seis departamentos y 23 agentes alrededor del cerebro.

## Qué hace

- **Cerebro real.** `brain.json` contiene los Markdown de este repositorio troceados por secciones (sin `archive/`, `site/` ni `oficina/`), sus enlaces, las decisiones de `DECISIONS.md`, las pendientes y el catálogo P01–P38. Antes de cada encargo, chat o decisión, la oficina busca por texto las secciones que encajan y se las da al agente. Cada entrega guarda qué secciones leyó.
- **CEO con contrato de tarea** (`docs/03`, `docs/14`): objetivo, datos confirmados, inferidos y desconocidos, proceso, riesgo, una de las cinco decisiones y criterio de aceptación.
- **Calidad** revisa cada entrega contra el criterio. Si no cumple, la devuelve una vez al agente. Lo que no es de riesgo bajo, o no pasa Calidad, espera la aprobación de un socio.
- **Flujo visible** de cada encargo, en los once pasos de `docs/03`.
- **Decisiones (D):** registro del repositorio, pendientes con días restantes, propuestas redactadas por el agente Registro de decisiones, y aceptar, descartar o copiar en formato `DECISIONS.md`.
- **Enseñar a los agentes:**
  - editar su ficha (nombre, qué hace, cómo trabaja, habilidades);
  - reglas fijas que salen de las revisiones (el CEO decide si una corrección es puntual o regla) y que se pueden editar o borrar;
  - habilidades propias por agente o departamento;
  - entrevista de cinco preguntas del jefe de departamento (escribe "prepara" en su chat).
- **Rutinas:**
  - se crean escribiendo "cada lunes a las 9, …", con el botón Repetir o desde un día del calendario;
  - se pueden pausar, reanudar, borrar, ejecutar ya o marcar con "necesita mi OK";
  - también hay encargos programados para un día y hora.
- **Equipos:** el jefe reparte en piezas, cada compañero trabaja a la vez, pueden dejarse notas (`@Nombre: …`) y el jefe une el resultado.
- **Reunión (X):** dos agentes hablan de un tema y uno redacta el acta.
- **Teclas:** 1–6, B, P, G, D, C (chat con el jefe), X, V (foco), Esc.

## Lo que no hace, a propósito

- **No usa conectores ni navegador.** Solo tiene Claude, y ninguna acción externa ocurre sin un socio (`CLAUDE.md`).
- **No escribe en GitHub.** Las entregas se descargan como nota `.md` con sus enlaces al cerebro, y las decisiones aceptadas se copian a `DECISIONS.md` a mano.
- **Las rutinas solo corren con la oficina abierta y Claude activo.** Si una tocaba en las últimas 24 horas, se ejecuta una vez al abrir, marcada con retraso.

## Mantenerla al día

Cuando cambien los documentos, regenera el cerebro y vuelve a publicar `brain.json` en el artefacto:

```
python3 tools/brain_build.py oficina/brain.json
```

Los datos de uso (encargos, reglas, fichas, habilidades, decisiones de la oficina, chats) se guardan con la capacidad `db` del artefacto. Sin ella, se guardan en el navegador.

Inspirada en la idea de Agents Office (github.com/ajsahni/agents-office), pero es código propio: aquel proyecto tiene una licencia no comercial que prohíbe renombrarlo o usarlo como producto de otra empresa, así que no se ha copiado nada de él.
