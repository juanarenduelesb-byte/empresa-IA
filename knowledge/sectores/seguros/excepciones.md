---
tipo: "paquete-sectorial"
id: "seguros-excepciones"
departamento: "sectores"
estado: "draft"
tags:
  - "sector/seguros"
---
# Catálogo de excepciones al abrir un siniestro

**Estado:** draft · **Borrador para abogado y para validar con tramitadores.** Una excepción es cualquier caso que saca el siniestro del camino normal. El código fijo detecta el disparador; la IA solo ayuda a detectarlo en el texto; **siempre decide una persona** (de la correduría o de la aseguradora). Base: *con fuente* (la regla sale de la norma citada) o *hipótesis* (práctica por validar). La versión máquina está en [dominio.json](dominio.json) y las dos deben coincidir (lo comprueba `tests/test_dominio_seguros.py`).

## Resumen
| Id | Excepción | Decide | Base |
|---|---|---|---|
| EX-01 | Comunicación fuera de plazo | aseguradora; la correduría informa | con fuente |
| EX-02 | Póliza no encontrada, no vigente o con recibo impagado | persona | hipótesis |
| EX-03 | Riesgo extraordinario (posible vía CCS) | persona | con fuente |
| EX-04 | Daños personales | persona | con fuente |
| EX-05 | Colisión de dos vehículos con daños materiales | aseguradora | con fuente |
| EX-06 | Tercero perjudicado que reclama | aseguradora | con fuente |
| EX-07 | Queja o reclamación dentro del mensaje | persona | con fuente |
| EX-08 | El cliente pide hablar con una persona | persona | con fuente |
| EX-09 | Indicios de fraude o datos incoherentes | persona | con fuente |
| EX-10 | Cerca de la prescripción | persona | hipótesis |
| EX-11 | Varias pólizas o aseguradoras para el mismo daño | persona | hipótesis |
| EX-12 | Dinero que pasa por la correduría | persona | con fuente |
| EX-13 | Faltan datos mínimos | persona | con fuente |
| EX-14 | Hay reclamación judicial, administrativa o atestado | persona | con fuente |
| EX-15 | Persona vulnerable, menor o fallecimiento | persona | hipótesis |

## EX-01 · Comunicación fuera de plazo
- **Disparador:** dias_desde_conocimiento > plazo_poliza (7 si la póliza no fija otro).
- **Regla:** Abrir igual, registrar la fecha de conocimiento y avisar. Nunca rechazar por el plazo.
- **IA:** Extrae la fecha de conocimiento del mensaje si aparece.
- **Decide:** aseguradora; la correduría informa.
- **Base:** con fuente · [LCS-50-1980](../../fuentes/registro.md#lcs-50-1980)

## EX-02 · Póliza no encontrada, no vigente o con recibo impagado
- **Disparador:** hay número de póliza pero no casa con la cartera, la fecha de ocurrencia cae fuera de la vigencia o el recibo está pendiente.
- **Regla:** No abrir parte en el portal; pasar a un tramitador. Las consecuencias del impago (LCS art. 15) no se han leído esta noche.
- **IA:** Propone la póliza más probable con su confianza; no la elige.
- **Decide:** persona.
- **Base:** hipótesis · [LCS-50-1980](../../fuentes/registro.md#lcs-50-1980)

## EX-03 · Riesgo extraordinario (posible vía CCS)
- **Disparador:** causa declarada en la lista del RD 300/2004 art. 1.1.
- **Regla:** Marcar como posible CCS, comprobar la carencia y preparar la solicitud; presentarla es una acción externa.
- **IA:** Clasifica la causa declarada; no decide la vía.
- **Decide:** persona.
- **Base:** con fuente · [RD-300-2004](../../fuentes/registro.md#rd-300-2004), [RDLEG-7-2004-CCS](../../fuentes/registro.md#rdleg-7-2004-ccs), [CCS-SOLICITUD](../../fuentes/registro.md#ccs-solicitud), [CCS-FAQ](../../fuentes/registro.md#ccs-faq)

## EX-04 · Daños personales
- **Disparador:** el mensaje menciona lesiones, heridos, fallecimiento o asistencia sanitaria.
- **Regla:** Registrar solo que hay daños personales; no guardar diagnósticos ni partes médicos hasta que el abogado fije la base del art. 9.2 RGPD.
- **IA:** Detecta la mención y la oculta del texto guardado.
- **Decide:** persona.
- **Base:** con fuente · [RGPD-2016-679](../../fuentes/registro.md#rgpd-2016-679), [LOSSEAR-ART99](../../fuentes/registro.md#lossear-art99), [AEPD-CORREDOR-2018](../../fuentes/registro.md#aepd-corredor-2018)

## EX-05 · Colisión de dos vehículos con daños materiales
- **Disparador:** ramo automóviles, dos o más vehículos y solo daños materiales: con dos vehículos y colisión directa, posible convenio; si no, posible SDM.
- **Regla:** Pedir la declaración amistosa si existe; marcar posible convenio de indemnización directa. Si hay más de dos vehículos o no hubo colisión directa, marcar posible SDM.
- **IA:** Extrae vehículos, matrículas y si hay declaración amistosa.
- **Decide:** aseguradora.
- **Base:** con fuente · [UNESPA-CONVENIO-2026](../../fuentes/registro.md#unespa-convenio-2026), [UNESPA-SDM](../../fuentes/registro.md#unespa-sdm)

## EX-06 · Tercero perjudicado que reclama
- **Disparador:** el mensaje viene de un tercero o el asegurado es responsable del daño a otro.
- **Regla:** Trasladar a la aseguradora: el perjudicado tiene acción directa (LCS art. 76) y en automóviles corre el plazo de oferta motivada.
- **IA:** Identifica quién escribe y en calidad de qué.
- **Decide:** aseguradora.
- **Base:** con fuente · [LCS-50-1980](../../fuentes/registro.md#lcs-50-1980), [RDLEG-8-2004](../../fuentes/registro.md#rdleg-8-2004)

## EX-07 · Queja o reclamación dentro del mensaje
- **Disparador:** el cliente expresa una queja sobre la correduría o la aseguradora.
- **Regla:** Separarla del siniestro y abrirla en el servicio de atención al cliente: un mes para resolver; no por teléfono.
- **IA:** Detecta el tono de queja y la separa.
- **Decide:** persona.
- **Base:** con fuente · [LEY-10-2025](../../fuentes/registro.md#ley-10-2025), [RDL-3-2020](../../fuentes/registro.md#rdl-3-2020)

## EX-08 · El cliente pide hablar con una persona
- **Disparador:** petición expresa de atención personal en cualquier momento.
- **Regla:** Pasar a una persona sin más preguntas; no cortar la comunicación por tiempo de espera.
- **IA:** Detecta la petición; no la discute.
- **Decide:** persona.
- **Base:** con fuente · [LEY-10-2025](../../fuentes/registro.md#ley-10-2025)

## EX-09 · Indicios de fraude o datos incoherentes
- **Disparador:** fechas imposibles, contradicciones entre documentos o con el historial.
- **Regla:** No acusar ni rechazar; marcar para revisión. La pérdida de la indemnización exige dolo o culpa grave, y eso no lo decide una máquina.
- **IA:** Señala la incoherencia concreta, sin calificarla.
- **Decide:** persona.
- **Base:** con fuente · [LCS-50-1980](../../fuentes/registro.md#lcs-50-1980), [INT-ATLAS](../../fuentes/registro.md#int-atlas)

## EX-10 · Cerca de la prescripción
- **Disparador:** han pasado más de 18 meses (daños) o 54 meses (personas) desde el siniestro.
- **Regla:** Avisar a una persona. El umbral de aviso es una propuesta, no una norma.
- **IA:** —
- **Decide:** persona.
- **Base:** hipótesis · [LCS-50-1980](../../fuentes/registro.md#lcs-50-1980)

## EX-11 · Varias pólizas o aseguradoras para el mismo daño
- **Disparador:** el cliente tiene más de una póliza que podría cubrir el siniestro.
- **Regla:** Pasar a un tramitador. La concurrencia de seguros (LCS art. 32) no se ha leído esta noche.
- **IA:** Lista las pólizas candidatas.
- **Decide:** persona.
- **Base:** hipótesis · [LCS-50-1980](../../fuentes/registro.md#lcs-50-1980)

## EX-12 · Dinero que pasa por la correduría
- **Disparador:** hay que cobrar o pagar algo por cuenta del cliente.
- **Regla:** Solo por cuentas de clientes separadas; cualquier movimiento necesita aprobación humana.
- **IA:** —
- **Decide:** persona.
- **Base:** con fuente · [RDL-3-2020](../../fuentes/registro.md#rdl-3-2020), [INT-DEC](../../fuentes/registro.md#int-dec)

## EX-13 · Faltan datos mínimos
- **Disparador:** falta alguno de: número de póliza, fecha de ocurrencia, descripción, contacto.
- **Regla:** Preparar la petición de documentación; enviarla es una acción externa que aprueba una persona.
- **IA:** Redacta la petición con la lista de lo que falta.
- **Decide:** persona.
- **Base:** con fuente · [RD-287-2021](../../fuentes/registro.md#rd-287-2021), [INT-DEC](../../fuentes/registro.md#int-dec)

## EX-14 · Hay reclamación judicial, administrativa o atestado
- **Disparador:** el mensaje menciona denuncia, atestado, juicio, abogado o reclamación ante un organismo.
- **Regla:** Anotarlo en el libro de siniestros (art. 15 c) y pasar a una persona.
- **IA:** Detecta la mención.
- **Decide:** persona.
- **Base:** con fuente · [RD-287-2021](../../fuentes/registro.md#rd-287-2021)

## EX-15 · Persona vulnerable, menor o fallecimiento
- **Disparador:** el mensaje menciona un menor, un fallecido o una situación de especial vulnerabilidad.
- **Regla:** Pasar a una persona con prioridad; trato y documentación especiales por validar con el sector.
- **IA:** Detecta la mención.
- **Decide:** persona.
- **Base:** hipótesis · [INT-ATLAS](../../fuentes/registro.md#int-atlas)

## Campos mínimos del expediente
Salen del libro de siniestros del RD 287/2021, art. 15 c), más la fecha en que el asegurado conoció el siniestro (LCS art. 16):

- `numero_siniestro_correduria`: numeración correlativa por series ([RD-287-2021](../../fuentes/registro.md#rd-287-2021)).
- `poliza`: datos de la póliza ([RD-287-2021](../../fuentes/registro.md#rd-287-2021)).
- `fecha_ocurrencia`: fecha de ocurrencia ([RD-287-2021](../../fuentes/registro.md#rd-287-2021)).
- `fecha_conocimiento_asegurado`: cómputo de los 7 días ([LCS-50-1980](../../fuentes/registro.md#lcs-50-1980)).
- `fecha_declaracion`: fecha de declaración ([RD-287-2021](../../fuentes/registro.md#rd-287-2021)).
- `fecha_liquidacion`: fecha de liquidación ([RD-287-2021](../../fuentes/registro.md#rd-287-2021)).
- `reclamacion`: si hay reclamación judicial, administrativa, ante el defensor u otra ([RD-287-2021](../../fuentes/registro.md#rd-287-2021)).
