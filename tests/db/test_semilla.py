"""Los datos de ejemplo cargan, no se duplican y respetan el aislamiento."""

from sqlalchemy import text

from varios.db.semilla import CLIENTES, _id, cargar
from varios.db.sesion import sesion_de_cliente


def test_semilla_idempotente_y_aislada(base, motor_app):
    cargar(base[0])
    segunda = cargar(base[0])
    assert segunda == {"fuentes": 0, "clientes": 0, "usuarios": 0, "solicitudes": 0}
    for slug, _, usuarios, solicitudes in CLIENTES:
        with sesion_de_cliente(motor_app, _id("cliente", slug)) as s:
            assert s.execute(text("SELECT count(*) FROM solicitud")).scalar() == len(solicitudes)
            assert s.execute(text("SELECT count(*) FROM usuario")).scalar() == len(usuarios)
            assert s.execute(text("SELECT count(*) FROM fuente WHERE cliente_id IS NULL")).scalar() > 0
