# 04 · Ejecución: motor de procesos, agentes y herramientas

_El plan se convierte en tareas controladas por estados. Ningún agente actúa libremente._

**Fuente:** Atlas · Mapa 4 + Atlas Evolución v1.1, apartado 3.2

## En palabras sencillas

Cuando el plan está aprobado, el motor de procesos lo convierte en tareas. Cada tarea va a un agente con lo justo para trabajar. Si el agente quiere usar una herramienta, tiene que pedir permiso en una puerta. El resultado se comprueba, y si falla se reintenta con límite o se escala. Todo queda registrado.

## Diagrama

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Instrument Sans, Helvetica, Arial, sans-serif','fontSize':'15px','primaryColor':'#FFFBF3','primaryBorderColor':'#B9A88A','primaryTextColor':'#22171A','lineColor':'#6A5A55','edgeLabelBackground':'#F6EFE1','clusterBkg':'#FBF6EC','clusterBorder':'#E4D6BC','tertiaryColor':'#FFFFFF'},'flowchart':{'curve':'basis','padding':14,'nodeSpacing':38,'rankSpacing':46}}}%%
flowchart TB
A["Plan aprobado<br/><small>objetivo, tareas, criterios, límites</small>"]:::re --> B["Motor de procesos<br/><small>estados, dependencias, plazos</small>"]:::core
B --> C["Asignador<br/><small>capacidad, carga, riesgo, coste</small>"]:::re
C --> D["Agente acotado<br/><small>contexto mínimo autorizado</small>"]:::ia
D -- "pide una acción" --> E{"Puerta de políticas<br/>¿autorizado?"}:::dec
E -- "no" --> X["Bloquear y alertar"]:::bad
E -- "sí" --> F["Puerta de herramientas<br/><small>valida argumentos, límites, sandbox</small>"]:::dec
F --> G["Herramienta<br/><small>permisos mínimos y aislada</small>"]:::re
G --> H{"¿Resultado válido?<br/><small>esquema y criterios</small>"}:::dec
H -- "sí" --> I["Control de calidad"]:::pe
H -- "no" --> J["Reintento limitado o escalado"]:::dec
J -- "replanifica" --> B
I --> K["Estado final<br/><small>terminada, fallida, bloqueada o espera aprobación</small>"]:::ok
B -. "registra" .-> L[("Auditoría<br/><small>quién, qué, cuándo, con qué permiso</small>")]:::re
F -. "registra" .-> L
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

1. El motor crea tareas con identificador y estado.
2. El asignador elige capacidad y modelo según política.
3. Se prepara el contexto mínimo autorizado.
4. La puerta valida identidad, argumentos, alcance y presupuesto.
5. La herramienta se ejecuta con permisos mínimos.
6. El resultado se valida contra esquema y criterios.
7. Se registra traza y coste.
8. Si falla: reintento limitado, compensación o escalado.
9. QA y aprobación antes de entregar.

## Si algo falla

- Tiempo agotado: cancelar si es seguro y reintentar con espera creciente.
- Respuesta mal formada: se rechaza y no se propaga.
- Herramienta no autorizada: se bloquea y se avisa.
- Efecto duplicado: claves de idempotencia y conciliación.
- Agente en bucle o coste excesivo: límites y botón de parada.

## Qué tiene que existir

- Catálogo de herramientas
- Máquina de estados
- Política de reintentos e idempotencia
- Registro de ejecuciones y costes
- Evaluaciones de agentes

## Correcciones respecto al original

- Se añade el motor de procesos y la salida "bloquear" de la puerta de políticas, que pedía el Atlas de Evolución.
- La flecha "replanifica" cruzaba toda la imagen por encima de otras cajas. Ahora vuelve limpia al motor.
