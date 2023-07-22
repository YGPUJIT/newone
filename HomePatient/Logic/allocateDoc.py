from PatientRegistration.models import Patient
from HospitalDashboard.models import hospital
from doctorRegistration.models import Doctor
from Hospital.settings import BASE_DIR
import os
import json

def assign(pid,hid,condition):
    print("ASSIGN")
    diseaseMapper=json.load(open(os.path.join(BASE_DIR,'HomePatient','Logic','json','diseaseMapper.json'),'r'))
    # print(diseaseMapper['common cold'])
    patient=Patient.objects.get(pid=pid)
    patient_disease=patient.disease_actual
    Hospital=hospital.objects.get(hid=hid)
    hospital_doctors=Hospital.doctors

    for doctorid in hospital_doctors:
        doctor_object=Doctor.objects.get(did=doctorid['did'])
        print(doctor_object.specilisation.lower(),diseaseMapper[patient_disease.lower()][0].lower())
        if(doctor_object.registrationConfirmed and patient_disease.lower() in diseaseMapper and doctor_object.specilisation.lower()==diseaseMapper[patient_disease.lower()][0].lower()):
            print(doctor_object.specilisation.lower(),diseaseMapper[patient_disease.lower()][0].lower())
            doctor_object.patients.append({"pid":pid})
            patient.symptoms_explanation=condition
            patient.doctorAssigned=True            
            patient.doctorAllocatedID=doctorid['did']
            patient_notification="Patient "+patient.first_name.upper()+" "+patient.last_name.upper()+" with id "+pid.upper()+" has been allocated to Dr. "+doctor_object.name.upper()+" with id "+doctor_object.did.upper()
            Hospital.notifications.insert(0,{"notification":patient_notification})
            Hospital.save()
            doctor_object.save()
            patient.save()
            return

    for doctorid in hospital_doctors:
        doctor_object=Doctor.objects.get(did=doctorid['did'])
        if(doctor_object.specilisation.lower()=="Hospital Primary Care".lower()):
            doctor_object.patients.append({"pid":pid})
            patient.symptoms_explanation=condition
            patient.doctorAssigned=True            
            patient.doctorAllocatedID=doctorid['did']
            patient_notification="Patient "+patient.first_name.upper()+" "+patient.last_name.upper()+" with id "+pid.upper()+" has been allocated to Dr. "+doctor_object.name.upper()+" with id "+doctor_object.did.upper()
            Hospital.notifications.insert(0,{"notification":patient_notification})
            Hospital.save()
            doctor_object.save()
            patient.save()
            return
    
    

       