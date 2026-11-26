"""Separación entre clientes (plan S3: «el acceso cruzado falla siempre por diseño»)."""

import uuid

import pytest
from sqlalchemy import text
from sqlalchemy.exc import DBAPIError

from varios.db.repositorio import NoEncontrado, Repositorio
from varios.db.sesion import sesion_de_cliente
from varios.procesos.motor import Identidad


def _quien(cliente, usuario):
    return Identidad(usuario=str(usuario), tenant=str(cliente), roles=frozenset({"aprobador"}))


def test_cada_cliente_solo_ve_lo_suyo(motor_app, dos_clientes):
    (ca, ua), (cb, ub) = dos_clientes["A"], dos_clientes["B"]
    with sesion_de_cliente(motor_app, ca) as s:
        sol = Repositorio(s, _quien(ca, ua)).crear_solicitud(ua, "Abrir siniestro de prueba")
    with sesion_de_cliente(motor_app, cb) as s:
        repo = Repositorio(s, _quien(cb, ub))
        assert repo.solicitudes() == []
        with pytest.raises(NoEncontrado):
            repo.solicitud(sol.id)
        # Ni siquiera saltándose el repositorio: RLS en PostgreSQL.
        assert s.execute(text("SELECT count(*) FROM solicitud")).scalar() == 0
        assert s.execute(text("SELECT count(*) FROM cliente")).scalar() == 1


def test_el_cliente_de_la_peticion_se_ignora(motor_app, dos_clientes):
    (ca, ua), (cb, _) = dos_clientes["A"], dos_clientes["B"]
    with sesion_de_cliente(motor_app, ca) as s:
        sol = Repositorio(s, _quien(ca, ua)).crear_solicitud(ua, "Prueba", cliente_id=cb)
        assert sol.cliente_id == ca


def test_escribir_en_otro_cliente_falla(motor_app, dos_clientes):
    (ca, ua), (cb, _) = dos_clientes["A"], dos_clientes["B"]
    with pytest.raises(DBAPIError):
        with sesion_de_cliente(motor_app, cb) as s:
            s.execute(text("INSERT INTO solicitud (id, cliente_id, autor_id, titulo, descripcion) "
                           "VALUES (:i, :c, :a, 'intruso', '')"), {"i": uuid.uuid4(), "c": ca, "a": ua})


def test_sin_cliente_no_se_ve_nada(motor_app, dos_clientes):
    with motor_app.connect() as c:
        assert c.execute(text("SELECT count(*) FROM solicitud")).scalar() == 0
        assert c.execute(text("SELECT count(*) FROM usuario")).scalar() == 0


def test_auditoria_inmutable(motor_app, motor_admin, dos_clientes):
    ca, ua = dos_clientes["A"]
    with sesion_de_cliente(motor_app, ca) as s:
        ev = Repositorio(s, _quien(ca, ua)).registrar("prueba", "objeto:1", None, "X", "prueba")
    for sql in ("UPDATE evento_auditoria SET motivo = 'cambiado' WHERE id = :i",
                "DELETE FROM evento_auditoria WHERE id = :i"):
        for motor in (motor_app, motor_admin):  # ni la aplicación ni el propietario
            with pytest.raises(DBAPIError):
                with motor.begin() as c:
                    c.execute(text("SELECT set_config('varios.cliente_id', :c, true)"), {"c": str(ca)})
                    c.execute(text(sql), {"i": ev.id})


def test_nadie_se_aprueba_a_si_mismo(motor_app, dos_clientes):
    ca, ua = dos_clientes["A"]
    with sesion_de_cliente(motor_app, ca) as s:
        sol = Repositorio(s, _quien(ca, ua)).crear_solicitud(ua, "Necesita aprobación", riesgo="medio")
    with pytest.raises(DBAPIError):
        with sesion_de_cliente(motor_app, ca) as s:
            s.execute(text("INSERT INTO aprobacion (id, cliente_id, solicitud_id, objeto, version, solicitada_por, "
                           "aprobador_id, decision, decidida_en) VALUES (:i, :c, :s, 'entregable', 1, :u, :u, "
                           "'aprobada', now())"), {"i": uuid.uuid4(), "c": ca, "s": sol.id, "u": str(ua)})
