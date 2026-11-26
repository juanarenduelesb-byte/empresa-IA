---
tipo: "metodologia"
id: "guion-validacion-semanal"
estado: "draft"
---
# Guion de la conversación semanal de validación

**Estado:** draft. Una conversación a la semana con alguien que hace el proceso de referencia (D-011; objetivo semanal del [director comercial](../comercial/director-comercial.md)). Sirve para que lo que construimos de noche no se aleje de lo que pasa en una correduría.

## Antes (15 min, quien la dirige)
1. Elegir **una sola pregunta** que más cambiaría el plan si la respuesta fuera distinta de lo que suponemos. Suele salir de las preguntas abiertas de la [ficha de cliente](../plantillas/ficha-cliente.md) o de una hipótesis del [catálogo de excepciones](../sectores/seguros/excepciones.md).
2. Llevar uno o dos siniestros inventados de los [20 casos](../../processes/referencia-seguros-apertura-siniestros/casos/README.md) para contrastarlos.
3. Repasar las reglas: hechos del pasado, nada de enseñar la solución si no estamos en G2 y nada de pedir datos personales de clientes finales ([MOM-TEST](../fuentes/registro.md#mom-test)).

## Durante (30 min)
| Min | Bloque | Qué se hace |
|---|---|---|
| 0–3 | Abrir | Agradecer, recordar para qué es (aprender, no vender) y pedir permiso para tomar notas sin nombres |
| 3–13 | Lo último que pasó | «Cuéntame el último siniestro que te dio guerra.» Seguir el hilo con «¿y entonces?» y «¿cuánto tardó eso?» |
| 13–20 | La pregunta de la semana | Formulada como hecho pasado. Ejemplo: «¿Cuándo fue la última vez que llegó un aviso sin número de póliza? ¿Qué hiciste?» |
| 20–26 | Contrastar un caso inventado | «Este caso es inventado: ¿te ha pasado algo así? ¿Qué harías tú?» Anotar si nuestra respuesta esperada coincide con la suya |
| 26–30 | Cerrar | «¿Qué debería haberte preguntado?» y pedir un compromiso pequeño: la siguiente cita, una presentación a otra persona o ver una mañana de trabajo |

## Después (20 min, el mismo día)
1. Añadir la conversación a la ficha: qué aprendimos, el compromiso, el siguiente paso y **qué cambia**.
2. Si cambia algo del producto, cambiarlo esa semana:
   - una excepción nueva o mal planteada va a `knowledge/sectores/seguros/dominio.json` y a `excepciones.md`;
   - un caso de prueba equivocado va a `casos.json`, y se corrige su resultado esperado;
   - un plazo o una norma va a `normas.md`, con su fuente.
3. Si contradice una decisión, abrir una propuesta en `DECISIONS.md`.
4. Una línea en el informe de la mañana: qué hipótesis se ha confirmado, cuál se ha caído y cuál sigue abierta.

## Señales
| Fuerte (avanza) | Débil (no cuenta) |
|---|---|
| Nos cuenta un caso concreto con fechas y tiempos | «Sí, eso estaría genial» |
| Nos deja ver su pantalla o una mañana de trabajo | «Mándame información» |
| Nos presenta a quien decide | Halagos sobre la idea |
| Saca el problema antes de que lo nombremos | Respuestas sobre lo que haría en el futuro |

## Registro (copiar en la ficha)
```
fecha: AAAA-MM-DD · tipo: validacion_semanal · con: [roles]
pregunta de la semana:
aprendido: [hechos, cada uno con su base: medido o declarado]
caso inventado contrastado: S__ · coincide: sí/no · por qué
compromiso:
siguiente paso:
cambia: [archivos o decisiones]
```
