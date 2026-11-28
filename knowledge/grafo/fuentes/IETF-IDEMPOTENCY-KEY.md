---
tipo: "fuente"
id: "IETF-IDEMPOTENCY-KEY"
titulo: "The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header-07)"
organismo: "IETF, grupo HTTPAPI (J. Jena y S. Dalal)"
fuente_tipo: "recomendacion-tecnica"
version: "borrador 07, 15/10/2025; caducó el 18/04/2026 (leída el 28/11/2026; no se ha mirado si hay una versión más nueva)"
autoridad: "media"
vigencia: "borrador"
estado: "draft"
citada: 3
tags:
  - "fuente"
  - "vigencia/borrador"
---
<!-- Generado por tools/obsidian_gen.py. No editar a mano: se regenera con tools/brain_build.py. -->
# IETF-IDEMPOTENCY-KEY · The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header-07)

- Origen: <https://www.ietf.org/archive/id/draft-ietf-httpapi-idempotency-key-header-07.html>
- Registro: [[knowledge/fuentes/registro|registro de fuentes]]
- Nota: §2.2: la clave «MUST NOT be reused with another request with a different request payload». §2.7: «If there is an attempt to reuse an idempotency key with a different request payload» «the resource SHOULD reply with a HTTP `422` status code». Es un borrador, no una norma. Base de que la API responda 422 cuando una clave de idempotencia se repite con otro estado de destino (repaso del 28/11).

## Citada en

- [[docs/21-trabajo-nocturno|Trabajo nocturno de Claude]]
- [[docs/24-base-de-datos|Base de datos (D-023, propuesta)]]
- [[docs/informes/2026-11-28|Informe de la mañana · 28/11/2026]]
