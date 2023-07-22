from django.urls import path,include
from . import views


urlpatterns=[
    path('',views.home),
    path('login',views.login),
    path('loginValidate',views.loginValidate),
    path('logout',views.logout),
    path('initiate/<str:patientid>',views.initiateTreatment),
    path('patientprofile/<str:patientid>',views.patientprofile),
    path('suggestion/<str:patientId>',views.suggestion),
    path('patientprofile/<str:patientid>/medicine',views.medicine)
]