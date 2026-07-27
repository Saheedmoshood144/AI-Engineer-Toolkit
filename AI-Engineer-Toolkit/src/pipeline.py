from src.dataset import Dataset
from src.validator import DatasetValidator
from src.feature_engineering import FeatureEngineer
from src.data_splitter import DataSplitter
from src.model_trainer import ModelTrainer
from src.model_evaluator import ModelEvaluator

from src.logger import get_logger


logger = get_logger(__name__)


class DataPipeline:
    """
    Handles the complete machine learning pipeline.
    """

    def __init__(self, config: dict) -> None:
        """
        Initialize the data pipeline.

        Args:
            config: Pipeline configuration dictionary.
        """

        self.config = config

        dataset_path = self.config.get("dataset_path")

        if not dataset_path:
            raise ValueError(
                "dataset_path is required in configuration."
            )

        self.dataset = Dataset(dataset_path)

        logger.info(
            "DataPipeline initialized."
        )

    def run(self) -> dict | None:
        """
        Execute the complete machine learning pipeline.

        Returns:
            Dictionary containing model evaluation metrics.
        """

        logger.info(
            "Starting machine learning pipeline."
        )

        # Load dataset
        self.dataset.load()

        if self.dataset.data is None:
            logger.error(
                "Dataset loading failed."
            )
            return None

        # Validate dataset
        validator = DatasetValidator(
            self.dataset.data
        )

        if not validator.validate():
            logger.error(
                "Dataset validation failed."
            )
            return None

        # Clean dataset
        self.dataset.clean()

        # Feature engineering
        engineer = FeatureEngineer(
            self.dataset.data
        )

        self.dataset.data = engineer.drop_columns([])

        logger.info(
            f"Columns before splitting: {list(self.dataset.data.columns)}"
        )

        # Split dataset
        target_column = self.config.get(
            "target_column"
        )

        if not target_column:
            logger.error(
                "Target column not provided."
            )
            return None

        splitter = DataSplitter(
            self.dataset.data,
            target_column
        )

        X_train, X_test, y_train, y_test = splitter.split()

        # Train model
        trainer = ModelTrainer()

        trainer.train(
            X_train,
            y_train
        )

        # Predict
        predictions = trainer.predict(
            X_test
        )

        # Evaluate
        evaluator = ModelEvaluator()

        metrics = evaluator.evaluate(
            y_test,
            predictions
        )

        logger.info(
            "Machine learning pipeline completed."
        )

        return metrics