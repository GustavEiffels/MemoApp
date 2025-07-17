from sqlalchemy.orm import Session
from app.domain.role.role import Role
from app.domain.role.role_repository import RoleRepository

class RoleRepositoryImpl(RoleRepository):
    def __init__(self, session:Session):
        self.session = session

    def create(self, role:Role) -> Role:
        new_role = role
        self.session.add(new_role)
        self.session.commit()
        self.session.refresh(new_role)
        return new_role
