# Trabajo nocturno de Claude

Lista de trabajo que Claude hace solo, en tandas, mientras los socios no están. Cada tanda:

1. Lee este archivo, `CLAUDE.md` y `DECISIONS.md`.
2. Coge la **primera tarea sin marcar** de la lista (en orden). Al empezarla, cámbiala a `[~] (en curso, tanda N, hora)` y sube ese cambio enseguida: así dos tandas no hacen lo mismo. Una tarea `[~]` de hace menos de 3 horas está ocupada; sáltala. Termina cada tarea entera antes de pasar a la siguiente: mejor una bien hecha que tres a medias.
3. Antes de subir: `python -m pytest -q`, `python tools/check_repo.py`, generados al día (`python3 tools/org_gen.py --check`, `python3 tools/agentes_gen.py --check`) y `python3 tools/brain_build.py oficina/brain.json` si cambió algún documento.
4. Marca la tarea `[x]`, añade una línea al **Registro** (fecha, tanda, qué se hizo, qué queda) y sube a `main` (los socios lo pidieron así el 26/11/2026).
5. Si una tarea necesita una decisión de un socio, la deja en **Preguntas para los socios** y pasa a la siguiente.

Reglas que no cambian: nada de datos reales, cifras ni fuentes inventadas; todo lo legal es borrador para abogado; toda decisión estructural va a `DECISIONS.md` como «propuesta».

## Lista (por orden)

### A · Base de datos real (adelanta S1–S2 del plan)
- [~] (en curso, sesión principal, 02:10) A1 · Entorno: FastAPI con `/health`, configuración por `.env`, Docker Compose con PostgreSQL 16, Ruff y pytest en CI. *Hecho cuando:* `docker compose up` arranca y `/health` responde con la base de datos conectada.
- [~] (en curso, sesión principal, 02:10) A2 · Modelo de datos de S2 con Alembic: cliente, usuario, solicitud, plan, tarea, documento, aprobación, evento de auditoría, ejecución de modelo, uso de herramienta. Auditoría que no se puede modificar ni borrar. *Hecho cuando:* las migraciones suben y bajan desde cero en PostgreSQL y las pruebas están en verde.
- [~] (en curso, sesión principal, 02:10) A3 · Aislamiento por cliente: repositorios que siempre filtran por el cliente de la identidad, dos clientes señuelo y pruebas de acceso cruzado (y RLS en PostgreSQL). *Hecho cuando:* leer o escribir datos de otro cliente falla siempre.
- [ ] A4 · Datos de ejemplo automáticos: script que carga dos clientes inventados con usuarios, solicitudes y documentos.

### B · Cerebro y conocimiento
- [ ] B1 · Conocimiento en la base de datos: fuentes y fichas con estado (draft, validated, deprecated), búsqueda de texto con permisos por cliente y cita obligatoria; carga de `knowledge/` y del registro de fuentes. *Hecho cuando:* una búsqueda desde el cliente A nunca devuelve nada del B y todo resultado trae su fuente.
- [ ] B2 · Paquete de dominio de seguros y corredurías: normas con fuente oficial verificada (LCS, distribución de seguros, libros-registro, baremo, convenios entre aseguradoras, Consorcio, atención al cliente, datos de salud), glosario de siniestros y catálogo de excepciones.
- [ ] B3 · Entender al cliente: ficha de cliente (esquema JSON + plantilla), cuestionario de descubrimiento por fases (G0–G2) y guion de la conversación semanal de validación.

### C · Calidad
- [ ] C1 · 20 siniestros inventados con su resultado esperado (esquema, casos y pruebas que validan los casos).
- [ ] C2 · 25 encargos para el Control A (20 normales + 5 trampas) con la decisión esperada y un banco de pruebas con modelo simulado.
- [ ] C3 · Rúbrica de calidad de entregables y lista de comprobación por tipo de entregable.

### D · Departamentos internos
- [ ] D1 · Legal (borradores para abogado): contrato marco de servicios, encargo de tratamiento (art. 28 RGPD), acuerdo de confidencialidad, anexo de uso de IA (Reglamento de IA) y matriz de aprobaciones.
- [ ] D2 · Finanzas: comparativa de forma jurídica con fuentes, requisitos de facturación (incluido Verifactu, con fechas verificadas), modelo de precio de diagnóstico, piloto y operación como hoja con parámetros (sin cifras inventadas) y previsión de caja por escenarios.

### E · Plantillas
- [ ] E1 · Plantillas de entregables con la misma estructura: propuesta de diagnóstico, informe de diagnóstico, diseño TO-BE, plan de piloto, informe mensual de operación y acta de reunión.

## Preguntas para los socios
(vacío)

## Registro
| Fecha | Tanda | Hecho | Queda |
|---|---|---|---|
