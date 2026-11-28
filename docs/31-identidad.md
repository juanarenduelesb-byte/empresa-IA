# Identidad y roles: opciones para los socios y, más adelante, los clientes (S3a)

**Estado:** comparativa y propuesta (D-033). Fecha: 27/11/2026. No añade ninguna tecnología: lo que se proponga entra solo cuando un socio apruebe D-033. Las cifras y citas son de las páginas oficiales leídas esta noche (fuentes al final); lo que no se ha podido leer va marcado «sin confirmar».

## Qué hace falta

| Necesidad | Por qué |
|---|---|
| Entrada de los dos socios con segundo factor | M-047: hoy la API acepta un token firmado con un secreto compartido (D-028), que vale para pruebas, no para L2 |
| Más adelante, personas de los clientes con su propio acceso, separadas por cliente | El cliente sale siempre de la identidad autenticada (`CLAUDE.md`); la RLS ya separa los datos |
| Que el proveedor diga **quién es** la persona, y Varios **qué puede hacer** | Los roles (aprobador, agente, cliente) se leen de la base de Varios, no del token: un token no puede darse a sí mismo el rol de aprobador (D-028). Se mantiene con cualquier opción |
| Datos en la UE y lo más cerca posible de nosotros | Clientes regulados; región de datos pendiente (decisión de Juan, antes del 05/02/2027) |
| Poco peso en Docker Compose y poco mantenimiento | Dos socios a tiempo parcial |
| Estándar (OpenID Connect) | Así la API solo cambia `varios.api.identidad.verificar` y lo demás no se entera (D-028) |

## Las opciones

| | Keycloak | Zitadel | authentik | Microsoft Entra External ID | Authlib + cuenta que ya tengáis |
|---|---|---|---|---|---|
| Qué es | Gestor de identidades autoalojado | Gestor de identidades autoalojado o en su nube | Gestor de identidades autoalojado | Servicio de identidad de Microsoft para usuarios externos | Librería de Python para OAuth y OpenID Connect; no es un proveedor, se apoya en uno (Microsoft, Google…) |
| Licencia | Apache 2.0 (`KEYCLOAK-REPO`); proyecto de la CNCF en *incubating* desde el 10/04/2023 (`CNCF-KEYCLOAK`) | AGPL 3.0 desde la v3 (anunciada para el 31/03/2025); según Zitadel, usar sus API sin modificar el código «doesn't trigger reciprocal requirements» (`ZITADEL-AGPL`) | Núcleo MIT, con una parte *enterprise* con licencia propia que no se ha leído (`AUTHENTIK-REPO`) | Servicio de pago por uso | BSD o comercial; «Any project, open or closed source, can use the BSD license» (`AUTHLIB`) |
| Coste | Sin licencia; el coste es el servidor | Sin licencia autoalojado; nube de pago (precio sin leer) | Sin licencia el núcleo | «free for the first 50,000 MAUs»; el precio por encima no se mostraba en la página. El SMS como segundo factor es un complemento de pago sin tramo gratis (`ENTRA-EXTERNAL-ID-PRECIOS`) | Gratis; el coste es el del proveedor que se use |
| Dónde quedan los datos | En nuestro servidor, en la región que elijamos | Autoalojado: en el nuestro | En el nuestro | En el inquilino de Microsoft. **Sin confirmar** en qué región | En el proveedor que se use |
| Segundo factor | «passkey, recovery codes and TOTP/HOTP via Google Authenticator or FreeOTP» (`KEYCLOAK-ADMIN`) | TOTP, U2F (huella, Windows Hello, llaves), OTP por correo y por SMS (con Twilio); se puede obligar (`ZITADEL-MFA`) | **Sin confirmar** (no leído) | Por SMS como complemento de pago; el resto **sin confirmar** | El del proveedor |
| Peso en Docker Compose | Un contenedor más. Según su guía, la base de memoria de una instancia (con 10.000 sesiones en caché) es de 1.250 MB, y la CPU depende del volumen: 1 vCPU por cada 15 entradas con contraseña por segundo (`KEYCLOAK-SIZING`). En producción necesita una base de datos de verdad (PostgreSQL 14–18 está soportada; la de desarrollo, `dev-file`, «is not suitable for production», `KEYCLOAK-DB`) | Un contenedor más; requisitos **sin confirmar** | Un contenedor más; requisitos **sin confirmar** | Nada en Compose | Nada en Compose |
| Lo que cambia en Varios | La API verifica tokens RS256 con las claves públicas del proveedor (JWKS); la oficina entra con el flujo de código y PKCE | Igual | Igual | Igual | La API hace de cliente OIDC (Authlib tiene integración con Starlette y FastAPI como cliente web, `AUTHLIB`) |

Arranque de prueba de Keycloak según su guía: `docker run … quay.io/keycloak/keycloak:26.8.2 start-dev` con usuario y contraseña de administrador por variables (`KEYCLOAK-DOCKER`). Es solo para desarrollo.

## Propuesta (D-033)

1. **Para el piloto con datos inventados (hasta L2): Keycloak autoalojado**, en el mismo Docker Compose, con su propia base en el PostgreSQL que ya tenemos (otra base, no las tablas de Varios). Razones: licencia Apache 2.0 sin dudas para ofrecerlo a clientes, proyecto de la CNCF, segundo factor con passkeys y TOTP de serie, los datos se quedan en nuestro servidor (lo que más pesa con clientes regulados) y habla OpenID Connect, así que cambiarlo después no toca la API. El precio es la memoria: alrededor de 1,25 GB más en el servidor.
2. **Alternativa si los socios prefieren no mantener nada: Microsoft Entra External ID**, gratis hasta 50.000 usuarios activos al mes, si ya usáis Microsoft 365 (pregunta 12 de `docs/21`). Antes hay que confirmar la región de los datos y qué segundo factor entra sin coste.
3. **Descartados por ahora:** Zitadel (AGPL 3.0: usarlo sin cambios no obliga a nada según Zitadel, pero si algún día lo modificamos y lo ofrecemos a clientes sí; mejor revisarlo con el abogado antes), authentik (la parte *enterprise* tiene licencia propia sin leer) y Authlib con una cuenta personal (no es un proveedor: depende de uno, y con Google o Microsoft personales no tenemos control sobre el segundo factor de los socios).
4. **Se mantiene con cualquier opción:**
   - El proveedor dice quién es; los roles siguen en la base de Varios. Lo que el token diga de roles (`realm_access.roles` en Keycloak) se ignora, y una prueba lo comprueba.
   - El cliente sale del token y tiene que casar con un usuario activo de ese cliente en la base.
   - Hace falta una correspondencia entre el sujeto del proveedor (`iss` + `sub`) y el usuario de Varios: hoy `sub` tiene que ser el identificador de Varios, y un sujeto externo responde 401 (prueba incluida). Sería una columna nueva en `usuario`, con su migración, cuando se apruebe.
   - Algoritmo fijo (RS256 con las claves públicas del proveedor) y `exp`, `iss` y `aud` obligatorios, como hoy con HS256 (hoja de FastAPI de OWASP, `OWASP-FASTAPI`).
   - **Lo que todavía no separa (hecho, repaso del 28/11):** hoy el papel **cliente** solo se distingue al aprobar. Cualquier persona activa de un cliente, tenga el papel que tenga, puede crear encargos, moverlos (también a CANCELADO o RECHAZADO cuando la máquina lo deja), crear y mover tareas y posponer. Con dos socios y datos inventados no importa; antes de dar acceso a personas de un cliente (después de L2) hay que decidir qué puede hacer cada papel y que la API lo compruebe en cada ruta, empezando por negarlo todo (propuesta, sin decidir).
5. **Tecnología que entraría al aprobarlo:** Keycloak (contenedor) y, para verificar RS256, el extra `crypto` de PyJWT (la librería `cryptography`). Cada una con su línea en `DECISIONS.md` cuando se apruebe; ninguna se añade ahora.

## Pruebas con un proveedor simulado

`tests/db/test_identidad_proveedor.py`, contra PostgreSQL real. Un proveedor simulado emite tokens con la forma de los de un proveedor OIDC (como Keycloak: `iss` con el realm, `aud`, `azp`, `typ`, `realm_access.roles`). Van firmados con el secreto de pruebas porque hoy la API solo verifica HS256; lo que se comprueba no depende del algoritmo.

| Prueba | Qué comprueba |
|---|---|
| Los tres papeles | Un **cliente** ve los encargos de su cliente pero no aprueba, aunque su token diga «aprobador» o «admin»; un **agente** no aprueba nunca; el **socio** que pidió la aprobación tampoco; otro socio sí |
| Emisor, audiencia, caducidad y firma | 401 con otro emisor, otra audiencia, caducado, firmado por otro, aún no válido (`nbf`), sin cliente y sin firma (`alg: none`) |
| El cliente sale del token | Un token con el usuario de un cliente y el cliente de otro, un usuario que no está en la base o un sujeto externo: 401 |
| Usuario desactivado | Deja de entrar en la siguiente petición, aunque su token siga vigente |

## Fuentes

`KEYCLOAK-SIZING`, `KEYCLOAK-DB`, `KEYCLOAK-ADMIN`, `KEYCLOAK-DOCKER`, `KEYCLOAK-REPO`, `CNCF-KEYCLOAK`, `ZITADEL-AGPL`, `ZITADEL-MFA`, `AUTHENTIK-REPO`, `ENTRA-EXTERNAL-ID-PRECIOS`, `AUTHLIB` y `OWASP-FASTAPI`, en el [registro de fuentes](../knowledge/fuentes/registro.md). Leídas el 27/11/2026.
