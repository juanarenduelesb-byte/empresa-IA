---
tipo: "habilidad"
id: "prevision-tesoreria"
usan: 1
estado: "draft"
tags:
  - "habilidad"
---
<!-- Generado por tools/agentes_gen.py desde tools/org_data/. No editar a mano. -->

# Previsión de tesorería a 13 semanas

`prevision-tesoreria` · **Estado:** draft

**Cuándo se usa:** Cada semana, y antes de cualquier decisión de gasto, contratación o precio.

## Pasos

1. Partir del saldo real de hoy.
2. Cobros esperados por hito y fecha, ajustados por probabilidad y por el retraso medio real.
3. Pagos comprometidos por fecha (proveedores, impuestos, cuotas, sueldos si los hay).
4. Escenario prudente, base y optimista con sus supuestos.
5. Semana del saldo mínimo y umbral de alerta.

## Resultado

Hoja semanal con saldo previsto, semana crítica y acciones si se cruza el umbral.

## Lista de control

- ¿Los cobros del 50/50 dependen de la métrica en el escenario prudente?
- ¿Cada supuesto está escrito?

## Quién la usa

- [Director financiero](../../knowledge/agentes/cfo.md)
