# Matriz de aprobaciones · BORRADOR

> Borrador para socios y abogado. Anexo 5 del contrato marco. Dice quién aprueba qué antes de que ocurra. La regla de fondo es de `CLAUDE.md`: **toda acción externa, financiera, legal o contractual requiere la aprobación de una persona**. Nadie aprueba su propio trabajo, y un agente nunca aprueba (lo comprueba `tests/test_motor.py`).

Leyenda: **A** aprueba · **R** realiza o propone · **I** informado · **—** no interviene. «Socio» es cualquiera de los dos socios de Varios salvo que diga «los dos».

## 1. Dentro de Varios
| Acción | IA o agente | Socio | Los dos socios | Abogado o gestor |
|---|---|---|---|---|
| Borrador interno (documento, análisis, código en una rama) | R | I | — | — |
| Subir a `main` documentación o código con pruebas en verde (D-012) | R | A, salvo excepciones | — | — |
| Marcar como aprobada una decisión de `DECISIONS.md` o cambiar `CLAUDE.md` | R (propuesta) | — | A | — |
| Tecnología nueva en el stack | R (justificación) | — | A | — |
| Enviar algo a un cliente o a un tercero | R (borrador) | A | — | — |
| Presupuesto, oferta o precio | R (borrador) | — | A | — |
| Contrato, acuerdo de confidencialidad o encargo del tratamiento | R (borrador) | — | A | A (revisión) |
| Pago, factura o cualquier movimiento de dinero | R (borrador) | — | A | I (gestor) |
| Usar datos reales (pasar de L0 a L1 o L2) | — | — | A | I |
| Publicar la web o algo con la marca | R | — | A | — |

## 2. En el servicio al cliente (proceso de referencia)
| Acción | Sistema (código fijo) | IA | Tramitador del cliente | Responsable del cliente | Socio de Varios |
|---|---|---|---|---|---|
| Recibir un mensaje y registrarlo | R | — | I | — | — |
| Extraer datos del mensaje | — | R | revisa | — | — |
| Detectar excepciones (EX-01 a EX-15) | R | ayuda a detectar | I | — | — |
| Preparar el borrador del parte o de la petición de documentación | R | R (redacción) | A | — | — |
| **Enviar** el parte al portal de la aseguradora o escribir al cliente | — | — | A y ejecuta | — | — |
| Decidir la vía del Consorcio (EX-03) | — | — | R | A | — |
| Cualquier caso con daños personales o fallecimiento (EX-04, EX-15) | — | — | R | A | — |
| Mover dinero por cuenta del cliente (EX-12) | — | — | R | A | — |
| Abrir una reclamación de un cliente (EX-07; un mes para resolver) | R (separa) | — | R | A | — |
| Pasar a una persona cuando el cliente lo pide (EX-08) | R, inmediato | — | atiende | — | — |
| Cambiar reglas, plazos o el modelo de IA | — | — | I | A | R (con pruebas) |
| Suspender la IA y volver al proceso manual | — | — | — | A | I |

## 3. Por puerta
| Puerta | Qué se aprueba | Quién |
|---|---|---|
| G0 · caso elegido | Acuerdo de confidencialidad y propuesta de diagnóstico | Los dos socios y el responsable del cliente |
| G1 · proceso entendido | Informe AS-IS y línea base | Responsable del cliente |
| G2 · diseño aceptado | TO-BE, métrica de éxito y umbral | Responsable del cliente y un socio |
| G3 · prototipo | Prototipo con datos inventados (L0) | Responsable del cliente |
| G4 · piloto seguro | Encargo del tratamiento firmado, L2 superada y anexo de IA | Los dos socios, el responsable del cliente y el abogado |
| G5 · producción | Resultado del piloto frente a la métrica | Responsable del cliente y los dos socios |
| G6 · escalado | Nuevo pedido | Los dos socios y el responsable del cliente |

*Nota: «un piloto con datos reales (G4) exige haber superado L2» (`docs/08-roadmap-y-decisiones.md`).*

## 4. Reglas de la aprobación
- Una aprobación vale para una versión concreta. Si el contenido cambia, se vuelve a aprobar (`tests/test_motor.py`).
- Rechazar exige un motivo, que queda en la auditoría y en la memoria (D-019).
- Lo que espera aprobación no caduca hacia «seguir»: si nadie responde, **se para**. Nunca sigue solo en lo externo, legal o financiero. Es el mismo patrón de Zapier y Power Automate, con la acción por defecto segura ([ZAPIER-HITL](../../../knowledge/fuentes/registro.md#zapier-hitl)).
- Todo queda en la auditoría inmutable: quién aprobó, cuándo, qué versión y con qué nota (D-023).
