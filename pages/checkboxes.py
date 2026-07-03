"""
    URL = https://the-internet.herokuapp.com/checkboxes
"""

from selenium.webdriver.common.by import By # find element by different parameters

from pages.base_page import BasePage
from config.config import Config

class CheckboxesPage(BasePage):
    URL = f"{Config.BASE_URL}/checkboxes"

    HEADING = (By.TAG_NAME, "h3")
    CHECKBOXES = (By.XPATH, "//form[@id='checkboxes']//input[@type='checkbox']")

    def open(self):
        super().open(self.URL)
    
    def click_on_checkbox(self, index):
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        if index < len(checkboxes):
            checkboxes[index].click()
        else:
            raise IndexError("Checkbox index out of range")
        
    def unclick_on_checkbox(self, index):
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        if index < len(checkboxes):
            if checkboxes[index].is_selected():
                checkboxes[index].click()
        else:
            raise IndexError("Checkbox index out of range")