import os
from enum import Enum

def base_image_name(email):
    return email.replace("@", "_")

class Path(Enum):
    IMAGE = os.getcwd().split("roomie")[0] + "\\roomie\\app\\commons\\image\\"
