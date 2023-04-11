from app.commons.database.db_helper import DBHelper
from app.features.room.entities.room_ad import RoomAd


class RoomDB(DBHelper):
    __instance = None

    def __init__(self):
        super().__init__('rooms.pkl')

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def add(self, room: RoomAd):
        if isinstance(room, RoomAd) and (room.id, str):
            super().add(room.id, room)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
