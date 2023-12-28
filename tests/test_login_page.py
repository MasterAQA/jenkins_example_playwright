import allure
import pytest

from conftest import data as env
from pages.login_page import LoginPage


@pytest.mark.only_browser("chromium")
# @pytest.mark.flaky(reruns=2)
@allure.feature("Login")
@allure.story("Login")
@allure.title("Login in Apple account, check two-factor auth")
def test_login(open):
    login_page = LoginPage(open)

    login_page.go_to("https://www.apple.com/shop/bag")
    login_page.sign_in.click()
    login_frame = login_page.page.frame_locator("//iframe")

    login_page.account_input.keyboard_fill_using_iframe(
        env.apple_username, login_frame, open
    )
    login_page.password_input.keyboard_fill_using_iframe(
        env.apple_password, login_frame, open
    )

    login_page.two_factor_auth.check_is_visible_using_iframe(login_frame)
