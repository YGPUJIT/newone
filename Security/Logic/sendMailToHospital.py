import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PatientRegistration.models import Patient



def sendMail(hospital,patientId,time):
    patient=Patient.objects.get(pid=patientId)
    email=MIMEMultipart()
    email['Subject']='Protocol Breached'
    email['from']='doctorgeek1947@gmail.com'
    email['to']=hospital.mailid
    string='A Patient named '+patient.first_name+' '+patient.last_name+' with ID '+patientId+' was seen breaching protocol at '+time
    text=MIMEText(string,'plain')
    email.attach(text)
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('doctorgeek1947@gmail.com','Dancebar123')
    server.send_message(email)
    print("Mail sent to Hospital")