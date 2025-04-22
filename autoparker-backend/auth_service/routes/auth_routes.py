from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from shared.dependencies import get_db
from auth_service.utils.token import create_access_token
from auth_service.services.user_service import authenticate_user, create_admin_user

router = APIRouter()

@router.post("/login", tags=["Auth"])
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Nesprávné přihlašovací údaje")
    token = create_access_token(data={"sub": user.username})
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "username": user.username,
            "roles": [r.role.name for r in user.roles]
        }
    }

@router.post("/create-admin", tags=["Auth"])
def create_admin(db: Session = Depends(get_db)):
    try:
        user = create_admin_user(db)
        return {"message": "Admin účet vytvořen", "username": user.username}
    except HTTPException as e:
        raise e
