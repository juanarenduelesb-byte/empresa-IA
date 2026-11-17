// Oficina de agentes — escena 3D (Three.js r170)
// Plano: (px, py) del plano 2D  ->  three.js (x = px, z = py), y = altura en metros.
// Base: office.js de referencia. Cambios para Varios (marcados con «Varios:»):
//  - departamentos y agentes reales (parámetro depts) y una séptima zona (Sectores) donde estaba la zona de descanso;
//  - geometrías y materiales compartidos entre personas;
//  - cambio de estado de un puesto sin reconstruir la escena (setSeated) y compositor persistente (makeComposer).
import * as THREE from 'three';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { GTAOPass } from 'three/addons/postprocessing/GTAOPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';

export const DEPTS = [
  { key: 'dir', name: 'Dirección', color: '#8E2F3C', at: [1, 1], states: ['work', 'free', 'free', 'free'] },
  { key: 'com', name: 'Comercial y clientes', color: '#2F7F7A', at: [11, 1], states: ['work', 'wait', 'work', 'free', 'free'] },
  { key: 'pro', name: 'Procesos', color: '#A8761F', at: [21, 1], states: ['work', 'free', 'free', 'free'] },
  { key: 'adm', name: 'Administración', color: '#6B625A', at: [1, 15], states: ['free', 'free', 'free'] },
  { key: 'cal', name: 'Calidad, seguridad y legal', color: '#B83F52', at: [11, 15], states: ['wait', 'free', 'free'] },
  { key: 'ing', name: 'Ingeniería', color: '#3F4F9A', at: [21, 15], states: ['work', 'work', 'free', 'free'] },
];
// Varios: el fondo crece 1,4 m para dejar pasillo alrededor de la séptima zona.
const W = 30, D = 24.4, WALL_H = 3.0;
// Varios: puesto de cada zona en el plano (x, z de la esquina).
export const ZONES = { dir: [1, 1], com: [11, 1], pro: [21, 1], sect: [1, 8.8], adm: [1, 16.2], cal: [11, 16.2], ing: [21, 16.2] };
export const FLOOR = { W, D };

// ---------- deterministic random ----------
let seed = 7;
const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);
const pick = (a) => a[Math.floor(rnd() * a.length)];

// ---------- canvas textures ----------
function canvasTex(w, h, draw, repeat) {
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  draw(c.getContext('2d'), w, h);
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
  if (repeat) { t.wrapS = t.wrapT = THREE.RepeatWrapping; t.repeat.set(...repeat); }
  return t;
}
function woodTex(night) {
  return canvasTex(2048, 2048, (g, w, h) => {
    const planks = 16, pw = w / planks;
    for (let i = 0; i < planks; i++) {
      let y = -rnd() * 600;
      while (y < h) {
        const len = 500 + rnd() * 700;
        const l = night ? 34 + rnd() * 8 : 76 + rnd() * 7;
        g.fillStyle = `hsl(${30 + rnd() * 6}, ${night ? 16 : 20 + rnd() * 7}%, ${l}%)`;
        g.fillRect(i * pw, y, pw, len);
        g.globalAlpha = 0.07;
        for (let k = 0; k < 14; k++) {
          g.strokeStyle = rnd() < 0.5 ? '#6b4a2a' : '#fff6e8';
          g.lineWidth = 1 + rnd() * 2;
          const x = i * pw + rnd() * pw;
          g.beginPath(); g.moveTo(x, y); g.bezierCurveTo(x + rnd() * 8 - 4, y + len * 0.3, x + rnd() * 8 - 4, y + len * 0.7, x + rnd() * 6 - 3, y + len); g.stroke();
        }
        g.globalAlpha = 0.35; g.fillStyle = '#5a4128';
        g.fillRect(i * pw, y, pw, 2); g.fillRect(i * pw, y, 2, len);
        g.globalAlpha = 1;
        y += len;
      }
    }
  }, [W / 4, D / 4]);
}
function carpetTex() {
  return canvasTex(512, 512, (g, w, h) => {
    g.fillStyle = '#e9e9e9'; g.fillRect(0, 0, w, h);
    const id = g.getImageData(0, 0, w, h);
    for (let i = 0; i < id.data.length; i += 4) {
      const v = 214 + rnd() * 41;
      id.data[i] = id.data[i + 1] = id.data[i + 2] = v;
    }
    g.putImageData(id, 0, 0);
    g.strokeStyle = 'rgba(0,0,0,0.06)'; g.lineWidth = 2;
    for (let i = 0; i <= 2; i++) { g.beginPath(); g.moveTo(i * w / 2, 0); g.lineTo(i * w / 2, h); g.stroke(); g.beginPath(); g.moveTo(0, i * h / 2); g.lineTo(w, i * h / 2); g.stroke(); }
  }, [4, 4]);
}
function skyTex(night) {
  return canvasTex(1024, 256, (g, w, h) => {
    const gr = g.createLinearGradient(0, 0, 0, h);
    if (night) { gr.addColorStop(0, '#0b1322'); gr.addColorStop(1, '#1b2a44'); }
    else { gr.addColorStop(0, '#bcd8ea'); gr.addColorStop(1, '#eef3f2'); }
    g.fillStyle = gr; g.fillRect(0, 0, w, h);
    // skyline
    let x = 0;
    while (x < w) {
      const bw = 30 + rnd() * 70, bh = 40 + rnd() * 120;
      g.fillStyle = night ? '#101826' : `rgba(150,170,180,${0.25 + rnd() * 0.2})`;
      g.fillRect(x, h - bh, bw, bh);
      if (night) for (let k = 0; k < bw * bh / 140; k++) { g.fillStyle = `rgba(255,214,140,${0.3 + rnd() * 0.6})`; g.fillRect(x + 3 + rnd() * (bw - 6), h - bh + 4 + rnd() * (bh - 8), 2, 3); }
      x += bw + 4;
    }
  });
}
function screenTex(accent) {
  return canvasTex(512, 300, (g, w, h) => {
    g.fillStyle = '#0f1115'; g.fillRect(0, 0, w, h);
    g.fillStyle = '#1b1e25'; g.fillRect(0, 0, 110, h);
    for (let i = 0; i < 6; i++) { g.fillStyle = i === 1 ? accent : '#2b2f38'; g.fillRect(16, 24 + i * 34, 78, 14); }
    for (let i = 0; i < 4; i++) { g.fillStyle = '#20242c'; g.fillRect(130 + i * 94, 24, 84, 60); g.fillStyle = accent; g.fillRect(140 + i * 94, 66, 20 + rnd() * 50, 8); }
    g.strokeStyle = accent; g.lineWidth = 4; g.beginPath(); g.moveTo(130, 250);
    for (let i = 0; i < 12; i++) g.lineTo(130 + i * 32, 250 - 20 - rnd() * 110 - i * 4);
    g.stroke();
  });
}

// ---------- materials ----------
const M = {};
function mat(key, opts) { return M[key] || (M[key] = new THREE.MeshStandardMaterial(opts)); }

// ---------- geometry helpers ----------
const RB = {};
function rbox(w, h, d, r, material, x, y, z, parent, opts = {}) {
  const k = [w, h, d, r].map((v) => v.toFixed(3)).join('_');
  const geo = RB[k] || (RB[k] = new RoundedBoxGeometry(w, h, d, 3, Math.min(r, w / 2, h / 2, d / 2)));
  const m = new THREE.Mesh(geo, material);
  m.position.set(x, y + h / 2, z);
  m.castShadow = opts.cast !== false; m.receiveShadow = true;
  parent.add(m); return m;
}
// Varios: caché de geometrías (todas las personas comparten las mismas).
const GC = {};
function geo(k, make) { return GC[k] || (GC[k] = make()); }
function cyl(rt, rb, h, material, x, y, z, parent, seg = 24) {
  const m = new THREE.Mesh(geo(`c${rt.toFixed(3)}_${rb.toFixed(3)}_${h.toFixed(3)}_${seg}`, () => new THREE.CylinderGeometry(rt, rb, h, seg)), material);
  m.position.set(x, y + h / 2, z); m.castShadow = true; m.receiveShadow = true; parent.add(m); return m;
}
function sph(r, material, x, y, z, parent, sx = 1, sy = 1, sz = 1) {
  const m = new THREE.Mesh(geo(`s${r.toFixed(4)}`, () => new THREE.SphereGeometry(r, 24, 16)), material);
  m.position.set(x, y, z); m.scale.set(sx, sy, sz); m.castShadow = true; m.receiveShadow = true; parent.add(m); return m;
}
// capsule between two points
function limb(a, b, r, material, parent) {
  const A = new THREE.Vector3(...a), B = new THREE.Vector3(...b);
  const len = A.distanceTo(B);
  const L = Math.max(0.001, Math.round(len * 200) / 200);
  const m = new THREE.Mesh(geo(`k${r.toFixed(3)}_${L.toFixed(3)}`, () => new THREE.CapsuleGeometry(r, L, 6, 12)), material);
  m.position.copy(A).add(B).multiplyScalar(0.5);
  m.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), B.clone().sub(A).normalize());
  m.castShadow = true; m.receiveShadow = true; parent.add(m); return m;
}

const SKIN = ['#F1D3B8', '#E2B48F', '#C68E66', '#9B6A47', '#6E4A33', '#F6DCC7'];
const HAIR = ['#2A211C', '#4B3426', '#7A5A3A', '#B8925E', '#1A1A1A', '#8C8C8C', '#5E2E1F'];
const PANTS = ['#2C2F36', '#3A3E48', '#4A4237', '#22252B', '#5A5E66'];

function personLook(deptColor, key) {
  const saved = seed; let h = 0; for (const ch of String(key)) h = (h * 31 + ch.charCodeAt(0)) % 2147483647; seed = h + 101;
  const shirt = new THREE.Color(deptColor).lerp(new THREE.Color('#d9d4cc'), 0.18);
  return {
    // Varios: un material por color, compartido entre personas.
    skin: (() => { const c = SKIN[Math.floor(rnd() * SKIN.length)]; return mat('skin' + c, { color: c, roughness: 0.65 }); })(),
    hair: (() => { const c = pick(HAIR); return mat('hair' + c, { color: c, roughness: 0.75 }); })(),
    shirt: mat('shirt' + deptColor, { color: shirt, roughness: 0.85 }),
    pants: (() => { const c = pick(PANTS); return mat('pants' + c, { color: c, roughness: 0.9 }); })(),
    shoe: mat('shoe', { color: '#1b1b1d', roughness: 0.5 }),
    long: rnd() < 0.4,
    _: (seed = saved),
  };
}
function head(L, x, y, z, parent, facing = 0) {
  const g = new THREE.Group(); g.position.set(x, y, z); g.rotation.y = facing; parent.add(g);
  cyl(0.045, 0.05, 0.08, L.skin, 0, -0.16, 0, g);
  sph(0.105, L.skin, 0, 0, 0, g, 0.92, 1.05, 1.0);
  const cap = new THREE.Mesh(geo('cap', () => new THREE.SphereGeometry(0.112, 24, 16, 0, Math.PI * 2, 0, Math.PI * 0.52)), L.hair);
  cap.position.set(0, 0.012, -0.012); cap.rotation.x = -0.35; cap.castShadow = true; g.add(cap);
  if (L.long) { const back = rbox(0.2, 0.2, 0.07, 0.035, L.hair, 0, -0.17, -0.07, g); }
  // ears
  sph(0.022, L.skin, 0.098, -0.01, 0.0, g); sph(0.022, L.skin, -0.098, -0.01, 0.0, g);
  return g;
}
// seated person facing +z, hips at (x, z)
function seated(x, z, deptColor, state, parent, key) {
  const L = personLook(deptColor, key); const g = new THREE.Group(); g.position.set(x, 0, z); parent.add(g);
  const hy = 0.56;
  for (const s of [-1, 1]) {
    limb([0.09 * s, hy, 0.02], [0.1 * s, hy + 0.01, 0.42], 0.068, L.pants, g);
    limb([0.1 * s, hy, 0.44], [0.1 * s, 0.1, 0.48], 0.056, L.pants, g);
    rbox(0.1, 0.07, 0.2, 0.03, L.shoe, 0.1 * s, 0.0, 0.53, g);
  }
  const lean = state === 'free' ? -0.06 : 0.06;
  const torso = new THREE.Group(); torso.position.set(0, hy, 0); torso.rotation.x = lean; g.add(torso);
  const t = limb([0, 0.08, 0], [0, 0.42, 0], 0.15, L.shirt, torso); t.scale.set(1.25, 1, 0.82);
  sph(0.075, L.shirt, 0.17, 0.43, 0, torso); sph(0.075, L.shirt, -0.17, 0.43, 0, torso);
  head(L, 0, 0.66, 0.02, torso);
  for (const s of [-1, 1]) {
    if (state === 'free') {
      limb([0.19 * s, 0.43, 0], [0.22 * s, 0.18, 0.06], 0.045, L.shirt, torso);
      limb([0.22 * s, 0.18, 0.06], [0.16 * s, 0.06, 0.3], 0.038, L.skin, torso);
    } else {
      limb([0.19 * s, 0.43, 0], [0.22 * s, 0.2, 0.12], 0.045, L.shirt, torso);
      limb([0.22 * s, 0.2, 0.12], [0.11 * s, 0.22, 0.46], 0.038, L.skin, torso);
    }
  }
  g.userData.agent = key;
  return { group: g, headPos: new THREE.Vector3(x, hy + 0.66 + 0.02, z) };
}
// standing / walking person; dir = angle around y (0 = facing +z); phase in [-1,1]
export function standing(x, z, deptColor, dir, phase, parent, carry, key) {
  const L = personLook(deptColor, key); const g = new THREE.Group(); g.position.set(x, 0, z); g.rotation.y = dir; parent.add(g);
  const hip = 0.88, sw = 0.42 * phase;
  for (const s of [-1, 1]) {
    const a = sw * s;
    const knee = [0.09 * s, hip - 0.42 * Math.cos(a), 0.42 * Math.sin(a)];
    const foot = [0.09 * s, 0.07, knee[2] + (s * phase > 0 ? 0.02 : -0.05)];
    limb([0.09 * s, hip, 0], knee, 0.068, L.pants, g);
    limb(knee, foot, 0.056, L.pants, g);
    const sh = rbox(0.1, 0.07, 0.22, 0.03, L.shoe, foot[0], 0.0, foot[2] + 0.04, g);
  }
  const t = limb([0, hip + 0.08, 0], [0, hip + 0.42, 0], 0.15, L.shirt, g); t.scale.set(1.25, 1, 0.82);
  sph(0.075, L.shirt, 0.17, hip + 0.43, 0, g); sph(0.075, L.shirt, -0.17, hip + 0.43, 0, g);
  head(L, 0, hip + 0.66, 0.01, g);
  for (const s of [-1, 1]) {
    const a = -sw * s * 0.8;
    const elbow = [0.21 * s, hip + 0.18, 0.26 * Math.sin(a)];
    const hand = carry && s === 1 ? [0.18, hip + 0.12, 0.26] : [0.22 * s, hip - 0.04, elbow[2] + 0.22 * Math.sin(a) + 0.03];
    limb([0.19 * s, hip + 0.43, 0], elbow, 0.045, L.shirt, g);
    limb(elbow, hand, 0.038, L.skin, g);
    if (carry && s === 1) {
      const doc = rbox(0.21, 0.28, 0.012, 0.004, mat('paper', { color: '#ffffff', roughness: 0.6 }), 0.18, hip + 0.02, 0.3, g);
      doc.rotation.x = -0.5;
    }
  }
  g.userData.agent = key;
  return { group: g, headPos: new THREE.Vector3(x, hip + 0.66, z) };
}

function chair(x, z, parent, color, facing = 0) {
  const g = new THREE.Group(); g.position.set(x, 0, z); g.rotation.y = facing; parent.add(g);
  const frame = mat('chairFrame', { color: '#2a2b2e', roughness: 0.35, metalness: 0.6 });
  const fabric = new THREE.MeshStandardMaterial({ color: color || '#3a3b40', roughness: 0.95 });
  for (let i = 0; i < 5; i++) {
    const a = (i / 5) * Math.PI * 2;
    const leg = rbox(0.3, 0.035, 0.05, 0.015, frame, 0, 0.06, 0, g); leg.position.set(Math.cos(a) * 0.15, 0.08, Math.sin(a) * 0.15); leg.rotation.y = -a;
    sph(0.028, frame, Math.cos(a) * 0.29, 0.03, Math.sin(a) * 0.29, g);
  }
  cyl(0.025, 0.025, 0.36, frame, 0, 0.08, 0, g);
  rbox(0.5, 0.08, 0.48, 0.035, fabric, 0, 0.44, 0.02, g);
  const back = rbox(0.48, 0.52, 0.06, 0.04, fabric, 0, 0.58, -0.24, g); back.rotation.x = -0.12;
  limb([0, 0.48, -0.22], [0, 0.66, -0.27], 0.022, frame, g);
  for (const s of [-1, 1]) { rbox(0.05, 0.03, 0.24, 0.012, frame, 0.25 * s, 0.68, 0.02, g); limb([0.25 * s, 0.5, -0.02], [0.25 * s, 0.68, 0.0], 0.014, frame, g); }
  return g;
}

function plant(x, z, s, parent, kind = 'bush') {
  const pot = mat('pot', { color: '#E8E3DA', roughness: 0.55 });
  const soil = mat('soil', { color: '#3b2d22', roughness: 1 });
  const g = new THREE.Group(); g.position.set(x, 0, z); g.scale.setScalar(s); parent.add(g);
  cyl(0.2, 0.15, 0.42, pot, 0, 0, 0, g, 28);
  cyl(0.185, 0.185, 0.01, soil, 0, 0.405, 0, g);
  const leafGeo = new THREE.SphereGeometry(1, 10, 8);
  const greens = ['#4E7F4F', '#3E6B42', '#5F9160', '#6E9F5E', '#2F5A36'];
  const n = kind === 'tall' ? 70 : 46;
  const inst = new THREE.InstancedMesh(leafGeo, new THREE.MeshStandardMaterial({ roughness: 0.7 }), n);
  const o = new THREE.Object3D(), col = new THREE.Color();
  for (let i = 0; i < n; i++) {
    const h = kind === 'tall' ? 0.5 + rnd() * 1.1 : 0.45 + rnd() * 0.5;
    const a = rnd() * Math.PI * 2, r = (kind === 'tall' ? 0.08 : 0.05) + rnd() * (kind === 'tall' ? 0.28 : 0.24) * Math.min(1, (h - 0.35) * 2);
    o.position.set(Math.cos(a) * r, h, Math.sin(a) * r);
    o.rotation.set(rnd() * 1.4 - 0.7, a, rnd() * 1.4 - 0.7);
    const L = kind === 'tall' ? 0.1 : 0.075;
    o.scale.set(L * 0.55, 0.012, L);
    o.updateMatrix(); inst.setMatrixAt(i, o.matrix);
    inst.setColorAt(i, col.set(pick(greens)));
  }
  inst.castShadow = true; inst.receiveShadow = true; g.add(inst);
  if (kind === 'tall') limb([0, 0.4, 0], [0.02, 1.4, 0.01], 0.012, mat('stem', { color: '#5a4630', roughness: 0.8 }), g);
  return g;
}

function desk(x, z, parent, opts) {
  // desk spans x..x+1.6, z..z+0.8 ; person sits at -z side facing +z
  const top = mat('deskTop', { color: opts.night ? '#8a7258' : '#D8C3A5', roughness: 0.55, map: opts.wood2 });
  const white = mat('deskLeg', { color: opts.night ? '#3a3b40' : '#EDEBE6', roughness: 0.4, metalness: 0.3 });
  const g = new THREE.Group(); parent.add(g);
  rbox(1.6, 0.035, 0.8, 0.012, top, x + 0.8, 0.72, z + 0.4, g);
  for (const lx of [x + 0.08, x + 1.52]) {
    rbox(0.05, 0.03, 0.7, 0.01, white, lx, 0.0, z + 0.4, g);
    rbox(0.04, 0.69, 0.04, 0.01, white, lx, 0.03, z + 0.4, g);
    rbox(0.05, 0.03, 0.7, 0.01, white, lx, 0.69, z + 0.4, g);
  }
  rbox(1.4, 0.32, 0.02, 0.005, white, x + 0.8, 0.36, z + 0.62, g); // modesty panel
  // monitor (faces -z, toward person)
  const mx = x + 0.95;
  const blk = mat('mon', { color: '#1c1d20', roughness: 0.35, metalness: 0.4 });
  rbox(0.22, 0.012, 0.16, 0.006, blk, mx, 0.755, z + 0.32, g);
  rbox(0.04, 0.2, 0.025, 0.01, blk, mx, 0.76, z + 0.36, g);
  const mon = rbox(0.66, 0.39, 0.028, 0.008, blk, mx, 0.9, z + 0.34, g);
  const screenMat = new THREE.MeshStandardMaterial({ color: '#000', emissive: '#ffffff', emissiveMap: opts.screen, emissiveIntensity: opts.state ? 0.9 : 0.05 });
  const scr = new THREE.Mesh(geo('screen', () => new THREE.PlaneGeometry(0.63, 0.36)), screenMat);
  scr.position.set(mx, 1.095, z + 0.325); scr.rotation.y = Math.PI; g.add(scr);
  // keyboard, mouse, mug, notebook
  rbox(0.42, 0.016, 0.13, 0.008, mat('kb', { color: '#E9E7E2', roughness: 0.6 }), mx - 0.08, 0.755, z + 0.16, g);
  rbox(0.05, 0.02, 0.08, 0.02, mat('kb', {}), mx + 0.25, 0.755, z + 0.17, g);
  const mug = cyl(0.04, 0.035, 0.1, mat('mug' + (seed % 3), { color: pick(['#ffffff', '#2F7F7A', '#E9D9C0']), roughness: 0.4 }), x + 1.45, 0.755, z + 0.28, g);
  if (rnd() < 0.6) rbox(0.22, 0.015, 0.3, 0.004, mat('note', { color: '#F4EFE3', roughness: 0.8 }), x + 0.28, 0.755, z + 0.3, g).rotation.y = rnd() * 0.4 - 0.2;
  if (rnd() < 0.35) plant(x + 0.18, z + 0.62, 0.32, g);
  chair(x + 0.62, z - 0.42, g, opts.chairColor);
  let anchor = null, person = null;
  if (opts.state) {
    const p = seated(x + 0.62, z - 0.42, opts.dept, opts.state, g, opts.key);
    anchor = p.headPos; person = p.group;
  }
  // Varios: lo necesario para cambiar el estado sin reconstruir la escena y para los paseos.
  return { anchor, seat: new THREE.Vector3(x + 0.62, 0, z - 0.42), group: g, person, screenMat, dept: opts.dept, key: opts.key, state: opts.state, front: new THREE.Vector3(x + 0.62, 0, z + 1.25), desk: [x, z] };
}

function cabinet(x0, z0, x1, z1, parent, night) {
  const white = mat('cab', { color: night ? '#3c3d43' : '#F2F0EB', roughness: 0.5 });
  rbox(x1 - x0, 0.75, z1 - z0, 0.02, white, (x0 + x1) / 2, 0, (z0 + z1) / 2, parent);
  let x = x0 + 0.15;
  while (x < x1 - 0.4) {
    const w = 0.04 + rnd() * 0.05, h = 0.2 + rnd() * 0.12;
    const c = pick(['#8E2F3C', '#2F7F7A', '#A8761F', '#3F4F9A', '#E8E2D6', '#C9C1B3', '#2b2b2e']);
    const b = rbox(w, h, 0.22, 0.006, mat('book' + c, { color: c, roughness: 0.8 }), x, 0.75, (z0 + z1) / 2, parent);
    if (rnd() < 0.1) b.rotation.z = 0.25;
    x += w + 0.008 + (rnd() < 0.1 ? 0.3 : 0);
  }
  plant(x1 - 0.2, (z0 + z1) / 2, 0.3, parent).position.y = 0.75;
}

function windowWall(axis, len, parent, glassMat, frameMat, wallMat) {
  // axis 'x': wall along x at z=0 (thickness to -z). axis 'z': wall along z at x=0.
  const T = 0.22, sill = 0.85, head = 2.55;
  const g = new THREE.Group(); parent.add(g);
  const put = (a0, a1, y0, y1, m, t = T, off = -T / 2) => {
    const L = a1 - a0, c = (a0 + a1) / 2;
    if (axis === 'x') rbox(L, y1 - y0, t, 0.004, m, c, y0, off, g);
    else rbox(t, y1 - y0, L, 0.004, m, off, y0, c, g);
  };
  put(-T, len, 0, sill, wallMat); put(-T, len, head, WALL_H, wallMat);
  let a = 0; const bays = [];
  for (let s = 1.0; s + 3.0 <= len - 0.5; s += 3.5) bays.push([s, s + 3.0]);
  for (const [s, e] of bays) { put(a, s, sill, head, wallMat); a = e; }
  put(a, len, sill, head, wallMat);
  for (const [s, e] of bays) {
    for (const m of [s, s + 1, s + 2, e]) put(m - 0.025, m + 0.025, sill, head, frameMat, 0.08, -0.08);
    put(s, e, sill - 0.02, sill + 0.03, frameMat, 0.3, -0.05);
    put(s, e, head - 0.04, head, frameMat, 0.08, -0.08);
    const glass = new THREE.Mesh(new THREE.PlaneGeometry(e - s, head - sill), glassMat);
    if (axis === 'x') { glass.position.set((s + e) / 2, (sill + head) / 2, -0.08); }
    else { glass.position.set(-0.08, (sill + head) / 2, (s + e) / 2); glass.rotation.y = Math.PI / 2; }
    g.add(glass);
  }
  return bays;
}

// Varios: estado de un puesto sin reconstruir nada más (null = silla vacía).
export function setSeated(desk, state) {
  if (desk.person) { desk.group.remove(desk.person); desk.person = null; }
  desk.state = state; desk.anchor = null;
  if (state) {
    const p = seated(desk.seat.x, desk.seat.z, desk.dept, state, desk.group, desk.key);
    desk.person = p.group; desk.anchor = p.headPos;
  }
  desk.screenMat.emissiveIntensity = state ? 0.9 : 0.05;
  return desk.anchor;
}

export function buildOffice({ night = false, override = {}, walkers = [], showPath = null, depts = null } = {}) {
  seed = 7;
  // Varios: departamentos reales. Cada uno: { key, name, color, at, agents: [{ id, state }] } (6 puestos por zona).
  const DL = depts || DEPTS.map((d) => ({ ...d, agents: d.states.map((st, i) => ({ id: d.key + i, state: st })) }));
  const desks = {};
  const scene = new THREE.Scene();
  const anchors = {}, pins = {};
  // floor
  const wood = woodTex(night);
  const floor = new THREE.Mesh(new THREE.BoxGeometry(W + 0.44, 0.3, D + 0.44), [null, null, new THREE.MeshStandardMaterial({ map: wood, roughness: 0.5 }), null, null, null].map((m) => m || mat('slab', { color: night ? '#24252a' : '#E3DDD2', roughness: 0.9 })));
  floor.position.set(W / 2 - 0.22, -0.15, D / 2 - 0.22); floor.receiveShadow = true; scene.add(floor);
  // walls
  const wallMat = mat('wall', { color: night ? '#34353b' : '#F4F1EC', roughness: 0.9 });
  const frameMat = mat('frame', { color: night ? '#2a2b30' : '#3B3C40', roughness: 0.4, metalness: 0.5 });
  const glassMat = new THREE.MeshPhysicalMaterial({ color: night ? '#22344d' : '#cfe3ea', transparent: true, opacity: night ? 0.55 : 0.22, roughness: 0.05, metalness: 0, envMapIntensity: 1.5, side: THREE.DoubleSide, depthWrite: false });
  windowWall('x', W, scene, glassMat, frameMat, wallMat);
  windowWall('z', D, scene, glassMat, frameMat, wallMat);
  // outside backdrop seen through windows
  const sky = new THREE.MeshBasicMaterial({ map: skyTex(night), toneMapped: false });
  const p1 = new THREE.Mesh(new THREE.PlaneGeometry(W - 0.4, 2.0), sky); p1.position.set(W / 2, 1.2, -0.9); scene.add(p1);
  const p2 = new THREE.Mesh(new THREE.PlaneGeometry(D - 0.4, 2.0), sky); p2.position.set(-0.9, 1.2, D / 2); p2.rotation.y = Math.PI / 2; scene.add(p2);

  // zones
  const carpet = carpetTex();
  const wood2 = null;
  for (const d of DL) {
    const [zx, zy] = d.at;
    const tint = new THREE.Color(d.color).lerp(new THREE.Color(night ? '#2c2d33' : '#e6e1d8'), night ? 0.72 : 0.62);
    const rug = new THREE.Mesh(new THREE.BoxGeometry(7.6, 0.012, 6.6), new THREE.MeshStandardMaterial({ color: tint, map: carpet, roughness: 1 }));
    rug.position.set(zx + 4, 0.006, zy + 3.5); rug.receiveShadow = true; scene.add(rug);
    const edge = new THREE.Mesh(new THREE.BoxGeometry(7.7, 0.008, 6.7), mat('edge' + d.key, { color: new THREE.Color(d.color).lerp(new THREE.Color('#888'), 0.2), roughness: 0.9 }));
    edge.position.set(zx + 4, 0.004, zy + 3.5); scene.add(edge);
    cabinet(zx + 0.6, zy + 0.25, zx + 3.0, zy + 0.75, scene, night);
    plant(zx + 7.3, zy + 0.7, 1.2, scene, 'tall');
    plant(zx + 0.55, zy + 6.4, 0.9, scene);
    const screen = screenTex(d.color);
    let i = 0;
    for (const ry of [zy + 2.35, zy + 5.0]) for (const cx of [zx + 0.6, zx + 3.2, zx + 5.8]) {
      const ag = d.agents[i];
      const k = ag ? ag.id : d.key + '-libre' + i;
      let st = ag ? ag.state || 'free' : null;
      if (k in override) st = override[k];
      const r = desk(cx, ry, scene, { state: st, dept: d.color, night, screen, wood2, key: k });
      r.deptKey = d.key; desks[k] = r;
      if (r.anchor) anchors[k] = { pos: r.anchor, state: st, dept: d.key };
      i++;
    }
    pins[d.key] = new THREE.Vector3(zx + 4, 2.6, zy + 3.4);
  }
  // lounge (Varios: solo si ninguna zona ocupa su sitio)
  if (!DL.some((d) => d.at[0] < 9 && d.at[1] > 7 && d.at[1] < 12)) {
    const x = 1.8, z = 9.7;
    const rug = new THREE.Mesh(new THREE.BoxGeometry(5.2, 0.014, 3.2), new THREE.MeshStandardMaterial({ color: night ? '#4a4038' : '#D9CBB4', map: carpet, roughness: 1 }));
    rug.position.set(x + 2.6, 0.007, z + 1.6); rug.receiveShadow = true; scene.add(rug);
    const fab = mat('sofa', { color: night ? '#55565e' : '#B9B2A6', roughness: 0.95 });
    rbox(3.0, 0.42, 0.95, 0.06, fab, x + 2.0, 0.08, z + 0.75, scene);
    rbox(3.0, 0.45, 0.25, 0.08, fab, x + 2.0, 0.4, z + 0.36, scene);
    for (const s of [-1, 1]) rbox(0.22, 0.28, 0.95, 0.08, fab, x + 2.0 + s * 1.39, 0.4, z + 0.75, scene);
    for (let i = 0; i < 3; i++) rbox(0.86, 0.14, 0.62, 0.07, mat('cush', { color: night ? '#606169' : '#C8C1B5', roughness: 1 }), x + 1.1 + i * 0.9, 0.5, z + 0.86, scene);
    for (const s of [-1, 1]) for (const e of [-1, 1]) cyl(0.025, 0.02, 0.08, frameMat, x + 2.0 + s * 1.4, 0, z + 0.75 + e * 0.4, scene);
    const oak = mat('oak', { color: night ? '#7a6048' : '#C9A47A', roughness: 0.5 });
    rbox(1.4, 0.05, 0.75, 0.02, oak, x + 2.0, 0.38, z + 1.95, scene);
    for (const s of [-1, 1]) for (const e of [-1, 1]) cyl(0.02, 0.02, 0.38, frameMat, x + 2.0 + s * 0.6, 0, z + 1.95 + e * 0.3, scene);
    cyl(0.06, 0.05, 0.12, mat('vase', { color: '#ffffff', roughness: 0.3 }), x + 1.7, 0.43, z + 1.9, scene);
    rbox(0.3, 0.03, 0.22, 0.004, mat('mag', { color: '#2F7F7A', roughness: 0.6 }), x + 2.3, 0.43, z + 2.0, scene).rotation.y = 0.3;
    // armchair
    const ac = new THREE.Group(); ac.position.set(x + 4.4, 0, z + 1.8); ac.rotation.y = -Math.PI / 2; scene.add(ac);
    rbox(0.85, 0.4, 0.8, 0.08, mat('arm', { color: night ? '#5c4a3c' : '#A8846A', roughness: 0.9 }), 0, 0.06, 0, ac);
    rbox(0.85, 0.4, 0.2, 0.08, mat('arm', {}), 0, 0.42, -0.32, ac);
    // floor lamp
    cyl(0.14, 0.14, 0.02, frameMat, x + 0.4, 0, z + 0.4, scene); cyl(0.012, 0.012, 1.55, frameMat, x + 0.4, 0.02, z + 0.4, scene);
    const shade = cyl(0.12, 0.2, 0.26, new THREE.MeshStandardMaterial({ color: '#F3EBDD', emissive: '#FFE2B0', emissiveIntensity: night ? 1.6 : 0.15, roughness: 0.9, side: THREE.DoubleSide }), x + 0.4, 1.5, z + 0.4, scene);
    if (night) { const pl = new THREE.PointLight('#FFD9A0', 6, 5, 2); pl.position.set(x + 0.4, 1.45, z + 0.4); scene.add(pl); }
    plant(x + 4.9, z + 0.4, 1.3, scene, 'tall');
  }
  // knowledge core ("Cerebro")
  {
    const x0 = 11.5, z0 = 9.9, x1 = 18.5, z1 = 14.3; // Varios: centrado en el pasillo central más ancho
    const dark = mat('core', { color: '#1d1c20', roughness: 0.35, metalness: 0.2 });
    rbox(x1 - x0, 0.12, z1 - z0, 0.02, dark, (x0 + x1) / 2, 0, (z0 + z1) / 2, scene);
    const glass = new THREE.MeshPhysicalMaterial({ color: '#d7eef0', transparent: true, opacity: 0.16, roughness: 0.03, envMapIntensity: 2, side: THREE.DoubleSide, depthWrite: false });
    const H = 2.4;
    const pane = (w, cx, cz, rotY) => { const m = new THREE.Mesh(new THREE.PlaneGeometry(w, H - 0.12), glass); m.position.set(cx, 0.12 + (H - 0.12) / 2, cz); m.rotation.y = rotY; scene.add(m); };
    pane(x1 - x0, (x0 + x1) / 2, z0, 0); pane(x1 - x0, (x0 + x1) / 2, z1, 0);
    pane(z1 - z0, x0, (z0 + z1) / 2, Math.PI / 2); pane(z1 - z0, x1, (z0 + z1) / 2, Math.PI / 2);
    const alu = mat('alu', { color: '#c8ccd0', roughness: 0.3, metalness: 0.8 });
    for (const [ax, az] of [[x0, z0], [x1, z0], [x0, z1], [x1, z1]]) rbox(0.05, H, 0.05, 0.005, alu, ax, 0, az, scene);
    rbox(x1 - x0, 0.05, 0.05, 0.005, alu, (x0 + x1) / 2, H - 0.05, z1, scene); rbox(0.05, 0.05, z1 - z0, 0.005, alu, x1, H - 0.05, (z0 + z1) / 2, scene);
    rbox(x1 - x0, 0.05, 0.05, 0.005, alu, (x0 + x1) / 2, H - 0.05, z0, scene); rbox(0.05, 0.05, z1 - z0, 0.005, alu, x0, H - 0.05, (z0 + z1) / 2, scene);
    // racks
    const rackM = mat('rack', { color: '#202024', roughness: 0.45, metalness: 0.5 });
    const ledG = new THREE.BoxGeometry(0.03, 0.012, 0.004);
    const ledCols = ['#2BC4AE', '#E9E4DA', '#7C9CFF', '#E08A1E'];
    for (let i = 0; i < 5; i++) {
      const rx = x0 + 3.5 + i * 0.68;
      rbox(0.6, 1.95, 0.85, 0.02, rackM, rx, 0.12, z0 + 0.7, scene);
      for (let j = 0; j < 16; j++) {
        rbox(0.54, 0.008, 0.01, 0.002, mat('slot', { color: '#34343a', roughness: 0.6 }), rx, 0.3 + j * 0.105, z0 + 1.126, scene, { cast: false });
        for (let l = 0; l < 3; l++) {
          const c = ledCols[Math.floor(rnd() * 4)];
          const led = new THREE.Mesh(ledG, mat('led' + c, { color: c, emissive: c, emissiveIntensity: 2.5 }));
          led.position.set(rx + 0.15 + l * 0.045, 0.34 + j * 0.105, z0 + 1.128); scene.add(led);
        }
      }
    }
    // plinth + knowledge graph
    const cx = x0 + 1.9, cz = (z0 + z1) / 2 + 0.3;
    cyl(1.05, 1.1, 0.5, mat('plinth', { color: '#141317', roughness: 0.25, metalness: 0.4 }), cx, 0.12, cz, scene, 64);
    const ring = new THREE.Mesh(new THREE.TorusGeometry(1.06, 0.012, 8, 96), mat('ring', { color: '#2BC4AE', emissive: '#2BC4AE', emissiveIntensity: 2 }));
    ring.rotation.x = Math.PI / 2; ring.position.set(cx, 0.62, cz); scene.add(ring);
    const nodes = [];
    for (let n = 0; n < 52; n++) {
      const a = rnd() * Math.PI * 2, r = 0.12 + Math.sqrt(rnd()) * 0.85, y = 0.85 + rnd() * 0.75;
      nodes.push(new THREE.Vector3(cx + Math.cos(a) * r, y, cz + Math.sin(a) * r * 0.9));
    }
    const ng = new THREE.SphereGeometry(0.022, 10, 8);
    nodes.forEach((p, n) => { const c = DL[n % DL.length].color; const m = new THREE.Mesh(ng, mat('node' + c, { color: c, emissive: new THREE.Color(c).lerp(new THREE.Color('#fff'), 0.3), emissiveIntensity: 2.2 })); m.position.copy(p); scene.add(m); });
    const segs = [];
    for (let i = 0; i < nodes.length; i++) for (let j = i + 1; j < nodes.length; j++) if (nodes[i].distanceTo(nodes[j]) < 0.42) segs.push(nodes[i], nodes[j]);
    const lg = new THREE.BufferGeometry().setFromPoints(segs);
    scene.add(new THREE.LineSegments(lg, new THREE.LineBasicMaterial({ color: '#bff3ea', transparent: true, opacity: 0.35 })));
    const coreGlow = new THREE.PointLight('#2BC4AE', night ? 8 : 3, 4, 2); coreGlow.position.set(cx, 1.2, cz); scene.add(coreGlow);
    pins.core = new THREE.Vector3(cx, 0.1, z1 + 0.2);
  }
  // meeting area
  {
    const x = 23.0, z = 10.2;
    const oak = mat('oak', {});
    rbox(3.2, 0.05, 1.2, 0.02, oak, x + 1.8, 0.72, z + 1.15, scene);
    for (const s of [-1, 1]) rbox(0.08, 0.72, 0.9, 0.02, frameMat, x + 1.8 + s * 1.3, 0, z + 1.15, scene);
    for (let i = 0; i < 3; i++) { chair(x + 0.8 + i * 1.0, z + 0.25, scene, '#4a4b52', 0); chair(x + 0.8 + i * 1.0, z + 2.05, scene, '#4a4b52', Math.PI); }
    const tv = rbox(1.6, 0.92, 0.05, 0.01, mat('mon', {}), x + 3.95, 0.75, z + 1.15, scene); tv.rotation.y = -Math.PI / 2;
    const tvs = new THREE.Mesh(new THREE.PlaneGeometry(1.52, 0.85), new THREE.MeshStandardMaterial({ color: '#000', emissive: '#fff', emissiveMap: screenTex('#2F7F7A'), emissiveIntensity: 0.8 }));
    tvs.position.set(x + 3.92, 1.21, z + 1.15); tvs.rotation.y = -Math.PI / 2; scene.add(tvs);
    rbox(0.08, 0.75, 0.5, 0.01, frameMat, x + 3.97, 0, z + 1.15, scene);
    plant(x + 0.1, z + 3.0, 1.0, scene, 'tall');
  }
  for (const [px, pz, s] of [[9.9, 15.6, 1.0], [20.1, 15.6, 1.0], [29.3, 23.7, 1.1], [9.9, 8.4, 0.9], [20.1, 8.4, 0.9]]) plant(px, pz, s, scene, 'tall');

  // walkers
  for (const w of walkers) {
    const d = DL.find((q) => q.key === w.dept);
    const p = standing(w.x, w.z, d.color, w.dir, w.phase || 0, scene, w.carry, w.as || w.key);
    anchors[w.key || 'walker'] = { pos: p.headPos, state: w.state || 'walk', dept: w.dept };
  }
  // route line
  if (showPath) {
    const pts = showPath.map(([x, z]) => new THREE.Vector3(x, 0.03, z));
    const curve = new THREE.CatmullRomCurve3(pts, false, 'catmullrom', 0.05);
    const dots = curve.getSpacedPoints(Math.floor(curve.getLength() / 0.28));
    const dg = new THREE.CircleGeometry(0.045, 12); dg.rotateX(-Math.PI / 2);
    const dm = new THREE.MeshBasicMaterial({ color: '#6B625A', transparent: true, opacity: 0.75 });
    dots.forEach((p) => { const m = new THREE.Mesh(dg, dm); m.position.copy(p); scene.add(m); });
    const end = new THREE.Mesh(new THREE.RingGeometry(0.28, 0.33, 40), dm); end.rotation.x = -Math.PI / 2; end.position.copy(pts[pts.length - 1]); scene.add(end);
  }
  return { scene, anchors, pins, desks };
}

export function lights(scene, renderer, night, depts = DEPTS) {
  const pm = new THREE.PMREMGenerator(renderer);
  scene.environment = pm.fromScene(new RoomEnvironment(), 0.04).texture;
  scene.environmentIntensity = night ? 0.12 : 0.55;
  const hemi = new THREE.HemisphereLight(night ? '#5d6c96' : '#ffffff', night ? '#1a1712' : '#cdbfa8', night ? 0.25 : 0.9);
  scene.add(hemi);
  const sun = new THREE.DirectionalLight(night ? '#8fa6ff' : '#FFF0D8', night ? 0.35 : 2.6);
  sun.position.set(-14, 22, 4); sun.target.position.set(13, 0, 12); scene.add(sun.target);
  sun.castShadow = true; sun.shadow.mapSize.set(4096, 4096);
  const sc = sun.shadow.camera; sc.left = -24; sc.right = 24; sc.top = 24; sc.bottom = -24; sc.near = 1; sc.far = 80;
  sun.shadow.bias = -0.0003; sun.shadow.normalBias = 0.02; sun.shadow.radius = 4;
  scene.add(sun);
  scene.userData.sun = sun;
  if (night) {
    // warm pools of light over each team + desk glow
    for (const d of depts) {
      const s = new THREE.SpotLight('#FFD9A8', 40, 9, 0.75, 0.6, 2);
      s.position.set(d.at[0] + 4, 4.2, d.at[1] + 3.6); s.target.position.set(d.at[0] + 4, 0, d.at[1] + 3.6);
      scene.add(s); scene.add(s.target);
    }
    const s2 = new THREE.SpotLight('#FFD9A8', 25, 8, 0.8, 0.6, 2); s2.position.set(25, 4, 10.8); s2.target.position.set(25, 0, 10.8); scene.add(s2, s2.target);
  }
}

export function makeRenderer(canvas, w, h, night) {
  const r = new THREE.WebGLRenderer({ canvas, antialias: true, preserveDrawingBuffer: true });
  r.setSize(w, h, false); r.setPixelRatio(1);
  r.shadowMap.enabled = true; r.shadowMap.type = THREE.PCFSoftShadowMap;
  r.toneMapping = THREE.NeutralToneMapping; r.toneMappingExposure = night ? 1.0 : 0.94;
  r.outputColorSpace = THREE.SRGBColorSpace;
  r.setClearColor(night ? '#141518' : '#F4F1EA', 1);
  return r;
}

export function camera(w, h, target, dist, fov = 22) {
  const cam = new THREE.PerspectiveCamera(fov, w / h, 0.5, 400);
  const dir = new THREE.Vector3(1, 1.05, 1).normalize();
  cam.position.copy(target).addScaledVector(dir, dist);
  cam.lookAt(target);
  return cam;
}

export function render(renderer, scene, cam, w, h, night, ao = true) {
  const comp = new EffectComposer(renderer);
  comp.addPass(new RenderPass(scene, cam));
  if (ao) {
    const g = new GTAOPass(scene, cam, w, h);
    g.updateGtaoMaterial({ radius: 0.35, distanceExponent: 1.5, thickness: 1, scale: 1, samples: 16 });
    g.updatePdMaterial({ lumaPhi: 10, depthPhi: 2, normalPhi: 3, radius: 6, rings: 2, samples: 16 });
    g.blendIntensity = 0.9;
    comp.addPass(g);
  }
  if (night) comp.addPass(new UnrealBloomPass(new THREE.Vector2(w, h), 0.55, 0.5, 0.55));
  comp.addPass(new OutputPass());
  comp.setSize(w, h);
  comp.render();
}

// Varios: compositor persistente para el render en tiempo real (mismos pases que render()).
export function makeComposer(renderer, scene, cam, w, h, night, ao = true) {
  const comp = new EffectComposer(renderer);
  comp.addPass(new RenderPass(scene, cam));
  let gtao = null;
  if (ao) {
    gtao = new GTAOPass(scene, cam, w, h);
    gtao.updateGtaoMaterial({ radius: 0.35, distanceExponent: 1.5, thickness: 1, scale: 1, samples: 16 });
    gtao.updatePdMaterial({ lumaPhi: 10, depthPhi: 2, normalPhi: 3, radius: 6, rings: 2, samples: 16 });
    gtao.blendIntensity = 0.9;
    comp.addPass(gtao);
  }
  if (night) comp.addPass(new UnrealBloomPass(new THREE.Vector2(w, h), 0.55, 0.5, 0.55));
  comp.addPass(new OutputPass());
  comp.setSize(w, h);
  return { comp, gtao };
}

export function project(v, cam, w, h) {
  const p = v.clone().project(cam);
  return [((p.x + 1) / 2) * w, ((1 - p.y) / 2) * h];
}
