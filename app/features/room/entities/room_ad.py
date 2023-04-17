from app.commons.entities.ad import *

class RoomAd(Ad):
    def __init__(self, email: str, share_date=None, active=None, rent_money=None, expenses_money=None, pictures=None, district=None, type=None, residents=None,
                 rooms=None, bathrooms=None, has_collateral=None, accept_smoker=None, accept_pets=None, accept_childs=None, private_condominium=None,
                 has_garage=None, has_gym=None, has_corcierge=None, has_pool=None, has_party_hall=None):
        super().__init__(email, share_date, active)
        self.__rent_money = None
        self.__expenses_money = None
        self.__pictures = None
        self.__district = None
        self.__type = None
        self.__residents = None
        self.__rooms = None
        self.__bathrooms = None
        self.__has_collateral = None
        self.__accept_smoker = None
        self.__accept_pets = None
        self.__accept_childs = None
        self.__private_condominium = None
        self.__has_garage = None
        self.__has_gym = None
        self.__has_corcierge = None
        self.__has_pool = None
        self.__has_party_hall = None
        if isinstance(email, str):
            self.__email = email
        if isinstance(rent_money, float):
            self.__rent_money = rent_money
        if isinstance(expenses_money, float):
            self.__expenses_money = expenses_money
        if isinstance(pictures, list):
            self.__pictures = pictures
        if isinstance(district, str):
            self.__district = district
        if isinstance(type, str):
            self.__type = type
        if isinstance(residents, int):
            self.__residents = residents
        if isinstance(rooms, int):
            self.__rooms = rooms
        if isinstance(bathrooms, int):
            self.__bathrooms = bathrooms
        if isinstance(has_collateral, bool):
            self.__has_collateral = has_collateral
        if isinstance(accept_smoker, bool):
            self.__accept_smoker = accept_smoker
        if isinstance(accept_pets, bool):
            self.__accept_pets = accept_pets
        if isinstance(accept_childs, bool):
            self.__accept_childs = accept_childs
        if isinstance(private_condominium, bool):
            self.__private_condominium = private_condominium
        if isinstance(has_garage, bool):
            self.__has_garage = has_garage
        if isinstance(has_gym, bool):
            self.__has_gym = has_gym
        if isinstance(has_corcierge, bool):
            self.__has_corcierge = has_corcierge
        if isinstance(has_pool, bool):
            self.__has_pool = has_pool
        if isinstance(has_party_hall, bool):
            self.__has_party_hall = has_party_hall

    @property
    def id(self):
        return self.email

    @property
    def district(self):
        return self.__district

    @district.setter
    def district(self, district):
        self.__district = district


    @property
    def rent_money(self):
        return self.__rent_money

    @rent_money.setter
    def rent_money(self, rent_money):
        self.__rent_money = rent_money

    @property
    def expenses_money(self):
        return self.__expenses_money

    @expenses_money.setter
    def expenses_money(self, expenses_money):
        self.__expenses_money = expenses_money

    @property
    def residents(self):
        return self.__residents

    @residents.setter
    def residents(self, residents):
        self.__residents = residents

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms):
        self.__rooms = rooms

    @property
    def bathrooms(self):
        return self.__bathrooms

    @bathrooms.setter
    def bathrooms(self, bathrooms):
        self.__bathrooms = bathrooms

    @property
    def has_collateral(self):
        return self.__has_collateral

    @has_collateral.setter
    def has_collateral(self, has_collateral):
        self.__has_collateral = has_collateral

    @property
    def accept_smoker(self):
        return self.__accept_smoker

    @accept_smoker.setter
    def accept_smoker(self, accept_smoker):
        self.__accept_smoker = accept_smoker

    @property
    def has_pets(self):
        return self.__has_pets

    @has_pets.setter
    def has_pets(self, has_pets):
        self.__has_pets = has_pets

    @property
    def has_childs(self):
        return self.__has_childs

    @has_childs.setter
    def has_childs(self, has_childs):
        self.__has_childs = has_childs

    @property
    def private_condominium(self):
        return self.__private_condominium

    @private_condominium.setter
    def private_condominium(self, private_condominium):
        self.__private_condominium = private_condominium

    @property
    def has_garage(self):
        return self.__has_garage

    @has_garage.setter
    def has_garage(self, has_garage):
        self.__has_garage = has_garage

    @property
    def has_gym(self):
        return self.__has_gym

    @has_gym.setter
    def has_gym(self, has_gym):
        self.__has_gym = has_gym

    @property
    def has_concierge(self):
        return self.__has_concierge

    @has_concierge.setter
    def has_concierge(self, has_concierge):
        self.__has_concierge = has_concierge

    @property
    def has_pool(self):
        return self.__has_pool

    @has_pool.setter
    def has_pool(self, has_pool):
        self.__has_pool = has_pool

    @property
    def has_party_hall(self):
        return self.__has_party_hall

    @has_party_hall.setter
    def has_party_hall(self, has_party_hall):
        self.__has_party_hall = has_party_hall

    @property
    def pictures(self):
        return self.__pictures

    @pictures.setter
    def pictures(self, pictures):
        self.__pictures = pictures