from sqlalchemy.orm import Session

from app.domain.member.member import Member
from app.domain.member.member_repository import MemberRepository


class SQLAlchemyMemberRepository(MemberRepository):

    def create(self, member_data: Member) -> Member:
        new_member = member_data
        self.session.add(new_member)
        self.session.commit()
        self.session.refresh(new_member)
        return new_member

    def __init__(self, session: Session):
        self.session = session

