from domain.member.member_service import MemberService
from domain.memo.memo_service import MemoService
from application.memo_facade_schemas import Criteria
from application.memo_facade_schemas import Result



class MemoFacade:
    def __init__(self, member_service: MemberService, memo_service: MemoService):
        self.memo = memo_service
        self.member = member_service
    
    
    def create_memo(self,criteria:Criteria.CreateMemo) -> Result.CreateMemo:
        # exist member? 
        self.member.exist_member(criteria.member_id)
        #  create memo
        created_memo = self.memo.create_memo(criteria.to_command())
        return Result.CreateMemo(created_memo.id)


        
