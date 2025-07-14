from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base


class Member(Base):
    __tablename__ = 'members'

    # Primary Key
    id = Column(Integer, primary_key=True)

    # Member Detail
    email = Column(String(100),nullable=False)
    nick = Column(String(30),nullable=False)
    password_hash = Column(String(255), nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<Member(id={self.id}, name='{self.nick}', email='{self.email}')>"