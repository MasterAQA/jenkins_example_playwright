from locators.locators import Button, Input, Text
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @property
    def sign_in(self) -> Button:
        return Button(
            self.page.locator("//a[@class='form-button']"),
            "Sign In",
        )

    @property
    def account_input(self) -> Input:
        return Input(
            self.page.locator("//input[@id='account_name_text_field']"),
            "Account input",
        )

    @property
    def password_input(self) -> Input:
        return Input(
            self.page.locator("//input[@id='password_text_field']"),
            "Password input",
        )

    @property
    def two_factor_auth(self) -> Text:
        return Text(
            self.page.get_by_text("message with a verification code"),
            "Two-Factor-Authentication",
        )
