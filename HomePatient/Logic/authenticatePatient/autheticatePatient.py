from PatientRegistration.models import Patient

def loginValidate(pid,password):
    try:
        patient=Patient.objects.get(pid=pid)
        print(patient)
        if(password==patient.password):
            return 'true'
        return 'false'
    except:
        return 'false'