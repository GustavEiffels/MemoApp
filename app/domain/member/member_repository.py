from abc import ABC, abstractmethod
from typing import List, Optional
from domain.member.member import Member


class MemberRepositoryInterface(ABC):
    @abstractmethod
    def add(self, member:Member) -> Member:
        pass

    # @abstractmethod
    # def find_by_id(self,member_id:int) -> Optional[Member]:
    #     pass
    
    # @abstractmethod
    # def find_by_email(self,email:str) -> Optional[Member]:
    #     pass