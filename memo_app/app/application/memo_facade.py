from app.application.memo_criteria import MemoCriteria
from app.domain.member.member_service import MemberService
from app.domain.memo.memo_service import MemoService
from app.domain.role.role_schema import RoleCreate
from app.domain.role.role_service import RoleService

class MemoFacade:
    def __init__(
            self,
            member_service: MemberService,
            memo_service: MemoService,
            role_service: RoleService,
    ):
        self.member_service = member_service
        self.memo_service = memo_service
        self.role_service = role_service

    def create_memo(self, memo_criteria:MemoCriteria) -> int:
        _member =  self.member_service.get_member(memo_criteria.member_id)
        _memo   =  self.memo_service.create_memo(memo_criteria.to_shema())
        _role   = self.role_service.create_role(RoleCreate(member_id=_member.id, memo_id=_memo.id))
        return _memo.id