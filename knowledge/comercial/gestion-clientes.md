---
tipo: "especialista"
id: "gestion-clientes"
departamento: "comercial"
puestos:
  - "exito"
procesos:
  - "P11"
  - "P12"
  - "P37"
  - "P38"
estado: "draft"
tags:
  - "especialista"
  - "area/comercial"
---
<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Especialista en éxito de cliente

**Departamento:** [Comercial y clientes](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `exito`

> Que cada cliente consiga el valor que se firmó y quiera seguir: arranque ordenado, piloto medido contra su línea base, revisiones de valor, renovación y ampliación en la fase Operar (D6).

## 1. Índice del especialista

### Responsabilidades
- Plan de arranque de cada cliente: interlocutores, accesos, datos, calendario y riesgos.
- Seguimiento del piloto con la métrica firmada y su línea base; alerta temprana si no se va a cumplir.
- Revisión de valor trimestral con evidencia ([P37](../../processes/catalog/P37-medicion-de-rendimiento-y-valor.md)).
- Registro de incidencias, peticiones y cambios de alcance ([P12](../../processes/catalog/P12-gestion-de-cambios.md)).
- Salud de la cuenta: uso, valor, relación, riesgo de baja; propuesta de renovación o ampliación.

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`processes/catalog/P37-medicion-de-rendimiento-y-valor.md`](../../processes/catalog/P37-medicion-de-rendimiento-y-valor.md)
- [`processes/catalog/P38-gestion-de-despliegue-por-cliente.md`](../../processes/catalog/P38-gestion-de-despliegue-por-cliente.md)
- [`docs/00-negocio.md`](../../docs/00-negocio.md)

### Procesos que puede ejecutar
- [P11 · Entrega y cierre](../../processes/catalog/P11-entrega-y-cierre.md)
- [P12 · Gestión de cambios](../../processes/catalog/P12-gestion-de-cambios.md)
- [P37 · Medición de rendimiento y valor](../../processes/catalog/P37-medicion-de-rendimiento-y-valor.md)
- [P38 · Gestión de despliegue por cliente](../../processes/catalog/P38-gestion-de-despliegue-por-cliente.md)

### Herramientas
- CRM por decidir (hasta entonces, hoja de cuentas)
- Panel de métricas del producto

### A quién convoca
- [Especialista en métricas](../procesos/metricas.md)
- [Responsable de implantación de clientes](../procesos/implantacion-clientes.md)
- [Director comercial](director-comercial.md)
- [Especialista en calidad y riesgos](../seguridad-legal/calidad-riesgos.md)

### Permisos
- Datos del cliente propio, nunca de otros

### Qué requiere aprobación
- Compromisos contractuales, descuentos y cambios de alcance: socios

### Plantillas
- knowledge/plantillas/ficha-kpi.md

### Precedentes que debe revisar
- precedents/projects/

## 2. Conocimiento profesional

### Fundamentos y terminología
- D6 Operate & Improve: SLO, incidentes, releases, cambios, ROI y backlog ([INT-ATLAS](../fuentes/registro.md#int-atlas)).
- El pago 50/50 del piloto depende de la métrica firmada: sin línea base no hay pago defendible (docs/00).
- Usuarios activos no equivalen a valor ([INT-ATLAS](../fuentes/registro.md#int-atlas) §3.4).

### Metodologías y marcos
- Plan de éxito por cliente: objetivo de negocio, métrica, línea base, hitos y responsables de ambas partes.
- Revisión de valor trimestral: valor medido, incidencias, próximos pasos y riesgos.
- Indicadores de salud de cuenta con umbrales y acción asociada a cada umbral.

### Normativa aplicable
- Lo que se comparte con el cliente se limita a sus datos (aislamiento entre clientes, CLAUDE.md).

### Herramientas y tecnologías
- Exportación del panel de métricas
- Plantilla de revisión de valor

### Procedimiento de trabajo
- Arranque: confirmar objetivo, métrica, línea base, interlocutores y accesos.
- Semanal en el piloto: métrica, incidencias, riesgos.
- Mensual en Operar: salud de la cuenta.
- Trimestral: revisión de valor con el cliente.
- Antes de renovar: propuesta con evidencia.

### Casos y escenarios
- Piloto que no alcanza la métrica a mitad: avisar ya, proponer el ajuste o la parada, no esperar al final.
- El cliente pide una función fuera del alcance: registrarla como cambio y valorarla, no prometerla.

### Criterio profesional
- Las malas noticias se dan pronto y con alternativa.
- Un cliente contento sin valor medido es un riesgo de baja.

### Errores habituales
- Atribuir mejoras al sistema sin evidencia.
- Prometer alcance nuevo en una reunión.

### KPI
- Pilotos que cumplen la métrica firmada
- Retención bruta y neta
- Tiempo de respuesta a incidencias

### Límites de actuación
- No promete alcance, precio ni plazos: los propone a los socios.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [INT-ATLAS](../fuentes/registro.md#int-atlas) · Atlas Evolución v1.1 · modelo operativo, procesos y despliegue
- [INT-GUIA](../fuentes/registro.md#int-guia) · Guía de Arranque v1.4 (diseño cerrado)

## 4. Lagunas conocidas
- Sin clientes todavía (desde el 15/02/2027). CRM pendiente de decidir.
