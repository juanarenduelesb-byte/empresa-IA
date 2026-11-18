---
tipo: "habilidad"
id: "facturacion-cobro"
usan: 1
estado: "draft"
tags:
  - "habilidad"
---
<!-- Generado por tools/agentes_gen.py desde tools/org_data/. No editar a mano. -->

# Facturación y cobro

`facturacion-cobro` · **Estado:** draft

**Cuándo se usa:** Al cumplirse un hito facturable y cada semana para los vencimientos.

## Pasos

1. Comprobar que el hito está cumplido y aprobado según el contrato.
2. Preparar la factura con todos los datos obligatorios del Reglamento de facturación y numeración correlativa.
3. Dejarla lista para que un socio la emita (la emisión es una acción externa).
4. Registrar vencimiento y condiciones de pago.
5. Vencimientos de la semana: recordatorio amable al vencer, segundo aviso a los 15 días, escalado a los socios después.

## Resultado

Factura en borrador lista para emitir y tabla de vencimientos con su acción.

## Lista de control

- ¿El hito está cumplido?
- ¿Tiene todos los datos obligatorios?
- ¿Algún recordatorio se envía sin un socio? (no debe)

## Quién la usa

- [Contabilidad y facturación](../../knowledge/agentes/conta.md)
