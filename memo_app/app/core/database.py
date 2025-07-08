from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Settings


SQLALCHEMY_DATABASE_URI = Settings.database_uri

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_recycle=500, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal() # ORM 객체
    try:
        yield db
    finally:
        db.close()

def get_raw_db_connection(): # DB 연결 객체를 직접 제공
    conn = engine.connect()
    try:
        yield conn
    finally:
        conn.close()
