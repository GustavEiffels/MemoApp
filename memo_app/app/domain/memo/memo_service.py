from app.domain.memo.memo import Memo
from app.domain.memo.memo_repository import MemoRepository
from app.domain.memo.memo_schema import MemoCreate


class MemoService:
    def __init__(self, repository: MemoRepository):
        self.repository = repository


    def create_memo(self, memo_create: MemoCreate) -> Memo:
        return self.repository.create(memo_create.to_domain())