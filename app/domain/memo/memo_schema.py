from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class MemoCreate(BaseModel):
    contents: str
    summary: str
    member_id:int