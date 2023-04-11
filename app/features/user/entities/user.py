
class User:
    def __init__(self, name, birthday, sex, cpf, cellphone_number, email, password):
        self.__name = name
        self.__birthday = birthday
        self.__sex = sex
        self.__cpf = cpf
        self.__cellphone_number = cellphone_number
        self.__email = email
        self.__password = password

    def name(self):
        return self.__name

    def birthday(self):
        return self.__birthday

    def sex(self):
        return self.__sex

    def cpf(self):
        return self.__cpf

    def cellphone_number(self):
        return self.__cellphone_number

    def email(self):
        return self.__email

    def password(self):
        return self.__password
