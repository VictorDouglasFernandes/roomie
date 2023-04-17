from app.commons.entities.ad import Ad


class Roomie(Ad):
    def __init__(self, email=None, price=None, share_date=None, active=None, roommate_type=None, living_type=None,
                 about=None, is_student=False,
                 is_smoker=False, has_pets=False, has_children=False, has_job=False, picture=None):
        super().__init__(email, share_date, active)
        self.__price = None
        self.__roommate_type = None
        self.__living_type = None
        self.__about = None
        self.__is_student = None
        self.__is_smoker = None
        self.__has_pets = None
        self.__has_children = None
        self.__has_job = None
        self.__picture = None
        self.__price = price
        self.__roommate_type = roommate_type
        self.__living_type = living_type
        self.__about = about
        self.__is_student = is_student
        self.__is_smoker = is_smoker
        self.__has_pets = has_pets
        self.__has_children = has_children
        self.__has_job = has_job
        self.__picture = picture

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

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

    @property
    def picture(self):
        return self.__picture

    @picture.setter
    def picture(self, picture):
        self.__picture = picture
