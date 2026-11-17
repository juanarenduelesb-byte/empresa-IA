# 12 · Ciclo de vida de un proyecto con cliente

_Fases D0 a D6, con su control de paso, y cómo se aprende sin mezclar clientes._

**Fuente:** Atlas · Mapa 8 + Atlas Evolución v1.1, apartado 3.5 + Guía v1.4, diagramas 7 y 9

## En palabras sencillas

Así avanza un cliente: se califica la oportunidad, se descubre el proceso, se diseña, se prueba en pequeño, se pilota y se pasa a producción. En cada paso hay una puerta (G0 a G6). Al cerrar, se aprende, pero lo aprendido se limpia de datos del cliente y lo aprueba una persona antes de reutilizarlo.

## Diagrama

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Instrument Sans, Helvetica, Arial, sans-serif','fontSize':'15px','primaryColor':'#FFFBF3','primaryBorderColor':'#B9A88A','primaryTextColor':'#22171A','lineColor':'#6A5A55','edgeLabelBackground':'#F6EFE1','clusterBkg':'#FBF6EC','clusterBorder':'#E4D6BC','tertiaryColor':'#FFFFFF'},'flowchart':{'curve':'basis','padding':14,'nodeSpacing':38,'rankSpacing':46}}}%%
flowchart TB
D0["D0 · Calificación<br/><small>problema, sponsor, éxito</small>"]:::re -- "G0" --> D1["D1 · Descubrimiento<br/><small>AS-IS, excepciones, línea base</small>"]:::ia
D1 -- "G1" --> D2["D2 · Diseño<br/><small>TO-BE, controles, RACI, coste</small>"]:::ia
D2 -- "G2" --> D3["D3 · Prototipo<br/><small>flujo acotado, datos controlados</small>"]:::re
D3 -- "G3" --> D4["D4 · Piloto<br/><small>usuarios reales limitados</small>"]:::dec
D4 -- "G4" --> D5["D5 · Producción<br/><small>contrato, SLA, soporte</small>"]:::ok
D5 -- "G5" --> D6["D6 · Operar y mejorar<br/><small>ROI, incidencias, cambios</small>"]:::ok
D6 -- "G6 · escalar" --> NX["Nuevo caso o cliente"]:::core
D2 -. "cambio de alcance" .-> CR["Petición de cambio<br/><small>reestimar</small>"]:::dec
CR -.-> D2
D6 --> PM["Post-mortem interno"]:::pe
PM --> SAFE["Extracción segura<br/><small>anonimizar y generalizar</small>"]:::pe
SAFE --> WP["Propuesta para la wiki<br/><small>borrador</small>"]:::ia
WP --> VA{"Validación<br/><small>fuente, permiso, aprobación</small>"}:::dec
VA -- "aprobada" --> REU["Se reutiliza en futuros proyectos"]:::ok
VA -- "no demostrada o identificable" --> DSC["Se descarta o queda aislada"]:::bad
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

1. Registrar oportunidad y solicitante.
2. Descubrimiento con supuestos y lagunas documentados.
3. Propuesta y plan con riesgos y responsables.
4. Aprobación de alcance y ejecución.
5. Ejecución con evidencias.
6. QA y aceptación del cliente.
7. Entrega y cierre con métricas.
8. Post-mortem interno.
9. Extraer patrones no confidenciales.
10. Proponer y validar antes de publicar en la wiki.

## Si algo falla

- Cambia el alcance: petición de cambio y reestimación.
- El cliente no acepta: registrar defectos y plan de corrección.
- Datos no reutilizables: se descarta el aprendizaje o se mantiene aislado.
- Lección no demostrada: no se publica como método.

## Qué tiene que existir

- Ficha de oportunidad
- Mapa AS-IS y TO-BE
- Métrica de éxito firmada
- Informe de cierre

## Correcciones respecto al original

- El original tenía una flecha "reutiliza en futuros proyectos" que cruzaba "completa" y "QA" en diagonal. Se integran las fases D0–D6 del Atlas de Evolución, que el mapa 8 debía incluir y no incluía.
