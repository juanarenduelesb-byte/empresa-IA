# 08 · Seguridad, identidad y aislamiento de clientes

_La autorización ocurre en el servidor. No se confía en instrucciones a la IA, carpetas ni filtros de pantalla._

**Fuente:** Atlas · Mapa 5 + Guía v1.4, diagrama 6 y Anexo III apartado 7

## En palabras sencillas

Cada petición lleva una identidad verificada. De ella sale de qué cliente es y qué puede ver, y eso no lo puede cambiar ni el usuario ni la IA. Con ese pase se consulta la base de datos, los archivos y las herramientas. A la IA le llega solo lo mínimo. Todo acceso, y todo intento denegado, queda registrado.

## Diagrama

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontFamily':'Instrument Sans, Helvetica, Arial, sans-serif','fontSize':'15px','primaryColor':'#FFFBF3','primaryBorderColor':'#B9A88A','primaryTextColor':'#22171A','lineColor':'#6A5A55','edgeLabelBackground':'#F6EFE1','clusterBkg':'#FBF6EC','clusterBorder':'#E4D6BC','tertiaryColor':'#FFFFFF'},'flowchart':{'curve':'basis','padding':14,'nodeSpacing':38,'rankSpacing':46}}}%%
flowchart TB
ID["Identidad<br/><small>usuario, servicio o agente · doble factor</small>"]:::re --> AU["Autenticación<br/><small>sesión, token, caducidad</small>"]:::re
AU --> AZ["Autorización<br/><small>rol + cliente + proyecto</small>"]:::dec
AZ --> CTX["Contexto de seguridad<br/><small>cliente, proyecto, rol, finalidad · no se puede cambiar</small>"]:::core
CTX --> PEF{"Aplicación de políticas<br/>en el servidor"}:::dec
PEF -- "lectura o escritura" --> DAL["Capa de acceso a datos<br/><small>consultas filtradas</small>"]:::re
DAL --> DB[("PostgreSQL con RLS<br/><small>segunda barrera</small>")]:::re
DAL --> OS[("Almacenamiento privado<br/><small>enlaces temporales</small>")]:::re
PEF -- "contexto para la IA" --> MG["Puerta de contexto del modelo<br/><small>minimizar y ocultar datos</small>"]:::ia
PEF -- "acción" --> TP["Permisos de herramientas<br/><small>lista cerrada y sandbox</small>"]:::dec
PEF -- "sin cliente resuelto" --> DENY["Denegar por defecto"]:::bad
DB -.-> AUD[("Auditoría y alertas<br/><small>accesos, exportaciones, denegaciones</small>")]:::re
OS -.-> AUD
TP -.-> AUD
AUD -- "alerta" --> IR["Respuesta a incidentes"]:::bad
subgraph T["Lo que ve cada uno"]
  direction LR
  CO["Corporativo<br/><small>conocimiento común aprobado</small>"]:::ok
  CA["Cliente A<br/><small>aislado</small>"]:::ia
  CB["Cliente B<br/><small>aislado</small>"]:::ia
end
DB --- T
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

1. Autenticar usuario o servicio.
2. Resolver cliente y permisos desde la identidad.
3. Construir un contexto de seguridad que no se puede modificar.
4. Autorizar cada lectura, escritura, exportación y herramienta.
5. RLS y controles de almacenamiento como segunda barrera.
6. Minimizar el contexto antes de enviarlo a un modelo externo.
7. Registrar accesos y denegaciones sin volcar secretos.
8. Detectar y gestionar incidentes.

## Si algo falla

- Cliente no resuelto: denegar por defecto.
- Token caducado: rechazar y volver a autenticar.
- RLS mal configurada: no se despliega hasta pasar las pruebas.
- Fuga o acceso cruzado: revocar, contener, preservar evidencias.
- Proveedor o modelo no aprobado: no se le envían datos confidenciales.

## Qué tiene que existir

- Modelo de amenazas
- Matriz de acceso
- Políticas RLS y pruebas negativas
- Inventario de datos y proveedores
- Plan de respuesta a incidentes

## Prueba de aceptación

Prueba de aceptación: dos clientes de prueba con datos señuelo únicos. Se intenta leer, buscar, exportar y usar herramientas de uno desde el otro. Cualquier fuga bloquea el lanzamiento.

## Correcciones respecto al original

- El original tenía cinco flechas diagonales que salían del mismo punto y se cruzaban sobre "PostgreSQL RLS", con etiquetas ilegibles como "archivo" y "tool scope" superpuestas. Se reorganiza en un árbol de decisión.
