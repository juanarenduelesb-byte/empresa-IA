# Procesos

Hay dos tipos de proceso. No hay que confundirlos.

| Tipo | Qué es | Dónde |
|---|---|---|
| **Procesos de Varios (P01–P38)** | Cómo funciona la organización digital: recibir, clasificar, planificar, ejecutar, revisar, aprobar, entregar, gobernar | [`catalog/`](catalog/README.md) |
| **Procesos de cliente** | El proceso de negocio que se descubre y automatiza para un cliente (AS-IS y TO-BE) | Una carpeta por proceso; la primera es [`referencia-seguros-apertura-siniestros/`](referencia-seguros-apertura-siniestros/README.md) |

## Carpetas
- [`catalog/`](catalog/README.md): fichas P01–P38 con 20 apartados y diagrama. Generadas por `tools/org_gen.py`.
- [`definitions/`](definitions/README.md): definiciones ejecutables (JSON) que valida el motor.
- [`diagrams/`](diagrams/ciclo-encargo.md): ciclo completo de un encargo y dependencias.
- [`templates/`](templates/proceso-cliente.md): plantilla de proceso de cliente.
- [`tests/`](tests/README.md): plan de pruebas por proceso.
- [`runbooks/`](runbooks/README.md): qué hacer cuando algo falla.
- [`autonomia.json`](autonomia.json): nivel de autonomía A0–A4 de cada proceso, con techo y criterio para subir y bajar ([docs/29](../docs/29-autonomia.md)).

Ningún dato real de clientes en este repositorio.
