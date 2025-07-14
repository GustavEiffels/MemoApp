import abc

from app.domain.member.member import Member


class MemberRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, member_data:Member) -> Member:
        raise NotImplementedError
