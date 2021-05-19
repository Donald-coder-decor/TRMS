from flask import request, jsonify

from daos.role_dao_impl import RoleDAOImpl
from daos.tuition_dao_impl import TuitionDAOImpl
from models.courses import Courses
from models.tuition import Tuition
from services.employee_services import EmployeeService


class TuitionService:
    tuition_serv = TuitionDAOImpl()

    @classmethod
    def create_tuition(cls, tuition, empid):
        return cls.tuition_serv.create_tuition(tuition, empid)
    @classmethod
    def tuition_calculation(cls,cost_limit,amount_awarded , amount_avail, amount_pending):
        course_object = Courses()
        courses = course_object.coursename
        if courses == "University":
            cost_limit= 1000




    @classmethod
    def all_tuition(cls):
        return cls.tuition_serv.all_tuition()

    @classmethod
    def get_tuition_id(cls, empid):
        return cls.tuition_serv.get_tuition(empid)

    # ---- update course with an ID
    @classmethod
    def update_tuition(cls, tuition_object, empid):
        return cls.tuition_serv.update_tuition(tuition_object, empid)

    @classmethod
    def update_tuition_reject(cls, tuition_object, empid):
        return cls.tuition_serv.update_tuition_reject(tuition_object, empid)
    # ----------------Delete course by id

    @classmethod
    def delete_tuition(cls, tuitionid):
        return cls.tuition_serv.delete_tuition(tuitionid)

    # ---------------Approval process -------------------

    @classmethod
    def approval_process(cls, empid):
        emp = EmployeeService.get_employee(empid)  # Get the specific employee to be approved/rejected
        if emp:
            get_tuit = TuitionService.get_tuition_id(empid)  # get get/view the reimbursement form information
            print("geting stuff",get_tuit)
            get_tuit.submision_status = "Approved"
            tuition_approve = TuitionService.update_tuition(get_tuit,empid)
            return  jsonify(str(tuition_approve)), 200
        else:
            return  "Employee not found", 404

    @classmethod
    def rejected_process(cls, empid): # rejecting a reimbursement
        emp = EmployeeService.get_employee(int(empid))  # Get the specific employee to be approved/rejected
        if emp:
            get_tuit = TuitionService.get_tuition_id(empid)  # get get/view the reimbursement form information
            get_tuit.submision_status = "Rejected"
            tuition_approve = TuitionService.update_tuition_reject(get_tuit, empid)
            return jsonify(str(tuition_approve)), 200
        else:
            return "Employee not found", 404


