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

**Identidad (provisional hasta el proveedor de S3).** Cabecera `Authorization: Bearer <token>`. El token es un JWT HS256 con `sub` (usuario), `cliente`, `exp`, `iss` y `aud`, firmado con `VARIOS_JWT_SECRETO`. El usuario tiene que existir y estar activo en ese cliente; sus roles se leen de la base. Para probar en local: `python -c "from varios.api.identidad import emitir; print(emitir('<usuario>', '<cliente>'))"` con los identificadores de la semilla.

**Errores.** 401 sin token válido · 404 si no existe o es de otro cliente (no se revela cuál) · 403 si la aprobación no cumple la regla · 409 si la transición no está permitida · 422 si los datos no son válidos. Cada petición es una transacción: si algo falla, no se guarda nada, tampoco el evento.

## Lo que falta (plan)

- Proveedor de identidad real (S3, antes de L2); hoy los tokens se firman con un secreto compartido (D-028).
- Pasar el motor en memoria (`varios.procesos`) a estas tablas (S5).
- Comprobar `docker compose up` en un equipo de los socios: en el entorno de Claude, la imagen no puede descargar paquetes.
