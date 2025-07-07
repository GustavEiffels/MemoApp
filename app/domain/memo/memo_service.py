from domain.memo.memo import Memo
from domain.memo.memo_repository import MemoRepository
from domain.memo.memo_schema import MemoCreate
from domain.exceptions import InvalidError

class MemoService:
    def __init__(self,repository: MemoRepository):
        self.repo = repository
    
    def create_memo(self, command: MemoCreate) -> Memo:

        new_memo = Memo(
            command.contents,
            command.contents,
            command.member_id
        )

        return self.repo.add(new_memo)
    