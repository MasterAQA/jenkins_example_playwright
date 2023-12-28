from locators.locators import Button, Text
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @property
    def remove_product(self) -> Button:
        return Button(
            self.page.locator("//button[contains(@id, 'delete')]"),
            "Remove product",
        )

    @property
    def empty_cart(self) -> Text:
        return Text(
            self.page.locator(
                "//h1[@class='rs-bag-header'][contains(text(), 'Your bag is empty')]"
            ),
            "Empty Cart",
        )
