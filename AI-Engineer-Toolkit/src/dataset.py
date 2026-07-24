from src.file_manager import read_csv
from src.logger import get_logger

import pandas as pd


logger = get_logger(__name__)


class Dataset:
    """
    Represents a dataset loaded from a file.
    """

    def __init__(self, file_path: str) -> None:
        """
        Initialize a Dataset instance.

        Args:
            file_path: Path to the dataset file.
        """
        self.file_path = file_path
        self.data: pd.DataFrame | None = None

    def display_path(self) -> None:
        """
        Display the dataset file path.
        """
        print(self.file_path)

    def load(self) -> None:
        """
        Load the CSV file into a pandas DataFrame.
        """
        self.data = read_csv(self.file_path)

    def clean(self) -> None:
        """
        Remove rows containing missing values from the dataset.
        """

        if self.data is None:
            logger.warning("No dataset loaded.")
            return

        logger.info("Removing missing values from dataset.")

        self.data = self.data.dropna()

        logger.info("Dataset cleaning completed successfully.")