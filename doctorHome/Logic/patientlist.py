from PatientRegistration.models import Patient
import os
from Hospital.settings import BASE_DIR


def getList(patient_list):
    return_value=[]
    for obj in patient_list:
        pid=obj['pid']
        patient=Patient.objects.get(pid=pid)
        directory_name=patient.pid.upper()+"-"+patient.first_name.upper()
        link=os.path.join(BASE_DIR,'Security','Logic','ML','FaceRec','dataset',directory_name)
        file_name=os.listdir(link)[0]
        patient.href="/static/"+directory_name+"/"+file_name
        return_value.append(patient)
    return return_value