"""Banco de pruebas del Control A (S4, tarea C2): 20 encargos normales y 5 trampas.

Modelos simulados, sin red ni coste:
- `ModeloOraculo`: devuelve las señales anotadas en el caso (un extractor perfecto). Prueba las reglas.
- `ModeloIngenuo`: no ve nada y siempre diría «continuar». Prueba que las trampas caen por los detectores fijos.
El adaptador real (Claude) implementará el mismo `Modelo.senales` en S4.

Uso: python -m varios.ceo.banco [oraculo|ingenuo]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from varios.ceo.decision import Encargo, Resultado, Senales, decidir
from varios.procesos.motor import Identidad

RAIZ = Path(__file__).resolve().parents[3]
BANCO = RAIZ / "processes" / "ceo-control-a" / "encargos.json"


def cargar(ruta: Path = BANCO) -> dict:
    return json.loads(ruta.read_text(encoding="utf-8"))


class ModeloOraculo:
    def __init__(self, casos: list[dict]):
        self._s = {c["id"]: Senales(**c["senales"]) for c in casos}

    def senales(self, e: Encargo) -> Senales:
        return self._s[e.id]


class ModeloIngenuo:
    def senales(self, e: Encargo) -> Senales:
        return Senales()


def ejecutar(modelo, datos: dict | None = None) -> list[tuple[dict, Resultado, bool]]:
    datos = datos or cargar()
    ident = Identidad(**datos["identidad"])
    out = []
    for c in datos["encargos"]:
        e = Encargo(id=c["id"], texto=c["texto"], documento=c.get("documento"))
        r = decidir(e, ident, modelo, datos["clientes"])
        out.append((c, r, r.decision in c["esperado"]["aceptables"]))
    return out


def informe(res: list[tuple[dict, Resultado, bool]]) -> str:
    ok = sum(x[2] for x in res)
    tr = [x for x in res if x[0]["tipo"] == "trampa"]
    lineas = [f"Aciertos: {ok}/{len(res)} · trampas que no acaban en CONTINUAR: "
              f"{sum(x[1].decision != 'CONTINUAR' for x in tr)}/{len(tr)}"]
    for c, r, bien in res:
        lineas.append(f"{'ok ' if bien else 'MAL'} {c['id']} esperado {c['esperado']['decision']:<9} "
                      f"obtenido {r.decision:<9} {r.motivo}")
    return "\n".join(lineas)


if __name__ == "__main__":
    datos = cargar()
    modelo = ModeloIngenuo() if sys.argv[1:] == ["ingenuo"] else ModeloOraculo(datos["encargos"])
    print(informe(ejecutar(modelo, datos)))
