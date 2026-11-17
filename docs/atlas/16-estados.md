# 16 · Estados de un encargo

_Por dónde puede pasar un encargo y quién puede moverlo de un estado a otro._

**Fuente:** Guía v1.4, Anexo I (estados mínimos) y Anexo III apartado 4

## En palabras sencillas

Un encargo siempre está en un único estado. Solo puede pasar a los estados que marcan las flechas, y cada cambio deja escrito quién lo hizo, cuándo y por qué. Así nunca se pierde el hilo de un caso.

## Diagrama

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Instrument Sans, Helvetica, Arial, sans-serif','fontSize':'15px','primaryColor':'#FFFBF3','primaryBorderColor':'#B9A88A','primaryTextColor':'#22171A','lineColor':'#6A5A55','edgeLabelBackground':'#F6EFE1','clusterBkg':'#FBF6EC','clusterBorder':'#E4D6BC','tertiaryColor':'#FFFFFF'},'flowchart':{'curve':'basis','padding':14,'nodeSpacing':38,'rankSpacing':46}}}%%
stateDiagram-v2
direction TB
state "Recibido" as Recibido
state "En clasificación" as EnClasificacion
state "Pendiente de información" as PendienteInfo
state "Planificado" as Planificado
state "Escalado" as Escalado
state "Rechazado" as Rechazado
state "En ejecución" as EnEjecucion
state "Bloqueado" as Bloqueado
state "Cancelado" as Cancelado
state "En QA" as EnQA
state "Retrabajo" as Retrabajo
state "Pendiente de aprobación" as PendienteAprobacion
state "Entregado" as Entregado
state "Cerrado" as Cerrado
state "Reabierto" as Reabierto
[*] --> Recibido
Recibido --> EnClasificacion: identidad y cliente validados
EnClasificacion --> PendienteInfo: falta un dato
PendienteInfo --> EnClasificacion: llega la respuesta
EnClasificacion --> Planificado: decisión CONTINUAR
EnClasificacion --> Escalado: riesgo alto
EnClasificacion --> Rechazado: no permitido
Escalado --> Planificado: persona autoriza
Planificado --> EnEjecucion: plan aprobado
EnEjecucion --> Bloqueado: dependencia o error
Bloqueado --> EnEjecucion: causa resuelta
Bloqueado --> Cancelado
EnEjecucion --> EnQA
EnQA --> Retrabajo: no supera
Retrabajo --> EnEjecucion
EnQA --> PendienteAprobacion: riesgo lo exige
EnQA --> Entregado: no requiere aprobación
PendienteAprobacion --> Entregado: aprobado
PendienteAprobacion --> Retrabajo: corregir
Entregado --> Cerrado: aceptado
Cerrado --> Reabierto: con motivo y autorización
Reabierto --> EnClasificacion
Rechazado --> [*]
Cancelado --> [*]
Cerrado --> [*]
```

## Pasos

1. Recibido → En clasificación: se validan identidad y cliente.
2. En clasificación → Pendiente de información / Planificado / Escalado / Rechazado: decisión del CEO con motivo.
3. Planificado → En ejecución: plan aprobado según riesgo y presupuesto.
4. En ejecución → Bloqueado / En QA.
5. En QA → Retrabajo / Pendiente de aprobación / Entregado.
6. Entregado → Cerrado; Cerrado → Reabierto solo con motivo y autorización.

## Si algo falla

- QA no puede aprobar lo que no ha comprobado.
- Quien aprueba debe ver la versión exacta; si cambia después, hay que volver a aprobar.

## Qué tiene que existir

- Tabla de transiciones permitidas en el código (no texto libre)

## Correcciones respecto al original

- Había tres listas de estados que se mezclaban: la del encargo (en español), la de la tarea (en inglés: queued, running…) y la de la instancia de proceso. Se separan: este es el encargo. Las tareas usan sus siete estados y se explican en Procesos.
