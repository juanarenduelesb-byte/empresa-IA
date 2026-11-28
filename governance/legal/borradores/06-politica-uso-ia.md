# Política de uso de inteligencia artificial de Varios · BORRADOR PARA ABOGADO

> **BORRADOR PARA ABOGADO. NO APROBAR NI PUBLICAR.** No es asesoría jurídica. Política **interna**: dice qué herramientas de IA usa Varios, con qué datos, quién aprueba y qué se registra. Lo que Varios promete al cliente está en el [anexo de uso de IA](04-anexo-uso-ia.md) y quién aprueba qué en la [matriz de aprobaciones](05-matriz-aprobaciones.md); esta política no los contradice y, si alguna vez lo hiciera, mandan ellos hasta que se corrija. Lo que está entre corchetes `[…]` lo deciden los socios o el abogado. Fecha: 27/11/2026 (P19).

**No se ha reinventado:** la estructura sigue la *Política general para el uso de IA generativa en procesos administrativos* de la AEPD, la primera de su tipo en el sector público español, de 27/11/2025 ([AEPD-POLITICA-IAG](../../../knowledge/fuentes/registro.md#aepd-politica-iag)): casos de uso, riesgos, gobernanza (quién decide), políticas por tema y procedimientos (alta de un caso de uso, incidentes, supervisión). Se ha simplificado para una sociedad de dos socios. La parte de alfabetización sigue las preguntas y respuestas de la Comisión sobre el art. 4 ([CE-ALFABETIZACION-QA](../../../knowledge/fuentes/registro.md#ce-alfabetizacion-qa)).

## 1. Objeto y alcance
1.1. Se aplica a todo uso de IA en el trabajo de Varios: por los socios, por cualquier persona que trabaje para Varios y por los agentes de la oficina.
1.2. Cubre dos usos: (a) **herramientas** de IA que las personas usan para trabajar (por ejemplo, un asistente de chat o de código); (b) **sistemas** que Varios construye y opera para un cliente (por ejemplo, el proceso de referencia de apertura de siniestros). Para (b), además de esta política, vale el anexo de IA del contrato con ese cliente.
1.3. Base: `CLAUDE.md` («proceso antes que agente»; código fijo para reglas y cálculos, IA para lenguaje y ambigüedad; toda acción externa, financiera, legal o contractual con aprobación humana), D-011 (solo datos inventados hasta los clientes), D-019 (todo pasa por un socio) y D-024 (el proceso de referencia no guarda datos de salud).

## 2. Principios
1. **Una persona responde de cada resultado.** La IA prepara; una persona revisa y decide. Ningún resultado de IA sale de Varios ni se usa para decidir sin que lo revise una persona competente (en la AEPD, los resultados «sean revisados y contrastados por personal competente», `AEPD-POLITICA-IAG`).
2. **Lo que la IA no decide nunca** es lo mismo que en el anexo de IA, §2: cobertura, culpa, fraude, importes o rechazos. Tampoco envía nada fuera, ni mueve dinero, ni firma.
3. **Solo herramientas del catálogo** (§3). Una herramienta que no está en el catálogo no se usa con nada de Varios.
4. **Los datos mandan sobre la herramienta.** Qué se puede meter en una herramienta depende del nivel de los datos (§4), no de lo cómoda que sea.
5. **Todo queda registrado** (§7), y lo que la IA hizo se distingue de lo que hizo una persona.

## 3. Catálogo de herramientas
Solo se usan las herramientas de esta tabla, para lo que dice su fila. Dar de alta una herramienta nueva es tecnología nueva: la justifican en `DECISIONS.md` y la aprueban **los dos socios** (matriz, §1). Hoy solo se trabaja con datos inventados (D-011, nivel L0).

| Herramienta | Para qué | Datos permitidos hoy | Estado |
|---|---|---|---|
| Claude (Anthropic), en la aplicación de Claude (también la oficina de agentes, que hoy es un artefacto de Claude) | Trabajo de los socios, trabajo nocturno sobre el repositorio y la oficina de agentes | Solo L0: documentos internos sin datos personales y datos inventados | En uso. Por la API, cuando exista el adaptador (S4). [El abogado revisa las condiciones del proveedor: uso de los datos para entrenar, conservación y región] |
| [Otras que usen hoy los socios] | [·] | [·] | [Los socios completan la lista; lo que no esté, no se usa con nada de Varios] |
| Herramientas de IA de terceros con cuenta personal o gratuita | — | Ninguno | **No autorizadas** para nada de Varios |

## 4. Qué datos se pueden usar, según el nivel
Los niveles son las puertas técnicas L0–L4 de la Guía v1.4 (`docs/08`). Pasar de nivel lo aprueban los dos socios (matriz, §1).

| Nivel | Qué datos | Con qué herramientas | Condición |
|---|---|---|---|
| L0 · datos inventados | Casos, clientes y cifras inventados, y documentos internos sin datos personales | Las del catálogo | — (hoy estamos aquí) |
| L1 · datos internos reales | Datos reales de Varios (por ejemplo, su contabilidad) | Solo las del catálogo autorizadas para L1 | Los dos socios lo aprueban; [el abogado revisa las condiciones del proveedor] |
| L2 · datos de clientes | Datos de un cliente, incluidos personales | Solo el sistema del pedido y sus subencargados listados en el anexo IV del encargo del tratamiento (`02`) | Encargo del tratamiento firmado, puerta G4 y L2 superadas (matriz, §3) |
| Nunca | Contraseñas, claves, tokens y secretos; datos de salud mientras siga D-024; datos de un cliente en la herramienta o el expediente de otro | Ninguna | — |

Como en la AEPD, en las herramientas externas que no controla Varios rige la prohibición de introducir información personal, confidencial o no publicada (`AEPD-POLITICA-IAG`) salvo que su nivel lo permita expresamente en esta tabla.

## 5. Quién aprueba
| Qué | Quién | Dónde consta |
|---|---|---|
| Dar de alta o de baja una herramienta del catálogo | Los dos socios | `DECISIONS.md` |
| Un caso de uso nuevo de IA en un proceso (qué hace la IA y qué el código) | Un socio, con su prueba en el banco de casos | La decisión y el banco de casos |
| Subir un nivel de autonomía a un proceso | Un socio, si la métrica cumple el umbral durante el periodo fijado; lo externo, legal o financiero no pasa de A2 (D-027) | `processes/autonomia.json` |
| Usar datos de un nivel superior | Los dos socios | Matriz, §1 |
| Enviar a un cliente o a un tercero algo hecho con IA | Un socio, que lo revisa antes | Auditoría de la oficina |
| Cambiar el modelo o las instrucciones de un sistema en servicio | Un socio, tras pasar el banco de casos; en procesos con techo A2 (lo externo, legal, financiero o contractual), los dos (D-030, regla 4). Se comunica al cliente (anexo de IA, §7.3) | Registro del cambio, con su versión y su nota del examen (D-030, regla 5) |

Nadie aprueba su propio trabajo y un agente nunca aprueba (matriz; `tests/test_motor.py` y `tests/db/test_api_oficina.py`).

## 6. Transparencia con las personas (art. 50 del Reglamento de IA)
6.1. Si un sistema de Varios conversa con personas (por ejemplo, un asistente que contesta al asegurado), se les informa de que hablan con una IA como muy tarde en la primera interacción, salvo que resulte evidente (art. 50.1 y 50.5; aplicable desde el 02/08/2026; [RIA-2024-1689](../../../knowledge/fuentes/registro.md#ria-2024-1689), [UE-RIA-OMNIBUS](../../../knowledge/fuentes/registro.md#ue-ria-omnibus)).
6.2. Si un texto generado con IA se publica para informar al público de asuntos de interés público, se dice que es artificial, salvo que lo haya revisado una persona con responsabilidad editorial (art. 50.4). Lo que Varios publica con su marca (web, artículos) lo revisa siempre un socio.
6.3. El cliente final de una correduría puede pedir en cualquier momento que le atienda una persona, también desde un bot (Ley 10/2025, art. 8, [LEY-10-2025](../../../knowledge/fuentes/registro.md#ley-10-2025)).
6.4. Nada de lo hecho con IA se presenta como trabajo de una persona concreta si no lo ha revisado esa persona, ni se inventan testimonios, clientes o cifras (`CLAUDE.md`).

## 7. Qué se registra
| Qué | Dónde | Base |
|---|---|---|
| Cada llamada a un modelo en un sistema de Varios: proveedor, modelo, versión de las instrucciones, tokens, coste y resultado | Tabla `ejecucion_modelo` (D-023) | Anexo de IA, §7.2 |
| Quién pidió, quién aprobó y qué versión; cada cambio de estado | Auditoría inmutable (`evento_auditoria`, D-023) | Matriz, §4 |
| Catálogo de herramientas y sus cambios | §3 de esta política y `DECISIONS.md` | — |
| Formación de cada persona (§8) | [Registro interno: fecha, contenido y persona] | `CE-ALFABETIZACION-QA` |
| Incidentes con IA (§9) | [Registro de incidentes] | RGPD art. 33 si hay brecha |

En las herramientas de chat de uso diario no se guarda cada conversación; sí el resultado que se use (en el repositorio o en la oficina) con la marca de que lo preparó la IA.

## 8. Alfabetización en IA (art. 4)
8.1. Desde el 27/07/2026, el art. 4, en la redacción del Reglamento (UE) 2026/1744, pide a proveedores y responsables del despliegue **adoptar medidas para apoyar la promoción** de la alfabetización en IA de su personal; **no exige** garantizar un nivel concreto ([RIA-ART4-ALFABETIZACION](../../../knowledge/fuentes/registro.md#ria-art4-alfabetizacion), [UE-RIA-OMNIBUS](../../../knowledge/fuentes/registro.md#ue-ria-omnibus)).
8.2. Varios es proveedor de los sistemas que construye y opera (anexo de IA, §3), así que la obligación le alcanza. Según la Comisión, un programa debe considerar al menos: que se entienda qué es la IA en la organización, el papel de la organización (proveedor o responsable del despliegue), el riesgo de los sistemas y el nivel técnico, la experiencia y la formación de cada persona. No hace falta certificado, y se puede llevar un registro interno de las formaciones (`CE-ALFABETIZACION-QA`).
8.3. Medidas: [una sesión inicial para cada persona que trabaje para Varios con esta política, el anexo de IA y los límites del §2; repaso cuando cambie el catálogo o el Reglamento]. A las personas del cliente que usan un sistema de Varios se las forma según el pedido (anexo de IA, §6).

## 9. Incidentes
9.1. Es un incidente: datos de un nivel no permitido metidos en una herramienta; un resultado de IA que sale sin revisión; una instrucción escondida en un documento que el sistema obedece; un dato de un cliente que aparece en el trabajo de otro.
9.2. Quien lo vea avisa a un socio el mismo día. Se para el uso afectado, se registra y se convierte en una regla o una prueba nueva (anexo de IA, §8.1).
9.3. Si afecta a datos personales, se valora como brecha: notificar a la autoridad de control en 72 horas si hay riesgo ([RGPD-2016-679](../../../knowledge/fuentes/registro.md#rgpd-2016-679), art. 33) y avisar al cliente responsable según el encargo del tratamiento (`02`).

## 10. Revisión
Se revisa cuando cambie el catálogo, el Reglamento de IA o la puerta L en la que trabaja Varios, y como mínimo [una vez al año]. La aprueban los dos socios tras la revisión del abogado.

## Preguntas para el abogado
1. ¿Basta esta política interna, o con clientes regulados conviene publicar un resumen (como hizo la AEPD con la suya)?
2. Condiciones del proveedor del modelo (§3): uso de los datos para entrenar, conservación, región y si se puede firmar como subencargado del anexo IV.
3. ¿Hace falta una evaluación de impacto (RGPD art. 35) antes de L2 en el proceso de referencia? La AEPD recomienda revisar las evaluaciones de impacto al incorporar agentes ([AEPD-AGENTICA](../../../knowledge/fuentes/registro.md#aepd-agentica)).
4. ¿La formación del §8 debe constar en el contrato con el cliente o basta el registro interno?
