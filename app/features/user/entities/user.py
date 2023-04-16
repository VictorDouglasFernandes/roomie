class User:
    def __init__(self, name: str, surname: str, birthday: str, sex: int, cpf: str, cellphone_number: str, email: str, password: str):
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
