from amapa_politico_monitor import Task


class PoliticalTasks:
    """Fábrica de tarefas do Amapá Político Monitor."""

    def pesquisar_noticias(self, agent) -> Task:
        return Task(
            description=(
                "Pesquise notícias públicas e recentes sobre política no Estado do Amapá. "
                "Inclua governo estadual, ALEAP, MP-AP, TJAP, TRE-AP, TCE-AP, prefeituras, "
                "licitações, contratos, eleições, partidos políticos, nomeações, exonerações, "
                "operações policiais e temas de administração pública. "
                "Para cada notícia, informe título, resumo, data, fonte, URL, pessoas citadas "
                "e órgãos envolvidos."
            ),
            expected_output=(
                "Lista estruturada de notícias políticas do Amapá contendo título, resumo, "
                "data, fonte, URL, pessoas citadas e órgãos envolvidos."
            ),
            agent=agent,
        )

    def verificar_fontes(self, agent) -> Task:
        return Task(
            description=(
                "Analise as notícias coletadas. Remova duplicidades, priorize fontes oficiais "
                "e veículos reconhecidos, verifique se os links estão claros e identifique "
                "inconsistências evidentes entre publicações."
            ),
            expected_output=(
                "Lista única de notícias verificadas, sem duplicidades, com fontes organizadas "
                "e links preservados."
            ),
            agent=agent,
        )

    def classificar_noticias(self, agent) -> Task:
        return Task(
            description=(
                "Classifique cada notícia em categorias como Governo Estadual, Assembleia "
                "Legislativa, Ministério Público, Poder Judiciário, Tribunal de Contas, "
                "Tribunal Eleitoral, Prefeituras, Licitações, Contratos, Eleições, Partidos "
                "Políticos, Operações Policiais, Transparência, Segurança Pública, "
                "Administração Pública ou Outros. Identifique órgãos, agentes públicos, "
                "municípios, palavras-chave e impacto institucional descritivo."
            ),
            expected_output=(
                "Lista classificada das notícias contendo categoria, órgãos, agentes públicos, "
                "municípios, palavras-chave e impacto institucional descritivo."
            ),
            agent=agent,
        )

    def gerar_relatorio(self, agent) -> Task:
        return Task(
            description=(
                "Produza um relatório executivo em Markdown com cabeçalho, data da coleta, "
                "quantidade de notícias, fontes pesquisadas e uma seção para cada notícia. "
                "Cada item deve conter título, resumo, data, fonte, URL, categoria, órgãos "
                "envolvidos, pessoas citadas, municípios, palavras-chave e impacto institucional. "
                "O texto deve ser objetivo, técnico, institucional e imparcial."
            ),
            expected_output=(
                "Relatório em Markdown pronto para consulta institucional."
            ),
            output_file="output/relatorio-politico-amapa.md",
            agent=agent,
        )