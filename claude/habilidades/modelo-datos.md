<!-- Generado por tools/agentes_gen.py desde tools/org_data/. No editar a mano. -->

# Modelo de datos

`modelo-datos` · **Estado:** draft

**Cuándo se usa:** Al diseñar tablas, migraciones o esquemas.

## Pasos

1. Entidades y relaciones; cliente (tenant) en cada tabla de negocio.
2. Auditoría: quién, qué, cuándo, desde dónde.
3. Datos personales: minimización, retención y borrado.
4. Migración reversible y probada desde cero.

## Resultado

Diagrama, definición de tablas y migración.

## Lista de control

- ¿El tenant sale de la identidad, nunca del usuario?
- ¿Hay retención definida?

## Quién la usa

- [Backend](../../knowledge/agentes/back.md)
