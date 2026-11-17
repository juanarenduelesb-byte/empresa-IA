# Librerías de terceros (sin modificar)

| Archivo | Proyecto | Versión | Licencia |
|---|---|---|---|
| pptxgen.bundle.js | PptxGenJS (incluye JSZip) | 3.12.0 | MIT |
| exceljs.min.js | ExcelJS | 4.4.0 | MIT |
| docx.iife.js | docx | 9.15.4 | MIT |
| jszip.min.js | JSZip | 3.10.2 | MIT o GPLv3 (se usa con MIT) |
| pdf.min.js, pdf.worker.min.js | PDF.js (pdfjs-dist) | 3.11.174 | Apache-2.0 |
| three/three.module.js y three/addons/ (solo los módulos usados) | Three.js | r170 | MIT (ver `three/LICENSE`) |

Se cargan solo cuando hace falta generar o leer un archivo. Justificación en DECISIONS.md (D-015 y D-016). Three.js solo se carga en la vista 3D.
