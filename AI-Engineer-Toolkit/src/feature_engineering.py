import pandas as pd

from src.logger import get_logger


logger = get_logger(__name__)


class FeatureEngineer:
    """
    Performs feature engineering on datasets.
    """

    def __init__(self, data: pd.DataFrame) -> None:
        """
        Initialize the feature engineer.

        Args:
            data: Dataset to transform.
        """
        self.data = data

    def drop_columns(
        self,
        columns: list[str]
    ) -> pd.DataFrame:
        """
        Remove specified columns from the dataset.

        Columns that do not exist are ignored.

        Args:
            columns: List of column names to remove.

        Returns:
            pd.DataFrame: Transformed dataset.
        """

        logger.info("Starting column removal.")

        self.data = self.data.drop(
            columns=columns,
            errors="ignore"
        )

        logger.info(
            f"Removed columns: {columns}"
        )

        return self.data