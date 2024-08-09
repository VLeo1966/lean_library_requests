import requests
import pprint

# URL API GitHub для поиска репозиториев
url = "https://api.github.com/search/repositories"

# Параметры запроса
params = {
    'q': 'language:html'  # Поиск репозиториев с кодом на языке HTML
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Распечатываем статус-код ответа
print("Status Code:", response.status_code)

# Распечатываем содержимое ответа в формате JSON с использованием pprint
json_response = response.json()
pprint.pprint(json_response)

