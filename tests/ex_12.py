import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions

def test_ex_11(self, BaseCase):

    url = "https://playground.learnqa.ru/api/homework_cookie"
    response = requests.get(url)
    a = print(response.headers)
    assert (a in response.headers)