from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth_service.services.user_service import get_users, delete_user
from shared.dependencies import get_db

router = APIRouter()

@router.get("")
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.delete("/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)
