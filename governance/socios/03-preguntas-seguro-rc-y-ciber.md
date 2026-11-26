---
tipo: "decision-socios"
id: "socios-seguro"
estado: "draft"
decision: "M-020"
---
# M-020 · Preguntas para el corredor: responsabilidad civil profesional y ciberriesgos

**Estado:** borrador para Álvaro, que lleva la conversación con el corredor. **No elige seguro ni aseguradora.** Preparado en la tarea S1 (26/11/2026). Objetivo del plan maestro: presupuestos comparados y seguro contratado antes del primer piloto.

## Conclusión
Lo que más importa preguntar no es el precio, sino **lo que queda fuera**. En el condicionado de responsabilidad civil para empresas de tecnología que se ha leído como ejemplo ([HISCOX-RC-TIC](../../knowledge/fuentes/registro.md#hiscox-rc-tic)), quedan fuera las multas y las penalizaciones contractuales, los defectos de software que no ha desarrollado el asegurado en exclusiva y los fallos de centros de datos y telecomunicaciones. Para una consultora que construye con modelos de IA de terceros y en la nube, eso es casi todo el riesgo. El condicionado no menciona la inteligencia artificial. Es un solo ejemplo, no una recomendación: cada aseguradora tiene sus exclusiones.

## Lo que el corredor necesita saber de nosotros
- **Actividad:** consultoría de procesos, diseño y construcción de automatizaciones con IA y operación mensual (cuatro fases, `CLAUDE.md`). Clientes medianos y regulados; el primero, previsiblemente, una correduría de seguros (D-011).
- **Cómo trabajamos:** datos inventados hasta la puerta L2; nada se envía a clientes o aseguradoras sin aprobación de una persona; modelos de IA de terceros a través de su API.
- **Contratos:** borradores para abogado con tope de responsabilidad entre corchetes (`governance/legal/borradores/`), pago del piloto ligado a una métrica (50/50).
- **Quiénes:** dos socios, sin empleados; sociedad aún sin constituir (`docs/27`).
- **Volumen previsto:** [facturación del primer año, por decidir].

## Preguntas sobre responsabilidad civil profesional
1. **Ámbito temporal.** ¿La póliza cubre por reclamación presentada durante su vigencia? ¿Desde qué fecha se cubren hechos anteriores (retroactividad)? ¿Qué periodo hay para notificar si no se renueva? En el ejemplo leído: reclamación durante el periodo de seguro, retroactividad fijada en las condiciones particulares y 6 meses gratis o 12 con prima adicional para notificar tras la no renovación.
2. **Antes de la sociedad.** ¿Puede asegurarse la actividad mientras la sociedad no existe? ¿Cubre a los dos socios a título personal?
3. **Errores de lo que propone o hace un sistema con IA.** ¿Está cubierto el daño a un cliente por un error de una automatización que hemos diseñado, aunque la causa sea la respuesta de un modelo de IA de un tercero? Preguntarlo así, con un ejemplo: «la herramienta abrió un siniestro con un dato equivocado y la aseguradora del cliente lo rechazó».
4. **Software de terceros.** El ejemplo excluye defectos de un producto «que no ha sido desarrollado por el asegurado en exclusiva». ¿Cómo se trata lo que construimos sobre modelos, librerías y servicios de terceros?
5. **Nube e infraestructura.** El ejemplo excluye fallos de electricidad, telecomunicaciones y centros de datos, con matices para la nube si no se ha renunciado al derecho de repetición. ¿Qué pasa si el fallo es del proveedor de la nube o del modelo?
6. **Contratos.** ¿Cubre el incumplimiento de un acuerdo de nivel de servicio? ¿Y las penalizaciones o la responsabilidad que asumamos por contrato por encima de la ley? (En el ejemplo, las penalizaciones contractuales quedan fuera.) ¿Qué tope de responsabilidad conviene poner en el contrato para que coincida con el límite asegurado?
7. **Datos personales y confidencialidad.** ¿Cubre la reclamación de un cliente o de sus asegurados por una brecha de datos o por romper la confidencialidad? ¿Las multas de la AEPD son asegurables? (En el ejemplo, las multas y sanciones quedan fuera.)
8. **Propiedad intelectual.** ¿Cubre reclamaciones por derechos de autor sobre lo que entregamos, incluido lo generado con IA? (El ejemplo cubre derechos de autor y marcas, no patentes ni secretos comerciales.)
9. **Límites, sublímites y franquicias.** Límite por reclamación y por año; sublímites de defensa, pérdida de documentos, daño reputacional y devolución de honorarios; franquicia.
10. **Clientes con DORA.** Si el cliente es una aseguradora sujeta a DORA (`governance/legal/borradores/`), ¿suelen pedir un límite mínimo o un certificado? ¿Lo emite la aseguradora?
11. **Territorio y ley.** España y la UE; reclamaciones de fuera.

## Preguntas sobre ciberriesgos
1. **Daños propios:** respuesta al incidente, análisis forense, recuperación de datos y sistemas, notificación a afectados y a la AEPD, pérdida de beneficios y extorsión.
2. **Daños a terceros:** reclamaciones de clientes por un incidente en nuestros sistemas o por transmitir un virus (el ejemplo de RC incluye la «transmisión negligente de un virus informático»).
3. **Requisitos previos:** ¿qué controles exige la aseguradora para dar cobertura (segundo factor, copias probadas, actualizaciones)? INCIBE avisa de que la aseguradora revisa aspectos técnicos antes de firmar y puede exigir correcciones ([INCIBE-CIBERSEGUROS](../../knowledge/fuentes/registro.md#incibe-ciberseguros), artículo de 2021). Comparar con lo que ya tenemos: M-070 y M-071 (cuentas de empresa, segundo factor y gestor de contraseñas).
4. **Exclusiones:** actos intencionados o ilícitos (INCIBE pone como ejemplo vulnerar la normativa de protección de datos), guerra, fallos de infraestructura.
5. **¿Una póliza o dos?** ¿Conviene RC profesional y ciber en un mismo contrato o por separado? ¿Se solapan?

## Qué pedir al corredor
- Al menos tres presupuestos comparables, con el condicionado completo, no solo el resumen.
- Una tabla con las respuestas a las preguntas 1 a 8 de RC y 1 a 4 de ciber para cada presupuesto.
- Qué cambiaría el precio: facturación, sectores, límite y franquicia.

## Para decidir
| Decisión | Quién | Antes de |
|---|---|---|
| Hablar con el corredor con esta lista | Álvaro | [fecha] |
| Elegir póliza y límite, coherente con el tope del contrato | Los dos, con el abogado | El primer piloto |
