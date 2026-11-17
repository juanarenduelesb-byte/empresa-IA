import pytest

from varios.procesos.motor import AprobacionInvalida, Identidad, Motor, TransicionInvalida

ANA = Identidad("ana", "cliente-ficticio-a")
LUIS = Identidad("luis", "cliente-ficticio-a", frozenset({"aprobador"}))
AGENTE = Identidad("agente-backend", "cliente-ficticio-a", frozenset({"aprobador"}), persona=False)
OTRO = Identidad("eva", "cliente-ficticio-b", frozenset({"aprobador"}))


def llevar_a_qa(m, quien, riesgo):
    e = m.alta(quien, "Encargo de prueba", riesgo=riesgo)
    for a in ("EN_CLASIFICACION", "PLANIFICADO", "EN_EJECUCION", "EN_QA"):
        m.mover(quien, e.id, a, "paso de prueba")
    return e


def test_tenant_sale_de_la_identidad():
    m = Motor()
    e = m.alta(ANA, "x", tenant="cliente-ficticio-b")
    assert e.tenant == "cliente-ficticio-a"


def test_otro_cliente_no_ve_el_encargo():
    m = Motor()
    e = m.alta(ANA, "x")
    with pytest.raises(KeyError):
        m.obtener(OTRO, e.id)
    with pytest.raises(KeyError):
        m.mover(OTRO, e.id, "EN_CLASIFICACION", "intento")


def test_transicion_invalida_rechazada_y_sin_auditoria():
    m = Motor()
    e = m.alta(ANA, "x")
    n = len(m.auditoria)
    with pytest.raises(TransicionInvalida):
        m.mover(ANA, e.id, "ENTREGADO", "saltarse pasos")
    assert e.estado == "RECIBIDO" and len(m.auditoria) == n


def test_motivo_obligatorio():
    m = Motor()
    e = m.alta(ANA, "x")
    with pytest.raises(TransicionInvalida):
        m.mover(ANA, e.id, "EN_CLASIFICACION", " ")


def test_auditoria_completa():
    m = Motor()
    e = llevar_a_qa(m, ANA, "bajo")
    esperado = ["RECIBIDO", "EN_CLASIFICACION", "PLANIFICADO", "EN_EJECUCION", "EN_QA"]
    assert [ev.despues for ev in e.historial] == esperado
    ev = e.historial[-1]
    assert ev.actor == "ana" and ev.antes == "EN_EJECUCION" and ev.motivo and ev.version_definicion == "1.0.0"
    with pytest.raises(AttributeError):
        ev.motivo = "cambiado"  # inmutable


def test_entrega_directa_solo_riesgo_bajo_y_qa_conforme():
    m = Motor()
    e = llevar_a_qa(m, ANA, "bajo")
    with pytest.raises(TransicionInvalida):
        m.mover(ANA, e.id, "ENTREGADO", "sin QA")
    m.resultado_qa(ANA, e.id, True, "cumple el criterio")
    m.mover(ANA, e.id, "ENTREGADO", "QA conforme")
    assert e.estado == "ENTREGADO"

    e2 = llevar_a_qa(m, ANA, "medio")
    m.resultado_qa(ANA, e2.id, True, "cumple")
    with pytest.raises(TransicionInvalida):
        m.mover(ANA, e2.id, "ENTREGADO", "riesgo medio")


def test_aprobacion_humana_distinta_del_autor_y_misma_version():
    m = Motor()
    e = llevar_a_qa(m, ANA, "alto")
    m.mover(ANA, e.id, "PENDIENTE_APROBACION", "riesgo alto")
    with pytest.raises(AprobacionInvalida):
        m.mover(ANA, e.id, "ENTREGADO", "saltar aprobación")
    with pytest.raises(AprobacionInvalida):
        m.aprobar(Identidad("ana", "cliente-ficticio-a", frozenset({"aprobador"})), e.id, 1, "me apruebo")
    with pytest.raises(AprobacionInvalida):
        m.aprobar(AGENTE, e.id, 1, "un agente no aprueba")
    with pytest.raises(AprobacionInvalida):
        m.aprobar(Identidad("pepe", "cliente-ficticio-a"), e.id, 1, "sin rol")
    with pytest.raises(AprobacionInvalida):
        m.aprobar(LUIS, e.id, 2, "otra versión")
    m.aprobar(LUIS, e.id, 1, "revisado")
    assert e.estado == "ENTREGADO" and e.historial[-1].actor == "luis"


def test_retrabajo_invalida_aprobacion_anterior():
    m = Motor()
    e = llevar_a_qa(m, ANA, "alto")
    m.mover(ANA, e.id, "PENDIENTE_APROBACION", "riesgo alto")
    m.mover(LUIS, e.id, "RETRABAJO", "falta un dato")
    m.mover(ANA, e.id, "EN_EJECUCION", "corrijo")
    m.mover(ANA, e.id, "EN_QA", "listo")
    m.mover(ANA, e.id, "PENDIENTE_APROBACION", "riesgo alto")
    with pytest.raises(AprobacionInvalida):
        m.aprobar(LUIS, e.id, 1, "aprobaba la versión vieja")
    m.aprobar(LUIS, e.id, 2, "versión nueva revisada")


def test_idempotencia_en_transiciones():
    m = Motor()
    e = m.alta(ANA, "x")
    m.mover(ANA, e.id, "EN_CLASIFICACION", "clasificar", clave_idempotencia="k1")
    n = len(m.auditoria)
    m.mover(ANA, e.id, "EN_CLASIFICACION", "clasificar", clave_idempotencia="k1")
    assert len(m.auditoria) == n and e.estado == "EN_CLASIFICACION"
