import time
from multiprocessing import Event
from threading import Lock

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


current_file = Path(__file__)
project_root = current_file.parent

USERS_FILE_PATH = project_root / "users.txt"
file_lock = Lock()
USERS_FILE_PATH = Path(USERS_FILE_PATH).resolve()

def unlock_all_users():
    with file_lock:
        with open(USERS_FILE_PATH, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith("#"):
                lines[i] = line[1:]

        with open(USERS_FILE_PATH, "w") as file:
            file.writelines(lines)


unlock_all_users()


class FixtureData:
    def __init__(self):
        self.data = None


@pytest.fixture
def lock_user_fixture(request):
    fixture_data = getattr(request.module, "_fixture_data", None)
    if fixture_data is None:
        fixture_data = FixtureData()
        setattr(request.module, "_fixture_data", fixture_data)
    return fixture_data


def lock_user(username):
    with file_lock:
        with open(USERS_FILE_PATH, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if username in line:
                lines[i] = "#" + line

        with open(USERS_FILE_PATH, "w") as file:
            file.writelines(lines)


def unlock_user(username):
    with file_lock:
        with open(USERS_FILE_PATH, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith("#") and username in line:
                lines[i] = line[1:]

        with open(USERS_FILE_PATH, "w") as file:
            file.writelines(lines)


def wait_for_available_users(access_levels, timeout=6000, poll_interval=1):
    start_time = time.time()

    while time.time() - start_time < timeout:
        with file_lock:
            with open(USERS_FILE_PATH, "r") as file:
                lines = file.readlines()

            for i, line in enumerate(lines):
                if not line.strip().startswith("#"):
                    user, user_access_level = line.strip().split()
                    if user_access_level in access_levels:
                        return user, user_access_level

        time.sleep(poll_interval)

    raise ValueError(f"No available user with access levels {access_levels} found within the timeout.")


def user_with_access(*access_levels, lock_user_fixture=None):
    user, access_level = wait_for_available_users(access_levels)

    with file_lock:
        with open(USERS_FILE_PATH, "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.strip() == f"{user} {access_level}":
                lines[i] = "#" + line

        with open(USERS_FILE_PATH, "w") as file:
            file.writelines(lines)

    if lock_user_fixture:
        lock_user_fixture.data = user, access_level

    return user


@pytest.fixture(scope="function")
def open_page(browser: Browser, request, lock_user_fixture):
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
    page.context.tracing.stop(path=f"reports/{request.node.name}.zip")

    # После окончания теста, проверяем, использовался ли username
    user_with_access_info = lock_user_fixture.data
    if user_with_access_info:
        username, _ = user_with_access_info
        unlock_user(username)