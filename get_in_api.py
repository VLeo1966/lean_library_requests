import requests
import pprint

# URL API для получения постов
url = "https://jsonplaceholder.typicode.com/posts"

# Параметры запроса (фильтрация по userId)
params = {
    'userId': 1  # Фильтруем посты по userId, равному 1
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Проверка статуса ответа
if response.status_code == 200:
    # Получаем и выводим данные в формате JSON
    posts = response.json()
    pprint.pprint(posts)
else:
    print("Failed to retrieve data. Status code:", response.status_code)
