# Base de datos (D-023, propuesta)

PostgreSQL 16 es la fuente operativa (D-004). Código en `src/varios/db/`, migraciones en `migrations/` (Alembic) y pruebas en `tests/db/`, que se ejecutan contra un PostgreSQL real.

## Qué guarda

| Tabla | Para qué | Proceso |
|---|---|---|
| `cliente` | El tenant. Varios también es un cliente para su trabajo interno | P14 |
| `usuario` | Personas y agentes de cada cliente, con sus roles | P14, P30 |
| `solicitud` | El encargo, con su estado (`encargo.json`) y su riesgo | P01, P02 |
| `plan`, `tarea` | Plan del encargo y sus tareas, con reintentos y clave de idempotencia | P05, P06, P08, P22 |
| `documento` | Documentos recibidos, identificados por su huella y en cuarentena hasta revisarlos | P07, P20 |
| `aprobacion` | Aprobaciones humanas. La base de datos impide aprobar lo que pide uno mismo | P10 |
| `evento_auditoria` | Todo cambio y toda acción. Nadie puede modificarlo ni borrarlo, tampoco el propietario | P15, P17 |
| `ejecucion_modelo` | Cada llamada a un modelo de IA, con coste, tokens y resultado | P16, P29 |
| `uso_herramienta` | Cada intento de usar una herramienta, esté autorizado o no | P21 |
| `fuente`, `ficha_conocimiento`, `ficha_fuente` | El cerebro: conocimiento con estado y fuentes, común o de un cliente | P04, P13 |

## Cómo se separan los clientes

Hay dos defensas independientes:

1. **En la aplicación.** El repositorio (`varios.db.repositorio`) toma el cliente de la identidad autenticada y filtra siempre por él. Si llega un `cliente_id` en los datos de la petición, se ignora.
2. **En PostgreSQL (RLS forzada en todas las tablas).** Cada transacción fija su cliente con `set_config('varios.cliente_id', …, true)` (`varios.db.sesion.sesion_de_cliente`). Una fila de otro cliente no se ve ni se puede escribir, aunque la consulta no filtre. Una conexión sin cliente fijado no ve nada.

La aplicación entra con el usuario `varios_app`, sin privilegios. Las migraciones y el conocimiento común (normas, sectores) los carga el propietario. El conocimiento común lo leen todos los clientes, pero no lo puede escribir ninguno.

## Cómo se busca en el cerebro

`Repositorio.buscar_conocimiento()` hace una búsqueda de texto en español y respeta los permisos. Las fichas sin al menos una fuente no salen, y las obsoletas tampoco. Cada resultado trae sus fuentes y la cita exacta. Más adelante, si hace falta búsqueda por significado, se añadiría pgvector (está en la lista de herramientas a estudiar del plan).

## Cómo arrancarla

- **Con Docker:** `cp .env.example .env`, cambiar las contraseñas y ejecutar `docker compose up --build`. Después, http://localhost:8000/health.
- **Sin Docker:** `python3 tools/pg_local.py` arranca un PostgreSQL desechable si está instalado. Luego, con `VARIOS_DATABASE_URL_ADMIN` apuntando a él, `alembic upgrade head`.
- **Datos de ejemplo** (todos inventados): `python -m varios.db.semilla`.
- **Pruebas:** `python -m pytest -q`. Usan `VARIOS_TEST_DATABASE_URL` o un PostgreSQL desechable. CI levanta PostgreSQL como servicio.

## Carga del cerebro

`python -m varios.db.carga_conocimiento` (con `VARIOS_DATABASE_URL_ADMIN`) carga:
- el registro de fuentes;
- cada sección de `knowledge/` como ficha, con su documento como fuente interna y las fuentes externas que cita.

Es idempotente. Lo que desaparece del repositorio queda como obsoleto, no se borra.

**Foto del 26/11/2026:** 633 fichas, todas en borrador. Solo 178 (28 %) citan una fuente externa. Ninguna está validada todavía por un socio o un profesional. Es la medida de cuánto le falta al cerebro para ser fiable, y el informe de la mañana la seguirá.

**Foto del 26/11/2026 por la noche (K1):** 757 fichas; 220 (29,1 %) citan una fuente externa. **Cambio de medida:** hasta ahora contaban como externas las fuentes internas del registro (Guía, Atlas, DECISIONS.md); con el cómputo antiguo saldría un 32,8 %. El paquete de seguros: 37 de 39 fichas (94,9 %); las otras dos solo citan fuentes internas y lo dicen. Se mide sin base de datos con `varios.db.carga_conocimiento.medir()`.

## API de la oficina (N3a, D-028)

Rutas en `src/varios/api/oficina.py`; pruebas en `tests/db/test_api_oficina.py`, contra PostgreSQL real.

| Ruta | Qué hace | Regla |
|---|---|---|
| `POST /encargos` · `GET /encargos` · `GET /encargos/{id}` | Alta y lectura de encargos | El cliente y el autor salen del token; si el cuerpo trae `cliente_id` o `autor_id`, se ignoran |
| `POST /encargos/{id}/estado` | Cambio de estado según `encargo.json`, con motivo y clave de idempotencia opcional | A PENDIENTE_APROBACION y a ENTREGADO solo se llega por las rutas de aprobación (D-019) |
| `POST /encargos/{id}/tareas` · `GET …/tareas` | Tareas del encargo | Solo en PLANIFICADO, EN_EJECUCION o RETRABAJO; la misma clave devuelve la misma tarea |
| `POST /encargos/{id}/aprobaciones` · `GET …/aprobaciones` | Pedir aprobación de la versión actual (EN_QA → PENDIENTE_APROBACION) | Queda quién la pide |
| `POST /aprobaciones/{id}/decision` | Aprobar (→ ENTREGADO) o rechazar (→ RETRABAJO, versión + 1) | Solo una persona con rol `aprobador`, que no la ha pedido ni es autora del encargo, y sobre la misma versión |
| `GET /encargos/{id}/auditoria` | Eventos del encargo, sus tareas y sus aprobaciones | Cada cambio deja uno; la tabla no se puede modificar |

**Identidad (provisional hasta el proveedor de S3).** Cabecera `Authorization: Bearer <token>`. El token es un JWT HS256 con `sub` (usuario), `cliente`, `exp`, `iss` y `aud`, firmado con `VARIOS_JWT_SECRETO` (al menos 32 caracteres; si se deja el valor de `.env.example`, la API no emite ni acepta tokens). El usuario tiene que existir y estar activo en ese cliente; sus roles se leen de la base. Para probar en local: `python -c "from varios.api.identidad import emitir; print(emitir('<usuario>', '<cliente>'))"` con los identificadores de la semilla.

**Errores.** 401 sin token válido · 404 si no existe o es de otro cliente (no se revela cuál) · 403 si la aprobación no cumple la regla · 409 si la transición no está permitida · 422 si los datos no son válidos. Cada petición es una transacción: si algo falla, no se guarda nada, tampoco el evento.

## La oficina sobre la API (N3b)

La oficina (`oficina/`) es la misma en los dos casos; `oficina/api.js` decide dónde guarda.

| Cómo se abre | Dónde guarda los encargos |
|---|---|
| Como artefacto de Claude o como archivos sueltos | Como hasta ahora: el almacén del artefacto o el del navegador. `api.js` no hace nada |
| Desde la API: `docker compose up` y http://localhost:8000/oficina/ | Además de su almacén, cada encargo se escribe en PostgreSQL por la API |

**Cómo se conecta.** La API sirve la oficina en `/oficina/` (misma dirección, sin CORS). Si `/health` responde, aparece el botón «Conectar API»: se pega un token (o se abre `/oficina/#token=…`) y el botón pasa a «API · PostgreSQL». El token se guarda en `sessionStorage` y se borra al cerrar la pestaña. Para sacar uno con los datos de ejemplo: `docker compose exec api python -c "from varios.db.semilla import _id; from varios.api.identidad import emitir; print(emitir(_id('usuario','atalaya','tramitador@atalaya.invalid'), _id('cliente','atalaya')))"`.

**Qué se escribe.** Alta del encargo; cada cambio de estado de la oficina se traduce al estado de la API y se recorre el camino más corto de `encargo.json` (la API publica las transiciones en `GET /definiciones/encargo`, así que la oficina no copia la tabla); al pedir el OK se pide la aprobación, y la decisión solo se envía si la tomó un socio en la oficina («Aprobado por un socio» o «Rechazado por un socio»). Si la API la rechaza (por ejemplo, porque quien aprueba es quien pidió el encargo), la oficina avisa y en la API sigue pendiente: no se fuerza nada.

**Qué se lee.** Al conectar, la oficina actualiza el estado de los encargos que ya conoce y muestra los que se crearon fuera (otra persona u otro equipo) como «Llega de la API», en solo lectura.

**Lo que aún no hace.** Las piezas de un encargo en equipo no se suben como tareas; la aprobación de un encargo que llegó de la API no se puede dar desde otra oficina; reglas, memoria, proyectos y entregables siguen solo en el almacén de la oficina. Es el paso siguiente de M-041 (y N4 para editar, posponer y caducar aprobaciones).

**Prueba de humo (26/11/2026, Chromium sin interfaz).** Con PostgreSQL desechable, migraciones, semilla y la API: un encargo creado en la oficina queda en la tabla `solicitud` en PENDIENTE_APROBACION con 7 eventos de auditoría (alta, cinco cambios de estado y la petición de aprobación); en modo demostración la oficina lo da por hecho sin un socio y la API no lo acepta como aprobado. Los dos encargos de la semilla aparecen en Inicio como preguntas. La misma oficina servida como archivos sin API guarda como siempre y no muestra el botón. Sin errores en la consola en ninguno de los dos casos. `docker compose up` sigue sin poder probarse aquí (ver «Pendiente de tu aprobación» en docs/21).

## Lo que falta (plan)

- Proveedor de identidad real (S3, antes de L2); hoy los tokens se firman con un secreto compartido (D-028).
- Pasar el motor en memoria (`varios.procesos`) a estas tablas (S5).
- Comprobar `docker compose up` en un equipo de los socios: en el entorno de Claude, la imagen no puede descargar paquetes.
