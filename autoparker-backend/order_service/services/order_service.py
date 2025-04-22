from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from shared.dependencies import get_db, get_current_user
from shared.schemas.order_schemas import OrderCreate
from shared.models.user import User
from order_service.services import order_service

router = APIRouter()

@router.get("/my", summary="Získat zakázky aktuálního uživatele")
def get_my_orders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    orders = order_service.get_user_orders(db, user_id=current_user.id)
    return orders

@router.get("/{order_id}", summary="Získat detail zakázky")
def get_order_detail(order_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    order = order_service.get_order_detail(db, order_id=order_id)
    if not order or order.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Zakázka nenalezena")
    return order

@router.post("/", summary="Vytvořit novou zakázku")
def create_order(order_data: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return order_service.create_order(db, order_data, user_id=current_user.id)
