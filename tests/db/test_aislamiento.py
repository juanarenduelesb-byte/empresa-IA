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


def test_ninguna_tabla_de_cliente_deja_ver_filas_de_otro(base, motor_admin, motor_app):
    """Repaso del 27/11 (tanda 23:30): `test_rls_forzada_en_todas_las_tablas` mira que la RLS esté activada, pero no
    que la política de cada tabla filtre de verdad. Aquí se recorren TODAS las tablas con `cliente_id` (también las que
    se añadan mañana) con la semilla cargada en los dos clientes: con el rol de la aplicación, nadie ve una fila de otro
    cliente, y sin cliente no se ve ninguna. Además, el rol de la aplicación no puede saltarse la RLS."""
    from varios.db.semilla import _id, cargar  # noqa: PLC0415

    cargar(base[0])
    with motor_admin.connect() as c:
        tablas = c.execute(text("SELECT table_name FROM information_schema.columns WHERE table_schema = 'public' "
                                "AND column_name = 'cliente_id' ORDER BY table_name")).scalars().all()
        rol = c.execute(text("SELECT rolsuper, rolbypassrls FROM pg_roles WHERE rolname = 'varios_app'")).one()
        suyas = c.execute(text("SELECT tablename FROM pg_tables WHERE schemaname = 'public' "
                               "AND tableowner = 'varios_app'")).scalars().all()
        clientes = [_id("cliente", "atalaya"), _id("cliente", "senuelo")]
        # Para que la prueba pruebe algo: como administrador hay filas de los dos clientes en estas tablas.
        for t in ("usuario", "solicitud", "poliza", "evento_auditoria"):
            con_filas = c.execute(text(f"SELECT count(DISTINCT cliente_id) FROM {t} WHERE cliente_id = ANY(:c)"),
                                  {"c": clientes}).scalar()
            assert con_filas == 2, t
    assert len(tablas) >= 10 and {"poliza", "solicitud", "tarea", "aprobacion", "evento_auditoria"} <= set(tablas)
    assert not rol.rolsuper and not rol.rolbypassrls, "El rol de la aplicación no puede saltarse la RLS"
    assert not suyas, f"El rol de la aplicación es dueño de tablas (podría desactivar la RLS): {suyas}"
    for cid in clientes:
        with sesion_de_cliente(motor_app, cid) as s:
            for t in tablas:
                ajenas = s.execute(text(f"SELECT count(*) FROM {t} WHERE cliente_id IS NOT NULL "
                                        "AND cliente_id <> :c"), {"c": cid}).scalar()
                assert ajenas == 0, f"{t}: el cliente {cid} ve {ajenas} filas de otro"
    with motor_app.connect() as c:  # sin cliente en la sesión
        for t in tablas:
            assert c.execute(text(f"SELECT count(*) FROM {t} WHERE cliente_id IS NOT NULL")).scalar() == 0, t
