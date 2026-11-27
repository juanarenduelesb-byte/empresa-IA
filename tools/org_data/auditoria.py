"""Auditoría de agentes y habilidades frente a los procesos (N2, M-040). Estado: propuesta (D-026).

Cada agente de agentes.py y cada habilidad de habilidades.py tiene aquí una entrada:
- veredicto «mantener»: procesos que lo necesitan (P01–P38 del catálogo o REF-SIN, el proceso de cliente de
  referencia) y la métrica que diría si lo hace bien.
- veredicto «fusionar»: con qué agente o habilidad se une («destino», que debe quedarse) y por qué.
- veredicto «retirar»: por qué no sirve hoy a ningún proceso y qué tendría que pasar para recuperarlo («reactivar»).
No se borra nada: es una propuesta para los socios. tests/test_auditoria_agentes.py falla si se añade un agente o una
habilidad sin entrada aquí, o si una entrada que se mantiene no tiene proceso o métrica.
El documento docs/28-auditoria-agentes.md se genera desde este archivo con tools/auditoria_gen.py.
"""

# Procesos válidos además de P01–P38 (tools/org_data/procesos.py).
PROCESOS_CLIENTE = {
    "REF-SIN": ("Apertura de siniestros en corredurías (proceso de cliente de referencia, D-011)",
                "processes/referencia-seguros-apertura-siniestros/README.md"),
}


def m(procesos, metrica, nota=""):
    return dict(veredicto="mantener", procesos=procesos, metrica=metrica, motivo=nota)


def f(destino, motivo):
    return dict(veredicto="fusionar", destino=destino, procesos=[], metrica="", motivo=motivo)


def r(motivo, reactivar):
    return dict(veredicto="retirar", procesos=[], metrica="", motivo=motivo, reactivar=reactivar)


AGENTES = {
    # --- Dirección
    "ceo": m(["P01", "P02", "P03", "P05", "P06", "P11"], "Acierto de decisión en el banco del Control A (25 encargos de processes/ceo-control-a/; umbral pendiente del 22/01/2027)",
             "Solo el CEO limitado que pide el proceso de referencia (D-006)."),
    "pmo": m(["P05", "P12", "P38"], "Semanas del plan con su «hecho cuando» cumplido y con evidencia en el repositorio",
             "Absorbe el registro de decisiones (P12)."),
    "dec": f("pmo", "Comparte con Plan y seguimiento la misma ficha de conocimiento (decisiones-seguimiento) y su único proceso (P12) lo puede llevar el PMO. Con dos socios a 10–15 h semanales, dos agentes para el mismo cuaderno duplican la coordinación."),
    "bib": m(["P04", "P07", "P11", "P13"], "Porcentaje de fichas de conocimiento con fuente externa (29,1 % el 26/11/2026 con la medida corregida en K1; `carga_conocimiento.medir()`) y respuestas con cita que existe"),
    # --- Comercial
    "comj": m(["P31", "P32"], "Oportunidades con decisión de seguir o no (go/no-go) registrada y motivo",
              "Absorbe Validación y Contenido."),
    "val": f("comj", "Las conversaciones de validación alimentan la cualificación (P31) y usan el mismo método que el descubrimiento (P32, The Mom Test). Juan decidió el 26/11 que Claude no haga por ahora la primera conversación (M-010): un agente propio no tiene trabajo hasta entonces."),
    "pros": m(["P31"], "Cuentas que pasan a cualificadas tras la primera conversación"),
    "prop": m(["P31", "P38"], "Propuestas que cumplen la rúbrica de C3 (src/varios/calidad/rubrica.py) a la primera, y tasa de aceptación"),
    "cont": f("comj", "Ningún proceso del catálogo produce contenido de web o LinkedIn, lo publican los socios y la web para clientes espera a la marca (M-002). La habilidad de posicionamiento se retira hasta entonces."),
    # --- Procesos
    "proj": m(["P32", "P33", "P34", "REF-SIN"], "Casos del proceso que pasan sin corrección humana y pasos eliminados frente al AS-IS"),
    "dat": m(["P23", "REF-SIN"], "Excepciones del catálogo EX-01–EX-15 con al menos un caso inventado y resultado esperado (15 de 15 el 26/11/2026)",
             "Separado de IA y evaluación a propósito: quien escribe el examen no es quien ajusta el modelo para aprobarlo."),
    "kpi": m(["P18", "P32", "P37"], "Métricas prometidas con ficha completa y línea base medida antes del cambio"),
    # --- Ingeniería
    "ingj": m(["P25", "P34"], "Cambios en main con CI en verde y que se pueden revertir"),
    "back": m(["P01", "P08", "P14", "P22", "P24", "P35"], "Pruebas de aislamiento entre clientes en verde contra PostgreSQL real"),
    "ia": m(["P02", "P09", "P16", "P23"], "Acierto por campo de la extracción frente a los «hechos» de los 20 casos, y tasa de invenciones"),
    "int": m(["P21", "P30", "P36"], "Acciones no autorizadas bloqueadas y reintentos sin duplicados"),
    "ops": m(["P15", "P17", "P26", "P28"], "Tiempo de recuperación ensayado con una restauración real"),
    "ux": m(["P03", "P10"], "Aprobaciones y preguntas que un socio resuelve sin ayuda y tiempo hasta decidir",
            "La interfaz de aprobación es donde se juega P10; si no hay cliente con pantallas propias, no crece."),
    # --- Calidad, seguridad y legal
    "calj": m(["P09", "P10", "P15", "P19"], "Entregables devueltos por Calidad y defectos que encuentran los socios después de Calidad"),
    "sec": m(["P14", "P17", "P20", "P26", "P28", "P30"], "Pruebas de aislamiento e inyección en verde (trampas del Control A: 5 de 5) y hallazgos abiertos"),
    "leg": m(["P07", "P19", "P24", "P27", "P28"], "Obligaciones mapeadas con fuente oficial y preguntas resueltas por el abogado",
             "Absorbe Cumplimiento normativo. Todo lo suyo es borrador para abogado."),
    "cump": f("leg", "Comparte la ficha de conocimiento «cumplimiento» con Legal y Calidad y sus procesos (P19, P24) ya los lleva Legal. Sin abogado ni cliente regulado, dos agentes legales producen dos borradores de lo mismo. Sus habilidades pasan a Legal."),
    # --- Administración
    "admj": r("Ningún proceso del catálogo cubre trámites de la empresa y la sociedad aún no existe (forma jurídica antes del 08/01/2027, D2). Lo que hace hoy (preguntas al gestor) ya lo hace Legal con «preguntas-profesional».",
              "Los socios eligen la forma jurídica y hay trámites recurrentes (altas, impuestos)."),
    "fin": f("cfo", "Comparte con el Director financiero el coste por caso y el presupuesto (P29); dos agentes de dinero sin ingresos ni gastos reales es duplicar."),
    "prov": m(["P27"], "Proveedores en uso con ficha completa: ubicación de datos, condiciones y salida"),
    "cfo": m(["P29", "P31"], "Coste por caso frente al presupuesto y margen por fase en cada propuesta",
             "Absorbe Costes. La previsión de tesorería espera a la primera factura."),
    "conta": r("No hay sociedad, ni facturas, ni cobros: ningún proceso del catálogo lo necesita antes del 15/02/2027.",
               "Se constituye la sociedad y se firma el primer diagnóstico con factura."),
    # --- Sectores
    "seg": m(["P02", "P32", "P33", "REF-SIN"], "Correcciones sectoriales de los socios por encargo (objetivo: bajan semana a semana)"),
    "sal": r("El único proceso de cliente es de seguros (D-011) y no hay ninguna oportunidad de sanidad en P31.",
             "Una oportunidad de sanidad privada pasa la cualificación (P31). La ficha de conocimiento se conserva."),
    "ase": r("No hay proceso ni oportunidad de asesorías o despachos; el estudio de prospectos de Álvaro aún no ha elegido nicho (12/02/2027).",
             "Una oportunidad del sector pasa P31 o los socios eligen el nicho. La ficha de conocimiento se conserva."),
    "fnz": r("Sin proceso ni oportunidad de financiero no bancario; DORA ya lo cubre Legal para aseguradoras.",
             "Una oportunidad del sector pasa P31. La ficha de conocimiento se conserva."),
    "ind": r("Sin proceso ni oportunidad de industria.",
             "Una oportunidad del sector pasa P31. La ficha de conocimiento se conserva."),
    "logi": r("Sin proceso ni oportunidad de logística.",
              "Una oportunidad del sector pasa P31. La ficha de conocimiento se conserva."),
    # --- Éxito de cliente
    "exito": m(["P37", "P38"], "Pilotos que cumplen la métrica firmada (pago 50/50) y retención en Operar",
               "Sin cliente hasta el 15/02/2027: diseña el plan de éxito, no lo ejecuta."),
}

HABILIDADES = {
    # transversales
    "marca-varios": m(["P11", "P31"], "Criterio de claridad de la rúbrica C3 en 4 o más en los entregables"),
    "hecho-hipotesis-propuesta": m(["P02", "P09", "P13"], "Cifras sin fuente ni etiqueta en entregables revisados (objetivo: 0; es bloqueante en la rúbrica C3)"),
    "citar-cerebro": m(["P04"], "Respuestas con al menos una cita a una ruta que existe",
                       "Hoy solo la tiene el Bibliotecario; la propuesta es que P04 la aplique a todos los encargos."),
    "acta-reunion": m(["P12", "P32"], "Siguientes pasos con responsable y fecha (100 %)"),
    "decision-registro": m(["P12", "P25"], "Entradas de DECISIONS.md con motivo, alternativas y estado", "Absorbe «adr»."),
    "contrato-de-tarea": m(["P01", "P02"], "Encargos con contrato de tarea completo: confirmado, inferido y desconocido"),
    "cinco-decisiones": m(["P02"], "Acierto de decisión en el banco del Control A"),
    "plan-con-criterio": m(["P05"], "Tareas del plan con criterio de aceptación comprobable"),
    "consultar-historico": m(["P04", "P05"], "Encargos parecidos a uno anterior en los que se cita el precedente"),
    "plan-semanal": m(["P05", "P38"], "Semanas con «hecho cuando» cumplido y con evidencia"),
    "raid": m(["P05", "P38"], "Riesgos con dueño y fecha de revisión, y cerrados a tiempo"),
    "analisis-opciones": m(["P12", "P33"], "Decisiones que se presentan con al menos dos alternativas y lo que cuesta cada una"),
    "ficha-conocimiento": m(["P13"], "Fichas con fuente, fecha y estado"),
    "contraste-fuentes": m(["P04", "P13"], "Afirmaciones críticas (legales, plazos, cifras) con dos fuentes («validated»)"),
    # comercial
    "cualificacion-oportunidad": m(["P31"], "Oportunidades con go/no-go y motivo"),
    "entrevista-descubrimiento": m(["P32"], "Conversaciones con al menos un hecho del pasado (no opiniones) por hipótesis"),
    "sintesis-entrevistas": m(["P32"], "Hipótesis validadas o descartadas con su evidencia"),
    "icp": m(["P31"], "Cuentas del ICP que pasan a cualificadas"),
    "investigacion-cuenta": m(["P31"], "Primeras conversaciones con la ficha de la cuenta preparada y con fuentes"),
    "propuesta-diagnostico": m(["P31", "P38"], "Propuestas que cumplen la rúbrica C3 a la primera"),
    "business-case": m(["P31", "P37"], "Casos de negocio con cada cifra marcada como medida, declarada o hipótesis"),
    "mensaje-posicionamiento": r("Solo la usaba Contenido y ningún proceso del catálogo la necesita; los textos de la web (docs/26) esperan a la marca.",
                                 "Los socios deciden la marca (M-002) y aprueban publicar la web."),
    # procesos
    "mapeo-as-is": m(["P32", "REF-SIN"], "Mapas AS-IS validados por quien hace el proceso, con tiempos activo y de espera"),
    "diseno-to-be": m(["P33", "REF-SIN"], "Diseños TO-BE aprobados por el cliente en la puerta G2 (diseño aceptado)"),
    "matriz-ia-regla-persona": m(["P33"], "Pasos con la decisión IA, regla o persona justificada; ninguna regla resuelta por IA"),
    "informe-as-is-to-be": m(["P32", "P33"], "Informes que cumplen la rúbrica C3 a la primera"),
    "casos-sinteticos": m(["P23", "REF-SIN"], "Reglas y excepciones con caso y resultado esperado"),
    "ficha-metrica": m(["P37"], "Métricas prometidas con ficha completa"),
    "linea-base": m(["P32", "P37"], "Métricas con línea base medida antes del cambio"),
    # ingeniería
    "spec-tecnica": m(["P08", "P25"], "Tareas de construcción que pasan la revisión sin rehacer"),
    "adr": f("decision-registro", "CLAUDE.md manda justificar cada tecnología nueva en DECISIONS.md: un formato aparte para las decisiones de arquitectura es un segundo registro de lo mismo."),
    "modelo-datos": m(["P14", "P24", "P34"], "Migraciones al día con los modelos (alembic check en CI) y RLS forzada en cada tabla con cliente"),
    "pruebas": m(["P08", "P23", "P25"], "CI en verde y regla nueva con su prueba"),
    "evaluacion-modelos": m(["P16", "P23"], "Cambios de modelo o instrucciones con evaluación antes y después"),
    "ficha-integracion": m(["P36"], "Conectores con ficha, permisos mínimos y prueba de revocación"),
    # calidad, seguridad y legal
    "criterio-aceptacion": m(["P05", "P09"], "Entregables con criterio de aceptación desde que se abren"),
    "revision-entregable": m(["P09"], "Defectos que encuentran los socios después de Calidad"),
    "modelo-amenazas": m(["P14", "P20", "P21"], "Amenazas con control y prueba"),
    "revision-riesgo-ia": m(["P19", "P24"], "Usos de IA sobre datos de personas con revisión antes de construir"),
    "mapa-obligaciones": m(["P19", "P33"], "Obligaciones con fuente oficial, control y evidencia", "Absorbe «matriz-cumplimiento»."),
    "preguntas-profesional": m(["P19", "P27"], "Preguntas al abogado o al gestor con respuesta y fecha"),
    # administración
    "coste-unitario": m(["P29"], "Coste por caso medido frente al presupuesto"),
    # sectores
    "claves-sector": m(["P02", "P32", "REF-SIN"], "Encargos de un sector con sus claves antes de empezar y correcciones sectoriales de los socios"),
    "glosario-sector": m(["P13", "P32"], "Términos del sector con definición y fuente (35 en seguros el 26/11/2026)"),
    "ficha-proveedor": m(["P27"], "Proveedores en uso con ficha completa"),
    "cierre-mensual": r("Solo la usa Contabilidad, que se propone retirar: no hay sociedad ni movimientos.", "Se constituye la sociedad."),
    "facturacion-cobro": r("Solo la usa Contabilidad; no hay facturas hasta el primer diagnóstico.", "Se firma el primer diagnóstico con factura."),
    "paquete-gestor": r("Solo la usa Contabilidad; no hay trimestres que cerrar.", "Se constituye la sociedad y empieza el primer trimestre con actividad."),
    "prevision-tesoreria": r("La hoja precio-y-caja.xlsx (D2) ya cubre la caja a 18 meses sin ingresos; una previsión semanal no aporta hasta que haya cobros.",
                             "Se firma el primer diagnóstico y entran o salen pagos cada semana."),
    "margen-proyecto": m(["P29", "P31"], "Propuestas con margen por fase calculado antes de enviarlas"),
    "financiacion-publica": r("Ningún proceso del catálogo la usa y todavía no hay sociedad con la que pedir una ayuda.",
                              "Los socios eligen la forma jurídica (antes del 08/01/2027)."),
    # plataforma y operaciones
    "integracion-continua": m(["P17", "P25"], "Duración de CI y fallos de CI arreglados antes de la siguiente subida"),
    "copias-restauracion": m(["P26"], "Restauraciones reales ensayadas y su tiempo"),
    "runbook-incidente": m(["P15", "P28"], "Incidentes con runbook seguido y lección registrada"),
    "observabilidad": m(["P15"], "Errores detectados por alerta antes que por un socio"),
    # diseño
    "flujo-pantallas": m(["P10", "P33"], "Tareas críticas con flujo dibujado antes de construir"),
    "prueba-usabilidad": m(["P10"], "Tareas completadas sin ayuda en la prueba"),
    "revision-accesibilidad": m(["P10", "P11"], "Errores de accesibilidad WCAG 2.2 AA abiertos al entregar"),
    # éxito de cliente
    "plan-exito-cliente": m(["P38"], "Clientes con plan de éxito firmado al empezar el diagnóstico o el piloto"),
    "revision-valor": m(["P37"], "Revisiones con la métrica firmada medida frente a la línea base", "Absorbe «salud-cuenta»."),
    "salud-cuenta": f("revision-valor", "Mide lo mismo que la revisión de valor con otra frecuencia (mensual frente a trimestral). Sin clientes, una sola habilidad con indicadores mensuales basta."),
    # cumplimiento (pasa a Legal)
    "inventario-ia": m(["P16", "P19"], "Usos de IA inventariados y clasificados por riesgo con fuente"),
    "registro-tratamientos": m(["P24"], "Tratamientos con finalidad, base y plazo de conservación"),
    "alfabetizacion-ia": m(["P19"], "Personas de Varios con la formación del art. 4 registrada"),
    "matriz-cumplimiento": f("mapa-obligaciones", "La matriz obligación → control → evidencia es el mapa de obligaciones con dos columnas más; mantener las dos crea dos listas que se desincronizan."),
}
