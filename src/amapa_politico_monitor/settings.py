"""
settings.py

Centraliza todas as configurações da aplicação.

Projeto:
Amapá Político Monitor
"""

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - fallback para ambientes sem python-dotenv
    def load_dotenv(*args, **kwargs):
        return False

# Carrega o arquivo .env localizado na raiz do projeto
BASE_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = BASE_DIR / ".env"
load_dotenv(ENV_FILE)

# Diretório raiz do projeto
PROJECT_NAME = os.getenv("PROJECT_NAME", "amapa-politico-monitor")

OUTPUT_DIR = BASE_DIR / os.getenv("OUTPUT_DIR", "output")
LOG_DIR = BASE_DIR / os.getenv("LOG_DIR", "logs")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

REPORT_MD = OUTPUT_DIR / "relatorio-politico-amapa.md"
REPORT_JSON = OUTPUT_DIR / "relatorio-politico-amapa.json"
LOG_FILE = LOG_DIR / "execucao.log"

OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)