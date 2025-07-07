from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from sqlalchemy.ext.declarative import declarative_base 

DB_URL = 'mysql+pymysql://myuser:mypassword@localhost:33066/mydb'


Base = declarative_base()


class EngineConn:

    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle = 500)
        self.Session = sessionmaker(bind=self.engine)

    @contextmanager 
    def get_session(self):
        session = self.Session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e 
        finally:
            session.close() 

    @contextmanager 
    def get_connection(self):
        conn = self.engine.connect()
        try:
            yield conn
        finally:
            conn.close()


engine_conn = EngineConn()


def get_db():
    with engine_conn.get_session() as db: 
        yield db

def get_raw_db_connection():
    with engine_conn.get_connection() as conn:
        yield conn