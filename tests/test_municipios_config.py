from amapa_politico_monitor.config.municipios import MUNICIPIOS_AMAPA


def test_municipios_amapa_exists():
    assert MUNICIPIOS_AMAPA is not None


def test_municipios_amapa_has_exactly_16_items():
    assert len(MUNICIPIOS_AMAPA) == 16


def test_municipios_amapa_has_no_duplicates():
    assert len(set(MUNICIPIOS_AMAPA)) == len(MUNICIPIOS_AMAPA)


def test_municipios_amapa_items_are_non_empty_strings():
    assert all(isinstance(item, str) and item.strip() for item in MUNICIPIOS_AMAPA)
