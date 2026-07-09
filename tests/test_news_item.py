from datetime import datetime

from amapa_politico_monitor.models.news_item import NewsItem


def test_news_item_can_be_created():
    item = NewsItem(
        id="1",
        titulo="Título",
        resumo="Resumo",
        fonte="Fonte",
        url="https://exemplo.com",
        data_publicacao="2024-01-01",
    )

    assert item.id == "1"
    assert item.titulo == "Título"
    assert item.coletado_em is not None


def test_news_item_defaults_are_initialized():
    item = NewsItem(
        id="1",
        titulo="Título",
        resumo="Resumo",
        fonte="Fonte",
        url="https://exemplo.com",
        data_publicacao=None,
    )

    assert item.municipios == []
    assert item.orgaos == []
    assert item.pessoas == []
    assert item.palavras_chave == []
    assert item.categoria is None
    assert item.impacto_institucional is None


def test_news_item_to_dict_serializes_content():
    item = NewsItem(
        id="1",
        titulo="Título",
        resumo="Resumo",
        fonte="Fonte",
        url="https://exemplo.com",
        data_publicacao="2024-01-01",
        municipios=["Macapá"],
        orgaos=["MP-AP"],
        pessoas=["Nome"],
        palavras_chave=["política"],
        categoria="Governo",
        impacto_institucional="Alta",
    )

    data = item.to_dict()

    assert data["titulo"] == "Título"
    assert data["municipios"] == ["Macapá"]
    assert isinstance(data["coletado_em"], str) and data["coletado_em"]


def test_news_item_to_json_returns_string():
    item = NewsItem(
        id="1",
        titulo="Título",
        resumo="Resumo",
        fonte="Fonte",
        url="https://exemplo.com",
        data_publicacao="2024-01-01",
    )

    payload = item.to_json()

    assert isinstance(payload, str)
    assert '"titulo": "Título"' in payload


def test_news_item_from_dict_restores_values():
    item = NewsItem.from_dict(
        {
            "id": "2",
            "titulo": "Outra notícia",
            "resumo": "Resumo",
            "fonte": "Fonte",
            "url": "https://exemplo.com",
            "data_publicacao": "2024-01-02",
            "municipios": ["Santana"],
            "orgaos": ["ALEAP"],
            "pessoas": ["Pessoa"],
            "palavras_chave": ["eleição"],
            "categoria": "Eleição",
            "impacto_institucional": "Médio",
        }
    )

    assert item.id == "2"
    assert item.categoria == "Eleição"
    assert isinstance(item.coletado_em, datetime)
