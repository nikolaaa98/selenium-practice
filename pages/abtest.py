"""
    URL = https://the-internet.herokuapp.com/abtest
"""
from selenium.webdriver.common.by import By # find element by different parameters

from pages.base_page import BasePage
from config.config import Config

class ABtest(BasePage):
    URL = f"{Config.BASE_URL}/abtest"

    HEADING = (By.TAG_NAME, "h3")
    PARAGRAPH = (By.TAG_NAME, "p")

    def open(self):
        super().open(self.URL)
        
    def get_heading(self):
        return self.get_text(self.HEADING)
    
    def get_paragraph(self):
        return self.get_text(self.PARAGRAPH)