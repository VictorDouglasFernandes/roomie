from app.commons.entities.ad import Ad


class Roomie(Ad):
    def __init__(self, price, share_date, active, roommate_type, living_type, about, is_student=False,
                 is_smoker=False, has_pets=False, has_children=False, has_job=False):
        super().__init__(price, share_date, active)
        self.__roommate_type = roommate_type
        self.__living_type = living_type
        self.__about = about
        self.__is_student = is_student
        self.__is_smoker = is_smoker
        self.__has_pets = has_pets
        self.__has_children = has_children
        self.__has_job = has_job

    @property
    def roommate_type(self):
        return self.__roommate_type

    @roommate_type.setter
    def roommate_type(self, roommate_type):
        self.__roommate_type = roommate_type

    @property
    def living_type(self):
        return self.__living_type

    @living_type.setter
    def living_type(self, living_type):
        self.__living_type = living_type

    @property
    def about(self):
        return self.__about

    @about.setter
    def about(self, about):
        self.__about = about

    @property
    def is_student(self):
        return self.__is_student

    @is_student.setter
    def is_student(self, is_student):
        self.__is_student = is_student

    @property
    def is_smoker(self):
        return self.__is_smoker

    @is_smoker.setter
    def is_smoker(self, is_smoker):
        self.__is_smoker = is_smoker

    @property
    def has_pets(self):
        return self.__has_pets

    @has_pets.setter
    def has_pets(self, has_pets):
        self.__has_pets = has_pets

    @property
    def has_children(self):
        return self.__has_children

    @has_children.setter
    def has_children(self, has_children):
        self.__has_children = has_children

    @property
    def has_job(self):
        return self.__has_job

    @has_job.setter
    def has_job(self, has_job):
        self.__has_job = has_job
