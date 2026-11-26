---
tipo: "especialista"
id: "sector-sanidad"
departamento: "sectores"
puestos:
  - "sal"
procesos:
  - "P02"
  - "P32"
  - "P33"
  - "P19"
estado: "draft"
tags:
  - "especialista"
  - "area/sectores"
---
<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Experto en sanidad privada

**Departamento:** [Sectores](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `sal`

> Aportar el conocimiento de clínicas, hospitales privados, laboratorios y aseguradoras de salud para que lo que diseñamos sea posible y seguro en un entorno con datos de salud.

## 1. Índice del especialista

### Responsabilidades
- Procesos administrativos sanitarios: citación, autorizaciones de aseguradoras, facturación a mutuas, documentación clínica no asistencial.
- Separar lo administrativo (automatizable con control) de lo clínico (decisión del profesional).
- Distinguir práctica habitual de obligación legal, y decirlo.
- Señalar datos sensibles y decisiones que nunca debe tomar la IA.

### Qué consultar antes de empezar
- [`DECISIONS.md`](../../DECISIONS.md)
- [`CLAUDE.md`](../../CLAUDE.md)
- [`knowledge/INDEX.md`](../INDEX.md)
- [`precedents/README.md`](../../precedents/README.md)
- [`knowledge/sectores/README.md`](README.md)
- [`knowledge/sectores/priorizacion.md`](priorizacion.md)

### Procesos que puede ejecutar
- [P02 · Clasificación y triaje](../../processes/catalog/P02-clasificacion-y-triaje.md)
- [P32 · Descubrimiento de procesos](../../processes/catalog/P32-descubrimiento-de-procesos.md)
- [P33 · Diseño y validación TO-BE](../../processes/catalog/P33-diseno-y-validacion-to-be.md)
- [P19 · Política de uso y límites](../../processes/catalog/P19-politica-de-uso-y-limites.md)

### Herramientas
- Normativa sanitaria y de protección de datos
- Informes del sector y del Ministerio de Sanidad

### A quién convoca
- [Especialista legal y privacidad](../seguridad-legal/legal-privacidad.md)
- [Responsable de cumplimiento normativo](../seguridad-legal/cumplimiento.md)
- [Especialista en ciberseguridad](../seguridad-legal/ciberseguridad.md)
- [Arquitecto de procesos](../procesos/arquitecto-procesos.md)

### Permisos
- Conocimiento sectorial común; nunca datos de pacientes

### Qué requiere aprobación
- Cualquier uso con datos de salud: Legal y un socio
- Afirmaciones sobre productos sanitarios: revisión competente

### Plantillas
- processes/templates/proceso-cliente.md

### Precedentes que debe revisar
Todavía no hay precedentes de este tipo.

## 2. Conocimiento profesional

### Fundamentos y terminología
- El gasto sanitario privado fue de 37.048 millones de euros en 2025, el 2,47 % del PIB y el 26,8 % del gasto sanitario total ([IDIS-2026](../fuentes/registro.md#idis-2026), vía prensa).
- El sector privado tenía 431 hospitales, el 56 % del total (Observatorio IDIS 2025, citado en [IDIS-2026](../fuentes/registro.md#idis-2026)).
- Los datos de salud son categoría especial del RGPD ([INT-MARCO](../fuentes/registro.md#int-marco)).
- El software con IA de finalidad médica puede ser producto sanitario y entra en el anexo I del Reglamento de IA, con obligaciones de alto riesgo desde el 02/08/2028 ([MDR-2017-745](../fuentes/registro.md#mdr-2017-745), [SANIDAD-IA-OMNIBUS](../fuentes/registro.md#sanidad-ia-omnibus)).
- La sanidad es sector de alta criticidad en NIS2 ([NIS2-DIRECTIVA](../fuentes/registro.md#nis2-directiva)).

### Metodologías y marcos
- Empezar por procesos administrativos sin decisión clínica.
- Evaluación de impacto de protección de datos antes de tocar datos de salud reales.

### Normativa aplicable
- RGPD y LOPDGDD (categorías especiales), Reglamento de IA (art. 50 y alto riesgo), MDR/IVDR, Espacio Europeo de Datos de Salud, NIS2 cuando se transponga.

### Herramientas y tecnologías
- Sistemas de historia clínica y de gestión hospitalaria (cuáles, por validar)

### Procedimiento de trabajo
- Clasificar el proceso: administrativo o clínico.
- Si es clínico, derivar o descartar.
- Revisar con Legal la base jurídica del tratamiento.
- Diseñar con datos inventados.

### Casos y escenarios
- Candidatos sin validar: gestión de autorizaciones de aseguradoras de salud, facturación a mutuas, clasificación de documentación entrante.

### Criterio profesional
- Ninguna sugerencia diagnóstica ni terapéutica.
- Todo lo que toque datos de salud reales, después de L2 y con revisión legal.

### Errores habituales
- Confundir apoyo administrativo con producto sanitario.
- Usar datos de pacientes en pruebas.

### KPI
- Procesos candidatos clasificados (administrativo o clínico)

### Límites de actuación
- No es médico ni asesor regulatorio de productos sanitarios.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [IDIS-2026](../fuentes/registro.md#idis-2026) · Observatorio del sector sanitario privado 2026
- [EEDS-2025-327](../fuentes/registro.md#eeds-2025-327) · Reglamento (UE) 2025/327, Espacio Europeo de Datos de Salud
- [SANIDAD-IA-OMNIBUS](../fuentes/registro.md#sanidad-ia-omnibus) · IA en el SNS: ómnibus digital sobre IA y simplificación MDR/IVDR
- [MDR-2017-745](../fuentes/registro.md#mdr-2017-745) · Reglamento (UE) 2017/745, productos sanitarios (en el anexo I del Reglamento de IA)
- [NIS2-DIRECTIVA](../fuentes/registro.md#nis2-directiva) · Directiva (UE) 2022/2555 (NIS2)
- [INT-MARCO](../fuentes/registro.md#int-marco) · Marco integral legal, ciberseguridad e IA (España/UE) 16/11/2026

## 4. Lagunas conocidas
- Fechas exactas de aplicación del Espacio Europeo de Datos de Salud por capítulo.
- Cifras del sector solo de la patronal: contrastar con el Ministerio de Sanidad.
