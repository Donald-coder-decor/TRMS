

class Courses:

    def __init__(self, courseid=0, coursename="", empid=0):
        self.courseid = courseid
        self.coursename = coursename
        self.empid = empid

    def json(self):
        return {
            'courseid': self.courseid,
            'coursename': self.coursename,
            'empid': self.empid,

        }

    @staticmethod
    def json_parse(json):  # convert to JSON format
        course = Courses()
        course.courseid = json["courseid"] if "courseid" in json else 0
        course.coursename = json["coursename"]
        course.empid = json["empid"]
        return course

    def __repr__(self):
        return str(self.json())
