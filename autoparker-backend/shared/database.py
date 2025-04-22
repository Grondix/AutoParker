from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from dotenv import load_dotenv
import os

from shared.models.base import Base

# Načti proměnné z .env souboru
load_dotenv()

DATABASE_URL = (
    f"postgresql://{getenv('POSTGRES_USER')}:{getenv('POSTGRES_PASSWORD')}"
    f"@{getenv('POSTGRES_HOST')}:{getenv('POSTGRES_PORT')}/{getenv('POSTGRES_DB')}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)
