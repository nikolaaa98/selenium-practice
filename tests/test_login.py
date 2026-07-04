import pytest

from config.config import Config
from pages.login_page import LoginPage

LOGIN_DATA = [
    (Config.VALID_USERNAME, Config.VALID_PASSWORD, "You logged into a secure area!", True, "valid credentials"),
    (Config.INVALID_USERNAME, Config.VALID_PASSWORD, "Your username is invalid!", False, "invalid username"),
    (Config.VALID_USERNAME, Config.INVALID_PASSWORD, "Your password is invalid!", False, "invalid password"),
    ("", "", "Your username is invalid!", False, "empty credentials")
]

@pytest.mark.parametrize(
        "username, password, expected_message, should_be_logged_in",
        [(u, p, m, l) for (u, p, m, l, _) in LOGIN_DATA],
        ids=[tid for (*_, tid) in LOGIN_DATA],
)
def test_login(driver, username, password, expected_message, should_be_logged_in):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    assert expected_message in login_page.get_flash_message()
    assert login_page.is_logged_in() == should_be_logged_in