from sqlalchemy.orm import Session
from typing import List, Optional
from models import MemberEntity
from domain.member.member import Member
from domain.member.member_repository import MemberRepositoryInterface 


class SQLAlchemyMemberRepository(MemberRepositoryInterface):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add(self, member: Member) -> Member:
        memberEntity = MemberEntity.from_domain(member)

        self.db_session.add(memberEntity)
        self.db_session.commit()
        self.db_session.refresh(memberEntity)
        return memberEntity.to_domain()
    

    def find_by_email(self,email:str) -> Optional[Member]:
        member_entity = self.db_session.query(MemberEntity).filter(MemberEntity.email == email).first()
        
        if member_entity:
            return member_entity.to_domain()
        return None