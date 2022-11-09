from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('appointment/<str:appointment_id>', views.patient_profile, name='patient_profile'),
    path('patient_report/', views.patient_report, name='patient_report'),

]