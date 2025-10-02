from app.parsers.parser_manager import ParserManager

def test_mock_parser():
    manager = ParserManager()
    
    # Тестовые URL для эмуляции
    test_urls = [
        "https://mock-store.com/iphone15-128gb-black",
        "https://mock-store.com/macbook-air-m2",
        "https://mock-store.com/airpods-pro-gen2",
    ]
    
    print("🧪 Тестируем эмулятор парсера...")
    print(f"📋 Поддерживаемые домены: {manager.get_supported_domains()}")
    print()
    
    for url in test_urls:
        print(f"🔍 Парсим: {url}")
        result = manager.parse_price(url)
        
        if result:
            print(f"✅ Товар: {result['title']}")
            print(f"💰 Цена: {result['price']:,.0f}₽")
            print(f"📦 В наличии: {'Да' if result['is_available'] else 'Нет'}")
        else:
            print("❌ Товар не найден")
        print("-" * 50)

if __name__ == "__main__":
    test_mock_parser()
