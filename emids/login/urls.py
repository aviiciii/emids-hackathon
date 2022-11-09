from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),    
    path("patient_login", views.patient_login, name="patient_login"),
    path("doctor_login", views.doctor_login, name="doctor_login"),
]