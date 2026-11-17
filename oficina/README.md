# Oficina de agentes de Varios

Artefacto de Claude "Varios · Oficina de agentes". Archivos: `index.html`, `entregables.js`, `brain.json` y `vendor/` (librerías para generar archivos; ver [LICENCIAS](vendor/LICENCIAS.md) y D-015).

Es una planta isométrica con siete departamentos y 29 agentes alrededor del cerebro. El séptimo departamento es **Sectores**: seis expertos (seguros, sanidad privada, asesorías y despachos, servicios financieros no bancarios, industria y logística). La priorización está en `knowledge/sectores/priorizacion.md`.

## Qué hace

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
- **Teclas:** 1–7, J (proyectos), N (nuevo proyecto), M (memoria), B, P, G, D, C (chat con el jefe), X, V (foco), Esc.

## Lo que no hace, a propósito

- **Solo un conector, de lectura:** Google Drive (`search_files` y `read_file_content`) para traer documentos a un proyecto. Pide permiso la primera vez y no escribe nada en Drive. Ninguna acción externa ocurre sin un socio (`CLAUDE.md`).
- **No escribe en GitHub.** Las entregas se descargan como nota `.md` con sus enlaces al cerebro, y las decisiones aceptadas se copian a `DECISIONS.md` a mano.
- **Las rutinas solo corren con la oficina abierta y Claude activo.** Si una tocaba en las últimas 24 horas, se ejecuta una vez al abrir, marcada con retraso.

## Mantenerla al día

Cuando cambien los documentos, regenera el cerebro y vuelve a publicar `brain.json` en el artefacto:

```
python3 tools/brain_build.py oficina/brain.json
```

Los datos de uso (encargos, reglas, fichas, habilidades, decisiones de la oficina, chats) se guardan con la capacidad `db` del artefacto. Sin ella, se guardan en el navegador.

Inspirada en la idea de Agents Office (github.com/ajsahni/agents-office), pero es código propio: aquel proyecto tiene una licencia no comercial que prohíbe renombrarlo o usarlo como producto de otra empresa, así que no se ha copiado nada de él.
