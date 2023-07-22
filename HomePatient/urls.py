from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('logout',views.logout),
    path('login',views.login),
    path('loginvalidate',views.loginValidate),
    path('storeData',views.storeData),
    path('storeImage',views.storeImage),
    path('complaint',views.complaint),
    path('complaint/<str:doctorid>',views.registerComplaint),
    path('allocateDoctor',views.allocateDoctor),
    path('downloadPharma',views.downloadPharma)
]