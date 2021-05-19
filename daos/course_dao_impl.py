from daos.employe_dao_impl import EmployeeDAOImpl
from exceptions.resource_not_found import ResourceNotFound
from daos import employee_dao, courses_dao
from models.courses import Courses
from util.db_connection import connection
from daos.courses_dao import CoursesDAO


class CourseDAOImpl(CoursesDAO):

    def create_courses(self, course, empid):  # Create new Course
        # check if employee exist before creating a course or raise an error (404)
        try:
            exist_empid = EmployeeDAOImpl()
            exist_empid.get_employee(empid)
        except ResourceNotFound as r:
            raise r

        sql = "INSERT INTO courses VALUES(DEFAULT, %s, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (course.coursename, course.empid,))
        connection.commit()
        record = cursor.fetchone()

        return Courses(
            Courses(record[0], record[1], record[2]))

    def all_courses(self ):  # Retrieve all Course from courses and return
        sql = "SELECT * FROM courses"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        courses_list = []
        for record in records:
            course = Courses(record[0], record[1], record[2])
            courses_list.append(course.json())
        return courses_list

    def get_courses(self, empid):  # Retrieve a single Course for an employee by passing an  employee ID
        sql = "SELECT * FROM courses WHERE  empid=%s "
        cursor = connection.cursor()
        cursor.execute(sql, [empid])
        record = cursor.fetchall()

        courses_list = []
        for records in record:
            course = Courses(records[0], records[1], records[2])
            courses_list.append(course.json())
        return courses_list

    # -----------------get course with a course ID
    def get_courseID(self, courseid):  # Retrieve a single Course for an employee by passing an course ID

        sql = "SELECT *  FROM courses WHERE  courseid=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [courseid])
        record = cursor.fetchone()

        if record:
            return Courses(record[0], record[1], record[2])
        else:
            return f'Course ID  {courseid} - Not found'

    def update_courses(self, change, courseid):  # Update Courses Table
        sql = "UPDATE courses SET coursename=%s  WHERE courseid=%s "
        cursor = connection.cursor()
        cursor.execute(sql, change.coursename)
        connection.commit()
        record = cursor.fetchone()
        return Courses(int(record[0]), record[1], int(record[2]))

    def delete_courses(self, courseid, empid):  # Delete a course   from Table
        try:
            exist_empid = EmployeeDAOImpl()
            exist_empid.get_employee(empid)
        except ResourceNotFound as r:
            raise r

        try:
            self.get_courses(empid, courseid)  # I need to double check this

        except ResourceNotFound as r:
            raise r

        sql = "DELETE FROM courses WHERE courseid =%s"
        cursor = connection.cursor()
        cursor.execute(sql, [courseid])
        connection.commit()


# ----------- Testing section -------------
# def _test():
#     pass
#     course = CoursesDAO()
#     courses = course.all_courses()
#
#     print(courses)
#     if courses_dao.get_courses(11):
#         print(courses_dao.get_courses(11))
#         print("found and ID")
#     else:
#         print("ID not found ID")
#
#
# if __name__ == '__main__':
#     _test()
