from selene import browser, have
from niffler_tests.pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self):
        super().__init__()
        self.register_btn = self.register_btn
        self.user_name = browser.element('#username')
        self.password = browser.element('#password')
        self.repeat_password = browser.element('#passwordSubmit')
        self.submit_btn = browser.element('.form__submit')
        self.error_message = browser.element('.form__error')
        self.error_messages = browser.all('.form__error')
        self.successful_message = browser.element('.form')

    def navigate(self):
        browser.open('')
        self.register_btn.click()

    def perform_registration(self, user_name, password, repeat_password):
        self.user_name.type(user_name)
        self.password.type(password)
        self.repeat_password.type(repeat_password)
        self.submit_btn.click()

    def varify_title(self, message):
        self.successful_message.should(have.text(message))

    def verify_error_message(self, error_message):
        self.error_message.should(have.exact_text(error_message))

    def verify_first_error_message(self, error_message):
        self.error_messages.first.should(have.text(error_message))

    def verify_second_error_message(self, error_message):
        self.error_messages.second.should(have.text(error_message))

    def verify_third_error_message(self, error_message):
        self.error_messages[2].should(have.text(error_message))


registration = RegistrationPage()
