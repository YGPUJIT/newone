from djongo import models
 
# Create your models here.


class Patient(models.Model):
    pid=models.CharField(max_length=50)
    
    class Meta:
        abstract=True



class Doctor(models.Model):
    did=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    hospital_id=models.CharField(max_length=50,default=None)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50,default=None)
    specilisation=models.CharField(max_length=100)
    patients=models.ArrayField(model_container=Patient,default=list)
    registrationConfirmed=models.BooleanField(default=False)



class doctorNotConfirm(models.Model):
    did=models.CharField(max_length=15)
    hashValue=models.CharField(max_length=200)