"""
main.py

Ponto de entrada do sistema Amapá Político Monitor.

Autor:
Fredson Alves

Descrição:
Inicializa a Crew responsável pelo monitoramento de notícias políticas
do Estado do Amapá.
"""

from amapa_politico_monitor.crew import PoliticalMonitorCrew
from amapa_politico_monitor.logger import app_logger

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - fallback para ambientes sem python-dotenv
    def load_dotenv(*args, **kwargs):
        return False

load_dotenv()


def main():
    app_logger.info("=" * 70)
    app_logger.info("AMAPÁ POLÍTICO MONITOR")
    app_logger.info("=" * 70)
    app_logger.info("Inicializando Crew...\n")

    try:
        crew = PoliticalMonitorCrew().build()

        resultado = crew.kickoff()

        app_logger.info("\nExecução finalizada com sucesso.\n")

        print("\n")
        print("=" * 70)
        print("RELATÓRIO GERADO")
        print("=" * 70)
        print(resultado)
        print("=" * 70)

    except Exception as exc:
        app_logger.exception(exc)
        raise


if __name__ == "__main__":
    main()