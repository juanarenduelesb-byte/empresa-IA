# 00 · Arquitectura del cerebro digital

_Las capas del sistema, de arriba (personas) a abajo (datos), con la seguridad cruzándolo todo._

**Fuente:** Imagen de WhatsApp del 16/11/2026 + Atlas Evolución v1.1, apartado 2

## En palabras sencillas

Piensa en un edificio de cuatro plantas. Arriba trabajan las personas. Debajo está la dirección (el CEO digital), que entiende el encargo y lo reparte. El motor de procesos lleva el control de cada tarea. Los departamentos hacen el trabajo y solo tocan los programas del cliente a través de una puerta vigilada. En el sótano están los datos y el conocimiento. La seguridad atraviesa todas las plantas.

## Diagrama

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Instrument Sans, Helvetica, Arial, sans-serif','fontSize':'15px','primaryColor':'#FFFBF3','primaryBorderColor':'#B9A88A','primaryTextColor':'#22171A','lineColor':'#6A5A55','edgeLabelBackground':'#F6EFE1','clusterBkg':'#FBF6EC','clusterBorder':'#E4D6BC','tertiaryColor':'#FFFFFF'},'flowchart':{'curve':'basis','padding':14,'nodeSpacing':38,'rankSpacing':46}}}%%
flowchart TB
U["Personas<br/><small>piden, revisan y aprueban</small>"]:::pe
U --> CEO["CEO digital<br/><small>entiende, clasifica, planifica, reparte</small>"]:::core
U -. "leen y editan" .-> OB["Obsidian<br/><small>ventana al conocimiento</small>"]:::re
OB -. "versiona" .-> GIT[("GitHub privado<br/><small>wiki no confidencial y código</small>")]:::re
CEO <-- "consulta con permisos" --> KAPI["API de conocimiento<br/><small>permisos antes de buscar</small>"]:::ia
KAPI --> IDX["Índice de búsqueda"]:::re
KAPI --> RAW[("Originales RAW<br/><small>evidencias y versiones</small>")]:::re
CEO --> PD["Descubrimiento de procesos<br/><small>AS-IS, excepciones, KPI, TO-BE</small>"]:::ia
CEO --> PE["Motor de procesos<br/><small>estados, reglas, plazos, aprobaciones</small>"]:::core
PD --> PE
PE --> PG[("PostgreSQL<br/><small>estados, permisos, auditoría</small>")]:::re
PE --> OI["Inteligencia operativa<br/><small>tiempo, coste, errores, ROI</small>"]:::ia
PE --> CAP["Departamentos + especialistas de sector"]:::re
CAP --> HUB["Centro de integraciones<br/>y puerta de herramientas"]:::dec
HUB --> SYS["Sistemas del cliente<br/><small>CRM, ERP, correo, gestor</small>"]:::re
CAP --> QA["Calidad y aprobaciones"]:::pe
QA --> OUT["Entrega con evidencias"]:::ok
OUT ~~~ SEC["Seguridad y gobierno en todas las capas<br/><small>aislamiento por cliente · permisos · secretos · cifrado · registros · copias · supervisión humana</small>"]:::wine
SYS ~~~ SEC
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

1. La petición entra por las personas o por un canal.
2. El CEO la entiende y decide: si hace falta, primero se descubre el proceso real.
3. El motor de procesos ejecuta las tareas con reglas y plazos.
4. Los departamentos trabajan y solo tocan sistemas del cliente a través de la puerta de herramientas.
5. Calidad y personas revisan antes de entregar.
6. Todo lo que pasa queda en PostgreSQL; el conocimiento validado, en la wiki.

## Si algo falla

- Si el conocimiento no tiene permiso, no se recupera, aunque exista.
- Obsidian no es la base de datos ni el sistema de permisos: solo es la ventana para leer y escribir.

## Qué tiene que existir

- Mapa de módulos con responsables
- Lista de qué vive en PostgreSQL, qué en Git y qué en almacenamiento privado

## Correcciones respecto al original

- El original tenía texto que se salía de las cajas y una flecha larga que cruzaba todo el dibujo. Ahora cada flecha va de una caja a la siguiente.
- Se añaden los módulos que pide el Atlas de Evolución: descubrimiento de procesos, motor de procesos, centro de integraciones e inteligencia operativa.
