from starlette import status
from app.core.custom_exception import CustomBaseException
from app.domain.member.member import Member
from app.domain.member.member_repository import MemberRepository
from app.domain.member.member_schema import MemberCreate
import bcrypt

class MemberService:

    def __init__(self, repository: MemberRepository):
        self.repository = repository


    def create_member(self, create_member: MemberCreate) -> Member:

        find_email = self.repository.find_by_email(create_member.email)
        find_nick  = self.repository.find_by_nick(create_member.nick)

        if find_email:
            raise CustomBaseException("Already Exist Email",status_code=status.HTTP_400_BAD_REQUEST)
        if find_nick:
            raise CustomBaseException("Already using nick",status_code=status.HTTP_400_BAD_REQUEST)

        hashed_password = bcrypt.hashpw(
            create_member.password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        created_member = self.repository.create(create_member.to_domain(hashed_password))
        return created_member
