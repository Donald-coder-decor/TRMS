
class Employee:
    def __init__(self, empid=0, firstname="", midname="", lastname="", email="" ,address="",emprole="",   username="",password="", phone=0 ):
        self.empid = empid
        self.firstname = firstname
        self.midname =midname
        self.lastname = lastname
        self.email = email
        self.address = address
        self.emprole = emprole
        self.username = username
        self.password = password
        self.phone = phone

    def json(self):
        return {
            'empid': self.empid,
            'firstname': self.firstname,
            'midlname': self.midname,
            'lastname': self.lastname,
            'email': self.email,
            'address': self.address,
            'emprole': self.emprole,
            'username': self.username,
            'password': self.password,
            'phone': self.phone,

        }

    @staticmethod
    def json_parse(json): # convert to JSON format
        employee = Employee()

        employee.empid = json["empid"] if 'empid' in json else 0
        employee.firstname = json["firstname"]
        employee.midname = json["midname"]
        employee.lastname = json["lastname"]
        employee.email = json["email"]
        employee.address = json["address"]
        employee.emprole = json["emprole"]
        employee.username = json["username"]
        employee.password = json["password"]
        employee.phone = json["phone"]
        return employee

    def __repr__(self):
        return str(self.json())
