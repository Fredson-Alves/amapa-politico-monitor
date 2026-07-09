from unittest.mock import Mock

import pytest

from amapa_politico_monitor.services.news_collection_service import NewsCollectionService


def test_news_collection_service_can_be_created():
    service = NewsCollectionService()

    assert service is not None
    assert hasattr(service, "search")


def test_news_collection_service_search_uses_runner():
    runner = Mock(return_value="resultado simulado")
    service = NewsCollectionService(search_runner=runner)

    result = service.search("Amapá")

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].titulo == "Coleta simulada"
    runner.assert_called_once_with("Amapá")


def test_news_collection_service_raises_for_empty_query():
    service = NewsCollectionService()

    with pytest.raises(ValueError):
        service.search("")


def test_news_collection_service_wraps_search_errors():
    runner = Mock(side_effect=RuntimeError("falha interna"))
    service = NewsCollectionService(search_runner=runner)

    with pytest.raises(RuntimeError, match="Falha ao executar a coleta de notícias"):
        service.search("Amapá")
