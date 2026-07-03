from pages.login_page import LoginPage

def test_succesfull_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.get_flash_message()
    assert login_page.is_logged_in()

def test_failed_login_wrong_username(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("wrong_user", "SuperSecretPassword!")
    assert "Your username is invalid!" in login_page.get_flash_message()
    assert not login_page.is_logged_in()

def test_failed_login_wrong_password(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("tomsmith", "wrong_password")
    assert "Your password is invalid!" in login_page.get_flash_message()
    assert not login_page.is_logged_in()

def test_empty_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_login()

    assert "Your username is invalid!" in login_page.get_flash_message()