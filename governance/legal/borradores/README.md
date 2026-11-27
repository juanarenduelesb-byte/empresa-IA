# Borradores legales para abogado (D1)

> **BORRADORES PARA ABOGADO. NO FIRMAR NI ENVIAR.** No son asesoría jurídica. Sirven para que el abogado parta de algo concreto y para que los socios vean qué decisiones hay que tomar. Cada cláusula que sale de una norma lleva su fuente del [registro](../../../knowledge/fuentes/registro.md). Lo que está entre corchetes `[…]` lo deciden los socios o el abogado. Cualquier contrato con un cliente es una acción legal y contractual: la aprueba un socio (`CLAUDE.md`).

| Documento | Para qué | Base |
|---|---|---|
| [01 · Contrato marco de servicios](01-contrato-marco-servicios.md) | Relación general con el cliente; cada fase (diagnóstico, diseño, piloto, operación) se contrata con un pedido | Código Civil, Ley 3/2004, DORA art. 30 si el cliente es una aseguradora sujeta |
| [02 · Encargo del tratamiento](02-encargo-tratamiento.md) | Varios trata datos personales por cuenta del cliente | RGPD art. 28 y cláusulas tipo de la Comisión (Decisión 2021/915) |
| [03 · Acuerdo de confidencialidad](03-acuerdo-confidencialidad.md) | Antes del diagnóstico, en ambos sentidos | Ley 1/2019 de Secretos Empresariales |
| [04 · Anexo de uso de IA](04-anexo-uso-ia.md) | Qué hace la IA, qué no decide nunca, quién es proveedor y quién responsable del despliegue | Reglamento (UE) 2024/1689 modificado por 2026/1744 |
| [05 · Matriz de aprobaciones](05-matriz-aprobaciones.md) | Quién aprueba qué, en Varios y en el cliente | `CLAUDE.md`, puertas G0–G6 y L0–L4, Ley 10/2025 |
| [06 · Política de uso de IA](06-politica-uso-ia.md) | Política **interna** (P19): qué herramientas de IA se usan, con qué datos según el nivel L0–L2, quién aprueba, transparencia, alfabetización y qué se registra | Reglamento de IA art. 4 y 50, RGPD art. 33; estructura de la política interna de la AEPD (27/11/2025) |

## Cómo se han hecho
- **No se ha reinventado nada:** el encargo del tratamiento sigue la estructura de las cláusulas contractuales tipo de la Comisión ([CCT-ENCARGO-2021-915](../../../knowledge/fuentes/registro.md#cct-encargo-2021-915)), que son de uso voluntario y ya contienen todo lo del art. 28.3. Las directrices de la AEPD ([AEPD-DIRECTRICES-ENCARGO](../../../knowledge/fuentes/registro.md#aepd-directrices-encargo)) son de 2017, anteriores a esas cláusulas.
- Lo que depende del cliente se marca: una correduría pyme **no** está sujeta a DORA, pero una aseguradora mediana sujeta a Solvencia II **sí** ([DORA-2022-2554](../../../knowledge/fuentes/registro.md#dora-2022-2554), art. 2.3).
- Datos inventados en todos los ejemplos. Ninguna cifra económica: precios, topes y penalizaciones son decisiones pendientes (precio antes del 29/01/2027).

## Preguntas para el abogado
1. ¿Usamos las cláusulas tipo de la Comisión tal cual (sin modificarlas, para que valgan como tales) o un contrato de encargo propio?
2. Tope de responsabilidad: ¿qué es razonable y asegurable para una consultora de dos socios? ¿Hace falta un seguro de RC profesional antes del primer cliente? (Ver la pregunta M-003 sobre la forma jurídica.)
3. Datos de salud en partes con daños personales: ¿qué base del art. 9.2 RGPD tiene la correduría y qué papel tiene Varios? (Pregunta 4 de la lista de la noche.)
4. Propiedad de lo que Varios construye para el cliente frente a lo que Varios reutiliza (motor, plantillas, conocimiento común).
5. Si el cliente es una aseguradora sujeta a DORA, ¿el piloto de apertura de siniestros sustenta una «función esencial o importante»? Cambia el contenido mínimo del contrato (art. 30.3).
6. Ley aplicable, jurisdicción o arbitraje.
7. Las cuatro preguntas propias de la política de uso de IA, al final del documento 06 (resumen público, condiciones del proveedor del modelo, evaluación de impacto antes de L2 y formación en el contrato).
