# Oficina de agentes de Varios

Artefacto de Claude "Varios · Oficina de agentes". Archivos: `index.html`, `entregables.js`, `brain.json`, `office.js` y `oficina3d.js` (vista 3D) y `vendor/` (librerías; ver [LICENCIAS](vendor/LICENCIAS.md), D-015 y D-016).

Es una planta isométrica con siete departamentos y 34 agentes alrededor del cerebro. El séptimo departamento es **Sectores**: seis expertos (seguros, sanidad privada, asesorías y despachos, servicios financieros no bancarios, industria y logística). La priorización está en `knowledge/sectores/priorizacion.md`.

## Qué hace

- **Secciones (F1, [docs/25](../docs/25-portal-interno.md)):** barra siempre visible con Inicio, Encargos, Proyectos, Clientes, Cerebro, Calendario y Agentes; las acciones (Nuevo proyecto, Decisiones, Reunión) van aparte. La oficina se abre en **Inicio**: lo que espera tu OK y las preguntas de los agentes, rutinas pendientes, lo que está en curso, lo próximo y las decisiones con fecha. **Clientes** agrupa los proyectos por cliente. La planta 2D/3D es la sección Agentes.

- **Fichas completas de los 34 agentes** (`agentes.json`, generado desde `tools/org_data/agentes.py`): misión, nivel, responsabilidades, entregables, cómo trabaja, reglas del puesto y de la oficina, habilidades con sus pasos, criterio senior, errores que evita, cómo se mide, con quién trabaja y límites. Se ven en la pestaña Ficha de cada agente y entran en su contexto en cada encargo. Fichas legibles en `knowledge/agentes/` y habilidades en `claude/habilidades/`.
- **Caso de práctica Atalaya** (`casos/atalaya.json`): diagnóstico completo de la apertura de siniestros en una correduría ficticia, 13 encargos para 12 agentes en 4 fases. Se carga desde Proyectos y se lanza entero con «Lanzar todo el plan»: cada encargo empieza cuando terminan los que necesita, cada agente hace uno a la vez y trabajan hasta 4 en paralelo. Detalle en `precedents/projects/caso-correduria-atalaya/`.
- **Todo acaba en GitHub (D-017):** cada noche se vuelca lo nuevo (encargos, conversaciones, chats, memoria, reglas y habilidades enseñadas) a `oficina/registro/` y `precedents/oficina/`, y se publica el cerebro nuevo. GitHub Actions comprueba, regenera y avisa sin IA. Instrucciones en `registro/VOLCADO.md`.

- **Vista 3D (botón 3D/2D):**
  - la escena es `office.js` tal cual (Three.js r170), con un puesto fijo por agente; `oficina3d.js` pone los datos reales encima;
  - estados en HTML sobre cada persona: punto verde (trabajando), bocadillo naranja (espera tu OK), bocadillo morado (hablando), punto gris (libre); las píldoras de zona se apartan para no tapar a nadie;
  - cuando dos agentes hablan de verdad, el emisor se levanta, camina por los pasillos (rejilla de 0,5 m y A*), conversa con bocadillos alternos y vuelve con el documento; como mucho tres paseos a la vez, el resto espera en cola, y si el receptor está ocupado espera en el pasillo;
  - clic en cualquiera de los dos abre la conversación con sus mensajes reales; clic en una píldora abre la zona con las tarjetas de cada agente («Dar el OK», «Ver detalle») y la lista del departamento;
  - panel lateral con Hoy, Te esperan y Departamentos; «Simular conversación» ensaya un paseo sin datos reales;
  - con movimiento reducido, el agente aparece en destino y la ruta se ve punteada un segundo.

- **Proyectos (J) y nuevo proyecto (N):**
  - cada proyecto guarda su informe (objetivo, contexto, alcance, interlocutores, restricciones, criterio de éxito), sus documentos, sus encargos, sus entregables y su memoria;
  - la página de nuevo proyecto admite documentos subidos (PDF, Word, Excel, PowerPoint, texto, CSV) y una carpeta de Google Drive;
  - el CEO propone un plan con fases y encargos, que se lanzan con un clic.
- **Entregables reales con la misma plantilla:**
  - presentación `.pptx`, hoja de cálculo `.xlsx` con fórmulas de total, documento `.docx` y diagrama de proceso de carriles (`.svg`, `.png` y pasos en `.xlsx`);
  - el CEO elige el formato o lo eliges tú;
  - cada entregable tiene vista previa, versiones y «pedir un cambio» (crea una versión nueva y conserva la anterior).
- **Memoria (M):**
  - antes de cada encargo, el CEO y el agente consultan el histórico de encargos parecidos, lecciones, correcciones y decisiones;
  - al terminar, se guarda un precedente y, con Claude, una lección;
  - las aprobaciones, los rechazos y las correcciones de los socios también quedan en la memoria.
- **Experto de sector:** si el encargo es de un sector, su experto aporta primero las claves (vocabulario, normas con fuente, excepciones y lo que la IA no debe decidir), y el agente trabaja con ellas.

- **Grafo de conocimiento (D-018).** El cerebro es también un grafo: cada relación lleva su confianza (EXTRACTADA, INFERIDA o AMBIGUA). Cada agente recibe, además de las secciones que encajan, las decisiones, procesos y fuentes que esas secciones citan y las secciones relacionadas. La vista del cerebro enseña nodos centrales, comunidades, puentes, huecos y preguntas sugeridas, y traza el camino entre dos cosas. Informe: `knowledge/grafo/INFORME.md`.
- **Cerebro real.** `brain.json` contiene los Markdown de este repositorio troceados por secciones (sin `archive/`, `site/` ni `oficina/`), sus enlaces, las decisiones de `DECISIONS.md`, las pendientes y el catálogo P01–P38. Antes de cada encargo, chat o decisión, la oficina busca por texto las secciones que encajan y se las da al agente. Cada entrega guarda qué secciones leyó.
- **CEO con contrato de tarea** (`docs/03`, `docs/14`): objetivo, datos confirmados, inferidos y desconocidos, proceso, riesgo, una de las cinco decisiones y criterio de aceptación.
- **Calidad exigente (D-019):** rúbrica de seis criterios, hasta 4 rondas de corrección; solo lo que la pasa llega a un socio, y todo espera su OK. Rechazar exige motivo y relanza el encargo aprendiendo; lo que dependía de él se actualiza solo. Flujo completo: `docs/18-flujo-de-calidad-y-aprendizaje.md`.
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
- **Teclas:** I (inicio), L (clientes), A (agentes), 1–7, J (proyectos), N (nuevo proyecto), M (memoria), B, P, G, D, C (chat con el jefe), X, V (foco), Esc.

## Lo que no hace, a propósito

- **Solo un conector, de lectura:** Google Drive (`search_files` y `read_file_content`) para traer documentos a un proyecto. Pide permiso la primera vez y no escribe nada en Drive. Ninguna acción externa ocurre sin un socio (`CLAUDE.md`).
- **No escribe en GitHub por sí misma.** Lo hace el volcado nocturno (D-017). Las decisiones aceptadas en la oficina se pasan a `DECISIONS.md` por propuesta de cambios.
- **Las rutinas solo corren con la oficina abierta y Claude activo.** Si una tocaba en las últimas 24 horas, se ejecuta una vez al abrir, marcada con retraso.

## Mantenerla al día

Cuando cambien los documentos, regenera el cerebro y vuelve a publicar `brain.json` en el artefacto:

```
python3 tools/brain_build.py oficina/brain.json
```

Los datos de uso (encargos, reglas, fichas, habilidades, decisiones de la oficina, chats) se guardan con la capacidad `db` del artefacto. Sin ella, se guardan en el navegador.

Inspirada en la idea de Agents Office (github.com/ajsahni/agents-office), pero es código propio: aquel proyecto tiene una licencia no comercial que prohíbe renombrarlo o usarlo como producto de otra empresa, así que no se ha copiado nada de él.
