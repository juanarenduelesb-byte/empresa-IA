# 14 · Operación y respuesta a incidentes

_Detectar, contener sin borrar pruebas, recuperar y aprender._

**Fuente:** Guía v1.4, diagrama 16 + Marco legal, apartado 10

## En palabras sencillas

Cuando algo raro pasa, primero se aísla para que no vaya a más, sin destruir pruebas. Después se mira a quién afecta y si hay que avisar a alguien por ley (cada norma tiene su reloj). Luego se arregla, se recupera desde una copia limpia y se escribe qué falló para que no vuelva a pasar.

## Diagrama

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Instrument Sans, Helvetica, Arial, sans-serif','fontSize':'15px','primaryColor':'#FFFBF3','primaryBorderColor':'#B9A88A','primaryTextColor':'#22171A','lineColor':'#6A5A55','edgeLabelBackground':'#F6EFE1','clusterBkg':'#FBF6EC','clusterBorder':'#E4D6BC','tertiaryColor':'#FFFFFF'},'flowchart':{'curve':'basis','padding':14,'nodeSpacing':38,'rankSpacing':46}}}%%
flowchart TB
OB["Observabilidad<br/><small>logs, métricas, trazas, costes</small>"]:::re --> DT["Detección<br/><small>alertas, anomalías, umbrales</small>"]:::re
DT --> TR{"Triaje<br/><small>severidad y alcance</small>"}:::dec
TR -- "confirmado" --> CT["Contener<br/><small>revocar, aislar, pausar agente</small>"]:::bad
TR -- "falsa alarma" --> AJ["Ajustar detección"]:::re
CT --> PE["Preservar evidencias<br/><small>logs, copias, cadena de custodia</small>"]:::pe
PE --> NO{"¿Hay que notificar?<br/><small>RGPD 72 h · NIS2 · DORA · contrato</small>"}:::dec
NO --> ER["Erradicar causa<br/><small>parchear, rotar secretos</small>"]:::re
ER --> RC["Recuperar<br/><small>desde copia limpia y probada</small>"]:::ok
RC --> PM["Post-mortem<br/><small>causa, acciones, responsable</small>"]:::pe
PM --> PP["Pruebas periódicas<br/><small>restauración, permisos, continuidad</small>"]:::re
PP -. "mejoras" .-> OB
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

1. Registrar la hora de detección y nombrar responsable.
2. Contener sin destruir evidencias.
3. Preservar registros y copias.
4. Determinar sistemas, clientes, datos y periodo afectados.
5. Activar privacidad y legal; evaluar cada régimen por separado.
6. Erradicar la causa.
7. Recuperar desde una copia limpia.
8. Comunicar con veracidad.
9. Informe posterior con acciones y responsables.

## Si algo falla

- Crítica: fuga entre clientes, ransomware, toma de control. Activar crisis.
- Alta: acceso no autorizado limitado o proveedor comprometido.
- Media: error de permisos sin explotación.
- Baja: evento bloqueado sin impacto.

## Qué tiene que existir

- Runbooks
- Matriz de relojes de notificación por norma y cliente
- Registro de incidentes

## Correcciones respecto al original

- El original no mostraba la preservación de evidencias ni la evaluación de notificaciones legales, que el Marco legal sí exige. Añadidas.
