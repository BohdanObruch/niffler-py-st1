from selene import browser, have

from niffler_tests.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.login_btn = self.login_btn
        self.user_name = browser.element('[name="username"]')
        self.password = browser.element('[name="password"]')
        self.submit_btn = browser.element('[type="submit"]')
        self.header_title = browser.element('.header__title')
        self.error_message = browser.element('.form__error')

    def navigate(self):
        browser.open('')
        self.login_btn.click()

    def perform_login(self, user_name, password):
        self.user_name.type(user_name)
        self.password.type(password)
        self.submit_btn.click()

    def varify_title(self, title):
        self.header_title.should(have.text(title))

    def verify_error_message(self, error_message):
        self.error_message.should(have.text(error_message))


login = LoginPage()
