from abc import *

class Grade(ABC):
    @abstractmethod
    def __init__(self, email=None):
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
