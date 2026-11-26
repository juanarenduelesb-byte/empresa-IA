# Contrato marco de prestación de servicios · BORRADOR PARA ABOGADO

> No firmar ni enviar. Entre corchetes, lo que deciden los socios o el abogado. Las notas en cursiva («*Nota:*») explican de dónde sale cada cláusula y se borran en la versión final.

**Entre** [RAZÓN SOCIAL DE VARIOS — forma jurídica pendiente, M-003], con NIF [·] y domicilio en [·] («el Prestador»), y [RAZÓN SOCIAL DEL CLIENTE], con NIF [·] y domicilio en [·] («el Cliente»).

## 1. Objeto
1.1. Este contrato fija las condiciones generales con las que el Prestador presta al Cliente servicios de análisis, diseño, construcción y operación de procesos con apoyo de inteligencia artificial.
1.2. Cada servicio concreto se contrata mediante un **pedido** firmado por las dos partes, que indica la fase, el alcance, los entregables, el calendario, el precio y la métrica de éxito. Las fases son Diagnosticar, Diseñar, Construir (piloto) y Operar.
1.3. Si un pedido contradice este contrato, prevalece el pedido solo en lo que diga expresamente que modifica.

*Nota: la oferta en cuatro fases y el pago del piloto según una métrica firmada son del modelo de negocio (`docs/00-negocio.md`, CLAUDE.md).*

## 2. Forma de trabajar
2.1. El Prestador trabaja «proceso antes que agente»: primero documenta el proceso actual y el propuesto, y solo después automatiza.
2.2. **Ninguna acción externa, financiera, legal o contractual se ejecuta sin la aprobación de una persona autorizada del Cliente.** Así lo detalla la matriz de aprobaciones (anexo 5).
2.3. El uso de IA se rige por el anexo de uso de IA (anexo 4). La IA no decide cobertura, culpa, fraude ni importes.
2.4. Cada parte nombra un responsable del contrato: [nombre y cargo, sin datos personales en este borrador].

## 3. Obligaciones del Cliente
3.1. Facilitar acceso a las personas, la información y los sistemas que el pedido indique, en los plazos acordados.
3.2. Validar los entregables en [10] días hábiles desde su entrega. Si no hay respuesta en ese plazo, [se entiende aceptado / se escala al responsable del contrato]. *Nota: decisión de los socios.*
3.3. No introducir datos personales reales en entornos de prueba. Las pruebas se hacen con datos inventados.

## 4. Precio y pago
4.1. El precio de cada fase está en su pedido. [Pendiente de decidir antes del 29/01/2027.]
4.2. En el piloto, [50 %] al inicio y [50 %] al alcanzar la métrica firmada en el pedido. Si no se alcanza, [·]. *Nota: el reparto 50/50 es del modelo de negocio; qué pasa si no se alcanza lo deciden los socios.*
4.3. Las facturas se pagan en [30] días naturales desde su recepción. Por pacto, nunca en más de 60 días naturales ([LEY-MOROSIDAD-3-2004](../../../knowledge/fuentes/registro.md#ley-morosidad-3-2004), art. 4). El retraso devenga sin aviso el interés de demora del art. 7 de esa ley y la indemnización por costes de cobro de su art. 8.
4.4. La facturación cumplirá la normativa de facturación vigente (ver la tarea D2: Verifactu y factura electrónica).

## 5. Propiedad intelectual
5.1. **Del Cliente:** sus datos, sus documentos y los entregables específicos del pedido, una vez pagados.
5.2. **Del Prestador:** su metodología, su motor de procesos, sus plantillas, su conocimiento común y cualquier mejora general de estos, aunque se haya hecho durante el pedido. Sobre lo que forme parte de un entregable, el Cliente recibe una licencia [no exclusiva, indefinida, para su uso interno].
5.3. El Prestador no usa los datos del Cliente para entrenar modelos ni para otros clientes. Las lecciones que aprenda se guardan sin datos del Cliente.

*Nota: pregunta 4 al abogado.*

## 6. Confidencialidad y protección de datos
6.1. La confidencialidad se rige por el acuerdo del anexo 3, que sigue vigente [5] años tras el fin del contrato.
6.2. Si el Prestador trata datos personales por cuenta del Cliente, firmarán el contrato de encargo del anexo 2 antes de empezar.

## 7. Responsabilidad
7.1. Cada parte responde de los daños que cause por incumplir este contrato ([CODIGO-CIVIL](../../../knowledge/fuentes/registro.md#codigo-civil), art. 1101).
7.2. Salvo dolo o culpa grave, la responsabilidad total del Prestador por cada pedido se limita a [el importe pagado por ese pedido en los 12 meses anteriores]. *Nota: la responsabilidad por dolo no se puede excluir (Código Civil, art. 1102). El tope lo fija el abogado con el seguro de RC profesional (pregunta 2).*
7.3. El Prestador no responde de las decisiones que tome el Cliente sobre las propuestas de la IA ni de lo que una persona del Cliente haya aprobado, salvo que el error venga de un incumplimiento del Prestador.
7.4. Ninguna parte responde de lucro cesante ni de daños indirectos, salvo dolo. [Validar con el abogado.]

## 8. Duración y terminación
8.1. El contrato dura [1 año] y se prorroga por periodos iguales salvo preaviso de [2 meses].
8.2. Cualquier parte puede resolverlo si la otra incumple gravemente y no lo corrige en [30] días desde el requerimiento.
8.3. Al terminar, el Prestador devuelve o borra los datos del Cliente, a elección de este, y entrega lo producido hasta la fecha en un formato fácilmente accesible. Los pedidos en curso se terminan o se liquidan según [·].

## 9. Si el Cliente está sujeto a DORA (anexo opcional)
*Nota: solo si el Cliente es una entidad financiera sujeta al Reglamento (UE) 2022/2554, por ejemplo una aseguradora mediana bajo Solvencia II. Las corredurías que sean pymes están excluidas ([DORA-2022-2554](../../../knowledge/fuentes/registro.md#dora-2022-2554), art. 2.3 e).*

Para cumplir el art. 30.2 de DORA, el contrato incluirá:

| Requisito | Letra | Dónde se cubre |
|---|---|---|
| Descripción completa de los servicios y condiciones de subcontratación | a | Pedido y cláusula 9.1 |
| Lugares donde se presta el servicio y se tratan los datos, con aviso previo de cambios | b | Anexo 2, anexo II, y cláusula 9.2 |
| Disponibilidad, autenticidad, integridad y confidencialidad de los datos | c | Anexo 2, anexo III |
| Acceso, recuperación y devolución de los datos en formato fácilmente accesible | d | Cláusula 8.3 |
| Niveles de servicio | e | Pedido de la fase Operar |
| Asistencia en incidentes TIC sin coste o a coste fijado antes | f | Cláusula 9.3 |
| Cooperación con las autoridades competentes | g | Cláusula 9.4 |
| Derechos de terminación y preavisos mínimos | h | Cláusula 8 |
| Participación en la formación de seguridad TIC del Cliente | i | Cláusula 9.5 |

9.1. El Prestador solo subcontrata con autorización previa y escrita del Cliente.
9.2. El Prestador avisa con [·] de antelación de cualquier cambio de región o país de tratamiento.
9.3. El Prestador ayuda en los incidentes TIC relacionados con el servicio [sin coste adicional / a la tarifa del pedido].
9.4. El Prestador coopera plenamente con las autoridades competentes y de resolución del Cliente.
9.5. El Prestador participa en los programas de concienciación y formación en seguridad TIC del Cliente que le afecten.

Si el servicio sustenta una función esencial o importante, se añaden los requisitos del art. 30.3: niveles de servicio con objetivos cuantitativos, planes de contingencia, acceso y auditoría, y una estrategia de salida con periodo transitorio. *Nota: pregunta 5 al abogado.*

## 10. Varios
10.1. Ley aplicable: española. Jurisdicción: [juzgados de · / arbitraje]. *Pregunta 6.*
10.2. Las comunicaciones se hacen por escrito a las direcciones del encabezado o a las que se indiquen en el pedido.
10.3. Ninguna parte cede este contrato sin el consentimiento escrito de la otra.

**Anexos:** 1 · modelo de pedido · 2 · encargo del tratamiento · 3 · confidencialidad · 4 · uso de IA · 5 · matriz de aprobaciones.

## Anexo 1 · Modelo de pedido (resumen)
Fase · alcance (qué entra y qué no) · entregables con su criterio de aceptación · calendario · personas de cada parte (roles) · precio y forma de pago · **métrica de éxito con su línea base, umbral y quién la certifica** · datos que se tratarán (si hay, anexo 2) · supuestos y riesgos.
