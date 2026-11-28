// Varios · Oficina 3D
// Escena de office.js (Three.js r170) con datos reales, estados en HTML, paseos entre agentes,
// tarjeta de conversación y vista de zona.
import * as THREE from 'three';
import { buildOffice, lights, makeRenderer, camera, makeComposer, project, setSeated, standing, ZONES, FLOOR } from './office.js';

const MIN_DIST = 10, MAX_DIST = 120;
const SPEED = 3, ACC = 0.2, RISE = 0.4, TALK_SLOT = 1.2, MIN_TALK = 2.4, MAX_WALKS = 3, CELL = 0.5, FR = 16;
const LABEL = { work: 'Trabajando', wait: 'Espera tu OK', talk: 'Hablando', free: 'Libre' };

export function mount(host, bridge) {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  host.innerHTML = '<canvas class="o3-cv"></canvas><div class="o3-ovl" aria-label="Estados de los agentes"></div><div class="o3-tip" role="status"></div>';
  const canvas = host.querySelector('canvas'), ovl = host.querySelector('.o3-ovl'), tip = host.querySelector('.o3-tip');
  let W = Math.max(320, host.clientWidth), H = Math.max(240, host.clientHeight);
  let night = bridge.isDark();
  const renderer = makeRenderer(canvas, W, H, night);
  renderer.setPixelRatio(Math.min(2, window.devicePixelRatio || 1));
  renderer.setSize(W, H, false);

  let world = null, comp = null, gtao = null, cam = null, grid = null;
  const target = new THREE.Vector3(FLOOR.W / 2 - 0.2, 0, FLOOR.D / 2);
  let dist = 70;
  const marks = {}, pills = {};
  let states = {}, dirty = true, posDirty = true, focusDep = null, camAnim = null;
  const walks = [], walkers = {};
  let card = null, cardConv = null, deptCard = null, pops = {};

  // ---------- datos reales ----------
  const base = (s) => (s === 'talk' ? 'work' : s || 'free');
  function deptList() {
    const st = bridge.states();
    return bridge.departments().map((d) => ({
      key: d.id, name: d.n, color: d.c, at: ZONES[d.id] || [1, 1],
      agents: bridge.agents().filter((a) => a.dep === d.id).slice(0, 6).map((a) => ({ id: a.id, state: base(st[a.id]) })),
    }));
  }

  // ---------- escena ----------
  function build() {
    walks.length = 0; for (const k in walkers) delete walkers[k];
    const depts = deptList();
    states = {}; depts.forEach((d) => d.agents.forEach((a) => (states[a.id] = a.state)));
    world = buildOffice({ night, depts });
    lights(world.scene, renderer, night, depts);
    renderer.toneMappingExposure = night ? 1.0 : 0.94;
    renderer.setClearColor(night ? '#0B0B0F' : '#F5F5F3', 1);
    cam = camera(W, H, target, dist);
    comp = makeComposer(renderer, world.scene, cam, W, H, night, quality < 1); gtao = comp.gtao;
    if (quality >= 2) shadows2048();
    grid = makeGrid(world.scene);
    buildOverlay(depts);
    dirty = posDirty = true;
  }

  // ---------- capa HTML ----------
  function buildOverlay(depts) {
    ovl.innerHTML = ''; card = null; cardConv = null; deptCard = null; pops = {};
    for (const k in marks) delete marks[k];
    for (const k in pills) delete pills[k];
    depts.forEach((d) => {
      const p = document.createElement('button');
      p.type = 'button'; p.className = 'o3-pill'; p.dataset.dep = d.key;
      p.innerHTML = `<i style="background:${d.color}"></i><b>${esc(d.name)}</b><span class="n">${d.agents.length}</span><span class="w"></span><span class="o"></span>`;
      p.onclick = () => (focusDep === d.key ? unfocus() : focus(d.key));
      ovl.appendChild(p); pills[d.key] = p;
      d.agents.forEach((a) => {
        const m = document.createElement('button');
        m.type = 'button'; m.className = 'o3-mk'; m.dataset.ag = a.id;
        m.innerHTML = '<span class="b"><i></i><i></i><i></i></span>';
        m.onclick = (e) => { e.stopPropagation(); clickAgent(a.id); };
        m.onpointerenter = () => showTip(a.id, m); m.onpointerleave = hideTip;
        m.onfocus = () => showTip(a.id, m); m.onblur = hideTip;
        ovl.appendChild(m); marks[a.id] = m; paintMark(a.id);
      });
    });
    const cb = document.createElement('button');
    cb.type = 'button'; cb.className = 'o3-core'; cb.innerHTML = '<i></i>' + esc(bridge.brainLabel ? bridge.brainLabel() : 'Cerebro');
    cb.onclick = () => bridge.openBrain && bridge.openBrain(); ovl.appendChild(cb); pills.__core = cb;
    paintPills();
  }
  const walkOf = (id) => walks.find((w) => w.phase !== 'queue' && w.phase !== 'done' && (w.from === id || (w.to === id && w.phase === 'talk')));
  function shownState(id) {
    const w = walkOf(id);
    if (w && w.phase === 'talk') return 'talk';
    return states[id] || 'free';
  }
  function walkLabel(w, id) {
    const A = bridge.agent(w.from), B = bridge.agent(w.to);
    if (w.phase === 'queue') return `En cola para ir a ${bridge.deptName(B.dep)}`;
    if (w.phase === 'rise' || w.phase === 'go') return id === w.from ? `Va a ${bridge.deptName(B.dep)} · ${w.reason || 'mensaje'}` : `${A.n} viene a hablar`;
    if (w.phase === 'wait') return `Espera en el pasillo: ${B.n} está ocupado`;
    if (w.phase === 'back' || w.phase === 'sit') return 'Vuelve a su sitio con el resultado';
    return `Hablando con ${(id === w.from ? B : A).n}`;
  }
  function paintMark(id) {
    const m = marks[id]; if (!m) return; const s = shownState(id), a = bridge.agent(id), w = walkOf(id);
    m.classList.remove('s-work', 's-wait', 's-talk', 's-free'); m.classList.add('s-' + s);
    m.classList.toggle('walk', !!(w && w.from === id && w.phase !== 'talk'));
    m.setAttribute('aria-label', `${a ? a.n : id}: ${w ? walkLabel(w, id) : LABEL[s]}`);
  }
  function paintPills() {
    const filt = bridge.depFilter();
    for (const k in pills) {
      if (k === '__core') continue;
      const ids = Object.keys(states).filter((id) => world && world.desks[id] && world.desks[id].deptKey === k);
      const sts = ids.map(shownState);
      const w = sts.filter((s) => s === 'work' || s === 'talk').length, o = sts.filter((s) => s === 'wait').length;
      const p = pills[k];
      p.querySelector('.w').innerHTML = w ? `<i></i>${w}` : ''; p.querySelector('.o').innerHTML = o ? `<i></i>${o}` : '';
      p.classList.toggle('dim', !!filt && filt !== k); p.classList.toggle('sel', filt === k);
      p.setAttribute('aria-label', `${p.querySelector('b').textContent}: ${ids.length} agentes, ${w} en curso, ${o} esperan tu OK`);
    }
    for (const id in marks) { const d = world && world.desks[id]; marks[id].classList.toggle('dim', !!filt && d && d.deptKey !== filt && !walkOf(id)); }
  }
  function showTip(id, el) {
    const a = bridge.agent(id); if (!a) return;
    const w = walkOf(id) || walks.find((x) => x.phase === 'queue' && x.from === id);
    tip.innerHTML = `<b>${esc(a.n)}</b><span>${esc(bridge.deptName(a.dep))} · ${esc(w ? walkLabel(w, id) : LABEL[shownState(id)])}</span>`;
    const r = el.getBoundingClientRect(), h = host.getBoundingClientRect();
    tip.style.left = (r.left - h.left + r.width / 2) + 'px'; tip.style.top = (r.top - h.top - 30) + 'px'; tip.classList.add('on');
  }
  function hideTip() { tip.classList.remove('on'); }
  function clickAgent(id) {
    const w = walks.find((x) => x.phase !== 'done' && (x.from === id || x.to === id));
    if (w) openCard(w.conv); else bridge.openAgent(id);
  }

  // ---------- posiciones (project()) y textos que no tapan ----------
  function headOf(id) {
    const w = walks.find((x) => x.from === id && x.walker && x.walker.root.visible);
    if (w) { const p = w.walker.root.position; return new THREE.Vector3(p.x, 1.74 + p.y, p.z); }
    const d = world.desks[id]; if (!d || !d.anchor) return null;
    return d.anchor.clone().add(new THREE.Vector3(0, 0.17, 0));
  }
  const OFFS = (w) => { const L = []; for (const dy of [0, -12, 12, -24, 24, -38, 38, -54, 54, -72, 72]) for (const dx of [0, -0.55 * w, 0.55 * w, -w, w]) L.push([dx, dy]); return L.sort((a, b) => Math.hypot(a[0] * 0.6, a[1]) - Math.hypot(b[0] * 0.6, b[1])); };
  const hit = (a, b) => a[0] < b[2] && a[2] > b[0] && a[1] < b[3] && a[3] > b[1];
  function place() {
    if (!world) return;
    const boxes = [];
    for (const id in marks) {
      const m = marks[id], h = headOf(id);
      if (!h) { m.style.display = 'none'; continue; }
      const [x, y] = project(h, cam, W, H);
      m.style.display = ''; m.style.transform = `translate(${x}px,${y}px)`;
      const s = shownState(id);
      boxes.push(s === 'wait' || s === 'talk' ? [x - 20, y - 34, x + 20, y + 4] : [x - 12, y - 12, x + 12, y + 12]);
    }
    placeCard(); placeDept();
    if (card) boxes.push(rectOf(card)); if (deptCard) boxes.push(rectOf(deptCard));
    for (const id in pops) boxes.push(rectOf(pops[id]));
    // píldoras: posición ideal; si chocan con un agente u otra píldora, se apartan en vertical
    const want = [];
    for (const k in pills) {
      let v;
      if (k === '__core') v = new THREE.Vector3(14.6, 0.05, 12.1);
      else { const z = ZONES[k]; if (!z) continue; v = new THREE.Vector3(z[0] + 4, 2.1, z[1] - 0.2); }
      const [x, y] = project(v, cam, W, H);
      const el = pills[k];
      want.push({ el, x, y, w: el.offsetWidth || 120, h: el.offsetHeight || 26 });
    }
    want.sort((a, b) => a.y - b.y);
    for (const p of want) {
      let best = null;
      for (const [dx, dy] of OFFS(p.w)) {
        const r = [p.x + dx - p.w / 2 - 3, p.y + dy - p.h - 9, p.x + dx + p.w / 2 + 3, p.y + dy - 3]; // anclada abajo-centro (CSS translate)
        if (r[0] < 4 || r[2] > W - 4 || r[1] < 4) continue;
        if (!boxes.some((b) => hit(r, b))) { best = { dx, dy, r }; break; }
      }
      p.el.classList.toggle('crowd', !best);
      if (!best) best = { dx: 0, dy: 0, r: [p.x - p.w / 2, p.y - p.h - 6, p.x + p.w / 2, p.y - 6] };
      boxes.push(best.r);
      p.el.style.transform = `translate(${p.x + best.dx}px,${p.y + best.dy}px)`;
    }
  }
  function rectOf(el) { const r = el.getBoundingClientRect(), h = host.getBoundingClientRect(); return [r.left - h.left - 4, r.top - h.top - 4, r.right - h.left + 4, r.bottom - h.top + 4]; }

  // ---------- estados: solo lo que cambia ----------
  function sync() {
    if (!world) return;
    const st = bridge.states(); let changed = false;
    for (const id in states) {
      const s = base(st[id]);
      if (s !== states[id]) {
        const d = world.desks[id];
        const poseChange = (s === 'free') !== (states[id] === 'free');
        states[id] = s; d.state = s;
        if (poseChange) {
          const away = walks.some((w) => w.from === id && w.walker && w.walker.root.visible);
          setSeated(d, s); if (away && d.person) d.person.visible = false;
        } else if (d.screenMat) d.screenMat.emissiveIntensity = s === 'free' ? d.screenMat.emissiveIntensity : 0.9;
        changed = true;
      }
      paintMark(id);
    }
    paintPills(); refreshCard(); if (focusDep) paintDept();
    if (changed) dirty = true;
    posDirty = true; dirty = true;
  }

  // ---------- rejilla de 0,5 m con muebles bloqueados ----------
  function makeGrid(scene) {
    const nx = Math.ceil(FLOOR.W / CELL), nz = Math.ceil(FLOOR.D / CELL), b = new Uint8Array(nx * nz);
    const box = new THREE.Box3();
    scene.updateMatrixWorld(true);
    scene.traverse((o) => {
      if (!o.isMesh) return;
      for (let p = o; p; p = p.parent) if (p.userData && p.userData.agent) return; // las personas no bloquean
      box.setFromObject(o);
      if (box.max.y < 0.06 || box.min.y > 1.9) return; // suelo, alfombras, lámparas
      const sx = box.max.x - box.min.x, sz = box.max.z - box.min.z;
      if (sx > FLOOR.W * 0.8 || sz > FLOOR.D * 0.8) return; // suelo y paredes perimetrales
      const pad = 0.1;
      const i0 = Math.max(0, Math.floor((box.min.x - pad) / CELL)), i1 = Math.min(nx - 1, Math.floor((box.max.x + pad) / CELL));
      const j0 = Math.max(0, Math.floor((box.min.z - pad) / CELL)), j1 = Math.min(nz - 1, Math.floor((box.max.z + pad) / CELL));
      for (let i = i0; i <= i1; i++) for (let j = j0; j <= j1; j++) b[j * nx + i] = 1;
    });
    for (let i = 0; i < nx; i++) { b[i] = 1; b[(nz - 1) * nx + i] = 1; }
    for (let j = 0; j < nz; j++) { b[j * nx] = 1; b[j * nx + nx - 1] = 1; }
    return { nx, nz, b };
  }
  const cellOf = (x, z) => [Math.min(grid.nx - 1, Math.max(0, Math.floor(x / CELL))), Math.min(grid.nz - 1, Math.max(0, Math.floor(z / CELL)))];
  const isFree = (i, j) => i >= 0 && j >= 0 && i < grid.nx && j < grid.nz && !grid.b[j * grid.nx + i];
  const center = (i, j) => new THREE.Vector2((i + 0.5) * CELL, (j + 0.5) * CELL);
  function nearestFree(x, z) {
    const [i0, j0] = cellOf(x, z); if (isFree(i0, j0)) return [i0, j0];
    for (let r = 1; r < 10; r++) {
      let best = null, bd = 1e9;
      for (let i = i0 - r; i <= i0 + r; i++) for (let j = j0 - r; j <= j0 + r; j++) {
        if (Math.max(Math.abs(i - i0), Math.abs(j - j0)) !== r || !isFree(i, j)) continue;
        const c = center(i, j), d = (c.x - x) ** 2 + (c.y - z) ** 2; if (d < bd) { bd = d; best = [i, j]; }
      }
      if (best) return best;
    }
    return [i0, j0];
  }
  function astar(s, g) {
    const nx = grid.nx, key = (i, j) => j * nx + i;
    const open = [[0, s[0], s[1]]], gs = new Map([[key(s[0], s[1]), 0]]), from = new Map(), closed = new Set();
    const h = (i, j) => { const dx = Math.abs(i - g[0]), dz = Math.abs(j - g[1]); return Math.max(dx, dz) + 0.414 * Math.min(dx, dz); };
    let n = 0;
    while (open.length && n++ < 30000) {
      let bi = 0; for (let k = 1; k < open.length; k++) if (open[k][0] < open[bi][0]) bi = k;
      const [, i, j] = open[bi]; open[bi] = open[open.length - 1]; open.pop();
      const kk = key(i, j); if (closed.has(kk)) continue; closed.add(kk);
      if (i === g[0] && j === g[1]) { const out = [[i, j]]; let c = kk; while (from.has(c)) { c = from.get(c); out.push([c % nx, Math.floor(c / nx)]); } return out.reverse(); }
      for (const [di, dj] of [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]) {
        const a = i + di, b = j + dj;
        if (!isFree(a, b) || (di && dj && (!isFree(i + di, j) || !isFree(i, j + dj)))) continue;
        const ng = gs.get(kk) + (di && dj ? 1.414 : 1), nk = key(a, b);
        if (ng < (gs.has(nk) ? gs.get(nk) : 1e9)) { gs.set(nk, ng); from.set(nk, kk); open.push([ng + h(a, b), a, b]); }
      }
    }
    return null;
  }
  function sight(a, b) {
    const n = Math.ceil(a.distanceTo(b) / 0.1);
    for (let k = 1; k < n; k++) { const t = k / n; for (const o of [-0.18, 0.18]) { const dx = b.x - a.x, dz = b.y - a.y, L = Math.hypot(dx, dz) || 1; const [i, j] = cellOf(a.x + dx * t - (dz / L) * o, a.y + dz * t + (dx / L) * o); if (!isFree(i, j)) return false; } }
    return true;
  }
  function smooth(pts) {
    if (pts.length < 3) return pts;
    const out = [pts[0]]; let i = 0;
    while (i < pts.length - 1) { let j = pts.length - 1; while (j > i + 1 && !sight(pts[i], pts[j])) j--; out.push(pts[j]); i = j; }
    return out;
  }
  function route(a, b) {
    const s = nearestFree(a.x, a.y), g = nearestFree(b.x, b.y), cells = astar(s, g);
    if (!cells) return null;
    const pts = smooth(cells.map((c) => center(c[0], c[1])));
    pts[0] = a.clone(); pts.push(b.clone());
    return pts;
  }
  // de pie junto a la mesa del receptor, mirándolo
  function spotsFor(id) {
    const d = world.desks[id], sx = d.seat.x, sz = d.seat.z;
    return [new THREE.Vector2(sx - 0.95, sz - 0.1), new THREE.Vector2(sx + 0.95, sz - 0.1), new THREE.Vector2(sx, sz - 1.05)];
  }
  const aisle = (id) => { const d = world.desks[id]; return new THREE.Vector2(d.seat.x, d.seat.z - 0.85); };

  // ---------- personas que caminan: fotogramas prefabricados con standing() ----------
  function walkerFor(id) {
    if (walkers[id]) return walkers[id];
    const d = world.desks[id], root = new THREE.Group(); root.visible = false; world.scene.add(root);
    const mk = (carry) => { const L = []; for (let i = 0; i < FR; i++) { const g = standing(0, 0, d.dept, 0, Math.sin((2 * Math.PI * i) / FR), root, carry, id).group; g.visible = false; g.traverse((o) => { if (o.isMesh) o.castShadow = true; }); L.push(g); } return L; };
    const w = { root, frames: [mk(false), mk(true)], still: [standing(0, 0, d.dept, 0, 0, root, false, id).group, standing(0, 0, d.dept, 0, 0, root, true, id).group], cur: null };
    w.still.forEach((g) => { g.visible = false; g.traverse((o) => { if (o.isMesh) o.castShadow = true; }); });
    walkers[id] = w; return w;
  }
  function showFrame(wk, carry, i) {
    const f = i == null ? wk.still[carry ? 1 : 0] : wk.frames[carry ? 1 : 0][((i % FR) + FR) % FR];
    if (wk.cur !== f) { if (wk.cur) wk.cur.visible = false; f.visible = true; wk.cur = f; }
  }

  // ---------- paseos ----------
  const active = () => walks.filter((w) => w.phase !== 'queue' && w.phase !== 'done');
  function message(m) {
    // m: { conv, from, to, reason }
    if (!world || !world.desks[m.from] || !world.desks[m.to] || m.from === m.to) return false;
    if (walks.some((w) => w.conv === m.conv)) return true;
    const w = { conv: m.conv, from: m.from, to: m.to, reason: m.reason || '', phase: 'queue', t: 0, ended: false, carry: false, s: 0, v: 0, cyc: 0, born: performance.now() };
    walks.push(w); pump(); paintAll(); return true;
  }
  function end(conv) { const w = walks.find((x) => x.conv === conv); if (w) w.ended = true; dirty = true; }
  function pump() {
    for (const q of walks) {
      if (q.phase !== 'queue') continue;
      if (active().length >= MAX_WALKS) break;
      if (active().some((w) => w.from === q.from || w.to === q.from)) continue; // ya está fuera o recibiendo
      start(q);
    }
  }
  function start(w) {
    const d = world.desks[w.from];
    const from = aisle(w.from);
    const cands = spotsFor(w.to).map((p) => ({ p, r: route(from, p) })).filter((x) => x.r);
    if (!cands.length) { w.phase = 'done'; return; }
    cands.sort((a, b) => plen(a.r) - plen(b.r));
    w.walker = walkerFor(w.from);
    const seat = new THREE.Vector2(d.seat.x, d.seat.z);
    w.path = [seat].concat(cands[0].r); w.goal = cands[0].p; w.len = plen(w.path); w.s = 0; w.v = 0; w.t = 0; w.cyc = 0;
    const r = w.walker.root; r.position.set(seat.x, 0, seat.y); r.rotation.y = Math.PI; r.visible = true;
    if (d.person) d.person.visible = false; // no puede estar en dos sitios
    if (reduced) {
      // fundido en origen y aparición en destino, con la ruta punteada 1 s
      showFrame(w.walker, false, null); r.position.set(w.goal.x, 0, w.goal.y); r.rotation.y = face(w.goal, w.to);
      flashPath(w.path); w.phase = 'talk'; w.talkAt = Date.now();
    } else { showFrame(w.walker, false, null); w.phase = 'rise'; }
    bridge.onWalk && bridge.onWalk(w.conv, 'start');
  }
  let pathLine = null;
  function flashPath(path) {
    if (pathLine) { world.scene.remove(pathLine); pathLine.geometry.dispose(); }
    const g = new THREE.BufferGeometry().setFromPoints(path.map((p) => new THREE.Vector3(p.x, 0.03, p.y)));
    pathLine = new THREE.Line(g, new THREE.LineDashedMaterial({ color: '#4646F0', dashSize: 0.25, gapSize: 0.18 })); pathLine.computeLineDistances();
    world.scene.add(pathLine); const pl = pathLine;
    setTimeout(() => { if (pathLine === pl) { world.scene.remove(pl); pl.geometry.dispose(); pathLine = null; dirty = true; } }, 1000);
  }
  const plen = (p) => { let s = 0; for (let i = 1; i < p.length; i++) s += p[i].distanceTo(p[i - 1]); return s; };
  const face = (p, id) => { const d = world.desks[id]; return Math.atan2(d.seat.x - p.x, d.seat.z - p.y); };
  function at(path, s) {
    let acc = 0;
    for (let i = 1; i < path.length; i++) {
      const L = path[i].distanceTo(path[i - 1]);
      if (acc + L >= s && L > 0) { const t = (s - acc) / L; return { p: path[i - 1].clone().lerp(path[i], t), dir: Math.atan2(path[i].x - path[i - 1].x, path[i].y - path[i - 1].y) }; }
      acc += L;
    }
    const n = path.length - 1; return { p: path[n].clone(), dir: Math.atan2(path[n].x - path[n - 1].x, path[n].y - path[n - 1].y) };
  }
  function turn(r, dir, dt) { let d = dir - r.rotation.y; d = Math.atan2(Math.sin(d), Math.cos(d)); r.rotation.y += d * Math.min(1, dt * 14); }
  const ACCEL = SPEED / ACC;
  function receiverBusy(w) { return walks.some((o) => o !== w && o.to === w.to && (o.phase === 'talk')); }
  function step(w, dt) {
    const r = w.walker.root;
    w.t += dt;
    if (w.phase === 'rise') { if (w.t >= RISE) { w.phase = 'go'; w.t = 0; paintAll(); } return; }
    if (w.phase === 'go' || w.phase === 'back') {
      // cruce: si otro camina a menos de 1 m, el que vuelve cede el paso
      const other = walks.find((o) => o !== w && (o.phase === 'go' || o.phase === 'back') && o.walker && o.walker.root.position.distanceTo(r.position) < 1.0);
      const yieldNow = other && ((w.phase === 'back' && other.phase === 'go') || (w.phase === other.phase && w.born > other.born));
      const rem = w.len - w.s;
      // receptor ocupado: parar en el pasillo a 1 m
      if (w.phase === 'go' && rem < 1.0 + 0.05 && receiverBusy(w)) { w.phase = 'wait'; w.v = 0; w.t = 0; showFrame(w.walker, false, null); r.position.y = 0; paintAll(); return; }
      const vmax = Math.min(SPEED, Math.sqrt(Math.max(0, 2 * ACCEL * rem)));
      w.v = yieldNow ? Math.max(0, w.v - ACCEL * dt) : Math.min(vmax, w.v + ACCEL * dt);
      w.s = Math.min(w.len, w.s + w.v * dt);
      const q = at(w.path, w.s); r.position.x = q.p.x; r.position.z = q.p.y; if (w.v > 0.05) turn(r, q.dir, dt);
      w.cyc += dt * 2 * (w.v / SPEED); // 2 pasos por segundo a velocidad de crucero
      if (w.v > 0.05) showFrame(w.walker, w.carry, Math.floor(w.cyc * FR / 2) % FR); else showFrame(w.walker, w.carry, null);
      r.position.y = 0.03 * Math.abs(Math.sin(Math.PI * w.cyc)) * Math.min(1, w.v / SPEED);
      if (w.s >= w.len - 1e-3) {
        r.position.y = 0;
        if (w.phase === 'go') { w.phase = 'talk'; w.t = 0; w.slot = -1; w.talkAt = Date.now(); showFrame(w.walker, false, null); paintAll(); }
        else { w.phase = 'sit'; w.t = 0; }
      }
      return;
    }
    if (w.phase === 'wait') { if (!receiverBusy(w)) { w.phase = 'go'; w.t = 0; paintAll(); } return; }
    if (w.phase === 'talk') {
      turn(r, face(w.goal, w.to), dt);
      const slot = Math.floor(w.t / TALK_SLOT) % 2;
      if (slot !== w.slot) { w.slot = slot; speak(w); }
      if ((w.ended && w.t >= MIN_TALK) || w.t > 120) {
        clearSpeak(w); w.carry = true;
        if (reduced) { w.phase = 'sit'; w.t = 0; return; }
        w.path = w.path.slice().reverse(); w.len = plen(w.path); w.s = 0; w.v = 0; w.cyc = 0; w.phase = 'back'; w.t = 0;
        paintAll();
      }
      return;
    }
    if (w.phase === 'sit') {
      if (w.t < (reduced ? 0 : 0.4)) return;
      const d = world.desks[w.from];
      if (d.person) d.person.visible = true;
      r.visible = false; if (w.walker.cur) { w.walker.cur.visible = false; w.walker.cur = null; }
      w.phase = 'done'; bridge.onWalk && bridge.onWalk(w.conv, 'end'); paintAll();
    }
  }
  function speak(w) { const a = marks[w.from], b = marks[w.to]; if (a) a.classList.toggle('quiet', w.slot === 1); if (b) b.classList.toggle('quiet', w.slot === 0); }
  function clearSpeak(w) { const a = marks[w.from], b = marks[w.to]; if (a) a.classList.remove('quiet'); if (b) b.classList.remove('quiet'); }
  function paintAll() { for (const id in marks) paintMark(id); paintPills(); refreshCard(); if (focusDep) paintDept(); posDirty = dirty = true; }
  function tickWalks(dt) {
    if (!walks.length) return false;
    for (const w of walks.slice()) if (w.phase !== 'queue' && w.phase !== 'done') step(w, dt);
    let gone = false;
    for (let i = walks.length - 1; i >= 0; i--) if (walks[i].phase === 'done') { walks.splice(i, 1); gone = true; }
    if (gone) { pump(); paintAll(); }
    return true;
  }

  // ---------- tarjeta de conversación ----------
  function openCard(conv) {
    if (!bridge.conversation || !bridge.conversation(conv)) return;
    closeCard(); cardConv = conv;
    card = document.createElement('div'); card.className = 'o3-card'; card.setAttribute('role', 'dialog');
    card.addEventListener('pointerdown', (e) => e.stopPropagation());
    ovl.appendChild(card); refreshCard(); posDirty = dirty = true;
  }
  function closeCard() { if (card) card.remove(); card = null; cardConv = null; posDirty = dirty = true; }
  let cardN = -1;
  function refreshCard() {
    if (!card) return;
    const c = bridge.conversation(cardConv); if (!c) { closeCard(); return; }
    const A = bridge.agent(c.from), B = bridge.agent(c.to), w = walks.find((x) => x.conv === cardConv);
    const live = w && w.phase === 'talk', secs = live ? Math.max(0, Math.round((Date.now() - w.talkAt) / 1000)) : 0;
    const status = live ? `<span class="lv"><i></i>Hablando · ${Math.floor(secs / 60)}:${String(secs % 60).padStart(2, '0')}</span>` : w ? `<span class="lv g">${esc(walkLabel(w, c.from))}</span>` : `<span class="lv g">${c.open ? 'En curso' : 'Terminada'}</span>`;
    const head = card.querySelector('.h .lv');
    if (head && cardN === c.lines.length) { head.outerHTML = status; return; } // solo el reloj
    cardN = c.lines.length;
    card.setAttribute('aria-label', `Conversación entre ${A.n} y ${B.n}`);
    card.innerHTML = `<div class="h"><span class="t"><b>${esc(bridge.deptName(A.dep))} → ${esc(bridge.deptName(B.dep))}</b><small>${esc(A.n)} y ${esc(B.n)}${c.reason ? ' · ' + esc(clip(c.reason, 60)) : ''}</small>${status}</span><button type="button" class="x" aria-label="Cerrar">×</button></div>`
      + `<div class="ls">${c.lines.length ? c.lines.map((l) => { const P = bridge.agent(l.from) || A; return `<div class="ln${l.from === c.to ? ' r' : ''}"><span class="av" style="background:${bridge.deptColor(P.dep)}">${esc(ini(P.n))}</span><div><small>${esc(P.n)}</small><p>${esc(clip(l.text, 360))}</p></div></div>`; }).join('') : '<p class="emp">Empezando…</p>'}</div>`
      + `<div class="f"><span>${c.sim ? 'Simulación: no se guarda' : 'Se guarda en el historial y cada noche en GitHub'}</span>${c.task ? '<button type="button" class="vc">Ver el encargo →</button>' : ''}</div>`;
    card.querySelector('.x').onclick = closeCard;
    const vc = card.querySelector('.vc'); if (vc) vc.onclick = () => bridge.openTask(c.task);
    const ls = card.querySelector('.ls'); ls.scrollTop = ls.scrollHeight;
    posDirty = dirty = true;
  }
  function placeCard() {
    if (!card) return;
    const c = bridge.conversation(cardConv); if (!c) return;
    const a = headOf(c.to), b = headOf(c.from);
    const pa = a ? project(a, cam, W, H) : [W / 2, H / 2], pb = b ? project(b, cam, W, H) : pa;
    const mx = (pa[0] + pb[0]) / 2, my = Math.min(pa[1], pb[1]);
    const cw = card.offsetWidth || 340, ch = card.offsetHeight || 220;
    let x = mx - cw / 2, y = my - ch - 46;
    if (y < 10) y = Math.max(pa[1], pb[1]) + 30;
    x = Math.max(10, Math.min(W - cw - 10, x)); y = Math.max(10, Math.min(H - ch - 10, y));
    card.style.transform = `translate(${x}px,${y}px)`;
  }

  // ---------- vista de zona ----------
  function focus(k) {
    const z = ZONES[k]; if (!z) return;
    focusDep = k; bridge.setDepFilter && bridge.setDepFilter(k);
    animateCam(new THREE.Vector3(z[0] + 4, 0, z[1] + 3.2), 24);
    if (!deptCard) { deptCard = document.createElement('div'); deptCard.className = 'o3-dcard'; deptCard.addEventListener('pointerdown', (e) => e.stopPropagation()); ovl.appendChild(deptCard); }
    paintDept(); paintPills();
  }
  function unfocus() {
    focusDep = null; bridge.setDepFilter && bridge.setDepFilter(null);
    if (deptCard) { deptCard.remove(); deptCard = null; }
    for (const k in pops) pops[k].remove(); pops = {};
    fit(true); paintPills();
  }
  function paintDept() {
    if (!deptCard || !focusDep) return;
    const d = bridge.departments().find((x) => x.id === focusDep), ags = bridge.agents().filter((a) => a.dep === focusDep);
    const c = { work: 0, wait: 0, talk: 0, free: 0 }; ags.forEach((a) => c[shownState(a.id)]++);
    deptCard.innerHTML = `<div class="h"><i style="background:${d.c}"></i><b>${esc(d.n)}</b><button type="button" class="x" aria-label="Volver a la vista general">×</button></div><small>${ags.length} agentes · ${c.work + c.talk} en curso · ${c.wait} te esperan</small>`
      + ags.map((a) => { const s = shownState(a.id); return `<button type="button" class="r" data-ag="${a.id}"><span>${esc(a.n)}</span><em class="st s-${s}"><i></i>${LABEL[s]}</em></button>`; }).join('');
    deptCard.querySelector('.x').onclick = unfocus;
    deptCard.querySelectorAll('[data-ag]').forEach((b) => (b.onclick = () => bridge.openAgent(b.dataset.ag)));
    // tarjetas junto a los agentes con tarea
    const want = {};
    ags.forEach((a) => { const s = shownState(a.id); if (s !== 'free') { const t = bridge.currentTask(a.id); if (t) want[a.id] = t; } });
    for (const id in pops) if (!want[id]) { pops[id].remove(); delete pops[id]; }
    for (const id in want) {
      const t = want[id], s = shownState(id), A = bridge.agent(id);
      let p = pops[id]; if (!p) { p = document.createElement('div'); p.className = 'o3-pop'; p.addEventListener('pointerdown', (e) => e.stopPropagation()); ovl.appendChild(p); pops[id] = p; }
      p.innerHTML = `<div class="h"><b>${esc(A.n)}</b><em class="st s-${s}"><i></i>${LABEL[s]}</em></div><p>${esc(clip(t.title, 90))}</p>`
        + (s === 'wait'
          ? `<small>${t.status === 'preg' ? 'Tiene una pregunta para ti.' : 'Necesita tu aprobación antes de seguir.'}</small><div class="a">${t.status === 'aprob' ? '<button type="button" class="ok">Dar el OK</button>' : ''}<button type="button" class="vd">${t.status === 'preg' ? 'Responder' : 'Ver detalle'}</button></div>`
          : `<div class="pb"><i style="width:${Math.round((t.step / t.of) * 100)}%"></i></div><small>Paso ${t.step} de ${t.of} · ${esc(t.label)}</small>`);
      const ok = p.querySelector('.ok'); if (ok) ok.onclick = () => bridge.approve(t.id);
      const vd = p.querySelector('.vd'); if (vd) vd.onclick = () => bridge.openTask(t.id);
    }
    posDirty = dirty = true;
  }
  function placeDept() {
    if (!focusDep) return;
    const taken = [];
    if (deptCard) taken.push(rectOf(deptCard));
    if (card) taken.push(rectOf(card));
    const heads = Object.keys(marks).map((id) => { const h = headOf(id); if (!h) return null; const [x, y] = project(h, cam, W, H); return [x - 22, y - 36, x + 22, y + 14]; }).filter(Boolean);
    const ids = Object.keys(pops).map((id) => ({ id, h: headOf(id) })).filter((o) => o.h).map((o) => ({ ...o, p: project(o.h, cam, W, H) })).sort((a, b) => a.p[1] - b.p[1]);
    for (const o of ids) {
      const el = pops[o.id], w = el.offsetWidth || 230, hh = el.offsetHeight || 90, [x, y] = o.p;
      let best = null;
      for (const [ox, oy] of [[26, -hh / 2], [-w - 26, -hh / 2], [26, -hh - 20], [-w - 26, -hh - 20], [26, 20], [-w - 26, 20], [-w / 2, -hh - 44], [-w / 2, 30]]) {
        let px = x + ox, py = y + oy;
        px = Math.max(8, Math.min(W - w - 8, px)); py = Math.max(8, Math.min(H - hh - 8, py));
        const r = [px, py, px + w, py + hh];
        if (!taken.some((t) => hit(r, t)) && !heads.some((t) => hit(r, t))) { best = r; break; }
        if (!best && !taken.some((t) => hit(r, t))) best = r;
      }
      if (!best) best = [Math.max(8, x + 26), y, x + 26 + w, y + hh];
      taken.push(best); el.style.transform = `translate(${best[0]}px,${best[1]}px)`;
    }
  }
  function animateCam(t2, d2) { camAnim = { t0: performance.now(), from: target.clone(), d0: dist, to: t2, d1: d2, dur: reduced ? 1 : 650 }; dirty = true; }

  // ---------- cámara: rueda, arrastrar, sin rotar ----------
  const ray = new THREE.Raycaster(), ground = new THREE.Plane(new THREE.Vector3(0, 1, 0), 0), ndc = new THREE.Vector2();
  function groundAt(px, py) { ndc.set((px / W) * 2 - 1, -(py / H) * 2 + 1); ray.setFromCamera(ndc, cam); const out = new THREE.Vector3(); return ray.ray.intersectPlane(ground, out) ? out : null; }
  function setCam() {
    target.x = Math.min(FLOOR.W + 4, Math.max(-4, target.x)); target.z = Math.min(FLOOR.D + 4, Math.max(-4, target.z));
    dist = Math.min(MAX_DIST, Math.max(MIN_DIST, dist));
    const dir = new THREE.Vector3(1, 1.05, 1).normalize();
    cam.position.copy(target).addScaledVector(dir, dist); cam.lookAt(target); cam.updateMatrixWorld();
    dirty = posDirty = true;
  }
  function zoomBy(f, px, py) { camAnim = null; const before = px != null ? groundAt(px, py) : null; dist *= f; setCam(); if (before) { const after = groundAt(px, py); if (after) { target.add(before.sub(after)); setCam(); } } }
  function fit(anim) {
    const corners = [[0, 0], [FLOOR.W, 0], [0, FLOOR.D], [FLOOR.W, FLOOR.D]].map(([x, z]) => new THREE.Vector3(x, 0, z)).concat([new THREE.Vector3(1, 3, 1)]);
    const t0 = target.clone(), d0 = dist;
    target.set(FLOOR.W / 2 - 0.2, 0, FLOOR.D / 2 + 0.6);
    let lo = MIN_DIST, hi = MAX_DIST;
    for (let i = 0; i < 24; i++) { dist = (lo + hi) / 2; setCam(); const ok = corners.every((v) => { const [x, y] = project(v, cam, W, H); return x > 8 && x < W - 8 && y > 30 && y < H - 50; }); if (ok) hi = dist; else lo = dist; }
    if (anim) { const t1 = target.clone(); target.copy(t0); dist = d0; setCam(); animateCam(t1, hi); } else { dist = hi; setCam(); }
  }
  let drag = null, moved = false;
  canvas.addEventListener('pointerdown', (e) => { camAnim = null; drag = { x: e.offsetX, y: e.offsetY, g: groundAt(e.offsetX, e.offsetY) }; moved = false; canvas.setPointerCapture(e.pointerId); canvas.classList.add('grab'); });
  canvas.addEventListener('pointermove', (e) => { if (!drag) return; if (Math.abs(e.offsetX - drag.x) + Math.abs(e.offsetY - drag.y) > 3) moved = true; const g = groundAt(e.offsetX, e.offsetY); if (g && drag.g) { target.add(drag.g.clone().sub(g)); setCam(); } });
  const endDrag = (e) => { if (drag && !moved) pick(e.offsetX, e.offsetY); drag = null; canvas.classList.remove('grab'); };
  canvas.addEventListener('pointerup', endDrag); canvas.addEventListener('pointercancel', () => { drag = null; canvas.classList.remove('grab'); });
  canvas.addEventListener('wheel', (e) => { e.preventDefault(); zoomBy(Math.exp(e.deltaY * 0.0012), e.offsetX, e.offsetY); }, { passive: false });
  function pick(px, py) {
    ndc.set((px / W) * 2 - 1, -(py / H) * 2 + 1); ray.setFromCamera(ndc, cam);
    const hits = ray.intersectObjects(world.scene.children, true);
    for (const h of hits) {
      let o = h.object, vis = true;
      for (let p = o; p; p = p.parent) if (p.visible === false) vis = false;
      if (!vis) continue;
      while (o && !(o.userData && o.userData.agent)) o = o.parent;
      if (o && bridge.agent(o.userData.agent)) { clickAgent(o.userData.agent); return; }
    }
    if (card) closeCard();
  }

  // ---------- calidad adaptativa ----------
  let quality = 0, lowSince = 0, frames = [], lastT = 0;
  function shadows2048() { const sun = world.scene.userData.sun; if (sun && sun.shadow.mapSize.x !== 2048) { sun.shadow.mapSize.set(2048, 2048); if (sun.shadow.map) { sun.shadow.map.dispose(); sun.shadow.map = null; } } }
  function adapt(t) {
    if (lastT && t - lastT < 250) { frames.push(t - lastT); if (frames.length > 30) frames.shift(); } else frames = [];
    lastT = t;
    if (frames.length < 15 || quality >= 2) return;
    const fps = 1000 / (frames.reduce((a, b) => a + b, 0) / frames.length);
    if (fps < 45) { if (!lowSince) lowSince = t; if (t - lowSince > 2000) { quality++; lowSince = 0; frames = []; if (quality === 1 && gtao) gtao.enabled = false; if (quality === 2) shadows2048(); bridge.onQuality && bridge.onQuality(quality); dirty = true; } }
    else lowSince = 0;
  }

  // ---------- bucle ----------
  let raf = 0, alive = true, prev = 0, cardTick = 0;
  function loop(t) {
    if (!alive) return; raf = requestAnimationFrame(loop);
    const dt = prev ? Math.min(0.2, (t - prev) / 1000) : 0.016; prev = t;
    if (camAnim) {
      const k = Math.min(1, (t - camAnim.t0) / camAnim.dur), e = k < 0.5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2;
      target.lerpVectors(camAnim.from, camAnim.to, e); dist = camAnim.d0 + (camAnim.d1 - camAnim.d0) * e; setCam();
      if (k >= 1) camAnim = null;
    }
    if (tickWalks(dt)) { dirty = posDirty = true; }
    if (card && t - cardTick > 1000) { cardTick = t; refreshCard(); }
    if (!dirty) { lastT = 0; return; }
    dirty = false;
    if (posDirty) { place(); posDirty = false; }
    comp.comp.render();
    adapt(t);
  }
  function resize() {
    const w = Math.max(320, host.clientWidth), h = Math.max(240, host.clientHeight);
    if (w === W && h === H) return; W = w; H = h;
    renderer.setSize(W, H, false); comp.comp.setSize(W, H); if (gtao) gtao.setSize(W, H);
    cam.aspect = W / H; cam.updateProjectionMatrix(); setCam();
  }
  const ro = new ResizeObserver(resize); ro.observe(host);
  const onKey = (e) => { if (e.key !== 'Escape') return; if (card) { closeCard(); e.stopPropagation(); } else if (focusDep) { unfocus(); e.stopPropagation(); } };
  window.addEventListener('keydown', onKey, true);

  build(); fit(); raf = requestAnimationFrame(loop);

  return {
    sync, message, end,
    openConversation: openCard, refreshConversation: () => { cardN = -1; refreshCard(); },
    zoomIn: () => zoomBy(1 / 1.25, W / 2, H / 2), zoomOut: () => zoomBy(1.25, W / 2, H / 2),
    home: () => { if (focusDep) unfocus(); else fit(true); },
    focus, unfocus, focused: () => focusDep,
    setNight(n) { if (n === night) return; night = n; build(); setCam(); },
    quality: () => quality,
    project: (id) => { const h = headOf(id); return h ? project(h, cam, W, H) : null; },
    debug: () => ({ quality, dist, target: target.toArray(), calls: renderer.info.render.calls, geos: renderer.info.memory.geometries, walks: walks.map((w) => [w.from, w.to, w.phase, Math.round(w.s * 10) / 10, Math.round((w.len || 0) * 10) / 10]), states: { ...states }, blocked: grid ? grid.b.reduce((a, b) => a + b, 0) : 0 }),
    destroy() { alive = false; cancelAnimationFrame(raf); ro.disconnect(); window.removeEventListener('keydown', onKey, true); renderer.dispose(); host.innerHTML = ''; },
  };
}
function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c])); }
function clip(t, n) { t = String(t || '').replace(/\s+/g, ' ').trim(); return t.length > n ? t.slice(0, n - 1) + '…' : t; }
function ini(n) { return String(n).split(/\s+/).filter((w) => w.length > 2).slice(0, 2).map((w) => w[0]).join('').toUpperCase() || String(n).slice(0, 2).toUpperCase(); }
