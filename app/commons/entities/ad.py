from abc import *

class Ad(ABC):
    @abstractmethod
    def __init__(self, email=None, share_date=None, active=True, interested_users_emails=None):
        self.__email = None
        self.__share_date = None
        self.__active = None
        self.__interested_users_emails = None
        self.__email = email
        self.__share_date = share_date
        self.__active = active
        self.__interested_users_emails = interested_users_emails

    @property
    def id(self):
        return self.email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def share_date(self):
        return self.__share_date

    @share_date.setter
    def share_date(self, share_date):
        self.__share_date = share_date

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active):
        self.__active = active

    @property
    def interested_users_emails(self):
        return self.__interested_users_emails

    @interested_users_emails.setter
    def interested_users_emails(self, interested_users_emails):
        self.__interested_users_emails = interested_users_emails

    def add_interested_user_email(self, user_email):
        if isinstance(self.interested_users_emails, list):
            self.__interested_users_emails.append(user_email)
        else:
            self.__interested_users_emails = [user_email]