"""I1: los agentes que escriben algo que lee un cliente o el público tienen la identidad como lectura obligatoria.

Repaso del 28/11: Cumplimiento (respuesta a cuestionarios de proveedor) y Arquitecto de procesos (informe AS-IS / TO-BE)
escribían al cliente sin leer la guía de voz, que dice justo lo que no se promete («nunca "cumple el RGPD"»).
"""

import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "tools"))

from org_data.agentes import AGENTES, ESCRIBEN_A_CLIENTES, IDENTIDAD  # noqa: E402

# Entregables que lee el cliente o el público (docs/00: diagnóstico, diseño, piloto, operar; web y publicaciones).
PARA_CLIENTES = ("propuesta", "web", "publicaciones", "demo", "cuestionario", "informe semanal del piloto",
                 "revisión de valor", "informe as-is", "guion de entrevista")


def test_quien_entrega_al_cliente_lee_la_identidad():
    for a in AGENTES:
        textos = " ".join(a["entregables"]).lower()
        if any(p in textos for p in PARA_CLIENTES):
            assert a["id"] in ESCRIBEN_A_CLIENTES, f"{a['id']} entrega al cliente ({textos}) sin leer la identidad"


def test_la_identidad_va_primero_y_existe():
    for ruta in IDENTIDAD:
        assert (RAIZ / ruta).is_file(), ruta
    for a in AGENTES:
        if a["id"] in ESCRIBEN_A_CLIENTES:
            assert a["lectura"][: len(IDENTIDAD)] == IDENTIDAD, a["id"]
