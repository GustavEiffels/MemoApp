from datetime import datetime
from typing import Optional
from domain.exceptions import InvalidError

class Memo:
    def __init__(
            self,
            contents:str,
            summary: str,
            member_id:int,
            id: Optional[int] = None,
            created_at: Optional[datetime] = None,
            updated_at: Optional[datetime] = None,
            deleted_at: Optional[datetime] = None
    ):
        main_contents = contents
        
        if member_id is None:
            raise InvalidError('Memo Owner is not Exist')
        
        if main_contents is None:
            main_contents = 'This Contents is Empty'
    
        self.id         = id
        self.contents   = main_contents
        self.summary    = summary
        self.member_id  = member_id
        self.created_at = created_at if created_at is not None else datetime.now()
        self.updated_at = updated_at if updated_at is not None else datetime.now()
        self.deleted_at = deleted_at