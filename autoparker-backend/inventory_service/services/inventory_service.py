from sqlalchemy.orm import Session
from shared.models.inventory import InventoryItem, InventoryLog
from datetime import datetime

def get_items(db: Session):
    return db.query(InventoryItem).all()

def create_item(db: Session, data: dict):
    item = InventoryItem(**data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def update_item(db: Session, item_id: int, data: dict):
    item = db.query(InventoryItem).get(item_id)
    for k, v in data.items():
        setattr(item, k, v)
    db.commit()
    return item

def delete_item(db: Session, item_id: int):
    db.query(InventoryItem).filter_by(id=item_id).delete()
    db.commit()
    return {"detail": "Položka smazána"}

def get_logs(db: Session, item_id: int):
    return db.query(InventoryLog).filter_by(inventory_item_id=item_id).all()

def move_item(db: Session, item_id: int, change: int, reason: str):
    item = db.query(InventoryItem).get(item_id)
    item.quantity += change
    log = InventoryLog(
        inventory_item_id=item_id,
        change=change,
        reason=reason,
        created_at=datetime.utcnow()
    )
    db.add(log)
    db.commit()
    return {"detail": "Změna provedena"}
