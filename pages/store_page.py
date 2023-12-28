from pages.base_page import BasePage
from locators.locators import Button, Text


class StorePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @property
    def go_to_category_airpods(self) -> Button:
        return Button(
            self.page.locator(
                "//a[@class='rf-productnav-card-title'][contains(text(), 'AirPods')]"
            ),
            "Category Airpods",
        )

    @property
    def buy_product(self) -> Button:
        return Button(
            self.page.locator("//a[@class='icon-wrapper button button-elevated buy']"),
            "Buy product",
        )

    @property
    def add_to_cart(self) -> Button:
        return Button(
            self.page.get_by_text("Add to Bag"),
            "Add to Cart",
        )

    @property
    def cart(self) -> Text:
        return Text(
            self.page.locator("//h1[@class='rs-bag-header']"),
            "Cart",
        )
