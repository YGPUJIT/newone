from django.shortcuts import render,HttpResponse,redirect
from django.http import StreamingHttpResponse
from Security.Logic import controller,combine_name_id,patient_information,sendMailToHospital,Check
from Security.Logic.ML.FaceRec import train_model,extract_embeddings
from HomePatient.Logic import clear_cache
from django.core.files.storage import FileSystemStorage
from PatientRegistration.models import Patient
from django.forms import model_to_dict
import os
from Hospital.settings import BASE_DIR
import json
from HospitalDashboard.models import hospital
import datetime

# Create your views here.



def index(request):
    # clear_cache.clear()
    # extract_embeddings.Embeddings().extract_embeddings()
    # train_model.Train().train_model()
    hospital_id=request.session['sid'].strip().upper()
    data=dict(map(combine_name_id.combine,Patient.objects.filter(hospitalRegistered=hospital_id).values_list('first_name','pid')))
    users_json=open(os.path.join(os.path.dirname(__file__),'Logic','json','user_name_id.json'),'w')
    json.dump(data,users_json)
    return render(request,'Security/index.html')


def loginPage(request):
    sid=request.session.get('sid',False)
    if(sid):
        return redirect('/Security')
    else:
        return render(request,'Security/login.html')


def loginValidate(request):
    hid=request.POST['hid'].strip().upper()
    request.session['sid']=hid
    print("INIININ",hid)
    try:
        Hospital=hospital.objects.get(hid=hid)
        return redirect('/Security')
    except:
        return redirect('/')

def Video(request):
    users_json=open(os.path.join(os.path.dirname(__file__),'Logic','json','user_name_id.json'),'r')
    data=dict(json.load(users_json))
    StreamingHttpResponse=controller.StreamingHttp(request,data)
    return StreamingHttpResponse

    
def toggle(request):
    return controller.toggle(request)


def stop(request):
    controller.stop(request)
    return HttpResponse('')



def getOffender(request):
    # value=json.dumps(controller.return_offernder()
    # print(type(controller.return_offernder()))
    value=json.dumps(controller.return_offernder())
    return HttpResponse(value)


def removeOffender(request):
    pid=request.GET['id']
    controller.delete_offender(pid)
    return HttpResponse(controller.return_offernder())


def getInformation(request):
    value=request.GET['searchId'].upper()
    patient=None
    print("Get Information")
    info=[]
    try:
        patient=Patient.objects.filter(pid=value).values()[0]
        info=dict(patient_information.getStructuredDocument(patient))
        print(info)
    except:
        return HttpResponse("Please enter vaid ID")
    return HttpResponse(json.dumps(info))


def protocolBreached(request):
    pid=request.GET['searchId'].strip().upper()
    hid=request.session['sid']
    Hospital=hospital.objects.get(hid=hid)
    time=str(datetime.datetime.today())
    Hospital.protocol_breached=Check.checkAndAdd(pid,Hospital.protocol_breached,time)
    Hospital.save()
    sendMailToHospital.sendMail(Hospital,pid,time)
    return HttpResponse("")