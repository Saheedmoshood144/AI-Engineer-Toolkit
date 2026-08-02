import pandas as pd

from src.logger import get_logger
from src.model_persistence import ModelPersistence


logger = get_logger(__name__)


class Predictor:
    """
    Loads a saved model and makes predictions.
    """

    def __init__(
        self,
        model_path: str
    ) -> None:
        """
        Initialize predictor.

        Args:
            model_path: Path to saved model.
        """

        persistence = ModelPersistence()

        self.model = persistence.load(
            model_path
        )

    def predict(
        self,
        data: pd.DataFrame
    ):
        """
        Generate predictions.

        Args:
            data: Feature dataframe.

        Returns:
            Model predictions.
        """

        logger.info(
            "Generating predictions from saved model."
        )

        return self.model.predict(
            data
        )