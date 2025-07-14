from sqlalchemy import Column, Integer, String
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
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

