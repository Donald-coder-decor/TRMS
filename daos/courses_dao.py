
from abc import abstractmethod, ABC


class CoursesDAO(ABC):

    @abstractmethod
    def create_courses(self, courses, empid):
        pass

    @abstractmethod
    def all_courses(self):
        pass

    @abstractmethod
    def get_courses(self, empid, courseid):
        pass

    @abstractmethod
    def get_courseID(self, courseid):
        pass

    @abstractmethod
    def update_courses(self, change):
        pass

    @abstractmethod
    def delete_courses(self, courseid):
        pass