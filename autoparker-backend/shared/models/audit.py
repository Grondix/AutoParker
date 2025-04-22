from sqlalchemy import Column, Integer, String, DateTime
from shared.models.base import Base
from datetime import datetime

class AuditLog(Base):
    __tablename__ = "audit_log"
    id = Column(Integer, primary_key=True)
    entity = Column(String)
    entity_id = Column(Integer)
    action = Column(String)
    user = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    changes = Column(String)
