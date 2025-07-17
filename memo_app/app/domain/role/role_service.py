from app.domain.role.role import Role
from app.domain.role.role_repository import RoleRepository
from app.domain.role.role_schema import RoleCreate


class RoleService:
    def __init__(self, repository: RoleRepository):
        self.repository = repository

    def create_role(self, role_create: RoleCreate) -> Role:
        return self.repository.create(role_create.to_domain())

