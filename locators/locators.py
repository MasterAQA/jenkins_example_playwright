import allure
import playwright
from playwright.sync_api import Locator

from locators.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, selector: playwright.sync_api.Locator, name: str):
        super().__init__(selector, name)

    def click(self):
        with allure.step(f"Click button [{self.name}]"):
            self.selector.click()


class Input(BaseElement):
    def __init__(self, selector: playwright.sync_api.Locator, name: str):
        super().__init__(selector, name)

    def fill(self, text: str):
        with allure.step(f"Fill [{self.name}] - [{text}]"):
            self.selector.fill(text)

    def clear(self):
        with allure.step(f"clear [{self.name}]"):
            self.selector.clear()

    def click(self):
        with allure.step(f"Click input form [{self.name}]"):
            self.selector.click()

    def keyboard_fill(self, text, page):
        with allure.step(f"Fill [{self.name}] - [{text}] from keyboard"):
            self.selector.click()
            page.keyboard.type(text)
            page.keyboard.press("Enter")

    def keyboard_fill_using_iframe(self, text, iframe, page):
        with allure.step(f"Fill [{self.name}] - [{text}] from keyboard in iframe"):
            iframe.locator(self.selector).click()
            page.keyboard.type(text)
            page.keyboard.press("Enter")


class Text(BaseElement):
    def __init__(self, selector: playwright.sync_api.Locator, name: str):
        super().__init__(selector, name)

    def get_text(self):
        with allure.step(f"Get text from [{self.name}]"):
            return self.selector.text_content()


class Item(BaseElement):
    def __init__(self, selector: playwright.sync_api.Locator, name: str):
        super().__init__(selector, name)
