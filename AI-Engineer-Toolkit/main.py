from src.logger import get_logger

logger = get_logger(__name__)

logger.info("Application started")
logger.warning("Configuration file not found")
logger.error("Unable to connect to database")

from src.dataset import Dataset

dataset = Dataset("employees.csv")

dataset.display_path()

dataset.load()

dataset.clean()

print(dataset.data)