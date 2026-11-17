# Ciclo completo de un encargo (P01 → P11)

Así se encadenan los procesos. Los estados son los de la Guía v1.4 §4. Las transiciones que la Guía no define están marcadas como *añadidas* en [`definitions/encargo.json`](../definitions/encargo.json).

```mermaid
flowchart TD
  P01["P01 Alta y recepción"] --> P02{"P02 Clasificación<br>cinco decisiones"}
  P02 -- PREGUNTAR --> P03["P03 Aclaraciones"] --> P02
  P02 -- RECHAZAR --> R(["RECHAZADO"])
  P02 -- ESCALAR o DERIVAR --> ESC[["Persona identificada decide"]]
  ESC --> P02
  P02 -- CONTINUAR --> P04["P04 Recuperar conocimiento y precedentes"]
  P04 --> P05["P05 Plan con criterios"]
  P05 --> P06["P06 Asignación"]
  P06 --> P08["P08 Ejecución"]
  P08 -- error --> P22["P22 Errores y reintentos"]
  P22 -- transitorio --> P08
  P22 -- agotado o no reintentable --> B(["BLOQUEADO o ESCALADO"])
  P08 --> P09{"P09 QA"}
  P09 -- no cumple --> P08
  P09 -- riesgo medio o alto --> P10[["P10 Aprobación humana"]]
  P09 -- riesgo bajo y conforme --> P11["P11 Entrega y cierre"]
  P10 -- aprobada --> P11
  P10 -- retrabajo --> P08
  P10 -- rechazada --> R
  P11 --> P13["P13 Precedente y wiki"]
  P11 --> P18["P18 Evaluación y mejora"]
```

Controles transversales en todo el ciclo:
- **P14:** aislamiento.
- **P15:** observabilidad.
- **P19:** política.
- **P20:** entradas no confiables.
- **P21:** herramientas.
- **P29:** costes.
