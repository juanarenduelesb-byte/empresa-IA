# Trabajo nocturno de Claude

Lista de la noche: las tareas que Juan ha elegido para esta noche, que Claude hace solo, en tandas, mientras los socios no están. El plan general, el ritual diario y el formato del informe de la mañana están en [22-plan-hasta-febrero.md](22-plan-hasta-febrero.md). Las tareas que no se terminan pasan a la noche siguiente si Juan lo decide.

**Noche del 26/11/2026:** sesión principal desde las 02:00 y tandas a las 03:30, 05:00 y 06:00. La de las 06:00 escribe el informe a las 07:15.

Cada tanda:

1. Lee este archivo, `CLAUDE.md` y `DECISIONS.md`.
2. Coge la **primera tarea sin marcar** de la lista (en orden). Al empezarla, cámbiala a `[~] (en curso, tanda N, hora)` y sube ese cambio enseguida: así dos tandas no hacen lo mismo. Una tarea `[~]` de hace menos de 3 horas está ocupada; sáltala. Termina cada tarea entera antes de pasar a la siguiente: mejor una bien hecha que tres a medias.
3. Antes de subir: `bash tools/comprobar.sh` (regenera el cerebro y pasa las mismas comprobaciones que CI). Si falla, no se sube.
4. Marca la tarea `[x]`, añade una línea al **Registro** (fecha, tanda, qué se hizo, qué queda) y sube a `main` (los socios lo pidieron así el 26/11/2026).
5. Si una tarea necesita una decisión de un socio, la deja en **Preguntas para los socios** y pasa a la siguiente.

Reglas que no cambian: **no reinventar la rueda** (antes de construir, mira cómo lo resuelve alguien que lo hace bien, con fuente, y adáptalo; ver [23-plan-maestro.md](23-plan-maestro.md)); **si detectas algo anterior mal, arréglalo** en la misma tarea y dilo en el registro; nada de datos reales, cifras ni fuentes inventadas; todo lo legal es borrador para abogado; toda decisión estructural va a `DECISIONS.md` como «propuesta».

## Lista de esta noche (hazlas en este orden)

- [ ] B1 · Conocimiento en la base de datos: fuentes y fichas con estado (draft, validated, deprecated), búsqueda de texto con permisos por cliente y cita obligatoria; carga de `knowledge/` y del registro de fuentes. *Hecho cuando:* una búsqueda desde el cliente A nunca devuelve nada del B y todo resultado trae su fuente.
- [ ] B2 · Paquete de dominio de seguros y corredurías: normas con fuente oficial verificada (LCS, distribución de seguros, libros-registro, baremo, convenios entre aseguradoras, Consorcio, atención al cliente, datos de salud), glosario de siniestros y catálogo de excepciones.
- [ ] F1 · Portal interno: auditoría de la oficina actual (`oficina/`) frente a referencias de gestión de trabajo con éxito, con fuente. Propuesta de distribución (inicio con lo que espera tu OK, encargos, proyectos, clientes, cerebro, calendario, agentes y la vista 3D como una vista más) y mejoras aplicadas sin romper lo que funciona. Si no puedes publicar el artefacto, deja los archivos listos y dilo en el informe.
- [ ] C1 · 20 siniestros inventados con su resultado esperado (esquema, casos y pruebas que validan los casos).
- [ ] D1 · Legal (borradores para abogado): contrato marco de servicios, encargo de tratamiento (art. 28 RGPD), acuerdo de confidencialidad, anexo de uso de IA (Reglamento de IA) y matriz de aprobaciones.
- [ ] F2 · Web para clientes: estudio de 5–8 webs de referencia (consultoras boutique de IA y procesos) con fuente; estructura, textos y maqueta navegable con datos y casos marcados como inventados. Sin publicar y sin cerrar la marca (M-002).
- [ ] B3 · Entender al cliente: ficha de cliente (esquema JSON + plantilla), cuestionario de descubrimiento por fases (G0–G2) y guion de la conversación semanal de validación.
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
(vacío)

## Registro
| Fecha | Tanda | Hecho | Queda |
|---|---|---|---|
| 26/11 02:30 | Sesión principal | A1–A4: API con /health, Docker Compose, modelo de S2 con Alembic, RLS forzada, auditoría inmutable, tablas de conocimiento con búsqueda y citas, datos de ejemplo, 14 pruebas nuevas contra PostgreSQL real, CI con PostgreSQL y Ruff (D-023, docs/24-base-de-datos.md) | `docker compose up` sin probar aquí (la imagen no puede descargar paquetes en este entorno); falta cargar en la base las fichas de knowledge/ (B1) |
