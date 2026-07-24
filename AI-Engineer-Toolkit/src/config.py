from pathlib import Path
import json

from src.logger import get_logger


logger = get_logger(__name__)


def load_config(file_path: str | Path) -> dict | None:
    """
    Load a JSON configuration file.

    Args:
        file_path: Path to the JSON configuration file.

    Returns:
        The configuration dictionary if successful, otherwise None.
    """
    path = Path(file_path)

    try:
        with path.open("r", encoding="utf-8") as file:
            config = json.load(file)

        logger.info("Configuration loaded successfully from '%s'.", path)
        return config

    except FileNotFoundError:
        logger.error("Configuration file not found: '%s'.", path)
        return None

    except json.JSONDecodeError:
        logger.error("Invalid JSON format in configuration file: '%s'.", path)
        return None

    except Exception:
        logger.exception("Unexpected error loading configuration from '%s'.", path)
        return None