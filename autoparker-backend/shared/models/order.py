from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from shared.models.base import Base
from datetime import datetime

class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, default="nová")
    user_id = Column(Integer)
    vehicle_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_item"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    order_id = Column(Integer, ForeignKey("order.id"))

    order = relationship("Order", back_populates="items")
