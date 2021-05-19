from flask import Flask, jsonify, request, app

from exceptions.resource_not_found import ResourceNotFound
from models.courses import Courses
from models.tuition import Tuition
from services.courses_services import CourseService
from services.employee_services import EmployeeService
from services.tuition_services import TuitionService


# ---------------- create a new tuition reimbursement the database and return status code of 200 for successful retrieval
def route(app):
    @app.route("/tuitions/<empid>", methods=['POST'])
    def post_tuition(empid):
        # try:
        reimburse = Tuition.json_parse(request.json)
        emp = EmployeeService.get_employee(empid)
        if emp:
            print(emp)
            reimburse_serv = TuitionService.create_tuition(reimburse, empid)
            return jsonify(str(reimburse_serv)), 201
        else:
            return f"Employee ID {empid} not Found", 404

    # Retrieve all tuition from the Tuition table
    @app.route("/tuitions", methods=['GET'])
    def get_all_tuition():
        return jsonify(TuitionService.all_tuition()), 200

    # +++++++++++++++++ Retrieve a Tuition  with a specific Employee ID from the database  +++++++++++ 04-20-21
    # and return status code of 200 for successful retrieval or 400 for bad request
    @app.route("/tuitions/<empid>", methods=['GET'])
    def get_Employee_tuition(empid):
        try:
            new_empid = EmployeeService.get_employee(int(empid))
            if new_empid:
                new_tuitions = TuitionService.get_tuition_id(empid)
                print("printing ", empid)
                return jsonify(new_tuitions.json()), 200
        except ValueError as e:
            return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    # ---------------- Update an employee  with an ID and return 200 status for a successful Update  or 404 ----------------------
    @app.route("/tuitions/updating/<empid>", methods=['PUT'])
    def update_tuition(empid):
        try:
            new_empid = EmployeeService.get_employee(int(empid))
            if new_empid:
                reimburse = Tuition.json_parse(request.json)
                tuition = TuitionService.update_tuition(reimburse, empid)
                return jsonify(str(tuition)), 200
        except ValueError as e:
            return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    # ----------------------------- delete  a tuition with id
    @app.route("/tuitions/<empid>/tuition/<tuitionid>", methods=['DELETE'])
    def del_employee(empid, tuitionid):
        try:
            TuitionService.delete_tuition(int(empid), int(tuitionid))
            return '', 204
        except ValueError as e:
            return "Not a valid ID or No such Tuition exist with this ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    #  --------------------------------------------- approval/reject processing......................

    @app.route("/roles/tuitions/<empid>", methods=['PUT'])
    def aprove_role(empid):
        reimburse = TuitionService.approval_process(empid)
        return f" Successfully Approved   {reimburse}", 200

    @app.route("/roles/rejected/<empid>", methods=['PUT'])
    def aprove_role_reject(empid):
        reimburse = TuitionService.rejected_process(empid)
        return f" Successfully Rejected   {reimburse}", 200
