# Sistemas, datos y restricciones · Atalaya (FICTICIO)

> **Datos inventados** para el caso de práctica.

## Sistemas que usan hoy
| Sistema | Para qué | Integración posible |
|---|---|---|
| Programa de gestión de la correduría (producto comercial genérico, en local con copia en la nube del proveedor) | Clientes, pólizas, recibos, expedientes de siniestro | Exportación CSV diaria; API de lectura a confirmar con el proveedor |
| Correo corporativo | Comunicación con clientes y aseguradoras | Buzón compartido «siniestros@» |
| WhatsApp Business (una línea) | Avisos de clientes particulares | Sin integración; se reenvía al correo a mano |
| Portales web de las aseguradoras A–F | Alta del siniestro y seguimiento | Sin API conocida; alta manual. La aseguradora A tiene un formulario estructurado; las demás, campos libres |
| Centralita | Llamadas | Sin grabación |

## Datos
- Datos personales de clientes (identificación, contacto, matrículas, direcciones de riesgo).
- Datos de salud en siniestros con lesionados y en pólizas de salud: **fuera del piloto**.
- Datos de terceros contrarios (otros conductores, vecinos, reclamantes).

## Restricciones de la dirección
- Nada sale de la correduría hacia clientes o aseguradoras sin que lo apruebe una persona.
- Ningún dato real se usa durante el diagnóstico: trabajaremos con su descripción y con casos inventados.
- El piloto no puede exigir cambiar el programa de gestión.
- El responsable de sistemas tiene 4 horas al mes para este proyecto.
- Cumplimiento quiere ver el análisis de RGPD y del Reglamento de IA antes del piloto, y que un abogado revise el contrato.

## Lo que se considera éxito (borrador de la dirección)
- Reducir a la mitad el tiempo de trabajo activo en la apertura de los siniestros sencillos.
- Que ningún siniestro se dé de alta con datos incorrectos por culpa de la herramienta.
- Que el cliente reciba en menos de 2 horas laborables un acuse con número y siguientes pasos.
