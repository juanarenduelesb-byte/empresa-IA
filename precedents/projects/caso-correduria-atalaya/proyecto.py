#!/usr/bin/env python3
"""Proyecto de práctica «Atalaya»: informe y plan para cargarlo en la oficina de agentes.

Genera proyecto.json y oficina/casos/atalaya.json (proyecto + documentos + plan) en el formato de la base de datos de la oficina.
Todo es ficticio (D-011). Uso: python3 precedents/projects/caso-correduria-atalaya/proyecto.py
"""
import json
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
PID = "atalaya-2026"
F = "Todo el caso es ficticio: no uses ni busques datos reales de ninguna correduría."

P = {
    "id": PID, "name": "Diagnóstico de apertura de siniestros · Atalaya (ficticia)",
    "client": "Atalaya Correduría de Seguros (ficticia)", "sector": "seg", "type": "Diagnóstico",
    "deadline": "2026-12-11", "risk": "medio", "status": "abierto",
    "objective": "Saber con datos dónde se va el tiempo al abrir un siniestro en una correduría mediana, qué parte puede hacer la IA con control y cuál no, y proponer un piloto medible con pago 50/50.",
    "context": "Caso de práctica con un cliente ficticio para ensayar el proceso de referencia (D-011). La correduría abre unos 320 siniestros al mes (dato ficticio) por teléfono, correo, WhatsApp, portal y comerciales; alta manual en seis portales de aseguradoras; el 30 % de partes se rehace según una impresión interna sin medir.",
    "scope": "Apertura de siniestros de autos, hogar, comercio, flotas y responsabilidad civil: recepción, identificación, comprobación de póliza y plazo, petición de documentación, alta en el portal, registro y aviso al cliente.",
    "out": "Tramitación posterior, peritaciones, pagos, decisiones de cobertura o rehúse, siniestros con lesionados y pólizas de salud (fuera del piloto por decisión de la dirección).",
    "people": "Director general (paga), directora de siniestros (dueña del proceso), responsable de cumplimiento (datos y DGSFP), responsable de sistemas externo (4 h/mes).",
    "constraints": "Ningún dato real. Nada sale hacia clientes o aseguradoras sin aprobación humana. No se cambia el programa de gestión. Cumplimiento revisa RGPD y Reglamento de IA antes del piloto; un abogado revisa el contrato. Precio: por decidir por los socios.",
    "success": "Comité de dirección (ficticio) con diagnóstico, caso de negocio y propuesta de piloto que puede decidir; AS-IS y TO-BE validados; examen de 20 casos + 5 trampas listo para el control A del plan.",
    "expect": ["pptx", "xlsx", "docx", "proceso"],
    "expectTxt": "Presentación de 10–12 diapositivas para el comité, Excel de línea base y caso de negocio, informe de diagnóstico en Word, diagramas AS-IS y TO-BE, casos de prueba.",
    "created": "2026-11-17T22:00:00.000Z", "updated": "2026-11-17T22:00:00.000Z",
}

FASES = [
    ("1 · Preparar", "Entender el sector, los límites legales y qué preguntar."),
    ("2 · Diagnosticar", "Proceso actual, línea base y examen con casos inventados."),
    ("3 · Diseñar", "Proceso nuevo, seguridad, especificación y coste por caso."),
    ("4 · Proponer", "Propuesta de piloto, plan y presentación al comité."),
]


def e(fase, agente, formato, titulo, texto):
    return {"titulo": titulo, "agente": agente, "formato": formato, "fase": FASES[fase][0], "encargo": f"{texto}\n\n{F}"}


ENCARGOS = [
    e(0, "seg", "docx", "Claves del sector para abrir siniestros en una correduría",
      "Proyecto Atalaya (correduría ficticia). Prepara las claves del sector para el resto del equipo: vocabulario del tramitador (parte amistoso, convenios entre aseguradoras, riesgo extraordinario, tomador, asegurado, perjudicado…), qué dice la norma sobre el plazo de comunicación y el papel del mediador (cita el cerebro: processes/referencia-seguros-apertura-siniestros y knowledge/sectores), práctica habitual frente a norma, excepciones frecuentes y lo que la IA no debe decidir nunca. Incluye un glosario en tabla."),
    e(0, "leg", "docx", "Mapa de obligaciones y riesgo de IA del proceso",
      "Proyecto Atalaya (ficticio). Haz el mapa de obligaciones del proceso de apertura de siniestros con IA: RGPD (bases jurídicas posibles, datos de terceros, categorías especiales y por qué quedan fuera), Reglamento de IA (si el uso encaja o no en alto riesgo, transparencia, supervisión humana), obligaciones del corredor que afecten al proceso y lo que pediría un cliente regulado a Varios como proveedor. Termina con 10 preguntas cerradas para el abogado. Aviso de que no es asesoría jurídica."),
    e(0, "val", "docx", "Guion de entrevistas con tramitadores y directora de siniestros",
      "Proyecto Atalaya (ficticio). Prepara dos guiones de 30 minutos (tramitadora y directora de siniestros) para medir lo que no se sabe: tiempo por paso, partes que se rehacen, datos que faltan, excepciones y quién decide. Preguntas abiertas sobre un caso reciente concreto, sin vender. Añade una plantilla de toma de notas y cómo cronometrar 20 aperturas reales en una semana (para cuando haya cliente real)."),
    e(1, "proj", "proceso", "Proceso actual (AS-IS) de apertura de siniestros",
      "Proyecto Atalaya (ficticio). Con las notas de la sesión de arranque y la muestra de siniestros del proyecto, dibuja el AS-IS por carriles (cliente, tramitador, tramitador senior, directora, cartera, aseguradora, programa de gestión, portal). Para cada paso: rol, sistema, entrada, salida, tiempo (dicho o estimado, marcado), problemas. Cataloga las excepciones con su ruta: lesionados, Consorcio, fraude, impago, varios implicados, instrucciones raras del cliente, duplicados."),
    e(1, "kpi", "xlsx", "Línea base y fichas de métricas",
      "Proyecto Atalaya (ficticio). Construye la hoja de línea base: volumen mensual por canal y ramo, tiempo activo por paso (rango dicho por el cliente), esperas, partes rehechos, coste de una hora de tramitador como supuesto marcado. Añade las fichas de las 5 métricas del piloto (tiempo activo por apertura, tiempo hasta el acuse al cliente, % de partes sin corrección, % que pasa a persona, coste por caso) con fórmula, fuente, exclusiones, línea base y objetivo propuesto. Distingue dato dicho, estimación y supuesto."),
    e(1, "dat", "xlsx", "Examen: 20 siniestros inventados + 5 trampas con resultado esperado",
      "Proyecto Atalaya (ficticio). Crea el examen del sistema: 20 siniestros inventados realistas (reparto por ramo y canal parecido al del cliente ficticio) y 5 trampas (instrucción escondida en el correo, fuera de plazo, póliza en impago, duplicado, petición de no comunicar a la aseguradora). Para cada caso: texto de entrada tal como llegaría, campos esperados (cliente, póliza, ramo, tipo, fecha de ocurrencia, aseguradora, datos que faltan), decisión correcta (abrir, pedir documentación, pasar a persona, Consorcio, rechazar instrucción) y qué regla prueba. Usa identificadores imposibles (POL-FIC-…)."),
    e(2, "proj", "proceso", "Proceso nuevo (TO-BE) con matriz IA · regla · persona",
      "Hazlo en equipo. Proyecto Atalaya (ficticio). A partir del AS-IS, la línea base y el examen ya entregados, diseña el TO-BE de la apertura: para cada paso, si lo hace una regla (código), la IA (extraer y redactar) o una persona (decidir y aprobar), con su motivo y control. Recepción multicanal en un buzón único, extracción estructurada con confianza, comprobación de póliza y plazo por reglas, petición de documentación redactada por IA y aprobada por persona, prellenado del parte y envío aprobado, acuse al cliente aprobado, rutas de excepción. Incluye qué pasa cuando la IA duda y cómo se mide."),
    e(2, "sec", "docx", "Modelo de amenazas del proceso nuevo",
      "Proyecto Atalaya (ficticio). Modelo de amenazas del TO-BE de apertura de siniestros: activos, fronteras de confianza, amenazas (inyección de instrucciones en correos y adjuntos, suplantación del cliente, fuga entre clientes de Varios, errores de la IA que llegan a la aseguradora, secretos de portales), controles y la prueba de cada control. Prioriza por impacto y di qué entra en el examen."),
    e(2, "ingj", "docx", "Especificación técnica del piloto",
      "Proyecto Atalaya (ficticio). Especificación técnica del piloto dentro del stack decidido (Python, FastAPI, Pydantic, PostgreSQL, Docker Compose, pytest): buzón de entrada simulado, extracción con esquema Pydantic y confianza, reglas de póliza y plazo con datos inventados, cola de revisión humana, puerta de herramientas con aprobación para cualquier envío, auditoría. Pasos pequeños con su test, qué no se toca y cómo encaja con las semanas S4 y S8 del plan."),
    e(2, "fin", "xlsx", "Coste por siniestro abierto",
      "Proyecto Atalaya (ficticio). Hoja de coste unitario del piloto: consumo de modelo por siniestro (supuestos de tokens marcados y precio con fuente y fecha o [POR CONFIRMAR]), infraestructura, revisión humana restante y soporte, en tres volúmenes (200, 320 y 600 siniestros al mes). Fórmulas visibles y supuestos en una pestaña aparte."),
    e(3, "prop", "docx", "Propuesta de piloto con pago 50/50",
      "Proyecto Atalaya (ficticio). Escribe la propuesta de piloto de 6 semanas para la directora y el director general: problema con sus palabras, alcance (siniestros sencillos de autos y hogar, sin lesionados ni salud), entregables, calendario, lo que necesitamos de ellos, métrica firmada con línea base, pago 50/50 ligado a la métrica, exclusiones y siguiente paso. Usa el caso de negocio y los costes ya entregados. Precio: [PRECIO POR DECIDIR]."),
    e(3, "pmo", "xlsx", "Plan del piloto y registro RAID",
      "Proyecto Atalaya (ficticio). Plan del piloto en 6 semanas con entregables, responsable (Varios o cliente), dependencias, fecha y criterio de aceptación; y registro RAID (riesgos, supuestos, incidencias, dependencias) con dueño. Incluye el control de paso al final de cada fase y lo que haría parar el piloto."),
    e(3, "comj", "pptx", "Presentación al comité de dirección",
      "Proyecto Atalaya (ficticio). Presentación de 10–12 diapositivas para el comité de dirección de la correduría ficticia: la conclusión primero, dónde se va el tiempo hoy (AS-IS y línea base), qué hará la IA y qué no (TO-BE), riesgos y cómo se controlan (legal y seguridad), caso de negocio con escenarios, propuesta de piloto con pago 50/50, plan y decisión que se pide. Usa solo lo ya entregado en el proyecto y marca como ficticio lo que lo sea."),
]


def docs():
    out = []
    d = os.path.join(AQUI, "documentos")
    for i, n in enumerate(sorted(os.listdir(d))):
        t = open(os.path.join(d, n), encoding="utf-8").read()
        out.append({"id": f"{PID}-doc{i + 1}", "project": PID, "name": n, "size": len(t.encode()), "type": "text/csv" if n.endswith(".csv") else "text/markdown",
                    "source": "subido", "url": "", "driveId": "", "asset": None, "chars": len(t), "nota": "Documento ficticio del caso de práctica", "text": t,
                    "created": P["created"]})
    return out


# Qué necesita cada encargo antes de empezar (índices de ENCARGOS). Lo que no depende de nada empieza a la vez.
DEPENDE = {0: [], 1: [], 2: [], 3: [0], 4: [3], 5: [0, 3], 6: [3, 4, 5], 7: [1, 6], 8: [6], 9: [4, 6], 10: [1, 4, 9], 11: [6, 8], 12: [3, 4, 6, 7, 10, 11]}
for _i, _e in enumerate(ENCARGOS):
    _e["depende"] = DEPENDE[_i]


def main():
    plan = {"resumen": "Diagnóstico de tres semanas en cuatro fases para la correduría ficticia Atalaya. Con «Lanzar todo el plan» se organizan solos: cada encargo empieza cuando terminan los que necesita, cada agente hace uno a la vez y trabajan varios en paralelo; cada encargo lee lo que ya han entregado los anteriores. Trabajan 12 agentes de los 7 departamentos, más el CEO, que asigna, y Calidad, que revisa cada entrega; el experto de seguros aporta las claves del sector a cada encargo.",
            "fases": [{"nombre": n, "objetivo": o} for n, o in FASES], "encargos": ENCARGOS,
            "preguntas": ["Precio del diagnóstico y del piloto (lo deciden los socios).", "¿Se confirma la apertura de siniestros en corredurías como proceso de referencia? (vence el 22/11/2026)"],
            "riesgos": ["Que las cifras ficticias se tomen como reales: todo lleva la marca de ficticio.", "Que la IA quiera decidir coberturas: queda fuera por diseño."],
            "created": P["created"]}
    proyecto = dict(P, plan=plan)
    txt = json.dumps({"project": proyecto, "docs": docs()}, ensure_ascii=False, indent=1) + "\n"
    raiz = os.path.dirname(os.path.dirname(os.path.dirname(AQUI)))
    for destino in (os.path.join(AQUI, "proyecto.json"), os.path.join(raiz, "oficina", "casos", "atalaya.json")):
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with open(destino, "w", encoding="utf-8") as f:
            f.write(txt)
    print(f"{len(ENCARGOS)} encargos, {len({x['agente'] for x in ENCARGOS})} agentes distintos, {len(docs())} documentos")


if __name__ == "__main__":
    main()
