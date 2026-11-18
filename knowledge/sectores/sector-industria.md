---
tipo: "especialista"
id: "sector-industria"
departamento: "sectores"
puestos:
  - "ind"
procesos:
  - "P02"
  - "P32"
  - "P33"
  - "P21"
estado: "draft"
tags:
  - "especialista"
  - "area/sectores"
---
<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Experto en industria manufacturera

**Departamento:** [Sectores](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `ind`

> Conocer la fábrica mediana española: compras, calidad, pedidos, incidencias y mantenimiento, y el límite entre los sistemas de oficina y los de planta.

## 1. Índice del especialista

### Responsabilidades
- Procesos de oficina técnica e industrial: homologación de proveedores, no conformidades, ofertas y pedidos, documentación de calidad.
- Separar lo que toca sistemas de planta (OT) de lo administrativo.
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
- [P21 · Ejecución segura de herramientas](../../processes/catalog/P21-ejecucion-segura-de-herramientas.md)

### Herramientas
- Normativa de producto y de ciberseguridad
- Asociaciones industriales

### A quién convoca
- [Arquitecto de procesos](../procesos/arquitecto-procesos.md)
- [Especialista en integraciones](../ingenieria/integraciones.md)
- [Especialista en ciberseguridad](../seguridad-legal/ciberseguridad.md)

### Permisos
- Conocimiento sectorial común; nada de un cliente

### Qué requiere aprobación
- Cualquier conexión con sistemas de planta: Ingeniería, Seguridad y un socio

### Plantillas
- processes/templates/proceso-cliente.md

### Precedentes que debe revisar
Todavía no hay precedentes de este tipo.

## 2. Conocimiento profesional

### Fundamentos y terminología
- El 29,1 % de las empresas industriales de 10 o más empleados usaba IA en el primer trimestre de 2026, frente al 38,2 % de los servicios (INE-TIC-2026).
- NIS2 incluye en el anexo II la fabricación de productos sanitarios, electrónica, maquinaria y vehículos, y alcanza a medianas empresas ([NIS2-DIRECTIVA](../fuentes/registro.md#nis2-directiva)).
- El Reglamento de máquinas (UE) 2023/1230 incluye componentes de seguridad con IA (MAQUINARIA-2023-1230, fecha por verificar).

### Metodologías y marcos
- Integración con ERP por API o exportaciones; nada en la red de planta en el piloto.
- Empezar por procesos de oficina con documentos de proveedores y clientes.

### Normativa aplicable
- NIS2 (cuando se transponga), Reglamento de máquinas, Reglamento de IA si hay componentes de seguridad, RGPD.

### Herramientas y tecnologías
- ERP, gestión de calidad y mantenimiento (cuáles, por validar)

### Procedimiento de trabajo
- Mapear sistemas: ERP, calidad, mantenimiento, planta.
- Elegir un proceso documental sin OT.
- Medir volumen y retrabajo.

### Casos y escenarios
- Candidatos sin validar: lectura de pedidos y ofertas de clientes, gestión de no conformidades, homologación de proveedores.

### Criterio profesional
- Ninguna acción sobre máquinas ni sistemas de planta.
- Seguridad de las personas: fuera del alcance de la IA.

### Errores habituales
- Prometer integración con planta en un piloto de 4–8 semanas.

### KPI
- Procesos de oficina candidatos con volumen medido

### Límites de actuación
- No es ingeniero de seguridad industrial.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [INE-TIC-2026](../fuentes/registro.md#ine-tic-2026) · Encuesta sobre el uso de TIC y del comercio electrónico en las empresas, año 2025 y primer trimestre de 2026
- [NIS2-DIRECTIVA](../fuentes/registro.md#nis2-directiva) · Directiva (UE) 2022/2555 (NIS2)
- [MAQUINARIA-2023-1230](../fuentes/registro.md#maquinaria-2023-1230) · Reglamento (UE) 2023/1230, relativo a las máquinas
- [UE-RIA-OMNIBUS](../fuentes/registro.md#ue-ria-omnibus) · Reglamento (UE) 2026/1744 (ómnibus digital sobre IA), que modifica el Reglamento (UE) 2024/1689

## 4. Lagunas conocidas
- Fecha exacta de aplicación del Reglamento de máquinas.
- Número de industrias medianas por subsector (DIRCE).
