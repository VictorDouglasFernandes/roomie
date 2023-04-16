class RoomAd:
    def __init__(self, email: str, price=None, extra=None, images=None, district=None, type=None, roommates=None,
                 rooms=None, bathrooms=None, advance=None, smoker=None, pets=None, children=None, condominium=None,
                 garage=None, gym=None, lobby=None, pool=None, party_room=None):
        self.email = None
        self.price = None
        self.extra = None
        self.images = None
        self.district = None
        self.type = None
        self.roommates = None
        self.rooms = None
        self.bathrooms = None
        self.advance = None
        self.smoker = None
        self.pets = None
        self.children = None
        self.condominium = None
        self.garage = None
        self.gym = None
        self.lobby = None
        self.pool = None
        self.party_room = None
        if isinstance(email, str):
            self.email = email
        if isinstance(price, float):
            self.price = price
        if isinstance(extra, float):
            self.extra = extra
        if isinstance(images, list):
            self.images = images
        if isinstance(district, str):
            self.district = district
        if isinstance(type, str):
            self.type = type
        if isinstance(roommates, int):
            self.roommates = roommates
        if isinstance(rooms, int):
            self.rooms = rooms
        if isinstance(bathrooms, int):
            self.bathrooms = bathrooms
        if isinstance(advance, bool):
            self.advance = advance
        if isinstance(smoker, bool):
            self.smoker = smoker
        if isinstance(pets, bool):
            self.pets = pets
        if isinstance(children, bool):
            self.children = children
        if isinstance(condominium, bool):
            self.condominium = condominium
        if isinstance(garage, bool):
            self.garage = garage
        if isinstance(gym, bool):
            self.gym = gym
        if isinstance(lobby, bool):
            self.lobby = lobby
        if isinstance(pool, bool):
            self.pool = pool
        if isinstance(party_room, bool):
            self.party_room = party_room

    @property
    def id(self):
        return self.email
