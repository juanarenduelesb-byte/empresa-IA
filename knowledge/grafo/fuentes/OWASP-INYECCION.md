---
tipo: "fuente"
id: "OWASP-INYECCION"
titulo: "LLM Prompt Injection Prevention Cheat Sheet"
organismo: "OWASP Cheat Sheet Series"
fuente_tipo: "recomendacion-tecnica"
version: "sin fecha visible (leída el 28/11/2026)"
autoridad: "media"
vigencia: "vigente"
estado: "draft"
citada: 2
tags:
  - "fuente"
  - "vigencia/vigente"
---
<!-- Generado por tools/obsidian_gen.py. No editar a mano: se regenera con tools/brain_build.py. -->
# OWASP-INYECCION · LLM Prompt Injection Prevention Cheat Sheet

- Origen: <https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html>
- Registro: [[knowledge/fuentes/registro|registro de fuentes]]
- Nota: «Normalize text before screening it», «screen a normalized copy instead of rewriting the user's input» y «Send unexpected zero-width or tag characters to review»; el filtro por frases «is not a security boundary» y conviene «Require human approval for consequential tool actions before execution». Base de la normalización de los detectores del CEO limitado (repaso del 28/11).

## Citada en

- [[docs/21-trabajo-nocturno|Trabajo nocturno de Claude]]
- [[processes/ceo-control-a/README|Banco del Control A: 25 encargos para el CEO limitado (C2)]]
