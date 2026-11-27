---
tipo: "fuente"
id: "OWASP-FASTAPI"
titulo: "FastAPI Security Cheat Sheet"
organismo: "OWASP Cheat Sheet Series"
fuente_tipo: "recomendacion-tecnica"
version: "sin fecha visible (leída el 26/11/2026)"
autoridad: "media"
vigencia: "vigente"
estado: "draft"
citada: 1
tags:
  - "fuente"
  - "vigencia/vigente"
---
<!-- Generado por tools/obsidian_gen.py. No editar a mano: se regenera con tools/brain_build.py. -->
# OWASP-FASTAPI · FastAPI Security Cheat Sheet

- Origen: <https://cheatsheetseries.owasp.org/cheatsheets/FastAPI_Security_Cheat_Sheet.html>
- Registro: [[knowledge/fuentes/registro|registro de fuentes]]
- Nota: Autenticar y autorizar con Depends(); OAuth2PasswordBearer no verifica el token. JWT con PyJWT, algoritmo fijo y exp, iss y aud obligatorios; secretos fuera del código. «Authentication alone does not authorize an operation». Pydantic ignora por defecto los campos no declarados; usar esquemas de entrada separados.

## Citada en

- [[docs/31-identidad|Identidad y roles: opciones para los socios y, más adelante, los clientes (S3a)]]
