import sys
import os

# Добавляем текущую папку в путь
sys.path.insert(0, os.getcwd())

try:
    from app.models import Product, Store, PriceHistory

    print("✅ Модели импортированы успешно")
except ImportError as e:
    print(f"❌ Ошибка импорта моделей: {e}")

try:
    from app.parsers.parser_manager import ParserManager

    print("✅ ParserManager импортирован успешно")
except ImportError as e:
    print(f"❌ Ошибка импорта ParserManager: {e}")

print("🎯 Тест импортов завершен")
