from django.urls import path
from . import views


urlpatterns=[
    path('registration',views.registration),
    path('registrationValidation',views.registrationValidation),
    path('registrationConfirmation',views.confirmation),
    path('registrationConfirmation/<str:hashCode>',views.finalConfirm),
    path('finalConfirmPasswordChange',views.finalConfirmPasswordChange)
]