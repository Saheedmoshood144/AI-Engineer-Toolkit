from pathlib import Path
import joblib

from src.logger import get_logger


logger = get_logger(__name__)


class ModelPersistence:
    """
    Handles saving and loading machine learning models.
    """

    def save(
        self,
        model,
        file_path: str
    ) -> bool:
        """
        Save trained model to disk.

        Args:
            model: Trained machine learning model.
            file_path: Location to save model.

        Returns:
            True if successful, otherwise False.
        """

        try:
            path = Path(file_path)

            path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            joblib.dump(
                model,
                path
            )

            logger.info(
                f"Model saved successfully: {path}"
            )

            return True

        except Exception as error:
            logger.error(
                f"Model saving failed: {error}"
            )

            return False


    def load(
        self,
        file_path: str
    ):
        """
        Load trained model from disk.

        Args:
            file_path: Model location.

        Returns:
            Loaded model.
        """

        try:
            model = joblib.load(
                file_path
            )

            logger.info(
                "Model loaded successfully."
            )

            return model

        except Exception as error:
            logger.error(
                f"Model loading failed: {error}"
            )

            return None