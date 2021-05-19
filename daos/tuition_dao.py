

from abc import abstractmethod, ABC


class TuitionDAO(ABC):

    @abstractmethod
    def create_tuition(self, empid, courseid, tuition):
        pass

    # @abstractmethod
    # def create_tuition_id(self, tuitionid):
    #     pass

    @abstractmethod
    def get_tuition(self, empid, tutionid):
        pass

    @abstractmethod
    def all_tuition(self):
        pass

    @abstractmethod
    def update_tuition(self, change):
        pass

    @abstractmethod
    def delete_tuition(self, tuitionid):
        pass



