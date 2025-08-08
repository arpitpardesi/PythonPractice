import logging

def setup_logging():
    """
    Set up the logging configuration.
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)
    return logger

def log_example():
    """
    Example function to demonstrate logging.
    """
    logger = setup_logging()

    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
if __name__ == "__main__":
    log_example()
    # The log messages will be written to 'app.log' and also printed to the console.
    # You can check the 'app.log' file for the logged messages.
