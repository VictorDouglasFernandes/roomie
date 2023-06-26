from app.features.room.entities.property_ad import PropertyAd
from app.features.roomie.entities.roomie import Roomie
from app.features.user.entities.system_grade import SystemGrade


class User:
    def __init__(self, name=None, surname=None, birthday=None, sex=None, cpf=None, cellphone_number=None, email=None,
                 password=None, property_ad=None, roommate_ad=None, favorite_properties=None, system_grade=None):
        self.__name = None
        self.__surname = None
        self.__birthday = None
        self.__sex = None
        self.__cpf = None
        self.__cellphone_number = None
        self.__email = None
        self.__password = None
        self.__property_ad = None
        self.__roommate_ad = None
        self.__system_grade = None
        self.__favorite_properties = None
        if isinstance(name, str):
            self.__name = name
        if isinstance(surname, str):
            self.__surname = surname
        if isinstance(birthday, str):
            self.__birthday = birthday
        if isinstance(sex, str):
            self.__sex = sex
        if isinstance(cpf, str):
            self.__cpf = cpf
        if isinstance(cellphone_number, str):
            self.__cellphone_number = cellphone_number
        if isinstance(email, str):
            self.__email = email
        if isinstance(password, str):
            self.__password = password
        if isinstance(property_ad, PropertyAd):
            self.__property_ad = property_ad
        if isinstance(roommate_ad, Roomie):
            self.__roommate_ad = roommate_ad
        if isinstance(system_grade, SystemGrade):
            self.__system_grade = system_grade
        if isinstance(favorite_properties, list):
            self.__favorite_properties = favorite_properties

    @property
    def id(self):
        return self.email

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        if isinstance(name, str):
            self.__name = name

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname) -> None:
        if isinstance(surname, str):
            self.__surname = surname

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex) -> None:
        if isinstance(sex, str):
            self.__sex = sex

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday) -> None:
        if isinstance(birthday, str):
            self.__birthday = birthday

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf) -> None:
        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def cellphone_number(self):
        return self.__cellphone_number

    @cellphone_number.setter
    def cellphone_number(self, cellphone_number) -> None:
        if isinstance(cellphone_number, str):
            self.__cellphone_number = cellphone_number

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email) -> None:
        if isinstance(email, str):
            self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password) -> None:
        if isinstance(password, str):
            self.__password = password

    @property
    def property_ad(self):
        return self.__property_ad

    @property_ad.setter
    def property_ad(self, property_ad) -> None:
        if property_ad is None or isinstance(property_ad, PropertyAd):
            self.__property_ad = property_ad

    @property
    def roommate_ad(self):
        return self.__roommate_ad

    @roommate_ad.setter
    def roommate_ad(self, roommate_ad) -> None:
        if roommate_ad is None or isinstance(roommate_ad, Roomie):
            self.__roommate_ad = roommate_ad

    @property
    def system_grade(self):
        return self.__system_grade

    @system_grade.setter
    def system_grade(self, system_grade):
        self.__system_grade = system_grade

    @property
    def favorite_properties(self):
        return self.__favorite_properties

    @favorite_properties.setter
    def favorite_properties(self, favorite_properties):
        if isinstance(favorite_properties, list):
            self.__favorite_properties = favorite_properties

    def add_favorite_property(self, favorite_property):
        if isinstance(self.favorite_properties, list):
            self.favorite_properties.append(favorite_property)
        else:
            self.favorite_properties = [favorite_property]
