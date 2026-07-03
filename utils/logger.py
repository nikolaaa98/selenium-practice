"""
Central logger for the framework.
Logs to both console and file (logs/test_run_<timestamp>.log).
"""
import logging
import os
from datetime import datetime

from config.config import Config

# Create logs directory if it does not exist
os.makedirs(Config.LOG_DIR, exist_ok=True)

# Timestamp for log file (one file per test run)
_TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILE_PATH = os.path.join(Config.LOG_DIR, f"test_run_{_TIMESTAMP}.log")

_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
_DATE_FMT = "%Y-%m-%d %H:%M:%S"


def get_logger(name: str = "selenium-practice") -> logging.Logger:
    """
    Returns a configured logger. If already configured, returns the existing instance.
    """
    logger = logging.getLogger(name)

    # Prevent adding handlers multiple times if get_logger is called repeatedly
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(_FORMAT, datefmt=_DATE_FMT)

    # Console handler - INFO and above
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # File handler - DEBUG and above (more detailed log in file)
    file_handler = logging.FileHandler(LOG_FILE_PATH, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Do not propagate to root logger (to avoid duplicate logging)
    logger.propagate = False

    return logger
