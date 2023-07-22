from django.shortcuts import render,HttpResponse,redirect
import os
from .Logic.ChatBot import cli
from autocorrect import Speller
# Create your views here.


def index(request):
    images=[]
    if('pid' in request.session):
        del request.session['pid']
    if('did' in request.session):
        del request.session['did']
    if('hid' in request.session):
        del request.session['hid']
    if('sid' in request.session):
        del request.session['sid']
    for i in range(5):
        images.append('static/Landing/images/'+str(i)+'.png')
    return render(request,'Landing/index.html',{'images':images})


def patientLoginPage(request):
    pid=request.session.get('pid',False)
    if(pid):
        return redirect('/home')
    else:
        return render(request,'Landing/patientLoginPage.html')


def hospitalLoginPage(request):
    hid=request.session.get('hid',False)
    if(hid):
        return redirect('/hospital/home')
    else:
        return render(request,'Landing/hospitalLogin.html')


def doctorLoginPage(request):
    did=request.session.get('did',False)
    if(did):
        return redirect('/doctorhome')
    else:
        return render(request,'Landing/doctorlogin.html')

def management(request):
    return render(request,'Landing/managementPage.html')


def chatbot(request):
    spell = Speller(lang='en')
    request_msg=spell(str(request.POST.get('q',"okok")))
    res=cli.chatResponse(request_msg)
    res=res.replace("\n",'<br>')
    return HttpResponse(res)