# Workflow bloqueado o fallido

**Proceso:** P22, P35 · **Estado:** draft (no ensayado)

## Pasos
1. Leer el último evento de auditoría y la clasificación del error.
2. Si es transitorio y quedan intentos: el motor reintenta solo.
3. Si es de autorización, seguridad o política: no reintentar; resolver la causa.
4. Antes de repetir una acción externa, comprobar con la clave de idempotencia si ya se hizo.
5. Si una secuencia quedó a medias: compensar o registrar qué no se pudo revertir.
6. Reanudar con autorización registrada.

## No hacer
- Forzar el estado en la base de datos.
- Repetir una acción externa sin comprobar.
