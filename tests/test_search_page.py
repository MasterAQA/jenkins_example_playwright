import allure
import pytest


from pages.search_page import SearchPage


@pytest.mark.only_browser("chromium")
@allure.feature("Search Page")
@allure.story("Search")
@allure.title("Test search page and function")
def test_search(open_page):
    search_page = SearchPage(open_page)

    search_page.go_to("https://www.apple.com/us/searchj")
    search_page.search_input.keyboard_fill("Mac", open_page)

    search_page.result_search.check_is_visible()
