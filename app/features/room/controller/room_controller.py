from app.features.room.entities.room_ad import RoomAd
from app.features.room.repository.room_db import RoomDB


class RoomController:
    def __init__(self):
        self.dao = RoomDB()

    @property
    def rooms(self):
        return self.dao.get_all()

    def ad_room_verification(self, room: RoomAd):
        _list = []
        if room.district is None:
            _list.append('bairro')
        if room.price is None:
            _list.append('aluguel')
        if room.extra is None:
            _list.append('despesas')
        if room.type is None:
            _list.append('tipo')
        if room.roomates is None:
            _list.append('moradores')
        if room.rooms is None:
            _list.append('quartos')
        if room.bathrooms is None:
            _list.append('banheiros')

        return _list

    def add_ad_room(self, room: RoomAd):
        self.dao.add(room)
