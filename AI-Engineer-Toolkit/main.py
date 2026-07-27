import argparse

from src.config import load_config
from src.logger import get_logger
from src.pipeline import DataPipeline


logger = get_logger(__name__)


def main() -> dict | None:
    """
    Run the AI Engineer Toolkit pipeline from the command line.
    """

    parser = argparse.ArgumentParser(
        description="AI Engineer Toolkit ML Pipeline"
    )

    parser.add_argument(
        "--config",
        required=True,
        help="Path to configuration file"
    )

    args = parser.parse_args()

    logger.info(
        "Application started."
    )

    config = load_config(
        args.config
    )

    if config is None:
        logger.error(
            "Configuration loading failed."
        )
        return None

    pipeline = DataPipeline(
        config
    )

    metrics = pipeline.run()

    if metrics is None:
        logger.error(
            "Pipeline execution failed."
        )
        return None

    logger.info(
        f"Model evaluation metrics: {metrics}"
    )

    return metrics


if __name__ == "__main__":
    main()