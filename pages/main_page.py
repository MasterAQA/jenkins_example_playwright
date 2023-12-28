from pages.base_page import BasePage
from locators.locators import Button, Input, Text, Item


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def category(self, category_name) -> Item:
        return Item(
            self.page.locator(
                "//li[@class='globalnav-submenu-trigger-item']//a[contains(@aria-label, '{}')]".format(
                    category_name
                )
            ),
            "category - " + category_name,
        )

    @property
    def search_icon_button(self) -> Button:
        return Button(
            self.page.locator("//a[@id='globalnav-menubutton-link-search']"),
            "Search icon button",
        )

    @property
    def search_input(self) -> Input:
        return Input(
            self.page.locator("//input[@class='globalnav-searchfield-input']"),
            "Search input",
        )

    @property
    def result_search(self) -> Text:
        return Text(
            self.page.locator("//div[@class='rf-serp-resultcount']"),
            "Result text",
        )
