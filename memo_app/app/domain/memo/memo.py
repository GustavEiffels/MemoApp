from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import DateTime

from app.core.database import Base


class Memo(Base):
    __tablename__ = "memo"

    # Primary Key
    id = Column(Integer, primary_key=True)

    # Memo Detail
    contents = Column(String(2000), nullable=True)
    summary  = Column(String(500), nullable=True)
    member_id = Column(Integer, nullable=False, index=True)
    # Time Setting 
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), server_default=func.now(), nullable=False)
    def __repr__(self):
        return f"<Memo {self.id}, member_id: {self.member_id}, summary: {self.summary}>"