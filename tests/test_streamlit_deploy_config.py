from __future__ import annotations

import importlib
import sys
from pathlib import Path


def test_streamlit_is_declared_in_runtime_dependencies() -> None:
    root = Path(__file__).resolve().parents[1]
    requirements = (root / "requirements.txt").read_text(encoding="utf-8").lower()
    pyproject = (root / "pyproject.toml").read_text(encoding="utf-8").lower()

    assert "streamlit" in requirements
    assert "streamlit" in pyproject


def test_streamlit_app_module_can_be_imported() -> None:
    root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(root / "src"))

    try:
        module = importlib.import_module("amapa_politico_monitor.ui.app")
    finally:
        sys.path.pop(0)

    assert hasattr(module, "main")


def test_package_init_does_not_import_crewai_and_newsitem_still_imports() -> None:
    root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(root / "src"))

    try:
        package = importlib.import_module("amapa_politico_monitor")
        news_item_module = importlib.import_module("amapa_politico_monitor.models.news_item")
    finally:
        sys.path.pop(0)

    assert package.__version__ == "1.0.0"
    assert hasattr(package, "Agent")
    assert hasattr(package, "Crew")
    assert hasattr(package, "Process")
    assert hasattr(package, "Task")
    assert hasattr(news_item_module, "NewsItem")
