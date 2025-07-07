from datetime import datetime
from typing import Optional

class Member:
    def __init__(
        self,
        email: str,
        password_hash: str,
        id: Optional[int] = None,
        is_super_member: bool = False,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        deleted_at: Optional[datetime] = None
    ):
        if not email or "@" not in email:
            raise ValueError("Invalid email format.")
        if not password_hash: 
            raise ValueError("Password hash cannot be empty.")

        self.id = id
        self.email = email
        self.password_hash = password_hash 
        self.is_super_member = is_super_member 
        self.created_at = created_at if created_at is not None else datetime.now()
        self.updated_at = updated_at if updated_at is not None else datetime.now()
        self.deleted_at = deleted_at

    def update_password(self, new_password_hash: str):
        """멤버 비밀번호 해시를 업데이트하고 업데이트 시각을 갱신합니다."""
        if not new_password_hash:
            raise ValueError("New password hash cannot be empty.")
        self.password_hash = new_password_hash
        self.updated_at = datetime.now()


    def soft_delete(self):
        """멤버를 논리적으로 삭제합니다 (deleted_at 필드 설정)."""
        if self.deleted_at is None: 
            self.deleted_at = datetime.now()
            self.updated_at = datetime.now()


    def restore(self):
        """논리적으로 삭제된 멤버를 복원합니다."""
        if self.deleted_at is not None:
            self.deleted_at = None
            self.updated_at = datetime.now()


    def to_dict(self):
        """객체를 딕셔너리로 변환하여 DTO 매핑 등에 활용."""
        return {
            "id": self.id,
            "email": self.email,
            "password_hash": self.password_hash,
            "is_super_member": self.is_super_member,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None
        }