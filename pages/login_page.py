"""
    URL = https://the-internet.herokuapp.com/login
"""
from selenium.webdriver.common.by import By # find element by different parameters

from pages.base_page import BasePage
from config.config import Config

class LoginBage(BasePage):
    URL = f"{Config.BASE_URL}/login"

    LOGIN_FORM = (By.ID, "login")
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")    
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    FLASH_MESSAGE = (By.ID, "flash")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")

    def open(self):
        super().open(self.URL)

    def enter_username(self, username):
        self.type(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_flash_message(self):
        return self.get_text(self.FLASH_MESSAGE)
    
    def is_logged_in(self):
        return self.is_element_present(self.LOGOUT_BUTTON)  