import allure
import playwright.sync_api
from playwright.sync_api import expect


class BaseElement:
    def __init__(self, selector: playwright.sync_api.Locator, name: str):
        self.selector = selector
        self.name = name

    def check_is_visible(self):
        with allure.step(f"Check what [{self.name}] is visible"):
            expect(self.selector).to_be_visible()

    def wait_for_element(self):
        with allure.step(f"Awaiting when [{self.name}] is visible"):
            self.selector.wait_for()

    def check_is_visible_using_iframe(self, iframe):
        with allure.step(f"Check what [{self.name}] is visible on iframe"):
            expect(iframe.locator(self.selector)).to_be_visible()