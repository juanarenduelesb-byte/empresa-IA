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
