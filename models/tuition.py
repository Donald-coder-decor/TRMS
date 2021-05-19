from psycopg2._psycopg import Date, Time


class Tuition:

    def __init__(self, tuitionid=0, locations="", description="",  gradeformat="", eventype="",
                 workrelate="",empid=0,   submision_status="Pending", costs=0, firsname_lastname="", amount_awarded=0,
                 amount_available=0, approval="", reject="", reason=""):
        self.tuitionid = tuitionid
        self.locations = locations
        self.description = description
        self.gradeformat = gradeformat
        self.eventype = eventype
        self.workrelate = workrelate
        self.empid = empid
        self.submision_status = submision_status
        self.costs = costs
        self.firsname_lastname = firsname_lastname
        self.amount_awarded = amount_awarded
        self.amount_available = amount_available
        self.approval = approval
        self.reject = reject
        self.reason = reason


    def json(self):
        return {
            'tuitionid': self.tuitionid,
            'locations': self.locations,
            'description': self.description,
            'gradeformat': self.gradeformat,
            'eventype': self.eventype,
            'workrelate': self.workrelate,
            'empid': self.empid,
            'submision_status': self.submision_status,
            'costs': self.costs,
            'firsname_lastname': self.firsname_lastname,
            'amount_awarded': self.amount_awarded,
            'amount_available': self.amount_available,
            'approval': self.approval,
            'reason': self.reason,

        }

    @staticmethod
    def json_parse(json):  # convert to JSON format
        tuition = Tuition()
        tuition.tuitionid = json["tuitionid"]
        tuition.locations = json["locations"]
        tuition.description = json["description"]
        tuition.gradeformat = json["gradeformat"]
        tuition.eventype = json["eventype"]
        tuition.workrelate = json["workrelate"]
        tuition.empid = json["empid"]
        tuition.submision_status = json["submision_status"]
        tuition.costs = json["costs"]
        tuition.firsname_lastname = json["firsname_lastname"]
        tuition.amount_awarded = json["amount_awarded"]
        tuition.amount_available = json["amount_available"]
        tuition.approval = json["approval"]
        tuition.reason = json["reason"]

        return tuition

    def __repr__(self):
        return str(self.json())
