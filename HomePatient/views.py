from django.shortcuts import render,redirect
from django.http import HttpResponse
from PatientRegistration.models import Patient
from HospitalDashboard.models import hospital
from doctorRegistration.models import Doctor
import PatientRegistration
from django.views.decorators.cache import never_cache,cache_control
# from django.forms.models import model_to_dict
from .Logic.authenticatePatient import autheticatePatient
from .Logic import save_image,clear_cache,model_to_dict,assignHospital
from .Logic import allocateDoc,compalintToken,store_file
from .Logic.Symptoms import symptoms
from .Logic.ML import DiseasePrediction
from .Logic.WebToPdf import webPageToPdf
from Security.Logic.ML.FaceRec import train_model,extract_embeddings
import os
import json
from datetime import datetime



# Create your views here.

@cache_control(max_age=0, no_cache=True, no_store=True,must_revalidate=True)
def home(request):
    print("HOME ININI")
    pid=request.session.get('pid',False)
    if(pid):
        # try:
        patient=Patient.objects.filter(pid=pid).values()[0]
        request.session['patient']=json.dumps(patient)
        if(patient['regisitraionComplete']):
            Hospital=hospital.objects.get(hid=patient['hospitalRegistered'])
            if(patient['doctorAssigned']):
                doctor=Doctor.objects.get(did=patient['doctorAllocatedID'].upper())
                # if(len(patient['updates_from_doctors'])==0):
                #     check=False
                # else:
                    # check=True
            else:
                doctor=None
            return render(request,'HomePatient/index.html',{"patient":patient,"hospital":Hospital,"doctor":doctor})
        else:
            data_symptoms=symptoms.getSymptoms()
            return render(request,'HomePatient/registration.html',data_symptoms)
        # except:
        #     return HttpResponse("Error.Please try again later")
    else:
        return redirect('/registration')


def loginValidate(request):
    pid=request.POST['id'].upper().strip()
    password=request.POST['password']
    print(pid,password)
    if(len(pid)==0 or len(password)==0):
        return HttpResponse('false')
    else:
        check=autheticatePatient.loginValidate(pid,password)
        if(check.upper()=='true'.upper()):
            request.session['pid']=pid
    return HttpResponse(check)


@cache_control(max_age=0, no_cache=True, no_store=True)
def login(request):
    print("patient login")
    pid=request.session.get('pid',False)
    if(pid):
        return redirect('/home')
    else:
        return redirect('/patientlogin')


@cache_control(max_age=0, no_cache=True, no_store=True)
def logout(request):
    print("patient logout")
    if(request.session.get('pid',False)):
        del request.session['pid']
    return redirect('/')




def storeImage(request):
    print("STORE IMAGE")
    pid=request.session.get('pid',False)
    patient= json.loads(request.session.get('patient',False))
    if(not patient['regisitraionComplete']):
        if(request.method=='POST'):
            save_image.save(request.FILES,pid,patient)
            #later update the registartioncomplete as true
        clear_cache.clear()
        extract_embeddings.Embeddings().extract_embeddings()
        train_model.Train().train_model()
    return redirect('/home')



def storeData(request):
    print("STORE DATA")
    try:
        pid=request.session['pid']
        patient=Patient.objects.get(pid=pid)
        print(patient)
        if(request.POST['photo_opt']=='desktop'):
            storeImage(request)
        store_file.storePrevious(request,pid)
        s1=request.POST.get('s1','nan')
        s2=request.POST.get('s2','nan')
        s3=request.POST.get('s3','nan')
        s4=request.POST.get('s4','nan')
        symptoms_object={
            "s1":str(s1),"s2":str(s2),"s3":str(s3),"s4":str(s4)
        }
        patient.symptoms=symptoms_object
        try:
            patient_disease=DiseasePrediction.Symptoms(s1,s2,s3,s4).predictDisease()
            patient.disease_actual=patient_disease.strip()
        except:
            return HttpResponse('Error,while predicting disease')
        patient.regisitraionComplete=True
        hospitalID=assignHospital.assign(pid)
        Hospital=hospital.objects.get(hid=hospitalID)
        Hospital.patient.append({"pid":pid})
        patient_notification="Patient "+patient.first_name.upper()+" "+patient.last_name.upper()+" with id "+pid.upper()+" has registered to your hospital"
        Hospital.notifications.insert(0,{"notification":patient_notification})
        Hospital.save()
        patient.hospitalRegistered=hospitalID
        patient.save()
    except:
        print("Error at Store Data of Patient")
    return redirect('/home')



def allocateDoctor(request):
    pid=request.session.get('pid',False)
    if(pid):
        hid=Patient.objects.get(pid=pid).hospitalRegistered
        condition=request.POST['condition']
        allocateDoc.assign(pid,hid,condition)
        return redirect('/home/')
    else:
        return redirect('/patientlogin')


def complaint(request):
    pid=request.session.get('pid',False)
    patient=Patient.objects.get(pid=pid)
    # doctor=Doctor.objects.get(did=patient.doctorAllocatedID.upper())
    # if(not patient.doctorAllocatedID.upper()==doctorid):
    #     return HttpResponse("The page which you are looking for doesn't exists")
    if(pid):
        return render(request,'HomePatient/complaint.html',{"patient":patient})
    else:
        return redirect('/patientlogin')


def registerComplaint(request,doctorid):
    pid=request.session.get('pid',False)
    patient=Patient.objects.get(pid=pid)
    if(doctorid.upper()=="None".upper()):
        return HttpResponse("Doctor Not Allocated")
    try:
        doctor=Doctor.objects.get(did=patient.doctorAllocatedID.upper())
        if(not patient.doctorAllocatedID.upper()==doctorid):
            raise Exception()
    except:
        return HttpResponse("The page which you are looking for doesn't exists")
    if(pid):
        Hospital=hospital.objects.get(hid=patient.hospitalRegistered.upper())
        token=compalintToken.createToken()
        complaint_object={
            "token":token,
            "did":doctor.did,
            "complaint":request.POST['complaint-content'].strip(),
            "pid":pid,
            "time":datetime.now()
        }
        Hospital.complaint_on_doctors.append(complaint_object)
        Hospital.save()
        return redirect('/home/')
    else:
        return redirect('/patientlogin')



def downloadPharma(request):
    pid=request.session.get('pid',False)
    if(pid):
        patient=Patient.objects.get(pid=pid)
        medicines=patient.medicine_list
        doctor_id=patient.doctorAllocatedID.strip().upper()
        doctor=Doctor.objects.get(did=doctor_id)
        patient_name=patient.first_name+" "+patient.last_name
        html=webPageToPdf.htmlToPdfApi(patient_name,
        str(patient.age),patient.location['area']+", "+patient.location['city']+"-"+patient.location['pincode'],patient.pid,medicines,doctor.name,doctor.specilisation,"12/12/12")
        response=HttpResponse(content=html,content_type='application/pdf')
        return response
    else:
        return HttpResponse('Nothing')
