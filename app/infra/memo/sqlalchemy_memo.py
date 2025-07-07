from sqlalchemy.orm import Session
from typing import Optional
from models import MemoEntity
from domain.memo.memo import Memo
from domain.memo.memo_repository import MemoRepository

class SQLAlchemyMemoRepository(MemoRepository):
    def __init__(self,db_session: Session):
        self.db_session = db_session

    
    def add(self, memo:Memo)->Memo:

        memoEntity = MemoEntity.from_domain(memo) 
        self.db_session.add(memoEntity)
        self.db_session.commit()
        self.db_session.refresh(memoEntity)
    
        return memoEntity.to_domain()
