import argparse
import pandas as pd

from src.config import load_config
from src.logger import get_logger
from src.pipeline import DataPipeline


logger = get_logger(__name__)


def main() -> pd.DataFrame | None:
    """
    Run the AI Engineer Toolkit pipeline from the command line.

    Returns:
        pd.DataFrame | None: Processed dataset if successful,
        otherwise None.
    """

    parser = argparse.ArgumentParser(
        description="AI Engineer Toolkit Pipeline"
    )

    parser.add_argument(
        "--config",
        required=True,
        help="Path to configuration file"
    )

    args = parser.parse_args()

    logger.info("Application started.")

    config = load_config(args.config)

    if config is None:
        logger.error("Configuration loading failed.")
        return None

    pipeline = DataPipeline(config)

    result = pipeline.run()

    if result is None:
        logger.error("Pipeline execution failed.")
        return None

    logger.info("Pipeline completed successfully.")

    return result


if __name__ == "__main__":
    main()