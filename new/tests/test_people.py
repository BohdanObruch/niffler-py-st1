from niffler_tests.pages.people_page import people
from new.niffler_tests.pages.main_page import main
import pytest


@pytest.mark.order(2)
def test_add_some_friend(browser_management, authorization, successful_registration):
    main.navigate_to_all_people()
    people.url_contains('/people')

    people.verify_title_table_names('Avatar', 'Username', 'Name', 'Actions')

    people.verify_message('There are no other users yet!', False)

    people.choice_random_users_add_to_friend(1)
    people.verify_alert_message('Invitation is sent')


@pytest.mark.order(1)
def test_verify_no_friends(browser_management, authorization):
    main.navigate_to_all_people()
    people.url_contains('/people')

    people.verify_title_table_names('Avatar', 'Username', 'Name', 'Actions')

    people.verify_message('There are no other users yet!')
