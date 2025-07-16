from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.domain.memo.memo_schema import MemoCreate
from app.domain.memo.memo_service import MemoService
from app.infrastructure.memo.repository_impl import MemoRepositoryImpl

router = APIRouter(
    prefix="/memo",
    tags=["memo"],
)


def get_memo_service(db:Session = Depends(get_db)) -> MemoService:
    memo_repository = MemoRepositoryImpl(db)
    return MemoService(repository=memo_repository)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_memo(
        memo_create: MemoCreate,
        memo_service: MemoService = Depends(get_memo_service)
) -> str:
    created_memo = memo_service.create_memo(memo_create)
    print(f'created memo: {created_memo}')
    return 'created_memo test'
