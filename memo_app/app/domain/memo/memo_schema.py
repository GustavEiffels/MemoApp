
from pydantic import BaseModel

from app.domain.memo.memo import Memo


class MemoCreate(BaseModel):
    contents: str
    member_id: int


    def to_domain(self) -> Memo:
        return Memo(contents=self.contents, summary="test", member_id=self.member_id)
