from selene import browser, be


class MainPage:
    def __init__(self):
        self.profile = browser.element('[href="/profile"]')
        self.all_people = browser.element('[href="/people"]')
        self.friends = browser.element('[href="/friends"]')
        self.main = browser.element('href="/main"')
        self.new_friends_point = browser.element('.header__navigation .header__sign')

    def navigate_to_main(self):
        self.main.click()

    def navigate_to_profile(self):
        self.profile.click()

    def navigate_to_all_people(self):
        self.all_people.click()

    def navigate_to_friends(self):
        self.friends.click()

    def verify_new_friends_point(self):
        self.new_friends_point.should(be.visible)


main = MainPage()
