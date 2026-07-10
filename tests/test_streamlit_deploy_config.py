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
