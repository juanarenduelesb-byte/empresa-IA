# 01 · Organización: modelo matricial

_Dos ejes que se combinan por proyecto, más las personas que responden del resultado._

**Fuente:** Guía v1.4, diagrama 2 + Atlas Evolución v1.1, apartados 4 y 4.1

## En palabras sencillas

No hay un robot para cada combinación. Hay departamentos que sirven para cualquier sector y especialistas de sector que se llaman cuando hace falta. Para cada cliente se forma un equipo a medida. Y siempre hay personas que responden: el responsable del despliegue y el ingeniero que trabaja con el cliente.

## Diagrama

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Instrument Sans, Helvetica, Arial, sans-serif','fontSize':'15px','primaryColor':'#FFFBF3','primaryBorderColor':'#B9A88A','primaryTextColor':'#22171A','lineColor':'#6A5A55','edgeLabelBackground':'#F6EFE1','clusterBkg':'#FBF6EC','clusterBorder':'#E4D6BC','tertiaryColor':'#FFFFFF'},'flowchart':{'curve':'basis','padding':14,'nodeSpacing':38,'rankSpacing':46}}}%%
flowchart TB
CEO["CEO digital<br/><small>prioriza y asigna</small>"]:::core
CEO --> F["Eje funcional<br/><small>Legal y privacidad · Finanzas · Comercial · Operaciones<br/>Tecnología · Datos e IA · Ciberseguridad · PMO · Calidad · RR. HH.</small>"]:::re
CEO --> S["Eje sectorial<br/><small>Seguros y peritaje · Banca · Salud · Construcción · Industria<br/>Logística · Retail · Inmobiliario · Servicios profesionales</small>"]:::ia
F --> EQ["Equipo de proyecto a medida<br/><small>solo las capacidades necesarias</small>"]:::dec
S --> EQ
subgraph H["Personas que responden"]
  direction LR
  DL["Responsable del despliegue<br/><small>resultado, alcance, riesgos, ROI</small>"]:::pe
  FDE["Ingeniero desplegado<br/><small>integra y construye con el cliente</small>"]:::pe
  PA["Arquitecto de procesos<br/><small>AS-IS, TO-BE, reglas, métricas</small>"]:::pe
end
EQ --> H
EQ --> EX["Ejemplo: siniestros<br/><small>Seguros + Operaciones + Tecnología + Datos e IA + Legal + Calidad</small>"]:::ok
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

1. El CEO identifica qué funciones y qué sector necesita el encargo.
2. Se combinan solo esas capacidades en un equipo de proyecto.
3. Una persona (responsable del despliegue) responde del resultado. La responsabilidad final nunca se delega en la IA.

## Si algo falla

- Si falta una capacidad, se deriva a un profesional externo en lugar de improvisarla.
- Un paquete sectorial no se lanza hasta tener un cliente con datos autorizados y una métrica de valor.

## Qué tiene que existir

- Catálogo de capacidades con responsable, versión, permisos y coste
- Equipo y responsables de cada proyecto (matriz RACI)

## Correcciones respecto al original

- El Atlas de Evolución pedía añadir al mapa de organización el responsable del despliegue, el ingeniero desplegado y el arquitecto de procesos. No estaba hecho; ahora sí.
