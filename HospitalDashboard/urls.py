from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home),
    path('loginValidate',views.loginValidate),
    path('logout',views.logout),
    path('registration/storeData',views.storeData),
    path('registration',views.registration),
    path('login',views.login),
    path('complaints/sendNotification',views.sendNotification),
    path('complaints/ignore/<str:value>',views.ignore),
    path('complaints/takeaction/<str:value>',views.takeaction),
    path('complaints',views.complaints),
    path('dashboard',views.dashboard),
    path('doctorspage/<str:doctorID>',views.doctorPage),
    path('patientspage/<str:patientID>',views.patientPage)
]