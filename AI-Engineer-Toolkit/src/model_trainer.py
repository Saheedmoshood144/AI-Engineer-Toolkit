from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

from src.logger import get_logger


logger = get_logger(__name__)


class ModelTrainer:
    """
    Trains machine learning models.
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
    ) -> None:
        """
        Train the machine learning model.

        Args:
            X_train: Training features.
            y_train: Training target.
        """

        logger.info("Starting model training.")

        self.model.fit(
            X_train,
            y_train
        )

        logger.info("Model training completed.")

   

    def predict(
     self,
      X_test: pd.DataFrame
    ) -> np.ndarray:
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