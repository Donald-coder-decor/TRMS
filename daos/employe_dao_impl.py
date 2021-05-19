from flask import request

from exceptions.resource_not_found import ResourceNotFound

from models.employee import Employee
from util.db_connection import connection
from daos.employee_dao import EmployeeDAO


class EmployeeDAOImpl(EmployeeDAO):

    def create_employee(self, employee):  # Create new Employee
        sql = "INSERT INTO employee VALUES(DEFAULT, %s, %s, %s , %s ,%s, %s , %s, %s, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [employee.firstname, employee.midname, employee.lastname,  employee.email,
                             employee.address, employee.emprole, employee.username, employee.password,employee.phone])
        connection.commit()
        record = cursor.fetchone()

        return Employee(
            Employee(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                     record[8], record[9]).json())

    def all_employee(self):  # Retrieve all employees from employee and return
        sql = "SELECT * FROM employee"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        emp_list = []
        for record in records:
            employee = Employee(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                                record[8], record[9])
            emp_list.append(employee.json())
        return emp_list

    def get_employee(self, empid):  # Retrieve a single employee by passing an EmployeeID

        sql = "SELECT * FROM employee WHERE empid =%s"
        cursor = connection.cursor()
        cursor.execute(sql, [empid])
        record = cursor.fetchone()

        if record:
            return Employee(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                            record[8], record[9])
        else:
            raise ResourceNotFound(f"Employee with id: {empid} - Not Found")

    def update_employee(self, change):  # Update Employee Table

        sql = "UPDATE employee SET firstname = %s, midname=%s, lastname=%s, phone=%s , email=%s,  address=%s,emprole=%s, username=%s ,password=%s WHERE empid=%s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql,
                       (change.firstname, change.midname, change.lastname, change.phone, change.email, change.address,
                        change.emprole, change.username, change.password, change.empid))
        connection.commit()
        record = cursor.fetchone()
        return Employee(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                        record[8], record[9])

    def delete_employee(self, empid):  # Delete an  Employee  from Table
        sql = "DELETE FROM employee WHERE empid =%s"
        cursor = connection.cursor()
        cursor.execute(sql, [empid])
        connection.commit()

    def update_employeeRole(self, change, empid):  # Update Employee Table

        sql = "UPDATE employee SET emprole=%s WHERE empid=%s RETURNING *"
        cursor = connection.cursor()
        # print("test if change",change)
        # print("test if empid", empid)
        cursor.execute(sql, change.emprole.change.empid)
        connection.commit()
        record = cursor.fetchone()
        # print(record[0],record[0],record[0],record[0],record[0],record[0],record[0],record[0])
        return Employee(record[0])

    # ----------- Testing section -------------
    def login_employees(self, username, password):  # Retrieve a single employee by passing user name and password
        sql = "SELECT  * FROM employee WHERE username =%s and password =%s"
        cursor = connection.cursor()
        cursor.execute(sql, [username, password])
        record = cursor.fetchone()

        if record:
            return Employee(record[0], record[1],record[2], record[3],record[4], record[5],record[6], record[7], record[8], record[9])
        else:
            raise ResourceNotFound(f"Employee with id: {username} or {username} - Not Found")

    # def get_employeeinfo(self, empid):  # Retrieve a single employee by passing an EmployeeID
    #
    #     sql = "SELECT e.empid, e.firstname, e.lastname, e.email,e.emprole ," \
    #           "c.courseid,c.coursename ,t.gradeformat, t.eventype , t.submision_status, t.costs " \
    #           "FROM employee as e " \
    #           "join courses as c on e.empid = c.empid " \
    #           "join tuition as t on e.empid = t.empid " \
    #           "WHERE e.empid =%s"
    #     cursor = connection.cursor()
    #     cursor.execute(sql, [empid])
    #     record = cursor.fetchone()
    #
    #     if record:
    #         return tuple(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
    #                         record[8], record[9], record[10]).json()
    #     else:
    #         raise ResourceNotFound(f"Employee with id: {empid} - Not Found")


