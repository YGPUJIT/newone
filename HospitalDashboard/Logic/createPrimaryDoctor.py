from doctorRegistration.models import Doctor
from doctorRegistration.Logic import doctorId

def assignPrimaryDoctor(hid,hname):
    PrimaryDoctor=Doctor()
    did=doctorId.generate()
    name="Hospital Management Doctor-"+hname
    hospital_id=hid.upper()
    email='doctorgeek1947@gmail.com'
    password='qwerty'
    specilisation='Hospital Primary Care'
    registrationConfirmed=True
    PrimaryDoctor.did=did
    PrimaryDoctor.name=name
    PrimaryDoctor.hospital_id=hospital_id
    PrimaryDoctor.email=email
    PrimaryDoctor.password=password
    PrimaryDoctor.specilisation=specilisation
    PrimaryDoctor.registrationConfirmed=registrationConfirmed
    PrimaryDoctor.save()
    return did

