from django.shortcuts import render,HttpResponse,redirect
from .Logic import authenticate,patientlist,patientFile,checkPatientList
from PatientRegistration.models import Patient
from doctorRegistration.models import Doctor


# Create your views here.


def home(request):
    did=request.session.get('did',False)
    if(did):
        doctor=Doctor.objects.get(did=did)
        patient_list=patientlist.getList(doctor.patients)
        return render(request,'doctorHome/home.html',{"patients":patient_list,"doctor":doctor})
    else:
        return redirect('/doctorlogin')



def patientprofile(request,patientid):
    did=request.session.get('did',False)
    if(did):
        patient=Patient.objects.get(pid=patientid.strip().upper())
        patient_file_name=patientFile.get(patientid.strip().upper())
        suggestions=patient.updates_from_doctors[:-1]
        return render(request,'doctorHome/patientProfile.html',{"patient":patient,"patient_file_name":patient_file_name,"suggestions":suggestions})
    else:
        return redirect('/doctorlogin')

def initiateTreatment(request,patientid):
    did=request.session.get('did',False)
    patient=Patient.objects.get(pid=patientid.upper())
    if(patient.doctorAllocatedID.upper()==did.upper()):
        patient.initiateTreatment=True;
        patient.updates_from_doctors.append({"notification":"The doctor has initiated the treatment, please stay tuned for further updates"})
        patient.save()
        return redirect('/doctorhome/patientprofile/'+patientid)
    else:
        return HttpResponse("The page you are looking for doesn't exists")
    if(did):
        pass
    else:
        return redirect('/doctorlogin')

def loginValidate(request):
    did=request.POST.get('id',False).upper().strip()
    password=request.POST.get('password',False)
    if(len(did)==0 or len(password)==0):
        return HttpResponse('false')
    else:
        value=authenticate.validate(did,password)
        if(value.upper()=='true'.upper()):
            request.session['did']=did
    return HttpResponse(value)

def login(request):
    did=request.session.get('did',False)
    if(did):
        return redirect('/doctorhome/')
    else:
        return redirect('/doctorlogin')


def logout(request):
    did=request.session.get('did',False)
    if(did):
        del request.session['did']
    return redirect('/management')


def suggestion(request,patientId):
    did=request.session.get('did',False)
    if(did):
        try:
            patient=Patient.objects.get(pid=patientId.upper().strip())
            if(patient.doctorAllocatedID.upper().strip() == did.upper().strip()):
                suggestion=request.POST['doctor_suggestion'].strip()
                patient.updates_from_doctors.insert(0,{"notification":suggestion})
                patient.save()
                return redirect('/doctorhome/patientprofile/'+patientId.upper().strip())
            else:
                raise Exception()
        except:
            return HttpResponse("The Page you are looking for dosen't exists")
    else:
        return redirect('/doctorlogin')


def medicine(request,patientid):
    print("Inside medicine")
    did=request.session.get('did',False)
    try:
        doctor=Doctor.objects.get(did=did)
        patient=Patient.objects.get(pid=patientid.strip().upper())
        patient_list=doctor.patients
        if(not checkPatientList.check(patientid,patient_list)):
            raise Exception()
        print(patientid)
        med_names=dict(request.POST)['medicine_name']
        med_directives=dict(request.POST)['directive']
        for medicine_name,directive in zip(med_names,med_directives):
            patient.medicine_list.append({"medicine_name":medicine_name,"medicine_directive":directive})
        patient.save()
        return redirect('/doctorhome/patientprofile/'+patientid)
    except:
        return HttpResponse("The page you are looking for doesn't exists")
