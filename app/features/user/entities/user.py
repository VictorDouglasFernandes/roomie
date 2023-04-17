
class User:
    def __init__(self, name=None, birthday=None, sex=None, cpf=None, cellphone_number=None, email=None, password=None):
        self.__name = None
        self.__birthday = None
        self.__sex = None
        self.__cpf = None
        self.__cellphone_number = None
        self.__email = None
        self.__password = None
        self.__name = name
        self.__birthday = birthday
        self.__sex = sex
        self.__cpf = cpf
        self.__cellphone_number = cellphone_number
        self.__email = email
        self.__password = password

    @property
    def id(self):
        return self.__email

    @property
    def name(self):
        return self.__name

    @property
    def birthday(self):
        return self.__birthday

    @property
    def sex(self):
        return self.__sex

    @property
    def cpf(self):
        return self.__cpf

    @property
    def cellphone_number(self):
        return self.__cellphone_number

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password
