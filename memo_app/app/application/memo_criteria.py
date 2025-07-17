from pydantic import BaseModel

from app.domain.memo.memo_schema import MemoCreate


class MemoCriteria(BaseModel):
    contents: str
    member_id: int

    def to_shema(self):
        return MemoCreate(contents=self.contents, member_id=self.member_id)