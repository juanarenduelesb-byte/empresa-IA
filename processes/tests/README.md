# Plan de pruebas de procesos

## Automatizadas hoy (`python3 -m pytest`)
| Prueba | Qué comprueba | Procesos |
|---|---|---|
| `tests/test_estados.py` | Las transiciones del motor coinciden con `encargo.json`; los estados finales no tienen salida salvo REABIERTO | P01–P11 |
| `tests/test_motor.py` | Transición inválida rechazada; auditoría completa; nadie se aprueba a sí mismo; aprobación de otra versión rechazada; QA directo solo con riesgo bajo | P09, P10, P35 |
| `tests/test_reintentos.py` | Solo se reintentan los transitorios; la espera crece; la idempotencia evita duplicados | P22 |
| `tests/test_definiciones.py` | Las definiciones son válidas, los procesos existen y las tareas humanas o con aprobación están marcadas | P34 |
| `tests/test_repositorio.py` | Las 38 fichas tienen 20 apartados; los enlaces internos existen; lo generado está al día; las fuentes citadas existen | Todos |

## Pendientes, con su semana del plan
- **Aislamiento entre clientes con PostgreSQL y RLS** (S3): pruebas negativas.
- **Inyección de instrucciones** en documentos y correos (S6 y S9).
- **Examen de 50 casos inventados del proceso de referencia** (S9). El umbral está pendiente de decidir.
- **Restauración de copias** (S11).
- **Reinicio sin perder ni duplicar tareas** (S5, con persistencia en PostgreSQL).
