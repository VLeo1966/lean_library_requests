import requests

img = 'https://emis.ru/upload/iblock/893/220506_Haupa_850x850.jpg'

response = requests.get(img)

with open('test.jpg', 'wb') as file:
    file.write(response.content)