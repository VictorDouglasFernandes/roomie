from app.commons.database.db_helper import DBHelper
from app.features.roomie.entities.roomie import Roomie


class RoomieDB(DBHelper):
    __instance = None

    def __init__(self):
        super().__init__('roomies.pkl')

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def add(self, roomie: Roomie):
        if isinstance(roomie, Roomie) and (roomie.id, str):
            super().add(roomie.id, roomie)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)