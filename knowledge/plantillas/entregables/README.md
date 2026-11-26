---
tipo: "plantilla"
id: "entregables"
estado: "draft"
---
# Plantillas de entregables al cliente (E1)

Seis plantillas con **la misma estructura**, para que el cliente sepa siempre dónde mirar y para que la rúbrica de calidad (C3) se aplique igual a todas. La oficina las genera en `.docx`, `.pptx` o `.xlsx` con la plantilla de marca (D-015). Estos Markdown son el contenido y el orden, no el diseño.

| Plantilla | Fase y puerta | Decisión que pide al cliente |
|---|---|---|
| [Propuesta de diagnóstico](01-propuesta-diagnostico.md) | Venta · G0 | Empezar el diagnóstico |
| [Informe de diagnóstico](02-informe-diagnostico.md) | Diagnosticar · G1–G2 | Qué proceso pasa a diseño |
| [Diseño TO-BE](03-diseno-to-be.md) | Diseñar · G2 | Aprobar el diseño y firmar la métrica |
| [Plan de piloto](04-plan-piloto.md) | Construir · G3–G4 | Arrancar el piloto con datos reales |
| [Informe mensual de operación](05-informe-mensual-operacion.md) | Operar · G5–G6 | Seguir, ajustar o ampliar |
| [Acta de reunión](06-acta-reunion.md) | Todas | Confirmar acuerdos y tareas |

## Estructura común
Basada en el principio de la pirámide: **primero la respuesta**, y después lo que la sostiene ([MINTO-PIRAMIDE](../../fuentes/registro.md#minto-piramide)).

0. **Cabecera.** Cliente, proyecto, fase y puerta, versión, fecha, autor (rol), revisado por (rol), estado (borrador o aprobado), clasificación (confidencial) y datos usados (inventados o reales, con su nivel L0–L4).
1. **Resumen en cinco líneas.** Qué hemos encontrado o propuesto, qué recomendamos y **qué decisión pedimos**, a quién y para cuándo.
2. **Contexto.** Situación, qué ha cambiado o qué duele y qué pregunta responde este documento.
3. **Contenido propio** del entregable.
4. **Decisiones que se piden.** Tabla con la decisión, las opciones, nuestra recomendación, quién decide y la fecha.
5. **Riesgos, supuestos y límites.** Cada afirmación marcada como **hecho** (con su fuente o medición), **hipótesis** o **propuesta**. Lo que la IA no decide.
6. **Siguientes pasos.** Qué, quién (rol) y cuándo.
7. **Fuentes y anexos.** Fuentes del registro, documentos del cliente consultados y versión de cada uno.

## Reglas para todas
- Nada de cifras sin origen. Si no se ha medido, se pone `[por medir]` y se dice cómo se medirá.
- Sin datos personales en el cuerpo. Las personas se nombran por rol.
- Toda afirmación legal es orientativa y lleva «no es asesoría jurídica».
- Antes de enviar: [rúbrica de calidad y lista de comprobación](rubrica.md) (C3) y aprobación de un socio, porque enviar es una acción externa.
