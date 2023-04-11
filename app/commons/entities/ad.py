class Ad:
    def __init__(self, price, share_date, active=True):
        self.__price = price
        self.__share_date = share_date
        self.__active = active

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

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
