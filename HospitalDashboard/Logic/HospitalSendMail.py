import smtplib
from email.message import EmailMessage
from datetime import date,datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendMail(emailid,id):
    print("MAIL HOSPITAL IN")
    email=MIMEMultipart('alternative')
    email['Subject']='HOSPITAL ID '+str(date.today().strftime("%d/%m/%Y"))
    email['From']='doctorgeek1947@gmail.com'
    email['To']=emailid
    mail_string='<h1>Hello, There thanks for registering with us</h1><p>Your ID is:</p>'+str(id)
    mail_string=MIMEText(mail_string,'html')
    email.attach(mail_string)
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('doctorgeek1947@gmail.com','Dancebar123')
    server.send_message(email)