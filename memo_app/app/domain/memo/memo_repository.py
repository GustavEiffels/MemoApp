import abc

from app.domain.memo.memo import Memo

class MemoRepository(abc.ABC):

    @abc.abstractmethod
    def create(self,memo_data:Memo) -> Memo:
        raise NotImplementedError

