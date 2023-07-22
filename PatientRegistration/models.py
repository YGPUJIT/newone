from djongo import models

# Create your models here.

class location(models.Model):
    area=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    country=models.CharField(max_length=100,default='India')
    longitude=models.CharField(max_length=100,default="Null")
    latitude=models.CharField(max_length=100,default='Null')

    class Meta:
        abstract = True

class Symptoms(models.Model):
    s1=models.CharField(max_length=100,default='Null')
    s2=models.CharField(max_length=100,default='Null')
    s3=models.CharField(max_length=100,default='Null')
    s4=models.CharField(max_length=100,default='Null')

    class Meta:
        abstract = True

class update(models.Model):
    notification=models.CharField(max_length=300,default='NONE')

    class Meta:
        abstract=True

class medicines(models.Model):
    medicine_name=models.CharField(max_length=100,default="none")
    medicine_directive=models.CharField(max_length=200,default='None')

    class Meta:
        abstract=True


class Patient(models.Model):
    pid=models.CharField(max_length=20,primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    age=models.IntegerField()
    sex=models.CharField(max_length=2,default='Null')
    password=models.CharField(max_length=30,default='None')
    email=models.EmailField(default='doctorgeek1947@gmail.com')
    hospitalRegistered=models.CharField(max_length=15,default='None')
    location=models.EmbeddedField(model_container=location)
    symptoms=models.EmbeddedField(model_container=Symptoms)
    symptoms_explanation=models.CharField(max_length=400,default="None")
    doctorAllocatedID=models.CharField(max_length=20,default='None')
    doctorAssigned=models.BooleanField(default=False)
    disease_actual=models.CharField(max_length=100,default="No Prediction")
    initiateTreatment=models.BooleanField(default=False)
    complaint_notification=models.CharField(max_length=100,default='No Complaint Registered')
    updates_from_doctors=models.ArrayField(model_container=update,default=list)
    regisitraionComplete=models.BooleanField(default=False)
    medicine_list=models.ArrayField(model_container=medicines,default=list)




