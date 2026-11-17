# 07 · Motor de conocimiento con Obsidian

_Cómo entra un documento, cómo se convierte en conocimiento aprobado y cómo se consulta con permisos._

**Fuente:** Atlas · Mapa 3 + Guía v1.4, diagrama 5 y Anexo III apartado 6

## En palabras sencillas

Arriba, el camino de entrada: el documento pasa por una aduana, se guarda el original intacto y la IA propone fichas que una persona aprueba. Abajo, el camino de consulta: antes de buscar se comprueban los permisos, y la respuesta siempre dice de dónde sale.

## Diagrama

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Instrument Sans, Helvetica, Arial, sans-serif','fontSize':'15px','primaryColor':'#FFFBF3','primaryBorderColor':'#B9A88A','primaryTextColor':'#22171A','lineColor':'#6A5A55','edgeLabelBackground':'#F6EFE1','clusterBkg':'#FBF6EC','clusterBorder':'#E4D6BC','tertiaryColor':'#FFFFFF'},'flowchart':{'curve':'basis','padding':14,'nodeSpacing':38,'rankSpacing':46}}}%%
flowchart TB
subgraph IN["Entrada"]
  direction TB
  F["Fuentes<br/><small>PDF, Word, Excel, web autorizada</small>"]:::re --> CU["Cuarentena<br/><small>huella, malware, tipo, permisos</small>"]:::dec
  CU --> RAW[("RAW<br/><small>original intacto y versionado</small>")]:::re
  CU --> EX["Extraer texto y metadatos"]:::re
  EX --> PR["Proponer fichas<br/><small>con citas a la fuente</small>"]:::ia
  PR --> LI["Revisión automática<br/><small>campos, enlaces, duplicados</small>"]:::re
  LI --> HU{"Revisión humana<br/>según sensibilidad"}:::pe
  HU -- "aprobada" --> WI["Wiki en Markdown<br/><small>Obsidian + Git</small>"]:::ok
  HU -- "contradice otra fuente" --> DI["En disputa<br/><small>se muestran ambas</small>"]:::dec
  HU -- "rechazada" --> DESC["Se descarta"]:::bad
end
subgraph OUT["Consulta"]
  direction TB
  CEO["CEO o agente"]:::core --> API["API de consulta"]:::ia
  API --> PERM{"¿Permisos?<br/><small>identidad, cliente, proyecto</small>"}:::dec
  PERM -- "no" --> NO["Denegar"]:::bad
  PERM -- "sí" --> IDX["Índice de búsqueda<br/><small>texto primero; semántica si compensa</small>"]:::re
  IDX --> RES["Fragmentos con cita<br/><small>fuente, versión, fecha</small>"]:::ok
  RES --> CEO
end
WI --> IDX
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

1. Recibir el documento en cuarentena.
2. Calcular huella, analizar tipo, malware y permisos.
3. Extraer texto y metadatos sin perder el vínculo al original.
4. Proponer fichas en Markdown con citas.
5. Revisión automática: campos obligatorios, enlaces, duplicados.
6. Revisión humana según sensibilidad.
7. Publicar en la wiki y versionar en Git si la clasificación lo permite.
8. Indexar solo lo autorizado.
9. Recuperar fragmentos con referencias.
10. Tras cada proyecto, proponer mejoras; nunca autoaprobarlas.

## Si algo falla

- Extracción incompleta: calidad baja y revisión manual.
- Fuentes contradictorias: estado en disputa.
- Fuente obsoleta: deprecada, sin borrar la evidencia histórica.
- Sin permiso: se deniega aunque exista en el índice.
- Datos confidenciales de un cliente: nunca en la wiki común.

## Qué tiene que existir

- Plantillas Markdown y metadatos
- Política de clasificación y estados
- Proceso de ingesta y revisión
- Índice y política de recuperación
- Registro de procedencia

## Correcciones respecto al original

- La flecha "conserva original" cruzaba en diagonal por encima de tres cajas, y las de "indexa" y "versiona" se cortaban. Se separa en dos caminos, entrada y consulta, que no se cruzan.
