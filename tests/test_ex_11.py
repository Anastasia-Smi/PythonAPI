import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions

def test_ex_11(self, BaseCase):
    data = {
        'email': 'vincotov@example.com',
        'password': '1234'
    }
    url = "https://playground.learnqa.ru/api/homework_cookie"
    response = requests.post(url, data)
    cookie = get_cookie(response, "auth_sid")
    print (cookie)

    Assertions.assert_json_value_by_name(
        response,
        "user_id",
        cookie,
        "Cookie is not available"
    )


