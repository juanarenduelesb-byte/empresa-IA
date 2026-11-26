"""Conocimiento con permisos y citas (plan S7): desde A nunca sale nada de B y todo resultado trae su fuente."""

import uuid

from sqlalchemy import text

from varios.db.repositorio import Repositorio
from varios.db.sesion import sesion_de_cliente
from varios.procesos.motor import Identidad


def _ficha(c, cliente, codigo, titulo, cuerpo, fuente=None):
    fid = uuid.uuid4()
    c.execute(text("INSERT INTO ficha_conocimiento (id, cliente_id, codigo, titulo, cuerpo, estado, etiquetas, origen) "
                   "VALUES (:i, :c, :co, :t, :b, 'draft', '[]', 'prueba')"),
              {"i": fid, "c": cliente, "co": codigo, "t": titulo, "b": cuerpo})
    if fuente:
        c.execute(text("INSERT INTO ficha_fuente (ficha_id, fuente_id, cliente_id, cita) "
                       "VALUES (:f, :u, :c, 'art. 16')"), {"f": fid, "u": fuente, "c": cliente})
    return fid


def test_busqueda_con_permisos_y_citas(motor_admin, motor_app, dos_clientes):
    (ca, ua), (cb, ub) = dos_clientes["A"], dos_clientes["B"]
    marca = uuid.uuid4().hex[:8]
    with motor_admin.begin() as c:  # conocimiento común: lo carga el administrador
        fuente = uuid.uuid4()
        c.execute(text("INSERT INTO fuente (id, codigo, titulo, organismo, url, tipo, autoridad, vigencia, estado) "
                       "VALUES (:i, :co, 'Ley de Contrato de Seguro', 'BOE', 'https://www.boe.es', 'ley', 'alta', "
                       "'vigente', 'validated')"), {"i": fuente, "co": f"LCS-{marca}"})
        _ficha(c, None, f"comun-{marca}", "Plazo de comunicación del siniestro",
               f"El tomador comunica el siniestro en siete días {marca}", fuente)
        _ficha(c, None, f"sin-fuente-{marca}", "Ficha sin fuente", f"Comunicación del siniestro {marca}")
    for letra, (cid, _) in dos_clientes.items():
        with sesion_de_cliente(motor_app, cid) as s:
            fuente_c = uuid.uuid4()
            s.execute(text("INSERT INTO fuente (id, cliente_id, codigo, titulo) VALUES (:i, :c, :co, 'Nota interna')"),
                      {"i": fuente_c, "c": cid, "co": f"interna-{marca}"})
            _ficha(s, cid, f"propia-{marca}", f"Siniestro del cliente {letra}",
                   f"Comunicación del siniestro en el cliente {letra} {marca}", fuente_c)
    with sesion_de_cliente(motor_app, ca) as s:
        res = Repositorio(s, Identidad(str(ua), str(ca))).buscar_conocimiento(f"siniestro {marca}")
    codigos = {r["codigo"] for r in res}
    assert codigos == {f"comun-{marca}", f"propia-{marca}"}
    assert all(r["cliente_id"] in (None, ca) for r in res)
    assert all(r["fuentes"] for r in res)
    with sesion_de_cliente(motor_app, cb) as s:
        res_b = Repositorio(s, Identidad(str(ub), str(cb))).buscar_conocimiento(f"cliente A {marca}")
    assert all(r["cliente_id"] in (None, cb) for r in res_b)


def test_la_aplicacion_no_escribe_conocimiento_comun(motor_app, dos_clientes):
    import pytest
    from sqlalchemy.exc import DBAPIError

    ca, _ = dos_clientes["A"]
    with pytest.raises(DBAPIError):
        with sesion_de_cliente(motor_app, ca) as s:
            s.execute(text("INSERT INTO fuente (id, cliente_id, codigo, titulo) VALUES (:i, NULL, 'x', 'x')"),
                      {"i": uuid.uuid4()})
