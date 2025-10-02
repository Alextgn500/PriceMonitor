from app.parsers.base_parser import BaseParser
from typing import Optional, Dict
import re
import asyncio
import requests
import traceback


class WildberriesParser(BaseParser):
    """Парсер для Wildberries"""

    def is_supported(self, url: str) -> bool:
        """Проверяет поддержку URL"""
        return "wildberries.ru" in url or "wb.ru" in url

    def parse_price(self, url: str) -> Optional[Dict]:
        """Парсит цену товара с Wildberries"""
        print(f"🔍 Начинаем парсинг URL: {url}")

        soup = self.get_page(url)
        if not soup:
            print("❌ Не удалось получить страницу")
            return None

        print("✅ Страница загружена, начинаем поиск данных")

        try:
            # Поиск названия товара
            name = "Товар Wildberries"
            name_selectors = [
                'h1[data-testid="product-title"]',
                ".product-page__title",
                "h1",
                ".goods-name",
            ]

            print("🔍 Ищем название товара...")
            for selector in name_selectors:
                name_element = soup.select_one(selector)
                print(f"  Селектор {selector}: {name_element is not None}")
                if name_element:
                    name = name_element.get_text(strip=True)
                    print(f"✅ Найдено название: {name}")
                    break

            # Поиск цены
            price = None
            price_selectors = [
                ".price-block__final-price",
                ".product-page__price-current",
                '[data-testid="price-current"]',
                ".price",
            ]

            print("🔍 Ищем цену...")
            for selector in price_selectors:
                price_element = soup.select_one(selector)
                print(f"  Селектор {selector}: {price_element is not None}")
                if price_element:
                    price_text = price_element.get_text(strip=True)
                    print(f"  Текст цены: '{price_text}'")
                    # Извлекаем числа
                    price_match = re.search(
                        r"(\d+(?:\s*\d+)*)",
                        price_text.replace(" ", "").replace("₽", ""),
                    )
                    if price_match:
                        price = float(price_match.group(1))
                        print(f"✅ Найдена цена: {price}")
                        break

            if price is None:
                print("❌ Цена не найдена")
                print("📄 Первые 500 символов страницы:")
                print(soup.get_text()[:500])
                return None

            result = {"name": name, "price": price, "available": True, "url": url}
            print(f"🎉 Результат: {result}")
            return result

        except (AttributeError, ValueError, TypeError, KeyError) as e:
            print(f"❌ Ошибка парсинга WB: {e}")
            print(traceback.format_exc())
            return None
        except requests.RequestException as e:
            print(f"❌ Ошибка сети при парсинге WB: {e}")
            return None

    async def parse(self, url: str) -> Optional[Dict]:
        """Async версия парсинга"""
        try:
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, self.parse_price, url)
            return result
        except (RuntimeError, asyncio.TimeoutError) as e:
            print(f"❌ Ошибка выполнения async парсинга: {e}")
            return None
