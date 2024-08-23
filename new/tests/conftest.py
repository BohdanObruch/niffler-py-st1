import pytest
import time
from selene import browser
import dotenv

from niffler_tests.test_data.credentials import standard_user
from niffler_tests.pages.login_page import login
from niffler_tests.utils.random_data import generate_random_data
from niffler_tests.utils.requests_helper import registration_with_api

import os

import pytest
from niffler_tests.clients.spends_client import SpendsHttpClient


@pytest.fixture(scope="session", autouse=True)
def envs():
    dotenv.load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--base_url", default="http://frontend.niffler.dc")


@pytest.fixture(scope="function")
def browser_management(request):
    base_url = request.config.getoption("--base_url")
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = base_url
    yield
    browser.quit()


@pytest.fixture()
def authorization():
    login.navigate()
    login.perform_login(standard_user['username'], standard_user['password'])
    login.varify_title('Niffler. The coin keeper.')


@pytest.fixture()
def successful_registration():
    username, password = generate_random_data()
    response = registration_with_api(username, password)
    assert response.status_code == 201
    assert 'Congratulations! You\'ve registered!' in response.text
    yield username, password



@pytest.fixture(scope="session")
def frontend_url(envs):
    return os.getenv("FRONTEND_URL")


@pytest.fixture(scope="session")
def gateway_url(envs):
    return os.getenv("GATEWAY_URL")


@pytest.fixture(scope="session")
def app_user(envs):
    return os.getenv("TEST_USERNAME"), os.getenv("TEST_PASSWORD")


@pytest.fixture(scope="session")
def auth(frontend_url, app_user):
    username, password = app_user
    browser.open(frontend_url)
    browser.element('a[href*=redirect]').click()
    browser.element('input[name=username]').set_value(username)
    browser.element('input[name=password]').set_value(password)
    browser.element('button[type=submit]').click()
    time.sleep(1)
    token = browser.driver.execute_script('return window.sessionStorage.getItem("id_token")')
    return token


@pytest.fixture(scope="session")
def spends_client(gateway_url, auth) -> SpendsHttpClient:
    return SpendsHttpClient(gateway_url, auth)


@pytest.fixture(params=[])
def category(request, spends_client):
    category_name = request.param
    current_categories = spends_client.get_categories()
    category_names = [category["category"] for category in current_categories]
    if category_name not in category_names:
        spends_client.add_category(category_name)
    return category_name


@pytest.fixture(params=[])
def spends(request, spends_client):
    spend = spends_client.add_spends(request.param)
    yield spend
    try:
        # TODO вместо исключения проверить список текущих spends
        spends_client.remove_spends([spend["id"]])
    except Exception:
        pass


@pytest.fixture()
def main_page(auth, frontend_url):
    browser.driver.refresh()
