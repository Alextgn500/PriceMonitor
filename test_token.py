import requests

token = ''
url = f'https://api.telegram.org/bot{token}/getMe'

try:
    response = requests.get(url)
    print(f'Статус: {response.status_code}')
    print(f'Ответ: {response.json()}')
except Exception as e:
    print(f'Ошибка: {e}')
