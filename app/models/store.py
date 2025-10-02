from sqlalchemy import Column, Integer, String, DateTime, Boolean, func, text
from app.core.database import Base

class Store(Base):
    """Модель магазина для мониторинга цен."""
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    url = Column(String(500), nullable=False)
    base_url = Column(String(200))
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(DateTime, onupdate=func.now)

    def __repr__(self):
        return f'<Store(name="{self.name}")>'
