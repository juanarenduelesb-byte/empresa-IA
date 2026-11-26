# Varios — repositorio maestro

> **Varios** es el nombre provisional (decidido el 17/11/2026). Algunos documentos antiguos usan "ExcluSa", "Esclusa" o "Cauce": es el mismo proyecto.

Consultora de inteligencia artificial para empresas medianas y reguladas. Elegimos un proceso concreto de una empresa, lo medimos, lo automatizamos con IA y controles, y demostramos el resultado con una métrica firmada antes de escalar.

Este repositorio es **la memoria oficial del proyecto**. Si algo no está aquí, no existe. Está pensado para que cualquier persona (o Claude, en una cuenta nueva) tenga todo el contexto desde el primer minuto.

## Estado a 17/11/2026

| | |
|---|---|
| Socios | 2 (Juan y Álvaro) |
| Arquitectura y método | Diseñados: Guía v1.4, Atlas Evolución v1.1, Marco legal v1.0 (ver `docs/fuentes/`) |
| Clientes con contrato | 0 |
| Código del sistema | 0 líneas: todavía no se construye |
| Siguiente objetivo | Construir el proceso de referencia y estar listo para el primer cliente el 12/02/2027 (D-011) |

## Empieza aquí

1. **Mapa visual del proyecto:** abre `site/index.html` en el navegador. Son 15 páginas, una por tema, con una **simulación interactiva** del cerebro (`site/simulacion.html`) y el **Atlas** de 17 diagramas (`site/atlas.html`).
2. **Diagramas en GitHub:** [docs/atlas/](docs/atlas/README.md). GitHub los dibuja directamente.
3. **El negocio:** [docs/00-negocio.md](docs/00-negocio.md)
4. **El plan de construcción (hasta el 12/02/2027):** [docs/10-plan-12-semanas.md](docs/10-plan-12-semanas.md)
5. **Cómo montar el cerebro en Claude:** [docs/11-cerebro-en-claude.md](docs/11-cerebro-en-claude.md)
6. **Decisiones:** [DECISIONS.md](DECISIONS.md)
7. **Base de datos y API (código):** [docs/24-base-de-datos.md](docs/24-base-de-datos.md). Arranque: `cp .env.example .env` y `docker compose up --build`.
8. **Plan diario y trabajo nocturno de Claude:** [docs/22-plan-hasta-febrero.md](docs/22-plan-hasta-febrero.md) · informes en [docs/informes/](docs/informes/README.md)

## Documentación

- [00 · Negocio](docs/00-negocio.md)
- [01 · Visión y modelo operativo](docs/01-vision-y-modelo-operativo.md)
- [02 · Arquitectura general](docs/02-arquitectura-general.md)
- [03 · CEO digital y orquestación](docs/03-ceo-digital-y-orquestacion.md)
- [04 · Motor de conocimiento](docs/04-motor-de-conocimiento.md)
- [05 · Agentes, procesos e integraciones](docs/05-agentes-procesos-e-integraciones.md)
- [06 · Seguridad y gobierno](docs/06-seguridad-y-gobierno.md)
- [07 · Calidad, infraestructura y operación](docs/07-calidad-infraestructura-y-operacion.md)
- [08 · Roadmap y decisiones](docs/08-roadmap-y-decisiones.md)
- [09 · Inventario documental](docs/09-inventario-documental.md)
- [10 · Plan de construcción](docs/10-plan-12-semanas.md)
- [11 · Cerebro en Claude](docs/11-cerebro-en-claude.md)
- [12 · Simulación del cerebro](docs/12-simulacion.md)
- [13 · Procesos P01–P38 y estados](docs/13-procesos-y-estados.md)
- [14 · Reglas del CEO](docs/14-reglas-del-ceo.md)
- [16 · Correcciones a los documentos](docs/16-correcciones.md)
- [Atlas de diagramas](docs/atlas/README.md)
- [Documentos fuente en Markdown](docs/fuentes/) (Guía v1.4, Atlas Evolución v1.1, Marco legal v1.0, mapas 2–9)

## Principios

Proceso antes que agente. Permisos antes que recuperación. Código determinista para operaciones exactas; IA para lenguaje y ambigüedad. Aprobación humana proporcional al riesgo. Trazabilidad y medición de resultados.

## Estructura

```
CLAUDE.md      reglas para Claude Code en este repositorio
DECISIONS.md   registro de decisiones (fecha, decisión, motivo, estado)
claude/        instrucciones para el proyecto de Claude y lista de habilidades
docs/          documentación funcional y técnica
site/          web visual del proyecto (abrir site/index.html)
processes/     catálogo de procesos, uno por carpeta
knowledge/     principios y plantillas de conocimiento
governance/    seguridad, calidad y legal
archive/       contexto consolidado y originales (archive/originales: Word e imagen recibidos)
tools/         atlas_data.py y gen.py: fuente única de los diagramas
```

No subir secretos, credenciales ni datos reales de clientes. Toda decisión estructural se registra en `DECISIONS.md`.
