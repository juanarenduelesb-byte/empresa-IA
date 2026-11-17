# Varios · empresa-ia

Repositorio maestro de Varios (nombre provisional), consultora de IA para empresas medianas y reguladas. Socios: Juan (producto y construcción) y Álvaro (clientes y relación); reparto pendiente de confirmar.

Contiene visión, arquitectura, procesos, decisiones, el plan de 12 semanas y una web visual en `site/`. Todavía no contiene código del sistema.

## Contexto rápido
- Oferta en cuatro fases: Diagnosticar (3 semanas) · Diseñar (2) · Construir (4–8, piloto con pago 50/50 según métrica firmada) · Operar (cuota mensual).
- Prioridad actual: conseguir el primer cliente de pago. Ver `docs/10-plan-12-semanas.md`.
- Estado: 0 clientes, 0 líneas de código. No construir el "CEO digital" completo antes del primer proceso piloto (D-006).

## Reglas
- No subir secretos, credenciales ni datos reales de clientes. Solo datos inventados en pruebas.
- No inventar datos, clientes, cifras ni fuentes. Separar hecho, hipótesis y propuesta.
- Toda decisión estructural se registra en DECISIONS.md (fecha, decisión, motivo, estado).
- Proceso antes que agente. Código fijo para reglas y cálculos; IA para lenguaje y ambigüedad.
- El cliente (tenant) se obtiene de la identidad autenticada, nunca de un dato que envía el usuario.
- Cualquier acción externa, financiera, legal o contractual requiere aprobación humana.
- Antes de añadir una tecnología nueva, justificar por qué en DECISIONS.md.
- Si cambias algo de `docs/`, revisa si la web de `site/` dice lo mismo.

## Estructura
- `docs/` documentación funcional y técnica (empieza por `00-negocio.md`)
- `site/` web visual del proyecto, HTML estático
- `claude/` instrucciones del proyecto de Claude y habilidades previstas
- `processes/` catálogo de procesos (uno por carpeta, con AS-IS, TO-BE y métricas)
- `knowledge/` principios y plantillas de conocimiento
- `governance/` seguridad, calidad, legal
- `archive/` versiones antiguas y contexto

## Stack previsto para el piloto
Python, FastAPI, Pydantic, PostgreSQL, Docker Compose, pytest, Ruff, Alembic. Nada más sin una decisión registrada.
