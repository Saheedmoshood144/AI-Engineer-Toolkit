# Read a CSV file and return it as a pandas DataFrame

from pathlib import Path
from typing import Optional
import logging
import pandas as pd

# Basic logging configuration
logging.basicConfig(level=logging.ERROR)

def read_csv(file_path: str | Path) -> pd.DataFrame | None:
    """
    Reads a CSV file and returns it as a pandas DataFrame.

    Parameters:
        file_path (str | Path): Path to the CSV file.

    Returns:
        Optional[pd.DataFrame]: The DataFrame if successful, otherwise None.
    """
    path = Path(file_path)

    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        logging.error("File not found: %s", path)
    except pd.errors.EmptyDataError:
        logging.error("The file is empty: %s", path)
    except pd.errors.ParserError:
        logger.error("Could not parse the CSV file: %s", path)
    except Exception as e:
        logger.exception("An unexpected error occurred while reading '%s': %s", path, e)

    return None

    # Write a CSV file from a pandas DataFrame

from pathlib import Path
import logging
import pandas as pd

# Basic logging configuration
from src.logger import get_logger

logger = get_logger(__name__)
def write_csv(dataframe: pd.DataFrame, file_path: str | Path) -> bool:
    """
    Writes a pandas DataFrame to a CSV file.

    If the parent directory does not exist, it is created automatically.

    Parameters:
        dataframe (pd.DataFrame): The DataFrame to save.
        file_path (str | Path): Destination path for the CSV file.

    Returns:
        bool: True if the file was written successfully, otherwise False.
    """
    path = Path(file_path)

    try:
        # Create parent directories if they don't exist
        path.parent.mkdir(parents=True, exist_ok=True)

        # Write the DataFrame to CSV
        dataframe.to_csv(path, index=False)

        return True

    except Exception as e:
        logging.exception("Failed to write CSV to '%s': %s", path, e)
        return False