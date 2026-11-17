# 02 · Flujo completo del CEO digital

_De la petición a la entrega, con todos los desvíos: preguntar, rechazar, escalar, rehacer y aprobar._

**Fuente:** Atlas · Mapa 2, versión 1.0

## En palabras sencillas

Este es el camino de cualquier encargo. Lo importante son los rombos: en cada uno el CEO puede parar. Si falta información, pregunta. Si no está permitido, rechaza o deriva. Si la calidad falla, se rehace. Si el riesgo lo exige, una persona aprueba antes de entregar.

## Diagrama

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Instrument Sans, Helvetica, Arial, sans-serif','fontSize':'15px','primaryColor':'#FFFBF3','primaryBorderColor':'#B9A88A','primaryTextColor':'#22171A','lineColor':'#6A5A55','edgeLabelBackground':'#F6EFE1','clusterBkg':'#FBF6EC','clusterBorder':'#E4D6BC','tertiaryColor':'#FFFFFF'},'flowchart':{'curve':'basis','padding':14,'nodeSpacing':38,'rankSpacing':46}}}%%
flowchart TB
A["Solicitud<br/><small>chat, formulario o integración</small>"]:::re --> B["Validar entrada<br/><small>identidad, formato, adjuntos</small>"]:::re
B --> C{"¿Entrada segura?"}:::dec
C -- "no" --> Q["Cuarentena y revisión<br/><small>no se ejecuta el adjunto</small>"]:::bad
C -- "sí" --> D["Clasificar<br/><small>intención, sector, proceso, riesgo</small>"]:::ia
D --> E{"¿Información suficiente?"}:::dec
E -- "no" --> F["Preguntar al solicitante"]:::ia
F -- "respuesta" --> D
E -- "sí" --> G{"¿Permitido y seguro?"}:::dec
G -- "no permitido" --> R["Rechazar o derivar<br/><small>con motivo registrado</small>"]:::bad
G -- "riesgo alto o dudoso" --> ES["Escalar a una persona"]:::pe
ES -- "autoriza" --> H
G -- "sí" --> H["Planificar<br/><small>tareas, dependencias, criterios, coste</small>"]:::ia
H --> I["Ejecutar con el motor de procesos<br/><small>departamentos y herramientas autorizadas</small>"]:::re
I --> J["Control de calidad y evidencias"]:::re
J --> K{"¿Supera QA?"}:::dec
K -- "no" --> L["Rehacer o replanificar<br/><small>con defectos concretos</small>"]:::dec
L --> I
K -- "sí" --> M{"¿Requiere aprobación?"}:::dec
M -- "sí" --> N["Aprobación humana"]:::pe
N -- "denegada" --> O["Detener y registrar decisión"]:::bad
N -- "aprobada" --> P["Entregar<br/><small>formato acordado y trazabilidad</small>"]:::ok
M -- "no" --> P
P --> Z["Cerrar y proponer aprendizaje<br/><small>como borrador, nunca autoaprobado</small>"]:::ok
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

1. Registrar solicitud, solicitante, cliente, fecha y adjuntos.
2. Validar identidad, formato, adjuntos y autorización.
3. Clasificar intención, sector, proceso, sensibilidad, riesgo y confianza.
4. Si falta información esencial, preguntar.
5. Comprobar alcance, política y permisos antes de planificar.
6. Crear el plan con responsables, dependencias y criterios de éxito.
7. Ejecutar con herramientas autorizadas.
8. Validar resultados contra fuentes y criterios.
9. Pedir aprobación humana si corresponde.
10. Entregar, registrar y cerrar; el aprendizaje se propone aparte.

## Si algo falla

- Entrada sospechosa: cuarentena; nunca se ejecuta el adjunto.
- Baja confianza: preguntar, no forzar la clasificación.
- Fuera de alcance: rechazar o proponer una alternativa segura.
- Fallo de tarea: reintento limitado o escalado.
- QA no superado: vuelve a ejecución con defectos concretos.
- Aprobación denegada: se detiene la acción y se registra.

## Qué tiene que existir

- Solicitud normalizada
- Ficha de clasificación y riesgo
- Plan de ejecución
- Registro de aprobaciones
- Paquete de entrega y cierre

## Correcciones respecto al original

- En el original, la entrega iba antes de la aprobación humana, al revés de lo que dice su propio texto (paso 9 aprobar, paso 10 entregar). Corregido: primero se aprueba y después se entrega.
- Faltaban en el dibujo los caminos de rechazar, escalar y cuarentena que el texto sí describe.
- Las etiquetas "no / respuesta" y "baja confianza" se pisaban. Ahora cada flecha tiene su etiqueta.
