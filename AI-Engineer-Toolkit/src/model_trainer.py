from sklearn.linear_model import LogisticRegression
import pandas as pd

from src.logger import get_logger


logger = get_logger(__name__)


class ModelTrainer:
    """
    Handles model training and prediction.
    """

    def __init__(self) -> None:
        """
        Initialize the model trainer.
        """
        self.model = LogisticRegression()

    def train(
        self,
        X_train: pd.DataFrame,
        y_train: pd.Series
    ) -> LogisticRegression:
        """
        Train the machine learning model.

        Args:
            X_train: Training features.
            y_train: Training target.

        Returns:
            LogisticRegression: The trained model.
        """

        logger.info(
            "Starting model training."
        )

        self.model.fit(
            X_train,
            y_train
        )

        logger.info(
            "Model training completed."
        )

        return self.model

    def predict(
        self,
        X_test: pd.DataFrame
    ) -> pd.Series:
        """
        Generate predictions.

        Args:
            X_test: Testing features.

        Returns:
            Model predictions.
        """

        logger.info("Generating predictions.")

        predictions = self.model.predict(X_test)

        return predictions