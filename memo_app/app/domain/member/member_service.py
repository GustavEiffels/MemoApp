from app.domain.member.member import Member
from app.domain.member.member_repository import MemberRepository
from app.domain.member.member_schema import MemberCreate
import bcrypt

class MemberService:

    def __init__(self, repository: MemberRepository):
        self.repository = repository

    def create_member(self, create_member: MemberCreate) -> Member:
        hashed_password = bcrypt.hashpw(
            create_member.password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")
        created_member = self.repository.create(create_member.to_domain(hashed_password))
        return created_member
