from pydantic import BaseModel

from app.domain.role.role import Role

class RoleCreate(BaseModel):
    member_id: int
    memo_id: int

    def to_domain(self)->Role:
        return Role(member_id=self.member_id, memo_id=self.memo_id)
