# Integraciones

**Estado:** no hay ningún conector construido (D-011: solo datos inventados hasta el 12/02/2027).

| Carpeta | Contenido |
|---|---|
| [`catalog/`](catalog/README.md) | Conectores que necesitaremos y software libre evaluado |
| [`contracts/`](contracts/README.md) | Contratos de datos (JSON Schema) entre piezas |
| [`connectors/`](connectors/README.md) | Código de conectores (vacío) |
| [`tests/`](tests/README.md) | Pruebas de contrato y de conector |

Reglas (P31, P32, P33):
- Cada conector se registra con dueño, permisos mínimos, credencial en el gestor de secretos, versión de la API y prueba de contrato.
- Toda escritura externa lleva clave de idempotencia y aprobación humana según la política.
