# import requests
# import pkce
#
#
#
# def test_get_site():
#     session = requests.Session()
#     code_verifier = pkce.generate_code_verifier(length=128)
#     code_challenge = pkce.get_code_challenge(code_verifier)
#     code_challenge_method = pkce.get_code_challenge(code_verifier)
#     print("Code Verifier:", code_verifier)
#     print("Code Challenge:", code_challenge)
#     print("Code Challenge Method:", code_challenge_method)
#
#     auth_url = "http://127.0.0.1:9000/oauth2/authorize"
#     params = {
#         "response_type": "code",
#         "client_id": "client",
#         "scope": "openid",
#         "redirect_uri": "http://127.0.0.1:3000/authorized",
#         "code_challenge": code_challenge,
#         "code_challenge_method": code_challenge_method
#     }
#
#     response = session.get(auth_url, params=params)
#     assert response.status_code == 200
#     print("All session cookies:", session.cookies)
#
#     login_url = "http://127.0.0.1:9000/login"
#     payload = {
#         "_csrf": session.cookies.get("XSRF-TOKEN"),
#         "username": "qwerty",
#         "password": "123456"
#     }
#     headers = {
#         "Cookie": f"XSRF-TOKEN={session.cookies.get('XSRF-TOKEN')}, JSESSIONID={session.cookies.get('JSESSIONID')}"
#     }
#
#     response = session.post(login_url, data=payload, headers=headers)
#     print(response.status_code)
#     for resp in response.history:
#         print(resp.status_code, resp.url)

"""
В запросе http://127.0.0.1:9000/login статус 200, но я не вижу как в примере Дмитрия, что после этого запроса должно быть такой ответ
    // 302 Found -> http://127.0.0.1:3000/authorized?code=u8AbPxCWftqGEjpRhjk9ceOqI9IIInedEd-ac6eTgTYOyQheNHHmKyGDuf3uryafM5d2lQmtLbJBuxWw-pA-PH8SwKTe-cQbp93b3CB2NZucerT1nFmQMNGw-AvIcSsP
    // Auto Redirect -> GET http://127.0.0.1:3000/authorized?code=u8AbPxCWftqGEjpRhjk9ceOqI9IIInedEd-ac6eTgTYOyQheNHHmKyGDuf3uryafM5d2lQmtLbJBuxWw-pA-PH8SwKTe-cQbp93b3CB2NZucerT1nFmQMNGw-AvIcSsP
    // 200 OK


вот что я вижу в консоли
Code Verifier: uw7oOh7z8TodkNsCnX8fYArkKz0dLUZdTj76EBcZrs8YKmtgX-mv42GVwkHOmaOWYtBhex5pLtIkXdoXxbO_AR9Qqdj-ZByh-xVS7toreEfYIoxOLpuN67RUN3AUv2tb
Code Challenge: ocSdGYUjvROnzy8TjmRCpTSo4MOe1tqYsjI__PCY2Uo
Code Challenge Method: ocSdGYUjvROnzy8TjmRCpTSo4MOe1tqYsjI__PCY2Uo
All session cookies: <RequestsCookieJar[<Cookie JSESSIONID=C97AB8603F7FB9DD0C15A067DE27E9D2 for 127.0.0.1/>, <Cookie XSRF-TOKEN=09d59b3e-6e2f-4385-b15e-d494b261db7d for 127.0.0.1/>]>
200
302 http://127.0.0.1:9000/login

"""

#     # token_url = "http://auth.niffler.dc:9000/oauth2/token"
#     # token_payload = {
#     #     "code": code,
#     #     "redirect_uri": "http://127.0.0.1:3000/authorized",
#     #     "code_verifier": "sT2C2AF_Y_F_JrlfOItvCZOhm7sIF_ltCTF9_VLucB4",
#     #     "grant_type": "authorization_code",
#     #     "client_id": "client"
#     # }
#     # headers = {
#     #     "Authorization": "Basic Y2xpZW50OnNlY3JldA==",
#     #     "Content-Type": "application/x-www-form-urlencoded"
#     # }
#     #
#     # response = session.post(token_url, data=token_payload, headers=headers)
#     #
#     # # Перевірка отримання токену
#     # assert response.status_code == 200
#     # tokens = response.json()
#     # assert "access_token" in tokens
#     # assert "refresh_token" in tokens
#     #
#     # # Виведення отриманих токенів
#     # print("Access Token:", tokens["access_token"])
#     # print("Refresh Token:", tokens["refresh_token"])
#     # print("ID Token:", tokens["id_token"])




