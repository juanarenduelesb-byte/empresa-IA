# Trabajo nocturno de Claude

Lista de la noche: las tareas que Juan ha elegido para esta noche, que Claude hace solo, en tandas, mientras los socios no están. El plan general, el ritual diario y el formato del informe de la mañana están en [22-plan-hasta-febrero.md](22-plan-hasta-febrero.md). Las tareas que no se terminan pasan a la noche siguiente si Juan lo decide.

**Noche del 26/11/2026:** sesión principal desde las 02:00 y tandas a las 03:30, 05:00 y 06:00. La de las 06:00 escribe el informe a las 07:15.

Cada tanda:

1. Lee este archivo, `CLAUDE.md` y `DECISIONS.md`.
2. Coge la **primera tarea sin marcar** de la lista (en orden). Al empezarla, cámbiala a `[~] (en curso, tanda N, hora)` y sube ese cambio enseguida: así dos tandas no hacen lo mismo. Una tarea `[~]` de hace menos de 3 horas está ocupada; sáltala. Termina cada tarea entera antes de pasar a la siguiente: mejor una bien hecha que tres a medias.
3. Antes de subir: `bash tools/comprobar.sh` (regenera el cerebro y pasa las mismas comprobaciones que CI). Si falla, no se sube.
4. Marca la tarea `[x]`, añade una línea al **Registro** (fecha, tanda, qué se hizo, qué queda) y sube a `main` (los socios lo pidieron así el 26/11/2026).
5. Si una tarea necesita una decisión de un socio, la deja en **Preguntas para los socios** y pasa a la siguiente.

Si al subir hay conflicto en archivos generados (`oficina/brain.json`, `knowledge/grafo/`), no los edites a mano: quédate con los tuyos, ejecuta `python3 tools/brain_build.py oficina/brain.json` y continúa el rebase. El robot de GitHub (`regenerar.yml`) los regenera tras cada subida.

Reglas que no cambian: **no reinventar la rueda** (antes de construir, mira cómo lo resuelve alguien que lo hace bien, con fuente, y adáptalo; ver [23-plan-maestro.md](23-plan-maestro.md)); **si detectas algo anterior mal, arréglalo** en la misma tarea y dilo en el registro; nada de datos reales, cifras ni fuentes inventadas; todo lo legal es borrador para abogado; toda decisión estructural va a `DECISIONS.md` como «propuesta».

## Lista de esta noche (hazlas en este orden)

- [x] B1 · Conocimiento en la base de datos: fuentes y fichas con estado (draft, validated, deprecated), búsqueda de texto con permisos por cliente y cita obligatoria; carga de `knowledge/` y del registro de fuentes. *Hecho cuando:* una búsqueda desde el cliente A nunca devuelve nada del B y todo resultado trae su fuente.
- [x] B2 · Paquete de dominio de seguros y corredurías: normas con fuente oficial verificada (LCS, distribución de seguros, libros-registro, baremo, convenios entre aseguradoras, Consorcio, atención al cliente, datos de salud), glosario de siniestros y catálogo de excepciones. *Pista ya encontrada:* la Ley 10/2025 de servicios de atención a la clientela (BOE-A-2025-26698, https://www.boe.es/eli/es/l/2025/12/26/10/con) fija con carácter general 15 días hábiles para resolver reclamaciones. Las empresas tienen hasta el 28/12/2026 para adaptarse, y los servicios financieros se rigen por su norma sectorial con esta como supletoria. Hay que comprobar en el texto cómo aplica a corredurías.
- [x] F1 · Portal interno: auditoría de la oficina actual (`oficina/`) frente a referencias de gestión de trabajo con éxito, con fuente. Propuesta de distribución (inicio con lo que espera tu OK, encargos, proyectos, clientes, cerebro, calendario, agentes y la vista 3D como una vista más) y mejoras aplicadas sin romper lo que funciona. Si no puedes publicar el artefacto, deja los archivos listos y dilo en el informe.
- [x] C1 · 20 siniestros inventados con su resultado esperado (esquema, casos y pruebas que validan los casos).
- [x] D1 · Legal (borradores para abogado): contrato marco de servicios, encargo de tratamiento (art. 28 RGPD), acuerdo de confidencialidad, anexo de uso de IA (Reglamento de IA) y matriz de aprobaciones.
- [x] F2 · Web para clientes: estudio de 5–8 webs de referencia (consultoras boutique de IA y procesos) con fuente; estructura, textos y maqueta navegable con datos y casos marcados como inventados. Sin publicar y sin cerrar la marca (M-002).
- [x] B3 · Entender al cliente: ficha de cliente (esquema JSON + plantilla), cuestionario de descubrimiento por fases (G0–G2) y guion de la conversación semanal de validación.
- [ ] C2 · 25 encargos para el Control A (20 normales + 5 trampas) con la decisión esperada y un banco de pruebas con modelo simulado.
- [ ] D2 · Finanzas: comparativa de forma jurídica con fuentes, requisitos de facturación (incluido Verifactu, con fechas verificadas), modelo de precio de diagnóstico, piloto y operación como hoja con parámetros (sin cifras inventadas) y previsión de caja por escenarios.
- [ ] E1 · Plantillas de entregables con la misma estructura: propuesta de diagnóstico, informe de diagnóstico, diseño TO-BE, plan de piloto, informe mensual de operación y acta de reunión.
- [ ] C3 · Rúbrica de calidad de entregables y lista de comprobación por tipo de entregable.

### Ya hechas por la sesión principal
- [x] A1 · Entorno: FastAPI con `/health`, configuración por `.env`, Docker Compose con PostgreSQL 16, Ruff y pytest en CI. *Hecho cuando:* `docker compose up` arranca y `/health` responde con la base de datos conectada.
- [x] A2 · Modelo de datos de S2 con Alembic: cliente, usuario, solicitud, plan, tarea, documento, aprobación, evento de auditoría, ejecución de modelo, uso de herramienta. Auditoría que no se puede modificar ni borrar. *Hecho cuando:* las migraciones suben y bajan desde cero en PostgreSQL y las pruebas están en verde.
- [x] A3 · Aislamiento por cliente: repositorios que siempre filtran por el cliente de la identidad, dos clientes señuelo y pruebas de acceso cruzado (y RLS en PostgreSQL). *Hecho cuando:* leer o escribir datos de otro cliente falla siempre.
- [x] A4 · Datos de ejemplo automáticos: script que carga dos clientes inventados con usuarios, solicitudes y documentos.
- [x] Plan maestro: [23-plan-maestro.md](23-plan-maestro.md)

## Preguntas para los socios
Están detalladas en [23-plan-maestro.md](23-plan-maestro.md), sección 6. Las tres primeras:
1. **M-001.** ¿Habéis revisado con un laboralista la compatibilidad con vuestros empleos actuales?
2. **M-002.** ¿Una sola marca? Claude recomienda Esclusa.
3. **M-003.** Acuerdo de socios, pendiente desde el 22/11.

4. **Abogado (B2).** ¿Con qué base del art. 9.2 del RGPD puede una correduría tratar los datos de salud de un parte con daños personales? El art. 99 de la Ley 20/2015 solo habilita a las aseguradoras. Hasta saberlo, el proceso de referencia no guarda datos de salud (D-024).
5. **Oportunidad (B2).** Las corredurías tienen hasta el 28/12/2026 para adaptar su atención al cliente a la Ley 10/2025 (un mes para resolver reclamaciones y persona a petición del cliente, también en bots). ¿Lo usamos en las conversaciones de validación o como argumento comercial?

6. **Abogado (D1).** Las seis preguntas de `governance/legal/borradores/README.md`: cláusulas tipo de la Comisión tal cual o contrato propio, tope de responsabilidad y seguro de RC, datos de salud, propiedad de lo construido, DORA si el cliente es una aseguradora y jurisdicción.

## Registro
| Fecha | Tanda | Hecho | Queda |
|---|---|---|---|
| 26/11 02:30 | Sesión principal | A1–A4: API con /health, Docker Compose, modelo de S2 con Alembic, RLS forzada, auditoría inmutable, tablas de conocimiento con búsqueda y citas, datos de ejemplo, 14 pruebas nuevas contra PostgreSQL real, CI con PostgreSQL y Ruff (D-023, docs/24-base-de-datos.md) | `docker compose up` sin probar aquí (la imagen no puede descargar paquetes en este entorno); falta cargar en la base las fichas de knowledge/ (B1) |
| 26/11 02:40 | Sesión principal | B1: `varios.db.carga_conocimiento` carga knowledge/ en la base (633 fichas, 28 % con fuente externa, todas en borrador); búsqueda con cita interna y externa; 2 pruebas más | Validar fichas (socios) y subir el % con fuente externa (B2) |
| 26/11 02:50 | Sesión principal | Plan maestro (docs/23) y plan diario (docs/22, D-022); B2 empezada y devuelta a la lista: leer el BOE pedía una aprobación que nadie podía dar a esta hora | B2 y siguientes, para las tandas de las 03:30, 05:00, 06:00 y 07:45 |
| 26/11 03:55 | Tanda 03:30 | B2: paquete `knowledge/sectores/seguros/` (normas con artículo, glosario de 35 términos, 15 excepciones, `dominio.json` con 10 plazos) y 21 fuentes nuevas leídas en el BOE, UNESPA, CCS y AEPD; prueba `test_dominio_seguros.py`; D-024. Arreglado lo anterior: la LCS se cita por el consolidado del BOE, RDL-3-2020 apuntaba a una resolución de 2024, RD 287/2021 citaba artículos equivocados, CIDE/ASCIDE están refundidos desde 2026 y el plazo de dos meses de reclamaciones está derogado (ahora un mes). La Ley 10/2025 da 12 meses (hasta el 28/12/2026), no 6 como dice su preámbulo | Leer en el BOE el consolidado del RDL 3/2020, la Ley 35/2015 y la Ley 5/2025; vigencia del SDM; base de datos de salud (abogado); validar excepciones con tramitadores |
| 26/11 04:05 | Tanda 03:30 | F1: auditoría de la oficina con 9 hallazgos frente a Linear, Basecamp, GitHub, Apple HIG, NN/g y Zapier (6 fuentes nuevas), distribución en siete secciones (docs/25, D-025) y aplicado: Inicio como entrada (te esperan, rutinas, en curso, próximo, decisiones con fecha), vista Clientes, barra visible encima de las vistas (antes las tapaba), avisos solo si hay algo, teclas I/L/A. Prueba de humo en Chromium sin errores, también a 390 px. **Artefacto sin publicar:** los archivos de `oficina/` están listos; publicarlo es de un socio | Editar antes de aprobar, posponer y caducidad; paleta Cmd+K; oficina sobre la API (M-041); ficha de cliente (B3) |
| 26/11 04:06 | Tanda 03:30 | C1: 20 siniestros inventados (`processes/referencia-seguros-apertura-siniestros/casos/`) con mensaje, hechos, resultado esperado y motivo; cartera de 11 pólizas ficticias; esquema JSON generado desde Pydantic; reglas fijas en `src/varios/seguros/apertura.py` que leen plazos y listas de `dominio.json` (D-024); 27 pruebas: cada excepción EX-01–EX-15 tiene caso, salen las cuatro acciones y el plazo se lee del dominio | Validar los casos con tramitadores; medir la extracción de la IA contra `hechos` (S6–S9); umbrales de prescripción y bloqueo son hipótesis |
| 26/11 04:15 | Tanda 03:30 | D1: cinco borradores para abogado en `governance/legal/borradores/`: contrato marco con pedido por fase y anexo DORA opcional, encargo del tratamiento sobre las cláusulas tipo de la Comisión (2021/915) con los anexos rellenos para el proceso de referencia y la comprobación del art. 28.3, confidencialidad mutua (Ley 1/2019), anexo de IA (papeles, riesgo, art. 50 y lo que la IA nunca decide) y matriz de aprobaciones por acción y por puerta. 7 fuentes nuevas leídas en EUR-Lex y el BOE. Arreglado lo anterior: el ómnibus ya se cita por EUR-Lex y el art. 4 ya no obliga a garantizar un nivel de alfabetización, solo a apoyarla. DORA no se aplica a corredurías pyme, pero sí a aseguradoras medianas bajo Solvencia II | Revisión del abogado (6 preguntas); precios, topes y plazos entre corchetes los deciden los socios |
| 26/11 04:27 | Tanda 03:30 | F2: estudio de 7 webs de referencia con su prueba de éxito (Fractional AI, Distyl, Tribe, Faculty, Datatonic, Keepler, Paradigma) y 10 lecciones; estructura, textos y requisitos LSSI-CE y cookies en `docs/26-web-clientes.md`; maqueta navegable en `web/maqueta/` (10 páginas, sin cookies, caso Atalaya marcado como inventado y sin cifras inventadas: la línea base y el umbral van como huecos). Probada a 1280 y 390 px sin errores | Marca (M-002), forma jurídica para el aviso legal (M-003), aprobación de textos por los socios y revisión legal |
| 26/11 04:30 | Tanda 03:30 | B3: ficha de cliente como modelo Pydantic (`src/varios/clientes/ficha.py`) con esquema JSON generado, plantilla legible y ejemplo inventado (Atalaya); sin campos para datos personales (roles, no nombres) y cada cifra con su base (medido, declarado o hipótesis); cuestionario por puertas G0–G2 con el campo de la ficha que alimenta cada pregunta; guion semanal de 30 minutos con el antes, el durante y el después, y qué archivo cambiar según lo aprendido. Base: The Mom Test, MEDDPICC y VSM (2 fuentes nuevas); 5 pruebas | Probar el guion en la primera conversación real (M-010) y ajustar las preguntas |
