from domain.memo.memo_schema import MemoCreate
from domain.memo.memo import Memo

class Criteria:
    def __init__(self):
        pass

    class CreateMemo:
        def __init__(self, contents:str, summary:str,member_id:int):
            self.contents = contents
            self.summary = summary
            self.member_id = member_id

        def to_command(self) -> MemoCreate:
            return MemoCreate(
                self.contents,
                self.summary,
                self.member_id
                )
            



class Result:
    def __init__(self,id:int):
        self.id = id

    class CreateMemo:
        def __init__(self, memo_id:int):
            self.memo_id = memo_id
        
        @classmethod
        def from_info(self,memo: Memo):
            return self(memo.id)