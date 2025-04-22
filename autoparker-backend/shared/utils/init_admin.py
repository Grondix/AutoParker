from sqlalchemy.orm import Session
from shared.database import engine
from auth_service.models.user import User
from auth_service.services.user_service import pwd_context
from shared.models.base import Base

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

def create_initial_admin():
    with Session(engine) as db:
        if not db.query(User).filter_by(email="admin@autoparker.cz").first():
            admin = User(
                username="admin",
                email="admin@autoparker.cz",
                hashed_password=pwd_context.hash("admin123"),
                is_active=True
            )
            db.add(admin)
            db.commit()
