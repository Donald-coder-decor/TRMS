
from abc import abstractmethod, ABC


class EmployeeDAO(ABC):

    @abstractmethod
    def create_employee(self, employee):
        pass

    @abstractmethod
    def all_employee(self):
        pass

    @abstractmethod
    def get_employee(self, empid):
        pass

    @abstractmethod
    def update_employee(self, change, empid):
        pass

    @abstractmethod
    def delete_employee(self, empid):
        pass

    @abstractmethod
    def update_employeeRole(self, change):
        pass
    # @abstractmethod
    # def create_employee_id(self, empid):
    #     pass
