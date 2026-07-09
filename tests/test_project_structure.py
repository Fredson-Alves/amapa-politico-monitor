def test_import_settings():
    from amapa_politico_monitor import settings

    assert settings.PROJECT_NAME == "amapa-politico-monitor"


def test_import_logger():
    from amapa_politico_monitor.logger import app_logger

    assert app_logger is not None


def test_import_agents_factory():
    from amapa_politico_monitor.agents.political_agents import PoliticalAgents

    assert PoliticalAgents is not None


def test_import_tasks_factory():
    from amapa_politico_monitor.tasks.political_tasks import PoliticalTasks

    assert PoliticalTasks is not None


def test_import_crew_factory():
    from amapa_politico_monitor.crews.political_monitor_crew import PoliticalMonitorCrew

    assert PoliticalMonitorCrew is not None