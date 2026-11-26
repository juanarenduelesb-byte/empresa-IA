---
tipo: "paquete-sectorial"
id: "paquete-seguros"
departamento: "sectores"
estado: "draft"
tags:
  - "area/sectores"
  - "sector/seguros"
---
# Paquete de dominio · seguros y corredurías

**Estado:** draft · **Fuentes leídas:** 26/11/2026 · **Revisión:** pendiente de un socio y, en lo legal, de un abogado.

> **Borrador para abogado.** Esto es conocimiento de trabajo para diseñar el proceso de referencia (apertura de siniestros en corredurías, D-011). No es asesoría jurídica ni se entrega a un cliente sin revisión. Cada afirmación lleva su fuente del [registro](../../fuentes/registro.md); lo que no tiene fuente está marcado como **hipótesis**.

## Qué contiene

| Archivo | Para qué |
|---|---|
| [normas.md](normas.md) | Las normas que tocan la apertura de un siniestro, con artículo, plazo y fuente oficial. |
| [glosario-siniestros.md](glosario-siniestros.md) | Vocabulario de siniestros para que agentes, pruebas y socios hablen igual. |
| [excepciones.md](excepciones.md) | Catálogo de excepciones: cuándo el caso sale del camino normal, qué hace la regla y quién decide. |
| [dominio.json](dominio.json) | Lo mismo en formato máquina (plazos, excepciones, términos) para el motor y para los casos de prueba de C1. Lo valida `tests/test_dominio_seguros.py`. |

## Cómo se usa
- El **código fijo** aplica los plazos y los disparadores de excepción de `dominio.json`. La IA solo extrae datos del mensaje y redacta; no decide cobertura, culpa, fraude ni importes ([INT-ATLAS](../../fuentes/registro.md#int-atlas)).
- Toda excepción termina en una persona. Las acciones externas (enviar el parte, escribir al cliente, pedir al CCS) necesitan aprobación humana ([INT-DEC](../../fuentes/registro.md#int-dec)).
- Antes de usar un dato con un cliente real: abrir la fuente oficial y comprobar que sigue vigente. Las fuentes en estado `draft` tienen una sola lectura.

## Lo que cambia esta noche respecto a lo que teníamos
- La Ley de Contrato de Seguro se cita ya por el texto consolidado del BOE (última modificación 03/10/2026), no por el PDF original de 1980 ([LCS-50-1980](../../fuentes/registro.md#lcs-50-1980)).
- La ficha del RDL 3/2020 apuntaba a una resolución de 2024 sobre importes. Ahora apunta al propio real decreto-ley, y la resolución tiene ficha aparte ([RDL-3-2020](../../fuentes/registro.md#rdl-3-2020), [DGSFP-IMPORTES-2024](../../fuentes/registro.md#dgsfp-importes-2024)).
- El RD 287/2021 regula los libros-registro en los art. 14–16, no en los 17–20 como decía la ficha anterior ([RD-287-2021](../../fuentes/registro.md#rd-287-2021)).
- Los convenios CIDE y ASCIDE están refundidos desde abril de 2026 en un único convenio de indemnización directa de UNESPA ([UNESPA-CONVENIO-2026](../../fuentes/registro.md#unespa-convenio-2026)).
- El plazo de dos meses para resolver reclamaciones (Orden ECO/734/2004, art. 10) está derogado: ahora es un mes ([LEY-10-2025](../../fuentes/registro.md#ley-10-2025)).

## Lo que falta
- Leer en el BOE el texto consolidado del RDL 3/2020, de la Ley 35/2015 y de la Ley 5/2025 (esta noche solo se pudieron leer copias y resúmenes).
- Confirmar si el SDM de 2014 sigue vigente y desde cuándo rige el convenio de 2026.
- Abogado: base jurídica para que una correduría trate datos de salud de un parte con daños personales (ver [normas.md](normas.md#datos-de-salud)).
- Validar el catálogo de excepciones con tramitadores de corredurías en las conversaciones semanales (D-011).
