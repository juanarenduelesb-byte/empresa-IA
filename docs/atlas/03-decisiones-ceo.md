# 03 · Las cinco decisiones del CEO

_La clasificación no es una etiqueta: termina siempre en una decisión auditable._

**Fuente:** Guía v1.4, Anexo III apartados 2 y 2.2 + diagrama 11

## En palabras sencillas

Después de entender un encargo, el CEO solo puede hacer una de cinco cosas: seguir, preguntar, escalar a una persona, rechazar o derivar a otro profesional. Siempre deja escrito por qué. La confianza que diga la IA es una pista, nunca un permiso.

## Diagrama

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Instrument Sans, Helvetica, Arial, sans-serif','fontSize':'15px','primaryColor':'#FFFBF3','primaryBorderColor':'#B9A88A','primaryTextColor':'#22171A','lineColor':'#6A5A55','edgeLabelBackground':'#F6EFE1','clusterBkg':'#FBF6EC','clusterBorder':'#E4D6BC','tertiaryColor':'#FFFFFF'},'flowchart':{'curve':'basis','padding':14,'nodeSpacing':38,'rankSpacing':46}}}%%
flowchart TB
A["Petición<br/><small>objetivo, datos, restricciones</small>"]:::re --> B["Ficha normalizada<br/><small>hechos, supuestos y preguntas separados</small>"]:::ia
B --> C["Detectar límites<br/><small>alcance, política, datos sensibles</small>"]:::re
C --> D{"¿Está permitido?"}:::dec
D -- "prohibido o no autorizado" --> RE["RECHAZAR<br/><small>explica el límite</small>"]:::bad
D -- "necesita otro profesional" --> DE["DERIVAR<br/><small>pasa el contexto mínimo</small>"]:::pe
D -- "sí" --> E{"¿Datos suficientes?"}:::dec
E -- "falta algo que cambia la solución" --> PR["PREGUNTAR<br/><small>pausa las tareas dependientes</small>"]:::ia
PR -- "nueva información" --> B
E -- "sí" --> F{"Riesgo según reglas fijas"}:::dec
F -- "alto, dudoso o excepción" --> ESC["ESCALAR<br/><small>revisa una persona identificada</small>"]:::pe
F -- "dentro de política" --> CO["CONTINUAR<br/><small>crea el plan y las tareas</small>"]:::ok
ESC -- "autoriza" --> CO
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

1. Recepción con identidad y cliente.
2. Normalización: separa hechos, supuestos y preguntas. El usuario puede corregirla.
3. Detección de límites: alcance, política, datos sensibles, conflicto de interés.
4. Clasificación con razones y campos desconocidos marcados.
5. Suficiencia: ¿hay datos para planificar?
6. Riesgo y autonomía con reglas fijas.
7. Equipo y plan versionado.
8. Supervisión: si cambia algo importante, se pausa y se replanifica.

## Si algo falla

- Cada campo se marca como confirmado, inferido o desconocido. No se usa un umbral tipo "80 % de confianza" sin calibrarlo antes.
- Seguridad, permisos, pagos, comunicaciones externas y efectos irreversibles nunca se habilitan por la puntuación del modelo.

## Qué tiene que existir

- Registro de la decisión con su motivo
- Política de parada por criticidad

## Correcciones respecto al original

- El diagrama original tenía flechas que salían de la misma caja con etiquetas superpuestas. Se rehace con las cinco decisiones con nombre propio, tal como las define el texto.
