from datetime import *

from app.features.room.entities.room import Room


class Property:
    def __init__(self, name: str, district: str):
        if isinstance(name, str):
            self.name = name
        if isinstance(district, str):
            self.district = district
        self.rooms = []
        self.active = False
        self.share_date

    def add_room(self, room: Room):
        if isinstance(room, Room):
            self.rooms.append(room)

    @property
    def active(self):
        return self.active

    @active.setter
    def active(self, active: bool):
        if isinstance(active, bool):
            self.active = active

    @property
    def share_date(self):
        return self.share_date

    @share_date.setter
    def share_date(self, share_date: datetime):
        if isinstance(share_date, str):
            self.share_date = share_date
