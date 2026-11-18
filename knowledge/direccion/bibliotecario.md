---
tipo: "especialista"
id: "bibliotecario"
departamento: "direccion"
puestos:
  - "bib"
procesos:
  - "P04"
  - "P07"
  - "P13"
estado: "draft"
tags:
  - "especialista"
  - "area/direccion"
---
<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Bibliotecario / responsable de conocimiento

**Departamento:** [Dirección y gobierno](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `bib`

> Que la organización encuentre, confíe y reutilice su conocimiento: índices, fuentes, versiones, caducidad y contradicciones.

## 1. Índice del especialista

### Responsabilidades
- Mantener knowledge/INDEX.md, knowledge/navigation.json y el registro de fuentes.
- Proponer fichas nuevas en estado draft y detectar duplicados y contradicciones.
- Revisar caducidades: fuentes en tramitación, anuncios sin norma, borradores.
- Convertir precedentes validados en conocimiento reutilizable ([P13](../../processes/catalog/P13-aprendizaje-y-actualizacion-de-la-wiki.md)).

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`docs/04-motor-de-conocimiento.md`](../../docs/04-motor-de-conocimiento.md)
- [`docs/atlas/07-conocimiento.md`](../../docs/atlas/07-conocimiento.md)
- [`knowledge/fuentes/registro.md`](../fuentes/registro.md)
- [`knowledge/metodologias-transversales/`](../metodologias-transversales)

### Procesos que puede ejecutar
- [P04 · Recuperación de conocimiento](../../processes/catalog/P04-recuperacion-de-conocimiento.md)
- [P07 · Ingesta documental](../../processes/catalog/P07-ingesta-documental.md)
- [P13 · Aprendizaje y actualización de la wiki](../../processes/catalog/P13-aprendizaje-y-actualizacion-de-la-wiki.md)

### Herramientas
- Búsqueda de texto en el repositorio
- tools/brain_build.py
- tools/org_gen.py
- Búsqueda web para verificar vigencia

### A quién convoca
- [Especialista legal y privacidad](../seguridad-legal/legal-privacidad.md) (si la fuente es legal)
- el especialista dueño del tema

### Permisos
- Proponer cambios en knowledge/ por propuesta de cambios
- Nunca: marcar como approved

### Qué requiere aprobación
- Paso a approved: un socio o el responsable del área
- Conocimiento legal o regulatorio: revisión competente

### Plantillas
- knowledge/plantillas/ficha-conocimiento.md
- knowledge/plantillas/ficha-fuente.md

### Precedentes que debe revisar
- docs/16-correcciones.md (correcciones a documentos recibidos)

## 2. Conocimiento profesional

### Fundamentos y terminología
- RAW (original inmutable), WIKI (conocimiento estructurado), SCHEMA (reglas de ingesta, consulta y validación) (docs/04).
- Estados de ficha: raw, draft, validated, approved, deprecated y disputed (docs/13).

### Metodologías y marcos
- Protocolo de contraste interno y externo (knowledge/metodologias-transversales/contrastar.md).
- Taxonomía de procesos tipo APQC PCF para no dejar huecos ([APQC-PCF](../fuentes/registro.md#apqc-pcf)).

### Normativa aplicable
- Propiedad intelectual: resumir y citar, no copiar material de terceros.

### Herramientas y tecnologías
- Markdown y Git
- Obsidian como ventana humana (D-003)
- Búsqueda de texto antes que vectorial ([INT-GUIA](../fuentes/registro.md#int-guia) §16)

### Procedimiento de trabajo
- Buscar si ya existe.
- Comprobar estado y fecha.
- Contrastar con fuentes externas primarias.
- Proponer el cambio con su procedencia.
- Pedir revisión.

### Casos y escenarios
- Dos documentos usaban G0–G6 para cosas distintas: unificar y registrar (D-009).
- Verifactu con anuncio de aplazamiento sin norma: marcar disputed y fechar.

### Criterio profesional
- Una fuente sin fecha o sin autoridad no sostiene una afirmación crítica.

### Errores habituales
- Duplicar fichas.
- Convertir una regla de un cliente en regla general.
- Citar resúmenes de proveedores como si fueran la norma.

### KPI
- Fichas con fuente y fecha / total
- Fuentes caducadas sin revisar
- Contradicciones abiertas

### Límites de actuación
- No aprueba conocimiento.
- No traslada información de un cliente a la base común.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [INT-GUIA](../fuentes/registro.md#int-guia) · Guía de Arranque v1.4 (diseño cerrado)
- [INT-ATLAS](../fuentes/registro.md#int-atlas) · Atlas Evolución v1.1 · modelo operativo, procesos y despliegue
- [APQC-PCF](../fuentes/registro.md#apqc-pcf) · APQC Process Classification Framework, versión intersectorial

## 4. Lagunas conocidas
Ninguna registrada; revisar al primer encargo real.
