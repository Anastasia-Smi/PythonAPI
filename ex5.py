# Внутри него создадим переменную json_text.
# Значение этой переменной должно быть таким, как указано
# тут: https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37
# Наша задача с помощью библиотеки “json”,
# которую мы показывали на занятии, распарсить
# нашу переменную json_text и вывести текст второго сообщения с помощью функции print.

import requests
import json
string=json.loads('{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},' \
        '{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}')
print(string['messages'][1]['message'])