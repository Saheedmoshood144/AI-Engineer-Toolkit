import os

from dotenv import load_dotenv

from src.logger import get_logger


load_dotenv()

logger = get_logger(__name__)


class Settings:
    """
    Application configuration settings.
    """

    def __init__(self) -> None:

        self.model_path = os.getenv(
            "MODEL_PATH",
            "models/model.pkl"
        )

        self.app_name = os.getenv(
            "APP_NAME",
            "AI Engineer Toolkit API"
        )

        logger.info(
            "Application settings loaded."
        )