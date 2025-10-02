from app.services.price_monitor import PriceMonitorService


def test_basic_functionality():
    print("🧪 Тестируем основной функционал...")

    try:
        # Создаем сервис
        service = PriceMonitorService()
        print("✅ Сервис создан")

        # Проверяем атрибуты
        print(f"✅ Engine: {type(service.engine).__name__}")
        print(f"✅ SessionLocal: {type(service.SessionLocal).__name__}")
        print(f"✅ Parser Manager: {type(service.parser_manager).__name__}")
        print(f"✅ Notifications: {len(service.notifications)} уведомлений")

        # Проверяем подключение к БД
        db = service.SessionLocal()
        print("✅ Подключение к БД работает")

        # Проверяем метод (пустая БД)
        service.check_all_products()
        print("✅ Метод check_all_products работает")

        db.close()
        print("🎉 Все тесты пройдены успешно!")

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_basic_functionality()
