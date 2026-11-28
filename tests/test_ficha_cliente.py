"""B3: la ficha de cliente tiene esquema al día, el ejemplo es válido y no admite datos personales."""

import json
import re
from pathlib import Path

import pytest
from pydantic import ValidationError

from varios.clientes.ficha import ESQUEMA, FichaCliente, Interlocutor

RAIZ = Path(__file__).resolve().parents[1]
EJEMPLO = RAIZ / "knowledge" / "plantillas" / "ejemplos" / "ficha-cliente-atalaya.json"


def test_esquema_al_dia():
    assert json.loads(ESQUEMA.read_text(encoding="utf-8")) == FichaCliente.model_json_schema()


def test_el_ejemplo_es_valido_y_ficticio():
    f = FichaCliente(**json.loads(EJEMPLO.read_text(encoding="utf-8")))
    assert f.ficticio and f.nivel_datos == "L0"


def test_no_hay_campos_para_datos_personales():
    with pytest.raises(ValidationError):
        Interlocutor(rol="Gerente", nombre="Alguien", correo="x@y.z")


def test_el_ejemplo_no_lleva_correos_ni_telefonos():
    t = EJEMPLO.read_text(encoding="utf-8")
    assert not re.search(r"[\w.]+@[\w.]+\.\w+|\b\d{9}\b", t)


def test_todo_dato_dice_de_donde_sale():
    f = FichaCliente(**json.loads(EJEMPLO.read_text(encoding="utf-8")))
    for p in f.procesos:
        for d in (p.volumen_mes, p.tiempo_activo_min, p.tiempo_total, p.retrabajo):
            assert d is None or (d.base and d.fuente)


@pytest.mark.parametrize("texto", ["Gerente (gerente@correduria-inventada.es)", "Gerente, móvil 612 345 678",
                                   "Tramitadora +34 912345678", "Responsable con DNI 12345678Z", "NIE X1234567L"])
def test_ningun_texto_de_la_ficha_admite_correos_telefonos_ni_dni(texto):
    """Repaso del 28/11: antes solo se miraba el archivo de ejemplo; el modelo admitía «Gerente, móvil 612…»."""
    with pytest.raises(ValidationError, match="datos personales"):
        Interlocutor(rol=texto)


def test_las_cifras_corrientes_no_parecen_datos_personales():
    f = FichaCliente(**json.loads(EJEMPLO.read_text(encoding="utf-8")))
    resto = {k: v for k, v in f.interlocutores[0].model_dump().items() if k != "rol"}
    assert Interlocutor(rol="Gerente; 1.200 pólizas y 2026", **resto)
