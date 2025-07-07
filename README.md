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