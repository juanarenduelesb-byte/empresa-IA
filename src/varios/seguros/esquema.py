"""Escribe el esquema JSON de los casos de siniestro a partir del modelo Pydantic.

Uso: python -m varios.seguros.esquema
"""

import json

from varios.seguros.apertura import RAIZ, Caso

DESTINO = RAIZ / "processes" / "referencia-seguros-apertura-siniestros" / "casos" / "esquema.json"

if __name__ == "__main__":
    DESTINO.write_text(json.dumps(Caso.model_json_schema(), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(DESTINO.relative_to(RAIZ))
