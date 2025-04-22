from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from shared.dependencies import get_db
from vehicle_service.services.vehicle_service import get_vehicles, create_vehicle

router = APIRouter()

@router.get("")
def list_vehicles(db: Session = Depends(get_db)):
    return get_vehicles(db)

@router.post("")
def create_vehicle_entry(data: dict, db: Session = Depends(get_db)):
    return create_vehicle(db, data)
