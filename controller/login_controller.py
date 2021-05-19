from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.employee import Employee
from services.employee_services import EmployeeService


def route(app):
    @app.route("/login/<username>/<password>", methods=['GET'])
    def employee_login(username, password):
        print(username, password)
        emp_login = EmployeeService.employees_login(username, password)
        if emp_login:
            print("what type is it",type(emp_login))
            if emp_login.emprole == "Benco":
                print("You are login as :", emp_login.emprole)
                return jsonify(emp_login.json()), 200
            elif emp_login.emprole == "Supervisor":
                print("You are login as : ",emp_login.emprole)
                return jsonify(emp_login.json()), 200
            elif emp_login.emprole == "Dept Head":
                 print(f"you have login as ", emp_login.emprole)
                 return jsonify(emp_login.json()), 200
            else:
                print(f"you have login as ", emp_login.username)
                return jsonify(emp_login.json()), 200
        else:
            return f"Username or Password does not match, please type in correct credentials!"

