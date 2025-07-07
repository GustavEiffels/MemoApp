from fastapi import APIRouter, Depends, status
from typing import Annotated
from sqlalchemy.orm import Session
from database import get_db 

from domain.memo.memo_schema import MemoCreate
from domain.memo.memo_repository import MemoRepository
from domain.memo.memo_service import MemoService
from infra.memo.sqlalchemy_memo import SQLAlchemyMemoRepository

router = APIRouter(
    prefix="/memos",
    tags=["memos"]
)

# repository
def get_memo_repository(db: Session = Depends(get_db)) -> MemoRepository:
    return SQLAlchemyMemoRepository(db)

# service
def get_memo_service(
        rep: Annotated[MemoRepository,Depends(get_memo_repository)]
)-> MemoService:
    return MemoService(rep)


@router.post('/',status_code=status.HTTP_201_CREATED)
async def create_memo(
    command: MemoCreate,
    service: Annotated[MemoService,Depends(get_memo_service)]
):
    new_memo = service.create_memo(command)
    return {"message": "Member created successfully", "memo_id": new_memo.id, "contents": new_memo.contents}