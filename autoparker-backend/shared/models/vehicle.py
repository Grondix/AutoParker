from sqlalchemy import Column, Integer, String
from shared.models.base import Base

class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True)
    license_plate = Column(String, unique=True, nullable=False)
    model = Column(String)
