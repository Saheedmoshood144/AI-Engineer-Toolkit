from sklearn.model_selection import train_test_split
import pandas as pd

from src.logger import get_logger


logger = get_logger(__name__)


class DataSplitter:
    """
    Splits datasets into training and testing sets.
    """

    def __init__(
        self,
        data: pd.DataFrame,
        target_column: str
    ) -> None:
        """
        Initialize data splitter.

        Args:
            data: Dataset to split.
            target_column: Column to predict.
        """
        self.data = data
        self.target_column = target_column

    def split(
        self,
        test_size: float = 0.2,
        random_state: int = 42
    ) -> tuple:
        """
        Split data into training and testing sets.

        Args:
            test_size: Percentage of data used for testing.
            random_state: Ensures reproducible results.

        Returns:
            Tuple containing:
            X_train, X_test, y_train, y_test
        """

        logger.info("Starting dataset split.")

        X = self.data.drop(
            columns=[self.target_column]
        )

        y = self.data[self.target_column]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=random_state
        )

        logger.info("Dataset split completed.")

        return X_train, X_test, y_train, y_test