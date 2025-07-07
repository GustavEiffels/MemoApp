from fastapi import FastAPI, Depends, HTTPException, status, Request # Request 임포트 추가
from fastapi.responses import JSONResponse 
from database import engine_conn, Base
from contextlib import contextmanager, asynccontextmanager
from sqlalchemy import text 
import models  

from routers import member_router 
from domain.exceptions import MemberAlreadyExistsError, ApplicationException, ValidationError
from common.response_schemas import ApiResponse


async def initialize_database():
    print("애플리케이션 시작 중... DB 연결 확인 시도.")
    try:
        with engine_conn.get_connection() as conn:
            result = conn.execute(text("SELECT 1"))
            if result.scalar() == 1:
                print("DB 연결 성공!")
            else:
                raise Exception("DB 연결 확인 쿼리에서 예상치 못한 결과 발생.")
            
        print("데이터베이스 테이블 생성/확인 시작...")
        Base.metadata.create_all(bind=engine_conn.engine) 
        print("데이터베이스 테이블 생성/확인 완료.")
    except Exception as e:
        print(f"DB 연결 실패: {e}")
        raise RuntimeError(f"데이터베이스 연결 오류로 애플리케이션 시작 실패: {e}")

# --- lifespan 함수 재정의 ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    await initialize_database()
    yield
    print("애플리케이션 종료 중...")
    engine_conn.engine.dispose()
    print("DB 엔진 연결 풀 닫힘.")

app = FastAPI(lifespan=lifespan)
app.include_router(member_router.router)


# -- Exception
@app.exception_handler(ApplicationException) # 모든 커스텀 애플리케이션 예외의 기본 처리기
async def application_exception_handler(request: Request, exc: ApplicationException):
    """
    ApplicationException의 하위 예외들이 특정 핸들러로 잡히지 않을 때의 기본 처리기.
    """
    print(f"Unhandled ApplicationException caught: {exc.message} - Details: {exc.details}")
    api_response = ApiResponse(
        success=False,
        message="An unexpected application error occurred.",
        error="Internal Server Error",
        code="UNEXPECTED_APPLICATION_ERROR",
        data=None
    )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=api_response.model_dump(exclude_none=True),
    )



@app.exception_handler(ValidationError) # 모든 커스텀 애플리케이션 예외의 기본 처리기
async def application_exception_handler(request: Request, exc: ValidationError):
    print(f"Unhandled ApplicationException caught: {exc.message} - Details: {exc.details}")
    api_response = ApiResponse(
        success=False,
        message="An unexpected application error occurred.",
        error="Internal Server Error",
        code="UNEXPECTED_APPLICATION_ERROR",
        data=None
    )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=api_response.model_dump(exclude_none=True),
    )

@app.exception_handler(MemberAlreadyExistsError)
async def member_already_exists_exception_handler(request: Request, exc: MemberAlreadyExistsError):
    """
    MemberAlreadyExistsError 발생 시 409 CONFLICT 응답을 반환합니다.
    """
    api_response = ApiResponse(
        success=False,
        message=exc.message,
        error="Resource Conflict",
        code="MEMBER_ALREADY_EXISTS",
        data=None
    )
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content=api_response.model_dump(exclude_none=True),
    )
