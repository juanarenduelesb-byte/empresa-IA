# Búsqueda de texto en el cerebro sin base de datos

- **Tipo:** solución · **Fecha:** noviembre de 2026 · **Estado:** validated
- **Contexto:** el CEO de la oficina necesitaba consultar los documentos del repositorio sin servidor.
- **Qué se hizo:** `tools/brain_build.py` trocea los documentos por apartados y genera `oficina/brain.json`; la oficina busca con BM25 en el navegador.
- **Resultado:** 52 documentos y 462 apartados en la última ejecución; responde con la fuente citada.
- **Qué reutilizar:** trocear por encabezados y citar siempre el apartado.
- **Límites:** solo palabras, sin sinónimos ni semántica; hay que regenerarlo a mano tras cada cambio.
