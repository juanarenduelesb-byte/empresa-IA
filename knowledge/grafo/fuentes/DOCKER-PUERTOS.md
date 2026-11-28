---
tipo: "fuente"
id: "DOCKER-PUERTOS"
titulo: "Docker: Port publishing and mapping"
organismo: "Docker (documentación oficial)"
fuente_tipo: "documentacion-producto"
version: "consultado 28/11/2026"
autoridad: "media"
vigencia: "vigente"
estado: "draft"
citada: 2
tags:
  - "fuente"
  - "vigencia/vigente"
---
<!-- Generado por tools/obsidian_gen.py. No editar a mano: se regenera con tools/brain_build.py. -->
# DOCKER-PUERTOS · Docker: Port publishing and mapping

- Origen: <https://docs.docker.com/engine/network/port-publishing/>
- Registro: [[knowledge/fuentes/registro|registro de fuentes]]
- Nota: «Publishing container ports is insecure by default.» Por defecto publica en todas las direcciones del ordenador (0.0.0.0 y [::]); con 127.0.0.1 «only the Docker host can access the published container port». Base de publicar la base y la API solo en 127.0.0.1 en docker-compose.yml (repaso del 28/11).

## Citada en

- [[docs/21-trabajo-nocturno|Trabajo nocturno de Claude]]
- [[docs/24-base-de-datos|Base de datos (D-023, propuesta)]]
