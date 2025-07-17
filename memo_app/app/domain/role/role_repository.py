import abc

from app.domain.role.role import Role

class RoleRepository(abc.ABC):

    @abc.abstractmethod
    def create(self,role:Role) -> Role:
        raise NotImplementedError