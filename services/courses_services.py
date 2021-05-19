from flask import request, jsonify

from daos.course_dao_impl import CourseDAOImpl


class CourseService:
    courses_serv = CourseDAOImpl()

    @classmethod
    def create_courses(cls, course, courseid):
        return cls.courses_serv.create_courses(course, courseid)

    @classmethod
    def all_courses(cls):
        return cls.courses_serv.all_courses()

    @classmethod
    def get_courses(cls, empid):
        return cls.courses_serv.get_courses(empid)

    @classmethod
    def get_course_ID(cls, courseid):
        return cls.courses_serv.get_courseID(courseid)

    # ---- update course with an ID
    @classmethod
    def update_course(cls,  course, courseid):
        return cls.courses_serv.update_courses(course, courseid)

    # ----------------Delete course by id

    @classmethod
    def delete_course(cls, courseid):
        return cls.courses_serv.delete_courses(courseid)
