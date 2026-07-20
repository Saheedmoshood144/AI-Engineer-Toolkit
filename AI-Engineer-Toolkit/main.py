from src.logger import get_logger

logger = get_logger(__name__)

logger.info("Application started")
logger.warning("Configuration file not found")
logger.error("Unable to connect to database")