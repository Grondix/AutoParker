from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from inventory_service.services.inventory_service import (
    get_items, create_item, update_item, delete_item,
    get_logs, move_item
)
from shared.dependencies import get_db

router = APIRouter()

@router.get("")
def list_inventory(db: Session = Depends(get_db)):
    return get_items(db)

@router.post("")
def create(data: dict, db: Session = Depends(get_db)):
    return create_item(db, data)

@router.put("/{item_id}")
def update(item_id: int, data: dict, db: Session = Depends(get_db)):
    return update_item(db, item_id, data)

@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return delete_item(db, item_id)

@router.get("/{item_id}/logs")
def logs(item_id: int, db: Session = Depends(get_db)):
    return get_logs(db, item_id)

@router.post("/{item_id}/move")
def move(item_id: int, data: dict, db: Session = Depends(get_db)):
    return move_item(db, item_id, data["change"], data["reason"])
