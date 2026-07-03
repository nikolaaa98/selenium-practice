"""
    URL = https://the-internet.herokuapp.com/context_menu
"""

from selenium.webdriver.common.by import By # find element by different parameters

from pages.base_page import BasePage
from config.config import Config

class ContextMenuPage(BasePage):
    URL = f"{Config.BASE_URL}/context_menu"

    HEADING = (By.TAG_NAME, "h3")
    HOTSPOT = (By.ID, "hot-spot")
    PARAGRAPH = (By.TAG_NAME, "p")

    def open(self):
        super().open(self.URL)

    def get_heading_text(self):
        return self.get_text(self.HEADING)
    
    def right_click_on_hotspot(self):
        hotspot_element = self.driver.find_element(*self.HOTSPOT)
        self.actions.context_click(hotspot_element).perform()

    def click_on_alert_ok(self):
        alert = self.driver.switch_to.alert
        alert.accept()