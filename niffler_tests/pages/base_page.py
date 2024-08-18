from selene import browser, have


class BasePage:
    def __init__(self):
        self.login_btn = browser.element('[href="/redirect"]')
        self.register_btn = browser.element('[href*="/register"]')
        self.alert_message = browser.element('.App .Toastify__toast-body')
        self.no_people = browser.element('.main-content__section>div')
        self.full_table = browser.element('.table')

    @staticmethod
    def url_contains(url):
        return url in browser.driver.current_url

    def verify_message(self, message, flag=True):
        if flag:
            self.no_people.should(have.text(message))
        else:
            self.no_people.should(have.no.text(message))

    def verify_alert_message(self, message):
        self.alert_message.should(have.text(message))

    def verify_title_table_names(self, avatar, username, name, actions):
        self.full_table.all('th').should(have.exact_texts(
            avatar, username, name, actions))
