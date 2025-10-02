import asyncio
from app.parsers.parser_manager import ParserManager

class PriceMonitorService:
    def __init__(self):
        self.parser_manager = ParserManager()
        print(f" Инициализирован сервис с ParserManager")

    async def check_price(self, url: str) -> dict:
        """Проверяем цену товара по URL"""
        try:
            print(f" Начинаем парсинг URL: {url}")
            
            # ИСПОЛЬЗУЕМ parse_product из parser_manager
            print(f" Вызываем parser_manager.parse_product()")
            product_data = await self.parser_manager.parse_product(url)
            
            if product_data is None:
                return {
                    'success': False,
                    'error': 'Не удалось получить данные о товаре или магазин не поддерживается'
                }
            
            # Приводим данные к нужному формату
            result_data = {
                'name': product_data.get('name', 'Товар без названия'),
                'price': str(product_data.get('price', 0)),  # Конвертируем обратно в строку
                'available': product_data.get('is_available', True),
                'store': product_data.get('store', 'Неизвестный магазин'),
                'image_url': None
            }
            
            print(f" Успешно получены данные: {result_data}")
            
            return {
                'success': True,
                'data': result_data
            }
            
        except Exception as e:
            print(f" Ошибка в check_price: {e}")
            import traceback
            traceback.print_exc()
            return {
                'success': False,
                'error': f'Внутренняя ошибка: {str(e)}'
            }
