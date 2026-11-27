/* Adaptador de la oficina con la API de Varios (N3b, M-041, D-028).
 *
 * - Solo se activa si la oficina se sirve desde la propia API (http://localhost:8000/oficina/) y /health responde.
 *   Como artefacto de Claude o abierta como archivo no hace nada: la oficina funciona como siempre (D-025).
 * - La oficina sigue guardando en su almacén (artefacto o navegador). Además, cada encargo se escribe en la API:
 *   alta, cambios de estado según encargo.json (camino más corto), petición de aprobación y decisión.
 * - El token va en sessionStorage (se borra al cerrar la pestaña). Es solo para desarrollo con datos inventados.
 * - Si la API rechaza algo (por ejemplo, aprobar lo que has pedido tú), la oficina lo avisa y no se fuerza nada.
 */
(function () {
  'use strict';
  var CLAVE = 'varios-api-token';
  // Estado de la API al que corresponde cada estado de la oficina.
  var DESTINO = {cola: 'PLANIFICADO', prog: 'PLANIFICADO', marcha: 'EN_EJECUCION', maqueta: 'EN_EJECUCION',
    revision: 'EN_QA', preg: 'PENDIENTE_INFO', aprob: 'PENDIENTE_APROBACION', hecha: 'ENTREGADO', rech: 'RECHAZADO'};
  // Y al revés, para los encargos que llegan de la API sin estar en esta oficina.
  var DESDE_API = {RECIBIDO: 'preg', EN_CLASIFICACION: 'preg', PENDIENTE_INFO: 'preg', PLANIFICADO: 'prog',
    EN_EJECUCION: 'prog', BLOQUEADO: 'preg', EN_QA: 'prog', RETRABAJO: 'prog', ESCALADO: 'preg',
    PENDIENTE_APROBACION: 'aprob', ENTREGADO: 'hecha', CERRADO: 'hecha', RECHAZADO: 'rech', CANCELADO: 'rech',
    REABIERTO: 'preg'};
  var RIESGOS = {bajo: 1, medio: 1, alto: 1, critico: 1};
  var A = {activa: false, base: '', token: '', grafo: null, colas: {}, ops: null, avisado: {}, apis: {}};

  function cab() { return {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + A.token}; }
  async function llamar(metodo, ruta, cuerpo) {
    var r = await fetch(A.base + ruta, {method: metodo, headers: cab(), body: cuerpo ? JSON.stringify(cuerpo) : undefined});
    var datos = null;
    try { datos = await r.json(); } catch (e) { datos = null; }
    if (!r.ok) { var err = new Error((datos && datos.detail) || ('HTTP ' + r.status)); err.status = r.status; throw err; }
    return datos;
  }

  // Camino más corto entre dos estados con las transiciones libres (sin pasar por las que exigen aprobación).
  function camino(de, a) {
    if (de === a) return [];
    var vistos = {}, cola = [[de, []]];
    vistos[de] = 1;
    while (cola.length) {
      var x = cola.shift(), sig = A.grafo[x[0]] || [];
      for (var i = 0; i < sig.length; i++) {
        var s = sig[i];
        if (vistos[s] || s === 'PENDIENTE_APROBACION' || s === 'ENTREGADO') continue;
        var p = x[1].concat([s]);
        if (s === a) return p;
        vistos[s] = 1; cola.push([s, p]);
      }
    }
    return null;
  }

  async function sincronizar(t) {
    // Lo último que se sabe de este encargo en la API (la copia de `t` puede ser anterior a la última respuesta).
    var api = Object.assign({}, A.apis[t.id] || t.api || {}), cambio = false;
    if (!api.id) {
      var e = await llamar('POST', '/encargos', {titulo: (t.title || t.text || 'Encargo').slice(0, 300),
        descripcion: t.text || '', riesgo: RIESGOS[t.risk] ? t.risk : 'bajo'});
      api = {id: e.id, estado: e.estado, version: e.version}; cambio = true;
    }
    var destino = DESTINO[t.status];
    if (destino && destino !== api.estado) {
      var antes = api.estado;
      if (destino === 'PENDIENTE_APROBACION' || destino === 'ENTREGADO' || antes === 'PENDIENTE_APROBACION') {
        // Aprobaciones: a QA, pedir, y decidir. De PENDIENTE_APROBACION solo se sale decidiendo (Guía v1.4 §4):
        // rechazar o descartar es una decisión «rechazada» que va a RECHAZADO si la oficina lo da por descartado y,
        // si no, a RETRABAJO y después el camino libre hasta donde esté en la oficina.
        if (antes !== 'PENDIENTE_APROBACION') {
          for (var p of (camino(antes, 'EN_QA') || [])) { api.estado = (await mover(api.id, p, 'Oficina: ' + t.status)).estado; }
          if (api.estado === 'EN_QA') {
            var ap = await llamar('POST', '/encargos/' + api.id + '/aprobaciones', {motivo: 'La oficina pide el OK de un socio'});
            api.aprobacion = ap.id; api.estado = 'PENDIENTE_APROBACION'; api.pedida = new Date().toISOString();
          }
        }
        if (api.estado === 'PENDIENTE_APROBACION' && destino !== 'PENDIENTE_APROBACION' && api.aprobacion) {
          var aprobada = destino === 'ENTREGADO';
          // Solo cuenta como decisión lo que hace un socio en la oficina, no el modo demostración (D-019).
          var ult = (t.log || []).filter(function (l) {
            return (!api.pedida || l.t >= api.pedida) && /^(Aprobado|Rechazado|Descartado) por un socio/.test(l.m || '');
          }).slice(-1)[0];
          if (!ult) {
            aviso(t.id, 'En la API, «' + (t.title || '').slice(0, 40) + '» sigue pendiente del OK de un socio.');
            A.apis[t.id] = api;
            if (cambio || api.estado !== antes) A.ops.guardarApi(t.id, api);
            return;
          }
          if (api.rehusada === api.aprobacion) return;
          try {
            var siRechaza = destino === 'RECHAZADO' ? 'RECHAZADO' : 'RETRABAJO';
            await llamar('POST', '/aprobaciones/' + api.aprobacion + '/decision',
              {decision: aprobada ? 'aprobada' : 'rechazada', motivo: ult.m, si_rechaza: siRechaza});
            api.estado = aprobada ? 'ENTREGADO' : siRechaza; api.aprobacion = '';
            if (!aprobada) for (var q of (camino(api.estado, destino) || [])) { api.estado = (await mover(api.id, q, 'Oficina: ' + t.status)).estado; }
          } catch (err) {
            if (err.status === 403) {
              api.rehusada = api.aprobacion; cambio = true;
              aviso(t.id, 'La API no acepta esta decisión: ' + err.message + '. Queda pendiente del OK de otra persona.');
            }
            else throw err;
          }
        }
      } else {
        var ruta = camino(antes, destino);
        if (ruta) for (var r of ruta) { api.estado = (await mover(api.id, r, 'Oficina: ' + t.status)).estado; }
      }
      cambio = cambio || api.estado !== antes;
    }
    A.apis[t.id] = api;
    if (cambio) A.ops.guardarApi(t.id, api);
  }
  function mover(id, a, motivo) { return llamar('POST', '/encargos/' + id + '/estado', {a: a, motivo: motivo}); }
  function aviso(id, m) { if (A.avisado[id + m]) return; A.avisado[id + m] = 1; A.ops.toast(m); }

  // Cola por encargo: los cambios de un mismo encargo se aplican en orden.
  function guardar(col, t) {
    // Las piezas son trabajo interno de un encargo y lo que llega de la API se muestra sin reescribirlo.
    if (!A.activa || col !== 'tasks' || !t || t.piece || !t.id || t.apiLectura) return;
    var previa = A.colas[t.id] || Promise.resolve();
    A.colas[t.id] = previa.then(function () { return sincronizar(t); }).catch(function (err) {
      aviso(t.id, 'No se ha podido guardar «' + (t.title || '').slice(0, 40) + '» en la API: ' + err.message);
    });
    return A.colas[t.id];
  }

  async function leer() {
    var lista = await llamar('GET', '/encargos'), locales = {};
    Object.values(A.ops.tareas()).forEach(function (t) { if (t.api && t.api.id) locales[t.api.id] = t; });
    lista.forEach(function (e) {
      var t = locales[e.id];
      if (t) {
        if (t.api.estado !== e.estado) {
          A.apis[t.id] = Object.assign({}, t.api, {estado: e.estado, version: e.version});
          A.ops.guardarApi(t.id, A.apis[t.id]);
        }
      }
      else A.ops.importar(e, DESDE_API[e.estado] || 'preg');
    });
    return lista.length;
  }

  async function conectar(token) {
    A.token = token;
    var def = await llamar('GET', '/definiciones/encargo');
    A.grafo = def.transiciones; A.activa = true;
    try { sessionStorage.setItem(CLAVE, token); } catch (e) { /* sin almacén: vale para esta visita */ }
    var n = await leer();
    A.ops.estado();
    return n;
  }

  async function iniciar(ops) {
    A.ops = ops;
    if (!/^https?:$/.test(location.protocol) || location.pathname.indexOf('/oficina') !== 0) return false;
    A.base = location.origin;
    try { var r = await fetch(A.base + '/health'); if (!r.ok) return false; } catch (e) { return false; }
    var token = '';
    var m = /(?:^#|&)token=([^&]+)/.exec(location.hash || '');
    if (m) { token = decodeURIComponent(m[1]); history.replaceState(null, '', location.pathname + location.search); }
    if (!token) { try { token = sessionStorage.getItem(CLAVE) || ''; } catch (e) { token = ''; } }
    A.disponible = true;
    ops.estado();
    if (!token) return false;
    try { await conectar(token); return true; } catch (e) {
      A.activa = false; ops.toast('La API no acepta el token: ' + e.message); ops.estado(); return false;
    }
  }

  window.VariosAPI = {
    iniciar: iniciar, guardar: guardar, conectar: conectar, leer: leer,
    activa: function () { return A.activa; }, disponible: function () { return !!A.disponible; },
    _camino: function (de, a, grafo) { var g = A.grafo; A.grafo = grafo; try { return camino(de, a); } finally { A.grafo = g; } }
  };
})();
