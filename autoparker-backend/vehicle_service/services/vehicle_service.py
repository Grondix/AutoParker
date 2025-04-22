from sqlalchemy.orm import Session
from shared.models.vehicle import Vehicle

def get_vehicles(db: Session):
    return db.query(Vehicle).all()

def create_vehicle(db: Session, data: dict):
    v = Vehicle(**data)
    db.add(v)
    db.commit()
    db.refresh(v)
    return v
