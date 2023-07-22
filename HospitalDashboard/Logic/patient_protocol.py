from PatientRegistration.models import Patient
from HospitalDashboard.models import hospital

def Patient_id_time_protocol(hid):
    protocol_breached_array=[]
    Hospital=hospital.objects.get(hid=hid)
    protocol_breached=Hospital.protocol_breached
    for pb in protocol_breached:
        patient=Patient.objects.get(pid=pb['pid'])
        name=patient.first_name+" "+patient.last_name
        time=pb['date_time']
        protocol_breached_array.append({"name":name,'time':time,'pid':pb['pid']})
    return protocol_breached_array
