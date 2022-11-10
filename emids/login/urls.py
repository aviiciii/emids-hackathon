from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),    
    path("patient", views.patient_login, name="patient_login"),
    path("doctor", views.doctor_login, name="doctor_login"),
]