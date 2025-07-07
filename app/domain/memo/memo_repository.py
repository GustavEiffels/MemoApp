from abc import ABC, abstractmethod
from typing import List, Optional
from domain.memo.memo import Memo

class MemoRepository(ABC):
    @abstractmethod
    def add(self, memo:Memo)->Memo:
        pass 