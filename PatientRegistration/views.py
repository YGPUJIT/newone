from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .Logic import randomId,longitude_latitude
from django.views.decorators.cache import never_cache,cache_control
from .models import Patient

# Create your views here.

@cache_control(max_age=0, no_cache=True, no_store=True)
def registration(request):
    print('IN')
    pid=request.session.get('id',False)
    if(pid):
        del request.session['id']
    context={
    "first_last_name":"*Please input your first name, last name, Age, Sex as per your aadhar card/PAN card or any Governement ID.",
    'location':"*NOTE: You will assigned to the hospital based on the current location",
    'picture':'*Please provide four recent picture of yours.',
    }
    return render(request,'PatientRegistration/index.html',context)



@cache_control(max_age=0, no_cache=True, no_store=True)
def registrationdata(request):
    pid=request.session.get('pid',False)
    if(not pid):
        patient=Patient()
        city=request.POST['city']
        pcode=request.POST['pcode']
        area=request.POST['area']
        password=request.POST['password']
        email=request.POST['email'].strip()
        lon_lat=longitude_latitude.get_lon_lat(city=city,pincode=pcode,area=area)
        patient.first_name=request.POST['fname'].upper().strip()
        patient.last_name=request.POST['lname'].upper().strip()
        patient.password=password
        patient.email=email
        patient.age=request.POST['age']
        patient.sex=request.POST['sex']
        patient.location={
            'city':city,
            'pincode':pcode,
            'area':area,
            'longitude':lon_lat['longitude'],
            'latitude':lon_lat['latitude'],
            'country':'India'
        }
        random_id=randomId.generateRandomId()
        patient.pid=random_id
        try:
            patient.save()
            request.session['pid']=random_id
        except:
            return HttpResponse("Error while creating profile please try again later")
    return redirect('/home')


