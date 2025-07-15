from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings as app_settings

SQLALCHEMY_DATABASE_URI = app_settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_recycle=500, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_raw_db_connection():
    conn = engine.connect()
    try:
        yield conn
    finally:
        conn.close()