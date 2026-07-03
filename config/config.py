"""
    CENTRAL FRAMEWORK CONFIGURATION FILE
"""
import os

from dotenv import load_dotenv

# Load environment variables from .env file (project root)
load_dotenv()


class Config:
    BASE_URL = "https://the-internet.herokuapp.com"

    # Timeout
    IMPLICIT_WAIT = 5
    EXPLICIT_WAIT = 10
    PAGE_LOAD_TIMEOUT = 30
    
    # Browser configuration
    DEFAULT_BROSWER = os.getenv("BROWSER", "chrome")
    DEFAULT_HEADLESS = os.getenv("HEADLESS", "False").lower() in ("true", "1", "yes", "no")

    # DIRECTORIES
    SCREENSHOTS_DIR = "screenshots"
    REPORTS_DIR = "reports"
    LOG_DIR = "logs"

    # CREDENTIALS (loaded from .env - never commit real values)
    VALID_USERNAME = os.getenv("VALID_USERNAME", "")
    VALID_PASSWORD = os.getenv("VALID_PASSWORD", "")
    INVALID_USERNAME = os.getenv("INVALID_USERNAME", "wrong_user")
    INVALID_PASSWORD = os.getenv("INVALID_PASSWORD", "wrong_password")
