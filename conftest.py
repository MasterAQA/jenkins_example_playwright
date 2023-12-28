import allure
from playwright.sync_api import Browser
import pytest
import os

from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path("../.env")
load_dotenv(dotenv_path=dotenv_path)


class data:

    apple_username = os.getenv("APPLE_USERNAME")
    apple_password = os.getenv("APPLE_PASSWORD")


@pytest.fixture(scope="function")
def open(browser: Browser, request):
    context = Browser.new_context(self=browser)
    context.set_default_timeout(10000)
    page = context.new_page()

    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page

    screenshot = page.screenshot(
        path=f"screenshots/{request.node.name}.png", full_page=True
    )
    allure.attach(
        screenshot,
        name=f"{request.node.name}",
        attachment_type=allure.attachment_type.PNG,
    )

    page.close()
    page.context.tracing.stop(path="reports/trace.zip")
