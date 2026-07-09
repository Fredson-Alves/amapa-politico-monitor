from amapa_politico_monitor import Agent
from amapa_politico_monitor.services.news_collection_service import NewsCollectionService


class PoliticalAgents:
    """Fábrica de agentes do Amapá Político Monitor."""

    def pesquisador_osint(self) -> Agent:
        service = NewsCollectionService()

        return Agent(
            role="Pesquisador OSINT de Notícias Políticas do Amapá",
            goal=(
                "Localizar notícias públicas, recentes e relevantes sobre política, "
                "gestão pública, instituições e agentes públicos no Estado do Amapá."
            ),
            backstory=(
                "Você é um pesquisador especializado em fontes abertas, com foco em "
                "notícias públicas e informações institucionais. Trabalha de forma "
                "objetiva, organizada e sempre preserva a fonte original da informação."
            ),
            tools=[service.search],
            verbose=True,
            allow_delegation=False,
        )

    def verificador_fontes(self) -> Agent:
        return Agent(
            role="Verificador de Fontes e Consistência Informacional",
            goal=(
                "Verificar fontes, remover duplicidades, organizar links e priorizar "
                "informações públicas verificáveis."
            ),
            backstory=(
                "Você é criterioso, atento a inconsistências e especializado em separar "
                "informações úteis de ruídos informacionais."
            ),
            verbose=True,
            allow_delegation=False,
        )

    def classificador_politico(self) -> Agent:
        return Agent(
            role="Classificador Político-Institucional",
            goal=(
                "Classificar notícias conforme tema político, institucional, "
                "administrativo ou eleitoral."
            ),
            backstory=(
                "Você conhece a estrutura político-institucional do Estado do Amapá "
                "e organiza informações por categorias como governo, eleições, "
                "licitações, legislativo, judiciário, controle externo e segurança pública."
            ),
            verbose=True,
            allow_delegation=False,
        )

    def redator_relatorio(self) -> Agent:
        return Agent(
            role="Redator de Relatório Executivo Institucional",
            goal=(
                "Produzir relatório claro, objetivo, técnico e imparcial para consulta "
                "por servidores da Coordenadoria de Inteligência do MP-AP."
            ),
            backstory=(
                "Você transforma informações públicas coletadas em relatórios executivos "
                "objetivos, sem emitir juízo de valor, opinião pessoal ou conclusão investigativa."
            ),
            verbose=True,
            allow_delegation=False,
        )