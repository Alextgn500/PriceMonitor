from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class PriceHistory(Base):
    __tablename__ = "price_history"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    price = Column(Float, nullable=False)
    currency = Column(String(10), default="RUB")
    
    # Дополнительная информация
    is_available = Column(Boolean, default=True)
    discount_percentage = Column(Float)  # Процент скидки
    
    recorded_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Связь с продуктом
    product = relationship("Product", backref="price_history")
    
    def __repr__(self):
        return f"<PriceHistory(product_id={self.product_id}, price={self.price})>"
