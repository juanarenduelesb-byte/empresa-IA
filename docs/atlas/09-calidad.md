# 09 · Calidad, evaluación y aprobación humana

_No se confunde una respuesta convincente con un resultado correcto y autorizado._

**Fuente:** Atlas · Mapa 6 + Guía v1.4, diagrama 8 y Anexo III apartado 9

## En palabras sencillas

Los criterios de "bien hecho" se escriben antes de empezar. Primero comprueban las reglas automáticas; después, si el riesgo lo pide, una persona. Lo que falla vuelve a rehacerse. Y cada error que se encuentra se convierte en una prueba nueva para que no se repita.

## Diagrama

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Instrument Sans, Helvetica, Arial, sans-serif','fontSize':'15px','primaryColor':'#FFFBF3','primaryBorderColor':'#B9A88A','primaryTextColor':'#22171A','lineColor':'#6A5A55','edgeLabelBackground':'#F6EFE1','clusterBkg':'#FBF6EC','clusterBorder':'#E4D6BC','tertiaryColor':'#FFFFFF'},'flowchart':{'curve':'basis','padding':14,'nodeSpacing':38,'rankSpacing':46}}}%%
flowchart TB
RQ["Criterios de aceptación<br/><small>se fijan antes de ejecutar</small>"]:::pe --> RA["Resultado del agente<br/><small>análisis, documento, acción propuesta</small>"]:::ia
RA --> QA["QA automático<br/><small>esquema, cálculos, fuentes, pruebas</small>"]:::re
QA --> D1{"¿Supera?"}:::dec
D1 -- "no" --> RT["Rehacer<br/><small>corregir, pedir datos o escalar</small>"]:::bad
RT --> RA
D1 -- "sí" --> D2{"¿El riesgo exige revisión humana?"}:::dec
D2 -- "sí" --> HR["Revisión humana<br/><small>persona, rol, fecha, versión exacta</small>"]:::pe
HR -- "corregir" --> RT
HR -- "aprobar" --> OK["Supera<br/><small>entrega o acción con registro</small>"]:::ok
D2 -- "no" --> OK
OK --> MT["Métricas<br/><small>acierto, errores, coste, tiempo, escalados</small>"]:::re
MT --> DS["Nuevos casos de prueba<br/><small>cada fallo relevante se convierte en prueba</small>"]:::ia
DS -. "alimenta" .-> QA
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

1. Definir aceptación, nivel de riesgo y revisor.
2. Validaciones automáticas fijas.
3. Evaluar calidad y fundamentación con pruebas controladas.
4. Revisión humana para tareas de riesgo.
5. Registrar decisión, versión y evidencias.
6. Medir calidad, coste, tiempo, fallos y escalados.
7. Convertir fallos en nuevos casos de prueba.

## Si algo falla

- Sin criterio de aceptación no se marca como terminado.
- Evaluadores no calibrados: no se automatiza la aprobación.
- Regresión detectada: se bloquea la versión y se revierte.
- Desacuerdo entre evaluadores: decide un experto humano.
- El agente que propone nunca se aprueba a sí mismo.

## Qué tiene que existir

- Conjunto de pruebas con versión (normales, límite y ataques)
- Umbrales por caso de uso
- Registro de aprobaciones

## Correcciones respecto al original

- El original mezclaba en un solo dibujo el control de cada resultado y el control de cambios del sistema, con cuatro flechas diagonales cruzadas ("mide", "registra", "añade casos"). Se separan: este mapa es el control de cada resultado; el de cambios va en el mapa 10.
