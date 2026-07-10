"""Amapá Político Monitor."""

from __future__ import annotations

__version__ = "1.0.0"


class Agent:
    """Stub leve para compatibilidade sem CrewAI."""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Task:
    """Stub leve para compatibilidade sem CrewAI."""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Crew:
    """Stub leve para compatibilidade sem CrewAI."""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def kickoff(self):
        return None


class Process:
    """Stub leve para compatibilidade sem CrewAI."""

    sequential = "sequential"


__all__ = ["__version__", "Agent", "Task", "Crew", "Process"]
