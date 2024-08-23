import pytest

from selene import browser
import dotenv

from niffler_tests.test_data.credentials import standard_user
from niffler_tests.pages.login_page import login
from niffler_tests.utils.random_data import generate_random_data
from niffler_tests.utils.requests_helper import registration_with_api


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