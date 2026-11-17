<!-- Generado por tools/agentes_gen.py desde tools/org_data/. No editar a mano. -->

# Integración continua

`integracion-continua` · **Estado:** draft

**Cuándo se usa:** Al montar o cambiar el pipeline (S1) y ante cada fallo de CI.

## Pasos

1. Cada cambio pasa pruebas, lint y escáner de secretos antes de entrar.
2. Tiempo de CI bajo control (objetivo: minutos, no decenas).
3. Fallos con causa raíz: nunca se desactiva una prueba para poner verde.
4. Rama principal protegida y propuestas de cambios obligatorias.

## Resultado

Pipeline documentado y en verde, con tiempos.

## Lista de control

- ¿Hay escáner de secretos?
- ¿Alguna prueba desactivada para pasar?

## Quién la usa

- [Plataforma y operaciones](../../knowledge/agentes/ops.md)
