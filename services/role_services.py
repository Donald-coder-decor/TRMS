# from flask import jsonify
#
# from daos.role_dao import RoleDAO
# from daos.role_dao_impl import RoleDAOImpl
# from daos.tuition_dao_impl import TuitionDAOImpl
# from models.employee import Employee
# from models.role import Roles
# from models.tuition import Tuition
# from services.employee_services import EmployeeService
# from services.tuition_services import TuitionService
#
#
# class RoleService:
#     role_dao = RoleDAOImpl()
#
#     # @classmethod
#     # def create_role(cls, role, empid):
#     #     return cls.role_dao.create_role(role, empid)
#
#     @classmethod
#     def all_role(cls):
#         return cls.role_dao.all_role()
#
#     # @classmethod
#     # def get_role(cls, roleid):
#     #     return cls.role_dao.get_role(roleid)
#
#     @classmethod
#     def update_role(cls, role, roleid):
#         return cls.role_dao.update_role(role, roleid)
#
#     @classmethod
#     def delete_role(cls, roleid):
#         return cls.role_dao.delete_role(roleid)
#
#     @classmethod
#     def approval_process(cls, empid):
#         tution2 = Tuition()
#         emp = EmployeeService.get_employee(int(empid))  # Get the specific employee to be approved/rejected
#         get_tuit = TuitionService.all_tuition()  # get get/view the reimbursement form information
#
#         if get_tuit:
#             all_role = RoleDAOImpl.all_role(empid)
#             supervisor = all_role[0]
#             depart_head = all_role[1]
#             benco = all_role[2]
#
#             print("I am Supervisor ", supervisor)
#             print("I am Department Head ", depart_head)
#             print("I am Benco", benco)
#
#             if supervisor:
#
#                 tution1 = Tuition()
#                 tution1.submision_status = "Approved"
#
#                 print("The approval process has been completed", tution1)
#                 t = TuitionService.update_tuition(empid, tution1)
#                 print("My tuition", t)
#                 # return tution1.submision_status
#                 return jsonify(get_tuit.json(), t.json()), 200
#             else:
#                 return "Other rules exist"
#
#         #     else:
#         #         return f'Course ID {roleid} - not found', 404
#         # else:
#         #     return f'Employee ID {emp} - not found', 404
#
