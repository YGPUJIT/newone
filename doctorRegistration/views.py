from django.shortcuts import render,HttpResponse,redirect
from .Logic import doctorId,sendMail,url_generate,doctorFields
from .Logic.json import specialist
from .models import Doctor,doctorNotConfirm
from HospitalDashboard.models import hospital
# Create your views here.


def registration(request):
    hid=request.session.get('hid',False)
    if(hid):
        context={"specilisation":specialist.getSecialists()}
        return render(request,'doctorRegistration/doctorRegistration.html',context)
    else:
        return redirect('/hospitallogin')



def registrationValidation(request):
    hid=request.session.get('hid',False)
    if(hid):
        # try:
        doctor=Doctor()
        doctorNot=doctorNotConfirm()
        did=doctorId.generate()
        Hospital=hospital.objects.get(hid=hid)
        name=request.POST['name']
        email=request.POST['email']
        specialisation=request.POST['specilisation'].lower()
        hashValue=str(abs(hash(str(did)+str(email))))
        url=url_generate.generate(hashValue,hid)
        doctorFields.saveData(did,name,email,specialisation,hashValue,hid,doctor,doctorNot)
        Hospital.doctors.append({"did":did})
        doctor_notification="A new doctor, Dr. "+name.upper()+", with specialisation "+specialisation.upper()+" has registered to your hospital."
        Hospital.notifications.insert(0,{"notification":doctor_notification})
        Hospital.save()
        sendMail.send(email,name,did,url)
        return redirect('/doctor/registrationConfirmation')
        # except:
        #     return HttpResponse("Please try again later, something went wrong")
    else:
        return redirect('/hospitallogin')



def confirmation(request):
    hid=request.session.get('hid',False)
    if(hid):
        return render(request,'doctorRegistration/doctorRegistrationComplete.html')
    else:
        return redirect('/hospitallogin')


def finalConfirm(request,hashCode):
    try:
        doctorId=doctorNotConfirm.objects.get(hashValue=hashCode)
        doctor=Doctor.objects.get(did=doctorId.did)
        context={"email":doctor.email,"name":doctor.name}
        request.session['doctorID_temp']=hashCode
        request.session['doctor_hospital']=doctor.hospital_id
        return render(request,'doctorRegistration/doctorRegistrationFinal.html',context)
    except:
        return HttpResponse("The page you are looking for doesn't exist anymore.")


def finalConfirmPasswordChange(request):
    hashValue=request.session.get('doctorID_temp',False)
    hid=request.session.get('doctor_hospital',False)
    if(hashValue and hid):
        try:
            password=request.POST.get('password',False)
            doctorId=doctorNotConfirm.objects.get(hashValue=hashValue)
            Hospital=hospital.objects.get(hid=hid)
            doctor=Doctor.objects.get(did=doctorId.did)
            doctor.password=password
            doctor.registrationConfirmed=True
            doctor.save()
            doctorId.delete()
            notification="Dr. "+doctor.name.upper()+" with id "+doctor.did+", has sucessfully confirmed the account."
            Hospital.notifications.insert(0,{"notification":notification})
            Hospital.save()
            del request.session['doctorID_temp']
            del request.session['doctor_hospital']
            return redirect("localhost:8000/management")
        except:
            return HttpResponse("Something went wrong, Please try again later")
    else:
        return HttpResponse("The page does not exist")

