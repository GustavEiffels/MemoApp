from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager 

DB_URL = 'mysql+pymysql://myuser:mypassword@localhost:33066/mydb'

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
        except Exception:
            session.rollback()
            raise 
        finally:
            session.close() 

    @contextmanager 
    def get_connection(self):
        conn = self.engine.connect()
        try:
            yield conn
        finally:
            conn.close()