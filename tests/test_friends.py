from niffler_tests.pages.people_page import people
from niffler_tests.pages.main_page import main


def test_verify_no_friends(browser_management, authorization):
    main.navigate_to_friends()
    people.url_contains('/friends')

    people.verify_title_table_names('Avatar', 'Username', 'Name', 'Actions')

    people.verify_message('There are no friends yet!')
