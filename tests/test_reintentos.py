import random

import pytest

from varios.procesos.reintentos import Agotado, ErrorClasificado, RegistroIdempotencia, con_reintentos, espera


def fallos(*tipos, ok="hecho"):
    pendientes = list(tipos)
    llamadas = []

    def accion():
        llamadas.append(1)
        if pendientes:
            raise ErrorClasificado(pendientes.pop(0))
        return ok

    return accion, llamadas


def test_transitorio_se_reintenta_y_termina():
    accion, llamadas = fallos("transitorio", "dependencia_externa")
    assert con_reintentos(accion, max_intentos=3) == "hecho"
    assert len(llamadas) == 3


@pytest.mark.parametrize("tipo", ["autorizacion", "seguridad", "politica", "permanente"])
def test_no_reintentables_fallan_a_la_primera(tipo):
    accion, llamadas = fallos(tipo)
    with pytest.raises(ErrorClasificado):
        con_reintentos(accion, max_intentos=5)
    assert len(llamadas) == 1


def test_agotado_tras_max_intentos():
    accion, llamadas = fallos("transitorio", "transitorio", "transitorio")
    with pytest.raises(Agotado) as e:
        con_reintentos(accion, max_intentos=3)
    assert e.value.intentos == 3 and len(llamadas) == 3


def test_espera_crece_y_tiene_tope():
    r = random.Random(0)
    techos = [min(60, 2 ** (i - 1)) for i in range(1, 10)]
    for i, techo in enumerate(techos, 1):
        assert 0 <= espera(i, azar=r) <= techo
    assert techos[-1] == 60


def test_duerme_entre_intentos():
    esperas = []
    accion, _ = fallos("transitorio", "transitorio")
    con_reintentos(accion, max_intentos=3, dormir=esperas.append)
    assert len(esperas) == 2


def test_tipo_desconocido_rechazado():
    with pytest.raises(ValueError):
        ErrorClasificado("raro")


def test_idempotencia_evita_duplicados():
    reg = RegistroIdempotencia()
    enviados = []

    def enviar():
        enviados.append(1)
        return "enviado-1"

    assert reg.ejecutar("parte-0001", enviar) == "enviado-1"
    assert reg.ejecutar("parte-0001", enviar) == "enviado-1"
    assert len(enviados) == 1 and reg.ya_hecho("parte-0001")
    with pytest.raises(ValueError):
        reg.ejecutar("", enviar)
