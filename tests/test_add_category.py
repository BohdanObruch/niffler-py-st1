from niffler_tests.test_data.credentials import categories
from niffler_tests.pages.profile_page import profile
from niffler_tests.pages.main_page import main
import pytest


@pytest.mark.order(1)
@pytest.mark.parametrize('category', categories)
def test_add_category(browser_management, authorization, category):
    main.navigate_to_profile()

    profile.varify_title('Add new category')
    profile.add_category(category)
    profile.verify_category_message('New category added')


@pytest.mark.order(2)
def test_add_present_category(browser_management, authorization):
    main.navigate_to_profile()

    profile.varify_title('Add new category')
    profile.add_category(categories[0])
    profile.verify_alert_message('Can not add new category')


# Это пока висит потому что не решил нюанс с логином
# def test_add_category_with_api():
#     import requests
#     import json
#
#     url = "http://gateway.niffler.dc:8090/api/categories/add"
#
#     payload = json.dumps({
#         "category": "1266"
#     })
#     headers = {
#         'Authorization': 'Bearer eyJraWQiOiI2NTcwNGEyMS1lNWEyLTRkMmEtOTJjYS0wZTdiZjU0ZDM4MDMiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJxd2VydHkiLCJhdWQiOiJjbGllbnQiLCJhenAiOiJjbGllbnQiLCJhdXRoX3RpbWUiOjE3MjM1MzQ0ODcsImlzcyI6Imh0dHA6Ly9hdXRoLm5pZmZsZXIuZGM6OTAwMCIsImV4cCI6MTcyMzUzNjI4NywiaWF0IjoxNzIzNTM0NDg3LCJqdGkiOiJjZWMwNTRhMS1hMGZjLTQ2YTYtYWI2MS00MDJjOWY3ZjhlMzMiLCJzaWQiOiJ3cDJIbTlpMmkzbzFuUC04dThzSUsyQVZZendTaFgxOUhkcnJzaWdpMjNvIn0.O2kaoXLXvdqPku-zLmVaorHIVmASGacZP3tM9BhZppFoabVk5ylWrJoM49lPrfSxtFoWalksGmbqmfozI0KuNBBuGI_n5fOwpyL8Z2cg3LuNo8323-MX9a6H8SXsmiF9p1aqON66Vey8562g9sMlc_pwHtOxHGH2wY5aQhr0Adv4JLbiN28xL8s-IEsXXGUr7CLuG_Ivo6QCgL8Sb90ZZB22MkorQOzGK3UTRAB-aiBFE-RxZq8tm_qDWJeG7sOjVDlkWyDqOIjUZGzjJSc35zU7YG2kbV7jfOVyMXP9ITGvPBVfHYW0kzlIVf8vUerz30XFK0mjKS9xwxl5F_zizQ',
#         'Content-Type': 'application/json',
#         'Cookie': 'JSESSIONID=95E3BEB0A76DE086A325CCD1D289564C'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#
#     print(response.text)
