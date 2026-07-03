"""
    CENTRAL FRAMEWORK CONFIGURATION FILE
"""

class Config:
    BASE_URL = "https://the-internet.herokuapp.com"

    # Timeout
    IMPLICIT_WAIT = 5
    EXPLICIT_WAIT = 10
    PAGE_LOAD_TIMEOUT = 30
    
    # Browser configuration
    DEFAULT_BROSWER = "chrome"
    DEFAULT_HEADLESS = False

    # DIRECTORIES
    SCREENSHOTS_DIR = "screenshots"
    REPORTS_DIR = "reports"
    LOG_DIR = "logs"