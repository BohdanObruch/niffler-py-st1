import requests
import os


def registration_with_api(username, password):
    url = os.getenv("REGISTRATION_URL")
    session = requests.Session()

    session.get(url)

    payload = {
        "_csrf": session.cookies.get("XSRF-TOKEN"),
        "username": username,
        "password": password,
        "passwordSubmit": password
    }

    headers = {
        'Cookie': f'XSRF-TOKEN={session.cookies.get("XSRF-TOKEN")}'
    }

    response = session.post(url, headers=headers, data=payload)
    return response
