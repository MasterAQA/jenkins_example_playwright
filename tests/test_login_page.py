import allure
import pytest

from conftest import data as env, lock_user, unlock_user, user_with_access
from pages.login_page import LoginPage



# @pytest.mark.only_browser("chromium")
# @pytest.mark.flaky(reruns=2)
@allure.feature("Login")
@allure.story("Login")
@allure.title("Login in Apple account, check two-factor auth")
def test_login(open_page, lock_user_fixture):
    login_page = LoginPage(open_page)

    login_page.go_to("https://www.apple.com/shop/bag")
    login_page.sign_in.click()
    login_frame = login_page.page.frame_locator("//iframe")

    username = user_with_access("premium", lock_user_fixture=lock_user_fixture)

    login_page.account_input.keyboard_fill_using_iframe(
        username, login_frame, open_page
    )
    # login_page.password_input.keyboard_fill_using_iframe(
    #     "fiy51746823", login_frame, open_page
    # )
    # finally:
    #     unlock_user(username)

    # login_page.two_factor_auth.check_is_visible_using_iframe(login_frame)
