"""S3a: la API con tokens de un proveedor de identidad simulado (docs/31, D-033 propuesta). Datos inventados.

El proveedor simulado emite tokens con la forma de uno de OpenID Connect (como los de Keycloak: `iss` con el realm,
`aud`, `azp`, `typ`, `realm_access.roles`), firmados con el secreto de pruebas porque hoy la API solo verifica HS256
(D-028). Lo que se comprueba no depende del algoritmo: emisor, audiencia, caducidad, firma, y que los roles salen de
la base de Varios y no de lo que diga el token.
"""

import uuid
from datetime import UTC, datetime, timedelta

import jwt
import pytest
from sqlalchemy import text

from varios.config import ajustes

from .test_api_oficina import SECRETO, api  # noqa: F401 (fixture)

EMISOR = "https://idp.simulado.invalid/realms/varios"
AUDIENCIA = "varios-api"


class ProveedorSimulado:
    """Emite tokens como lo haría un proveedor OIDC. Solo para pruebas: no hay ningún proveedor real detrás."""

    def __init__(self, secreto: str = SECRETO, emisor: str = EMISOR, audiencia: str = AUDIENCIA):
        self.secreto, self.emisor, self.audiencia = secreto, emisor, audiencia

    def token(self, sub, cliente, minutos: int = 5, roles=(), **extra) -> str:
        ahora = datetime.now(UTC)
        datos = {"iss": self.emisor, "aud": self.audiencia, "sub": str(sub), "cliente": str(cliente),
                 "iat": ahora, "exp": ahora + timedelta(minutes=minutos), "azp": "oficina", "typ": "Bearer",
                 "realm_access": {"roles": list(roles)}, **extra}
        return jwt.encode(datos, self.secreto, algorithm="HS256")


@pytest.fixture()
def idp(monkeypatch, api):  # noqa: F811
    monkeypatch.setenv("VARIOS_JWT_EMISOR", EMISOR)
    monkeypatch.setenv("VARIOS_JWT_AUDIENCIA", AUDIENCIA)
    ajustes.cache_clear()
    yield ProveedorSimulado()
    ajustes.cache_clear()


@pytest.fixture()
def papeles(motor_admin, dos_clientes):
    """Cliente A con los tres papeles de S3a: socio (persona que aprueba), agente (no persona) y cliente (persona
    del cliente, sin rol de aprobación). Cliente B con su socio."""
    ca, _ = dos_clientes["A"]
    cb, ub = dos_clientes["B"]
    p = {}
    with motor_admin.begin() as c:
        c.execute(text("SELECT set_config('varios.cliente_id', :c, true)"), {"c": str(ca)})
        for nombre, roles, persona in (("socio", '["aprobador"]', True), ("socio2", '["aprobador"]', True),
                                       ("agente", '["agente"]', False), ("cliente", '["cliente"]', True)):
            uid = uuid.uuid4()
            c.execute(text("INSERT INTO usuario (id, cliente_id, email, nombre, roles, es_persona) "
                           "VALUES (:u, :c, :e, :n, CAST(:r AS json), :p)"),
                      {"u": uid, "c": ca, "e": f"{nombre}@idp-a.invalid", "n": f"{nombre} (inventado)", "r": roles,
                       "p": persona})
            p[nombre] = (uid, ca)
    p["b"] = (ub, cb)
    return p


def _h(tok: str) -> dict:
    return {"Authorization": f"Bearer {tok}"}


def _pendiente(api, idp, quien):  # noqa: F811
    tok = idp.token(*quien)
    enc = api.post("/encargos", json={"titulo": "Propuesta (inventada)", "riesgo": "medio"}, headers=_h(tok)).json()
    for a in ("EN_CLASIFICACION", "PLANIFICADO", "EN_EJECUCION", "EN_QA"):
        assert api.post(f"/encargos/{enc['id']}/estado", json={"a": a, "motivo": a}, headers=_h(tok)).status_code == 200
    ap = api.post(f"/encargos/{enc['id']}/aprobaciones", json={}, headers=_h(tok)).json()
    return enc, ap


def test_los_tres_papeles(api, idp, papeles):  # noqa: F811
    socio, socio2, agente, cliente = papeles["socio"], papeles["socio2"], papeles["agente"], papeles["cliente"]
    enc, ap = _pendiente(api, idp, socio)
    ok = {"decision": "aprobada", "motivo": "Revisado"}
    # El cliente ve los encargos de su cliente, pero no aprueba aunque su token diga que es aprobador.
    assert api.get("/encargos", headers=_h(idp.token(*cliente))).status_code == 200
    r = api.post(f"/aprobaciones/{ap['id']}/decision", json=ok,
                 headers=_h(idp.token(*cliente, roles=["aprobador", "admin"])))
    assert r.status_code == 403
    # Un agente no aprueba nunca, tampoco con roles en el token.
    r = api.post(f"/aprobaciones/{ap['id']}/decision", json=ok, headers=_h(idp.token(*agente, roles=["aprobador"])))
    assert r.status_code == 403
    # Quien lo pidió tampoco; otro socio sí.
    assert api.post(f"/aprobaciones/{ap['id']}/decision", json=ok, headers=_h(idp.token(*socio))).status_code == 403
    r = api.post(f"/aprobaciones/{ap['id']}/decision", json=ok, headers=_h(idp.token(*socio2)))
    assert r.status_code == 200 and r.json()["aprobador_id"] == str(socio2[0])


def test_emisor_audiencia_caducidad_y_firma(api, idp, papeles):  # noqa: F811
    socio = papeles["socio"]
    assert api.get("/encargos", headers=_h(idp.token(*socio))).status_code == 200
    malos = {
        "otro emisor": ProveedorSimulado(emisor="https://otro-idp.invalid/realms/varios").token(*socio),
        "otra audiencia": ProveedorSimulado(audiencia="otra-aplicacion").token(*socio),
        "caducado": idp.token(*socio, minutos=-1),
        "otra firma": ProveedorSimulado(secreto="otro-proveedor-" + "q" * 40).token(*socio),
        "aún no válido": idp.token(*socio, nbf=datetime.now(UTC) + timedelta(minutes=10)),
        "sin cliente": jwt.encode({"iss": EMISOR, "aud": AUDIENCIA, "sub": str(socio[0]),
                                   "exp": datetime.now(UTC) + timedelta(minutes=5)}, SECRETO, algorithm="HS256"),
        "sin firma": jwt.encode({"iss": EMISOR, "aud": AUDIENCIA, "sub": str(socio[0]), "cliente": str(socio[1]),
                                 "exp": datetime.now(UTC) + timedelta(minutes=5)}, None, algorithm="none"),
    }
    for nombre, tok in malos.items():
        assert api.get("/encargos", headers=_h(tok)).status_code == 401, nombre


def test_el_cliente_sale_del_token_y_tiene_que_casar_con_el_usuario(api, idp, papeles):  # noqa: F811
    socio, b = papeles["socio"], papeles["b"]
    # Un token del proveedor con el usuario de A y el cliente de B: el usuario no existe en B → no autenticado.
    assert api.get("/encargos", headers=_h(idp.token(socio[0], b[1]))).status_code == 401
    # Un usuario que no está en la base, aunque el proveedor lo firme bien.
    assert api.get("/encargos", headers=_h(idp.token(uuid.uuid4(), socio[1]))).status_code == 401
    # Un sujeto que no es un identificador de Varios (como los de un proveedor real) todavía no se acepta: hará falta
    # la tabla de correspondencias que propone D-033.
    assert api.get("/encargos", headers=_h(idp.token("f:1b2c:usuario-externo", socio[1]))).status_code == 401


def test_un_usuario_desactivado_deja_de_entrar_aunque_su_token_siga_vigente(api, idp, papeles, motor_admin):  # noqa: F811
    cliente = papeles["cliente"]
    tok = idp.token(*cliente, minutos=30)
    assert api.get("/encargos", headers=_h(tok)).status_code == 200
    with motor_admin.begin() as c:
        c.execute(text("SELECT set_config('varios.cliente_id', :c, true)"), {"c": str(cliente[1])})
        c.execute(text("UPDATE usuario SET activo = false WHERE id = :u"), {"u": cliente[0]})
    assert api.get("/encargos", headers=_h(tok)).status_code == 401
