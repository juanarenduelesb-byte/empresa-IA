# Calidad, infraestructura y operación

## Calidad
Criterios de aceptación observables; pruebas unitarias e integración deterministas; validación de esquemas; pruebas de aislamiento; evaluaciones LLM con datasets versionados; revisión humana por riesgo; regresión; métricas de error/latencia/coste; rollback. No prometer cero errores.

## Infraestructura inicial
GitHub privado, VS Code/Python, PostgreSQL, Docker Compose. Supabase Free/Render Free u otros free tiers solo para demos y datos sintéticos, considerando límites y suspensión. Mocks antes de activar API de modelos. La suscripción de chat no equivale a crédito API. Cloudflare R2 es alternativa condicionada a cuotas y condiciones.

## Portabilidad
Separar código, runtime, DB, documentos, secretos y configuración. Contenedores y migraciones reproducibles. El Mac personal no debe ser servidor ni único repositorio de datos.

## Operación
Responsables, alertas, SLO, RPO/RTO, backups, restauración, gestión de incidentes, cambios, releases, soporte y continuidad.

## Métricas
Tiempo de ciclo, coste por caso, automatización efectiva, intervención humana, errores/retrabajo, SLA, satisfacción, adopción y ROI.