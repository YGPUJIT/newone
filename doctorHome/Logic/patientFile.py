from Hospital.settings import BASE_DIR
import os

def get(pid):
    try:
        path=os.path.join(BASE_DIR,'HomePatient','Logic','PatientFile',pid)
        file_name=os.listdir(path)[0]
        return os.path.join(pid,file_name).replace("\\","/")
    except:
        return False