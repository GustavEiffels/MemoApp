from app.domain.memo.memo import Memo
from app.domain.memo.memo_repository import MemoRepository
from sqlalchemy.orm import Session


class MemoRepositoryImpl(MemoRepository):
    def create(self, memo_data: Memo) -> Memo:
        new_memo = memo_data
        self.session.add(new_memo)
        self.session.commit()
        self.session.refresh(new_memo)
        return new_memo

    def __init__(self, session: Session):
        self.session = session



