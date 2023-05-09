from app.commons.database.db_helper import DBHelper
from app.features.room.entities.property_ad import PropertyAd


class RoomDB(DBHelper):
    __instance = None

    def __init__(self):
        super().__init__('rooms.pkl')

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def add(self, room: PropertyAd):
        if isinstance(room, PropertyAd) and (room.id, str):
            super().add(room.id, room)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
