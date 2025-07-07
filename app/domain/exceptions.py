from typing import Any


class ApplicationException(Exception):
     def __init__(self, message: str = "An application error occurred.", details: Any = None):
        super().__init__(message)
        self.message = message
        self.details = details

class InvalidError(ApplicationException):
    pass

class MemberAlreadyExistsError(ApplicationException):
    pass 

class DuplicationError(ApplicationException):
    """중복된 항목이 존재할 때 발생하는 예외."""
    pass 

class NotFoundError(ApplicationException):
    """요청한 리소스를 찾을 수 없을 때 발생하는 예외."""
    pass

class ValidationError(ApplicationException):
    """입력 데이터의 유효성 검사 실패 시 발생하는 예외 (도메인 레벨)."""
    pass

class MemberAlreadyExistsError(DuplicationError):
    def __init__(self, email: str, message: str = "Member with this email already exists."):
        super().__init__(message, details={"email": email})