# Definiciones ejecutables

| Archivo | Qué es |
|---|---|
| [`encargo.json`](encargo.json) | Máquina de estados del encargo. Transiciones de la Guía v1.4 §4 y las *añadidas* para cubrir sus huecos (pendientes de confirmar) |
| [`objetos.json`](objetos.json) | Estados de tarea, instancia, definición, conector, despliegue, ficha y capacidad (docs/13, Atlas §10.1) |
| [`ciclo-encargo.json`](ciclo-encargo.json) | Workflow P01→P11 con tipo, responsable, timeout, intentos, criterio y aprobación por tarea |

Las valida `src/varios/procesos/definiciones.py` y lo prueba `tests/test_definiciones.py`. Una definición aprobada no se modifica: un cambio crea una versión nueva (Atlas §6.1).
