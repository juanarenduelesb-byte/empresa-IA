# Protocolo: guardar el conocimiento

Los resultados no se quedan en la conversación con Claude.

| Qué | Dónde | Formato |
|---|---|---|
| Ficha de conocimiento | `knowledge/<departamento>/` | [Plantilla](../plantillas/ficha-conocimiento.md) |
| Fuente nueva | `tools/org_data/fuentes.py`; después, `python3 tools/org_gen.py` | Campos del registro |
| Especialista o proceso | `tools/org_data/`; después, generar | Datos, no Markdown a mano |
| Precedente | `precedents/<tipo>/AAAA-MM-slug.md` | [Plantilla](../../precedents/plantilla-precedente.md) |
| Decisión | `DECISIONS.md` | [Plantilla](../plantillas/entrada-decision.md) |
| Entrega de la oficina | Descargar la nota `.md` y llevarla a su sitio | Con sus enlaces al cerebro |

Después de guardar:
1. Regenera lo generado: `python3 tools/org_gen.py` y `python3 tools/brain_build.py oficina/brain.json`.
2. Pasa las comprobaciones: `python3 -m pytest`.
3. Abre la propuesta de cambios. Todo entra como `draft`.
