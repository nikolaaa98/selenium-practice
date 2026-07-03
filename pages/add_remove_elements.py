"""
    URL = https://the-internet.herokuapp.com/add_remove_elements/
"""

from selenium.webdriver.common.by import By # find element by different parameters

from pages.base_page import BasePage
from config.config import Config

class AddRemoveElementsPage(BasePage):
    URL = f"{Config.BASE_URL}/add_remove_elements/"

    HEADING = (By.TAG_NAME, "h3")
    ADD_ELEMENT_BUTTON = (By.XPATH, "//*[@id='content']/div/button")
    DELETE_BUTTON = (By.XPATH, "//*[@id='elements']/button")
    FOOTER_LINK = (By.LINK_TEXT, "Elemental Selenium")

    def open(self):
        super().open(self.URL)

    def get_header_text(self):
        return self.get_text(self.HEADING)

    def click_add_element(self):
        self.click(self.ADD_ELEMENT_BUTTON)

    def get_footer_link_text(self):
        return self.get_text(self.FOOTER_LINK)
    
    def click_on_delete_button(self):
        self.click(self.DELETE_BUTTON)
