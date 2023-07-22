from django.urls import path
from . import views


urlpatterns=[
    path('',views.index),
    path('loginpage',views.loginPage),
    path('loginValidate',views.loginValidate),
    path('video',views.Video),
    path('toggle',views.toggle),
    path('stop',views.stop),
    path('offender',views.getOffender),
    path('removeOffender',views.removeOffender),
    path('getInformation',views.getInformation),
    path('sendAlert',views.protocolBreached)
]