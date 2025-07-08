# MemoApp
- python 가상화 
```
python -m venv venv

## mac
source venv/bin/activate  // mac
.\venv\Scripts\Activate.ps1  // window
```

## Branch

### feature/demo
- memo 앱을 만들기전에 lexrank 패키지 익히기 위함 
- nltk, lexrank, konlpy

```
pip install -r requirements.txt // mac 
```

### fast api load 
```
uvicorn app:app --reload
```


### Architecture
```
.
├── main.py                     # FastAPI 애플리케이션 진입점
├── app/
│   ├── __init__.py
│   ├── core/                   # 코어 설정 (DB 설정, 환경 변수 등)
│   │   ├── __init__.py
│   │   ├── config.py           # 환경 변수, 설정 로드
│   │   └── database.py         # DB 세션, ORM 엔진 초기화
│   │
│   ├── models/                 # Domain/Model Layer (데이터 모델)
│   │   ├── __init__.py
│   │   ├── user.py             # User 모델 (SQLAlchemy/Pydantic)
│   │   ├── product.py          # Product 모델 (SQLAlchemy/Pydantic)
│   │   └── order.py            # Order 모델 (SQLAlchemy/Pydantic)
│   │   └── ... (다른 엔티티)
│   │
│   ├── schemas/                # Presentation Layer (Pydantic 요청/응답 스키마)
│   │   ├── __init__.py
│   │   ├── user.py             # UserRequest, UserResponse, UserCreate 등
│   │   ├── product.py          # ProductRequest, ProductResponse 등
│   │   └── ...
│   │
│   ├── repositories/           # Repository Layer (데이터 접근 로직)
│   │   ├── __init__.py
│   │   ├── user.py             # UserRepository
│   │   ├── product.py          # ProductRepository
│   │   └── base.py             # 공통 Repository CRUD 메서드 (옵션)
│   │   └── ...
│   │
│   ├── services/               # Service Layer (비즈니스 로직)
│   │   ├── __init__.py
│   │   ├── user.py             # UserService
│   │   ├── product.py          # ProductService
│   │   └── ...
│   │
│   └── api/                    # Presentation Layer (API 라우트)
│       └── v1/                 # API 버전 관리 (옵션)
│           ├── __init__.py
│           ├── endpoints/
│           │   ├── __init__.py
│           │   ├── users.py      # /users 관련 라우트
│           │   ├── products.py   # /products 관련 라우트
│           │   └── ...
│           └── routers.py      # v1 API 라우터들을 통합하는 파일
│
└── tests/                      # 테스트 코드
    ├── __init__.py
    ├── unit/
    │   ├── test_services.py
    │   └── test_repositories.py
    └── integration/
        └── test_api.py
```