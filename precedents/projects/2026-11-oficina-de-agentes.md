# Oficina de agentes (artifact)

- **Tipo:** proyecto · **Fecha:** noviembre de 2026 · **Estado:** validated (en uso)
- **Contexto:** queríamos ver cómo trabajaría la organización digital antes de tener código.
- **Qué se hizo:** artifact con escena isométrica, CEO que devuelve un contrato JSON, búsqueda en el cerebro (`oficina/brain.json`), QA con un retrabajo automático, decisiones, rutinas y reuniones. Escrito desde cero inspirándonos en agents-office, cuya licencia no permite copiarlo.
- **Resultado:** demostración funcional y fusionada en main (PR #2).
- **Qué reutilizar:** el contrato del CEO (ver [`encargo.schema.json`](../../integrations/contracts/encargo.schema.json)); el patrón de datos en Python que generan los documentos.
- **Qué no repetir:** dejar la lógica de negocio solo en el navegador. El motor real va en `src/`.
- **Evidencias:** `oficina/`, PR #2 y PR #3.
