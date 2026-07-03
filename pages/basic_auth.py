"""
    URL = https://the-internet.herokuapp.com/basic_auth/
"""

from selenium.webdriver.common.by import By # find element by different parameters

from pages.base_page import BasePage
from config.config import Config

class BasicAuthPage(BasePage):
    URL = f"{Config.BASE_URL}/basic_auth/"

    HEADING = (By.TAG_NAME, "h3")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='content']/div/p")
    FOOTER_LINK = (By.LINK_TEXT, "Elemental Selenium")

    def open(self):
        super().open(self.URL)

    def get_header_text(self):
        return self.get_text(self.HEADING)

    def get_success_message_text(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_footer_link_text(self):
        return self.get_text(self.FOOTER_LINK)