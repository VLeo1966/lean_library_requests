import requests
import pprint

# URL API для отправки POST-запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Данные для отправки в виде словаря
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправка POST-запроса с данными
response = requests.post(url, json=data)

# Вывод статус-кода ответа
print("Status Code:", response.status_code)

# Вывод содержимого ответа в формате JSON
response_data = response.json()
pprint.pprint(response_data)
