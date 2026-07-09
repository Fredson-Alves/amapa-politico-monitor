from amapa_politico_monitor import Crew, Process
from amapa_politico_monitor.agents.political_agents import PoliticalAgents
from amapa_politico_monitor.tasks.political_tasks import PoliticalTasks


class PoliticalMonitorCrew:
    """Orquestra a crew de monitoramento político do Amapá."""

    def __init__(self):
        agents_factory = PoliticalAgents()
        tasks_factory = PoliticalTasks()

        self.pesquisador = agents_factory.pesquisador_osint()
        self.verificador = agents_factory.verificador_fontes()
        self.classificador = agents_factory.classificador_politico()
        self.redator = agents_factory.redator_relatorio()

        self.pesquisar_task = tasks_factory.pesquisar_noticias(self.pesquisador)
        self.verificar_task = tasks_factory.verificar_fontes(self.verificador)
        self.classificar_task = tasks_factory.classificar_noticias(self.classificador)
        self.relatorio_task = tasks_factory.gerar_relatorio(self.redator)

    def build(self) -> Crew:
        return Crew(
            agents=[
                self.pesquisador,
                self.verificador,
                self.classificador,
                self.redator,
            ],
            tasks=[
                self.pesquisar_task,
                self.verificar_task,
                self.classificar_task,
                self.relatorio_task,
            ],
            process=Process.sequential,
            verbose=True,
        )