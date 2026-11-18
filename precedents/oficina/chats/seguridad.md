<!-- Generado por tools/registro_oficina.py desde la oficina de agentes. No editar a mano. -->

# Conversaciones con Seguridad

**Seguridad** · 2026-11-17 21:18

**Reunión con IA y evaluación**

## Respuesta de Seguridad (borrador)

**Conclusión:** de acuerdo con las tres capas. Faltan amenazas fuera del texto de entrada, un umbral explícito y una prueba del contexto enviado al modelo.

**De acuerdo**
- Dato frente a instrucción, modelo que propone y puerta de herramientas que decide. Es la base correcta.
- Registrar cada llamada y repetir el examen ante cada cambio de modelo o instrucciones.
- Honestidad sobre lo que 50 casos permiten afirmar: informar de qué casos pasan, sin prometer un porcentaje general.

**No de acuerdo o matices**
- Una regla impuesta por el adaptador no basta como defensa. La inyección puede colarse igualmente, así que la protección real es que el modelo no pueda ejecutar nada ni ver datos de otro cliente. Hipótesis a validar, no hecho.
- Umbral propuesto (a confirmar entre los dos socios): cero fallos en los casos de aislamiento y de acciones prohibidas. En el resto, cada fallo se analiza y se corrige antes del control. [POR CONFIRMAR]
- El riesgo de L2 no se puede dejar solo como "abierto". Propongo que no se pase a L2 sin una prueba de aislamiento equivalente con datos de dos clientes ficticios.

**Propongo**
1. Un test automático en S3 que construya el contexto exacto enviado al modelo para el cliente A y falle si aparece cualquier identificador del cliente B.
2. Lista de amenazas priorizadas (entrega en S3): inyección en documentos, fuga entre clientes, secretos en registros y prompts, acciones prohibidas, abuso de la puerta de herramientas y salida que no valida.
3. Validación de casos adversos: Seguridad redacta, Ingeniería los ejecuta y Álvaro revisa el realismo desde el lado de la correduría. [POR CONFIRMAR]

**Seguridad** · 2026-11-17 21:18

**Reunión con IA y evaluación**

## Respuesta de Seguridad (borrador)

**Conclusión:** de acuerdo con las tres capas. Faltan amenazas fuera del texto de entrada, un umbral explícito y una prueba del contexto enviado al modelo.

**De acuerdo**
- Dato frente a instrucción, modelo que propone y puerta de herramientas que decide. Es la base correcta.
- Registrar cada llamada y repetir el examen ante cada cambio de modelo o instrucciones.
- Honestidad sobre lo que 50 casos permiten afirmar: informar de qué casos pasan, sin prometer un porcentaje general.

**No de acuerdo o matices**
- Una regla impuesta por el adaptador no basta como defensa. La inyección puede colarse igualmente, así que la protección real es que el modelo no pueda ejecutar nada ni ver datos de otro cliente. Hipótesis a validar, no hecho.
- Umbral propuesto (a confirmar entre los dos socios): cero fallos en los casos de aislamiento y de acciones prohibidas. En el resto, cada fallo se analiza y se corrige antes del control. [POR CONFIRMAR]
- El riesgo de L2 no se puede dejar solo como "abierto". Propongo que no se pase a L2 sin una prueba de aislamiento equivalente con datos de dos clientes ficticios.

**Propongo**
1. Un test automático en S3 que construya el contexto exacto enviado al modelo para el cliente A y falle si aparece cualquier identificador del cliente B.
2. Lista de amenazas priorizadas (entrega en S3): inyección en documentos, fuga entre clientes, secretos en registros y prompts, acciones prohibidas, abuso de la puerta de herramientas y salida que no valida.
3. Validación de casos adversos: Seguridad redacta, Ingeniería los ejecuta y Álvaro revisa el realismo desde el lado de la correduría. [POR CONFIRMAR]
