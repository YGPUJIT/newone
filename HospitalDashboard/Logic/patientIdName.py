from HospitalDashboard.models import hospital
from PatientRegistration.models import Patient

def get_patient_id_name(hid):
    patient_list=[]
    Hospital=hospital.objects.get(hid=hid)
    hospital_patients=Hospital.patient
    for patient in hospital_patients:
        pid=patient['pid']
        patient_object=Patient.objects.get(pid=pid)
        name=patient_object.first_name+" "+patient_object.last_name
        patient_list.append({"id":pid,"name":name})
    return patient_list