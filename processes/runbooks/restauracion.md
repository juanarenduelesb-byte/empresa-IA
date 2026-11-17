# Restauración de copias

**Proceso:** P26 · **Estado:** draft (no ensayado)

## Pasos
1. Elegir el punto de restauración según el RPO acordado.
2. Restaurar en un entorno limpio.
3. Verificar integridad y aislamiento entre clientes.
4. Medir el tiempo real (RTO).
5. Registrar el resultado: una copia no probada no es recuperable.

## No hacer
- Restaurar directamente sobre producción sin probar.
