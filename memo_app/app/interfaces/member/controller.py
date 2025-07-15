from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.domain.member.member_schema import MemberCreate
from app.domain.member.member_service import MemberService
from app.core.database import get_db
from app.infrastructure.member.repository_impl import SQLAlchemyMemberRepository

router = APIRouter(
    prefix="/members",
    tags=["Members"],
)

def get_member_service(db: Session = Depends(get_db)) -> MemberService:
    member_repository = SQLAlchemyMemberRepository(db)
    return MemberService(repository=member_repository)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_member_endpoint(
    member_create: MemberCreate,
    member_service: MemberService = Depends(get_member_service)
) -> str:

    try:
        created_member = member_service.create_member(member_create)
        print(f'created_member : {created_member}')
        return 'test'
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"회원 생성 중 오류 발생: {e}"
        )