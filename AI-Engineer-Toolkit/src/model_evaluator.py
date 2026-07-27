from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

import pandas as pd

from src.logger import get_logger


logger = get_logger(__name__)


class ModelEvaluator:
    """
    Evaluates machine learning model performance.
    """

    def evaluate(
    self,
    y_true: pd.Series,
    y_pred: np.ndarray
) -> dict[str, float]:
        """
        Calculate evaluation metrics.

        Args:
            y_true: Actual target values.
            y_pred: Model predictions.

        Returns:
            Dictionary containing evaluation scores.
        """

        logger.info("Starting model evaluation.")

        metrics = {
            "accuracy": accuracy_score(
                y_true,
                y_pred
            ),
            "precision": precision_score(
                y_true,
                y_pred,
                zero_division=0
            ),
            "recall": recall_score(
                y_true,
                y_pred,
                zero_division=0
            ),
            "f1_score": f1_score(
                y_true,
                y_pred,
                zero_division=0
            )
        }

        logger.info("Model evaluation completed.")

        return metrics