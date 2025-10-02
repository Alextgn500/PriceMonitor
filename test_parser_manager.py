# Быстрая проверка parser_manager
import sys
sys.path.append('.')

try:
    from app.parsers.parser_manager import ParserManager
    
    manager = ParserManager()
    print(f" ParserManager загружен успешно")
    print(f" Доступные парсеры: {len(manager.parsers) if hasattr(manager, 'parsers') else 'неизвестно'}")
    
    # Проверим метод parse_product
    if hasattr(manager, 'parse_product'):
        print(f" Метод parse_product найден")
    else:
        print(f" Метод parse_product НЕ найден")
        
except ImportError as e:
    print(f" Ошибка импорта: {e}")
except Exception as e:
    print(f" Другая ошибка: {e}")
