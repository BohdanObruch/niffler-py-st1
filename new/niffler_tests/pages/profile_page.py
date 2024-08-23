from selene import browser, have
from niffler_tests.pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self):
        super().__init__()
        self.category_title = browser.element('form h2')
        self.add_category_input = browser.element('.add-category__input-container .form__input')
        self.add_category_btn = browser.element('.add-category__input-container .button')

    def varify_title(self, title):
        self.category_title.should(have.text(title))

    def add_category(self, category):
        self.add_category_input.type(category)
        self.add_category_btn.click()

    def verify_category_message(self, message):
        self.alert_message.should(have.text(message))

    def verify_error_message(self, message):
        self.alert_message.should(have.text(message))


profile = ProfilePage()
