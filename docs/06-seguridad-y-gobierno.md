# Seguridad, privacidad y gobierno

## Requisitos
Identidad verificada, mínimo privilegio, separación de funciones, aislamiento por cliente, trazabilidad, supervisión humana proporcional al riesgo y seguridad desde diseño.

## Multi-tenancy
El tenant deriva de identidad autenticada, nunca de un tenant_id confiado al usuario. Autorizar en backend antes de recuperar documentos, embeddings, índices o invocar herramientas. Incluir pruebas negativas de acceso cruzado.

## Controles
MFA privilegiado; secretos fuera de Git; bases no expuestas; buckets privados y URLs temporales; RLS como defensa adicional; logs sin secretos; backups y restauración probada; entornos separados; cifrado; gestión de dependencias; retención y borrado definidos.

## Riesgos de IA
Prompt injection en fuentes; exfiltración entre clientes; abuso de herramientas; alucinación/falsa atribución; salidas no validadas; envenenamiento de conocimiento; cambios no aprobados; dependencia de proveedores.

## Tool Gateway
Allowlist, autorización, validación de argumentos, permisos mínimos, sandbox, rate limits, timeouts, idempotencia, auditoría y aprobación según riesgo.

Los planes gratuitos sirven para prototipos con datos sintéticos. Antes de datos reales revisar DPA, subprocesadores, región, retención, uso para entrenamiento, backups, controles, incidentes y obligaciones legales/regulatorias.