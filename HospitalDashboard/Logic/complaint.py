from HospitalDashboard.models import hospital
from PatientRegistration.models import Patient
from doctorRegistration.models import Doctor
from datetime import datetime


def removeHash(value):
    return value.replace('#',"")

def getComplaints(hid):
    Complaints=hospital.objects.get(hid=hid).complaint_on_doctors
    return_value=[]
    for complaint in Complaints:
        did=complaint['did']
        pid=complaint['pid']
        Patient_name_first=Patient.objects.get(pid=pid).first_name
        Patient_name_last=Patient.objects.get(pid=pid).last_name
        Doctor_name=Doctor.objects.get(did=did).name
        value={
        "token":removeHash(complaint['token']),
        "doctorId":did,
        'doctorname':Doctor_name,
        "complaint_text":complaint['complaint'],
        "patientname":Patient_name_first+" "+Patient_name_last,
        "patientId":pid,
        "time":complaint['time'].strftime("%B,%Y %I:%S%p")
        }
        return_value.append(value)
    return return_value


