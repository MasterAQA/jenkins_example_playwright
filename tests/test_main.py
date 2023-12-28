import allure
import pytest

from pages.main_page import MainPage

main_directories = [
    "Store",
    "Mac",
    "iPad",
    "iPhone",
    "Watch",
    "AirPods",
    "TV and Home",
    "Entertainment",
    "Accessories",
    "Support",
]


@allure.feature("Main Page")
@allure.story("Main Page")
@allure.title("Test all directories displays")
def test_main_menu(open):
    main_page = MainPage(open)

    main_page.go_to("https://www.apple.com/")

    for directory in main_directories:
        main_page.category(directory).check_is_visible()


@pytest.mark.only_browser("chromium")
@allure.feature("Main Page")
@allure.story("Search")
@allure.title("Test search function")
def test_search_function(open):
    main_page = MainPage(open)

    main_page.go_to("https://www.apple.com/")
    main_page.search_icon_button.click()
    main_page.search_input.keyboard_fill("iPhone", open)

    main_page.result_search.check_is_visible()
