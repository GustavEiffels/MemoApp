from app.domain.member.member import Member
from app.domain.member.member_repository import MemberRepository
from app.domain.member.member_schema import MemberCreate


class MemberService:

    def __init__(self, repository: MemberRepository):
        self.repository = repository

    def create_member(self, create_member: MemberCreate) -> Member:
        created_member = self.repository.create(create_member.to_domain())
        return created_member
