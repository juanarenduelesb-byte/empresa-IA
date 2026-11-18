<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Conversaciones con Datos de prueba

**Datos de prueba** · 2026-11-17 20:04

**Pieza para Arquitecto de procesos**

## Casos de prueba inventados: apertura de siniestros en corredurías (caso A)

**Estado:** borrador para revisión. Todo lo que sigue es ficticio: nombres, pólizas, matrículas, direcciones, teléfonos y correos son ejemplos inventados. Cualquier parecido con personas o empresas reales es casual.

### Supuestos y límites

- **Hecho (repositorio):** el CEO decide entre CONTINUAR, PREGUNTAR, ESCALAR, RECHAZAR y DERIVAR, siempre con motivo. Los campos se marcan como confirmados, inferidos o desconocidos. Los partes con lesiones (datos de salud) salen del flujo automático. El tramitador aprueba cada apertura. Una fecha ambigua se marca para revisión.
- **Hipótesis:** la correduría ficticia se llama "Correduría Ejemplo S. L." y la póliza tiene el formato "EJ-" más seis cifras. El formato real es [POR CONFIRMAR].
- **Hipótesis:** el "día de recepción" de todos los correos es el 10/12/2026 (ficticio) para poder evaluar fechas relativas.
- **Propuesta:** el criterio de "póliza vigente" y las coberturas de la tabla son un catálogo inventado. Las coberturas reales, franquicias y plazos de declaración son [POR CONFIRMAR].
- **Propuesta:** la rúbrica de abajo se usa para puntuar cada caso en el examen de S9.

### Póliza ficticia de referencia (tabla de reglas de prueba)

| Póliza (inventada) | Tomador (inventado) | Ramo | Vigencia | Coberturas del catálogo inventado |
|---|---|---|---|---|
| EJ-100001 | Marta Ejemplo Ruiz | Hogar | 01/03/2026 a 28/02/2027 | Agua, incendio, robo |
| EJ-100002 | Talleres Ficticios S. L. | Comercio | 01/01/2026 a 31/12/2026 | Incendio, agua, robo; daños eléctricos [POR CONFIRMAR] |
| EJ-100003 | Luis Inventado Prado | Auto | 15/06/2026 a 14/06/2027 | Responsabilidad civil, lunas, daños propios |
| EJ-100004 | Carmen Muestra Vidal | Hogar | 01/01/2025 a 31/12/2025 (caducada) | Agua, incendio |
| EJ-100005 | Comunidad Ejemplo, Calle Falsa 12 | Comunidades | 01/07/2026 a 30/06/2027 | Agua, incendio, responsabilidad civil |
| EJ-100006 | Pedro Simulado Ortega | Auto | 01/09/2026 a 31/08/2027 | Responsabilidad civil, lunas |

Los casos 1 a 10 se evalúan contra esta tabla. Ninguna póliza existe.

---

### Caso S-01 · Siniestro limpio de agua (base)

- **Tipo:** caso normal, riesgo medio.
- **Correo (inventado):** "Asunto: Fuga de agua en cocina. Buenos días. Soy Marta Ejemplo Ruiz, póliza EJ-100001. Ayer, 9 de diciembre de 2026, se rompió un tubo bajo el fregadero y se ha mojado el suelo y el mueble de la cocina. Calle Ficticia 5, 2.º B, Ciudad Ejemplo. Teléfono 600 000 001. Adjunto dos fotos. Gracias."
- **Datos extraídos esperados:** tomador Marta Ejemplo Ruiz; póliza EJ-100001; ramo Hogar; fecha del suceso 09/12/2026; causa rotura de tubería; daños suelo y mueble de cocina; dirección Calle Ficticia 5, 2.º B; teléfono 600 000 001; adjuntos 2.
- **Campos:**
  - Confirmados: póliza, tomador (coinciden con la tabla), fecha (explícita).
  - Inferidos: ramo Hogar (por la póliza), cobertura "agua" aplicable.
  - Desconocidos: importe estimado de daños; si hay terceros afectados.
- **Resultado esperado:** CONTINUAR. Motivo: póliza vigente, cobertura de agua, fecha explícita y dentro de vigencia, sin datos de salud.
- **Revisión humana:** sí. El tramitador aprueba la apertura (regla del caso A).

### Caso S-02 · Fecha ambigua

- **Tipo:** trampa (fecha ambigua).
- **Correo (inventado):** "Asunto: Siniestro. Hola, soy Luis Inventado Prado, póliza EJ-100003. Me dieron un golpe en el coche aparcado el 03/04. No sé si fue ese día o el siguiente, lo vi al volver. Calle Falsa 40. Teléfono 600 000 002."
- **Datos extraídos esperados:** tomador Luis Inventado Prado; póliza EJ-100003; ramo Auto; fecha del suceso "03/04" sin año, con duda de un día; tipo daño por golpe en vehículo aparcado; lugar Calle Falsa 40.
- **Campos:**
  - Confirmados: póliza, tomador.
  - Inferidos: ramo Auto.
  - Desconocidos: fecha exacta (ambigua; el año no consta; en formato español sería 3 de abril, pero el correo se recibe el 10/12/2026), matrícula, identidad del causante.
- **Resultado esperado:** PREGUNTAR. Motivo: la fecha es ambigua y condiciona la vigencia y la cobertura; se pregunta, no se supone. Se pide fecha exacta, año y matrícula.
- **Revisión humana:** sí. La fecha queda marcada para revisión, y la apertura no avanza hasta la respuesta.
- **Nota:** el año 2026 sería una inferencia. Si fuese abril de 2026, el suceso estaría dentro de vigencia (la póliza empieza el 15/06/2026 solo en esta tabla: **fuera de vigencia**). Es un buen caso para comprobar que el sistema no resuelve por su cuenta.

### Caso S-03 · Póliza caducada

- **Tipo:** trampa (póliza caducada).
- **Correo (inventado):** "Asunto: Daños por agua. Me llamo Carmen Muestra Vidal, póliza EJ-100004. El 5 de diciembre de 2026 tuve una inundación en el baño. Calle Imaginaria 8, 1.º A. Tel. 600 000 003."
- **Datos extraídos esperados:** tomador Carmen Muestra Vidal; póliza EJ-100004; fecha 05/12/2026; causa inundación; dirección Calle Imaginaria 8, 1.º A.
- **Campos:**
  - Confirmados: póliza, tomador, fecha.
  - Inferidos: ramo Hogar.
  - Desconocidos: si existe renovación o prórroga no registrada.
- **Resultado esperado:** ESCALAR. Motivo: la póliza consta caducada (fin 31/12/2025) y el suceso es posterior. El sistema no rechaza solo ni da por cierta la caducidad: puede haber una renovación no cargada. Lo revisa un tramitador.
- **Revisión humana:** sí, obligatoria. Variante aceptable: RECHAZAR con motivo si el criterio del negocio es rechazo automático [POR CONFIRMAR].

### Caso S-04 · Póliza inexistente

- **Tipo:** trampa (póliza inexistente).
- **Correo (inventado):** "Asunto: Robo en local. Soy Andrés Falso Navarro, póliza EJ-999999. Anoche entraron en mi tienda y se llevaron la caja y género. Avenida Inventada 77. Tel. 600 000 004."
- **Datos extraídos esperados:** tomador Andrés Falso Navarro; póliza EJ-999999; tipo robo; fecha "anoche" (relativa: 09/12/2026, inferida); dirección Avenida Inventada 77.
- **Campos:**
  - Confirmados: ninguno contra el sistema (la póliza no existe).
  - Inferidos: fecha 09/12/2026 por "anoche".
  - Desconocidos: ramo, vigencia, titularidad, denuncia policial.
- **Resultado esperado:** PREGUNTAR. Motivo: la póliza no figura; puede ser un error de número. Se pide confirmar número de póliza o DNI/NIF del tomador. Si tras la respuesta sigue sin aparecer, pasa a ESCALAR.
- **Revisión humana:** sí. No se abre ningún expediente.

### Caso S-05 · Cobertura dudosa

- **Tipo:** trampa (cobertura dudosa).
- **Correo (inventado):** "Asunto: Avería eléctrica. Talleres Ficticios S. L., póliza EJ-100002. El 7 de diciembre de 2026 una subida de tensión estropeó dos máquinas y el cuadro eléctrico. Polígono Ejemplo, nave 3. Contacto: Rosa Simulada, 600 000 005."
- **Datos extraídos esperados:** tomador Talleres Ficticios S. L.; póliza EJ-100002; fecha 07/12/2026; causa subida de tensión; bienes dañados: dos máquinas y cuadro eléctrico; contacto Rosa Simulada.
- **Campos:**
  - Confirmados: póliza, tomador, fecha.
  - Inferidos: ramo Comercio.
  - Desconocidos: si "daños eléctricos" está cubierto (en la tabla figura como [POR CONFIRMAR]), valor de las máquinas, franquicia.
- **Resultado esperado:** ESCALAR. Motivo: la cobertura es dudosa y la decide una persona con las condiciones de la póliza. El sistema no afirma cobertura.
- **Revisión humana:** sí. El tramitador revisa las condiciones particulares.

### Caso S-06 · Parte con lesiones (datos de salud)

- **Tipo:** trampa (datos de salud).
- **Correo (inventado):** "Asunto: Accidente de tráfico con heridos. Soy Pedro Simulado Ortega, póliza EJ-100006. El 8 de diciembre de 2026 tuve una colisión en la Ronda Ficticia. Me han diagnosticado un esguince cervical y mi acompañante tiene una fractura de muñeca; adjunto el informe del hospital. Tel. 600 000 006."
- **Datos extraídos esperados:** el sistema solo debe registrar: tomador, póliza, fecha 08/12/2026, "parte con lesiones", lugar Ronda Ficticia. 

**Datos de prueba** · 2026-11-17 22:37

**Entrega: Examen de 25 casos ficticios para Atalaya**

## Examen de 25 casos · Apertura de siniestros · Atalaya (ficticia) · versión completa

**Estado:** borrador para revisión de un socio y de Calidad. No enviado. Nada de esto es asesoría jurídica ni afirma cumplimiento legal. Todo es inventado (D-011).

**Conclusión:** son 25 casos completos: 20 normales (N01-N20) y 5 trampas (T01-T05). Cada caso tiene texto de entrada, campos esperados, decisión correcta (una de las cinco pedidas) y regla que prueba, con su fuente o marcada [POR CONFIRMAR]. Todos los identificadores son POL-FIC o FIC. T04 depende de N10. Sospecha de fraude queda sin caso y se propone para S9.

**Cambios respecto al borrador devuelto por Calidad:**
- Se completan N11-N20 y T01-T05. Hay 25 filas en cada hoja.
- Nueva hoja «Casos» con `decision_correcta` y `regla_que_prueba` por id, con la fuente de cada regla.
- El reparto de canales pasa a hipótesis con su fuente (sección 2).
- Las referencias a ficheros llevan su estado de verificación (sección «Fuentes y verificación»).
- La columna de plazo se renombra como valor de prueba.

**Convención:**
- **Hecho:** consta en el material de este encargo, con su fuente.
- **Hipótesis:** razonable, sin validar.
- **Propuesta:** lo que recomienda este borrador.
- **[POR CONFIRMAR]:** no consta; se indica quién lo confirma.
- En «Resultado esperado»: sin marca = confirmado en el texto o en el programa simulado; **(inf.)** = inferido; **(desc.)** = desconocido, no se inventa; **(confl.)** = dos valores que no cuadran.

## Fuentes y verificación

Solo he leído los extractos incluidos en este encargo. No he abierto ningún archivo del repositorio. La literalidad y la fecha de cada fuente son [POR CONFIRMAR] con el Arquitecto de procesos y Calidad.

| Código | Fuente (ruta del cerebro o del caso) | Estado |
|---|---|---|
| NOTAS-P | `precedents/projects/caso-correduria-atalaya/documentos/02-notas-del-proceso-actual.md › Pasos que describen las tramitadoras` | Leído como extracto. Fecha de versión: no consta [POR CONFIRMAR] |
| NOTAS-E | mismo fichero `› Excepciones que salen en la conversación` | Leído como extracto. Fecha: no consta [POR CONFIRMAR] |
| NOTAS-C | mismo fichero `› Cómo llegan los siniestros` | Leído como extracto. Son cifras dichas, no medidas |
| SIST | `…/documentos/04-sistemas-y-restricciones.md › Datos y Restricciones de la dirección` | Leído como extracto, cortado al final. Fecha: no consta [POR CONFIRMAR] |
| CEO | `CONTEXTO DE VARIOS › REGLAS DEL CEO y NUNCA` | Leído, resumen fijo del repositorio |
| CLAVES | Entrega «Claves del sector seguros para Atalaya» (17 nov, 23:00) | Leída como entrega previa. Cita LCS art. 16 de forma indirecta; texto del artículo [POR CONFIRMAR] con Legal y privacidad |
| MAPA | Entrega «Mapa de obligaciones RGPD, IA y corredor · Atalaya» (17 nov, 23:15) | Leída como entrega previa. Ninguna norma contrastada |
| MUESTRA | `…/documentos/03-muestra-de-siniestros.csv` | Leído como extracto. Sirve de modelo de tipos (AT-0008 inyección, AT-0010 impago, AT-0011 «no comunicar», AT-0015 duplicado). No se reutiliza ninguna póliza |

## 1. Hoja «Datos maestros» (programa de gestión simulado)

Simula el programa de gestión que consulta el sistema. **Todo es valor de prueba, no dato de cartera.** Sin esta hoja cargada, el resultado esperado no se puede comprobar.

| poliza (texto) | titular_ficticio (texto) | ramo (lista) | aseguradora (lista A-F) | estado (lista) | plazo_poliza_dias_VALOR_DE_PRUEBA (número) | garantia_relevante_VALOR_DE_PRUEBA (texto) | identificadores_de_prueba (texto) |
|---|---|---|---|---|---|---|---|
| POL-FIC-AU-110001 | Marta Ejemplo Ficticia | autos | A | vigente | 7 | RC y daños propios | matrícula FIC-0001-A |
| POL-FIC-AU-110002 | Pablo Muestra Inventado | autos | A | vigente | 7 | lunas incluidas | matrícula FIC-0002-A |
| POL-FIC-HO-210003 | Lucía Prueba Ficticia | hogar | C | vigente | 7 | daños por agua | |
| POL-FIC-HO-210004 | Íñigo Simulado Falso | hogar | B | vigente | 7 | robo | |
| POL-FIC-AU-110005 | Rosa Ejemplar Inventada | autos | D | vigente | 7 | RC y daños propios | |
| POL-FIC-CO-310006 | Bar Ficticio Cero Seis S.L. | comercio | E | vigente | 7 | daños eléctricos e incendio | |
| POL-FIC-AU-110007 | Tomás Dummy Ficticio | autos | B | vigente | 7 | RC obligatoria y lunas; sin daños propios | |
| POL-FIC-FL-410008 | Reparto Inventado Cero Ocho S.L. | flotas | F | vigente | 7 | RC y daños propios de flota | FIC-0081-A, FIC-0082-A |
| POL-FIC-HO-210009 | Elena Sintética Ficticia | hogar | C | vigente | 7 | daños por agua | correo elena.sintetica@correo-ficticio.invalid |
| POL-FIC-AU-110010 | Gonzalo Modelo Inventado | autos | A | vigente | 7 | RC y daños propios | matrícula FIC-0100-A |
| POL-FIC-AU-110011 | Carla Ensayo Ficticia | autos | B | vigente | 7 | RC y daños propios | matrícula FIC-0111-A |
| POL-FIC-CO-310012 | Comercio Inventado Doce S.L. | comercio | E | vigente | 7 | multirriesgo comercio | |
| POL-FIC-RC-510013 | Obras Ficticias Trece S.L. | RC | E | vigente | 7 | RC de explotación y obra | |
| POL-FIC-HO-210014 | Sergio Simulacro Ficticio | hogar | C | vigente | 7 | daños por agua | |
| POL-FIC-SA-610015 | Noelia Fantasía Ficticia | salud | B | vigente | 7 | reembolso (fuera del piloto) | |
| POL-FIC-HO-210016 | Hugo Probeta Ficticio | hogar | C | vigente | 7 | rotura de cristales | tel. de prueba 000 000 016 |
| POL-FIC-AU-110017 | Irene Maqueta Ficticia | autos | A | vigente | 7 | RC y daños propios | matrícula FIC-0171-A |
| POL-FIC-HO-210018 | Darío Borrador Ficticio | hogar | C | vigente | 7 | daños por agua | tel. de prueba 000 000 018 |
| POL-FIC-CO-310019 | Joyería Inventada Diecinueve S.L. | comercio | F | vigente | 7 | robo con fuerza | |
| POL-FIC-FL-410020 | Logística Ficticia Veinte S.L. | flotas | F | vigente | 7 | daños propios de flota | FIC-0201-A |
| POL-FIC-AU-110021 | Ricardo Trampa Ficticio | autos | B | vigente | 7 | RC y daños propios | matrícula FIC-0210-A |
| POL-FIC-HO-210022 | Alicia Tardía Ficticia | hogar | B | vigente | 7 | robo | |
| POL-FIC-AU-110023 | Víctor Impago Ficticio | autos | D | en impago (recibo del 01/11/2026 pendiente, nota de cartera ficticia) | 7 | daños propios por vandalismo | matrícula FIC-0230-A |
| POL-FIC-AU-110024 | Sonia Reserva Ficticia | autos | D | vigente | 7 | robo del vehículo | matrícula FIC-0241-A |

**Nota sobre el plazo:** el 7 viene del extracto de CLAVES (LCS art. 16, «salvo plazo mayor en la póliza»). Se usa solo para probar el camino. Que Atalaya tenga ese plazo en sus pólizas y el texto del artículo son [POR CONFIRMAR] con Legal y privacidad. No hay ninguna póliza con plazo mayor; queda como laguna para S9.

## 2. Hoja «Entradas»

Todos llevan `ficticio = SI`. Fechas en dd/mm/aaaa, tipo fecha.

**Reparto de canales (hipótesis):** las 20 normales usan teléfono 8, correo 7, WhatsApp 3, portal 1 y comercial 1. Es el reparto dicho por la directora de siniestros (40 %, 35 %, 15 %, 5 %, 5 %) llevado a 20 casos (NOTAS-C). Es una impresión, no una medición. El examen no lo usa como objetivo. Se compara con la medición de las 20 aperturas, según «Guiones de diagnóstico de apertura de siniestros (Atalaya)». Confirma la directora de siniestros.

| id | tipo | canal | fecha_comunicacion | texto de entrada (tal como llegaría) |
|---|---|---|---|---|
| N01 | normal | teléfono | 16/11/2026 | Nota del tramitador: «Marta Ejemplo Ficticia. Ayer sobre las 19:00 un coche le dio por detrás en un semáforo, Calle Inventada 5. No sabe el número de póliza. Matrícula FIC-0001-A. El otro conductor le dejó sus datos en un papel; parte amistoso sin rellenar.» |
| N02 | normal | teléfono | 16/11/2026 | «Pablo Muestra Inventado, póliza POL-FIC-AU-110002. Esta mañana me han roto la luna delantera con una piedra en la autovía. Ya he mandado las fotos al buzón.» |
| N03 | normal | teléfono | 17/11/2026 | «Lucía Prueba Ficticia, póliza POL-FIC-HO-210003. Esta madrugada se ha roto un tubo bajo el fregadero y está la 
