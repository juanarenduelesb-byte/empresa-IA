# Roadmap y decisiones

## Estado actual
Arquitectura conceptual y documentación consolidadas; implementación pendiente. El siguiente paso no es construir un CEO omnisciente, sino elegir un proceso real.

## Secuencia
**F0 Preparación:** alcance, repositorio, responsables, política de secretos y entornos.  
**F1 Proceso piloto:** AS-IS/TO-BE, excepciones, fuentes, línea base y KPI.  
**F2 Núcleo:** FastAPI, PostgreSQL, identidad/autorización, motor de estados y auditoría.  
**F3 Conocimiento e integración:** RAW/WIKI/SCHEMA, búsqueda autorizada y un conector real.  
**F4 IA controlada:** modelo configurable, mocks, límites de coste, evaluaciones y QA.  
**F5 Piloto y escalado:** piloto supervisado, métricas, corrección de riesgos y despliegue gradual.

## Decisiones pendientes
Primer sector/proceso; canal inicial; identidad/proveedor; hosting/región; política de datos/retención; aprobaciones humanas; límites de coste/SLA; primer conector; autonomía por tipo de acción.

## Gates
Unificadas el 17/11/2026 con el Atlas de Evolución v1.1 (ver D-009).

**Puertas de cliente (G0–G6), una por fase D0–D6:** G0 caso elegido · G1 proceso entendido · G2 diseño aceptado · G3 prototipo · G4 piloto seguro · G5 producción · G6 escalado.

**Puertas técnicas (L0–L4), de la Guía v1.4:** L0 MVP local con datos inventados · L1 datos internos reales · L2 datos de clientes · L3 automatización externa · L4 escala.

Un piloto con datos reales (G4) exige haber superado L2.

**Riesgo de enfoque:** sin proceso real, datos, integraciones y métricas, construir primero el CEO optimiza una abstracción.