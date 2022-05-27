import requests
import json
import time

#create task
url="https://playground.learnqa.ru/ajax/api/longtime_job"
response = requests.get(url).text
token_value=json.loads(response)

#2) делал один запрос с token ДО того,
# как задача готова, убеждался в правильности поля status
response_1 = requests.get(url, params={"token":token_value})
print(response_1.text)
assert(response_1.status_code == 200)

#3) ждал нужное количество секунд с помощью функции
# time.sleep() - для этого надо сделать import time
time.sleep(3)

#4) делал бы один запрос c token ПОСЛЕ того,
# как задача готова, убеждался в правильности поля status и наличии поля result
response_2 = requests.get(url, params={"token":token_value})
assert(response_2.status_code == 200)
