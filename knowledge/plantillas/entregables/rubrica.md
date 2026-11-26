---
tipo: "plantilla"
id: "rubrica-entregables"
estado: "draft"
---
# Rúbrica de calidad de entregables y listas de comprobación (C3)

**Estado:** draft. Desarrolla la regla de D-019 (`docs/18-flujo-de-calidad-y-aprendizaje.md`) para los entregables al cliente. Es una rúbrica analítica: cada criterio tiene un descriptor concreto por nivel, para que dos revisores puntúen igual ([CMU-RUBRICAS](../../fuentes/registro.md#cmu-rubricas)). La versión máquina está en `rubrica.json` y `listas-comprobacion.json`, y la decisión de si cumple la toma el código (`src/varios/calidad/rubrica.py`), no el revisor.

## Cuándo cumple
- **Todos** los criterios con al menos **4**.
- Media de al menos **4,5**.
- **Ningún** problema grave ni medio abierto.
- **Todos** los puntos de la lista común y de la lista de su tipo cumplidos.

Aunque cumpla, lo aprueba un socio antes de enviarlo.

## Bloqueantes (son siempre problema grave)
- Cifra, cliente, fuente o norma inventada.
- Datos personales de terceros en el cuerpo.
- Afirmar cumplimiento legal sin revisión competente.
- Enviar o proponer enviar algo sin aprobación de un socio.
- Una decisión que solo puede tomar una persona presentada como tomada por la IA.

## Criterios
| Criterio | Pregunta | 1 · Inaceptable | 2 · Insuficiente | 4 · Bien | 5 · Excelente |
|---|---|---|---|---|---|
| **Criterio** | ¿Responde a lo que se pidió y a la decisión que el cliente tiene que tomar? | No responde al encargo o no pide ninguna decisión | Responde a medias; la decisión pedida es vaga | Responde al encargo y pide una decisión concreta, con quién y cuándo | Además, la recomendación está razonada y se ven las alternativas |
| **Completo** | ¿Están todos los apartados de la plantilla y nada importante falta? | Faltan apartados de la estructura común | Están los apartados pero alguno vacío sin decir por qué | Todos los apartados con contenido; lo que falta está marcado [por medir] con cómo se medirá | Además, anexos y fuentes permiten a otro reproducirlo |
| **Veracidad** | ¿Cada afirmación es cierta y dice de dónde sale? | Hay cifras, clientes, fuentes o normas inventadas | Hay afirmaciones sin fuente o fuentes sin fecha | Cada cifra tiene base (medido, declarado o hipótesis) y cada norma su fuente vigente | Además, se contrastó con una segunda fuente lo importante |
| **Coherencia** | ¿Cuadra consigo mismo y con lo ya entregado o decidido? | Contradice decisiones registradas o entregables aprobados | Pequeñas contradicciones internas (cifras o nombres que no cuadran) | Sin contradicciones; las cifras coinciden en todo el documento | Además, se citan las versiones anteriores que cambia |
| **Nivel** | ¿Lo firmaría un profesional senior del sector? | Genérico; podría ser de cualquier empresa | Correcto pero superficial; no usa el vocabulario del sector | Concreto para este cliente y proceso, con el vocabulario del sector | Además, anticipa objeciones y riesgos que el cliente no había visto |
| **Forma** | ¿Se lee rápido y sin errores? | Errores de ortografía, formato roto o datos personales en el cuerpo | Frases largas, jerga o formato irregular | Claro, con la respuesta primero, sin errores y con la plantilla de marca | Además, una persona ocupada entiende la decisión leyendo solo el resumen |

El 3 («aceptable con cambios») queda entre el 2 y el 4.

## Lista común (todos los entregables)
- [ ] **C01** Cabecera completa: versión, fecha, autor y revisor por rol, estado, clasificación y datos usados (inventados o reales, con su nivel L0–L4).
- [ ] **C02** El resumen cabe en cinco líneas y dice qué decisión se pide, a quién y para cuándo.
- [ ] **C03** Cada cifra tiene base (medido, declarado o hipótesis) y origen; lo no medido va como [por medir].
- [ ] **C04** Cada norma citada tiene fuente vigente del registro y, si es legal, «no es asesoría jurídica».
- [ ] **C05** Sin datos personales de terceros: personas por rol.
- [ ] **C06** Hechos, hipótesis y propuestas separados.
- [ ] **C07** Siguientes pasos con quién (rol) y cuándo.
- [ ] **C08** Nada se envía sin el OK de un socio (acción externa).

## Propuesta de diagnóstico (`propuesta-diagnostico`, plantilla [01-propuesta-diagnostico.md](01-propuesta-diagnostico.md))
- [ ] **PD1** Qué entra y qué no entra, por escrito.
- [ ] **PD2** Qué necesitamos del cliente (personas, horas, acceso).
- [ ] **PD3** Precio sin IVA o hueco [precio] si aún no está decidido; nunca un precio inventado.
- [ ] **PD4** Dice que en esta fase no se usan datos reales de sus clientes.
- [ ] **PD5** Explica cómo se medirá la línea base sin sacar datos personales del cliente (añadido en N6).

## Informe de diagnóstico (`informe-diagnostico`, plantilla [02-informe-diagnostico.md](02-informe-diagnostico.md))
- [ ] **ID1** AS-IS validado por quien hace el proceso, con fecha.
- [ ] **ID2** Línea base con cómo se midió y en qué periodo.
- [ ] **ID3** Excepciones con su frecuencia observada.
- [ ] **ID4** Casos de uso puntuados con el mismo criterio para todos.
- [ ] **ID5** Riesgo según el Reglamento de IA, datos personales y DORA, marcado como orientativo.

## Diseño TO-BE (`diseno-to-be`, plantilla [03-diseno-to-be.md](03-diseno-to-be.md))
- [ ] **DT1** Cada paso dice qué es regla fija, qué propone la IA y qué decide una persona.
- [ ] **DT2** Cada excepción del catálogo tiene detector, acción y responsable.
- [ ] **DT3** Métrica con línea base, umbral, cómo se mide, periodo y quién la certifica.
- [ ] **DT4** Matriz de aprobaciones y forma de volver al proceso manual.
- [ ] **DT5** Validado con los casos de prueba inventados (por ejemplo C1).

## Plan de piloto (`plan-piloto`, plantilla [04-plan-piloto.md](04-plan-piloto.md))
- [ ] **PP1** Datos reales solo tras L2 y con el encargo del tratamiento firmado.
- [ ] **PP2** Criterios de parada y qué pasa si se activan.
- [ ] **PP3** Cómo y quién mide la métrica firmada.
- [ ] **PP4** Formación de los usuarios (Reglamento de IA, art. 4) prevista.

## Informe mensual de operación (`informe-mensual`, plantilla [05-informe-mensual-operacion.md](05-informe-mensual-operacion.md))
- [ ] **IM1** La métrica firmada frente al umbral y a la línea base.
- [ ] **IM2** Todas las incidencias del mes, con causa y prueba añadida.
- [ ] **IM3** Cambios de reglas, instrucciones o modelo con sus pruebas.
- [ ] **IM4** Coste de uso del modelo.

## Acta de reunión (`acta`, plantilla [06-acta-reunion.md](06-acta-reunion.md))
- [ ] **AC1** Decisiones tomadas separadas de las abiertas.
- [ ] **AC2** Cada tarea con quién y cuándo.
- [ ] **AC3** Plazo para confirmar el acta.

## Cómo se usa
1. El revisor lee el entregable con su plantilla al lado.
2. Puntúa los seis criterios, con un problema por cada punto menor de 5: dónde está y cómo arreglarlo.
3. Marca la lista común y la de su tipo.
4. El código decide si cumple. Si no, vuelve al autor con los problemas (hasta cuatro rondas, D-019).
