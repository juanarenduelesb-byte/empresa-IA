# Varios — repositorio maestro

> **Varios** es el nombre provisional (decidido el 17/11/2026). Algunos documentos antiguos usan "ExcluSa", "Esclusa" o "Cauce": es el mismo proyecto.

Consultora de inteligencia artificial para empresas medianas y reguladas. Elegimos un proceso concreto de una empresa, lo medimos, lo automatizamos con IA y controles, y demostramos el resultado con una métrica firmada antes de escalar.

Este repositorio es **la memoria oficial del proyecto**. Si algo no está aquí, no existe. Está pensado para que cualquier persona (o Claude, en una cuenta nueva) tenga todo el contexto desde el primer minuto.

## Estado a 17/11/2026

| | |
|---|---|
| Socios | 2 (Juan y Álvaro) |
| Arquitectura y método | Diseñados (ver `docs/`) |
| Clientes con contrato | 0 |
| Código del sistema | 0 líneas: todavía no se construye |
| Siguiente objetivo | Diagnóstico de pago entregado y piloto firmado antes del 12/02/2027 |

## Empieza aquí

1. **Mapa visual del proyecto:** abre `site/index.html` en el navegador. Son 12 páginas, una por tema, incluida una **simulación interactiva** del cerebro (`site/simulacion.html`).
2. **El negocio:** [docs/00-negocio.md](docs/00-negocio.md)
3. **El plan de 12 semanas:** [docs/10-plan-12-semanas.md](docs/10-plan-12-semanas.md)
4. **Cómo montar el cerebro en Claude:** [docs/11-cerebro-en-claude.md](docs/11-cerebro-en-claude.md)
5. **Decisiones:** [DECISIONS.md](DECISIONS.md)

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
- [10 · Plan de 12 semanas](docs/10-plan-12-semanas.md)
- [11 · Cerebro en Claude](docs/11-cerebro-en-claude.md)
- [12 · Simulación del cerebro](docs/12-simulacion.md)

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
archive/       contexto consolidado y versiones antiguas
```

No subir secretos, credenciales ni datos reales de clientes. Toda decisión estructural se registra en `DECISIONS.md`.
