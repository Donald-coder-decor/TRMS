
from abc import abstractmethod, ABC


class RoleDAO(ABC):

    @abstractmethod
    def create_role(self, role):
        pass

    @abstractmethod
    def create_role_id(self, roleid):
        pass

    @abstractmethod
    def get_role(self, roleid):
        pass

    @abstractmethod
    def all_role(self):
        pass

    @abstractmethod
    def update_role(self, change):
        pass

    @abstractmethod
    def delete_role(self, roleid):
        pass



