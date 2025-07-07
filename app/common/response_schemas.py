from pydantic import BaseModel
from typing import TypeVar, Generic, Any, Optional

PayloadType = TypeVar("PayloadType")

class ApiResponse(BaseModel, Generic[PayloadType]):
    success: bool
    message: str
    data: Optional[PayloadType] = None  
    error: Optional[str] = None         



class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    error: Optional[str] = None
    code: Optional[str] = None