from fastapi import status


class CustomBaseException(Exception):
    def __init__(self, message: str, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR):
        self.detail = message
        self.status_code = status_code


