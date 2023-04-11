
class Ad:
    def __init__(self, price, share_date, active=True):
        self.__price = price
        self.__share_date = share_date
        self.__active = active

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_share_date(self):
        return self.__share_date

    def set_share_date(self, share_date):
        self.__share_date = share_date

    def is_active(self):
        return self.__active

    def set_active(self, active):
        self.__active = active