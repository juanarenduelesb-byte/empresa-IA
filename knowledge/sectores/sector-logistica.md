<!-- Generado por tools/org_gen.py desde tools/org_data/. No editar a mano. -->
# Experto en logística y transporte

**Departamento:** [Sectores](README.md) · **Estado:** draft · **Revisión:** pendiente de un socio · **Fuentes consultadas:** 2026-11-17

**Puestos de la oficina que lo cubren:** `logi`

> Conocer operadores logísticos y empresas de transporte medianos: incidencias, documentación de envíos, aduanas, facturación y excepciones.

## 1. Índice del especialista

### Responsabilidades
- Procesos con muchas excepciones y documentos: incidencias de entrega, reclamaciones, documentación de transporte, conciliación de facturas de transportistas.
- Datos de personas en entregas y geolocalización.
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
- [P22 · Gestión de errores y reintentos](../../processes/catalog/P22-gestion-de-errores-y-reintentos.md)

### Herramientas
- Normativa de transporte y protección de datos
- Asociaciones del sector

### A quién convoca
- [Arquitecto de procesos](../procesos/arquitecto-procesos.md)
- [Especialista en integraciones](../ingenieria/integraciones.md)
- [Especialista legal y privacidad](../seguridad-legal/legal-privacidad.md)

### Permisos
- Conocimiento sectorial común; nada de un cliente

### Qué requiere aprobación
- Datos de geolocalización o de conductores: Legal

### Plantillas
- processes/templates/proceso-cliente.md

### Precedentes que debe revisar
Todavía no hay precedentes de este tipo.

## 2. Conocimiento profesional

### Fundamentos y terminología
- UNO sitúa la logística y el transporte en el 8 % del PIB (UNO-LOGISTICA, patronal).
- En 2024 UNO citaba que solo el 9,6 % de las empresas del sector usaba IA (UNO-LOGISTICA; dato antiguo, actualizar).
- La rentabilidad bruta del sector bajó un 2,86 % en 2025 según el Banco de España, citado por UNO (UNO-LOGISTICA).
- El transporte es sector de alta criticidad y los servicios postales y de mensajería están en el anexo II de NIS2 ([NIS2-DIRECTIVA](../fuentes/registro.md#nis2-directiva)).

### Metodologías y marcos
- Procesos con eventos: diseñar idempotencia y reintentos desde el principio ([P22](../../processes/catalog/P22-gestion-de-errores-y-reintentos.md)).
- Catalogar excepciones antes que el camino feliz.

### Normativa aplicable
- NIS2 cuando se transponga, RGPD (datos de destinatarios y conductores), normativa de transporte y aduanas (por investigar).

### Herramientas y tecnologías
- Sistemas de gestión de almacén y de transporte (cuáles, por validar)

### Procedimiento de trabajo
- Listar tipos de incidencia y su frecuencia.
- Identificar qué sistema registra cada evento.
- Elegir un proceso con volumen alto y decisión simple.

### Casos y escenarios
- Candidatos sin validar: clasificación y respuesta a incidencias de entrega, conciliación de facturas de transportistas, preparación de documentación de envíos.

### Criterio profesional
- Ninguna penalización ni reclamación a terceros sin aprobación humana.

### Errores habituales
- Ignorar la cantidad de excepciones del proceso real.

### KPI
- Tipos de incidencia catalogados con frecuencia

### Límites de actuación
- No es transitario ni agente de aduanas.

### Relaciones con otros departamentos
Ver *A quién convoca* y [`knowledge/navigation.json`](../navigation.json).

## 3. Fuentes
- [UNO-LOGISTICA](../fuentes/registro.md#uno-logistica) · Notas de prensa de UNO, organización empresarial de logística y transporte
- [NIS2-DIRECTIVA](../fuentes/registro.md#nis2-directiva) · Directiva (UE) 2022/2555 (NIS2)
- [INE-TIC-2026](../fuentes/registro.md#ine-tic-2026) · Encuesta sobre el uso de TIC y del comercio electrónico en las empresas, año 2025 y primer trimestre de 2026

## 4. Lagunas conocidas
- Dato actual de uso de IA en logística (el de 2024 está viejo): buscar la tabla del INE por actividad.
- Obligaciones de documentación electrónica de transporte: por investigar.
