from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from config.config import Config

SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]

def get_driver(browser: str = None, headless: bool = None):
    """
    Returns a Selenium WebDriver instance based on the specified browser and headless mode.

    :param browser: The browser to use (chrome, firefox, edge). Defaults to the value in Config if not provided.
    :param headless: Whether to run the browser in headless mode. Defaults to the value in Config if not provided.
    :return: A Selenium WebDriver instance.
    """
    browser = (browser or Config.DEFAULT_BROSWER).lower()
    headless = headless if headless is not None else Config.DEFAULT_HEADLESS
    
    if browser not in SUPPORTED_BROWSERS:
        raise ValueError(f"Unsupported browser: {browser}. Supported browsers are: {SUPPORTED_BROWSERS}")
    
    if browser == "chrome":
        driver = _create_chromium_driver(headless)
    elif browser == "firefox":
        driver = _create_firefox_driver(headless)
    elif browser == "edge":
        driver = _create_edge_driver(headless)

    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
    if not headless:
        driver.maximize_window()
    
    return driver
    
def _create_chromium_driver(headless: bool):
    options = ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-notifications") # disable popups and notifications
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox") # only for chrome because it blocks security mechanisms
    
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def _create_firefox_driver(headless: bool):
    options = FirefoxOptions()
    if headless:
        options.add_argument("--headless")
    
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    return driver

def _create_edge_driver(headless: bool):
    options = EdgeOptions()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-notifications")
    
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)
    return driver
