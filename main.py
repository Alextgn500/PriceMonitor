from app.core.database import init_db

def main():
    # Инициализируем базу данных
    init_db()
    print(" База данных инициализирована!")
    print(" Проект готов к использованию!")
    print(" Для запуска бота: python app/bot/telegram_bot.py")

if __name__ == "__main__":
    main()
