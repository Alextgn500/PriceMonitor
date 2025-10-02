"""Модуль управления парсерами интернет-магазинов."""

from typing import Optional, Dict
from abc import ABC, abstractmethod
import asyncio


class BaseParser(ABC):
    """Базовый класс для всех парсеров"""

    @abstractmethod
    async def parse(self, url: str) -> Optional[Dict]:
        """Парсит товар по URL"""
        pass


class WildberriesParser(BaseParser):
    """Парсер для Wildberries"""
    
    async def parse(self, url: str) -> Optional[Dict]:
        try:
            # Пока заглушка - потом добавим реальный парсинг
            return {
                'name': 'Товар с Wildberries',
                'price': 1500.0,
                'is_available': True
            }
        except (ValueError, AttributeError, KeyError) as e:
            print(f"Ошибка WB парсера: {e}")
            return None


class DNSParser(BaseParser):
    """Парсер для DNS"""
  
    async def parse(self, url: str) -> Optional[Dict]:
        try:
            return {
                'name': 'Товар с DNS',
                'price': 2500.0,
                'is_available': True
            }
        except (ValueError, AttributeError, KeyError) as e:
            print(f"Ошибка DNS парсера: {e}")
            return None


class OzonParser(BaseParser):
    """Парсер для Ozon"""
    
    async def parse(self, url: str) -> Optional[Dict]:
        try:
            return {
                'name': 'Товар с Ozon',
                'price': 1200.0,
                'is_available': True
            }
        except (ValueError, AttributeError, KeyError) as e:
            print(f"Ошибка Ozon парсера: {e}")
            return None


class ParserManager:
    """Менеджер для управления парсерами"""

    def __init__(self):  # Исправлено: было init
        # Словарь парсеров по доменам
        self.parsers = {
            'wildberries.ru': WildberriesParser(),
            'dns-shop.ru': DNSParser(),
            'ozon.ru': OzonParser(),
        }

    def is_supported_url(self, url: str) -> bool:
        """Проверяет, поддерживается ли URL"""
        if not isinstance(url, str):
            return False

        try:
            url_lower = url.lower()
            for domain in self.parsers:
                if domain in url_lower:
                    return True
            return False
        except AttributeError:
            return False

    def get_parser_for_url(self, url: str):
        """Возвращает подходящий парсер для URL"""
        if not isinstance(url, str):
            return None

        try:
            url_lower = url.lower()
            for domain, parser in self.parsers.items():
                if domain in url_lower:
                    return parser
            return None
        except AttributeError:
            return None

    # Добавляем метод parse_price для совместимости
    def parse_price(self, url: str) -> Optional[Dict]:
        """Синхронная обертка для парсинга цены товара"""
        try:
            # Запускаем асинхронный метод в синхронном коде
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                result = loop.run_until_complete(self.parse_product(url))
                return result
            finally:
                loop.close()
        except Exception as e:
            print(f"Ошибка при парсинге цены {url}: {e}")
            return None

    async def parse_product(self, url: str) -> Optional[Dict]:
        """Парсит информацию о товаре по URL"""
        try:
            parser = self.get_parser_for_url(url)
            if not parser:   
                print(f"Парсер для URL {url} не найден")
                return None

            result = await parser.parse(url)

            if result and isinstance(result, dict):
                return {
                    'name': result.get('name', 'Товар'),
                    'price': float(result.get('price', 0)),  # Приводим к float
                    'store': self._get_store_name_from_url(url),
                    'is_available': result.get('is_available', True)  # Исправлено: было available
                }
            return None

        except (ValueError, AttributeError, KeyError, TypeError) as e:
            print(f"Ошибка при парсинге {url}: {e}")
            return None

    def _get_store_name_from_url(self, url: str) -> str:
        """Определяет название магазина по URL"""
        if not isinstance(url, str):
            return 'Неизвестный магазин'
        
        url_lower = url.lower()
        if 'wildberries.ru' in url_lower:
            return 'Wildberries'
        elif 'dns-shop.ru' in url_lower:
            return 'DNS'
        elif 'ozon.ru' in url_lower:
            return 'Ozon'
        else:
            return 'Неизвестный магазин'
