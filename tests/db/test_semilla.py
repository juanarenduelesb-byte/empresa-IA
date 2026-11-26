"""Los datos de ejemplo cargan, no se duplican y respetan el aislamiento."""

from sqlalchemy import text

from varios.db.semilla import _id, cargar
from varios.db.sesion import sesion_de_cliente


def test_semilla_idempotente_y_aislada(base, motor_app):
    primera = cargar(base[0])
    segunda = cargar(base[0])
    assert primera["clientes"] == 2 and primera["fuentes"] > 0
    assert segunda == {"fuentes": 0, "clientes": 0, "usuarios": 0, "solicitudes": 0}
    with sesion_de_cliente(motor_app, _id("cliente", "senuelo")) as s:
        assert s.execute(text("SELECT count(*) FROM solicitud")).scalar() == 1
        assert s.execute(text("SELECT count(*) FROM fuente")).scalar() >= primera["fuentes"]
