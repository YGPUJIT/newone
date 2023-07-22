from HospitalDashboard.models import hospital
from PatientRegistration.models import Patient
import urllib
import json
import random

def assign(pid):
    patient=Patient.objects.get(pid=pid)
    patient_city=patient.location['city']
    print(patient_city,"OKOKOK")
    Hospitals=hospital.objects.filter(location={"city":patient_city})
    try:
        print("assigning hospital")
        lon=patient.location['longitude']
        lat=patient.location['latitude']
        key="5b3ce3597851110001cf62480c1246a931d94b9bb624f6e16a44d5e3"
        start=lon+","+lat
        print(start)
        hospital_distance=[]
        for h in Hospitals:
            longitude=h.location['longitude']
            latitude=h.location['latitude']
            end=longitude+","+latitude
            print(end)
            url="https://api.openrouteservice.org/v2/directions/driving-car?api_key="+key+"&start="+start+"&end="+end
            value=urllib.request.urlopen(url)
            val=json.loads(value.read())
            distance=int(val['features'][0]['properties']['segments'][0]['distance'])/1000
            hospital_distance.append((h.hid,distance))
        return calculateMinimum(hospital_distance)
    except:
        print("ERROR. SO RANDOM HOSPITAL ASSIGNED")
        return random.choice(Hospitals).hid


def calculateMinimum(arr):
    minV=999
    hospitalId=None
    for a in arr:
        if(minV>a[1]):
            minV=a[1]
            hospitalId=a[0]
    return hospitalId