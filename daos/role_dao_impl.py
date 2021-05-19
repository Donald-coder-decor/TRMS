from daos.employe_dao_impl import EmployeeDAOImpl
from exceptions.resource_not_found import ResourceNotFound

from models.role import Roles
from util.db_connection import connection
from daos.role_dao import RoleDAO


class RoleDAOImpl(RoleDAO):

    # def create_role(self, roles, empid):  # Create new Roles
    #
    #     # check if employee exist before creating a assigning a role: else raise an error (404)
    #     try:
    #         exist_empid = EmployeeDAOImpl()
    #         exist_empid.get_employee(empid)
    #     except ResourceNotFound as r:
    #         raise r
    #
    #     sql = "INSERT INTO roles VALUES(DEFAULT, %s, %s) RETURNING *"
    #     cursor = connection.cursor()
    #     cursor.execute(sql, (roles.rolename, roles.empid))
    #     connection.commit()
    #     record = cursor.fetchone()
    #
    #     return Roles(Roles(record[0], record[1], record[2]))

    def all_role(self):  # Retrieve all Role from Role and return
        sql = "SELECT * FROM roles"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        roles_list = []
        for record in records:
            role = Roles(record[0], record[1], record[2])
            roles_list.append(role.json())
        return roles_list

    # def get_role(self, roleid):  # Retrieve a single Role by passing a RoleID
    #
    #     sql = "SELECT * FROM roles WHERE roleid =%s"
    #     cursor = connection.cursor()
    #     cursor.execute(sql, [roleid])
    #     record = cursor.fetchone()
    #
    #     if record:
    #         return Roles(record[0], record[1], record[2])
    #     else:
    #         return f'Employee ID  {roleid} - Not found'
    #
    # def create_role_id(self, roleid):
    #     pass
    # ================================================================================================

    # def get_role(self, empid, roleid):  # Retrieve a single Role  Assigned to an employee
    #
    #     sql = "SELECT * FROM roles WHERE roleid =%s"
    #     cursor = connection.cursor()
    #     cursor.execute(sql, [roleid])
    #     record = cursor.fetchone()
    #
    #     if record:
    #         return Roles(record[0], record[1], record[2])
    #     else:
    #         raise ResourceNotFound(f"Role with id: {roleid} - Not Found")

    # ================================================================================================

    def update_role(self, change, roleid):  # Update Role Table
        sql = "UPDATE roles SET rolename = %s where roleid=%s"
        cursor = connection.cursor()
        cursor.execute(sql, (change.rolename, change.roleid))
        connection.commit()

    def delete_role(self, roleid):  # Delete a role  from Table
        sql = "DELETE FROM roles WHERE roleid =%s"
        cursor = connection.cursor()
        cursor.execute(sql, [roleid])
        connection.commit()


# ----------- Testing section -------------
def _test():
    pass
    role = RoleDAOImpl()
    emp = role.all_role()
    print(emp)


if __name__ == '__main__':
    _test()
