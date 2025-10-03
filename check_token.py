import requests

TOKEN = ""
url = f"https://api.telegram.org/bot{TOKEN}/getMe"

try:
    response = requests.get(url)
    print(f"Статус код: {response.status_code}")
    print(f"Ответ: {response.json()}")
except Exception as e:
    print(f"Ошибка: {e}")
