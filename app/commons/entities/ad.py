class Ad:
    def __init__(self, email=None, share_date=None, active=True):
        self.__email = None
        self.__share_date = None
        self.__active = None
        self.__email = email
        self.__share_date = share_date
        self.__active = active

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
