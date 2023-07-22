from django.urls import path
from . import views


urlpatterns=[
    path('',views.index),
    path('management',views.management),
    path('patientlogin',views.patientLoginPage),
    path('hospitallogin',views.hospitalLoginPage),
    path('doctorlogin',views.doctorLoginPage),
    path('chatBot',views.chatbot)
]