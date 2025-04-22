from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth_service.services.user_service import assign_role, remove_role
from shared.dependencies import get_db

router = APIRouter()

@router.post("/users/{user_id}/roles")
def assign_user_role(user_id: int, role: dict, db: Session = Depends(get_db)):
    return assign_role(db, user_id, role["role"])

@router.delete("/users/{user_id}/roles/{role}")
def remove_user_role(user_id: int, role: str, db: Session = Depends(get_db)):
    return remove_role(db, user_id, role)
