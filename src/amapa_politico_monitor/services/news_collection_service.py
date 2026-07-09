"""Serviço responsável pela coleta de notícias públicas para o monitoramento político."""

from __future__ import annotations

from typing import Callable

from amapa_politico_monitor.logger import app_logger
from amapa_politico_monitor.models.news_item import NewsItem
from amapa_politico_monitor.tools.custom_tool import pesquisar_noticias_amapa


class NewsCollectionService:
    """Encapsula a lógica de coleta de notícias para os agentes."""

    def __init__(self, search_runner: Callable[[str], str] | None = None) -> None:
        self._search_runner = search_runner or pesquisar_noticias_amapa

    def search(self, query: str) -> list[NewsItem]:
        """Realiza a coleta de notícias para uma consulta informada.

        Args:
            query: Texto com o tema ou contexto da pesquisa.

        Returns:
            Lista de objetos NewsItem representando as notícias coletadas.

        Raises:
            RuntimeError: Se a coleta falhar internamente.
        """
        if not query or not str(query).strip():
            raise ValueError("A consulta de busca não pode ser vazia.")

        try:
            app_logger.info("Iniciando coleta de notícias para consulta: %s", query)
            resultado = self._search_runner(str(query).strip())
            app_logger.info("Coleta concluída com sucesso.")
            return [
                NewsItem(
                    id="coleta-simulada",
                    titulo="Coleta simulada",
                    resumo=resultado,
                    fonte="serviço",
                    url="",
                    data_publicacao=None,
                    municipios=[],
                    orgaos=[],
                    pessoas=[],
                    palavras_chave=[],
                    categoria=None,
                    impacto_institucional=None,
                )
            ]
        except Exception as exc:  # pragma: no cover - comportamento defensivo
            app_logger.exception("Falha na coleta de notícias: %s", exc)
            raise RuntimeError("Falha ao executar a coleta de notícias.") from exc
