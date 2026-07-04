from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class KeywordEngine:
    def __init__(self):
        self.driver = None

    def execite(self, keyword: str, locator_type: str, locator: str, value: str):
        action = self._action.get(keyword.strip().lower())

    def _open_browser(self, _it, _loc, value):
        if value.lower() == "chrome":
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        elif value.lower() == "firefox":
            self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        else:
            raise ValueError(f"Unsupported browser: {value}")
        self.driver.maximize_window()

    def _navigate(self, _it, _loc, value):
        self.driver.get(value)

    def _type(self, locator_type, locator, value):
        self.driver.find_element(*self._by(locator_type, locator)).send_keys(value)

    def _click(self, locator_type, locator, _value):
        self.driver.find_element(*self._by(locator_type, locator)).click()

    def _verify_text(self, locator_type, locator, value):
        element_text = self.driver.find_element(*self._by(locator_type, locator)).text
        assert element_text == value, f"Expected text '{value}', but got '{element_text}'"

    def _close_browser(self, *_):
        if self.driver:
            self.driver.quit()
            self.driver = None

    @staticmethod
    def _by(locator_type: str, locator: str):
        mapping = {
            "id" : By.ID,
            "name" : By.NAME,
            "css" : By.CSS_SELECTOR,
            "xpath" : By.XPATH,
            "class" : By.CLASS_NAME,
            "linktext" : By.LINK_TEXT,
        }
        key = locator_type.strip().lower()
        if key not in mapping:
            raise ValueError(f"Unsupported locator type: {locator_type}")
        return mapping[key], locator


    _action = {
        "open_browser": _open_browser,
        "navigate": _navigate,
        "type": _type,
        "click": _click,
        "verify_text": _verify_text,
        "close_browser": _close_browser
    }