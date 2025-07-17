from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.application.memo_criteria import MemoCriteria
from app.application.memo_facade import MemoFacade
from app.core.database import get_db
from app.domain.member.member_service import MemberService
from app.domain.memo.memo_service import MemoService
from app.domain.role.role_service import RoleService
from app.infrastructure.member.repository_impl import SQLAlchemyMemberRepository
from app.infrastructure.memo.repository_impl import MemoRepositoryImpl
from app.infrastructure.role.repository_impl import RoleRepositoryImpl

router = APIRouter(
    prefix="/memo",
    tags=["memo"],
)

def get_memo_service(db:Session = Depends(get_db)) -> MemoService:
    memo_repository = MemoRepositoryImpl(db)
    return MemoService(repository=memo_repository)

def get_member_service(db:Session = Depends(get_db)) -> MemberService:
    member_repository = SQLAlchemyMemberRepository(db)
    return MemberService(repository=member_repository)

def get_role_service(db:Session = Depends(get_db)) -> RoleService:
    role_repository = RoleRepositoryImpl(db)
    return RoleService(repository=role_repository)

def get_memo_facade(
    memo_service: MemoService = Depends(get_memo_service),
    member_service: MemberService = Depends(get_member_service),
    role_service: RoleService = Depends(get_role_service)
) -> MemoFacade:
    return MemoFacade(memo_service=memo_service, member_service=member_service, role_service=role_service)
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_memo(
        memo_create: MemoCriteria,
        memo_facade: MemoFacade = Depends(get_memo_facade)
) -> str:
    created_memo = memo_facade.create_memo(memo_create)
    print(f'created memo: {created_memo}')
    return 'created_memo test'
