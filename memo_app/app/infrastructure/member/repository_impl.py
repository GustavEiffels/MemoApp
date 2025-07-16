from typing import Optional

from sqlalchemy.orm import Session

from app.domain.member.member import Member
from app.domain.member.member_repository import MemberRepository


class SQLAlchemyMemberRepository(MemberRepository):

    def find_by_nick(self, nick: str) -> Optional[Member]:
        return self.session.query(Member).filter(Member.nick == nick).first()

    def get_by_id(self, member_id: int) -> Optional[Member]:
        return self.session.query(Member).filter(Member.id == member_id).first()

    def find_by_email(self, email: str) -> Optional[Member]:
        return self.session.query(Member).filter(Member.email == email).first()


    def create(self, member_data: Member) -> Member:
        new_member = member_data
        self.session.add(new_member)
        self.session.commit()
        self.session.refresh(new_member)
        return new_member

    def __init__(self, session: Session):
        self.session = session

