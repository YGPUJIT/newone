import smtplib
from email.message import EmailMessage
from datetime import date,datetime
from HospitalDashboard.models import hospital
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendMail(name,patient):
    print("MAIL INIININ")
    email=MIMEMultipart()
    email['Subject']='Test6 '+str(date.today().strftime("%d/%m/%Y"))
    email['From']='doctorgeek1947@gmail.com'
    print(str(name)+" was seen breaching protocol at "+datetime.now().strftime("%H:%M:%S"))
    # email['To']=hospital.objects.get(hid=patient.hospitalRegistered.upper().strip()).mailid
    email['To']=patient.email.strip()
    string=str(name)+" was seen breaching protocol at "+datetime.now().strftime("%H:%M:%S")
    string="Hello "+str(name.split('-')[1])+", you were seen breaching protocol at "+datetime.now().strftime("%H:%M:%S")+".Return to your Room immediately.\n Ignore if this isn't you.\n Thank you."
    text=MIMEText(string,'plain')
    email.attach(text)

    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('doctorgeek1947@gmail.com','Dancebar123')
    server.send_message(email)
    print("Sent"+str(name))