from niffler_tests.test_data.credentials import standard_user, wrong_user
from niffler_tests.pages.registration_page import registration
import pytest
from niffler_tests.utils.requests_helper import registration_with_api


@pytest.mark.order("first")
def test_successful_registration(browser_management):
    registration.navigate()
    registration.url_contains('/register')
    registration.perform_registration(
        standard_user['username'], standard_user['password'], standard_user['repeat_password'])
    registration.varify_title('Congratulations! You\'ve registered!')


def test_unsuccessful_registration(browser_management):
    registration.navigate()
    registration.url_contains('/register')
    registration.perform_registration(
        wrong_user['username'], wrong_user['password'], wrong_user['repeat_password'])
    registration.verify_error_message('Passwords should be equal')


def test_registration_with_same_registration_data(browser_management):
    registration.navigate()
    registration.url_contains('/register')
    registration.perform_registration(standard_user['username'], standard_user['password'],
                                      standard_user['repeat_password'])
    registration.verify_error_message(f'Username `{standard_user['username']}` already exists')


def test_registration_with_same_registration_data_with_api(successful_registration):
    username, password = successful_registration

    response = registration_with_api(username, password)
    assert response.status_code == 400
    assert f'Username `{username}` already exists' in response.text
