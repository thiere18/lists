from sqlalchemy import create_engine
from logging import raiseExceptions
import time

from random import randrange
import psycopg2 as psy
from psycopg2.extras import RealDictCursor
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings as st

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@db:5432/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
