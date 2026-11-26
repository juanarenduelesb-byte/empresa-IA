# Revisión con la rúbrica C3 · Propuesta de diagnóstico de Atalaya (FICTICIA)

**Veredicto del código** (`src/varios/calidad/rubrica.py` sobre [la revisión en JSON](01-propuesta-diagnostico.revision.json)): **no cumple todavía.** Media 4,33, por debajo de 4,5. Los seis criterios están en 4 o más, no hay problemas graves ni medios y las 13 comprobaciones (C01–C08 y PD1–PD5) se cumplen. `tests/test_ejemplo_atalaya.py` vuelve a calcularlo en cada cambio.

**Quién revisa.** Claude, que también la escribió: es una revisión provisional. Según D-019 la confirma un socio, y nadie aprueba lo suyo. Fecha: 26/11/2026 (tarea N6).

## Puntos
| Criterio | Nota | Por qué |
|---|---|---|
| Criterio | 5 | Responde a lo que pidió la dirección (saber con datos dónde se va el tiempo) y pide tres decisiones con opciones, recomendación razonada, quién y cuándo |
| Completo | 4 | Todos los apartados con contenido; precio, fechas, horas y días del registro van como huecos y dicen quién los decide |
| Veracidad | 4 | Cada cifra está marcada como declarada y enlaza al documento del que sale; la única norma (LCS art. 16) tiene fuente del registro y aviso de que no es asesoría jurídica. No llega a 5: las cifras del cliente tienen una sola fuente |
| Coherencia | 4 | Las cifras coinciden con la ficha y las notas del caso, con D-011 (solo datos inventados) y con D-024 (el proceso de referencia no guarda datos de salud). Es la primera versión, no hay anteriores que citar |
| Nivel | 5 | Concreto para una correduría (portales por aseguradora, Consorcio, plazo de comunicación, lesionados) y anticipa una objeción que el cliente no había planteado: cómo medir la línea base sin sacar datos personales, cuando él mismo ha prohibido usar datos reales en el diagnóstico |
| Forma | 4 | La respuesta va primero y la decisión se entiende con el resumen, pero el resumen tiene dos huecos |

## Lo que falta para que cumpla
1. Que los socios decidan precio y fechas (precio antes del 29/01/2027, `DECISIONS.md`). Con eso, completo y forma pueden subir a 5.
2. Que un socio confirme o corrija estos puntos. Si dos revisores puntúan distinto, se calibra la rúbrica (pendiente de C3).

## Cambios hechos a la plantilla y a la rúbrica (N6)
| Dónde | Qué fallaba | Cambio |
|---|---|---|
| Plantilla, cabecera | No decía el nivel de los datos, que pide C01 | «Datos: ninguno del cliente (L0)» |
| Plantilla, §1 | «Pedimos **[nombre del rol que firma]** que apruebe»: mezcla nombre y rol y falta la preposición | «Pedimos a **[rol que firma]** que apruebe» |
| Plantilla, §2 | No separaba lo que dice el cliente de lo que nadie sabe, que pide C06 | Marcas «declarado» y línea «Lo que no se sabe» |
| Plantilla, §3 | Prometía una línea base sin decir cómo se mide sin datos personales, y la propia propuesta dice que no se usan | Línea «Cómo medimos sin datos personales» |
| Plantilla, §5 | Se llamaba «Supuestos y límites» y no marcaba hecho, hipótesis o riesgo, como manda la estructura común de E1 | «Riesgos, supuestos y límites», con cada línea marcada |
| Plantilla, §7 | No tenía fuentes, que la estructura común pone en el apartado 7 | «Condiciones, fuentes y anexos» |
| Lista de la propuesta | Nada comprobaba cómo se mide la línea base sin datos personales | Punto nuevo **PD5** |
| Lista común, C01 | «datos usados (L0–L4)» no decía qué se declara | «datos usados (inventados o reales, con su nivel L0–L4)», como el README de E1 |
| Código de la rúbrica | Un punto mal escrito o de otra lista (por ejemplo «PD9» o «ID1» en una propuesta) se ignoraba sin avisar, y un problema podía citar un criterio que no existe | Ahora es un error; prueba nueva en `tests/test_rubrica_entregables.py` |
