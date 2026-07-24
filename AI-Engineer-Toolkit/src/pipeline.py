from src.dataset import Dataset
from src.logger import get_logger

import pandas as pd


logger = get_logger(__name__)


class DataPipeline:
    """
    Coordinates dataset loading and preprocessing steps.
    """

    def __init__(self, config: dict) -> None:
        """
        Initialize the data pipeline.

        Args:
            config: Configuration dictionary.
        """
        self.config = config

        dataset_path = self.config.get("dataset_path")

        if not dataset_path:
            raise ValueError("dataset_path is required in configuration.")

        self.dataset = Dataset(dataset_path)

        logger.info("DataPipeline initialized.")

    def run(self) -> pd.DataFrame | None:
        """
        Execute the dataset processing workflow.

        Returns:
            Cleaned DataFrame if successful, otherwise None.
        """
        try:
            logger.info("Starting data pipeline.")

            self.dataset.load()

            if self.dataset.data is None:
                logger.warning("Dataset loading failed.")
                return None

            self.dataset.clean()

            logger.info("Data pipeline completed successfully.")

            return self.dataset.data

        except Exception:
            logger.exception("Pipeline execution failed.")
            return None