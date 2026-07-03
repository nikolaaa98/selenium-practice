from config.config import Config
from pages.login_page import LoginPage

def test_succesfull_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
    assert "You logged into a secure area!" in login_page.get_flash_message()
    assert login_page.is_logged_in()

def test_failed_login_wrong_username(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(Config.INVALID_USERNAME, Config.VALID_PASSWORD)
    assert "Your username is invalid!" in login_page.get_flash_message()
    assert not login_page.is_logged_in()

def test_failed_login_wrong_password(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(Config.VALID_USERNAME, Config.INVALID_PASSWORD)
    assert "Your password is invalid!" in login_page.get_flash_message()
    assert not login_page.is_logged_in()

def test_empty_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_login()

    assert "Your username is invalid!" in login_page.get_flash_message()