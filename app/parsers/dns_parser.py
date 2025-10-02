import re
from typing import Optional, Dict
from .base_parser import BaseParser

class DNSParser(BaseParser):
    def is_supported(self, url: str) -> bool:
        return 'dns-shop.ru' in url
    
    def parse_price(self, url: str) -> Optional[Dict]:
        soup = self.get_page(url)
        if not soup:
            return None
        
        try:
            # Ищем цену (может быть в разных местах)
            price_selectors = [
                '.product-buy__price',
                '.price-current__value',
                '[data-role="price"]',
                '.product-card-top__price-current'
            ]
            
            price_text = None
            for selector in price_selectors:
                price_element = soup.select_one(selector)
                if price_element:
                    price_text = price_element.get_text().strip()
                    break
            
            if not price_text:
                return None
            
            # Извлекаем числовое значение цены
            price_match = re.search(r'(\d[\d\s]*)', price_text.replace(' ', ''))
            if price_match:
                price = float(price_match.group(1).replace(' ', ''))
                
                # Проверяем доступность
                is_available = not bool(soup.select_one('.product-buy__unavailable, .out-of-stock'))
                
                return {
                    'price': price,
                    'is_available': is_available,
                    'title': soup.select_one('h1').get_text().strip() if soup.select_one('h1') else 'Товар'
                }
                
        except Exception as e:
            print(f"❌ Ошибка парсинга DNS: {e}")
        
        return None