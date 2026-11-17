# Caída del proveedor de IA

**Proceso:** P26 · **Estado:** draft (no ensayado)

## Pasos
1. Confirmar la caída: estado del proveedor y errores en P15.
2. Pausar las colas de tareas de IA; no reintentar en bucle.
3. Activar la alternativa aprobada (P16), si existe.
4. Si no hay alternativa, procedimiento manual y aviso a los afectados.
5. Al volver, reanudar desde el estado persistido sin duplicar.
6. Registrar el incidente y la lección.

## No hacer
- Cambiar de modelo sin evaluación.
- Reintentar sin límite.
