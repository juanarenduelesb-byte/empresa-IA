# Catálogo de integraciones

**Estado:** draft. Fuentes consultadas el 17/11/2026; ver el [registro de fuentes](../../knowledge/fuentes/registro.md).

## Conectores que necesitaremos (hipótesis hasta validar el proceso de referencia)
| Conector | Para qué | Cuándo | Riesgo | Estado |
|---|---|---|---|---|
| Correo entrante (IMAP o Microsoft Graph) | Recibir comunicaciones de siniestros | S7 (simulado con archivos) | Medio: contenido no confiable (P20) | propuesto |
| Almacén de documentos | Adjuntos y evidencias | S7 | Medio | propuesto |
| Programa de gestión de la correduría | Registrar el expediente | Tras el piloto; depende del cliente | Alto: escritura | por investigar |
| Portales de aseguradoras | Presentar el parte | No en el piloto; sin API pública conocida | Alto: acción externa | por investigar |
| Proveedor de modelos de IA | Extracción y redacción | S6 | Medio: datos personales, coste | propuesto |
| Firma o notificación al cliente | Acuse de recibo | Tras el piloto | Alto: acción externa | por investigar |

## Software libre evaluado
Se priorizan las licencias, el mantenimiento, la seguridad, las dependencias, el esfuerzo de integración, las limitaciones, el coste y la aplicabilidad. **Ninguno se adopta** sin una decisión registrada (CLAUDE.md: stack cerrado).

| Proyecto | Licencia | Encaje | Dependencias y esfuerzo | Limitaciones | Recomendación |
|---|---|---|---|---|---|
| [Temporal](../../knowledge/fuentes/registro.md#oss-temporal) | MIT | Ejecución duradera, reintentos y compensación | Clúster propio que operar; alto | Mucho para un piloto | Revisar tras S5 si el motor propio se queda corto |
| [Camunda 8](../../knowledge/fuentes/registro.md#oss-camunda) | Camunda License 1.0 (producción de pago) | BPMN completo | Alto; coste de licencia | No es OSI | Descartado para el piloto |
| [n8n](../../knowledge/fuentes/registro.md#oss-n8n) | Sustainable Use License | Automatizaciones internas | Bajo | Restringe ofrecerlo alojado a terceros | Solo uso interno; nunca en la oferta al cliente sin revisión legal |
| [SpiffWorkflow](../../knowledge/fuentes/registro.md#oss-spiff) | LGPL-3.0 | Motor BPMN en Python | Medio | Copyleft débil | Candidato si necesitamos BPMN ejecutable |
| [Docling](../../knowledge/fuentes/registro.md#oss-docling) | MIT | Leer PDF y Office en local | Medio (modelos locales) | Calidad variable con escaneados | Candidato para S7 |
| [Presidio](../../knowledge/fuentes/registro.md#oss-presidio) | MIT | Detectar y seudonimizar datos personales | Medio | Español y DNI/NIE requieren configuración; no lo encuentra todo | Candidato para S6, con pruebas propias |
| [Langfuse](../../knowledge/fuentes/registro.md#oss-langfuse) | MIT (núcleo) | Trazas de LLM | Alto: ClickHouse, Redis, S3 | Auditoría solo en Enterprise | Aplazar; empezar con trazas propias y OpenTelemetry |
| [promptfoo](../../knowledge/fuentes/registro.md#oss-promptfoo) | MIT | Evaluación y pruebas adversariales | Node.js fuera del stack | Propiedad de OpenAI desde marzo de 2026 | Opcional en S9; alternativa: pytest propio |

**Laguna:** no se han revisado avisos de seguridad (CVE) de cada proyecto. Hacerlo antes de cualquier adopción.
