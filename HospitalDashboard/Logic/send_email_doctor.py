import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from doctorRegistration.models import Doctor
from PatientRegistration.models import Patient


def send(did,message,pid):
    doctor=Doctor.objects.get(did=did)
    patient=Patient.objects.get(pid=pid)
    email=MIMEMultipart()
    email['Subject']='Complaint'
    email['from']='doctorgeek1947@gmail.com'
    email['to']=doctor.email

    string="Hello Dr. "+doctor.name.capitalize()+",\n\nThis is an Email regarding complaint from "+patient.first_name.capitalize()+" with ID: "+patient.pid+"\n\n"+message.capitalize()+"\n\nThank you."
    text=MIMEText(string,'plain')
    email.attach(text)

    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('doctorgeek1947@gmail.com','Dancebar123')
    server.send_message(email)
    print("Mail sent to doctor")