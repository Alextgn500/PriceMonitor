                                                   О проекте

PriceMonitor — это MVP-проект системы мониторинга цен, демонстрирующий полнофункциональный интерфейс 
без реального парсинга сайтов. Проект использует заранее подготовленные данные для имитации работы парсеров, 
что позволяет показать все возможности системы и взаимодействие компонентов.

                                                 Основные возможности
— Мониторинг цен товаров из различных источников
— REST API для управления товарами и получения данных о ценах
— Фоновая обработка задач с помощью Celery
— Веб-интерфейс для управления системой
— Telegram бот для уведомлений (опционально)
— База данных с миграциями

                                                  Технический стек
— Backend: FastAPI, SQLAlchemy, Alembic
— Фоновые задачи: Celery, Redis
— Парсинг: Scrapy, Selenium, BeautifulSoup4, Requests
— База данных: SQLite (по умолчанию), PostgreSQL (в продакшене)
— API документация: OpenAPI/Swagger
— Telegram бот: aiogram

                                                  Структура проекта


PriceMonitor/
├── app/                    # Основное FastAPI приложение
│   ├── main.py            # Точка входа приложения
│   ├── config.py          # Конфигурация
│   ├── models/            # SQLAlchemy модели
│   ├── routers/           # API роуты
│   ├── schemas/           # Pydantic схемы
│   └── services/          # Бизнес-логика
├── parsers/               # Парсеры (MVP с фейковыми данными)
│   ├── base_parser.py     # Базовый класс парсера
│   ├── fixtures.py        # Тестовые данные
│   └── implementations/   # Конкретные парсеры
├── db/                    # База данных
│   ├── database.py        # Настройка подключения
│   └── migrations/        # Alembic миграции
├── tasks/                 # Celery задачи
│   ├── worker.py          # Celery воркер
│   └── scheduler.py       # Планировщик задач
├── bot/                   # Telegram бот (опционально)
│   ├── handlers/          # Обработчики команд
│   └── main.py           # Запуск бота
├── scripts/               # Вспомогательные скрипты
│   ├── init_db.py        # Инициализация БД
│   └── run_dev.py        # Запуск в режиме разработки
├── tests/                 # Тесты
├── static/               # Статические файлы
├── templates/            # HTML шаблоны
├── requirements.txt      # Python зависимости
├── docker-compose.yml    # Docker Compose конфигурация
├── Dockerfile           # Docker образ
├── alembic.ini          # Конфигурация Alembic
├── .env.example         # Пример переменных окружения
└── README.md           # Документация проекта


                                             Быстрый старт

1. Клонирование репозитория
    bash
git clone https://github.com/lextgn500/PriceMonitor.git
cd PriceMonitor


2. Настройка окружения

Локальная установка:
    bash
# Создание виртуального окружения
python -m venv venv

# Активация (Linux/macOS)
source venv/bin/activate

# Активация (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Установка зависимостей
pip install -r requirements.txt

Docker (рекомендуется):
    bash
# Запуск всех сервисов
docker-compose up -d

# Просмотр логов
docker-compose logs -f


3. Настройка конфигурации**
    bash
# Копирование примера конфигурации
cp .env.example .env

# Редактирование переменных окружения
nano .env

4. Инициализация базы данных**
    bash
# Применение миграций
alembic upgrade head

# Загрузка тестовых данных (опционально)
python scripts/init_db.py

5. Запуск приложения

Режим разработки:
    bash
# FastAPI сервер
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Celery воркер (в отдельном терминале)
celery -A tasks.worker worker --loglevel=info

# Telegram бот (опционально, в отдельном терминале)
python bot/main.py

Доступ к приложению:
— Веб-интерфейс: http://localhost:8000
— API документация: http://localhost:8000/docs
— Альтернативная документация: http://localhost:8000/redoc

                                              Конфигурация

Основные переменные окружения (.env файл):

    bash
# База данных
DATABASE_URL=sqlite:///./price_monitor.db
# Для PostgreSQL: postgresql://user:password@localhost/price_monitor

# Redis для Celery
REDIS_URL=redis://localhost:6379/0

# Безопасность
SECRET_KEY=your-secret-key-here
DEBUG=true

# Telegram бот (опционально)
TELEGRAM_BOT_TOKEN=bot-token
TELEGRAM_ADMIN_ID=admin-id

# Настройки парсинга
PARSERDELAYMIN=1
PARSERDELAYMAX=5
USERAGENT=PriceMonitor/1.0

# Уведомления
EMAILSMTPHOST=smtp.gmail.com
EMAILSMTPPORT=587
EMAILUSERNAME=your-email@gmail.com
EMAILPASSWORD=your-app-password


                                             API Endpoints

Товары:
— `GET /api/v1/products` — список всех товаров
— `POST /api/v1/products` — добавить новый товар
— `GET /api/v1/products/{product_id}` — получить товар по ID
— `PUT /api/v1/products/{product_id}` — обновить товар
— `DELETE /api/v1/products/{product_id}` — удалить товар

Цены:
— `GET /api/v1/prices` — история цен
— `GET /api/v1/prices/current` — текущие цены всех товаров
— `GET /api/v1/products/{product_id}/prices` — история цен товара

Парсеры:
— `POST /api/v1/parsers/run` — запустить парсинг вручную
— `GET /api/v1/parsers/status` — статус парсеров
— `GET /api/v1/parsers/logs` — логи парсинга

Статистика:
— `GET /api/v1/stats/summary` — общая статистика
— `GET /api/v1/stats/trends` — тренды цен

                                               Примеры запросов


Добавление товара:

    bash
curl -X POST "http://localhost:8000/api/v1/products" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "iPhone 15 Pro",
       "url": "https://example-shop.com/iphone-15-pro",
       "targetprice": 999.99,
       "currency": "USD",
       "parsertype": "exampleparser"
     }'

Получение текущих цен:
    bash
curl "http://localhost:8000/api/v1/prices/current"

                                                Примеры ответов API

Товар:
    json
{
  "id": 1,
  "name": "iPhone 15 Pro",
  "url": "https://example-shop.com/iphone-15-pro",
  "targetprice": 999.99,
  "currentprice": 1099.99,
  "currency": "USD",
  "parsertype": "exampleparser",
  "isactive": true,
  "createdat": "2025-09-15T10:30:00Z",
  "updatedat": "2025-09-15T18:45:00Z",
  "lastchecked": "2025-09-15T18:45:00Z"
}


                                                  История цен:
    json
{
  "productid": 1,
  "prices": 
    {
      "price": 1099.99,
      "currency": "USD",
      "timestamp": "2025-09-15T18:45:00Z",
      "source": "example_parser",
      "is_available": true
    }
  ,
  "statistics": {
    "minprice": 999.99,
    "maxprice": 1099.99,
    "avgprice": 1049.99,
    "pricechange24h": -50.00,
    "pricechangepercent": -4.35
  }
}


                                             Работа с парсерами (MVP)

В MVP версии парсеры возвращают заранее подготовленные данные из parsers/fixtures.py. Это позволяет:

1. Демонстрировать функциональность без настройки реальных парсеров
2. Тестировать интеграцию между компонентами системы
3. Показывать различные сценарии (изменения цен, недоступность товаров)

                                           Настройка тестовых данных:
    python
# parsers/fixtures.py
MOCKPRODUCTS = 
    {
        "name": "iPhone 15 Pro",
        "price": 1099.99,
        "currency": "USD",
        "availability": True,
        "price_history": [1199.99, 1149.99, 1099.99
    },
    # ... другие товары
]


                                                 База данных и миграции

Создание новой миграции:
    bash
alembic revision --autogenerate -m "Описание изменений"


Применение миграций:
    bash
# Применить все миграции
alembic upgrade head


# Откатить последнюю миграцию
alembic downgrade -1

# Посмотреть текущую версию
alembic current


                                                   Мониторинг и логирование

Просмотр логов:
bash
# Логи FastAPI
tail -f logs/app.log

# Логи Celery
tail -f logs/celery.log

# Логи парсеров
tail -f logs/parsers.log


Метрики производительности:
— Количество успешных/неудачных парсингов
— Время выполнения задач
— Статистика изменений цен
— Активность пользователей API

                                                       Развертывание

Docker Compose (продакшен):
yaml
# docker-compose.prod.yml
version: '3.8'
services:
  web:
    build: .
    environment:
      - DATABASEURL=postgresql://user:pass@db:5432/pricemonitor
      - REDISURL=redis://redis:6379/0
    dependson:
      - db
      - redis

  db:
    image: postgres:15
    environment:
      POSTGRESDB: pricemonitor
      POSTGRESUSER: user
      POSTGRESPASSWORD: password

  redis:
     image: redis:7-alpine

  worker:
    build: .
    command: celery -A tasks.worker worker --loglevel=info
    depends_on:
      - redis
      - db


                                                    Тестирование

Запуск тестов:
    bash
# Все тесты
pytest

# Тесты с покрытием
pytest --cov=app tests/

# Только API тесты
pytest tests/test_api.py

# Только тесты парсеров
pytest tests/test_parsers.py


                                                   Roadmap развития

Следующие версии:
1. "v1.0" — Реальные парсеры для популярных магазинов
2. "v1.1" — Система уведомлений (email, Telegram, webhook)
3. "v1.2" — Веб-интерфейс для управления
4. "v1.3" — Мобильное приложение
5. "v2.0" — Машинное обучение для прогнозирования цен
