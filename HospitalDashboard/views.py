from django.shortcuts import HttpResponse,render,redirect
from .Logic import randomId,longitude_latitude,checkAccount
from .models import hospital
from doctorRegistration.models import Doctor
from PatientRegistration.models import Patient
from HospitalDashboard.models import hospital
from .Logic import HospitalSendMail,removeComplaint,patientIdName
from .Logic import doctorIdName,complaint,createPrimaryDoctor,patient_protocol,complaint_token, send_email_doctor
from datetime import datetime
import json
# Create your views here.


def registration(request):
    print("Hospital Registration")
    if(request.session.get('hid',False)):
        del request.session['hid']
    return render(request,'HospitalDashboard/registration.html')


def storeData(request):
    print("Hospital Registration save data")
    if(request.session.get('hid',False)):
        del request.session['hid']
    try:
        Hospital=hospital()
        hid_value=randomId.generateRandomId("HO")
        Hospital.hid=hid_value
        Hospital.hospital_name=request.POST['hname'].strip()
        Hospital.password=request.POST['password'].strip()
        city=request.POST['city']
        area=request.POST['area'].strip()
        Hospital.mailid=str(request.POST['mail'].strip())
        pin_code=request.POST['pcode'].strip()
        lon_lat=longitude_latitude.get_lon_lat(city,area,pin_code)
        Hospital.doctors=[]
        Hospital.patient=[]
        Hospital.security=None
        Hospital.beds={'normal_beds':0,'icu_beds':0}
        Hospital.location={
            'city':city,
            'pincode':pin_code,
            'area':area,
            'longitude':lon_lat['longitude'],
            'latitude':lon_lat['latitude'],
            'country':'India'
        }
        notification="Hospital Registered with ID "+hid_value+" at "+datetime.utcnow().strftime("%B,%Y %I:%S%p")
        Hospital.notifications.append({"notification":notification})
        PrimaryDoctorID=createPrimaryDoctor.assignPrimaryDoctor(hid_value,request.POST['hname'].strip())
        Hospital.doctors.append({"did":PrimaryDoctorID})
        Hospital.save()
        HospitalSendMail.sendMail(request.POST['mail'].strip(),hid_value)
    except:
        return HttpResponse('Some error please try again later')
    return redirect('/hospitallogin')


def home(request):
    hid=request.session.get('hid',False)
    if(hid):
        Hospital=hospital.objects.get(hid=hid)
        qa={"qa":[
        {"question":'Dashboard',"answer":"Click here to visit dashboard.","href":"/hospital/dashboard","src":"/static/HospitalDashboard/images/dashboard.png"},
        {"question":"Complaints","answer":"Click here to view various complaints.","href":"/hospital/complaints","src":"/static/HospitalDashboard/images/complaint.jpg"},
        {'question':"Doctor Registration",'answer':"click here to add new doctors to your hospital.","href":"/doctor/registration","src":"/static/HospitalDashboard/images/registration.jpg"}],
        "notifications":Hospital.notifications}
        return render(request,'HospitalDashboard/home.html',qa)
    else:
        return redirect('/hospitallogin')


def dashboard(request):
    hid=request.session.get('hid',False)
    if(hid):
        # try:
        doctors_list=doctorIdName.get_Doctor_Name_Id(hid)
        patient_list=patientIdName.get_patient_id_name(hid)
        protocol_breached=patient_protocol.Patient_id_time_protocol(hid)
        context={"doctors":doctors_list,"patients":patient_list,'protocol':protocol_breached}
        return render(request,'HospitalDashboard/dashboard.html',context)
        # except:
        #     return HttpResponse("Please try again later")
    else:
        return redirect('/hospitallogin')



def loginValidate(request):
    print('Hospital Login')
    hid=request.session.get('hid',False)
    if(hid):
        return redirect('/hospital/home')
    try:
        hid= request.POST['id'].strip().upper()
        password=request.POST['password'].strip()
        if(len(hid)==0 or len(password)==0):
            raise Exception()
        else:
            #code to check in database
            hospital_model=hospital.objects.get(hid=hid)
            if(checkAccount.check(hospital_model,hid,password)):
                request.session['hid']=hid
                return HttpResponse('True')
            else:
                raise Exception()
    except:
        return HttpResponse('False')
    # return redirect('/hospital/home')

def logout(request):
    hid=request.session.get('hid',False)
    if(hid):
        del request.session['hid']
    return redirect('/')


def login(request):
    hid=request.session.get('hid',False)
    if(hid):
        return redirect('/hospital/home')
    else:
        return redirect('/hospitallogin')


def doctorPage(request,doctorID):
    hid=request.session.get('hid',False)
    if(hid):
        try:
            doctor_object=Doctor.objects.get(did=doctorID)
            context={"Doctor":doctor_object}
            return render(request,'HospitalDashboard/doctorPage.html')
        except:
            return HttpResponse("The page you are looking for doesn't exist")
    else:
        return HttpResponse("The page you are looking for doesn't exist")


def patientPage(request,patientID):
    hid=request.session.get('hid',False)
    if(hid):
        try:
            patient_object=Patient.objects.get(pid=patientID)
            context={"Patient":patient_object}
            return render(request,'HospitalDashboard/patientsPage.html')
        except:
            return HttpResponse("The page you are looking for doesn't exist")
    else:
        return HttpResponse("The page you are looking for doesn't exist")




def complaints(request):
    hid=request.session.get('hid',False)
    if(hid):
        print(len(complaint.getComplaints(hid)))
        complaints={"complaints":complaint.getComplaints(hid),"complaint_length":len(complaint.getComplaints(hid))}
        return render(request,'HospitalDashboard/complaints.html',complaints)
    else:
        return redirect('/hospitallogin')



def ignore(request,value):
    hid=request.session['hid']
    token=value.strip()
    Hospital=hospital.objects.get(hid=hid)
    complaints=Hospital.complaint_on_doctors
    Hospital.complaint_on_doctors=removeComplaint.remove(token,complaints)
    Hospital.save()
    return redirect('/hospital/complaints')


def takeaction(request,value):
    hid=request.session.get('hid',False)
    try:
        if(hid):
            print(value)
            ct=complaint_token.getToken(hid,value)
            return HttpResponse(json.dumps({"did":ct['did'],"token":ct['token']}))
        else:
            raise Exception()
    except:
        return HttpResponse("false")


def sendNotification(request):
    hid=request.session.get('hid',False)
    # print(request.POST)
    try:
        if(hid):
            did=request.POST['did']
            token=request.POST['token']
            ct=complaint_token.getToken(hid,token)
            action_message=request.POST['action-text'].strip()
            send_email_doctor.send(did,action_message,ct['pid'].strip().upper())
            complaint_token.removeToken(hid,token,did)
        else:
            raise Exception()
    except:
        return HttpResponse("ERROR")
    return redirect('/hospital/complaints')