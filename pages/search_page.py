from locators.locators import Input, Text
from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @property
    def search_input(self) -> Input:
        return Input(
            self.page.locator("//input[@id='searchform-input']"),
            "Search input",
        )

    @property
    def result_search(self) -> Text:
        return Text(
            self.page.locator("//div[@class='rf-serp-resultcount']"),
            "Result text",
        )
