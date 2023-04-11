from app.features.roomie.entities.ad import Ad


class RoommateAd(Ad):
    def __init__(self, price, share_date, roommate_type, living_type, about, is_student=False,
                 is_smoker=False, has_pets=False, has_children=False, has_job=False):
        super().__init__(price, share_date)
        self.__roommate_type = roommate_type
        self.__living_type = living_type
        self.__about = about
        self.__is_student = is_student
        self.__is_smoker = is_smoker
        self.__has_pets = has_pets
        self.__has_children = has_children
        self.__has_job = has_job

    def get_roommate_type(self):
        return self.__roommate_type

    def set_roommate_type(self, roommate_type):
        self.__roommate_type = roommate_type

    def get_living_type(self):
        return self.__living_type

    def set_living_type(self, living_type):
        self.__living_type = living_type

    def get_about(self):
        return self.__about

    def set_about(self, about):
        self.__about = about

    def is_student(self):
        return self.__is_student

    def set_student(self, is_student):
        self.__is_student = is_student

    def is_smoker(self):
        return self.__is_smoker

    def set_smoker(self, is_smoker):
        self.__is_smoker = is_smoker

    def has_pets(self):
        return self.__has_pets

    def set_pets(self, has_pets):
        self.__has_pets = has_pets

    def has_children(self):
        return self.__has_children

    def set_children(self, has_children):
        self.__has_children = has_children

    def has_job(self):
        return self.__has_job

    def set_job(self, has_job):
        self.__has_job = has_job
