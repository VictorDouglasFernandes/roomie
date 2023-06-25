from app.commons.entities.grade import Grade

class SystemGrade(Grade):
    def __init__(self, email=None, description=None):
        super().__init__(email)
        self.__description = None
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description
