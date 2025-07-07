from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Member(Base):
    __tablename__ = "Members"
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(50), nullable=False)
    super_member = Column(Boolean, default=False)
    createAt = Column(DateTime, nullable=False)
    updateAt = Column(DateTime, nullable=False)
    deleteAt = Column(DateTime, nullable=True)

class Memo(Base):
    __tablename__ = "Memos"
    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(2000), nullable=True)
    summary  = Column(String(500), nullable=True)
    member_id = Column(Integer, nullable=False, index=True)
    createAt = Column(DateTime, nullable=False)
    updateAt = Column(DateTime, nullable=False)
    deleteAt = Column(DateTime, nullable=True)


class Role(Base):
    __tablename__ = "Roles"
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey('members.id'), nullable=False, index=True)
    memo_id = Column(Integer, ForeignKey('memos.id'), nullable=False, index=True)
    member = relationship("Member", back_populates="member_memo_roles")
    memo = relationship("Memo", back_populates="member_memo_roles")