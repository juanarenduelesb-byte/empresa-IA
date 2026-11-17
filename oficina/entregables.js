/* Varios · Entregables
 * Plantilla única de marca y generadores de archivos reales:
 * presentación (.pptx), hoja de cálculo (.xlsx), documento (.docx) y diagrama de proceso (.svg/.png).
 * También lee el texto de los documentos que se suben (txt, md, csv, json, html, docx, xlsx, pptx, pdf).
 * Las librerías se cargan solo cuando hacen falta, desde vendor/ (todas con licencia MIT o Apache-2.0).
 */
(function () {
  "use strict";

  // ---------- Marca (la misma en todos los formatos) ----------
  var T = {
    wine: "7A1F2E", acc: "0B7A78", champ: "EADBB8", surf: "F6EFE1", ink: "22171A",
    mut: "6A5A55", hair: "E4D6BC", card: "FFFBF3", wineT: "F3E2E1", accT: "DDEFEA", champT: "FBF4E6",
    font: "Arial"
  };
  var KINDS = {
    pptx: { n: "Presentación", ext: "pptx", ic: "P" },
    xlsx: { n: "Hoja de cálculo", ext: "xlsx", ic: "X" },
    docx: { n: "Documento", ext: "docx", ic: "W" },
    proceso: { n: "Diagrama de proceso", ext: "svg", ic: "◇" }
  };
  var ACTOR = {
    persona: { n: "Persona", fill: "#F3E2E1", stroke: "#7A1F2E" },
    regla: { n: "Regla (código)", fill: "#FBF4E6", stroke: "#B07A2A" },
    ia: { n: "IA (propone)", fill: "#DDEFEA", stroke: "#0B7A78" },
    sistema: { n: "Sistema", fill: "#FFFBF3", stroke: "#6A5A55" }
  };

  // ---------- Utilidades ----------
  function str(x) { return x == null ? "" : String(x); }
  function arr(x) { return Array.isArray(x) ? x : (x == null || x === "" ? [] : [x]); }
  function esc(t) { return str(t).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function clip(t, n) { t = str(t).trim(); return t.length > n ? t.slice(0, n - 1) + "…" : t; }
  function plain(t) { return str(t).replace(/\*\*(.+?)\*\*/g, "$1").replace(/`([^`]+)`/g, "$1"); }
  function slug(t) { return str(t).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 60) || "entregable"; }
  function hoy() { var d = new Date(); return ("0" + d.getDate()).slice(-2) + "/" + ("0" + (d.getMonth() + 1)).slice(-2) + "/" + d.getFullYear(); }
  function fileName(kind, meta, ext) { return slug((meta.proyecto ? meta.proyecto + " " : "") + (meta.titulo || KINDS[kind].n)) + "-v" + (meta.version || 1) + "." + (ext || KINDS[kind].ext); }

  // ---------- Carga perezosa de librerías ----------
  var LIBS = {
    pptx: { src: "vendor/pptxgen.bundle.js", ok: function () { return window.PptxGenJS; } },
    xlsx: { src: "vendor/exceljs.min.js", ok: function () { return window.ExcelJS; } },
    docx: { src: "vendor/docx.iife.js", ok: function () { return window.docx; } },
    zip: { src: "vendor/jszip.min.js", ok: function () { return window.JSZip; } },
    pdf: { src: "vendor/pdf.min.js", ok: function () { return window.pdfjsLib; } }
  };
  var loading = {};
  function need(k) {
    var L = LIBS[k];
    if (L.ok()) return Promise.resolve(L.ok());
    if (loading[k]) return loading[k];
    loading[k] = new Promise(function (res, rej) {
      var s = document.createElement("script"); s.src = L.src; s.async = true;
      s.onload = function () { L.ok() ? res(L.ok()) : rej(new Error("No se cargó " + k)); };
      s.onerror = function () { delete loading[k]; rej(new Error("No se pudo cargar " + L.src)); };
      document.head.appendChild(s);
    });
    return loading[k];
  }

  // ---------- Logotipo en PNG (dibujado, no copiado) ----------
  var logoCache = {};
  function logoPng(withWord, dark) {
    var key = (withWord ? "w" : "m") + (dark ? "d" : "l");
    if (logoCache[key]) return logoCache[key];
    var s = 6, c = document.createElement("canvas"), x = c.getContext("2d");
    var W = withWord ? 118 : 30, H = 24;
    c.width = W * s; c.height = H * s; x.scale(s, s);
    function bar(bx, by, bw, bh, col) { x.fillStyle = col; var r = 3.5; x.beginPath(); x.moveTo(bx + r, by); x.arcTo(bx + bw, by, bx + bw, by + bh, r); x.arcTo(bx + bw, by + bh, bx, by + bh, r); x.arcTo(bx, by + bh, bx, by, r); x.arcTo(bx, by, bx + bw, by, r); x.closePath(); x.fill(); }
    bar(2, 3, 7, 18, "#" + T.wine); bar(12, 8, 7, 13, "#" + T.acc); bar(22, 4.5, 7, 15, "#" + T.champ);
    if (withWord) { x.fillStyle = dark ? "#FFFFFF" : "#" + T.ink; x.font = "700 19px Arial, sans-serif"; x.textBaseline = "middle"; x.fillText("varios", 36, 13); }
    logoCache[key] = { url: c.toDataURL("image/png"), w: W, h: H };
    return logoCache[key];
  }
  function b64ToBytes(dataUrl) { var b = atob(dataUrl.split(",")[1]), u = new Uint8Array(b.length); for (var i = 0; i < b.length; i++) u[i] = b.charCodeAt(i); return u; }

  // ---------- Esquemas que se piden a la IA ----------
  var SCHEMA = {
    pptx: '{"titulo": str, "subtitulo": str, "slides": [ {"tipo": "portada"|"seccion"|"puntos"|"dos_columnas"|"cifras"|"tabla"|"cierre", "antetitulo": str corto, "titulo": frase completa con punto, "puntos": [str, máx 6], "izquierda": {"titulo": str, "puntos": [str]}, "derecha": {"titulo": str, "puntos": [str]}, "cifras": [{"valor": str, "etiqueta": str}] (máx 4), "tabla": {"cabecera": [str], "filas": [[str]]} (máx 10 filas), "notas": notas del orador} ] (entre 5 y 12 diapositivas; la primera "portada" y la última "cierre"), "fuentes": [str]}',
    xlsx: '{"titulo": str, "subtitulo": str, "hojas": [ {"nombre": máx 28 caracteres, "descripcion": str, "columnas": [{"nombre": str, "tipo": "texto"|"numero"|"euros"|"porcentaje"|"fecha", "ancho": número 8-60, "entrada": true si la rellena el usuario}], "filas": [[valores; números sin separador de miles y con punto decimal; porcentajes como 0.25; fechas dd/mm/aaaa; fórmulas en inglés empezando por = y con coma como separador, referenciando celdas como B5]], "totales": true|false} ] (1 a 4 hojas), "notas": [str]}',
    docx: '{"titulo": str, "subtitulo": str, "resumen": str de 2-4 frases, "secciones": [ {"titulo": str, "bloques": [ {"tipo": "parrafo", "texto": str (admite **negrita**)} | {"tipo": "lista", "items": [str]} | {"tipo": "tabla", "cabecera": [str], "filas": [[str]]} | {"tipo": "nota", "titulo": str, "texto": str} ] } ], "fuentes": [str]}',
    proceso: '{"titulo": str, "descripcion": str, "carriles": [nombres de quién actúa, 2 a 5], "pasos": [ {"id": "p1", "nombre": verbo + objeto en máx 6 palabras, "carril": uno de carriles, "tipo": "inicio"|"tarea"|"decision"|"fin", "actor": "persona"|"regla"|"ia"|"sistema"} ] (6 a 16 pasos, un inicio y al menos un fin), "flujos": [ {"de": id, "a": id, "etiqueta": str corto o ""} ], "notas": [str]}'
  };
  var GUIA = {
    pptx: "Una idea por diapositiva. Antetítulo en pocas palabras y título como frase completa con punto. Máximo 6 puntos de 12 palabras. Cifras solo si están en el contenido; si no, no uses diapositivas de cifras.",
    xlsx: "Tablas listas para usar: cabeceras claras, una fila por registro, tipos correctos. Si hay importes, columna de tipo euros y totales. No inventes cifras: si faltan, deja la celda vacía y márcala en notas como [POR CONFIRMAR].",
    docx: "Documento profesional: resumen al principio, secciones con títulos cortos, párrafos breves, listas y tablas cuando ayuden. Lo que falte, [POR CONFIRMAR].",
    proceso: "Diagrama de carriles. Cada paso dice quién lo hace y si lo hace una persona, una regla de código, la IA (solo propone) o un sistema. Decisiones con dos salidas etiquetadas. La IA nunca decide lo que corresponde a una persona."
  };

  // ---------- Normalización (la IA no siempre cumple el esquema) ----------
  function norm(kind, s) {
    s = s && typeof s === "object" ? s : {};
    s.titulo = clip(plain(s.titulo || "Entregable"), 120); s.subtitulo = clip(plain(s.subtitulo || ""), 200);
    if (kind === "pptx") {
      var sl = arr(s.slides).filter(function (x) { return x && typeof x === "object"; }).slice(0, 14).map(function (x) {
        var tipo = ["portada", "seccion", "puntos", "dos_columnas", "cifras", "tabla", "cierre"].indexOf(x.tipo) >= 0 ? x.tipo : "puntos";
        var col = function (c) { c = c || {}; return { titulo: clip(plain(c.titulo), 60), puntos: arr(c.puntos).map(function (p) { return clip(plain(p), 140); }).slice(0, 6) }; };
        var tb = x.tabla || {};
        return { tipo: tipo, antetitulo: clip(plain(x.antetitulo), 50), titulo: clip(plain(x.titulo), 130), puntos: arr(x.puntos).map(function (p) { return clip(plain(p), 170); }).slice(0, 7), izquierda: col(x.izquierda), derecha: col(x.derecha), cifras: arr(x.cifras).slice(0, 4).map(function (c) { return { valor: clip(plain(c && c.valor), 14), etiqueta: clip(plain(c && c.etiqueta), 70) }; }), tabla: { cabecera: arr(tb.cabecera).map(function (c) { return clip(plain(c), 40); }).slice(0, 6), filas: arr(tb.filas).slice(0, 10).map(function (r) { return arr(r).map(function (c) { return clip(plain(c), 80); }).slice(0, 6); }) }, notas: clip(plain(x.notas), 1200) };
      });
      if (!sl.length || sl[0].tipo !== "portada") sl.unshift({ tipo: "portada", antetitulo: "", titulo: s.titulo, puntos: [], izquierda: { puntos: [] }, derecha: { puntos: [] }, cifras: [], tabla: { cabecera: [], filas: [] }, notas: "" });
      s.slides = sl; s.fuentes = arr(s.fuentes).map(plain).slice(0, 12);
    } else if (kind === "xlsx") {
      var used = {};
      s.hojas = arr(s.hojas).slice(0, 6).map(function (h, i) {
        h = h || {}; var nm = clip(str(h.nombre || "Hoja " + (i + 1)).replace(/[\[\]\*\?\/\\:]/g, " "), 28) || "Hoja " + (i + 1);
        if (/^portada$/i.test(nm)) nm = nm + " 2"; while (used[nm.toLowerCase()]) nm = clip(nm, 25) + " " + (i + 1); used[nm.toLowerCase()] = 1;
        var cols = arr(h.columnas).slice(0, 20).map(function (c) { c = typeof c === "string" ? { nombre: c } : (c || {}); return { nombre: clip(plain(c.nombre || "Columna"), 60), tipo: ["texto", "numero", "euros", "porcentaje", "fecha"].indexOf(c.tipo) >= 0 ? c.tipo : "texto", ancho: Math.max(8, Math.min(60, +c.ancho || 0)) || 0, entrada: !!c.entrada }; });
        var filas = arr(h.filas).slice(0, 500).map(function (r) { return arr(r).slice(0, cols.length || 20); });
        if (!cols.length) cols = (filas[0] || ["Dato"]).map(function (_, k) { return { nombre: "Columna " + (k + 1), tipo: "texto", ancho: 0, entrada: false }; });
        return { nombre: nm, descripcion: clip(plain(h.descripcion), 300), columnas: cols, filas: filas, totales: !!h.totales };
      });
      if (!s.hojas.length) s.hojas = [{ nombre: "Datos", descripcion: "", columnas: [{ nombre: "Dato", tipo: "texto", ancho: 30 }], filas: [], totales: false }];
      s.notas = arr(s.notas).map(plain).slice(0, 12);
    } else if (kind === "docx") {
      s.resumen = clip(plain(s.resumen), 900);
      s.secciones = arr(s.secciones).slice(0, 20).map(function (x) {
        x = x || {};
        return { titulo: clip(plain(x.titulo || "Apartado"), 100), bloques: arr(x.bloques).slice(0, 30).map(function (b) {
          if (typeof b === "string") return { tipo: "parrafo", texto: b };
          b = b || {}; var t = ["parrafo", "lista", "tabla", "nota"].indexOf(b.tipo) >= 0 ? b.tipo : "parrafo";
          return { tipo: t, texto: str(b.texto).slice(0, 4000), titulo: clip(plain(b.titulo), 80), items: arr(b.items).map(function (i) { return str(i).slice(0, 600); }).slice(0, 25), cabecera: arr(b.cabecera).map(function (c) { return clip(plain(c), 60); }).slice(0, 7), filas: arr(b.filas).slice(0, 40).map(function (r) { return arr(r).map(function (c) { return clip(plain(c), 300); }).slice(0, 7); }) };
        }) };
      });
      s.fuentes = arr(s.fuentes).map(plain).slice(0, 20);
    } else if (kind === "proceso") {
      s.descripcion = clip(plain(s.descripcion), 400);
      var lanes = arr(s.carriles).map(function (c) { return clip(plain(c), 28); }).filter(Boolean).slice(0, 6);
      var seen = {};
      s.pasos = arr(s.pasos).slice(0, 24).map(function (p, i) {
        p = p || {}; var id = str(p.id || "p" + (i + 1)).replace(/[^\w-]/g, "") || "p" + (i + 1); while (seen[id]) id += "x"; seen[id] = 1;
        var lane = clip(plain(p.carril), 28); if (lane && lanes.indexOf(lane) < 0) lanes.push(lane);
        return { id: id, nombre: clip(plain(p.nombre || "Paso"), 60), carril: lane || lanes[0] || "Equipo", tipo: ["inicio", "tarea", "decision", "fin"].indexOf(p.tipo) >= 0 ? p.tipo : "tarea", actor: ACTOR[p.actor] ? p.actor : "persona" };
      });
      if (!lanes.length) lanes = ["Equipo"];
      s.pasos.forEach(function (p) { if (lanes.indexOf(p.carril) < 0) p.carril = lanes[0]; });
      s.carriles = lanes.slice(0, 7);
      var ids = s.pasos.map(function (p) { return p.id; });
      s.flujos = arr(s.flujos).filter(function (f) { return f && ids.indexOf(f.de) >= 0 && ids.indexOf(f.a) >= 0 && f.de !== f.a; }).slice(0, 40).map(function (f) { return { de: f.de, a: f.a, etiqueta: clip(plain(f.etiqueta), 22) }; });
      if (!s.flujos.length) for (var k = 1; k < ids.length; k++) s.flujos.push({ de: ids[k - 1], a: ids[k], etiqueta: "" });
      s.notas = arr(s.notas).map(plain).slice(0, 10);
    }
    return s;
  }

  // ---------- Diagrama de proceso (SVG) ----------
  function layoutProceso(s) {
    var col = {}, ids = s.pasos.map(function (p) { return p.id; });
    var start = s.pasos.filter(function (p) { return p.tipo === "inicio"; }).map(function (p) { return p.id; });
    if (!start.length && ids.length) start = [ids[0]];
    start.forEach(function (i) { col[i] = 0; });
    var queue = start.slice(), guard = 0;
    while (queue.length && guard++ < 500) {
      var n = queue.shift();
      s.flujos.forEach(function (f) {
        if (f.de !== n) return;
        if (col[f.a] == null) { col[f.a] = col[n] + 1; queue.push(f.a); }
      });
    }
    var maxc = 0; ids.forEach(function (i) { if (col[i] == null) col[i] = ++maxc; maxc = Math.max(maxc, col[i]); });
    // evita dos pasos en la misma celda (columna y carril)
    var occ = {};
    s.pasos.forEach(function (p) { var k; while (occ[k = col[p.id] + "|" + p.carril]) col[p.id]++; occ[k] = 1; maxc = Math.max(maxc, col[p.id]); });
    return { col: col, ncol: maxc + 1 };
  }
  function procesoSvg(s, opt) {
    opt = opt || {};
    var L = layoutProceso(s), CW = 178, LH = 112, LX = 150, TOP = 74, BW = 136, BH = 50;
    var W = LX + L.ncol * CW + 30, H = TOP + s.carriles.length * LH + 92;
    var pos = {};
    s.pasos.forEach(function (p) { var li = s.carriles.indexOf(p.carril); pos[p.id] = { x: LX + L.col[p.id] * CW + CW / 2, y: TOP + li * LH + LH / 2, p: p }; });
    var o = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + W + " " + H + '" width="' + W + '" height="' + H + '" font-family="Arial, Helvetica, sans-serif">';
    o += '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#6A5A55"/></marker></defs>';
    o += '<rect width="' + W + '" height="' + H + '" fill="#FFFFFF"/>';
    o += '<text x="24" y="34" font-size="20" font-weight="700" fill="#22171A">' + esc(s.titulo) + "</text>";
    if (s.descripcion) o += '<text x="24" y="56" font-size="12.5" fill="#6A5A55">' + esc(clip(s.descripcion, 150)) + "</text>";
    s.carriles.forEach(function (c, i) {
      var y = TOP + i * LH;
      o += '<rect x="16" y="' + y + '" width="' + (W - 32) + '" height="' + LH + '" fill="' + (i % 2 ? "#FFFBF3" : "#F6EFE1") + '" stroke="#E4D6BC"/>';
      o += '<rect x="16" y="' + y + '" width="118" height="' + LH + '" fill="#EADBB8" fill-opacity=".55" stroke="#E4D6BC"/>';
      wrap(c, 15).forEach(function (ln, k, all) { o += '<text x="75" y="' + (y + LH / 2 + (k - (all.length - 1) / 2) * 15 + 4) + '" text-anchor="middle" font-size="12.5" font-weight="700" fill="#7A1F2E">' + esc(ln) + "</text>"; });
    });
    function edgePt(a, b) {
      var dx = b.x - a.x, dy = b.y - a.y, hw = a.p.tipo === "tarea" ? BW / 2 : a.p.tipo === "decision" ? 38 : 18, hh = a.p.tipo === "tarea" ? BH / 2 : a.p.tipo === "decision" ? 30 : 18;
      if (Math.abs(dx) * hh > Math.abs(dy) * hw) return { x: a.x + Math.sign(dx) * hw, y: a.y + dy * hw / Math.abs(dx || 1) * (a.p.tipo === "tarea" ? 1 : 0) };
      return { x: a.x + (a.p.tipo === "tarea" ? dx * hh / Math.abs(dy || 1) : 0), y: a.y + Math.sign(dy) * hh };
    }
    s.flujos.forEach(function (f) {
      var a = pos[f.de], b = pos[f.a]; if (!a || !b) return;
      var p1 = edgePt(a, b), p2 = edgePt(b, a), d;
      if (b.x <= a.x - 4) { var up = Math.min(a.y, b.y) - LH * 0.42; d = "M" + a.x + " " + (a.y - 20) + " C" + a.x + " " + up + " " + b.x + " " + up + " " + b.x + " " + (b.y - 22); }
      else if (Math.abs(a.y - b.y) < 2) d = "M" + p1.x + " " + p1.y + " L" + p2.x + " " + p2.y;
      else { var mx = (p1.x + p2.x) / 2; d = "M" + p1.x + " " + p1.y + " C" + mx + " " + p1.y + " " + mx + " " + p2.y + " " + p2.x + " " + p2.y; }
      o += '<path d="' + d + '" fill="none" stroke="#6A5A55" stroke-width="1.4" marker-end="url(#ah)"/>';
      if (f.etiqueta) { var lx = (p1.x + p2.x) / 2, ly = (p1.y + p2.y) / 2 - 6; if (b.x <= a.x - 4) { lx = (a.x + b.x) / 2; ly = Math.min(a.y, b.y) - LH * 0.36; } var tw = f.etiqueta.length * 6.2 + 10; o += '<rect x="' + (lx - tw / 2) + '" y="' + (ly - 11) + '" width="' + tw + '" height="16" rx="8" fill="#FFFFFF" stroke="#E4D6BC"/><text x="' + lx + '" y="' + (ly + 1) + '" text-anchor="middle" font-size="10.5" fill="#22171A">' + esc(f.etiqueta) + "</text>"; }
    });
    s.pasos.forEach(function (p) {
      var q = pos[p.id], A = ACTOR[p.actor] || ACTOR.persona;
      if (p.tipo === "inicio" || p.tipo === "fin") {
        o += '<circle cx="' + q.x + '" cy="' + q.y + '" r="17" fill="' + (p.tipo === "inicio" ? "#DDEFEA" : "#F3E2E1") + '" stroke="' + (p.tipo === "inicio" ? "#0B7A78" : "#7A1F2E") + '" stroke-width="' + (p.tipo === "fin" ? 4 : 2) + '"/>';
        wrap(p.nombre, 20).slice(0, 2).forEach(function (ln, k) { o += '<text x="' + q.x + '" y="' + (q.y + 32 + k * 13) + '" text-anchor="middle" font-size="11" fill="#22171A">' + esc(ln) + "</text>"; });
      } else if (p.tipo === "decision") {
        o += '<polygon points="' + q.x + "," + (q.y - 30) + " " + (q.x + 40) + "," + q.y + " " + q.x + "," + (q.y + 30) + " " + (q.x - 40) + "," + q.y + '" fill="#FBF4E6" stroke="#B07A2A" stroke-width="1.6"/>';
        wrap(p.nombre, 16).slice(0, 3).forEach(function (ln, k, all) { o += '<text x="' + q.x + '" y="' + (q.y + 44 + k * 12) + '" text-anchor="middle" font-size="10.5" fill="#22171A">' + esc(ln) + "</text>"; });
        o += '<text x="' + q.x + '" y="' + (q.y + 5) + '" text-anchor="middle" font-size="15" font-weight="700" fill="#B07A2A">?</text>';
      } else {
        o += '<rect x="' + (q.x - BW / 2) + '" y="' + (q.y - BH / 2) + '" width="' + BW + '" height="' + BH + '" rx="11" fill="' + A.fill + '" stroke="' + A.stroke + '" stroke-width="1.6"/>';
        var ls = wrap(p.nombre, 20).slice(0, 3);
        ls.forEach(function (ln, k) { o += '<text x="' + q.x + '" y="' + (q.y + (k - (ls.length - 1) / 2) * 13 + 4) + '" text-anchor="middle" font-size="11.5" fill="#22171A">' + esc(ln) + "</text>"; });
        o += '<text x="' + (q.x + BW / 2 - 6) + '" y="' + (q.y - BH / 2 + 11) + '" text-anchor="end" font-size="8.5" font-weight="700" fill="' + A.stroke + '">' + esc(A.n.split(" ")[0].toUpperCase()) + "</text>";
      }
    });
    var ly0 = TOP + s.carriles.length * LH + 30, lx0 = 24;
    o += '<text x="' + lx0 + '" y="' + ly0 + '" font-size="11" font-weight="700" fill="#6A5A55">QUIÉN HACE CADA PASO</text>';
    Object.keys(ACTOR).forEach(function (k, i) { var A = ACTOR[k], x = lx0 + 180 + i * 150; o += '<rect x="' + x + '" y="' + (ly0 - 11) + '" width="22" height="14" rx="4" fill="' + A.fill + '" stroke="' + A.stroke + '"/><text x="' + (x + 30) + '" y="' + ly0 + '" font-size="11" fill="#22171A">' + esc(A.n) + "</text>"; });
    o += '<text x="' + lx0 + '" y="' + (ly0 + 26) + '" font-size="10" fill="#6A5A55">varios · ' + esc(opt.proyecto || "oficina de agentes") + " · borrador del " + esc(opt.fecha || hoy()) + ". La IA propone; las decisiones las toma una persona.</text>";
    return o + "</svg>";
  }
  function wrap(t, n) { var w = str(t).split(/\s+/), out = [], cur = ""; w.forEach(function (x) { if ((cur + " " + x).trim().length > n && cur) { out.push(cur); cur = x; } else cur = (cur + " " + x).trim(); }); if (cur) out.push(cur); return out.length ? out : [""]; }
  function svgToPng(svg, scale) {
    return new Promise(function (res, rej) {
      var m = svg.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/), W = m ? +m[1] : 1200, H = m ? +m[2] : 600, k = scale || 2;
      var img = new Image(), url = URL.createObjectURL(new Blob([svg], { type: "image/svg+xml" }));
      img.onload = function () { var c = document.createElement("canvas"); c.width = W * k; c.height = H * k; var x = c.getContext("2d"); x.fillStyle = "#fff"; x.fillRect(0, 0, c.width, c.height); x.drawImage(img, 0, 0, c.width, c.height); URL.revokeObjectURL(url); c.toBlob(function (b) { b ? res(b) : rej(new Error("png")); }, "image/png"); };
      img.onerror = function () { URL.revokeObjectURL(url); rej(new Error("svg")); };
      img.src = url;
    });
  }

  // ---------- Presentación (.pptx) ----------
  async function buildPptx(s, meta) {
    var P = await need("pptx"), pptx = new P();
    pptx.layout = "LAYOUT_WIDE"; pptx.author = "Varios · " + (meta.autor || "oficina de agentes"); pptx.company = "Varios"; pptx.title = s.titulo; pptx.subject = meta.proyecto || "";
    var logo = logoPng(true), logoW = logoPng(true, true), F = T.font, foot = "varios · " + (meta.proyecto || "oficina de agentes") + " · borrador";
    pptx.defineSlideMaster({ title: "VARIOS", background: { color: "FFFFFF" }, objects: [
      { line: { x: 0.6, y: 6.95, w: 12.13, h: 0, line: { color: T.hair, width: 0.75 } } },
      { image: { data: logo.url, x: 0.6, y: 7.04, w: 0.22 * logo.w / logo.h, h: 0.22 } },
      { text: { text: foot, options: { x: 1.75, y: 7.0, w: 8, h: 0.3, fontFace: F, fontSize: 9, color: T.mut } } }
    ], slideNumber: { x: 12.15, y: 7.0, w: 0.6, h: 0.3, fontFace: F, fontSize: 9, color: T.mut, align: "right" } });
    function motif(sl, x, y, h, light) {
      var cs = light ? ["FFFFFF", "FFFFFF", "FFFFFF"] : [T.wine, T.acc, T.champ], tr = light ? [70, 82, 76] : [0, 0, 0], w = 0.62, g = 0.26;
      [[0, 1, 0], [1, 0.72, 1], [2, 0.84, 0.5]].forEach(function (b) { var hh = h * b[1]; sl.addShape(pptx.ShapeType.roundRect, { x: x + b[0] * (w + g), y: y + (b[2] === 1 ? h - hh : b[2] === 0.5 ? (h - hh) / 2 : 0), w: w, h: hh, rectRadius: 0.3, fill: { color: cs[b[0]], transparency: tr[b[0]] }, line: { type: "none" } }); });
    }
    function head(sl, x) { if (x.antetitulo) sl.addText(x.antetitulo.toUpperCase(), { x: 0.6, y: 0.45, w: 12, h: 0.35, fontFace: F, fontSize: 12, bold: true, color: T.acc, charSpacing: 1.5 }); sl.addText(x.titulo, { x: 0.6, y: 0.8, w: 12.1, h: 1.0, fontFace: F, fontSize: 28, bold: true, color: T.ink, valign: "top", fit: "shrink" }); }
    function bullets(list, size) { return list.map(function (p) { return { text: p, options: { bullet: { code: "25AA", indent: 18 }, color: T.ink, paraSpaceAfter: 10 } }; }); }
    s.slides.forEach(function (x, i) {
      var sl;
      if (x.tipo === "portada") {
        sl = pptx.addSlide(); sl.background = { color: T.surf };
        sl.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: 0.32, h: 7.5, fill: { color: T.wine }, line: { type: "none" } });
        sl.addImage({ data: logo.url, x: 0.9, y: 0.7, w: 0.42 * logo.w / logo.h, h: 0.42 });
        sl.addText((x.antetitulo || meta.proyecto || "Varios").toUpperCase(), { x: 0.9, y: 3.35, w: 8.6, h: 0.4, fontFace: F, fontSize: 13, bold: true, color: T.acc, charSpacing: 2 });
        sl.addText(x.titulo || s.titulo, { x: 0.9, y: 3.75, w: 8.6, h: 1.7, fontFace: F, fontSize: 38, bold: true, color: T.ink, valign: "top", fit: "shrink" });
        if (s.subtitulo) sl.addText(s.subtitulo, { x: 0.9, y: 5.5, w: 8.6, h: 0.7, fontFace: F, fontSize: 17, color: T.mut, valign: "top" });
        sl.addText("Borrador · " + (meta.fecha || hoy()) + (meta.cliente ? " · " + meta.cliente : "") + (meta.autor ? " · " + meta.autor : ""), { x: 0.9, y: 6.7, w: 9, h: 0.35, fontFace: F, fontSize: 11, color: T.mut });
        motif(sl, 10.05, 1.3, 4.6, false);
      } else if (x.tipo === "seccion") {
        sl = pptx.addSlide(); sl.background = { color: T.wine };
        if (x.antetitulo) sl.addText(x.antetitulo.toUpperCase(), { x: 0.9, y: 2.9, w: 9, h: 0.4, fontFace: F, fontSize: 13, bold: true, color: T.champ, charSpacing: 2 });
        sl.addText(x.titulo, { x: 0.9, y: 3.3, w: 9, h: 1.6, fontFace: F, fontSize: 34, bold: true, color: "FFFFFF", valign: "top", fit: "shrink" });
        sl.addImage({ data: logoW.url, x: 0.9, y: 6.75, w: 0.26 * logoW.w / logoW.h, h: 0.26 });
        motif(sl, 10.3, 1.6, 4.2, true);
      } else if (x.tipo === "cierre") {
        sl = pptx.addSlide({ masterName: "VARIOS" }); sl.background = { color: T.surf };
        sl.addText((x.antetitulo || "Siguientes pasos").toUpperCase(), { x: 0.6, y: 0.45, w: 12, h: 0.35, fontFace: F, fontSize: 12, bold: true, color: T.acc, charSpacing: 1.5 });
        sl.addText(x.titulo || "Siguientes pasos.", { x: 0.6, y: 0.8, w: 8.6, h: 1.0, fontFace: F, fontSize: 28, bold: true, color: T.ink, valign: "top", fit: "shrink" });
        if (x.puntos.length) sl.addText(bullets(x.puntos), { x: 0.6, y: 2.0, w: 8.4, h: 4.3, fontFace: F, fontSize: 17, valign: "top" });
        sl.addText("Borrador generado en la oficina de agentes de Varios. Revisar antes de usar. Sin datos reales de clientes.", { x: 0.6, y: 6.45, w: 12, h: 0.35, fontFace: F, fontSize: 10, italic: true, color: T.mut });
        motif(sl, 10.3, 1.7, 3.6, false);
      } else {
        sl = pptx.addSlide({ masterName: "VARIOS" }); head(sl, x);
        if (x.tipo === "dos_columnas") {
          [x.izquierda, x.derecha].forEach(function (c, k) {
            var cx = 0.6 + k * 6.17;
            sl.addShape(pptx.ShapeType.roundRect, { x: cx, y: 2.0, w: 5.95, h: 4.6, rectRadius: 0.12, fill: { color: T.card }, line: { color: T.hair, width: 0.75 } });
            sl.addText(c.titulo || "", { x: cx + 0.3, y: 2.2, w: 5.4, h: 0.5, fontFace: F, fontSize: 17, bold: true, color: T.wine });
            sl.addText(bullets(c.puntos), { x: cx + 0.3, y: 2.8, w: 5.4, h: 3.6, fontFace: F, fontSize: 14, valign: "top" });
          });
        } else if (x.tipo === "cifras" && x.cifras.length) {
          var n = x.cifras.length, w = (12.13 - (n - 1) * 0.3) / n;
          x.cifras.forEach(function (c, k) {
            var cx = 0.6 + k * (w + 0.3);
            sl.addShape(pptx.ShapeType.roundRect, { x: cx, y: 2.3, w: w, h: 3.0, rectRadius: 0.12, fill: { color: T.card }, line: { color: T.hair, width: 0.75 } });
            sl.addText(c.valor, { x: cx + 0.2, y: 2.6, w: w - 0.4, h: 1.3, fontFace: F, fontSize: 48, bold: true, color: T.acc, fit: "shrink" });
            sl.addText(c.etiqueta, { x: cx + 0.2, y: 3.95, w: w - 0.4, h: 1.1, fontFace: F, fontSize: 14, color: T.mut, valign: "top" });
          });
          if (x.puntos.length) sl.addText(x.puntos.join("  ·  "), { x: 0.6, y: 5.6, w: 12.1, h: 0.8, fontFace: F, fontSize: 13, color: T.ink });
        } else if (x.tipo === "tabla" && x.tabla.cabecera.length) {
          var rows = [x.tabla.cabecera.map(function (c) { return { text: c, options: { bold: true, color: "FFFFFF", fill: { color: T.wine } } }; })];
          x.tabla.filas.forEach(function (r, ri) { rows.push(x.tabla.cabecera.map(function (_, ci) { return { text: str(r[ci]), options: { color: T.ink, fill: { color: ri % 2 ? T.card : "FFFFFF" } } }; })); });
          sl.addTable(rows, { x: 0.6, y: 2.0, w: 12.13, fontFace: F, fontSize: x.tabla.filas.length > 7 ? 11 : 13, border: { type: "solid", pt: 0.5, color: T.hair }, valign: "middle", margin: 0.08 });
        } else {
          var pts = x.puntos.length ? x.puntos : ["[POR CONFIRMAR]"];
          sl.addText(bullets(pts), { x: 0.6, y: 2.0, w: 11.8, h: 4.7, fontFace: F, fontSize: pts.length > 5 ? 16 : 19, valign: "top" });
        }
      }
      if (x.notas) sl.addNotes(x.notas);
    });
    if (s.fuentes.length) {
      var sf = pptx.addSlide({ masterName: "VARIOS" }); head(sf, { antetitulo: "Fuentes", titulo: "De dónde sale lo que se afirma." });
      sf.addText(s.fuentes.map(function (f) { return { text: f, options: { bullet: true, color: T.ink, paraSpaceAfter: 6 } }; }), { x: 0.6, y: 2.0, w: 12, h: 4.7, fontFace: F, fontSize: 12, valign: "top" });
    }
    return await pptx.write({ outputType: "blob" });
  }

  // ---------- Hoja de cálculo (.xlsx) ----------
  function toNum(v) {
    if (typeof v === "number") return v;
    var t = str(v).trim().replace(/[€%\s]/g, "");
    if (!t || /[a-z]/i.test(t)) return null;
    if (/^-?\d{1,3}(\.\d{3})+(,\d+)?$/.test(t)) t = t.replace(/\./g, "").replace(",", ".");
    else if (/^-?\d+,\d+$/.test(t)) t = t.replace(",", ".");
    var n = Number(t); return isFinite(n) ? n : null;
  }
  function toDate(v) { var m = str(v).match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})$/); if (m) return new Date(Date.UTC(+m[3], +m[2] - 1, +m[1])); m = str(v).match(/^(\d{4})-(\d{2})-(\d{2})/); return m ? new Date(Date.UTC(+m[1], +m[2] - 1, +m[3])) : null; }
  var FMT = { numero: "#,##0.##", euros: '#,##0.00 "€"', porcentaje: "0.0%", fecha: "dd/mm/yyyy" };
  function cellVal(v, tipo) {
    if (v === "" || v == null) return null;
    if (typeof v === "string" && /^=/.test(v.trim())) return { formula: v.trim().slice(1) };
    if (tipo === "fecha") return toDate(v) || (v == null ? null : str(v));
    if (tipo === "numero" || tipo === "euros" || tipo === "porcentaje") { var n = toNum(v); if (n == null) return v == null || v === "" ? null : str(v); if (tipo === "porcentaje" && /%/.test(str(v))) n = n / 100; else if (tipo === "porcentaje" && Math.abs(n) > 1.5) n = n / 100; return n; }
    return v == null ? null : str(v);
  }
  async function buildXlsx(s, meta) {
    var X = await need("xlsx"), wb = new X.Workbook(), F = T.font;
    wb.creator = "Varios · " + (meta.autor || "oficina de agentes"); wb.created = new Date(); wb.title = s.titulo;
    var argb = function (h) { return "FF" + h; };
    var cov = wb.addWorksheet("Portada", { views: [{ showGridLines: false }], properties: { tabColor: { argb: argb(T.wine) } } });
    cov.getColumn(1).width = 3; cov.getColumn(2).width = 26; cov.getColumn(3).width = 70;
    var lg = logoPng(true), img = wb.addImage({ base64: lg.url, extension: "png" });
    cov.addImage(img, { tl: { col: 1, row: 1 }, ext: { width: lg.w * 1.6, height: lg.h * 1.6 } });
    cov.getCell("B5").value = s.titulo; cov.getCell("B5").font = { name: F, size: 20, bold: true, color: { argb: argb(T.ink) } };
    if (s.subtitulo) { cov.getCell("B6").value = s.subtitulo; cov.getCell("B6").font = { name: F, size: 12, color: { argb: argb(T.mut) } }; }
    var info = [["Proyecto", meta.proyecto || "—"], ["Cliente", meta.cliente || "—"], ["Preparado por", meta.autor || "Oficina de agentes de Varios"], ["Fecha", meta.fecha || hoy()], ["Versión", "v" + (meta.version || 1)], ["Estado", "Borrador. Revisar antes de usar."]];
    info.forEach(function (r, i) { var a = cov.getCell("B" + (8 + i)), b = cov.getCell("C" + (8 + i)); a.value = r[0]; b.value = r[1]; a.font = { name: F, size: 10, bold: true, color: { argb: argb(T.wine) } }; b.font = { name: F, size: 10, color: { argb: argb(T.ink) } }; a.border = b.border = { bottom: { style: "thin", color: { argb: argb(T.hair) } } }; });
    var r0 = 8 + info.length + 2;
    cov.getCell("B" + r0).value = "CÓMO USAR ESTE LIBRO"; cov.getCell("B" + r0).font = { name: F, size: 10, bold: true, color: { argb: argb(T.acc) } };
    s.hojas.forEach(function (h, i) { var a = cov.getCell("B" + (r0 + 1 + i)), b = cov.getCell("C" + (r0 + 1 + i)); a.value = { text: h.nombre, hyperlink: "#'" + h.nombre + "'!A1" }; a.font = { name: F, size: 10, bold: true, color: { argb: argb(T.acc) }, underline: true }; b.value = h.descripcion || ""; b.font = { name: F, size: 10, color: { argb: argb(T.ink) } }; b.alignment = { wrapText: true, vertical: "top" }; });
    var rn = r0 + 2 + s.hojas.length;
    cov.getCell("B" + rn).value = "Celdas con fondo champán: datos que rellenas tú. Fila de total: fórmulas."; cov.getCell("B" + rn).font = { name: F, size: 9, italic: true, color: { argb: argb(T.mut) } };
    s.notas.forEach(function (n, i) { var c = cov.getCell("B" + (rn + 2 + i)); c.value = "· " + n; c.font = { name: F, size: 9, color: { argb: argb(T.mut) } }; cov.mergeCells("B" + (rn + 2 + i) + ":C" + (rn + 2 + i)); });

    s.hojas.forEach(function (h) {
      var ws = wb.addWorksheet(h.nombre, { views: [{ state: "frozen", ySplit: 4, showGridLines: false }], properties: { tabColor: { argb: argb(T.acc) } } });
      var nc = h.columnas.length;
      ws.getCell("A1").value = h.nombre; ws.getCell("A1").font = { name: F, size: 14, bold: true, color: { argb: argb(T.wine) } };
      if (h.descripcion) { ws.getCell("A2").value = h.descripcion; ws.getCell("A2").font = { name: F, size: 10, italic: true, color: { argb: argb(T.mut) } }; }
      var hr = ws.getRow(4);
      h.columnas.forEach(function (c, i) {
        var cell = hr.getCell(i + 1); cell.value = c.nombre;
        cell.font = { name: F, size: 10, bold: true, color: { argb: "FFFFFFFF" } }; cell.fill = { type: "pattern", pattern: "solid", fgColor: { argb: argb(T.wine) } };
        cell.alignment = { vertical: "middle", wrapText: true }; cell.border = { bottom: { style: "thin", color: { argb: argb(T.wine) } } };
        var maxLen = Math.max(c.nombre.length, h.filas.reduce(function (m, r) { return Math.max(m, str(r[i]).length); }, 0));
        ws.getColumn(i + 1).width = c.ancho || Math.max(10, Math.min(50, maxLen + 3));
      });
      hr.height = 22;
      h.filas.forEach(function (r, ri) {
        var row = ws.getRow(5 + ri);
        h.columnas.forEach(function (c, ci) {
          var cell = row.getCell(ci + 1); cell.value = cellVal(r[ci], c.tipo);
          cell.font = { name: F, size: 10, color: { argb: argb(T.ink) } };
          if (FMT[c.tipo]) cell.numFmt = FMT[c.tipo];
          cell.alignment = { vertical: "top", wrapText: c.tipo === "texto" };
          cell.border = { bottom: { style: "hair", color: { argb: argb(T.hair) } } };
          if (c.entrada) cell.fill = { type: "pattern", pattern: "solid", fgColor: { argb: argb(T.champT) } };
        });
      });
      var last = 4 + h.filas.length;
      if (nc) ws.autoFilter = { from: { row: 4, column: 1 }, to: { row: Math.max(4, last), column: nc } };
      var nums = h.columnas.map(function (c, i) { return (c.tipo === "numero" || c.tipo === "euros") ? i : -1; }).filter(function (i) { return i >= 0; });
      if (h.totales && nums.length && h.filas.length) {
        var tr = ws.getRow(last + 1);
        tr.getCell(1).value = nums[0] === 0 ? null : "Total";
        nums.forEach(function (i) { var L = ws.getColumn(i + 1).letter, c = tr.getCell(i + 1); c.value = { formula: "SUM(" + L + "5:" + L + last + ")" }; c.numFmt = FMT[h.columnas[i].tipo]; });
        for (var k = 1; k <= nc; k++) { var c2 = tr.getCell(k); c2.font = { name: F, size: 10, bold: true, color: { argb: argb(T.ink) } }; c2.fill = { type: "pattern", pattern: "solid", fgColor: { argb: argb(T.champ) } }; c2.border = { top: { style: "thin", color: { argb: argb(T.wine) } } }; }
      }
      ws.pageSetup = { orientation: nc > 6 ? "landscape" : "portrait", fitToPage: true, fitToWidth: 1, fitToHeight: 0 };
      ws.headerFooter = { oddFooter: "&L&8varios · " + str(meta.proyecto || "oficina de agentes").replace(/&/g, "&&") + " · borrador&R&8&P / &N" };
    });
    var buf = await wb.xlsx.writeBuffer();
    return new Blob([buf], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
  }

  // ---------- Documento (.docx) ----------
  function runs(D, text, base) {
    base = base || {};
    return str(text).split(/(\*\*[^*]+\*\*)/).filter(Boolean).map(function (part) {
      var b = /^\*\*[^*]+\*\*$/.test(part);
      return new D.TextRun(Object.assign({}, base, { text: b ? part.slice(2, -2) : part.replace(/`/g, ""), bold: b || base.bold }));
    });
  }
  async function buildDocx(s, meta) {
    var D = await need("docx"), F = T.font;
    var lg = logoPng(true), logoBytes = b64ToBytes(lg.url);
    var hairB = { style: D.BorderStyle.SINGLE, size: 4, color: T.hair }, none = { style: D.BorderStyle.NONE, size: 0, color: "FFFFFF" };
    function logoRun(h) { return new D.ImageRun({ type: "png", data: logoBytes, transformation: { width: Math.round(h * lg.w / lg.h), height: h } }); }
    function para(text, o) { o = o || {}; return new D.Paragraph({ spacing: { after: o.after == null ? 120 : o.after, before: o.before || 0 }, alignment: o.align, children: runs(D, text, { font: F, size: o.size || 21, color: o.color || T.ink, bold: o.bold, italics: o.italics, characterSpacing: o.cs }) }); }
    function table(cab, filas) {
      var n = cab.length || (filas[0] || []).length || 1, wpct = Math.floor(100 / n);
      var mk = function (txt, head, i) { return new D.TableCell({ width: { size: wpct, type: D.WidthType.PERCENTAGE }, margins: { top: 60, bottom: 60, left: 90, right: 90 }, shading: head ? { type: D.ShadingType.CLEAR, color: "auto", fill: T.wine } : (i % 2 ? { type: D.ShadingType.CLEAR, color: "auto", fill: T.card } : undefined), borders: { top: none, left: none, right: none, bottom: head ? { style: D.BorderStyle.SINGLE, size: 6, color: T.wine } : hairB }, children: [new D.Paragraph({ children: runs(D, txt, { font: F, size: head ? 18 : 19, bold: head, color: head ? "FFFFFF" : T.ink }) })] }); };
      var rows = [];
      if (cab.length) rows.push(new D.TableRow({ tableHeader: true, children: cab.map(function (c) { return mk(c, true, 0); }) }));
      filas.forEach(function (r, i) { var cells = []; for (var k = 0; k < n; k++) cells.push(mk(str(r[k]), false, i)); rows.push(new D.TableRow({ children: cells })); });
      return new D.Table({ width: { size: 100, type: D.WidthType.PERCENTAGE }, rows: rows, borders: { top: none, bottom: none, left: none, right: none, insideHorizontal: hairB, insideVertical: none } });
    }
    function nota(t, x) { return new D.Paragraph({ shading: { type: D.ShadingType.CLEAR, color: "auto", fill: T.champT }, border: { left: { style: D.BorderStyle.SINGLE, size: 0, color: T.champT } }, indent: { left: 200, right: 200 }, spacing: { before: 120, after: 160 }, children: [new D.TextRun({ text: (t || "Nota").toUpperCase() + "  ", font: F, size: 17, bold: true, color: T.wine })].concat(runs(D, x, { font: F, size: 20, color: T.ink })) }); }

    var cover = [
      new D.Paragraph({ children: [logoRun(30)], spacing: { after: 1800 } }),
      para((meta.proyecto || "Varios").toUpperCase() + (meta.cliente ? " · " + meta.cliente.toUpperCase() : ""), { size: 18, bold: true, color: T.acc, cs: 30, after: 160 }),
      para(s.titulo, { size: 56, bold: true, after: 200 }),
      s.subtitulo ? para(s.subtitulo, { size: 28, color: T.mut, after: 600 }) : para("", { after: 600 }),
      table([], [["Preparado por", meta.autor || "Oficina de agentes de Varios"], ["Fecha", meta.fecha || hoy()], ["Versión", "v" + (meta.version || 1)], ["Estado", "Borrador. Revisar antes de usar."]]),
      new D.Paragraph({ spacing: { before: 600 }, children: [] }),
      nota("Aviso", "Documento generado en la oficina de agentes de Varios. No contiene datos reales de clientes. Lo marcado como [POR CONFIRMAR] falta verificarlo.")
    ];
    var body = [];
    if (s.resumen) { body.push(para("RESUMEN", { size: 17, bold: true, color: T.acc, cs: 30, after: 80 })); body.push(para(s.resumen, { size: 23, after: 240 })); }
    s.secciones.forEach(function (sec, i) {
      body.push(new D.Paragraph({ spacing: { before: 320, after: 0 }, keepNext: true, children: [new D.TextRun({ text: ("0" + (i + 1)).slice(-2), font: F, size: 17, bold: true, color: T.acc, characterSpacing: 30 })] }));
      body.push(new D.Paragraph({ heading: D.HeadingLevel.HEADING_1, keepNext: true, spacing: { before: 40, after: 140 }, children: [new D.TextRun({ text: sec.titulo, font: F, size: 32, bold: true, color: T.wine })] }));
      sec.bloques.forEach(function (b) {
        if (b.tipo === "lista") b.items.forEach(function (it) { body.push(new D.Paragraph({ numbering: { reference: "vpunto", level: 0 }, spacing: { after: 80 }, children: runs(D, it, { font: F, size: 21, color: T.ink }) })); });
        else if (b.tipo === "tabla") { body.push(table(b.cabecera, b.filas)); body.push(para("", { after: 120 })); }
        else if (b.tipo === "nota") body.push(nota(b.titulo, b.texto));
        else str(b.texto).split(/\n{2,}/).forEach(function (p) { if (p.trim()) body.push(para(p.trim())); });
      });
    });
    if (s.fuentes.length) {
      body.push(new D.Paragraph({ heading: D.HeadingLevel.HEADING_1, spacing: { before: 360, after: 140 }, children: [new D.TextRun({ text: "Fuentes", font: F, size: 32, bold: true, color: T.wine })] }));
      s.fuentes.forEach(function (f) { body.push(new D.Paragraph({ numbering: { reference: "vpunto", level: 0 }, children: runs(D, f, { font: F, size: 19, color: T.ink }) })); });
    }
    var doc = new D.Document({
      creator: "Varios", title: s.titulo, description: "Borrador · " + (meta.proyecto || ""),
      styles: { default: { document: { run: { font: F, size: 21, color: T.ink } } }, paragraphStyles: [{ id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: F, size: 32, bold: true, color: T.wine } }] },
      numbering: { config: [{ reference: "vpunto", levels: [{ level: 0, format: D.LevelFormat.BULLET, text: "▪", alignment: D.AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 260 } }, run: { color: T.acc } } }] }] },
      sections: [
        { properties: { page: { margin: { top: 1418, bottom: 1418, left: 1418, right: 1418 } } }, children: cover },
        { properties: { page: { margin: { top: 1418, bottom: 1300, left: 1418, right: 1418 } } },
          headers: { default: new D.Header({ children: [new D.Paragraph({ tabStops: [{ type: D.TabStopType.RIGHT, position: 9070 }], border: { bottom: { style: D.BorderStyle.SINGLE, size: 4, color: T.hair, space: 4 } }, children: [logoRun(14), new D.TextRun({ text: "\tBorrador · " + (meta.proyecto || s.titulo), font: F, size: 16, color: T.mut })] })] }) },
          footers: { default: new D.Footer({ children: [new D.Paragraph({ tabStops: [{ type: D.TabStopType.RIGHT, position: 9070 }], children: [new D.TextRun({ text: "Varios · oficina de agentes", font: F, size: 16, color: T.mut }), new D.TextRun({ children: ["\t", D.PageNumber.CURRENT, " / ", D.PageNumber.TOTAL_PAGES], font: F, size: 16, color: T.mut })] })] }) },
          children: body.length ? body : [para("[POR CONFIRMAR]")] }
      ]
    });
    return await D.Packer.toBlob(doc);
  }

  // ---------- Construir y vista previa ----------
  async function build(kind, spec, meta, fmt) {
    meta = Object.assign({ fecha: hoy(), version: 1 }, meta || {}); meta.titulo = meta.titulo || spec.titulo;
    var s = norm(kind, JSON.parse(JSON.stringify(spec || {})));
    if (kind === "pptx") return { blob: await buildPptx(s, meta), filename: fileName(kind, meta) };
    if (kind === "xlsx") return { blob: await buildXlsx(s, meta), filename: fileName(kind, meta) };
    if (kind === "docx") return { blob: await buildDocx(s, meta), filename: fileName(kind, meta) };
    if (kind === "proceso") {
      var svg = procesoSvg(s, meta);
      if (fmt === "png") return { blob: await svgToPng(svg, 2), filename: fileName(kind, meta, "png") };
      if (fmt === "xlsx") {
        var sheet = { titulo: s.titulo, subtitulo: "Pasos del proceso", hojas: [{ nombre: "Pasos", descripcion: s.descripcion, columnas: [{ nombre: "Paso", tipo: "texto", ancho: 8 }, { nombre: "Nombre", tipo: "texto", ancho: 40 }, { nombre: "Quién", tipo: "texto", ancho: 24 }, { nombre: "Tipo", tipo: "texto", ancho: 12 }, { nombre: "Lo hace", tipo: "texto", ancho: 16 }, { nombre: "Sigue a", tipo: "texto", ancho: 30 }], filas: s.pasos.map(function (p) { return [p.id, p.nombre, p.carril, p.tipo, (ACTOR[p.actor] || {}).n, s.flujos.filter(function (f) { return f.de === p.id; }).map(function (f) { return f.a + (f.etiqueta ? " (" + f.etiqueta + ")" : ""); }).join(", ")]; }), totales: false }], notas: s.notas };
        return { blob: await buildXlsx(norm("xlsx", sheet), meta), filename: fileName(kind, meta, "xlsx") };
      }
      return { blob: new Blob([svg], { type: "image/svg+xml" }), filename: fileName(kind, meta, "svg") };
    }
    throw new Error("Formato desconocido: " + kind);
  }

  var CSS = '.ve-sl{position:relative;aspect-ratio:16/9;border:1px solid var(--hairline);border-radius:12px;overflow:hidden;background:#fff;color:#22171A;container-type:inline-size;font-family:Arial,Helvetica,sans-serif;margin-bottom:12px}' +
    '.ve-sl .in{position:absolute;inset:0;padding:5.5cqw 4.5cqw 6cqw}.ve-sl .ant{font-size:1.25cqw;font-weight:700;letter-spacing:.12em;color:#0B7A78;text-transform:uppercase}.ve-sl .tt{font-size:2.6cqw;font-weight:700;line-height:1.15;margin:.6cqw 0 2cqw}' +
    '.ve-sl ul{margin:0;padding-left:2.2cqw;font-size:1.65cqw;line-height:1.45}.ve-sl li{margin-bottom:.8cqw}.ve-sl li::marker{color:#0B7A78}.ve-sl .ft{position:absolute;left:4.5cqw;right:4.5cqw;bottom:1.6cqw;border-top:1px solid #E4D6BC;padding-top:.8cqw;font-size:.9cqw;color:#6A5A55;display:flex;justify-content:space-between}' +
    '.ve-sl.cov{background:#F6EFE1}.ve-sl.cov::before{content:"";position:absolute;left:0;top:0;bottom:0;width:2.4cqw;background:#7A1F2E}.ve-sl.cov .tt{font-size:3.6cqw;max-width:62%}.ve-sl.cov .in{padding-top:32cqh}.ve-sl.sec{background:#7A1F2E;color:#fff}.ve-sl.sec .ant{color:#EADBB8}.ve-sl.sec .in{padding-top:36cqh}.ve-sl.sec .tt{font-size:3.2cqw;max-width:68%}' +
    '.ve-mo{position:absolute;right:7cqw;top:17%;height:62%;display:flex;gap:2cqw}.ve-mo i{display:block;width:4.6cqw;border-radius:2.3cqw}.ve-mo i:nth-child(1){height:100%;background:#7A1F2E}.ve-mo i:nth-child(2){height:72%;align-self:flex-end;background:#0B7A78}.ve-mo i:nth-child(3){height:84%;align-self:center;background:#EADBB8}.ve-sl.sec .ve-mo i{background:rgba(255,255,255,.25)!important}' +
    '.ve-two{display:grid;grid-template-columns:1fr 1fr;gap:1.6cqw}.ve-two>div{background:#FFFBF3;border:1px solid #E4D6BC;border-radius:1cqw;padding:1.6cqw}.ve-two b{display:block;color:#7A1F2E;font-size:1.6cqw;margin-bottom:.8cqw}.ve-two ul{font-size:1.35cqw}' +
    '.ve-fig{display:grid;gap:1.6cqw;grid-auto-flow:column;grid-auto-columns:1fr}.ve-fig>div{background:#FFFBF3;border:1px solid #E4D6BC;border-radius:1cqw;padding:2cqw 1.6cqw}.ve-fig b{display:block;font-size:4.2cqw;color:#0B7A78}.ve-fig span{font-size:1.3cqw;color:#6A5A55}' +
    '.ve-sl table{border-collapse:collapse;width:100%;font-size:1.2cqw}.ve-sl th{background:#7A1F2E;color:#fff;text-align:left;padding:.6cqw}.ve-sl td{border-bottom:1px solid #E4D6BC;padding:.6cqw}' +
    '.ve-doc{background:#fff;color:#22171A;border:1px solid var(--hairline);border-radius:12px;padding:34px 40px;font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:1.55;max-width:820px}.ve-doc .ant{font-size:11px;font-weight:700;letter-spacing:.12em;color:#0B7A78;text-transform:uppercase;margin-top:22px}.ve-doc h1{font-size:28px;margin:6px 0 4px}.ve-doc h2{font-size:20px;color:#7A1F2E;margin:2px 0 8px}.ve-doc .sub{color:#6A5A55;font-size:16px}.ve-doc table{border-collapse:collapse;width:100%;margin:8px 0 14px;font-size:13px}.ve-doc th{background:#7A1F2E;color:#fff;text-align:left;padding:6px 8px}.ve-doc td{border-bottom:1px solid #E4D6BC;padding:6px 8px}.ve-doc .nt{background:#FBF4E6;border-radius:8px;padding:10px 12px;margin:10px 0}.ve-doc .nt b{color:#7A1F2E;font-size:11px;letter-spacing:.08em;text-transform:uppercase;margin-right:6px}.ve-doc li::marker{color:#0B7A78}.ve-doc .hd{display:flex;justify-content:space-between;color:#6A5A55;font-size:11px;border-bottom:1px solid #E4D6BC;padding-bottom:6px;margin-bottom:18px}' +
    '.ve-xl .tabs{display:flex;gap:4px;flex-wrap:wrap;margin-bottom:8px}.ve-xl .tabs button{border:1px solid var(--hairline);background:var(--card);border-radius:8px 8px 0 0;padding:5px 10px;font-size:12.5px;cursor:pointer;color:var(--ink)}.ve-xl .tabs button[aria-selected=true]{background:#7A1F2E;color:#fff;border-color:#7A1F2E}.ve-xl .grid{overflow:auto;border:1px solid var(--hairline);border-radius:10px;background:#fff;max-height:460px}.ve-xl table{border-collapse:collapse;font-family:Arial,Helvetica,sans-serif;font-size:12.5px;color:#22171A;min-width:100%}.ve-xl th{position:sticky;top:0;background:#7A1F2E;color:#fff;text-align:left;padding:6px 8px;white-space:nowrap}.ve-xl td{border-bottom:1px solid #E4D6BC;border-right:1px solid #F1E8D6;padding:5px 8px;vertical-align:top}.ve-xl td.n{text-align:right;font-variant-numeric:tabular-nums}.ve-xl td.in{background:#FBF4E6}.ve-xl tr.tot td{background:#EADBB8;font-weight:700}.ve-xl .rn{background:#F6EFE1;color:#6A5A55;text-align:right;width:34px}' +
    '.ve-pr{overflow:auto;border:1px solid var(--hairline);border-radius:12px;background:#fff}.ve-pr svg{display:block;width:100%;height:auto;min-width:860px}';
  function injectCss() { if (document.getElementById("ve-css")) return; var st = document.createElement("style"); st.id = "ve-css"; st.textContent = CSS; document.head.appendChild(st); }

  function fmtCell(v, tipo) {
    if (typeof v === "string" && /^=/.test(v.trim())) return "ƒ " + v.trim().slice(1);
    if (tipo === "euros") { var n = toNum(v); return n == null ? str(v) : n.toLocaleString("es-ES", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + " €"; }
    if (tipo === "porcentaje") { var p = cellVal(v, "porcentaje"); return typeof p === "number" ? (p * 100).toLocaleString("es-ES", { maximumFractionDigits: 1 }) + " %" : str(v); }
    if (tipo === "numero") { var q = toNum(v); return q == null ? str(v) : q.toLocaleString("es-ES"); }
    return str(v);
  }
  function preview(kind, spec, meta) {
    injectCss(); meta = meta || {};
    var s = norm(kind, JSON.parse(JSON.stringify(spec || {}))), o = "";
    if (kind === "pptx") {
      var ft = function (i) { return '<div class="ft"><span>varios · ' + esc(meta.proyecto || "oficina de agentes") + " · borrador</span><span>" + (i + 1) + "</span></div>"; };
      var ul = function (l) { return l.length ? "<ul>" + l.map(function (p) { return "<li>" + esc(p) + "</li>"; }).join("") + "</ul>" : ""; };
      s.slides.forEach(function (x, i) {
        if (x.tipo === "portada") o += '<div class="ve-sl cov"><div class="in"><div class="ant">' + esc(x.antetitulo || meta.proyecto || "Varios") + '</div><div class="tt">' + esc(x.titulo || s.titulo) + '</div><div style="font-size:1.6cqw;color:#6A5A55;max-width:62%">' + esc(s.subtitulo) + '</div></div><div class="ve-mo"><i></i><i></i><i></i></div></div>';
        else if (x.tipo === "seccion") o += '<div class="ve-sl sec"><div class="in"><div class="ant">' + esc(x.antetitulo) + '</div><div class="tt">' + esc(x.titulo) + '</div></div><div class="ve-mo"><i></i><i></i><i></i></div></div>';
        else {
          var inner = '<div class="ant">' + esc(x.tipo === "cierre" ? (x.antetitulo || "Siguientes pasos") : x.antetitulo) + '</div><div class="tt">' + esc(x.titulo) + "</div>";
          if (x.tipo === "dos_columnas") inner += '<div class="ve-two"><div><b>' + esc(x.izquierda.titulo) + "</b>" + ul(x.izquierda.puntos) + "</div><div><b>" + esc(x.derecha.titulo) + "</b>" + ul(x.derecha.puntos) + "</div></div>";
          else if (x.tipo === "cifras" && x.cifras.length) inner += '<div class="ve-fig">' + x.cifras.map(function (c) { return "<div><b>" + esc(c.valor) + "</b><span>" + esc(c.etiqueta) + "</span></div>"; }).join("") + "</div>";
          else if (x.tipo === "tabla" && x.tabla.cabecera.length) inner += "<table><tr>" + x.tabla.cabecera.map(function (c) { return "<th>" + esc(c) + "</th>"; }).join("") + "</tr>" + x.tabla.filas.map(function (r) { return "<tr>" + x.tabla.cabecera.map(function (_, k) { return "<td>" + esc(r[k]) + "</td>"; }).join("") + "</tr>"; }).join("") + "</table>";
          else inner += ul(x.puntos);
          o += '<div class="ve-sl' + (x.tipo === "cierre" ? " cov" : "") + '" style="' + (x.tipo === "cierre" ? "" : "") + '"><div class="in"' + (x.tipo === "cierre" ? ' style="padding-top:5.5cqw"' : "") + ">" + inner + "</div>" + ft(i) + "</div>";
        }
      });
      return o;
    }
    if (kind === "docx") {
      o = '<div class="ve-doc"><div class="hd"><span><b style="color:#7A1F2E">varios</b></span><span>Borrador · ' + esc(meta.proyecto || s.titulo) + '</span></div><div class="ant" style="margin-top:0">' + esc(meta.proyecto || "Varios") + "</div><h1>" + esc(s.titulo) + "</h1>" + (s.subtitulo ? '<div class="sub">' + esc(s.subtitulo) + "</div>" : "");
      if (s.resumen) o += '<div class="ant">Resumen</div><p style="font-size:15.5px">' + esc(s.resumen) + "</p>";
      s.secciones.forEach(function (x, i) {
        o += '<div class="ant">' + ("0" + (i + 1)).slice(-2) + "</div><h2>" + esc(x.titulo) + "</h2>";
        x.bloques.forEach(function (b) {
          if (b.tipo === "lista") o += "<ul>" + b.items.map(function (it) { return "<li>" + esc(it).replace(/\*\*(.+?)\*\*/g, "<b>$1</b>") + "</li>"; }).join("") + "</ul>";
          else if (b.tipo === "tabla") o += "<table>" + (b.cabecera.length ? "<tr>" + b.cabecera.map(function (c) { return "<th>" + esc(c) + "</th>"; }).join("") + "</tr>" : "") + b.filas.map(function (r) { return "<tr>" + r.map(function (c) { return "<td>" + esc(c) + "</td>"; }).join("") + "</tr>"; }).join("") + "</table>";
          else if (b.tipo === "nota") o += '<div class="nt"><b>' + esc(b.titulo || "Nota") + "</b>" + esc(b.texto) + "</div>";
          else str(b.texto).split(/\n{2,}/).forEach(function (p) { if (p.trim()) o += "<p>" + esc(p.trim()).replace(/\*\*(.+?)\*\*/g, "<b>$1</b>") + "</p>"; });
        });
      });
      if (s.fuentes.length) o += "<h2>Fuentes</h2><ul>" + s.fuentes.map(function (f) { return "<li>" + esc(f) + "</li>"; }).join("") + "</ul>";
      return o + "</div>";
    }
    if (kind === "xlsx") {
      var id = "x" + Math.random().toString(36).slice(2, 7);
      o = '<div class="ve-xl" id="' + id + '"><div class="tabs" role="tablist">' + s.hojas.map(function (h, i) { return '<button type="button" role="tab" aria-selected="' + (i === 0) + '" data-h="' + i + '">' + esc(h.nombre) + "</button>"; }).join("") + "</div>";
      s.hojas.forEach(function (h, i) {
        var nums = h.columnas.map(function (c) { return c.tipo === "numero" || c.tipo === "euros"; });
        o += '<div class="grid" data-p="' + i + '"' + (i ? " hidden" : "") + ">" + (h.descripcion ? '<p style="margin:8px 10px;color:#6A5A55;font:italic 12.5px Arial">' + esc(h.descripcion) + "</p>" : "") + '<table><tr><th class="rn"></th>' + h.columnas.map(function (c) { return "<th>" + esc(c.nombre) + "</th>"; }).join("") + "</tr>";
        h.filas.forEach(function (r, ri) { o += '<tr><td class="rn">' + (ri + 5) + "</td>" + h.columnas.map(function (c, ci) { var cls = (c.tipo === "texto" || c.tipo === "fecha" ? "" : "n") + (c.entrada ? " in" : ""); return '<td class="' + cls + '">' + esc(fmtCell(r[ci], c.tipo)) + "</td>"; }).join("") + "</tr>"; });
        if (h.totales && h.filas.length && nums.some(Boolean)) o += '<tr class="tot"><td class="rn"></td>' + h.columnas.map(function (c, ci) { if (!nums[ci]) return "<td>" + (ci === 0 ? "Total" : "") + "</td>"; var sum = h.filas.reduce(function (m, r) { var n = toNum(r[ci]); return m + (n || 0); }, 0); return '<td class="n">' + esc(fmtCell(sum, c.tipo)) + "</td>"; }).join("") + "</tr>";
        o += "</table></div>";
      });
      if (s.notas.length) o += '<ul style="font-size:12.5px;color:var(--ink-muted)">' + s.notas.map(function (n) { return "<li>" + esc(n) + "</li>"; }).join("") + "</ul>";
      return o + "</div>";
    }
    if (kind === "proceso") return '<div class="ve-pr">' + procesoSvg(s, meta) + "</div>" + (s.notas.length ? '<ul style="font-size:12.5px;color:var(--ink-muted)">' + s.notas.map(function (n) { return "<li>" + esc(n) + "</li>"; }).join("") + "</ul>" : "");
    return "";
  }
  function bindPreview(root) {
    root.querySelectorAll(".ve-xl").forEach(function (x) {
      x.querySelectorAll("[data-h]").forEach(function (b) { b.onclick = function () { x.querySelectorAll("[data-h]").forEach(function (o) { o.setAttribute("aria-selected", o === b); }); x.querySelectorAll("[data-p]").forEach(function (p) { p.hidden = p.dataset.p !== b.dataset.h; }); }; });
    });
  }

  // ---------- Lectura de documentos subidos ----------
  function xmlText(xml, tag) { var re = new RegExp("<" + tag + "(?:\\s[^>]*)?>([\\s\\S]*?)</" + tag + ">", "g"), out = [], m; while ((m = re.exec(xml))) out.push(m[1]); return out; }
  function unxml(t) { return str(t).replace(/<[^>]+>/g, "").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"').replace(/&apos;/g, "'").replace(/&amp;/g, "&"); }
  async function extractText(file) {
    var name = file.name || "documento", ext = (name.split(".").pop() || "").toLowerCase();
    if (/^(txt|md|csv|tsv|json|html?|xml|yml|yaml|log)$/.test(ext) || /^text\//.test(file.type || "")) { var t = await file.text(); if (/^html?$/.test(ext)) t = unxml(t.replace(/<(script|style)[\s\S]*?<\/\1>/gi, "")); return { text: t, nota: "" }; }
    if (/^(docx|xlsx|pptx)$/.test(ext)) {
      var Z = await need("zip"), zip = await Z.loadAsync(await file.arrayBuffer()), out = [];
      if (ext === "docx") { var dx = await zip.file("word/document.xml").async("string"); xmlText(dx, "w:p").forEach(function (p) { var s = xmlText(p, "w:t").map(unxml).join(""); if (s.trim()) out.push(s); }); }
      if (ext === "pptx") { var sl = Object.keys(zip.files).filter(function (f) { return /^ppt\/slides\/slide\d+\.xml$/.test(f); }).sort(function (a, b) { return parseInt(a.match(/\d+/)[0]) - parseInt(b.match(/\d+/)[0]); }); for (var i = 0; i < sl.length; i++) { var sx = await zip.file(sl[i]).async("string"); out.push("— Diapositiva " + (i + 1) + " —"); xmlText(sx, "a:p").forEach(function (p) { var s = xmlText(p, "a:t").map(unxml).join(""); if (s.trim()) out.push(s); }); } }
      if (ext === "xlsx") {
        var ss = zip.file("xl/sharedStrings.xml") ? xmlText(await zip.file("xl/sharedStrings.xml").async("string"), "si").map(function (si) { return xmlText(si, "t").map(unxml).join(""); }) : [];
        var wbx = zip.file("xl/workbook.xml") ? await zip.file("xl/workbook.xml").async("string") : "", names = (wbx.match(/<sheet [^>]*name="[^"]*"/g) || []).map(function (m) { return unxml(m.match(/name="([^"]*)"/)[1]); });
        var sheets = Object.keys(zip.files).filter(function (f) { return /^xl\/worksheets\/sheet\d+\.xml$/.test(f); }).sort(function (a, b) { return parseInt(a.match(/\d+/)[0]) - parseInt(b.match(/\d+/)[0]); });
        for (var k = 0; k < sheets.length; k++) {
          var wx = await zip.file(sheets[k]).async("string"); out.push("— Hoja: " + (names[k] || k + 1) + " —");
          (wx.match(/<row[\s\S]*?<\/row>/g) || []).slice(0, 2000).forEach(function (r) {
            var cells = (r.match(/<c [^>]*?(?:\/>|>[\s\S]*?<\/c>)/g) || []).map(function (c) { var tt = (c.match(/ t="(\w+)"/) || [])[1], v = (c.match(/<v>([\s\S]*?)<\/v>/) || [])[1], is = xmlText(c, "t").map(unxml).join(""); return tt === "s" ? (ss[+v] || "") : tt === "inlineStr" ? is : unxml(v || ""); });
            if (cells.some(function (c) { return str(c).trim(); })) out.push(cells.join("\t"));
          });
        }
      }
      return { text: out.join("\n"), nota: "" };
    }
    if (ext === "pdf" || file.type === "application/pdf") {
      var pdfjs = await need("pdf"); pdfjs.GlobalWorkerOptions.workerSrc = "vendor/pdf.worker.min.js";
      var pdf = await pdfjs.getDocument({ data: new Uint8Array(await file.arrayBuffer()) }).promise, parts = [], N = Math.min(pdf.numPages, 80);
      for (var p = 1; p <= N; p++) { var pg = await pdf.getPage(p), tc = await pg.getTextContent(); parts.push(tc.items.map(function (it) { return it.str; }).join(" ").replace(/\s+/g, " ").trim()); }
      var txt = parts.filter(Boolean).join("\n\n");
      return { text: txt, nota: (pdf.numPages > N ? "Leídas " + N + " de " + pdf.numPages + " páginas. " : "") + (txt.length < 40 ? "Sin texto: parece escaneado (no hay OCR)." : "") };
    }
    if (/^(png|jpe?g|gif|webp)$/.test(ext)) return { text: "", nota: "Imagen: se guarda, pero no se extrae texto (no hay OCR)." };
    return { text: "", nota: "Formato no admitido para leer el texto." };
  }

  window.VE = { T: T, KINDS: KINDS, ACTOR: ACTOR, SCHEMA: SCHEMA, GUIA: GUIA, norm: norm, build: build, preview: preview, bindPreview: bindPreview, extractText: extractText, procesoSvg: procesoSvg, logoPng: logoPng, need: need, fileName: fileName, slug: slug };
})();
