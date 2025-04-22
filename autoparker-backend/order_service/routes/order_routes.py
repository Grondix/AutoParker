from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from shared.dependencies import get_db, get_current_user
from shared.models.order import Order, OrderItem
from shared.models.user import User
from shared.schemas.order_schemas import OrderCreate, OrderUpdate

router = APIRouter()

@router.post("/", response_model=Order)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(
        title=order.title,
        description=order.description,
        status="nová",
        user_id=order.user_id
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/", response_model=list[Order])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@router.get("/my", response_model=list[Order])
def get_my_orders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Order).filter(Order.user_id == current_user.id).all()

@router.get("/{order_id}", response_model=Order)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Zakázka nenalezena")
    return order

@router.put("/{order_id}", response_model=Order)
def update_order(order_id: int, update_data: OrderUpdate, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Zakázka nenalezena")

    for attr, value in update_data.dict(exclude_unset=True).items():
        setattr(order, attr, value)

    db.commit()
    db.refresh(order)
    return order

@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Zakázka nenalezena")

    db.delete(order)
    db.commit()
    return {"detail": "Zakázka smazána"}
