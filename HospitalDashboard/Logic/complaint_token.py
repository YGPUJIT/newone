from HospitalDashboard.models import hospital

def getToken(hid,value):
    complaint_tokens=hospital.objects.get(hid=hid).complaint_on_doctors
    for token in complaint_tokens:
        if(token['token']==value):
            return token


def removeToken(hid,tokenID,did):
    Hospital=hospital.objects.get(hid=hid)
    cts=Hospital.complaint_on_doctors
    object_token=None
    for obj in cts:
        if obj['token']==tokenID and obj['did']==did:
            object_token=obj
            break
    if(object_token!=None):
        cts.remove(object_token)
        Hospital.complaint_on_doctors=cts
        print(Hospital.complaint_on_doctors)
        Hospital.save()