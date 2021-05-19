from flask import jsonify

from daos.employe_dao_impl import EmployeeDAOImpl
from models.employee import Employee
from models.role import Roles


class EmployeeService:
    employee_dao = EmployeeDAOImpl()

    @classmethod
    def create_employee(cls, employee):
        return cls.employee_dao.create_employee(employee)

    @classmethod
    def all_employee(cls):
        return cls.employee_dao.all_employee()

    @classmethod
    def get_employee(cls, empid):
        return cls.employee_dao.get_employee(empid)

    @classmethod
    def update_employee(cls, employee):
        return cls.employee_dao.update_employee(employee)

    @classmethod
    def delete_employee(cls, empid):
        return cls.employee_dao.delete_employee(empid)

    @classmethod
    def update_employeeRole(cls, employee, empid):
        return cls.employee_dao.update_employeeRole(employee, empid)

    @classmethod
    def employees_login(cls, username, password):
        return cls.employee_dao.login_employees(username, password)

    @classmethod
    def get_employeeinfos(cls, empid):
        return cls.employee_dao.get_employeeinfo(empid)
