import abc
from typing import Optional

from app.domain.member.member import Member


class MemberRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, member_data:Member) -> Member:
        raise NotImplementedError

    @abc.abstractmethod
    def find_by_email(self, email: str) -> Optional[Member]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_id(self, member_id: int) -> Optional[Member]:
        raise NotImplementedError

    @abc.abstractmethod
    def find_by_nick(self,nick: str) -> Optional[Member]:
        raise NotImplementedError
