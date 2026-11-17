# Caso de práctica · Atalaya Correduría de Seguros (ficticia)

**Estado:** preparado para lanzarlo en la oficina de agentes · **Datos:** todos inventados (D-011)

Primer proyecto completo de la oficina: el diagnóstico de la apertura de siniestros (el proceso de referencia del plan) en una correduría que no existe. Sirve para dos cosas: comprobar que los agentes trabajan juntos y producen entregables utilizables, y adelantar material real del plan (AS-IS, línea base, examen de 20 casos + 5 trampas para el control A, TO-BE, especificación técnica).

## Documentos del cliente ficticio
- [Ficha del cliente](documentos/01-ficha-del-cliente.md)
- [Notas del proceso actual](documentos/02-notas-del-proceso-actual.md)
- [Muestra de 15 siniestros](documentos/03-muestra-de-siniestros.csv)
- [Sistemas y restricciones](documentos/04-sistemas-y-restricciones.md)

## Plan (13 encargos, 12 agentes, 4 fases)
Lo define [`proyecto.py`](proyecto.py), que genera `proyecto.json` para cargarlo en la base de datos de la oficina.

| Fase | Encargo | Agente | Formato |
|---|---|---|---|
| 1 · Preparar | Claves del sector | Coordinación sectorial · Seguros | Word |
| 1 · Preparar | Mapa de obligaciones y riesgo de IA | Legal y privacidad | Word |
| 1 · Preparar | Guiones de entrevista | Validación | Word |
| 2 · Diagnosticar | AS-IS | Arquitecto de procesos | Diagrama |
| 2 · Diagnosticar | Línea base y métricas | Métricas | Excel |
| 2 · Diagnosticar | Examen 20 + 5 trampas | Datos de prueba | Excel |
| 3 · Diseñar | TO-BE (en equipo) | Arquitecto de procesos con su equipo | Diagrama |
| 3 · Diseñar | Modelo de amenazas | Seguridad | Word |
| 3 · Diseñar | Especificación técnica | Arquitecto técnico | Word |
| 3 · Diseñar | Coste por siniestro | Costes | Excel |
| 4 · Proponer | Propuesta de piloto 50/50 | Propuestas | Word |
| 4 · Proponer | Plan y RAID del piloto | Plan y seguimiento | Excel |
| 4 · Proponer | Presentación al comité | Jefe comercial | PowerPoint |

## Cómo se lanza
En la oficina: **Proyectos → Atalaya → Lanzar «1 · Preparar»**, y cuando terminen, la fase siguiente. Cada encargo lee lo ya entregado en el proyecto. Lo que pase (encargos, conversaciones, entregables y lecciones) se vuelca cada noche al repositorio en `oficina/registro/` (D-017).
