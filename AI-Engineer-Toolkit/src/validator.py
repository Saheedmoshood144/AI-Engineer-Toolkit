import pandas as pd

from src.logger import get_logger


logger = get_logger(__name__)


class DatasetValidator:
    """
    Validates datasets before processing.
    """

    def __init__(self, data: pd.DataFrame) -> None:
        """
        Initialize validator.

        Args:
            data: Dataset to validate.
        """
        self.data = data

    def validate(self) -> bool:
        """
        Validate dataset.

        Returns:
            bool: True if dataset passes validation,
            otherwise False.
        """
        logger.info("Starting dataset validation.")

        if self.data is None:
            logger.error("No dataset provided.")
            return False

        if self.data.empty:
            logger.error("Dataset contains no rows.")
            return False

        logger.info("Dataset validation successful.")

        return True