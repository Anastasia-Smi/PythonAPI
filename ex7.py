import requests
url = " https://playground.learnqa.ru/ajax/api/compare_query_type"
#task1
response= requests.get(url)
print(response)

#task2
response_2= requests.head(url)
print(response_2)

#task3
response_3= requests.get(url, params = {"method": "GET"})
print(response_3)

#task4
list= ["GET", "PUT", "POST","DELETE"]


for m in list :
    response_4 = requests.get(url, params={"method": m}).text
    if (m!= list[0] and response_4 =='{"success":"!"}')\
                :print(f"Wrong param_value is {m} in response_4")


for m in list :
    response_5 = requests.put(url, data={"method":m}).text
    if (m!= list[1] and response_5 =='{"success":"!"}')\
                :print(f"Wrong param_value is {m} in response_5")


for m in list :
    response_6 = requests.post(url, data={"method":m}).text
    if (m != list[2] and response_6 == '{"success":"!"}') \
            :print(f"Wrong param_value is {m} in response_6")

for m in list :
    response_7 = requests.delete(url, data={"method":m}).text
    if (m != list[3] and response_7 == '{"success":"!"}') \
            : print(f"Wrong param_value is {m} in response_7")