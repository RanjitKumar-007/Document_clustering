import logging
import os
from config import Config
"""
Logging configuration module.
Responsibilities:
- Create log directory
- Configure logging format
- Write pipeline execution logs
- Track errors and document processing
"""
def setup_logger():
    """
    Configure application logger.
    Creates:
    - logs/ directory
    - run.log file
    Returns:
        logging.Logger:
            Configured logger instance
    """
    os.makedirs(
        "logs",
        exist_ok=True
    )
    logging.basicConfig(
        filename=Config.LOG_FILE,
        level=logging.INFO,
        format=(
            "%(asctime)s - "
            "%(levelname)s - "
            "%(message)s"
        )
    )
    return logging.getLogger()
