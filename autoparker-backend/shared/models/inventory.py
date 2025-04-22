from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from shared.models.base import Base
from datetime import datetime

class InventoryItem(Base):
    __tablename__ = "inventory_item"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    unit = Column(String)
    part_id = Column(Integer)

    logs = relationship("InventoryLog", back_populates="item")

class InventoryLog(Base):
    __tablename__ = "inventory_log"
    id = Column(Integer, primary_key=True)
    inventory_item_id = Column(Integer, ForeignKey("inventory_item.id"))
    change = Column(Integer)
    reason = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    item = relationship("InventoryItem", back_populates="logs")
