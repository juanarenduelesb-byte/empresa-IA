<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Conversaciones con Legal y privacidad

**Legal y privacidad** · 2026-11-17 22:15

**Entrega: Mapa de obligaciones RGPD, IA y corredor · Atalaya**

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
| Encaje en alto riesgo | Hipótesis: no encaja por uso previsto, porque el sistema no decide cobertura, rehúse ni acceso a prestaciones. Hay que comprobar con el texto del anexo III si algún apartado alcanza al uso. Si l
