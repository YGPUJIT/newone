

def saveData(did,name,email,specialisation,hashValue,hid,doctor,doctor_temp):
    try:
        doctor.did=did
        doctor.name=name
        doctor.email=email
        doctor.specilisation=specialisation
        doctor_temp.did=did
        doctor_temp.hashValue=hid+hashValue
        doctor.hospital_id=hid
        doctor.save()
        doctor_temp.save()
    except:
        raise