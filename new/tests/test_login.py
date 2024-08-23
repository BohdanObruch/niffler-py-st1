from niffler_tests.test_data.credentials import standard_user, wrong_user
from niffler_tests.pages.login_page import login


def test_successful_login(browser_management):
    login.navigate()
    login.url_contains('/login')
    login.perform_login(standard_user['username'], standard_user['password'])
    login.url_contains('/main')
    login.varify_title('Niffler. The coin keeper.')


def test_unsuccessful_login(browser_management):
    login.navigate()
    login.url_contains('/login')
    login.perform_login(wrong_user['username'], wrong_user['password'])
    login.verify_error_message('Bad credentials')
