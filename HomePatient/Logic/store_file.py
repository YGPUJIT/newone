import os
from django.core.files.storage import FileSystemStorage
from Hospital.settings import BASE_DIR
import shutil

def storePrevious(request,pid):
    try:
        path=os.path.join(BASE_DIR,'HomePatient','Logic','PatientFile',pid)
        if(os.path.exists(path)):
            shutil.rmtree(path)
        fs=FileSystemStorage(path)
        previous_record=request.FILES['previous_record']
        print(previous_record)
        image_type=previous_record.name.split('.')[-1]
        fs.save(str(pid)+"."+image_type,previous_record)
    except:
        print("Error occured at previous record storage")
    