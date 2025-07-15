from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Member(Base):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String(100), nullable=False, unique=True)
    nick = Column(String(30), nullable=False)
    password_hash = Column(String(255), nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<Member(id={self.id}, nick='{self.nick}', email='{self.email}')>"