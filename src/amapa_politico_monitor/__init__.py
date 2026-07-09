"""Pacote principal do projeto Amapá Político Monitor."""

try:
    from crewai import Agent, Crew, Process, Task
except ImportError:  # pragma: no cover - fallback para ambientes sem CrewAI
    class Agent:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    class Task:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    class Crew:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

        def kickoff(self):
            return None

    class Process:
        sequential = "sequential"


__all__ = ["Agent", "Task", "Crew", "Process"]
