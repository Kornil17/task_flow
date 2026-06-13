import logging.config
from pathlib import Path


def setup_logger() -> None:
    """Настройка логгера из файла logging.config."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    config_path = Path("logger") / "logging.conf"
    if not config_path.is_file():
        raise FileNotFoundError(f"Файл конфигурации логгера не найден: {config_path}")

    logging.config.fileConfig(
        str(config_path),
        disable_existing_loggers=False,
    )
