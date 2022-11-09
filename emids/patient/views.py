from django.shortcuts import render, redirect
from db import models

# Create your views here.
def dashboard(request):
    # get the user
    username = request.user.get_username()
    # get the patient
    patient = models.Patient.objects.get(id=username)

    # get all the appointments
    appointments = models.Appointment.objects.filter(patient=patient).all()
    
    context={
        'patient':patient,
        'appointments':appointments,

    }

    return render(request, 'patient/dashboard.html', context)

def appointments(request, appointment_id):
    # get the user
    username = request.user.get_username()
    # get the patient
    patient = models.Patient.objects.get(id=username)

    # get the appointment
    appointment = models.Appointment.objects.get(id=appointment_id)

    context={
        'patient':patient,
        'appointment':appointment,
    }

    return render(request, 'patient/appointment.html')

def patient_report(request):
    return render(request, 'patient/patient_report.html')