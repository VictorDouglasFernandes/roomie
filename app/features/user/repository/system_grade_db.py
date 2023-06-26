from app.commons.database.db_helper import DBHelper
from app.features.user.entities.system_grade import *


class SystemGradeDB(DBHelper):
    __instance = None

    def __init__(self):
        super().__init__('system_grade.pkl')

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def add(self, grade: SystemGrade):
        if isinstance(grade, SystemGrade) and (grade.email, str):
            super().add(grade.email, grade)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)