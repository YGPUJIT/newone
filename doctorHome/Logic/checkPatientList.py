

def check(patientid,patient_list):
    for patient in patient_list:
        if(patientid.upper() == patient['pid'].upper()):
            return True
    return False