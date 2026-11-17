# Volcado nocturno de la oficina a GitHub (D-017)

Instrucciones para la tarea programada que corre cada noche. Están en el repositorio para que se puedan revisar y cambiar como cualquier otro documento.

**Objetivo:** que todo lo que pasa en la oficina de agentes (encargos, resultados, conversaciones entre agentes, chats con los socios, memoria, reglas y habilidades enseñadas, proyectos y decisiones propuestas) quede en el repositorio y alimente el cerebro, gastando los mínimos tokens.

## Datos
- Artefacto de la oficina: `f475bcf0-b915-4b88-9e07-039ccb390bd3` (base de datos con las colecciones de la oficina).
- Repositorio: `juanarenduelesb-byte/empresa-IA`, rama `main`.
- Marca del último volcado: `oficina/registro/ultimo-volcado.txt` (fecha ISO). Cada documento de la oficina lleva `_ts`, la fecha de su último cambio.

## Pasos
1. Actualiza el repositorio (`git pull` en `main`) y lee la marca del último volcado.
2. Para cada colección (`projects`, `tasks`, `convs`, `chats`, `routines`, `memory`, `rules`, `skills`, `agents`, `decisions`, `deliverables`, `docs`), pide a la base de datos del artefacto solo los documentos con `_ts` posterior a la marca (`db_query` con `where _ts > marca`; si no hay marca, `db_list` completo). Pagina hasta el final.
3. Si no hay nada nuevo en ninguna colección, termina sin avisar a nadie.
4. Guarda cada colección tal cual en `/tmp/volcado/<colección>.json` (lista de `{id, data}`).
5. Ejecuta, en este orden:
   ```
   python3 tools/registro_oficina.py /tmp/volcado
   python3 tools/agentes_gen.py
   python3 tools/brain_build.py oficina/brain.json
   python3 tools/check_repo.py
   python3 -m pytest -q
   ```
6. Escribe la nueva marca (la fecha `_ts` más alta vista) en `oficina/registro/ultimo-volcado.txt`.
7. Crea una rama `volcado-AAAA-MM-DD`, haz commit y abre una propuesta de cambios con el resumen que imprime `registro_oficina.py`.
8. Aceptación (D-012): acéptala tú si las comprobaciones pasan, no hay conflictos y nada del volcado parece un dato real de un cliente (nombres de empresas o personas reales, NIF, pólizas que no empiecen por `POL-FIC`, datos de salud). Si dudas, déjala abierta y dilo en la propuesta.
9. Si se ha aceptado, publica en el artefacto los archivos que han cambiado de entre `brain.json` y `agentes.json` (`publish_files` en modo patch, con la versión vigente como base), para que la oficina use el cerebro nuevo.
10. Avisa al usuario solo si algo ha fallado o ha quedado una propuesta abierta.

## Qué no se vuelca
- Proyectos marcados como confidenciales (`confidencial: true`) y todo lo suyo.
- El texto de los documentos subidos: solo su nombre.
- Cualquier registro con algo que parezca un secreto.
- Las conversaciones de «Simular conversación».

## Coste
La tarea solo mueve lo nuevo desde la última noche. Todo lo demás (regenerar el cerebro, comprobar, avisar) lo hacen scripts y GitHub Actions, sin IA.
