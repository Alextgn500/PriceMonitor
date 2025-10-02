from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Store, Product, PriceHistory
from app.parsers.parser_manager import ParserManager

# Настройка БД
engine = create_engine('sqlite:///./price_monitor.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_full_system():
    db = SessionLocal()
    manager = ParserManager()
    
    try:
        # Создаем тестовый магазин
        store = Store(name="Mock Store", url="https://mock-store.com")
        db.add(store)
        db.commit()
        
        # Создаем товары для мониторинга
        products_data = [
            {
                "name": "iPhone 15 128GB", 
                "url": "https://mock-store.com/iphone15-128gb-black",
                "target_price": 80000.0
            },
            {
                "name": "MacBook Air M2", 
                "url": "https://mock-store.com/macbook-air-m2",
                "target_price": 120000.0
            }
        ]
        
        print("🏪 Создан магазин:", store.name)
        print("=" * 60)
        
        for product_data in products_data:
            # Парсим актуальную цену
            price_info = manager.parse_price(product_data["url"])
            
            if price_info:
                # Создаем товар
                product = Product(
                    name=product_data["name"],
                    url=product_data["url"],
                    store_id=store.id,
                    current_price=price_info["price"],
                    target_price=product_data["target_price"]
                )
                db.add(product)
                db.commit()
                
                # Добавляем в историю цен
                history = PriceHistory(
                    product_id=product.id,
                    price=price_info["price"],
                    is_available=price_info["is_available"]
                )
                db.add(history)
                db.commit()
                
                # Проверяем достижение целевой цены
                price_dropped = price_info["price"] <= product_data["target_price"]
                status = "🎯 ЦЕЛЬ ДОСТИГНУТА!" if price_dropped else "⏳ Ждем снижения"
                
                print(f"📱 {product.name}")
                print(f"💰 Текущая цена: {price_info['price']:,.0f}₽")
                print(f"🎯 Целевая цена: {product.target_price:,.0f}₽")
                print(f"📊 Статус: {status}")
                print(f"📦 В наличии: {'Да' if price_info['is_available'] else 'Нет'}")
                print("-" * 60)
        
        print("✅ Полная система работает!")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_full_system()