import requests
from json.decoder import JSONDecodeError

response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)


payload= {"name":"User"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.text)

response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
parsed_response_text= response.json()
print(parsed_response_text["answer"])

response = requests.get("https://playground.learnqa.ru/api/get_text")

print(response.text)
try:
    parsed_response_text= response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Respons is not JSON format")


response = requests.get("https://playground.learnqa.ru/api/check_type", data={"param1":"value1"})
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response= response.history[0]
second_response=response
print(first_response.url)

#cookies
payload = {"login":"secret_login", "password":"secret_pass"}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data= payload)
print(response.text)
print(response.status_code)
print(dict(response.cookies))

payload = {"login":"secret_login", "password":"secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data= payload)

cookie_value= response1.cookies.get('auth_cookie')
cookies={'auth_cookie':cookie_value}

response2 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", cookies= cookies)
print(response.text)
print(response2.text)
print(response.status_code)
print(dict(response.cookies))