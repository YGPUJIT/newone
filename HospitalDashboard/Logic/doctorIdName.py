from HospitalDashboard.models import hospital
from doctorRegistration.models import Doctor



def get_Doctor_Name_Id(hid):
    hospital_object=hospital.objects.get(hid=hid)
    doctor_list=hospital_object.doctors
    doctor_name_id=[]
    for doc in doctor_list:
        doctorID=doc['did']
        doctor_object=Doctor.objects.get(did=doctorID)
        if(doctor_object.registrationConfirmed):
            doctor_name=doctor_object.name
            doctor_name_id.append({"name":doctor_name,"Id":doctorID})
    return doctor_name_id
