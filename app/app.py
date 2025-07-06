from fastapi import FastAPI, Depends, Path, HTTPException
from database import EngineConn
from contextlib import contextmanager, asynccontextmanager
from sqlalchemy import text 

engine = EngineConn()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("애플리케이션 시작 중... DB 연결 확인 시도.")
    try:
        with engine.get_connection() as conn:
            result = conn.execute(text("SELECT 1"))
            if result.scalar() == 1:
                print("DB 연결 성공!")
            else:
                raise Exception("DB 연결 확인 쿼리에서 예상치 못한 결과 발생.")
    except Exception as e:
        print(f"DB 연결 실패: {e}")
        raise RuntimeError(f"데이터베이스 연결 오류로 애플리케이션 시작 실패: {e}")

    yield

    print("애플리케이션 종료 중...")
    engine.engine.dispose()
    print("DB 엔진 연결 풀 닫힘.")

app = FastAPI(lifespan=lifespan)