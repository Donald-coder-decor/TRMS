# from flask import request, jsonify
#
# from daos.role_dao_impl import RoleDAOImpl
# from exceptions.resource_not_found import ResourceNotFound
# from models.employee import Employee
# from models.role import Roles
# from models.tuition import Tuition
# from services.employee_services import EmployeeService
# from services.role_services import RoleService
# from services.tuition_services import TuitionService
#
#
# def route(app):
#     # +++++++++++++++++ create or assign  a  new course  to an employee (ID)   +++++++++++ 04-20-21
#     # and return status code of 201 for successful creation or 400
#     @app.route("/employees/<empid>/role", methods=['POST'])
#     def create_employee_roles(empid):
#         try:
#             role = Roles.json_parse(request.json)
#             RoleService.create_role(role, empid)
#             return jsonify(role.json()), 201
#         except ValueError as e:
#             return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
#
#         # -----------Retrieve all Roles ----------------------
#
#     @app.route("/roles", methods=['GET'])
#     def get_all_roles():
#         return jsonify(RoleService.all_role()), 200
#
#     # +++++++++++++++++ Retrieve all Courses assigned to an employee  with a specific employee ID from the database  +++++++++++ 04-20-21
#     # and return status code of 200 for successful retrieval or 400 for bad request
#     # @app.route("/courses/<empid>/courses", methods=['GET'])
#     # def get_employee_roles(empid):
#     #     try:
#     #         if EmployeeService.get_employee(int(empid)):
#     #             course = RoleService.get_role(empid)
#     #             return jsonify(course), 200
#     #     except ValueError as e:
#     #         return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
#     #     except ResourceNotFound as r:
#     #         return r.message, 404
#
#     @app.route("/roles/<roleid>", methods=['GET'])
#     def get_role_withID(roleid):
#         roles = RoleService.get_role(roleid)
#         return jsonify(str(roles)), 200
#
#
#
#
#
#
