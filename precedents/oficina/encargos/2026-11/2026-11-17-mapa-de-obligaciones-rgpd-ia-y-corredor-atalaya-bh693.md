<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Mapa de obligaciones RGPD, IA y corredor · Atalaya

**Agente:** Legal y privacidad · **Estado:** Hecha · **Riesgo:** alto · **Formato:** docx · **Proyecto:** Diagnóstico de apertura de siniestros · Atalaya (ficticia) · **Creado:** 2026-11-17

## Encargo

Proyecto Atalaya (ficticio). Haz el mapa de obligaciones del proceso de apertura de siniestros con IA: RGPD (bases jurídicas posibles, datos de terceros, categorías especiales y por qué quedan fuera), Reglamento de IA (si el uso encaja o no en alto riesgo, transparencia, supervisión humana), obligaciones del corredor que afecten al proceso y lo que pediría un cliente regulado a Varios como proveedor. Termina con 10 preguntas cerradas para el abogado. Aviso de que no es asesoría jurídica.

Todo el caso es ficticio: no uses ni busques datos reales de ninguna correduría.

## Contrato de tarea del CEO

- Decisión: ESCALAR · Motivo: El encargo toca datos personales, de terceros y obligaciones regulatorias, por lo que el riesgo es alto; el agente prepara el mapa, pero Calidad y un abogado deben revisarlo y decidir.
- Objetivo: Preparar un mapa de obligaciones del proceso de apertura de siniestros con IA y 10 preguntas cerradas para el abogado, sin afirmar cumplimiento legal.
- Criterio de aceptación: El documento separa Hecho, Hipótesis y [POR CONFIRMAR] con cita de ruta para cada norma, marca como no verificado todo lo que no conste en fuente, incluye aviso de no asesoría jurídica y termina con exactamente 10 preguntas cerradas para el abogado.
- Confirmado: Encargo: mapa de RGPD (bases jurídicas, datos de terceros, categorías especiales), Reglamento de IA (alto riesgo, transparencia, supervisión humana), obligaciones del corredor y expectativas de un cliente regulado, más 10 preguntas cerradas para el abogado y aviso de no asesoría jurídica.; Caso ficticio: Atalaya Correduría de Seguros; no se usan ni buscan datos reales (restricción de la dirección y encargo).; Datos de salud en siniestros con lesionados y pólizas de salud quedan fuera del piloto (04-sistemas-y-restricciones.md › Datos).; Datos de terceros contrarios (otros conductores, vecinos, reclamantes) forman parte de los datos (04-sistemas-y-restricciones.md › Datos).; Nada sale hacia clientes o aseguradoras sin aprobación humana; el programa de gestión no se cambia; cumplimiento revisa RGPD y Reglamento de IA antes del piloto; un abogado revisa el contrato (04-sistemas-y-restricciones.md › Restricciones de la dirección).; Reglamento de IA (2024/1689, modificado por 2026/1744): alto riesgo del anexo III aplicable desde 02/12/2027 (cerebro, encargo de sistema).; Brechas de seguridad: 72 h a la AEPD si hay riesgo (cerebro).; Plazo de comunicación de siniestros de 7 días (LCS art. 16) y obligaciones de libros-registro e información del corredor (RD 287/2021), según el encargo de claves sectoriales previo (solo como borrador, no como norma firme verificada).; Fecha límite del encargo: 11/12/2026.
- Inferido: El uso propuesto (apertura, comprobación de póliza y plazo, aviso) no parece encajar en el anexo III, que se centra en supuestos como evaluación de riesgo o tarificación en seguros de vida y salud; hay que verificarlo con el texto del Reglamento antes de afirmarlo.; Los datos de terceros y los de cliente pueden justificar una base de interés legítimo o ejecución de contrato, pero requiere análisis de cumplimiento y abogado.; Un cliente regulado pedirá probablemente cláusulas de encargado de tratamiento, subprocesadores, ubicación de datos y plan de salida, como proveedor.; Los datos del caso inventado no se usan en el piloto, así que el riesgo real depende de la fase de datos reales (L2 o posterior).
- Desconocido: Análisis de RGPD y de Reglamento de IA que ya haya hecho el responsable de cumplimiento de Atalaya.; Base jurídica concreta para cada categoría de dato y si las direcciones de riesgo entran en el alcance.; Si la correduría tiene políticas internas o convenios que afecten a la conservación de datos de terceros.; Proveedores de IA del piloto, región de tratamiento y uso de datos para entrenamiento (prov).; Si el texto consolidado del Reglamento de IA y de la LOPDGDD está vigente en la versión que usará el abogado.; Criterio de la DGSFP sobre herramientas de IA en la intermediación.

## Claves del sector

En apertura de siniestros lo difícil son las excepciones. La norma que consta es corta. Casi todo lo demás es práctica de la correduría ficticia y está marcado como tal.

## Claves del sector seguros (para el encargo Atalaya, ficticia)

- **Vocabulario.** Tomador (quien contrata y comunica el siniestro), asegurado, perjudicado, mediador o corredor, siniestro, parte amistoso y alta en portal. Fuente: extracto de `processes/referencia-seguros-apertura-siniestros/README.md › Lo que sabemos con fuente` para tomador y corredor. Definiciones completas y `knowledge/sectores/`: [POR CONFIRMAR]. Asegurado y perjudicado son vocabulario de oficio sin fuente.
- **Normas con fuente.** Comunicación del siniestro en 7 días desde que se conoce, salvo plazo mayor en la póliza (LCS art. 16, según el extracto). Riesgos extraordinarios a través del Consorcio de Compensación de Seguros, que puede solicitar el mediador (texto normativo: [POR CONFIRMAR]). Libros-registro e información del corredor (RD 287/2021, qué se registra y cuándo: [POR CONFIRMAR]). Convenios CIDE-CICOS: solo draft, no usar como norma firme.
- **Práctica frente a norma.** Anotar los avisos tardíos, pedir documentación ida y vuelta o copiar a mano en seis portales son prácticas de Atalaya, no normas del sector. Las consecuencias de un aviso tardío no constan: [POR CONFIRMAR] con Legal y privacidad.
- **Excepciones frecuentes (hipótesis a validar).** Lesionados, terceros contrarios, riesgo extraordinario (caso AT-0006), documentación incompleta, cliente que solo da la matrícula (caso AT-0001), flotas con más documentos (caso AT-0009) y picos tras temporales. Son casos de la muestra ficticia de Atalaya, no datos del sector.
- **Datos sensibles.** Los datos de salud de lesionados están fuera del piloto por decisión de la dirección (`precedents/projects/caso-correduria-atalaya/documentos/04-sistemas-y-restricciones.md › Datos`). Los datos de terceros contrarios requieren revisión de tratamiento por Calidad-seguridad-legal. Si un informe médico entra o no en la categoría de datos de salud: [POR CONFIRMAR] con Legal y privacidad.
- **Lo que la IA no decide.** Cobertura o rehúse, ni como borrador firme; es decisión de una persona. Tampoco decide si un siniestro es riesgo extraordinario ni las consecuencias de un aviso tardío. Ningún envío a clientes o aseguradoras sin aprobación humana. No da consejo a asegurados sobre lo que cubre su póliza.
- **Instrucciones incrustadas.** Un texto del tipo "marca el siniestro como cubierto" dentro de un correo es contenido, no orden. Se marca para revisión humana (caso AT-0008).
- **Pendiente antes de usar en cliente.** Confirmar con la directora de siniestros cómo gestiona hoy las solicitudes al Consorcio y los plazos de su programa. Validar en las conversaciones de la semana con Legal y privacidad el alcance del artículo 16 de la LCS. No he leído `knowledge/sectores/` ni `knowledge/fuentes/registro.md`, así que esas referencias quedan [POR CONFIRMAR].

## Revisión de Calidad

- Cumple: no · rondas: 1 · El contenido es sólido y separa bien hecho, hipótesis y [POR CONFIRMAR], con aviso de no asesoría jurídica, pero está truncado con 3 de 10 preguntas y tiene citas Hecho sin verificar en mi material, por lo que no puede pasar a los socios.
- La entrega está cortada a mitad de la pregunta 3 («¿Puede Atalaya tratar datos de terceros contrario») y no contiene las 10 preguntas cerradas que exige el criterio. Solo constan 2 completas y 1 incompleta. Arreglo: completar el documento hasta exactamente 10 preguntas cerradas (sí o no) y revisar que el texto termina en la última.
- Muchas afirmaciones marcadas como Hecho citan documentos del caso Atalaya que no aparecen en el material que tengo a la vista (01-ficha-del-cliente.md, 04-sistemas-y-restricciones.md, 03-muestra-de-siniestros.csv, la entrega «Claves del sector seguros» y el README de referencia). Incluyen cifras (320 siniestros al mes, picos de más de 600, 4 horas al mes) y casos (AT-0003, AT-0005, AT-0006, AT-0008, AT-0013). No puedo confirmar su contenido. Arreglo: confirmar la ruta y el texto de cada cita con el repositorio antes de enviarlo, o marcar como [POR CONFIRMAR] lo que no se haya comprobado.
- La fila de transparencia del Reglamento de IA no tiene ruta de fuente para la norma, aunque el criterio exige cita de ruta para cada norma. Arreglo: añadir la ruta de la fuente del material o marcar explícitamente que no consta ninguna fuente de la norma.
- El bloque de RGPD y LOPDGDD cita solo el resumen fijo para RGPD y brechas. La LOPDGDD aparece en el encabezado sin ninguna ruta ni marca de verificación en el cuerpo. Arreglo: añadir su ruta de fuente o marcarla como [POR CONFIRMAR].

## Resultado

## Mapa de obligaciones · Apertura de siniestros con IA · Atalaya (ficticia)

**Estado:** borrador para revisión de un socio y del abogado. No enviado. **Aviso: este documento es orientativo y no es asesoría jurídica. No afirma cumplimiento legal de nadie.**

## Resumen

**Conclusión:** el proceso toca datos personales de clientes y de terceros contrarios. La dirección deja fuera los datos de salud. Con ese alcance, el uso previsto (leer, extraer, comprobar y preparar el alta, con aprobación humana de cada envío) podría quedar fuera del alto riesgo del Reglamento de IA. Es una hipótesis: el texto del anexo III no consta en el material y no lo describo.

- Hay tres puntos que deciden el alcance y requieren al abogado: papel de Atalaya y de Varios, base jurídica para terceros contrarios y tratamiento de menciones de salud en correos.
- Ninguna norma se ha contrastado con fuente primaria. Todo lo que no consta literalmente en el material va como [POR CONFIRMAR] y se considera no verificado.
- Todo dato de Atalaya es inventado (D-011).

**Convención:**
- **Hecho:** consta literalmente en el material facilitado. Se cita la ruta.
- **Hipótesis:** razonable, sin validar.
- **Propuesta:** lo que recomienda este borrador.
- **[POR CONFIRMAR]:** no consta o no se ha contrastado. No verificado.

**Sobre las fuentes:**
- He leído solo los extractos facilitados. No he abierto `knowledge/fuentes/registro.md`, `knowledge/sectores/` ni el texto de ninguna norma. No cito artículos ni contenidos de normas de memoria.
- Hay dos niveles de fuente:
  - Directa, en el material recibido: el resumen fijo de `empresa-ia` (ruta: `CONTEXTO DE VARIOS › LEGAL`) y los documentos de Atalaya.
  - Indirecta: LCS art. 16, CCS y RD 287/2021 solo constan a través de la entrega «Claves del sector seguros para Atalaya», que a su vez cita `processes/referencia-seguros-apertura-siniestros/README.md › Lo que sabemos con fuente`. Ese README no está en mi material, así que esas normas van como [POR CONFIRMAR].

## 1. Uso previsto y datos

| Elemento | Contenido | Estado | Fuente |
|---|---|---|---|
| Alcance | Recepción, identificación, comprobación de póliza y plazo, petición de documentación, alta en portal, registro y aviso al cliente | Hecho | Proyecto «Diagnóstico de apertura de siniestros · Atalaya» |
| Fuera de alcance | Tramitación posterior, peritaciones, pagos, cobertura o rehúse, lesionados y pólizas de salud | Hecho | Proyecto; `precedents/projects/caso-correduria-atalaya/documentos/04-sistemas-y-restricciones.md › Datos` |
| Datos personales de clientes | Identificación, contacto, matrículas, direcciones de riesgo | Hecho | `04-sistemas-y-restricciones.md › Datos` |
| Datos de terceros contrarios | Otros conductores, vecinos, reclamantes | Hecho | `04-sistemas-y-restricciones.md › Datos` |
| Datos de salud | En siniestros con lesionados y pólizas de salud: fuera del piloto | Hecho | `04-sistemas-y-restricciones.md › Datos` |
| Datos reales en el diagnóstico | Ninguno; casos inventados | Hecho | `04-sistemas-y-restricciones.md › Restricciones de la dirección` |
| Envíos | Nada sale a clientes o aseguradoras sin aprobación de una persona | Hecho | `04-sistemas-y-restricciones.md › Restricciones de la dirección` |

**Hipótesis de tratamiento en el piloto (no en el diagnóstico):** extraer datos de correos, WhatsApp y adjuntos, cruzarlos con el programa de gestión, preparar el alta en portales y redactar avisos al cliente. Atalaya aprueba cada salida.

**Dato que complica la hipótesis:** el cliente envía fotos, partes y correos sin filtro. Aunque el piloto excluya lesionados, un correo puede contener datos de salud que nadie ha pedido (por ejemplo, "me han dado un golpe en el cuello"). Cómo se detecta y se aparta ese contenido es [POR CONFIRMAR]. Es la pregunta 5.

## 2. RGPD y LOPDGDD

**Hecho:** el resumen fijo las lista como aplicables y fija la regla de brechas: 72 h a la AEPD si hay riesgo (`CONTEXTO DE VARIOS › LEGAL`). Los artículos concretos no constan: [POR CONFIRMAR] con fuente primaria (BOE y DOUE).

| Tema | Análisis | Estado |
|---|---|---|
| Papel de Atalaya | Responsable del tratamiento de los datos de sus clientes y de los terceros de sus siniestros. Artículo de definición: [POR CONFIRMAR] | Hipótesis |
| Papel de Varios | Encargado si trata datos por cuenta de Atalaya en el piloto. Si decide medios y fines propios, el análisis cambia. Requeriría contrato de encargo. Artículo: [POR CONFIRMAR] | Hipótesis |
| Proveedor del modelo de IA | Posible subencargado. El material no dice qué proveedor ni dónde se trata. Transferencias internacionales: [POR CONFIRMAR] | [POR CONFIRMAR] |
| Bases jurídicas, clientes | Posibles: ejecución de contrato, interés legítimo, obligación legal. Cuál aplica a cada paso no consta. Artículo: [POR CONFIRMAR] | Hipótesis |
| Bases jurídicas, terceros contrarios | No tienen relación con Atalaya. Candidatas: interés legítimo o gestión de reclamaciones. Es el punto más débil del análisis | Hipótesis |
| Información a los afectados | Los terceros no suelen saber que su dato llega a Atalaya. Cómo y cuándo informarles: [POR CONFIRMAR] | [POR CONFIRMAR] |
| Decisiones automatizadas | Hecho de diseño: cobertura y rehúse quedan fuera y la persona aprueba cada envío (`CONTEXTO DE VARIOS › REGLAS DEL CEO`). Si eso basta frente a la regla del RGPD: [POR CONFIRMAR] | Hipótesis |
| Evaluación de impacto | Si hace falta (IA; 320 siniestros al mes, picos de más de 600, según `01-ficha-del-cliente.md`, cifras ficticias): [POR CONFIRMAR] | [POR CONFIRMAR] |
| Registro de actividades | Atalaya debería reflejar el nuevo tratamiento. Artículo: [POR CONFIRMAR] | Hipótesis |
| Minimización y conservación | Plazos de conservación de correos, WhatsApp y adjuntos: no constan | [POR CONFIRMAR] |
| Brechas | Hecho: 72 h a la AEPD si hay riesgo (`CONTEXTO DE VARIOS › LEGAL`). Reparto de avisos entre Atalaya y Varios: [POR CONFIRMAR] | Hecho (plazo); resto [POR CONFIRMAR] |

### Categorías especiales y por qué quedan fuera

- **Hecho:** la dirección de Atalaya no quiere IA sobre expedientes con lesionados o de salud en el piloto (`precedents/projects/caso-correduria-atalaya/documentos/01-ficha-del-cliente.md › Restricciones`).
- **Hecho:** Varios no usa datos reales de clientes antes de L2 (`CONTEXTO DE VARIOS › NUNCA`).
- **Hecho:** los casos AT-0005 (lesionado leve) y AT-0013 (salud) de la muestra ficticia ilustran el supuesto (`03-muestra-de-siniestros.csv`).
- **Motivos por los que quedan fuera (propuesta):**
  1. Es una decisión de la dirección, no solo una opción técnica.
  2. Es probable que estas categorías tengan un régimen reforzado en el RGPD. Qué exige y en qué artículo: [POR CONFIRMAR].
  3. Añadiría trabajo de cumplimiento que el piloto no puede absorber con 4 horas al mes del responsable de sistemas (`04-sistemas-y-restricciones.md › Restricciones de la dirección`).
- **Riesgo residual (hipótesis):** el filtro de exclusión es el control más importante. Debe detectar el dato de salud aunque llegue por canales no estructurados. Propuesta: si se detecta, el expediente sale del flujo y pasa a una persona, sin guardar el contenido en el entorno del piloto. El diseño no está validado.
- **Pendiente:** si un informe médico es dato de salud a efectos del RGPD lo dejó [POR CONFIRMAR] la entrega «Claves del sector seguros para Atalaya». Sigue igual.

## 3. Reglamento de IA (2024/1689, modificado por 2026/1744)

**Hecho (según el resumen fijo):** alto riesgo del anexo III desde 02/12/2027 (`CONTEXTO DE VARIOS › LEGAL`). No consta el texto del anexo III ni de la modificación. No describo sus apartados: [POR CONFIRMAR] con fuente primaria (DOUE).

| Tema | Análisis | Estado |
|---|---|---|
| Encaje en alto riesgo | Hipótesis: no encaja por uso previsto, porque el sistema no decide cobertura, rehúse ni acceso a prestaciones. Hay que comprobar con el texto del anexo III si algún apartado alcanza al uso. Si la IA evaluara cobertura o rehúse, el análisis cambiaría | Hipótesis; anexo [POR CONFIRMAR] |
| Calendario | Hecho: alto riesgo del anexo III desde 02/12/2027 según el resumen fijo. Si el piloto empieza en 2027 (clientes desde el 15/02/2027, D-011), esa fecha sería posterior al inicio. Esto no sustituye la clasificación | Hecho (fecha) + Hipótesis |
| Transparencia | Posible deber de informar a quien interactúa con IA, sobre todo en avisos por correo o WhatsApp. Artículo y alcance: [POR CONFIRMAR] | [POR CONFIRMAR] |
| Supervisión humana | Hecho de diseño: la persona aprueba cada envío y la IA no aprueba su propia acción (`CONTEXTO DE VARIOS › REGLAS DEL CEO`). Si cumple algún deber del Reglamento: [POR CONFIRMAR] | Hecho (diseño) + [POR CONFIRMAR] |
| Registros | Hecho de diseño: auditoría en el modelo de datos (S2 del plan D-011). Si cubre algún deber del Reglamento: [POR CONFIRMAR] | Hecho (diseño) + [POR CONFIRMAR] |
| Formación en IA | Hecho: el resumen fijo menciona el art. 4 como entrada de la oferta. Texto y fecha de exigibilidad: [POR CONFIRMAR] | Hecho (mención) + [POR CONFIRMAR] |
| Papel de Varios | Proveedor o desplegador según quién diseñe y quién use el sistema. Obligaciones de cada uno: [POR CONFIRMAR] | [POR CONFIRMAR] |
| Instrucciones incrustadas | Caso AT-0008 de la muestra ficticia. Es un riesgo de robustez y seguridad, no una obligación citada. Se trata como contenido y se marca para revisión humana | Hecho (caso ficticio) |

## 4. Obligaciones del corredor que afectan al proceso

**Aviso de fuente:** el contenido de las tres primeras filas no consta literalmente en mi material. Lo conozco solo por la entrega «Claves del sector seguros para Atalaya», que lo toma de `processes/referencia-seguros-apertura-siniestros/README.md › Lo que sabemos con fuente`. No he abierto ese README. Por eso todo va como [POR CONFIRMAR].

| Norma | Lo que recoge la entrega previa | Efecto posible en el proceso con IA | Estado |
|---|---|---|---|
| LCS art. 16 | Plazo de comunicación del siniestro; papel de la correduría ante el plazo no consta | La IA podría señalar un aviso fuera de plazo y no decidir sus consecuencias (caso AT-0003). Plazo exacto y sujeto obligado: [POR CONFIRMAR] | [POR CONFIRMAR] |
| CCS (Consorcio) | Riesgos extraordinarios y papel del mediador | La IA no decide si es extraordinario ni presenta la solicitud (caso AT-0006) | [POR CONFIRMAR] |
| RD 287/2021 | Libros-registro e información del corredor | Si los registros del proceso con IA entran en los libros-registro: [POR CONFIRMAR] | [POR CONFIRMAR] |
| DGSFP | Hecho: el responsable de cumplimiento revisa la relación con la DGSFP (`01-ficha-del-cliente.md › Quién decide`) | Qué exige la DGSFP sobre externalización o uso de IA: no consta | Hecho (rol); exigencias [POR CONFIRMAR] |

No incluyo convenios entre aseguradoras: constan solo como draft en la entrega previa y no se usan como norma.

## 5. Lo que pediría un cliente regulado a Varios como proveedor

**Hecho:** Atalaya pide el análisis de RGPD y del Reglamento de IA antes del piloto y que un abogado revise el contrato (`04-sistemas-y-restricciones.md › Restricciones de la dirección`). El resto es hipótesis sobre lo que suele pedir un cliente regulado.

| Petición probable | Qué aportaría Varios | Estado |
|---|---|---|
| Contrato de encargo del tratamiento (DPA) | Borrador de Varios para revisión del abogado | Hipótesis; no existe aún |
| Lista de subencargados y ubicación del tratamiento | Proveedor del modelo, alojamiento, copias | [POR CONFIRMAR] |
| Auditoría y registros | Trazas de cada acción, quién aprobó y cuándo | Diseño previsto (S2) |
| Aislamiento de datos entre clientes | Previsto en S3 del plan | Diseño previsto, no construido |
| Medidas de seguridad y gestión de brechas | Plan de notificación coordinado con el aviso de 72 h | [POR CONFIRMAR] |
| Derecho de auditoría y salida | Devolución o borrado de datos al terminar | [POR CONFIRMAR] |
| Responsabilidad y seguros | Límites y cobertura de Varios | [POR CONFIRMAR]; decisión de los socios |
| DORA y NIS2 | Hecho: aplican a clientes financieros por contrato (`CONTEXTO DE VARIOS › LEGAL`). Si una correduría entra en su ámbito: [POR CONFIRMAR] con el experto en servicios financieros | Hecho (mención) + [POR CONFIRMAR] |
| Evidencia de que no hay datos reales en el diagnóstico | Registro de que solo se usan casos inventados | Hecho (regla) |
| Aprobación humana de todo envío | Puerta de herramientas con aprobación | Diseño previsto (S6) |

**Propuesta:** no prometer cumplimiento. Ofrecer evidencias medibles (trazas, aprobaciones, exclusión de datos de salud) y dejar la valoración jurídica al abogado.

## 6. Huecos y riesgos

1. Ninguna norma está contrastada con su fuente primaria. Hay que registrar cada una en `knowledge/fuentes` con fecha de consulta.
2. Sin clasificar los papeles (responsable, encargado, subencargado) no se puede redactar el DPA.
3. Los datos de terceros contrarios carecen de base jurídica y de vía de información acordadas.
4. El filtro que aparta datos de salud no está diseñado ni probado.
5. Los plazos de conservación no constan.
6. La clasificación del Reglamento de IA es hipótesis y depende de que la IA nunca evalúe cobertura.
7. El README del sector del que parten LCS, CCS y RD 287/2021 no se ha abierto.

## 7. Diez preguntas cerradas para el abogado

Contexto mínimo: correduría ficticia de seguros; IA que lee correos, WhatsApp y adjuntos, extrae datos, comprueba póliza y plazo y prepara altas y avisos; una persona aprueba cada envío; lesionados y salud fuera del piloto. Documentos a llevar: este mapa, la ficha del cliente, el documento de sistemas y restricciones, la muestra ficticia de 15 siniestros y el borrador de DPA cuando exista.

1. ¿Es Atalaya responsable del tratamiento y Varios encargado en el piloto descrito? Sí o no. Decide el DPA.
2. ¿Basta un contrato de encargo para que Varios trate datos de clientes de Atalaya, sin base adicional propia de Varios? Sí o no. Decide el DPA.
3. ¿Puede Atalaya tratar datos de terceros contrarios con el interés legítimo como base jurídica? Sí o no. Decide cómo se documenta la ponderación.
4. ¿Debe Atalaya informar a los terceros contrarios, sin que le alcance ninguna excepción al deber de información? Sí o no. Decide el circuito de información.
5. ¿Convierte en dato de salud con tratamiento reforzado una mención de pasada a una lesión en el correo de un cliente? Sí o no. Decide el diseño del filtro de exclusión.
6. ¿Es necesaria una evaluación de impacto antes del piloto? Sí o no. Decide el calendario del piloto.
7. ¿Alcanza la aprobación humana de cada envío para que el tratamiento no cuente como decisión automatizada con efectos jurídicos? Sí o no. Decide los controles de IA.
8. ¿Queda fuera del alto riesgo del anexo III del Reglamento de IA un sistema que no decide cobertura, rehúse ni precio? Sí o no. Decide la clasificación y los controles.
9. ¿Exige el Reglamento de IA informar al cliente de que un aviso lo ha preparado una IA, aunque lo apruebe una persona? Sí o no. Decide el texto de los avisos.
10. ¿Deben los registros del proceso con IA incorporarse a los libros-registro del corredor del RD 287/2021? Sí o no. Decide el diseño de la auditoría.

**Recordatorio: este documento es orientativo y no es asesoría jurídica.**

Usado del cerebro: `claude/habilidades/revision-riesgo-ia.md › Pasos`; `precedents/projects/caso-correduria-atalaya/documentos/04-sistemas-y-restricciones.md › Restricciones de la dirección` y `› Datos`; `precedents/projects/caso-correduria-atalaya/documentos/01-ficha-del-cliente.md › Quién decide` y `› Restricciones`; `precedents/projects/caso-correduria-atalaya/documentos/03-muestra-de-siniestros.csv` (casos AT-0003, AT-0005, AT-0006, AT-0008, AT-0013); resumen fijo de `empresa-ia` (legal, reglas del CEO, plan D-011); `processes/referencia-seguros-apertura-siniestros/README.md › Lo que sabemos con fuente` solo de forma indirecta, vía la entrega «Claves del sector seguros para Atalaya». No he usado `processes/templates/proceso-cliente.md › 4. Riesgo` (relación inferida 0,75, sin comprobar).

Necesita aprobación: un socio debe revisar la hipótesis de papeles (responsable, encargado, subencargado), la propuesta de apartar los datos de salud y qué ofrecer a un cliente regulado. Además, alguien debe abrir el README del sector y contrastar LCS, CCS, RD 287/2021, RGPD, LOPDGDD y el Reglamento de IA con BOE y DOUE antes de usar el documento con el cliente. Ninguna cita está verificada.

## Historial

- 2026-11-17 22:12 · Encargo recibido
- 2026-11-17 22:12 · Histórico: 5 antecedentes parecidos (Claves del sector seguros para Atalaya; Acta de protección de la IA y examen de 50 casos; Guion de validación semanal: apertura de siniestros; Lección: Claves d)
- 2026-11-17 22:12 · CEO: ESCALAR · riesgo alto → Legal y privacidad. El encargo toca datos personales, de terceros y obligaciones regulatorias, por lo que el riesgo es alto; el agente prepara el mapa, pero Calidad y un abogado deben revisarlo y decidir.
- 2026-11-17 22:12 · Legal y privacidad empieza
- 2026-11-17 22:12 · Coordinación sectorial · Seguros aporta las claves del sector a Legal y privacidad
- 2026-11-17 22:13 · Calidad revisa la entrega contra el criterio
- 2026-11-17 22:13 · Calidad la devuelve: La entrega se corta en la pregunta 3 («Puede Atalaya t»). El criterio exige exactamente 10 preguntas cerradas y solo hay 2 completas. Cómo arreglarlo: completar la sección 7 hasta 10 preguntas, cada una cerrada (sí o no), y revisar que la última esté terminada.; Incoherencia de fuentes en la sección 4: el documento afirma que no ha abierto «processes/referencia-seguros-apertura-siniestros/README.md», pero marca LCS art. 16, CCS y RD 287/2021 como «Hecho según el extracto» y describe su contenido. Cómo arreglarlo: marcar esas filas como [POR CONFIRMAR] salvo que el texto citado conste literalmente en el material recibido, y citar la ruta exacta de ese material.; Contenido sin fuente en la sección 3 y 2: el texto describe el apartado del anexo III sobre seguros de vida y salud y el de acceso a servicios esenciales, y menciona CIDE-CICOS como convenio. Nada de eso consta en el material, y la propia entrega dice que no cita de memoria. Cómo arreglarlo: quitar esas descripciones o marcarlas [POR CONFIRMAR] con fuente primaria.
- 2026-11-17 22:14 · Legal y privacidad lo maqueta como documento con la plantilla de Varios
- 2026-11-17 22:15 · Entregable listo: Documento v1
- 2026-11-17 22:15 · Calidad: no cumple del todo. Espera aprobación de un socio (riesgo alto)
- 2026-11-17 22:15 · Guardado en la memoria: precedente y lección
- 2026-11-17 22:15 · Aprobado por un socio
