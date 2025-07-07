from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from database import Base
from domain.member.member import Member
from domain.memo.memo import Memo


class MemberEntity(Base):
    __tablename__ = "Members"
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(50), nullable=False)
    is_super_member = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    @classmethod
    def from_domain(cls, domain_member: Member) -> "MemberEntity":
        return cls(
            id=domain_member.id,
            email=domain_member.email,
            password=domain_member.password_hash,
            is_super_member=domain_member.is_super_member,
            created_at=domain_member.created_at,
            updated_at=domain_member.updated_at,
            deleted_at=domain_member.deleted_at
        )
    
    def to_domain(self) -> Member:
        return Member(
            id=self.id,
            email=self.email,
            password_hash=self.password,
            is_super_member=self.is_super_member,
            created_at=self.created_at,
            updated_at=self.updated_at,
            deleted_at=self.deleted_at
        )


class MemoEntity(Base):
    __tablename__ = "Memos"
    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(2000), nullable=True)
    summary  = Column(String(500), nullable=True)
    member_id = Column(Integer, nullable=False, index=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    @classmethod
    def from_domain(cls,domain_memo: Memo) -> "MemoEntity":
        return cls(
            contents=domain_memo.contents,
            summary=domain_memo.summary,
            id=domain_memo.id,
            member_id=domain_memo.member_id,
            created_at=domain_memo.created_at,
            updated_at=domain_memo.updated_at,
            deleted_at=domain_memo.deleted_at
        )
    
    def to_domain(self) -> Memo:
        return Memo(
            id=self.id,
            contents=self.contents,
            summary=self.summary,
            member_id=self.member_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
            deleted_at=self.deleted_at
        )


class RoleEntity(Base):
    __tablename__ = "Roles"
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, nullable=False, index=True)
    memo_id = Column(Integer, nullable=False, index=True)
