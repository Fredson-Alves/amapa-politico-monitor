"""Serviço de enriquecimento determinístico para notícias do projeto."""

from __future__ import annotations

from amapa_politico_monitor.config.municipios import MUNICIPIOS_AMAPA
from amapa_politico_monitor.config.orgaos import ORGAOS_AMAPA
from amapa_politico_monitor.config.palavras_chave import PALAVRAS_CHAVE_AMAPA
from amapa_politico_monitor.logger import app_logger
from amapa_politico_monitor.models.news_item import NewsItem


class NewsEnrichmentService:
    """Enriquece NewsItem com dados determinísticos baseados em regras locais."""

    def enrich(self, news_item: NewsItem) -> NewsItem:
        """Preenche municípios, órgãos e palavras-chave a partir do título e resumo.

        Args:
            news_item: Objeto NewsItem a ser enriquecido.

        Returns:
            O mesmo objeto NewsItem enriquecido.
        """
        if not isinstance(news_item, NewsItem):
            raise TypeError("news_item deve ser uma instância de NewsItem")

        texto = " ".join(
            parte for parte in [news_item.titulo, news_item.resumo] if parte
        ).lower()

        app_logger.info("Enriquecendo notícia: %s", news_item.titulo)

        news_item.municipios = self._match_values(texto, MUNICIPIOS_AMAPA)
        news_item.orgaos = self._match_values(texto, ORGAOS_AMAPA)
        news_item.palavras_chave = self._match_values(texto, PALAVRAS_CHAVE_AMAPA)

        return news_item

    def _match_values(self, text: str, values: list[str]) -> list[str]:
        """Retorna valores encontrados em um texto, sem duplicidades e sem case sensitivity."""
        matches: list[tuple[int, str]] = []

        for value in values:
            position = text.find(value.lower())
            if position >= 0:
                matches.append((position, value))

        matches.sort(key=lambda item: item[0])
        return [value for _, value in matches]
