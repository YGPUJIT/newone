from djongo import models
from datetime import datetime

# Create your models here.

class Location(models.Model):
    area=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    country=models.CharField(max_length=100,default='India')
    longitude=models.CharField(max_length=100,default="Null")
    latitude=models.CharField(max_length=100,default='Null')

    class Meta:
        abstract = True


class Beds(models.Model):
    normal_beds=models.IntegerField()
    icu_beds=models.IntegerField()

    class Meta:
        abstract=True


class Patient(models.Model):
    pid=models.CharField(max_length=50)
    
    class Meta:
        abstract=True


class Doctors(models.Model):
    did=models.CharField(max_length=50)
    
    class Meta:
        abstract=True

class DoctorsComplaint(models.Model):
    token=models.CharField(max_length=100)
    did=models.CharField(max_length=50)
    complaint=models.CharField(max_length=300)
    pid=models.CharField(max_length=15)
    time=models.DateTimeField(default=datetime.now)

    class Meta:
        abstract=True


class Notification(models.Model):
    notification=models.CharField(max_length=300)
        
    class Meta:
        abstract=True

class Time(models.Model):
    time=models.CharField(max_length=300)

    class Meta:
        abstract=True

class protocol(models.Model):
    pid=models.CharField(max_length=300)
    date_time=models.ArrayField(model_container=Time,default=list)

    class Meta:
        abstract=True

class hospital(models.Model):
    hid=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20,default='null')
    hospital_name=models.CharField(max_length=40)
    location=models.EmbeddedField(model_container=Location)
    mailid=models.EmailField(default=None)
    beds=models.EmbeddedField(model_container=Beds)
    security=models.CharField(max_length=20)
    notifications=models.ArrayField(model_container=Notification,default=list)
    doctors=models.ArrayField(model_container=Doctors,default=list)
    patient=models.ArrayField(model_container=Patient,default=list)
    complaint_on_doctors=models.ArrayField(model_container=DoctorsComplaint,default=list)
    protocol_breached=models.ArrayField(model_container=protocol,default=list)
 