from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Role(Base):
    __tablename__ = "roles"

    # Primary Key
    id = Column(Integer, primary_key=True)

    # Role Detail
    member_id = Column(Integer, nullable=False, index=True)
    memo_id = Column(Integer, nullable=False, index=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

