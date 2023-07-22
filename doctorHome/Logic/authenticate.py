from doctorRegistration.models import Doctor

def validate(did,password):
    print("Doctor login validation IN")
    try:
        doctor=Doctor.objects.get(did=did)
        if(str(doctor.registrationConfirmed).upper()=='true'.upper()):
            doctor_password=doctor.password
            if(password==doctor_password):
                return 'true'
        return 'false'
    except:
        return 'false'