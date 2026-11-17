# Cerebro en Claude

Hay dos cerebros y no se mezclan:

- **Cerebro de trabajo (ya):** Claude configurado con todo lo que sabemos (oferta, método, decisiones, clientes). Prepara reuniones, propuestas, actas y nos ayuda a programar.
- **Cerebro producto (desde el piloto):** el sistema de `docs/02` a `docs/06`. Código propio que usa modelos de IA por API. Se empieza por un solo proceso del primer cliente.

## Ocho pasos para el cerebro de trabajo

1. **Plan de Claude.** Para compartir proyectos entre los dos hace falta plan Team. Precios publicados en dólares sin impuestos (verificar en claude.com/pricing antes de pagar): Pro desde 20 $/mes, Max desde 100 $/mes, Team desde 25 $/puesto/mes (20 $ anual). Comprobar si el tipo de puesto incluye Claude Code.
2. **Una sola fuente de verdad.** Este repositorio. Una versión de cada documento; lo antiguo a `archive/`.
3. **Proyecto "Varios · Cerebro".** Instrucciones en `claude/instrucciones-proyecto.md`; este repositorio conectado como conocimiento.
4. **Habilidades.** Ver lista en `claude/instrucciones-proyecto.md`. Se crea una cuando la tarea se ha hecho dos veces a mano.
5. **Conectores.** Gmail, Google Calendar, Google Drive y GitHub. Claude pide confirmación antes de enviar o crear.
6. **Claude Code.** Trabaja sobre este repositorio siguiendo `CLAUDE.md`. Se usa desde el piloto.
7. **Rutinas.** Tras cada reunión: acta al repo (15 min). Cada viernes: revisión de 45 min y actualizar el plan. Cada decisión: una línea en `DECISIONS.md`.
8. **Comprobar.** 3–4 casos de prueba por habilidad; se repiten si cambia.

## No hacer
- Seguir generando documentos de arquitectura antes de hablar con clientes.
- Pegar datos reales de clientes sin revisar las condiciones del plan y su contrato.
- Construir el CEO digital completo antes del primer proceso.
