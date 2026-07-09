"""
custom_tool.py

Ferramenta personalizada para pesquisa de notícias políticas
relacionadas ao Estado do Amapá.

Autor:
Fredson Alves

Projeto:
Amapá Político Monitor
"""

try:
    from crewai_tools import SerperDevTool, tool
except ImportError:  # pragma: no cover - fallback para ambientes sem crewai_tools
    class SerperDevTool:
        def run(self, query: str) -> str:
            return f"Simulação de busca para: {query}"

    def tool(name: str = ""):
        def decorator(func):
            return func

        return decorator


# Ferramenta nativa de busca do CrewAI
_search = SerperDevTool()


@tool("Pesquisa Política Amapá")
def pesquisar_noticias_amapa(assunto: str) -> str:
    """
    Pesquisa notícias políticas relacionadas ao Estado do Amapá.

    Args:
        assunto (str):
            Tema que será pesquisado.

    Returns:
        str:
            Resultado textual da pesquisa.
    """

    consulta = f"""
    {assunto}

    Estado do Amapá

    política OR governo OR assembleia legislativa OR prefeitura
    OR ministério público OR tribunal OR licitação OR contrato
    OR eleição OR corrupção OR operação policial
    """

    resultado = _search.run(consulta)

    return resultado