import os
from enum import Enum


class Path(Enum):
    IMAGE = os.getcwd().split("roomie")[0] + "\\roomie\\app\\commons\\image\\"