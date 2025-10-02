from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Используем правильное имя атрибута
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Создание всех таблиц"""
    Base.metadata.create_all(bind=engine)

def init_db():
    """Инициализация базы данных"""
    try:
        # Импортируем модели чтобы SQLAlchemy их увидел
        from app.models.user import User
        from app.models.product import Product
        
        # Создаем таблицы
        Base.metadata.create_all(bind=engine)
        print(" База данных инициализирована")
        return True
    except Exception as e:
        print(f" Ошибка инициализации БД: {e}")
        return False
