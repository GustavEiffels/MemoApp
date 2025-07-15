from contextlib import asynccontextmanager
from fastapi import FastAPI, status
from sqlalchemy import text
from app.interfaces.member.controller import router as member_router
from app.core.database import engine, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("DB 연결 확인 및 테이블 생성 시작...")
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            if result.scalar() == 1:
                print("DB 연결 성공!")
            else:
                raise Exception("DB 연결 확인 쿼리에서 예상치 못한 결과 발생.")

        Base.metadata.create_all(bind=engine)
        print("데이터베이스 테이블 생성/확인 완료.")

    except Exception as e:
        print(f"ERROR: 데이터베이스 연결 또는 초기화 실패: {e}")
        raise RuntimeError(f"애플리케이션 시작 실패: 데이터베이스 초기화 오류 - {e}")

    yield

    print("애플리케이션 종료 중... (lifespan shutdown event)")

app = FastAPI(
    title="Memo App API",
    description="A simple API for managing members and potentially memos.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

app.include_router(member_router)

@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Welcome to Memo App API! Visit /docs for API documentation."}