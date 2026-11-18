---
tipo: "habilidad"
id: "copias-restauracion"
usan: 1
estado: "draft"
tags:
  - "habilidad"
---
<!-- Generado por tools/agentes_gen.py desde tools/org_data/. No editar a mano. -->

# Copias y restauración probada

`copias-restauracion` · **Estado:** draft

**Cuándo se usa:** Al montar la base de datos y antes de cada control de paso (S11).

## Pasos

1. Política: qué se copia, cada cuánto, dónde (al menos una copia fuera) y cuánto tiempo.
2. Cifrado y control de acceso de las copias.
3. Restauración completa en un entorno limpio, cronometrada.
4. Comprobación de integridad de los datos restaurados.
5. Runbook con los pasos exactos y el tiempo medido.

## Resultado

Informe de restauración con fecha, tiempo y resultado, más el runbook.

## Lista de control

- ¿Se ha restaurado de verdad?
- ¿Hay una copia fuera del entorno principal?

## Quién la usa

- [Plataforma y operaciones](../../knowledge/agentes/ops.md)
