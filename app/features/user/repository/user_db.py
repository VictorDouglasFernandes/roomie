from app.commons.database.db_helper import DBHelper
from app.features.room.entities.room_ad import RoomAd
from app.features.user.entities.user import User


class UserDB(DBHelper):
    __instance = None

    def __init__(self):
        super().__init__('users.pkl')

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def add(self, user: User):
        if isinstance(user, User) and (user.id, str):
            super().add(user.id, user)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
