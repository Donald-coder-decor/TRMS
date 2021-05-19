from datetime import datetime

from daos.course_dao_impl import CourseDAOImpl
from daos.employe_dao_impl import EmployeeDAOImpl
from exceptions.resource_not_found import ResourceNotFound

from models.tuition import Tuition
from util.db_connection import connection
from daos.tuition_dao import TuitionDAO


class TuitionDAOImpl(TuitionDAO):

    def create_tuition(self, tuition, empid):  # Create new Tuition form
        print("what is the insertion order", tuition)
        sql = "INSERT INTO tuition VALUES(DEFAULT,  %s , %s , %s , %s , %s, %s , %s, %s, %s , %s, %s, %s, %s,  %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (
            tuition.locations, tuition.description, tuition.gradeformat, tuition.eventype,
            tuition.workrelate, tuition.empid, tuition.submision_status, tuition.costs,
            tuition.firsname_lastname, tuition.amount_awarded, tuition.amount_available,
            tuition.approval, tuition.reject, tuition.reason
        ), )
        connection.commit()
        record = cursor.fetchone()

        return Tuition(
            Tuition(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8],
                    record[9]))

    def all_tuition(self):  # Retrieve all Tuition from Tuition and return
        sql = "SELECT * FROM tuition"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        tuition_list = []
        for record in records:
            tuition = Tuition(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                              record[8], record[10], record[11], record[12], record[13], record[14])
            tuition_list.append(tuition.json())
        return tuition_list

    def get_tuition(self, empid):  # Retrieve a single Tuition by passing a Employee ID

        sql = "SELECT * FROM tuition WHERE empid=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [empid])
        record = cursor.fetchone()

        if record:
            return Tuition(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                           record[8], record[9])
        else:
            raise ResourceNotFound(f" This Employee  id: {empid} doesn't have a Tuition created yet")

    def update_tuition(self, tuition_object, empid):  # Update Tuition Table
        sql = "UPDATE tuition SET  submision_status = %s WHERE empid=%s RETURNING *"

        # locations=%s, description=%s ,  gradeformat=%s, eventype=%s ,workrelate=%s , empid=%s, submision_status =%s," \
        # " costs=%s, firsname_lastname=%s, amount_awarded=%s  amount_available=%s,  approval=%s, reject=%s, reason=%s WHERE empid=%s RETURNING *"
        cursor = connection.cursor()
        print(" tution object", tuition_object)

        cursor.execute(sql, [tuition_object.submision_status, tuition_object.empid])
        # tuition_object.locations, tuition_object.description, tuition_object.gradeformat,
        # tuition_object.eventype, tuition_object.workrelate, tuition_object.empid ,
        ## tuition_object.submision_status ,tuition_object.costs,tuition_object.firsname_lastname,
        # tuition_object.amount_awarded,tuition_object.amount_available, tuition_object.approval,tuition_object.reject,tuition_object.reason
        connection.commit()

        record = cursor.fetchone()

        return Tuition(record[0], record[1])


    def update_tuition_reject(self, tuition_object, empid):  # Update Tuition Table
        sql = "UPDATE tuition SET  submision_status = %s ,reason=%s WHERE empid=%s RETURNING *"

        cursor = connection.cursor()
        print(" tution object", tuition_object)

        cursor.execute(sql, [tuition_object.submision_status, tuition_object.reason, tuition_object.empid])
        print("tut", tuition_object)
        connection.commit()

        record = cursor.fetchone()

        return Tuition(record[0], record[1])

    def delete_tuition(self, tuitionid):  # Delete a  Tuition by ID  from Table
        sql = "DELETE FROM tuition WHERE tuitionid =%s"
        cursor = connection.cursor()
        cursor.execute(sql, [tuitionid])
        connection.commit()


# ----------- Testing section -------------
def _test():
    pass
    tuition = TuitionDAOImpl()
    emp = tuition.all_tuition()


if __name__ == '__main__':
    _test()
