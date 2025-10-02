import random
from typing import Optional, Dict
from .base_parser import BaseParser

class MockParser(BaseParser):
    """Парсер-эмулятор для демонстрации работы системы"""
    
    def __init__(self):
        super().__init__()
        self.mock_products = {
            "iphone15": {
                "title": "iPhone 15 128GB Черный",
                "base_price": 89990,
                "store": "DNS"
            },
            "macbook": {
                "title": "MacBook Air 13 M2",
                "base_price": 134990,
                "store": "DNS" 
            },
            "airpods": {
                "title": "AirPods Pro 2-го поколения",
                "base_price": 24990,
                "store": "DNS"
            }
        }
    
    def is_supported(self, url: str) -> bool:
        return any(product in url.lower() for product in self.mock_products.keys())
    
    def parse_price(self, url: str) -> Optional[Dict]:
        """Эмулирует парсинг с реалистичными данными"""
        try:
            print(f"🔍 Эмулируем парсинг: {url}")
            
            # Определяем товар по URL
            product_key = None
            for key in self.mock_products.keys():
                if key in url.lower():
                    product_key = key
                    break
            
            if not product_key:
                return None
            
            product = self.mock_products[product_key]
            
            # Эмулируем изменение цены (±10%)
            price_variation = random.uniform(-0.1, 0.1)
            current_price = product["base_price"] * (1 + price_variation)
            current_price = round(current_price, -1)  # Округляем до десятков
            
            # Эмулируем доступность (95% времени в наличии)
            is_available = random.random() > 0.05
            
            return {
                'price': current_price,
                'is_available': is_available,
                'title': product['title']
            }
            
        except Exception as e:
            print(f"❌ Ошибка эмуляции: {e}")
            return None