from flask import Flask, jsonify, request, app

from daos.employe_dao_impl import EmployeeDAOImpl
from exceptions.resource_not_found import ResourceNotFound

from models.courses import Courses
from services.employee_services import EmployeeService
from services.courses_services import CourseService


def route(app):
    # +++++++++++++++++ create or assign  a  new course  to an employee (ID)   +++++++++++ 04-20-21
    # and return status code of 201 for successful creation or 400
    @app.route("/employees/<empid>", methods=['POST'])
    def post_employee_course(empid):
        try:
            course_ = Courses.json_parse(request.json)
            CourseService.create_courses(course_, empid)
            return jsonify(course_.json()), 201
        except ValueError as e:
            return "Not a valid ID or No such user exist with this ID", 400  # Bad Request

    # -----------Retrieve all courses ----------------------
    @app.route("/courses", methods=['GET'])
    def get_all_course():
        return jsonify(CourseService.all_courses()), 200

    # +++++++++++++++++ Retrieve all Courses assigned to an employee  with a specific employee ID from the database  +++++++++++ 04-20-21
    # and return status code of 200 for successful retrieval or 400 for bad request
    @app.route("/courses/<empid>", methods=['GET'])
    def get_employee_courses(empid):
        try:
            if EmployeeService.get_employee(int(empid)):
                course = CourseService.get_courses(empid)
                return jsonify(course), 200
        except ValueError as e:
            return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/courses/<courseid>", methods=['GET'])
    def get_course_withID(courseid):
        courses = CourseService.get_course_ID(courseid)
        return jsonify(str(courses)), 200

    # ---------------- Update an Employee Coures  with an ID and return 200 status for a successful Update  or 404 ----------------------
    @app.route("/employees/<empid>/courses/<courseid>", methods=['PUT'])
    def update_course(empid, courseid):
        # try:
        emp = EmployeeService.get_employee(int(empid))
        if emp:
            # print(emp)
            get_course = CourseService.get_course_ID(int(courseid))

            if get_course:
                all_course = Courses.json_parse(request.json)
                CourseService.update_course(all_course, courseid)
                return jsonify(all_course.json()), 200
            else:
                return f'Course ID {courseid} - not found', 404
        else:
            return f'Employee ID {emp} - not found', 404

    # except ValueError as e:
    #     return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
    # except ResourceNotFound as r:
    #     return r.message, 404

    # ----------------------------- delete  a course with id
    @app.route("/employees/<empid>/courses/<courseid>", methods=['DELETE'])
    def del_course(empid, courseid):
        try:
            CourseService.delete_course(int(empid), int(courseid))
            return '', 204
        except ValueError as e:
            return "Not a valid ID or No such user exist with this ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    # @app.route("/users/<user_id>", methods=["PATCH"])
    # def patch_user(user_id):
    #     action = request.json['action']
