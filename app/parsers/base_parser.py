import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import time
import random
from typing import Optional, Dict


class BaseParser(ABC):
    def __init__(self):  # ← ИСПРАВЛЕНО: было init, должно быть __init__
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Accept-Encoding": "gzip, deflate, br",
                "DNT": "1",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
            }
        )

    def get_page(self, url: str) -> Optional[BeautifulSoup]:
        """Получает HTML страницу"""
        try:
            print(f"🌐 Запрос к: {url}")

            # Случайная задержка между запросами
            delay = random.uniform(1, 3)
            print(f"⏱️ Задержка: {delay:.1f}с")
            time.sleep(delay)

            response = self.session.get(url, timeout=15)
            print(f"📊 Статус ответа: {response.status_code}")

            if response.status_code == 200:
                print("✅ Страница загружена успешно")
                return BeautifulSoup(response.content, "html.parser")
            elif response.status_code in [403, 429, 498]:
                print(f"🚫 Заблокировано (статус {response.status_code})")
                return None
            else:
                response.raise_for_status()

        except Exception as e:
            print(f"❌ Ошибка загрузки страницы {url}: {e}")
            return None

    @abstractmethod
    def parse_price(self, url: str) -> Optional[Dict]:
        """Парсит цену товара"""
        pass

    @abstractmethod
    def is_supported(self, url: str) -> bool:
        """Проверяет, поддерживается ли данный URL"""
        pass
