# Varios · empresa-ia

Repositorio maestro de Varios (nombre provisional), consultora de IA para empresas medianas y reguladas. Socios: Juan (producto y construcción) y Álvaro (clientes y relación); reparto pendiente de confirmar.

Contiene visión, arquitectura, procesos, decisiones, el plan de 12 semanas y una web visual en `site/`. Todavía no contiene código del sistema.

## Contexto rápido
- Oferta en cuatro fases: Diagnosticar (3 semanas) · Diseñar (2) · Construir (4–8, piloto con pago 50/50 según métrica firmada) · Operar (cuota mensual).
- Prioridad actual (D-011): construir hasta el 12/02/2027 el proceso de referencia con datos inventados, siguiendo `docs/10-plan-12-semanas.md`. Clientes desde el 15/02/2027. Ningún dato real.
- Estado: 0 clientes, 0 líneas de código. No construir el "CEO digital" generalista: solo el CEO limitado que necesita el proceso de referencia (D-006).

## Documentos base (por orden de autoridad)
1. `DECISIONS.md`
2. `docs/fuentes/Guia_de_Arranque_Proyecto_v1.4_Diseno_Cerrado.md` (línea base de diseño)
3. `docs/fuentes/Atlas_Evolucion_v1.1_Modelo_Operativo_Procesos_y_Despliegue.md` (procesos y despliegue)
4. `docs/fuentes/Marco_Integral_Legal_Ciberseguridad_IA_Espana_UE_2026-11-16.md` (legal)
5. `docs/atlas/` (diagramas corregidos) y `docs/16-correcciones.md`
Puertas: G0–G6 = cliente; L0–L4 = técnicas. No confundirlas.

## Reglas
- No subir secretos, credenciales ni datos reales de clientes. Solo datos inventados en pruebas.
- No inventar datos, clientes, cifras ni fuentes. Separar hecho, hipótesis y propuesta.
- Toda decisión estructural se registra en DECISIONS.md (fecha, decisión, motivo, estado).
- Propuestas de cambios (D-012): al terminar, abre la propuesta y acéptala tú mismo si no tiene conflictos ni pruebas fallidas, y resume en el chat qué has aceptado. Déjala abierta para un socio si marca como aprobada una decisión, cambia CLAUDE.md, toca documentos legales o lleva datos reales o secretos.
- Proceso antes que agente. Código fijo para reglas y cálculos; IA para lenguaje y ambigüedad.
- El cliente (tenant) se obtiene de la identidad autenticada, nunca de un dato que envía el usuario.
- Cualquier acción externa, financiera, legal o contractual requiere aprobación humana.
- Antes de añadir una tecnología nueva, justificar por qué en DECISIONS.md.
- Si cambias algo de `docs/`, revisa si la web de `site/` dice lo mismo.
- Los diagramas se editan solo en `tools/atlas_data.py` y se regeneran con `python3 tools/gen.py site/js/atlas-data.js docs/atlas`.
- Si cambias documentos, regenera el cerebro de la oficina con `python3 tools/brain_build.py oficina/brain.json`.

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
