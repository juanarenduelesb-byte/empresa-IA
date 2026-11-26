---
tipo: "paquete-sectorial"
id: "seguros-glosario"
departamento: "sectores"
estado: "draft"
tags:
  - "sector/seguros"
  - "glosario"
---
# Glosario de siniestros

**Estado:** draft. Definiciones de trabajo en lenguaje llano, con la norma de la que salen. Las que no tienen norma son uso habitual del sector y se marcan como *uso del sector (por validar)*. Los identificadores están también en [dominio.json](dominio.json) (`terminos`).

## Personas y papeles
- **Tomador** (`tomador`): quien contrata la póliza con la aseguradora y paga la prima ([LCS-50-1980](../../fuentes/registro.md#lcs-50-1980)).
- **Asegurado** (`asegurado`): la persona cuyo interés o persona cubre el seguro. Puede coincidir con el tomador ([LCS-50-1980](../../fuentes/registro.md#lcs-50-1980)).
- **Beneficiario** (`beneficiario`): quien cobra la indemnización o la prestación ([LCS-50-1980](../../fuentes/registro.md#lcs-50-1980)).
- **Perjudicado o tercero** (`perjudicado`): quien sufre un daño causado por el asegurado. En responsabilidad civil puede reclamar directamente a la aseguradora: es la **acción directa** (`accion-directa`) ([LCS-50-1980](../../fuentes/registro.md#lcs-50-1980), art. 76).
- **Corredor de seguros** (`corredor`): mediador que asesora de forma independiente, con un análisis objetivo, y que asiste al cliente en caso de siniestro ([RDL-3-2020](../../fuentes/registro.md#rdl-3-2020), art. 155).
- **Agente de seguros** (`agente`): mediador vinculado por contrato de agencia con una o varias aseguradoras; no es independiente ([RDL-3-2020](../../fuentes/registro.md#rdl-3-2020), art. 135).
- **Responsable del tratamiento** (`responsable-del-tratamiento`): quien decide para qué y cómo se tratan los datos. La AEPD considera responsable al corredor ([AEPD-CORREDOR-2018](../../fuentes/registro.md#aepd-corredor-2018)).

## El siniestro y su tramitación
- **Siniestro** (`siniestro`): el hecho cubierto por la póliza cuyas consecuencias reclama el asegurado ([LCS-50-1980](../../fuentes/registro.md#lcs-50-1980)).
- **Comunicación o declaración del siniestro** (`comunicacion-del-siniestro`): el aviso a la aseguradora, en 7 días como máximo desde que se conoce salvo plazo mayor en la póliza ([LCS-50-1980](../../fuentes/registro.md#lcs-50-1980), art. 16). Si la hace el corredor en nombre del tomador, vale igual (art. 21).
- **Parte** (`parte`): el documento o formulario con que se declara el siniestro a la aseguradora, a menudo en su portal. *Uso del sector (por validar).*
- **Expediente**: el registro del siniestro en el programa de la correduría; equivale a la anotación en el **libro-registro de siniestros** (`libro-registro-de-siniestros`), que se hace en cuanto el corredor conoce el siniestro ([RD-287-2021](../../fuentes/registro.md#rd-287-2021), art. 15 c).
- **Tramitador**: la persona de la correduría que abre y sigue los siniestros. *Uso del sector (por validar).*
- **Peritación** (`peritacion`): la valoración del daño por un perito; si las partes no se ponen de acuerdo, cada una nombra el suyo y, si hace falta, un tercero ([LCS-50-1980](../../fuentes/registro.md#lcs-50-1980), art. 38).
- **Salvamento** (`salvamento`): lo que se gasta para aminorar las consecuencias del siniestro; lo paga la aseguradora hasta la suma asegurada (art. 17).
- **Importe mínimo** (`importe-minimo`): lo que la aseguradora sabe que debe como mínimo y paga en 40 días desde la declaración (art. 18).
- **Interés de demora** (`interes-de-demora`): el recargo si la aseguradora no paga a tiempo: interés legal más un 50 %, y desde los 2 años al menos el 20 % (art. 20).
- **Subrogación** (`subrogacion`): tras pagar, la aseguradora reclama al responsable en lugar del asegurado (art. 43).
- **Prescripción** (`prescripcion`): el plazo tras el que ya no se puede reclamar: 2 años en daños y 5 en personas (art. 23).
- **Franquicia** (`franquicia`): la parte del daño que paga el asegurado. En riesgos extraordinarios es el 7 % de los daños en bienes, con excepciones ([CCS-FAQ](../../fuentes/registro.md#ccs-faq)).

## Automóviles
- **Oferta motivada** (`oferta-motivada`): la propuesta de indemnización que la aseguradora presenta en 3 meses desde la reclamación del perjudicado; si no la presenta, da una respuesta motivada ([RDLEG-8-2004](../../fuentes/registro.md#rdleg-8-2004), art. 7).
- **Baremo** (`baremo`): el sistema legal de valoración de los daños a las personas en accidentes de circulación, con cuantías que se actualizan cada año ([RDLEG-8-2004](../../fuentes/registro.md#rdleg-8-2004), [BAREMO-2026](../../fuentes/registro.md#baremo-2026)).
- **Declaración amistosa de accidente** (`declaracion-amistosa`): el formulario que firman los dos conductores; con él se fija la responsabilidad en el convenio entre aseguradoras ([UNESPA-CONVENIO-2026](../../fuentes/registro.md#unespa-convenio-2026), art. 6).
- **Convenio de indemnización directa** (`convenio-indemnizacion-directa`): el acuerdo entre aseguradoras por el que cada una paga a su cliente los daños materiales de una colisión entre dos vehículos y luego compensa con la otra. Refunde los antiguos CIDE y ASCIDE ([UNESPA-CONVENIO-2026](../../fuentes/registro.md#unespa-convenio-2026)).
- **CICOS** (`cicos`): la plataforma informática de compensación de siniestros entre aseguradoras ([CNMC-CIDE-2014](../../fuentes/registro.md#cnmc-cide-2014)).
- **TIREA** (`tirea`): la sociedad del sector que gestiona CICOS y el SDM ([UNESPA-CONVENIO-2026](../../fuentes/registro.md#unespa-convenio-2026)).
- **SDM** (`sdm`): el sistema de daños materiales para lo que no cubre el convenio de indemnización directa ([UNESPA-SDM](../../fuentes/registro.md#unespa-sdm)).

## Consorcio
- **Riesgos extraordinarios** (`riesgos-extraordinarios`): fenómenos de la naturaleza graves, terrorismo y alteraciones del orden, y actuaciones de las Fuerzas Armadas o de Seguridad en tiempo de paz ([RD-300-2004](../../fuentes/registro.md#rd-300-2004), art. 1.1).
- **Recargo del Consorcio** (`recargo-ccs`): la cantidad que se paga con la prima de ciertas pólizas y que da derecho a la cobertura del CCS ([RDLEG-7-2004-CCS](../../fuentes/registro.md#rdleg-7-2004-ccs), art. 8).
- **Carencia** (`carencia`): el tiempo tras contratar en el que aún no hay cobertura; en riesgos extraordinarios de la naturaleza, 7 días ([RD-300-2004](../../fuentes/registro.md#rd-300-2004), art. 8.1).

## Clientes y reclamaciones
- **Servicio de atención al cliente** (`servicio-de-atencion-al-cliente`): el departamento que resuelve quejas y reclamaciones; en corredurías, en un mes ([LEY-10-2025](../../fuentes/registro.md#ley-10-2025), disposición final segunda).
- **Defensor del cliente** (`defensor-del-cliente`): experto o entidad independiente que puede asumir las reclamaciones; su decisión favorable al cliente vincula a la correduría ([RDL-3-2020](../../fuentes/registro.md#rdl-3-2020), art. 167).
- **Servicio de Reclamaciones de la DGSFP** (`servicio-de-reclamaciones-dgsfp`): la segunda instancia, tras reclamar por escrito a la entidad; resuelve en 90 días naturales ([LEY-10-2025](../../fuentes/registro.md#ley-10-2025)).
- **Atención personalizada** (`atencion-personalizada`): la atención por una persona que se identifica, que el cliente puede pedir en cualquier momento, también a un bot ([LEY-10-2025](../../fuentes/registro.md#ley-10-2025), art. 8).
- **Cuentas de clientes** (`cuentas-de-clientes`): las cuentas separadas por las que el mediador mueve el dinero de sus clientes ([RDL-3-2020](../../fuentes/registro.md#rdl-3-2020), art. 136).

## Datos
- **Datos de salud** (`datos-de-salud`): categoría especial del RGPD; aparecen en cuanto hay daños personales ([RGPD-2016-679](../../fuentes/registro.md#rgpd-2016-679), art. 9; ver [normas.md](normas.md)).
