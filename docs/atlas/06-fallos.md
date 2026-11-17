# 06 · Fallos, reintentos y recuperación

_Nada se reintenta para siempre. Lo dudoso no se propaga._

**Fuente:** Guía v1.4, diagrama 13 y Anexo III apartado 4.1

## En palabras sencillas

Si algo sale mal, el sistema distingue: un fallo pasajero se reintenta unas pocas veces; si se agotan los intentos, se prueba otra vía o se pasa a una persona; si el resultado parece peligroso, se aparta y se abre una incidencia. Nunca se repite una acción que ya se hizo, como un pago.

## Diagrama

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Instrument Sans, Helvetica, Arial, sans-serif','fontSize':'15px','primaryColor':'#FFFBF3','primaryBorderColor':'#B9A88A','primaryTextColor':'#22171A','lineColor':'#6A5A55','edgeLabelBackground':'#F6EFE1','clusterBkg':'#FBF6EC','clusterBorder':'#E4D6BC','tertiaryColor':'#FFFFFF'},'flowchart':{'curve':'basis','padding':14,'nodeSpacing':38,'rankSpacing':46}}}%%
flowchart LR
A["Tarea<br/><small>entrada validada</small>"]:::re --> B["Ejecutar<br/><small>tiempo máximo, límites, idempotencia</small>"]:::re
B --> C{"¿Resultado válido?"}:::dec
C -- "sí" --> OK["Aceptar resultado<br/><small>evidencia, estado, salida</small>"]:::ok
C -- "error pasajero" --> R["Reintento controlado<br/><small>límite, espera, sin duplicar</small>"]:::dec
R -- "quedan intentos" --> B
R -- "agotados" --> FB["Alternativa o escalado<br/><small>otro modelo aprobado o persona</small>"]:::pe
FB -- "validado" --> OK
FB -- "no recuperable" --> INC["Incidencia<br/><small>alerta, causa, corrección</small>"]:::bad
C -- "inseguro o inválido" --> BQ["Bloquear y cuarentena<br/><small>no propagar</small>"]:::bad
BQ --> INC
classDef ia fill:#DDEFEA,stroke:#0B7A78,stroke-width:1.6px,color:#22171A
classDef re fill:#FFFBF3,stroke:#B9A88A,stroke-width:1.4px,color:#22171A
classDef pe fill:#F3E2E1,stroke:#7A1F2E,stroke-width:1.6px,color:#22171A
classDef dec fill:#F8EBCF,stroke:#8A5A0C,stroke-width:1.6px,color:#22171A
classDef bad fill:#F6DEDF,stroke:#A8283A,stroke-width:1.6px,color:#22171A
classDef ok fill:#E1F0E4,stroke:#1D6B3E,stroke-width:1.6px,color:#22171A
classDef core fill:#22171A,stroke:#22171A,color:#F6EFE1
classDef wine fill:#7A1F2E,stroke:#7A1F2E,color:#FFFFFF
```

## Pasos

1. Clasificar el error: pasajero, permanente, funcional, de permisos o de seguridad.
2. Tiempo máximo y número de intentos configurables, con espera creciente.
3. Antes de reintentar una acción externa, comprobar si ya se ejecutó.
4. Agotados los intentos: bloqueado o escalado, con evidencia y alternativa manual.
5. El estado persiste: reiniciar el sistema no pierde ni duplica tareas.

## Si algo falla

- Los errores de permisos o de política no se reintentan nunca.

## Qué tiene que existir

- Política de reintentos
- Claves de idempotencia
- Procedimiento manual alternativo

## Correcciones respecto al original

- El original tenía la etiqueta "Sí" lejos de su flecha y una línea de vuelta que pasaba por debajo de otras cajas.
