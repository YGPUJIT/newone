import os
import json
from Hospital.settings import BASE_DIR


def getSecialists():
    file_json=open(os.path.join(BASE_DIR,'doctorRegistration','Logic','json','specialist.json'),'r')
    return json.load(file_json)