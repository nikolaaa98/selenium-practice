from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from config.config import Config
from utils.logger import get_logger

logger = get_logger(__name__)

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    def open(self, url):
        logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def get_title(self):
        title = self.driver.title
        logger.debug(f"Page title: {title}")
        return title
    
    def get_current_url(self):
        return self.driver.current_url
    
    def click(self, locator):
        logger.debug(f"Clicking element: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text, sensitive: bool = False):
        """
        Type text into the element found by `locator`.
        :param sensitive: if True, the value is masked in logs (e.g. passwords).
        """
        display_text = "***" if sensitive else f"'{text}'"
        logger.debug(f"Typing {display_text} into element: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        text = element.text
        logger.debug(f"Read text '{text}' from element: {locator}")
        return text
    
    def is_displayed(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except TimeoutException:
            logger.warning(f"Element not visible within timeout: {locator}")
            return False

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            logger.warning(f"Element not present within timeout: {locator}")
            return False

    def is_element_present_now(self, locator):
        self.driver.implicitly_wait(0)
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            self.driver.implicitly_wait(Config.IMPLICIT_WAIT)

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))