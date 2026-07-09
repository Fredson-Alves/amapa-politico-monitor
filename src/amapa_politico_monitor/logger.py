"""
logger.py

Configuração centralizada de logs.

Projeto:
Amapá Político Monitor
"""

from .settings import LOG_FILE

try:
    from loguru import logger
except ImportError:  # pragma: no cover - fallback para ambientes sem loguru
    import logging

    logger = logging.getLogger("amapa_politico_monitor")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(handler)

    logger.remove = lambda *args, **kwargs: None
    logger.add = lambda *args, **kwargs: None
else:
    logger.remove()

    logger.add(
        LOG_FILE,
        rotation="10 MB",
        retention="30 days",
        level="INFO",
        encoding="utf-8",
        enqueue=True,
    )

    logger.add(
        sink=lambda msg: print(msg, end=""),
        level="INFO",
    )

app_logger = logger