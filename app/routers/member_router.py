from fastapi import APIRouter, Depends, status
from typing import Annotated
from sqlalchemy.orm import Session

from database import get_db 
from domain.member.member_schema import MemberCreate
from domain.member.member_repository import MemberRepositoryInterface 
from domain.member.member_service import MemberService 
from infra.member.sqlalchemy_member_repository import SQLAlchemyMemberRepository


router = APIRouter(
    prefix="/members",
    tags=["members"]
)

def get_member_repository(db: Session = Depends(get_db)) -> MemberRepositoryInterface:
    return SQLAlchemyMemberRepository(db)

def get_member_service(
        rep : Annotated[MemberRepositoryInterface,Depends(get_member_repository)]
) -> MemberService:
    return MemberService(rep)


@router.post('/',status_code=status.HTTP_201_CREATED)
async def create_member(
    command: MemberCreate,
    service: Annotated[MemberService,Depends(get_member_service)]
):
    new_member = service.create_member(command)
    return {"message": "Member created successfully", "email": new_member.email, "id": new_member.id}