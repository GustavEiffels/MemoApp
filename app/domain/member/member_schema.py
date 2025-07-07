from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class MemberCreate(BaseModel):
    email: str
    password: str = Field(min_length=8) 


class MemberUpdate(BaseModel):
    email: Optional[str] = None
    is_super_member: Optional[bool] = None