

class Roles:

    def __init__(self, roleid=0, rolename="", empid=0):
        self.roleid = roleid
        self.rolename = rolename
        self.empid = empid

    def json(self):
        return {
            'roleid': self.roleid,
            'rolename': self.rolename,
            'empid': self.empid,

        }

    @staticmethod
    def json_parse(json):  # convert to JSON format
        role = Roles()
        role.roleid = json["roleid"]
        role.rolename = json["rolename"]
        role.empid = json["empid"]

        return role

    def __repr__(self):
        return str(self.json())
