"""K1: la medida de fichas con fuente externa no cuenta las fuentes internas del registro."""

from varios.db.carga_conocimiento import medir


def test_las_fuentes_internas_no_cuentan_como_externas(tmp_path):
    k = tmp_path / "knowledge" / "x"
    k.mkdir(parents=True)
    relleno = "Texto suficiente para que la sección cuente como ficha de conocimiento."
    (k / "a.md").write_text(
        "# A\n\n## Interna\n" + relleno + " [INT-DEC](registro.md#int-dec)\n\n"
        "## Externa\n" + relleno + " [LCS-50-1980](registro.md#lcs-50-1980)\n\n"
        "## Sin cita\n" + relleno + "\n",
        encoding="utf-8",
    )
    m = medir(tmp_path)
    # «Sin cita» hereda las citas del documento (una interna y una externa), como en la carga.
    assert m["fichas"] == 3 and m["con_fuente_externa"] == 2


def test_el_paquete_de_seguros_esta_respaldado():
    assert medir(prefijo="knowledge/sectores/seguros/")["porcentaje"] >= 90
