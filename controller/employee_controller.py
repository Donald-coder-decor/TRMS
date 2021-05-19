# from flask import jsonify, request
from flask import Flask, jsonify, request, app


from exceptions.resource_not_found import ResourceNotFound

from models.employee import Employee

from services.employee_services import EmployeeService



# ---------------- Create new user and return 201 status code for successful creation ----------------------
def route(app):
    @app.route("/employees", methods=['POST'])
    def post_employees():
        emp = Employee.json_parse(request.json)
        empserv = EmployeeService.create_employee(emp)
        return jsonify(empserv.json()), 201  # resource created
        # return jsonify(str(empserv)), 201

    # ---------------- Retrieve all users from the database and return status code of 200 for successful retrieval
    @app.route("/employees", methods=['GET'])
    def get_all_employee():
        return jsonify(EmployeeService.all_employee()), 200

    # ---------------- Retrieve Employee with a specific ID from the database and return status code of 200 for successful retrieval or 400 for bad request
    @app.route("/employees/<empid>", methods=['GET'])
    def get_employee(empid):
        try:
            emp = EmployeeService.get_employee(int(empid))

            return jsonify(emp.json()), 200
        except ValueError as e:
            return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    # ---------------- Update a Employee  with an ID and return 200 status for a successful Update  or 404 ----------------------
    @app.route("/employees/<empid>", methods=['PUT'])
    def put_employees(empid):
        try:
            emp = Employee.json_parse(request.json)
            emp.empid = int(empid)
            EmployeeService.update_employee(emp)
            return jsonify(emp.json()), 200
        except ValueError as e:
            return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    # -------------delete with id -----------------
    @app.route("/employees/<empid>", methods=['DELETE'])
    def del_employees(empid):
        try:
            EmployeeService.delete_employee(int(empid))
            return f'Employee with id of  {empid} has been deleted', 204
        except ValueError as e:
            return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employees/<empid>", methods=["PATCH"])
    def patch_users(user_id):
        action = request.json['action']

    # get a join employee infos

    # @app.route("/information/<empid>", methods=['GET'])
    # def get_employeeinformation(empid):
    #     try:
    #         emp = EmployeeService.get_employeeinfos(int(empid))
    #
    #         return jsonify(emp.json()), 200
    #     except ValueError as e:
    #         return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
    #     except ResourceNotFound as r:
    #         return r.message, 404
