from app.services.price_monitor import PriceMonitorService

def main():
    """Запуск службы мониторинга"""
    try:
        service = PriceMonitorService()
        service.start_monitoring()
    except KeyboardInterrupt:
        print("\n🛑 Служба остановлена пользователем")
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")

if __name__ == "__main__":
    main()