from pathlib import Path


def test_required_directories_exist():
    root = Path(__file__).resolve().parents[1]

    assert (root / "src").exists()
    assert (root / "docs").exists()
    assert (root / "output").exists()
    assert (root / "logs").exists()


def test_required_files_exist():
    root = Path(__file__).resolve().parents[1]

    assert (root / "README.md").exists()
    assert (root / "pyproject.toml").exists()
    assert (root / ".env.example").exists()