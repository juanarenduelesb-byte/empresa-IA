# Base de datos (D-023, propuesta)

PostgreSQL 16 es la fuente operativa (D-004). Código en `src/varios/db/`, migraciones en `migrations/` (Alembic) y pruebas en `tests/db/`, que se ejecutan contra un PostgreSQL real.

## Qué guarda

| Tabla | Para qué | Proceso |
|---|---|---|
| `cliente` | El tenant. Varios también es un cliente para su trabajo interno | P14 |
| `usuario` | Personas y agentes de cada cliente, con sus roles | P14, P30 |
| `solicitud` | El encargo, con su estado (`encargo.json`), su riesgo y hasta cuándo está pospuesto | P01, P02 |
| `plan`, `tarea` | Plan del encargo y sus tareas, con reintentos y clave de idempotencia | P05, P06, P08, P22 |
| `documento` | Documentos recibidos, identificados por su huella y en cuarentena hasta revisarlos | P07, P20 |
| `poliza` | Cartera del cliente que usa el proceso de referencia (número, ramo, aseguradora y vigencia). Inventada hasta L2 (A5, D-032) | Proceso de referencia |
| `aprobacion` | Aprobaciones humanas, con su hora de caducidad. La base de datos impide aprobar lo que pide uno mismo, y una caducada no tiene aprobador | P10 |
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
- **Datos de ejemplo** (todos inventados): `python -m varios.db.semilla` carga; `python -m varios.db.semilla --vaciar` quita los de A5. Con Docker: `docker compose exec api python -m varios.db.semilla`.

## Datos de ejemplo (A5)

La semilla carga, además de los dos clientes inventados (Correduría Atalaya y el señuelo de aislamiento) con sus usuarios:

| Qué | De dónde | Cómo se reparte | Atalaya | Señuelo |
|---|---|---|---|---|
| 11 pólizas (tabla `poliza`) | `processes/referencia-seguros-apertura-siniestros/casos/cartera.json` | Por ramo: hogar y comercio a Atalaya; automóvil, RC y accidentes al señuelo | 6 | 5 |
| 20 siniestros (encargos «Siniestro S01…») | `…/casos/casos.json` (el mensaje va en la descripción) | Con el cliente de su póliza; sin póliza, a Atalaya | 16 | 4 |
| 25 encargos del Control A («Control A N01…») | `processes/ceo-control-a/encargos.json` | Alternos en el orden del archivo | 13 | 12 |

Todos entran en RECIBIDO. **Riesgo:** el de los encargos del Control A sale de las reglas fijas del CEO (`varios.ceo.decision.REGLAS`) aplicadas a las señales etiquetadas de cada caso; el de los siniestros es alto si hay daños personales, una persona vulnerable o fallecida, dinero o un juzgado o atestado, y medio en el resto (abrirlo acaba en un envío a la aseguradora con el OK de un socio). Es una propuesta: lo ajusta quien valide los casos.

Los identificadores son fijos, así que cargar dos veces no duplica y `--vaciar` quita solo estas filas: lo que haya creado una persona no se toca. Sus tareas y aprobaciones se van con ellas; la auditoría se queda, porque no se puede borrar. Las pruebas (`tests/db/test_semilla.py`) comprueban que cada caso de los archivos está una vez y en un solo cliente, que cada siniestro está con su póliza y que, por la API, cada cliente ve solo lo suyo.

**Prueba de humo (27/11/2026, A5).** PostgreSQL desechable, migraciones, semilla y la API; la oficina en Chromium con el token de cada cliente: en «Encargos» la de Atalaya muestra sus 29 ejemplos (16 siniestros y 13 encargos del Control A, además de sus dos solicitudes de siempre) y la del señuelo sus 16 (4 y 12, además de la suya), y ninguna muestra uno del otro. Sin errores en la consola. **Arreglado:** la imagen de Docker solo copiaba `processes/definitions`, así que `docker compose exec api python -m varios.db.semilla` no habría encontrado el registro de fuentes (`tools/org_data`) ni los casos; ahora los copia y la semilla los busca también en la carpeta de trabajo.
- **Pruebas:** `python -m pytest -q`. Usan `VARIOS_TEST_DATABASE_URL` o un PostgreSQL desechable. CI levanta PostgreSQL como servicio.

## Carga del cerebro

`python -m varios.db.carga_conocimiento` (con `VARIOS_DATABASE_URL_ADMIN`) carga:
- el registro de fuentes;
- cada sección de `knowledge/` como ficha, con su documento como fuente interna y las fuentes externas que cita.

Es idempotente. Lo que desaparece del repositorio queda como obsoleto, no se borra.

**Foto del 26/11/2026:** 633 fichas, todas en borrador. Solo 178 (28 %) citan una fuente externa. Ninguna está validada todavía por un socio o un profesional. Es la medida de cuánto le falta al cerebro para ser fiable, y el informe de la mañana la seguirá.

**Foto del 26/11/2026 por la noche (K1):** 757 fichas; 220 (29,1 %) citan una fuente externa. **Cambio de medida:** hasta ahora contaban como externas las fuentes internas del registro (Guía, Atlas, DECISIONS.md); con el cómputo antiguo saldría un 32,8 %. El paquete de seguros: 37 de 39 fichas (94,9 %); las otras dos solo citan fuentes internas y lo dicen. Se mide sin base de datos con `varios.db.carga_conocimiento.medir()`.

## API de la oficina (N3a y N3c, D-028 y D-031)

Rutas en `src/varios/api/oficina.py`; pruebas en `tests/db/test_api_oficina.py` y `tests/db/test_api_n3c.py`, contra PostgreSQL real.

| Ruta | Qué hace | Regla |
|---|---|---|
| `POST /encargos` · `GET /encargos` · `GET /encargos/{id}` | Alta y lectura de encargos. La lista trae también la última aprobación de cada uno (con `caduca_en`) y sus tareas: la oficina se puede rehacer solo con ella | El cliente y el autor salen del token; si el cuerpo trae `cliente_id` o `autor_id`, se ignoran |
| `POST /encargos/{id}/estado` | Cambio de estado según `encargo.json`, con motivo y clave de idempotencia opcional | A PENDIENTE_APROBACION y a ENTREGADO solo se llega por las rutas de aprobación (D-019), y de PENDIENTE_APROBACION solo se sale decidiendo la aprobación, también para devolver a retrabajo o rechazar (Guía v1.4 §4; arreglado el 27/11) |
| `POST /encargos/{id}/tareas` · `GET …/tareas` | Tareas del encargo | Solo en PLANIFICADO, EN_EJECUCION o RETRABAJO; la misma clave devuelve la misma tarea |
| `POST /encargos/{id}/aprobaciones` · `GET …/aprobaciones` | Pedir aprobación de la versión actual (EN_QA → PENDIENTE_APROBACION) | Queda quién la pide |
| `POST /aprobaciones/{id}/decision` | Aprobar (→ ENTREGADO) o rechazar: devolver para rehacer (→ RETRABAJO, versión + 1, por defecto) o rechazar del todo con `"si_rechaza": "RECHAZADO"` (→ RECHAZADO) | Solo una persona con rol `aprobador`, que no la ha pedido ni es autora del encargo, y sobre la misma versión |
| `POST /encargos/{id}/posponer` | Apartar hasta una hora (`hasta`, con zona horaria) un encargo que espera a una persona (N3c) | Solo una persona; solo en PENDIENTE_APROBACION, PENDIENTE_INFO, ESCALADO o BLOQUEADO; como mucho 7 días; no decide nada, no para la caducidad y se pierde al cambiar de estado |
| `POST /tareas/{id}/estado` | Cambio de estado de una tarea según `objetos.json` (N3c) | Solo mientras el encargo trabaja (PLANIFICADO, EN_EJECUCION o RETRABAJO). De `needs_approval` a `succeeded`, solo una persona con rol `aprobador` que no la puso a esperar ni es autora del encargo |
| `GET /definiciones/tarea` | Transiciones de la tarea, para que la oficina no copie la tabla | — |
| `GET /encargos/{id}/auditoria` | Eventos del encargo, sus tareas y sus aprobaciones | Cada cambio deja uno; la tabla no se puede modificar |

**Caducidad (N3c, D-031).** Cada aprobación se pide con `caduca_en` (72 h por defecto, `VARIOS_APROBACION_CADUCA_H`; lo fijan los socios). Al empezar cada petición de un cliente, en una transacción aparte y con su RLS, se caducan sus aprobaciones vencidas: la decisión pasa a `caducada` sin aprobador y el encargo de PENDIENTE_APROBACION a ESCALADO, con dos eventos firmados por `sistema:caducidad` (`aprobacion_caducada` y `mover`). Vuelve como pregunta y nunca se aprueba sola (P10). Es la expiración pasiva de Redis (`REDIS-EXPIRE`): no hace falta un proceso programado. Decidir una aprobación vencida responde 403. PENDIENTE_APROBACION → ESCALADO es una transición añadida a `encargo.json` (1.1.0) que solo hace la caducidad: como cambio libre responde 409. Desde ESCALADO una persona decide cómo seguir (por ejemplo, volver a PLANIFICADO y pedir el OK otra vez).

**Identidad (provisional hasta el proveedor de S3).** Cabecera `Authorization: Bearer <token>`. El token es un JWT HS256 con `sub` (usuario), `cliente`, `exp`, `iss` y `aud`, firmado con `VARIOS_JWT_SECRETO` (al menos 32 caracteres; si se deja el valor de `.env.example`, la API no emite ni acepta tokens). El usuario tiene que existir y estar activo en ese cliente; sus roles se leen de la base. Para probar en local: `python -c "from varios.api.identidad import emitir; print(emitir('<usuario>', '<cliente>'))"` con los identificadores de la semilla.

**Errores.** 401 sin token válido · 404 si no existe o es de otro cliente (no se revela cuál) · 403 si la aprobación no cumple la regla · 409 si la transición no está permitida · 422 si los datos no son válidos. Cada petición es una transacción: si algo falla, no se guarda nada, tampoco el evento.

## La oficina sobre la API (N3b)

La oficina (`oficina/`) es la misma en los dos casos; `oficina/api.js` decide dónde guarda.

| Cómo se abre | Dónde guarda los encargos |
|---|---|
| Como artefacto de Claude o como archivos sueltos | Como hasta ahora: el almacén del artefacto o el del navegador. `api.js` no hace nada |
| Desde la API: `docker compose up` y http://localhost:8000/oficina/ | Además de su almacén, cada encargo se escribe en PostgreSQL por la API |

**Cómo se conecta.** La API sirve la oficina en `/oficina/` (misma dirección, sin CORS). Si `/health` responde, aparece el botón «Conectar API»: se pega un token (o se abre `/oficina/#token=…`) y el botón pasa a «API · PostgreSQL». El token se guarda en `sessionStorage` y se borra al cerrar la pestaña. Para sacar uno con los datos de ejemplo: `docker compose exec api python -c "from varios.db.semilla import _id; from varios.api.identidad import emitir; print(emitir(_id('usuario','atalaya','tramitador@atalaya.invalid'), _id('cliente','atalaya')))"`.

**Qué se escribe.** Alta del encargo; cada cambio de estado de la oficina se traduce al estado de la API y se recorre el camino más corto de `encargo.json` (la API publica las transiciones en `GET /definiciones/encargo`, así que la oficina no copia la tabla); al pedir el OK se pide la aprobación, y la decisión solo se envía si la tomó un socio en la oficina («Aprobado por un socio», «Rechazado por un socio» o «Descartado por un socio»). Descartar algo que espera el OK es una decisión «rechazada» que lo lleva directo a RECHAZADO; rechazar sin descartar lo devuelve a RETRABAJO y desde ahí sigue el camino libre (antes del 27/11 también el descarte pasaba por RETRABAJO, EN_EJECUCION y ESCALADO, que dejaba en la auditoría tres pasos que nadie dio). Si la API la rechaza (por ejemplo, porque quien aprueba es quien pidió el encargo), la oficina avisa y en la API sigue pendiente: no se fuerza nada.

**Qué se lee.** Al conectar, la oficina actualiza el estado de los encargos que ya conoce y muestra los que se crearon fuera (otra persona u otro equipo) como «Llega de la API», en solo lectura.

**Posponer, caducar y tareas (N3c, 27/11/2026).** Con la API conectada:
- *Posponer* en la oficina llama a `POST /encargos/{id}/posponer`; al leer, la oficina toma `pospuesto_hasta` de la API, así que una recarga u otra oficina lo ven igual.
- *Caducar* lo decide la API. La oficina toma de ella la hora de caducidad, no caduca por su cuenta lo que está en la API y vuelve a leer la lista cada minuto: una aprobación caducada pasa a pregunta en Inicio. Si el encargo ya espera a una persona en la API (ESCALADO), la oficina no lo mueve para que coincida el nombre del estado. Lo que no está en la API sigue la regla de N4 en el navegador.
- *Piezas.* Cada pieza de un encargo en equipo se sube como tarea del encargo (clave de idempotencia: el id de la pieza), en la misma cola que su encargo para que lleguen en orden: «en marcha» → `running`, «hecha» → `succeeded`.
- *Desde otra oficina.* Lo que llega de la API se muestra con sus piezas, su aplazamiento y su caducidad, y si espera el OK se puede aprobar, devolver (lo rehace quien lo pidió, no un agente de esta oficina) o descartar. Si lo pidió quien está conectado, la oficina lo avisa y la API no lo acepta: vuelve a «espera tu OK».

- *Decidido en otra oficina.* Si otra oficina aprueba, devuelve o descarta un encargo de esta, al leer la API esta se pone al día (hecha, pregunta con el motivo o rechazada) y no lo reabre ni vuelve a pedir el OK. Arreglado en el repaso del 27/11: antes lo reabría y dejaba en la auditoría cuatro pasos que nadie dio (prueba de humo en Chromium, antes y después).

**Lo que aún no hace.** Reglas, memoria, proyectos y entregables siguen solo en el almacén de la oficina. Si la API no acepta una decisión sobre un encargo de esta misma oficina, la oficina lo avisa, pero el encargo queda como decidido en ella y pendiente en la API (en los que llegan de la API sí vuelve a «espera tu OK»).

**Prueba de humo (26/11/2026, Chromium sin interfaz).** Con PostgreSQL desechable, migraciones, semilla y la API: un encargo creado en la oficina queda en la tabla `solicitud` en PENDIENTE_APROBACION con 7 eventos de auditoría (alta, cinco cambios de estado y la petición de aprobación); en modo demostración la oficina lo da por hecho sin un socio y la API no lo acepta como aprobado. Los dos encargos de la semilla aparecen en Inicio como preguntas. La misma oficina servida como archivos sin API guarda como siempre y no muestra el botón. Sin errores en la consola en ninguno de los dos casos. `docker compose up` sigue sin poder probarse aquí (ver «Pendiente de tu aprobación» en docs/21).

**Segunda prueba de humo (27/11/2026).** Mismo montaje. Un encargo inventado que espera el OK se pospone (la oficina lo crea en la API y pide la aprobación: PENDIENTE_APROBACION) y después se descarta: la oficina envía la decisión «rechazada» en vez de un cambio libre, la API la rechaza con 403 porque quien decide es quien la pidió, la oficina lo avisa y en la API sigue pendiente. Antes del arreglo, el mismo usuario lo sacaba a RECHAZADO sin decidir y la aprobación quedaba pendiente para siempre.

**Tercera prueba de humo (27/11/2026, N3c).** PostgreSQL desechable, migraciones, semilla y la API; dos oficinas en Chromium (tramitadora y gerente, dos tokens del mismo cliente inventado). (1) La tramitadora crea tres encargos: uno espera el OK (la hora de caducidad de la oficina es la de la API), otro en equipo con una pieza que acaba como tarea `succeeded`, y lo pospone hasta mañana: en la API queda `pospuesto_hasta` y sigue PENDIENTE_APROBACION. (2) Se borra el almacén del navegador y se recarga: el encargo vuelve de PostgreSQL pospuesto, con su caducidad y con su pieza hecha. (3) La tramitadora intenta aprobar lo que pidió ella: la API responde 403 y la oficina lo devuelve a «espera tu OK». (4) El gerente lo ve pospuesto en su oficina y lo aprueba: ENTREGADO. (5) Se adelanta el plazo de dos aprobaciones (una importada y otra de la propia oficina): tras leer la API, las dos son preguntas en Inicio y en la API quedan en ESCALADO con los dos eventos de `sistema:caducidad`, sin pasos de más. Único error en la consola: el 403 esperado del paso 3.

## Lo que falta (plan)

- Proveedor de identidad real (S3, antes de L2); hoy los tokens se firman con un secreto compartido (D-028).
- Pasar el motor en memoria (`varios.procesos`) a estas tablas (S5).
- Comprobar `docker compose up` en un equipo de los socios: en el entorno de Claude, la imagen no puede descargar paquetes.
