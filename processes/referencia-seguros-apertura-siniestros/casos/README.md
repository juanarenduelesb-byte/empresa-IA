# Casos de prueba: 20 siniestros inventados (C1)

**Todo inventado (D-011).** Ninguna persona, póliza, aseguradora ni hecho es real. Son hipótesis hasta validarlos con tramitadores: sirven para probar las reglas, no para afirmar cómo trabaja una correduría.

| Archivo | Qué es |
|---|---|
| `casos.json` | 20 siniestros: mensaje tal como llega, hechos que un extractor perfecto sacaría, resultado esperado y por qué. |
| `cartera.json` | 11 pólizas inventadas de dos aseguradoras ficticias. |
| `esquema.json` | Esquema JSON de un caso, generado desde el modelo Pydantic con `python -m varios.seguros.esquema`. |

## Cómo se usa
- `src/varios/seguros/apertura.py` aplica con código fijo el [catálogo de excepciones](../../../knowledge/sectores/seguros/excepciones.md). Plazos, listas y umbrales salen de [`dominio.json`](../../../knowledge/sectores/seguros/dominio.json).
- El ramo lo da la póliza de la cartera, no el mensaje. Las incoherencias que se pueden comprobar con código (ocurrencia posterior a la recepción, conocimiento anterior a la ocurrencia, ramo del mensaje distinto del de la póliza) saltan como EX-09 aunque la IA no las vea.
- `tests/test_casos_siniestros.py` comprueba:
  - que los 20 casos cumplen el esquema;
  - que cada excepción EX-01 a EX-15 tiene al menos un caso;
  - que hay casos limpios y salen las cuatro acciones;
  - que las reglas dan exactamente lo esperado;
  - que el plazo se lee del dominio, no del código;
  - que las incoherencias comprobables y el ramo de la póliza no dependen de la IA.
- Más adelante (S6–S9), la IA leerá `mensaje` y se medirá cuánto se parecen sus hechos a `hechos`. Esa será la parte del examen de 50 casos que mide la extracción.

## Cobertura
| Acción esperada | Casos |
|---|---|
| Preparar el parte (el envío lo aprueba una persona) | S01, S02, S03, S06, S07, S10 |
| Pedir documentación | S16 |
| Trasladar a la aseguradora | S09 |
| Pasar a una persona | S04, S05, S08, S11, S12, S13, S14, S15, S17, S18, S19, S20 |

Casos sin ninguna excepción: S01 y S03. Casos con varias a la vez: S12, S13 y S20.

## En la base de datos (A5)

La semilla (`python -m varios.db.semilla`) carga estos casos inventados en PostgreSQL, repartidos entre los dos clientes de ejemplo, y `--vaciar` los quita. Reparto, riesgo y pruebas: [docs/24, «Datos de ejemplo»](../../../docs/24-base-de-datos.md#datos-de-ejemplo-a5). Si cambias los casos, la prueba `tests/db/test_semilla.py` comprueba que la base sigue coincidiendo.
