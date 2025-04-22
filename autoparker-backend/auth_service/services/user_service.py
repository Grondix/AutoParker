from sqlalchemy.orm import Session
from auth_service.models.user import User, Role, UserRole
from passlib.context import CryptContext
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_users(db: Session):
    return db.query(User).all()

def delete_user(db: Session, user_id: int):
    user = db.query(User).get(user_id)
    if user:
        db.delete(user)
        db.commit()
        return {"detail": "Uživatel smazán"}
    return {"detail": "Uživatel nenalezen"}

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if user and pwd_context.verify(password, user.hashed_password):
        return user
    return None

def assign_role(db: Session, user_id: int, role_name: str):
    role = db.query(Role).filter(Role.name == role_name).first()
    if not role:
        role = Role(name=role_name)
        db.add(role)
        db.commit()
        db.refresh(role)
    user_role = UserRole(user_id=user_id, role_id=role.id)
    db.add(user_role)
    db.commit()
    return {"detail": "Role přidána"}

def remove_role(db: Session, user_id: int, role_name: str):
    role = db.query(Role).filter(Role.name == role_name).first()
    if role:
        db.query(UserRole).filter_by(user_id=user_id, role_id=role.id).delete()
        db.commit()
    return {"detail": "Role odebrána"}

def create_admin_user(db: Session):
    existing = db.query(User).filter_by(username="admin").first()
    if existing:
        raise HTTPException(status_code=400, detail="Admin už existuje")

    hashed_password = pwd_context.hash("admin123")
    user = User(username="admin", hashed_password=hashed_password)

    admin_role = db.query(Role).filter_by(name="admin").first()
    if not admin_role:
        admin_role = Role(name="admin")
        db.add(admin_role)
        db.commit()
        db.refresh(admin_role)

    user.roles.append(admin_role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
