import os
from datetime import datetime
from typing import Optional  # <-- Dodato za kompatibilnost sa Python 3.9

from config.config import Config
from utils.logger import get_logger

logger = get_logger(__name__)

# Create screenshots directory if it does not exist
os.makedirs(Config.SCREENSHOTS_DIR, exist_ok=True)


def take_screenshot(driver, test_name: str) -> Optional[str]:  # <-- Promenjeno sa str | None
    """
    Takes a screenshot and returns the path to the saved file.
    :param driver: Selenium WebDriver instance
    :param test_name: Name of the test (used in the file name)
    :return: Path to the screenshot or None if capture failed
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Sanitize the test name to be safe for the file system
    safe_name = "".join(c if c.isalnum() or c in "._-" else "_" for c in test_name)
    file_name = f"{safe_name}_{timestamp}.png"
    file_path = os.path.join(Config.SCREENSHOTS_DIR, file_name)

    try:
        driver.save_screenshot(file_path)
        logger.info(f"Screenshot saved: {file_path}")
        return file_path
    except Exception as e:
        logger.error(f"Failed to take screenshot: {e}")
        return Noneå