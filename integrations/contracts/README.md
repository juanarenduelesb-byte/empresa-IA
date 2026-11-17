# Contratos de datos

| Contrato | Uso |
|---|---|
| [`encargo.schema.json`](encargo.schema.json) | Lo que recibe P01 y devuelve P02 (contrato del CEO) |
| [`evento-auditoria.schema.json`](evento-auditoria.schema.json) | Evento inmutable de auditoría (P15) |

Se validan en `tests/test_repositorio.py` (son JSON válidos y con los campos obligatorios). Cuando entre Pydantic (S1), estos esquemas se generarán desde los modelos y no a mano.
