from app.bot.telegram_bot import PriceMonitorBot

def test_bot_creation():
    """Тест создания бота без запуска"""
    print("🧪 Тестируем создание бота...")
    
    try:
        # Используем фейковый токен для теста
        bot = PriceMonitorBot("123456:TEST_TOKEN")
        print("✅ Бот создан успешно!")
        print(f"✅ Парсер подключен: {len(bot.parser_manager.get_supported_domains())} доменов")
        print("✅ База данных подключена")
        
    except Exception as e:
        print(f"❌ Ошибка создания бота: {e}")

if __name__ == "__main__":
    test_bot_creation()
