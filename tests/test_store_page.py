import allure
import pytest

from pages.cart_page import CartPage
from pages.store_page import StorePage


@pytest.mark.only_browser("chromium")
@allure.feature("Cart")
@allure.story("Add in Cart")
@allure.title("Add product in Cart")
def test_add_product(open_page):
    store_page = StorePage(open_page)

    store_page.go_to("https://www.apple.com/store")
    store_page.go_to_category_airpods.click()
    store_page.buy_product.click()
    store_page.add_to_cart.click()
    store_page.cart.wait_for_element()

    store_page.cart.check_is_visible()

@pytest.mark.only_browser("chromium")
# @pytest.mark.flaky(reruns=2)
@allure.feature("Cart")
@allure.story("Add and Remove")
@allure.title("Add product, and remove from Cart")
def test_add_and_remove_product(open_page):
    store_page = StorePage(open_page)
    cart_page = CartPage(open_page)

    store_page.go_to("https://www.apple.com/store")
    store_page.go_to_category_airpods.click()

    store_page.buy_product.click()
    store_page.add_to_cart.click()
    store_page.cart.wait_for_element()

    store_page.cart.check_is_visible()

    cart_page.remove_product.click()
    cart_page.empty_cart.check_is_visible()
