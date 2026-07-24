import logging


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger.

    Args:
        name: The name of the logger, typically __name__.

    Returns:
        A configured Logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Only add handlers if they haven't already been added
    if not logger.handlers:
        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.propagate = False

    return logger