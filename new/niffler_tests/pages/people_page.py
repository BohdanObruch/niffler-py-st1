from selene import browser, have, command, query
from niffler_tests.pages.base_page import BasePage
from niffler_tests.utils.choice_random_people import choice_random_friends


class PeoplePage(BasePage):
    def __init__(self):
        super().__init__()
        self.full_table = browser.element('.table')
        self.message_invitation = browser.all('.abstract-table__buttons div:not([data-tooltip-id="add-friend"], '
                                              '.react-tooltip, .react-tooltip-arrow)')
        self.add_people = browser.all('[data-tooltip-id="add-friend"]')
        self.all_actions = browser.all('.abstract-table__buttons>div:not([role="tooltip"])')

    def choice_random_users_add_to_friend(self, count_people):
        all_people = len(self.add_people)
        random_people = choice_random_friends(all_people, count_people)
        for i in random_people:
            self.add_people[i].perform(command.js.scroll_into_view).click()
            self.all_actions[i].with_(timeout=5).click().should(have.text('Pending invitation'))

    def verify_message_invitation(self, message):
        for element in self.message_invitation:
            element.should(have.text(message))
            if message in element.get(query.text):
                return
        raise AssertionError(f"'{message}' not found in any of the elements")


people = PeoplePage()
