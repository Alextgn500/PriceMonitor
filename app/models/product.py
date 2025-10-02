from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text
from datetime import datetime, timezone
from app.core.database import Base


# Функция для текущего времени
def utc_now():
    return datetime.now(timezone.utc)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(500), nullable=False)
    url = Column(Text, nullable=False)
    shop_name = Column(String(100), nullable=False)
    category = Column(String(100))

    # Текущая цена
    current_price = Column(Float)
    currency = Column(String(10), default="RUB")

    # Настройки отслеживания
    is_active = Column(Boolean, default=True)
    target_price = Column(Float)  # Желаемая цена для уведомлений

    # Технические поля
    created_at = Column(DateTime(timezone=True), default=utc_now)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)
    last_checked = Column(DateTime(timezone=True))

    def __repr__(self):
        return f"<Product(name='{self.name}', current_price={self.current_price})>"
